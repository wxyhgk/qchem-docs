---
title: "7.3.10 自旋-轨道耦合"
---

## 7.3.10 自旋-轨道耦合

（2026 年 7 月 4 日）

以下小节介绍在 TDDFT 计算中纳入自旋-轨道耦合（Spin-Orbit Coupling, SOC）的两种不同方式。

## 7.3.10.1 TDDFT 态之间的 SOC

将 SOC 纳入 TDDFT 计算可以有多个层次的近似方案：[[713]](../bib_references/bib.md#bib745)

1. (i)

Breit-Pauli 哈密顿量的一电子部分，
2. (ii)

使用缩放核电荷的一电子 SOC，以及
3. (iii)

通过对两电子部分采用平均场（mean-field）处理的完整 SOC。[[1103]](../bib_references/bib.md#bib1151)

方案 (i) 和 (ii)
对 TDA 与 RPA 两种变体均可用（包括 TDHF 和 CIS 态），但仅限于限制型 Kohn-Sham（restricted Kohn-Sham）参考。
方案 (iii) 对限制型和非限制型变体均可用，但仅限于 TDA 框架内。
在 TDA 框架内使用方案 (iii) 也可以计算 SF-TDDFT（包括标准 SF-TDDFT 和 MR-SFTDDFT）的 SOC。
目前有一个可用的 Python 程序，[[882]](../bib_references/bib.md#bib1655) 它从 **Q-Chem** 输出中提取 SOC 以及 TDDFT 能量和振子强度，
并利用它们构造和是对角化 Breit-Pauli 哈密顿量，从而得到耦合态。[[881]](../bib_references/bib.md#bib916)
该程序可用于计算 TDDFT、CIS 和 DFT/CIS 方法的 L 边与 M 边光谱。

一电子 SOC（方案 (i) 和 (ii)）的实现基于以下内容。
SOC 通过计算 Breit-Pauli 哈密顿量一电子部分的矩阵元来获得：

<a id="eq:HSO_Breit_Pauli"></a>

$$
\hat{H}_{\text{SO}}=-\frac{\alpha_{0}^{2}}{2}\sum_{i,A}\frac{Z_{A}}{r^{3}_{iA}}\left(\mathbf{r}_{iA}\times\mathbf{p}_{i}\right)\bm{\cdot}\mathbf{s}_{i} \tag{7.38}
$$

其中 $i$ 表示电子，$A$ 表示原子核，$\alpha_{0}=1/137.037$ 是
精细结构常数，$Z_{A}$ 是原子核 $A$ 上的裸正电荷。
在二次量子化表示下，不同方向的自旋-轨道哈密顿量可以表示为

<a id="Ch7.E39"></a>

$$
\displaystyle\hat{H}_{\text{SO},x} \tag{7.39a}
$$

其中对 $\alpha\in\{x,y,z\}$ 有 $\hat{\tilde{L}}_{\alpha}=\hat{L}_{\alpha}r^{-3}$，而
$\tilde{L}_{\alpha,pq}$ 是该算符的矩阵元。单参考 *ab initio*
激发态（在 TDA 框架内）由下式给出

<a id="Ch7.E40"></a>

$$
\displaystyle\big{|}\Phi^{I}_{\text{singlet}}\big{\rangle} \tag{7.40a}
$$

其中 $s^{Ia}_{i}$ 和 $t^{Ia}_{i}$ 分别是第 $I$ 个单重态或三重态的单重态与三重态激发系数，其归一化条件为

<a id="Ch7.E41"></a>

$$
\sum_{ia}(s^{Ia}_{i})^{2}=\sum_{ia}(t^{Ia}_{i})^{2}=\frac{1}{2}\;. \tag{7.41}
$$

量 $|\Phi_{\text{HF}}\rangle$ 指 Hartree-Fock 基态。因此，从单重态到不同三重态多重流形（manifold）的 SOC 常数为

<a id="Ch7.E42"></a>

$$
\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=0}_{\text{triplet}}\big{\rangle}=\frac{\alpha_{0}^{2}\hbar}{2}\left(\sum_{i,a,b}\tilde{L}_{z,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{z,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right) \tag{7.42}
$$

或者

<a id="A3.S8.EGx45"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}&\displaystyle=\mp\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}}\left(\sum_{i,a,b}\tilde{L}_{x,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{x,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right)\\
&\displaystyle\qquad\qquad+\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}\text{i}}\left(\sum_{i,a,b}\tilde{L}_{y,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{y,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right)\;.\end{aligned} \tag{7.43}
$$

不同三重态多重流形之间的 SOC 常数可由下式得到

<a id="A3.S8.EGx46"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{\langle}\Phi^{I,M_{s}=0}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}&\displaystyle=\mp\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}}\left(\sum_{i,a,b}\tilde{L}_{x,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{x,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\\
&\displaystyle\qquad\qquad\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}\text{i}}\left(\sum_{i,a,b}\tilde{L}_{y,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{y,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\end{aligned} \tag{7.44}
$$

或者

<a id="Ch7.E45"></a>

$$
\big{\langle}\Phi^{I,M_{s}=\pm 1}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}=\pm\frac{\alpha_{0}^{2}\hbar}{2}\left(\sum_{i,a,b}\tilde{L}_{z,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{z,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\;. \tag{7.45}
$$

注意有

<a id="Ch7.E46"></a>

$$
\big{\langle}\Phi^{I,M_{s}=0}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=0}_{\text{triplet}}\big{\rangle}=0=\big{\langle}\Phi^{I,M_{s}=\pm 1}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\mp 1}_{\text{triplet}}\big{\rangle}\;. \tag{7.46}
$$

总的（均方根，root-mean-square）自旋-轨道耦合为

<a id="eqn:soc_const"></a>

$$
\displaystyle\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J}_{\text{triplet}}\big{\rangle} \tag{7.47a}
$$

对于 RPA 态，只需将 $s^{Ia}_{i}\;t^{Jb}_{j}$ 替换为 $X^{Ia}_{i,\text{triplet}}X^{Jb}_{j,\text{triplet}}+Y^{Ia}_{i,\text{singlet}}Y^{Jb}_{j,\text{triplet}}$，
并将 $t^{Ia}_{i}\;t^{Jb}_{j}$ 替换为
$X^{Ia}_{i,\text{triplet}}X^{Jb}_{j,\text{triplet}}+Y^{Ia}_{i,\text{triplet}}Y^{Jb}_{j,\text{triplet}}$，即可简单地得到 RPA 态的 SOC 常数。

通过 *$rem* 变量 CALC_SOC 来启用 TDDFT + SOC 计算：

### `CALC_SOC`

> **控制是否为 EOM-CC、RAS-CI、CIS、TDDFT/TDA 和 TDDFT/RPA 计算 SOC 常数。**
>
> * **类型**: `INTEGER/LOGICAL`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不执行 SOC 计算。
>     * `1`: 使用 Breit-Pauli 哈密顿量的一电子部分执行 SOC 计算
>     * `2`: 对两电子贡献采用平均场处理，执行完整 SOC 计算
>     * `4`: 使用缩放核电荷执行 SOC 计算
> * **建议**: 最后两个选项在第 7.9.21.4 节中描述。

示例 [7.3.10.1](#ex:dftcis-soc)、[7.3.10.1](#ex:dftcis-soc) 和 [7.3.10.1](#ex:dftcis-soc)
演示了利用上述功能计算 (SF)-TDDFT 态 SOC 的过程。
通过适当修改 METHOD，这些计算同样可用于 CIS 态。

针对无自旋的单粒子跃迁密度矩阵（如文献 [[1105]](../bib_references/bib.md#bib1152)
所述）的 **libwfa** 分析已在 TDDFT 和 SF-TDDFT 计算中实现。
要启用该分析，请使用以下设置：CALC_SOC = 2、
STATE_ANALYSIS = TRUE、MOLDEN_FORMAT = TRUE
以及 NTO_PAIRS = $N$。有关 **libwfa** 包的详情，请参阅第 [10.2](../ch10_properties/sec_wfa.md) 节。

!!! note "注意"
    该分析与单重态和三重态之间常规跃迁密度矩阵的 NTO 分析不同。


???+ example "示例 7.21: 使用 TDDFT/TDA 计算一电子 SOC。"
    ```qchem
    $comment
       This sample input calculates the spin-orbit coupling constants for water
       between its ground state and its TDDFT/TDA excited triplets as well as the
       coupling between its TDDFT/TDA singlets and triplets.  Results are given in
       cm-1.
    $end
    
    $molecule
       0 1
       H       0.000000    -0.115747     1.133769
       H       0.000000     1.109931    -0.113383
       O       0.000000     0.005817    -0.020386
    $end
    
    $rem
       EXCHANGE             b3lyp
       BASIS                6-31G
       CIS_N_ROOTS          4
       CIS_CONVERGENCE      8
       MAX_SCF_CYCLES       600
       MAX_CIS_CYCLES       50
       SCF_ALGORITHM        diis
       MEM_STATIC           300
       MEM_TOTAL            2000
       CIS_SINGLETS         true
       CIS_TRIPLETS         true
       CALC_SOC             true
       MAX_CIS_CYCLES       300
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 7.22: 对水分子计算完整 SOC（包含对 Breit-Pauli 哈密顿量两电子部分的平均场处理）"
    以及 UHF/TDDFT/TDA。
    ```qchem
    $comment
    Calculation of full SOCs for water molecule inlcuding mean-field treatment
    of the two-electron part of the Breit-Pauli Hamiltonian and Wigner-Eckart theorem.
    UHF/TDDFT/B3LYP/6-31G within the TDA.
    $end
    
    $molecule
    0 1
    H       0.000000    -0.115747     1.133769
    H       0.000000     1.109931    -0.113383
    O       0.000000     0.005817    -0.020386
    $end
    
    $rem
    jobtype                 sp
    unrestricted            true
    method                  b3lyp
    basis                   6-31G
    cis_n_roots             4
    cis_convergence         8
    cis_singlets            true
    cis_triplets            true
    calc_soc                2
    $end
    ```

???+ example "示例 7.23: 使用非共线 SF-TDDFT/PBE0 计算亚甲基（methylene）的 SOC。"
    ```qchem
    $comment
    Calculation of SOCs for methylene using non-collinear SF-TDDFT/PBE0,
    with tight convergence.
    $end
    
    $molecule
    0 3
    H1
    C  H1 1.0775
    H2 C  1.0775 H1 133.29
    $end
    
    $rem
    method = pbe0
    basis = cc-pvtz
    scf_convergence = 12
    cis_convergence = 12
    thresh = 14
    cis_n_roots = 2
    calc_soc = 2                    Compute full SOC with mean-field treatment of 2el part
    wang_ziegler_kernel =  true     Important for 1,1 diradicals
    spin_flip = true
    $end
    ```

???+ example "示例 7.24: 对 H ${}_{2}$ S 中硫的 L ${}_{2,3}$ 边进行 DFT/CIS 计算。输入设置为计算 SOC 以及态-态跃迁矩，"
    可由 pySETSOC 程序（文献 882）读取，用于构造和是对角化 Breit-Pauli 哈密顿量。
    关于 DFT/CIS 方法的更多细节，请参见第 7.2.2.4 节。
    ```qchem
    $molecule
    0 1
    S
    H  1 1.343015
    H  1 1.343015 2 92.538291
    $end
    
    
    $rem
     method         cam-b3lyp
     unrestricted   false
     cis_n_roots    200
     calc_soc       2     ! spin-orbit mean-field
     sts_mom        true  ! state-to-state moments, for osc. strengths
     dftcis         1
     dftcis_params  2
     basis          def2-tzvpd
     trnss          true
     trtype         3     ! use alist
     n_sol          3
    $end
    
    $alist
    2 3 4 5
    $end
    ```

## 7.3.10.2 自旋绝热线（Spin-Adiabats）的 TDDFT+SOC

对于存在 SOC 的体系，计算整个（Coulomb + SOC）哈密顿量的电子本征函数（称为"自旋绝热线"，spin-adiabats）可能很有帮助。
此类自旋绝热态的计算已在 CIS 或 TDDFT/TDA 框架内实现，其中 SOC 在 post-SCF 层次上由一电子
Breit–Pauli 哈密顿量处理。

在 CIS 或 TDDFT/TDA-SOC 中，波函数表示为

<a id="A3.S8.EGx48"></a>

$$
\displaystyle\left|{\Psi}\right\rangle=\sum_{\epsilon}{\sum_{ia}{t_{ia}^{(\epsilon)}\left|{\Phi_{i}^{a(\epsilon)}}\right\rangle}} \tag{7.48}
$$

其中 $\epsilon$ 是自旋标签，且

<a id="A3.S8.EGx49"></a>

$$
\displaystyle\left|{\Phi_{i}^{a(\epsilon)}}\right\rangle\equiv\begin{cases}\frac{1}{\sqrt{2}}\left(|{\Psi_{i_{\alpha}}^{a_{\alpha}}}\rangle+|{\Psi_{i_{\beta}}^{a_{\beta}}}\rangle\right)&\text{if }\epsilon=\text{singlet}\\
\frac{1}{\sqrt{2}}\left(|{\Psi_{i_{\alpha}}^{a_{\alpha}}}\rangle-|{\Psi_{i_{\beta}}^{a_{\beta}}}\rangle\right)&\text{if }\epsilon=\text{triplet,}m_{s}=0\\
|{\Psi_{i_{\beta}}^{a_{\alpha}}}\rangle&\text{if }\epsilon=\text{triplet,}m_{s}=+1\\
|{\Psi_{i_{\alpha}}^{a_{\beta}}}\rangle&\text{if }\epsilon=\text{triplet,}m_{s}=-1\end{cases} \tag{7.49}
$$

式 ([7.48](#eq:spinadiabatdef)) 中的自旋绝热波函数可作为如下哈密顿量的本征态获得，该哈密顿量共有 $(4N_{O}N_{V})^{2}$ 个矩阵元：

<a id="A3.S8.EGx50"></a>

$$
\displaystyle H=A+V_{\text{SO}}+V_{m} \tag{7.50}
$$

在式 ([7.50](#eq:tda_soc)) 中，$A$ 是通常的类 CIS 的 TDDFT/TDA 线性响应矩阵（包括一电子项和两电子项）：

<a id="A3.S8.EGx51"></a>

$$
\displaystyle\langle{\Phi_{\bm{i}}^{\bm{a}}}|{A}|{\Phi_{\bm{j}}^{\bm{b}}}\rangle \tag{7.51}
$$

其中指标 $\bm{a},\bm{b},\bm{i},\bm{j}$ 为自旋轨道，$F$ 是 Fock 矩阵，$E_{gs}$ 是 SCF 能量，$\Omega$ 是 DFT 交换-关联泛函。更多细节可参见第 [7.3.1](sect_tddftintro.md) 节及文献 [[107]](../bib_references/bib.md#bib94)
。

式 ([7.50](#eq:tda_soc)) 中的 $V_{\text{SO}}$ 是式 ([7.38](#eq:HSO_Breit_Pauli)) 中出现的一电子 SOC 哈密顿量，而 $V_{m}=g\mu_{B}\mathbf{B}\cdot\mathbf{S}$ 是自旋-Zeeman 项。这里假设 $g=2$。（轨道运动与磁场的耦合尚未包括在内。）$V_{\text{SO}}+V_{m}$ 的矩阵形式为

<a id="A3.S8.EGx52"></a>

$$
\displaystyle\langle{\Psi_{\bm{i}}^{\bm{a}}}|{V_{\text{SO}}+V_{m}}|{\Psi_{\bm{j}}^{\bm{b}}}\rangle=V_{\bm{a}\bm{b}}\delta_{\bm{i}\bm{j}}-V_{\bm{j}\bm{i}}\delta_{\bm{a}\bm{b}} \tag{7.52}
$$

$V$ 的矩阵元由下式给出

<a id="A3.S8.EGx53"></a>

$$
\displaystyle V_{p_{\alpha}q_{\alpha}} \tag{7.53}
$$

其中 $\alpha_{0}$ 是精细结构常数，$\tilde{\mathbf{L}}=\mathbf{L}/r^{3}$。

!!! note "注意"
    目前，该 CIS 或 TDDFT/TDA-SOC 实现仅支持限制型 SCF 计算（在没有 SOC 时，此类计算会产生激发单重态和三重态）。此外，基态不通过 SOC（或以其他方式）与激发态耦合。


该程序通过设置 *$rem* 变量 CIS_SOC = $N$ 来触发，其中 $N$ 是所需的根数：

### `CIS_SOC`

> **控制 TDDFT/TDA-SOC 计算所求根的数目。**
>
> * **类型**: `INTEGER/LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行该计算。 $N$ 求解 $N$ 个最低的 TDDFT/TDA-SOC 自旋绝热态。
> * **建议**: 不大于 $4\times$ CIS_N_ROOTS。TDDFT/TDA-SOC 会先执行一次标准的 TDDFT/TDA 计算以生成初始猜测，然后重新进行对角化以生成自旋绝热线。因此，一个好的做法是先单独执行一次常规的 TDDFT/TDA 计算，生成激发自旋 diabats（自旋 diabatic 态）并检查所需的能量范围，之后再生成激发自旋绝热线。

若要加入 post-SCF 磁场，必须初始化 *$bfield_postscf* 区块：

> ```qchem
> $bfield_postscf
>     B_x B_y B_z
>     $end
> ```

这里，$B_{x},B_{y},B_{z}$ 是外磁场的空间分量，单位为特斯拉（Tesla）。其数值格式必须为浮点数（即 "0" 应写为 "0.0"）。

自旋绝热线之间的导数耦合计算是可行的，但请注意，实部和虚部的数值可能在不同计算之间有所变化——因为波函数是复数值，且每次计算可能带有不同的全局相位（规范）。导数耦合的模（norm）不应改变。

示例 [7.3.10.2](#ex:cissoc)、[7.3.10.2](#ex:cissoc) 和 [7.3.10.2](#ex:cissoc) 演示了使用 TDDFT/TDA-SOC 进行能量、梯度和导数耦合的计算。在示例 [7.3.10.2](#ex:cissoc) 中，还加入了 post-SCF 外磁场。

???+ example "示例 7.25: 使用 $\omega$ B97X 泛函，对甲醛进行 TDDFT/TDA-SOC 计算，求最低的 7 个自旋绝热线。"
    ```qchem
    $rem
    jobtype                 sp
    exchange                wb97x
    basis                   6-31g
    cis_convergence         8
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 7
    $end
    
    $molecule
    0   1
    C 0 0 0
    H 0 0 1.101224
    H 1.00171657 0 -0.45744749
    O -1.00461935 0 -0.645642
    $end
    
    ```

???+ example "示例 7.26: 使用 $\omega$ B97X 泛函对甲醛进行 TDDFT/TDA-SOC 计算中第 4 态的核梯度。"
    ```qchem
    $rem
    jobtype                 force
    exchange                wb97x
    basis                   6-31g
    cis_convergence         8
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 4
    cis_state_deriv         4
    new_dft                 1 ! This is necessary
    $end
    
    $molecule
    0   1
    C 0 0 0
    H 0 0 1.101224
    H 1.00171657 0 -0.45744749
    O -1.00461935 0 -0.645642
    $end
    
    ```

???+ example "示例 7.27: 在沿 z 方向 10 特斯拉外磁场存在下，使用 $\omega$ B97X 泛函对苯甲醛计算第 4 与第 7 个 TDDFT/TDA-SOC 态之间的导数耦合。"
    ```qchem
    $rem
    jobtype                 sp
    exchange                wb97x
    basis                   6-31g
    scf_convergence         10
    cis_convergence         10
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 7
    calc_nac                true
    cis_der_numstate        2
    $end
    
    $derivative_coupling
    ...
    4 7
    $end
    
    $bfield_postscf
    0.0 0.0 10.0
    $end
    
    $molecule
    0   1
    C -0.0827555811 -0.0021927111 0.0742168160
    C 0.0163712008 -0.0019362341 1.3503524350
    H 0.9426483579 -0.0021873514 1.9554892885
    C -1.2462538108 -0.0012178895 2.1035447415
    H -1.1928615664 -0.0009432042 3.1942205420
    C -2.4029093145 -0.0008942470 1.4089112839
    H -3.3571329386 -0.0003915665 1.9718859042
    C -2.4418611557 -0.0012099958 0.0672877891
    H -3.3674530317 -0.0009676703 -0.5174127708
    C -1.1678601986 -0.0019316068 -0.6798528411
    H -1.2448466539 -0.0022668669 -1.7738119236
    C 1.1607172056 -0.0028394281 -0.8113481262
    H 1.2563061018 -0.0031882755 -1.8250763954
    O 2.4950317353 -0.0032860998 -0.1735593327
    $end
    
    ```
