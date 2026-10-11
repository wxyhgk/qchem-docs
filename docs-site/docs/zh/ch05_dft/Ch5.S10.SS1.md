---
title: "5.10.1 引言"
---

## 5.10.1 引言

（2026 年 7 月 4 日）

没有任何 GGA 交换泛函能够同时在分子体系的渐近区域（asymptotic region）给出交换能量密度和交换势的正确贡献，[[1386]](../bib_references/bib.md#bib1445)
 而且现有的 GGA 交换-相关（exchange-correlation, XC）势在渐近区域的衰减速度远快于正确的 $-1/r$ XC 势。[[214]](../bib_references/bib.md#bib211)
 因此，高能占据轨道和低能虚轨道的结合过于松散，$-\varepsilon_{\rm HOMO}$ 也远小于电离能，
尽管对于精确泛函而言，二者相等本是一条严格成立的条件。[[1385]](../bib_references/bib.md#bib1444)
 此外，使用 GGA 泛函进行含时密度泛函理论（TDDFT）计算时，响应性质的预测结果也可能很不理想。[[1385]](../bib_references/bib.md#bib1444)
 第 [5.6](sect_LRC-DFT.md) 节所介绍的长程校正杂化密度泛函理论（Long-Range Corrected hybrid DFT, LRC-DFT）在很大程度上改善了这一状况，
但由于引入了哈特里-福克（Hartree-Fock）交换，其计算代价高于采用 GGA 泛函的 Kohn-Sham DFT（KS-DFT）。本节所介绍的渐近修正方法旨在解决同样的问题，但完全在 GGA 框架内进行。

---

已同步写入：
- `docs-site/docs/zh/ch05_dft/Ch5.S10.SS1.md`（中文版站点文件）

说明：原文中的 "Hatree-Fock" 为手册笔误，译文按正确的 Hartree-Fock 处理；链接路径与公式均保持原样。
