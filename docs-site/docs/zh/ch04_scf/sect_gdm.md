---
title: "4.5.7 几何直接极小化 (GDM)"
---

## 4.5.7 几何直接极小化（Geometric Direct Minimization, GDM）

(July 4, 2026)

gdm

几何直接极小化（GDM）是一种极其稳健的自洽场（SCF）收敛算法，其效率仅略低于直接迭代子空间方法（DIIS）。GDM 算法在轨道旋转空间中走出迭代步，并且正确地考虑了允许的 SCF 解流形（manifold）所具有的双球面（hyperspherical）几何结构。换句话说，轨道旋转所描述的空间是像高维球面一样弯曲的。正如飞机的最优航线不是直线而是大圆，轨道旋转空间中的最优步长同样如此。GDM 正确地考虑了这一点，这正是其高效性与稳健性的根源。完整细节请参见文献 [[1391]](../bib_references/bib.md#bib1453) 。对于使用 DIIS 时出现收敛困难的 SCF 计算，GDM 是 DIIS 的一个良好替代方案。GDM 算法已被推广到限制开壳层（restricted open-shell）SCF 计算，结果表明与早期的直接极小化方法相比，它的效率要高得多。

第 [4.5.3](sect_diis.md) 节讨论了这样一个事实：在迭代早期，DIIS 能够高效地朝全局 SCF 极小值前进。即使 DIIS 在后续迭代中无法收敛，这一点仍然成立。因此，程序实现了一种混合方案：先用 DIIS 极小化过程收敛到某个中间截止阈值，随后再改用几何直接极小化算法。该方案相当出色地结合了两种方法的优势：DIIS 能够从可能远离全局极小值的初始猜测中恢复，而 GDM 则能够稳健地收敛到局部极小值，即使局域曲面拓扑对 DIIS 而言颇具挑战性。这是调用 GDM 的推荐做法（*即*，设置 SCF_ALGORITHM = DIIS_GDM）。该混合过程同样兼容 SAD 猜测，而 GDM 本身则不兼容，因为它需要一组初始猜测轨道。如果希望在启用 GDM 之前尽可能少地扰动初始猜测，还应额外指定 MAX_DIIS_CYCLES = 1，从而只执行一次 Roothaan 步（这一步同时也会给出正确正交化后的轨道集合）。

与 GDM 相关的 *$rem* 选项包括 SCF_ALGORITHM（应设置为 GDM 或 DIIS_GDM），以及以下选项：

### `MAX_DIIS_CYCLES`

> **当 SCF_ALGORITHM 为 DIIS_GDM 或 DIIS_DM 时，在切换到（几何）直接极小化之前所允许的最大 DIIS 迭代次数。另见 THRESH_DIIS_SWITCH 。**
>
> * **类型**：`INTEGER`
> * **默认值**：`50`
> * **可选值**：
>     * 1
>     * 在切换到 (G)DM 之前只执行一次 Roothaan 步
>     * $n$
>     * $n$
>     * 在切换到 (G)DM 之前的 DIIS 迭代次数。
> * **建议**：无

### `THRESH_DIIS_SWITCH`

> **当 SCF_ALGORITHM 为 DIIS_GDM 或 DIIS_DM 时，在 DIIS 外推与 SCF 能量直接极小化之间进行切换的阈值为 $10^{-\mbox{{\small THRESH\_DIIS\_SWITCH}}}$ 。另见 MAX_DIIS_CYCLES 。**
>
> * **类型**：`INTEGER`
> * **默认值**：`2`
> * **可选值**：
>     * 由用户自定义。
> * **建议**：无

???+ example "示例 4.12: 苯基自由基（phenyl radical）在使用 DIIS 完成初始迭代后，采用几何直接极小化（GDM）进行非限制 Hartree-Fock（UHF）计算的输入。"
    ```qchem
    $molecule
       0   2
       c1
       x1  c1  1.0
       c2  c1  rc2  x1  90.0
       x2  c2  1.0  c1  90.0  x1    0.0
       c3  c1  rc3  x1  90.0  c2    tc3
       c4  c1  rc3  x1  90.0  c2   -tc3
       c5  c3  rc5  c1   ac5  x1  -90.0
       c6  c4  rc5  c1   ac5  x1   90.0
       h1  c2  rh1  x2  90.0  c1  180.0
       h2  c3  rh2  c1   ah2  x1   90.0
       h3  c4  rh2  c1   ah2  x1  -90.0
       h4  c5  rh4  c3   ah4  c1  180.0
       h5  c6  rh4  c4   ah4  c1  180.0
    
       rc2 =   2.672986
       rc3 =   1.354498
       tc3 =  62.851505
       rc5 =   1.372904
       ac5 = 116.454370
       rh1 =   1.085735
       rh2 =   1.085342
       ah2 = 122.157328
       rh4 =   1.087216
       ah4 = 119.523496
    $end
    
    $rem
       BASIS           = 6-31G*
       METHOD          = hf
       SCF_ALGORITHM   = diis_gdm
       SCF_CONVERGENCE = 7
       THRESH          = 10
    $end
    ```
