---
title: "11.7.5 从文件读取外部势"
---

## 11.7.5 从文件读取外部势

（2026 年 7 月 4 日）

用户可以在密度泛函理论（Density Functional Theory, DFT）计算中引入一个影响活性分子的外部势，以表征嵌入环境（embedding environment）。任何泛函均可使用。若要调用外部势的读取功能，用户必须在 `$rem` 区段中将关键字 **PROJ_CAP = -10** 进行设置，并且同名目录（即同一目录）下必须存在名为 **external_potential.grid** 的文件。该外部势必须在完全相同的网格点上给出。势文件仅包含以*原子坐标*表示的势值。作为准备工作，可以通过设置标志 **use_libqints = true**，使用 libqints 打印网格点。相关已发表的工作参见[[232]](../bib_references/bib.md#bib-232)。
