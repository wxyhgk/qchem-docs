---
title: "8.10.7 含 ECP 的力与振动频率"
---

## 8.10.7 含 ECP 的力与振动频率

(July 4, 2026)

能够使用赝势（pseudopotentials）进行几何优化非常重要，为此 **Q-Chem** 提供了 ECP 核势能项的解析一阶导数（analytical first derivatives）。

ECP 程序包还与振动分析程序包实现了集成，因此可以计算部分原子带有 ECP 的体系的振动频率（进而得到红外光谱和拉曼光谱）。从 **Q-Chem** 5.0 版本开始，ECP 的完全解析二阶导数也已可用。

???+ example "示例 8.12: 使用 Hartree-Fock 方法计算 TeO ${}_{2}$ 的结构与振动频率"
    ```qchem
    $rem
    $end

    $molecule
    $end
    ```
