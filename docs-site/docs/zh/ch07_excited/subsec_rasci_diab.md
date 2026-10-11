---
title: "7.11.6 RAS-CI 本征态的非绝热化（Diabatization）"
---

## 7.11.6 RAS-CI 本征态的非绝热化（Diabatization）

（2026 年 7 月 4 日）

RAS-CI 电子态的表征也可以通过对 RAS-CI 哈密顿量的多个本征态进行非绝热化（diabatization）来完成。
遵循 Boys[[1323]](../bib_references/bib.md#bib1379)、

Edmiston-Ruedenberg[[1319]](../bib_references/bib.md#bib1380)
 或偶极-四极（dipole-quadrupole, DQ）定域化方案，可以得到非绝热态（diabatic states）。[[598]](../bib_references/bib.md#bib621)

详情参见第 [10.15.1.3](../ch10_properties/Ch10.S15.SS1.md#subsec:diabatic) 节。
要在 RAS-CI 方法中激活激发态的非绝热化分析，需要定义一个 section block（参见 *$localized_diabatization* 关键字），用以指定纳入非绝热化的激发态列表（按升序排列）。这与用于 CIS/TDDFT 态非绝热化的设置等价。
