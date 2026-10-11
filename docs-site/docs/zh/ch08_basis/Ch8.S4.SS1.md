---
title: "8.4.1 引言"
---

## 8.4.1 引言

(July 4, 2026)

用户有时可能希望使用非标准基组（Basis Set），并且可以在 **Q-Chem** 输入中声明用户自定义基组（参见关于 **Q-Chem** 输入的[第 3 章](../ch03_inputs/chap_inputs.md)）。插入非标准用户自定义基组的格式既合乎逻辑又灵活，其详细信息见下文的任务控制（job control）部分。

请注意，目前 SAD 初始猜测（guess）不支持非标准或用户自定义基组。当前的默认设置是使用 SCF_GUESS = AUTOSAD，除非指定了混合基组（mixed basis）。使用混合基组时，最简单的替代方案是为 SCF_GUESS 指定 GWH 或 CORE 选项，但这些选项的效果相对有限。
