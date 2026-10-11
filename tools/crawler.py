#!/usr/bin/env python3
"""
Crawler for Q-Chem 7.0 User's Manual
URL: https://manual.q-chem.com/latest/index.html

Crawls:
- All HTML manual pages (~758 pages)
- All images (.png, .svg, .jpg, .gif)
- PDF manual (qchem_manual.pdf)
"""

import os
import re
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

BASE_URL = "https://manual.q-chem.com/latest/"
CRAWL_DIR = Path(__file__).resolve().parent.parent / "crawl"
HTML_DIR = CRAWL_DIR / "html"
ASSETS_DIR = CRAWL_DIR / "assets"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def setup_dirs():
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

def download_file(session, url, target_path, skip_existing=True):
    if skip_existing and target_path.exists() and target_path.stat().st_size > 0:
        return True, "skipped"

    for attempt in range(1, 4):
        try:
            resp = session.get(url, headers=HEADERS, timeout=20)
            if resp.status_code == 200:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with open(target_path, "wb") as f:
                    f.write(resp.content)
                return True, "downloaded"
            elif resp.status_code == 404:
                return False, f"404 Not Found"
            else:
                time.sleep(1)
        except Exception as e:
            if attempt == 3:
                return False, str(e)
            time.sleep(1.5)
    return False, "failed after 3 retries"

def extract_links_and_assets(html_content, page_url):
    html_links = set()
    asset_links = set()

    # Match href and src
    hrefs = re.findall(r'href=[\"\']([^\"\'#\s]+)[\"\']', html_content)
    srcs = re.findall(r'src=[\"\']([^\"\'#\s]+)[\"\']', html_content)

    for ref in hrefs + srcs:
        if ref.startswith("data:") or ref.startswith("mailto:") or ref.startswith("javascript:"):
            continue
        full_url = urllib.parse.urljoin(page_url, ref)
        if not full_url.startswith(BASE_URL):
            continue

        rel_path = full_url[len(BASE_URL):]
        if rel_path.endswith(".html") or rel_path == "" or rel_path == "index.html":
            html_links.add(full_url)
        elif any(rel_path.lower().endswith(ext) for ext in [".png", ".svg", ".jpg", ".jpeg", ".gif", ".pdf", ".css"]):
            asset_links.add(full_url)

    return html_links, asset_links

def crawl_site(max_workers=8):
    setup_dirs()
    session = requests.Session()

    index_url = urllib.parse.urljoin(BASE_URL, "index.html")
    print(f"[*] Fetching root index: {index_url}")
    index_file = HTML_DIR / "index.html"
    success, status = download_file(session, index_url, index_file, skip_existing=False)
    if not success:
        print(f"[!] Error fetching index: {status}")
        return

    with open(index_file, "r", encoding="utf-8", errors="ignore") as f:
        root_html = f.read()

    discovered_html, discovered_assets = extract_links_and_assets(root_html, index_url)
    to_visit_html = set(discovered_html)
    visited_html = {index_url}
    all_assets = set(discovered_assets)

    print(f"[*] Discovered {len(to_visit_html)} HTML pages and {len(all_assets)} assets from index.")

    # Phase 1: Download all HTML pages in parallel
    print(f"[*] Downloading HTML pages with {max_workers} threads...")
    completed_count = 0
    failed_pages = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for url in to_visit_html:
            rel_name = url[len(BASE_URL):]
            if not rel_name:
                rel_name = "index.html"
            target_path = HTML_DIR / rel_name
            f = executor.submit(download_file, session, url, target_path)
            futures[f] = (url, target_path)

        for future in as_completed(futures):
            url, target_path = futures[future]
            success, msg = future.result()
            completed_count += 1
            if success:
                # Read page to check for any assets
                try:
                    with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    _, assets = extract_links_and_assets(content, url)
                    all_assets.update(assets)
                except Exception:
                    pass
            else:
                failed_pages.append((url, msg))
                print(f"\n[!] Failed: {url} -> {msg}")

            if completed_count % 50 == 0 or completed_count == len(to_visit_html):
                print(f"    Progress: {completed_count}/{len(to_visit_html)} pages ({completed_count * 100 // len(to_visit_html)}%)")

    print(f"[+] Finished HTML crawl. Total pages: {completed_count}, Failed: {len(failed_pages)}")

    # Phase 2: Download assets (images, PDF, etc.)
    print(f"[*] Downloading {len(all_assets)} assets...")
    asset_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for url in all_assets:
            rel_name = url[len(BASE_URL):]
            target_path = ASSETS_DIR / rel_name
            f = executor.submit(download_file, session, url, target_path)
            futures[f] = (url, target_path)

        for future in as_completed(futures):
            url, target_path = futures[future]
            success, msg = future.result()
            asset_count += 1
            if not success:
                print(f"[!] Asset failed: {url} -> {msg}")

    print(f"[+] All assets downloaded ({asset_count} items).")
    print(f"[✓] Crawl complete! Raw data stored in {CRAWL_DIR}")

if __name__ == "__main__":
    workers = 8
    if len(sys.argv) > 1:
        workers = int(sys.argv[1])
    crawl_site(max_workers=workers)
