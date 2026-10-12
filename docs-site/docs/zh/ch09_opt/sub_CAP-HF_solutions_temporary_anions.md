---
title: "9.11.2 寻找临时阴离子的电子共振态"
---

## 9.11.2 寻找临时阴离子的电子共振态

(July 4, 2026)

此处的讨论仅限于 HF 方法，但所概述的一般原理同样适用于更高级别的方法。

1. 要正确描述临时阴离子的电子态，通常需要在基组（Basis Set）中加入额外的弥散函数。
因此请考虑在你的基组中包含足够的额外弥散函数。
2. 最好使用核哈密顿量（core Hamiltonian）作为 CAP-HF SCF 程序的初始猜测
（*即*，设置 SCF_GUESS = CORE）。
3. 对于 CAP 计算，**Q-Chem** 首先使用 **Q-Chem** 中的旧版 SCF 驱动求解 SCF 问题；
随后该解被用作计算中 CAP 部分的起点。
这一预处理 SCF 解通常会导致错误的 CAP-HF 解。你可以通过在 *$rem* 中设置
SKIP_OLD_SCFMAN = TRUE 来避免这一问题，
参见示例 [9.11.3](ex_CAP_HF_energy_decomp.md)。
4. 请确保 CAP 对所得 SCF 解的实部与虚部的贡献可以忽略不计。
你可以通过在 *$rem* 中设置 CS_SCF_FINAL_PRINT = 1 来要求对复能量做能量分解，
从而获得这些 CAP 贡献。
另一种做法是观察 CAP-HF 能量及其校正后的 CAP-HF 能量的虚部（与实部）有多接近；
虚部之比应接近 1。参见示例 [9.11.3](ex_CAP_HF_energy_decomp.md)。

对于 CAP-HF 计算，请设置 *$rem* 变量 CS_STRICT = TRUE，
以打印该解的正确性质（*例如*，Mulliken 电荷与多极矩）。
参见示例 [9.11.3](ex_CAP_HF_energy_decomp.md)。
