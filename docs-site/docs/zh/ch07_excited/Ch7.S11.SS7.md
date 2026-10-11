---
title: "7.11.7 带微扰外部单激发修正的自旋翻转 CAS（casman）"
---

## 7.11.7 带微扰外部单激发修正的自旋翻转 CAS（**casman**）

（2026 年 7 月 4 日）

**casman** 模块允许用户执行基于自旋翻转 CAS（spin-flip CAS）的计算，并通过微扰修正来考虑活性空间（active space）之外的空穴（hole）与粒子（particle）激发。
（若需对空穴与粒子激发做变分处理，请参阅 **librassf** 相关章节。）
该模块还允许限制自旋翻转（spin-flip）的最大数目，这对于无法执行最大自旋翻转数的大型过渡金属配合物非常有用。关于此方法的更多细节，请参阅 Mayhall 与 Head-Gordon 的出版物。[[926]](../bib_references/bib.md#bib926)
