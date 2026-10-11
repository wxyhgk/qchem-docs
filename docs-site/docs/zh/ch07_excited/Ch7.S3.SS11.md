---
title: "7.3.11 CIS-1D 与 TDDFT-1D"
---

## 7.3.11 CIS-1D 与 TDDFT-1D

（2026 年 7 月 4 日）

模拟非绝热动力学极具挑战性，尤其是在基态（S${}_{0}$）与第一激发态（S${}_{1}$）之间的锥形交叉区域。对于 S${}_{1}$/S${}_{0}$ 锥形交叉，常规的电子结构方法（如 HF/CIS 和 DFT/TDDFT——但其自旋翻转（spin-flip）变体除外）会给出错误的交叉接缝（crossing seam）维数。[[1548]](../bib_references/bib.md#bib1614)

TDDFT-1D 方法通过结合 DFT 与组态相互作用（Configuration Interaction, CI）来克服这一局限，从而实现 S${}_{0}$ 与 S${}_{1}$ 态之间的平滑交叉[[1351]](../bib_references/bib.md#bib1410)，同时保持与标准 TDDFT 计算相当的计算成本。

CIS-1D 与 TDDFT-1D 方法的核心思想是，对一个组态相互作用哈密顿量进行对角化，其基组包含参考态、所有单激发组态以及一个独特的双激发组态。CI 哈密顿量中的这个独特双激发组态（即 CIS-1D/TDDFT-1D 名称中的“1D”）决定了方法的类型：若从 Hartree–Fock 参考出发，则得到 CIS-1D 方法；若从 Kohn–Sham 参考出发，则得到 TDDFT-1D 方法。

该双激发组态由一对电子从最高占据分子轨道（HOMO，$h$）激发至最低未占据分子轨道（LUMO，$l$）而形成。为找到这一独特双激发组态，需对正则分子轨道进行旋转，使得双激发组态的能量（$E_{d}$）达到最小。[[56]](../bib_references/bib.md#bib38)

基于这些优化后的轨道，构造出如下的 CI 哈密顿量，

<a id="eq:configHamiltoninan_tddft1d"></a>

$$
\mathbf{H}=\begin{pmatrix}\epsilon_{0}&0&\left\langle\psi_{0}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\\
0&\left\langle\psi_{i}^{a}|H|\psi_{j}^{b}\right\rangle&\left\langle\psi_{i}^{a}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\\
\left\langle\psi_{0}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle&\left\langle\psi_{h\bar{h}}^{l\bar{l}}|H|\psi_{i}^{a}\right\rangle&\left\langle\psi_{h\bar{h}}^{l\bar{l}}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\end{pmatrix}\;, \tag{7.57}
$$

其基组由参考态、所有单替换行列式（$\text{\textbar}{\psi_{i}^{a}}\rangle$）以及一个独特的双替换行列式（$\text{\textbar}{\psi_{h\bar{h}}^{l\bar{l}}}\rangle$）构成。对 $\mathbf{H}$ 进行对角化即可得到 CIS-1D 或 TDDFT-1D 的激发态。在远离交叉点的几何构型下，采用 TDDFT-1D 计算的激发能精度通常与采用 Tamm–Dancoff 近似（TDA）的 TDDFT 处于同一水平。TDDFT-1D 的关键优势体现在基态与激发态交叉点附近，此时它能够给出平滑的势能面。

为便于非绝热动力学模拟，TDDFT-1D 方法已具备解析梯度和导数耦合[[1352]](../bib_references/bib.md#bib1411)。

这使得对电子态之间的最小能量交叉点（Minimum-Energy Crossing Point, MECP）进行几何优化成为可能。

## 7.3.11.1 TDDFT-1D 的任务控制

TDDFT-1D 计算的 *rem* 变量与 CIS 计算的类似，以下 *$rem* 变量用于控制 TDDFT-1D 计算。

CIS1D_N_ROOTS

### `CIS1D_N_ROOTS`

> **设置要计算的 CIS-1D 和 TDDFT-1D 态的数目。$\mathbf{H}$ 的最低本征态为基态，其后依次为激发态。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * $n>0$
>     * ，计算最低的
>     * $n$
>     * 个 CIS-1D 或 TDDFT-1D 态。
> * **建议**：无

CIS1D_ED_CONVERGENCE

### `CIS1D_ED_CONVERGENCE`

> **用于轨道优化的 $E_{d}$ 最小化收敛判据。停止准则设为 $10^{-\text{CIS1D\_ED\_CONVERGENCE}}$ 。**
>
> * **类型**：`INTEGER`
> * **默认值**：`7`
> * **选项**：
>     * $n$
>     * 当误差低于
>     * $10^{-n}$
>     * 时认为已收敛。
> * **建议**：$\mathbf{H}$ 本征根的收敛性由 CIS_CONVERGENCE 控制，对于 CIS-1D 或 TDDFT-1D 计算，其默认值为 9。若增大 CIS_CONVERGENCE，则本变量也应相应增大。

CIS1D_MAX_CYCLES

### `CIS1D_MAX_CYCLES`

> **对 $\mathbf{H}$ 进行对角化时 Davidson 迭代的最大次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`60`
> * **选项**：
>     * $n$
>     * 最多使用
>     * $n$
>     * 次迭代。
> * **建议**：为 Davidson 迭代（用于对角化 $\mathbf{H}$ ）分配的内存为 $(n_{\text{occ}}n_{\text{virt}}+\text{2})$ ( )( CIS1D_N_ROOTS )/2 个双精度数，其中 $n_{\text{occ}}$ 和 $n_{\text{virt}}$ 分别为占据轨道数和虚轨道数。较大的取值可能需要增大 MEM_TOTAL。

CIS1D_SCALE_GD

### `CIS1D_SCALE_GD`

> **参考态与双替换 Slater 行列式之间耦合矩阵元 $\langle\psi_{0}|\hat{H}|\psi_{h\bar{h}}^{l\bar{l}}\rangle$ 的缩放因子。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $n$
>     * $0\leq n\leq 100$
>     * ，耦合元按
>     * $n/100$
>     * 缩放。
> * **建议**：由于 Kohn-Sham 行列式并非真正的波函数，因此没有严格的方法来确定 $\mathbf{H}$ 中的耦合元，故采用“伪波函数”（pseudo-wave function）方法计算这些耦合。1028 Ou Q., Alguire E. C., Subotnik J. E. J. Phys. Chem. B (2015) , 119 , pp. 7150 . Link , 1548 Zhang X., Herbert J. M. J. Chem. Phys. (2015) , 142 , pp. 064109 . Link 有时为了获得准确的势能面，需要对耦合元进行缩放，而缩放因子需通过一定的基准测试来确定。56 Athavale V., Teh H.-H., Subotnik J. E. J. Chem. Phys. (2021) , 155 , pp. 154105 . Link

CIS1D_SCALE_SD

### `CIS1D_SCALE_SD`

> **单激发组态与唯一双激发组态之间耦合矩阵元 $\langle\psi_{i}^{a}|H|\psi_{h\bar{h}}^{l\bar{l}}\rangle$ 的缩放因子。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $n$
>     * $0\leq n\leq 100$
>     * ，耦合元按
>     * $n/100$
>     * 缩放。
> * **建议**：与 CIS1D_SCALE_GD 相同。

CIS1D_STATE_DERIV

### `CIS1D_STATE_DERIV`

> **选择要计算梯度的 CIS-1D/TDDFT-1D 态。这对于几何优化等任务非常有用。**
>
> * **类型**：`INTEGER`
> * **默认值**：`$-1$`
> * **选项**：
>     * $n$
>     * $n\geq 0$
>     * ，选择第
>     * $n$
>     * 个 CIS-1D/TDDFT-1D 态。
> * **建议**：无

CIS1D_DER_NUMSTATE

### `CIS1D_DER_NUMSTATE`

> **确定要计算导数耦合的态的数目。这些态在 $derivative_coupling 区块中指定。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不计算导数耦合。
>     * $n$
>     * 计算
>     * $n(n-1)/2$
>     * 对导数耦合。
> * **建议**：无

## 7.3.11.2 TDDFT-1D 示例

???+ example "示例 7.28: 使用 B3LYP 泛函对水分子最低的 5 个态进行 TDDFT-1D 计算。"
    ```qchem
    $molecule
    0 1
    H 0.96 0 0
    O 0.000000000000000 0.000000000000000 0.000000000000000
    H -0.240364803892264 0.929421734762983 0
    $end
    
    $rem
    METHOD    b3lyp
    BASIS     cc-pvdz
    SYM_IGNORE  true
    cis1d_n_roots 5
    $end
    ```

???+ example "示例 7.29: 在外加点电荷存在下，对水分子第一激发态的梯度进行 TDDFT-1D 计算"
    ```qchem
    $molecule
    0 1
    H 0.96 0 0
    O 0.000000000000000 0.000000000000000 0.000000000000000
    H -0.240364803892264 0.929421734762983 0
    $end
    
    $rem
    METHOD    b3lyp
    BASIS     cc-pvdz
    SYM_IGNORE  true
    cis1d_n_roots 4
    cis1d_state_deriv 1
    jobtype force
    $end
    
    $external_charges
    0.0 0.0 -1.0 -1.0
    0.0 0.0 1.2 1.0
    0.0 0.0 -2.0 -1.0
    0.0 0.0 2.2 1.0
    $end
    ```

???+ example "示例 7.30: 使用 $\omega$ B97X 泛函优化乙烯基态与第一激发态之间的 MECP。"
    ```qchem
    $rem
    geom_opt_driver optimize
    scf_convergence 10
    thresh_diis_switch 9
    cis_convergence 8
    jobtype opt
    mecp_opt      true
    mecp_methods  branching_plane
    MECP_PROJ_HESS true
    mecp_state1  [0,0]
    mecp_state2  [0,1]
    unrestricted false
    calc_nac 1
    scf_algorithm diis_gdm
    cis1d_n_roots 5
    exchange wb97x
    basis 6-31G*
    symmetry_ignore true
    $end
    
    $molecule
    0 1
    C         0.0188526101    0.0181382820   -0.3533168752
    C         1.3813178426    0.0038321438   -0.0594695222
    H         2.0062266305   -0.8967843506    0.0891927721
    H        -0.3788613100   -0.7769905091   -1.0012547284
    H        -0.0243170648   -0.6123230262    0.6288689086
    H         1.9213240937    0.9262667800    0.1943673040
    $end
    ```
