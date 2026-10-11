---
title: "4.5.6 伪分数占据数方法（pFON）"
---

## 4.5.6 伪分数占据数方法（Pseudo-Fractional Occupation Number Method, pFON）

（2026 年 7 月 4 日）

对于最高占据分子轨道/最低未占分子轨道（HOMO/LUMO）能隙很小（或为零）的情形，除能级移动（level-shifting）之外的另一种选择是伪分数占据数（pseudo-fraction occupation number, pFON）方法，[[1140]](../bib_references/bib.md#bib1192)
 该方法相当于对 HOMO 能级处的占据数进行“抹平”处理。通常情况下，这可以消除小能隙体系中可能出现的（从一次自洽场（SCF）迭代到下一次迭代的）不连续占据变化，从而改善稳定性并加速收敛。本质上，在同一次轨道优化过程中允许存在多种电子组态，并带有分数占据。这在形式上等价于有限温度形式体系。

pFON 方法引入如下的密度矩阵

<a id="Ch4.E37"></a>

$$
P_{\mu\nu}=\sum_{p=1}^{N}\;n_{p}C_{\mu p}C_{\nu p} \tag{4.37}
$$

其占据数 $0\leq n_{p}\leq 1$ 可以取分数值；而在常规的 SCF 计算中，要么 $n_{p}=1$（占据），要么 $n_{p}=0$（虚轨道）。在 pFON 中，占据数遵循费米-狄拉克（Fermi-Dirac）分布，

<a id="Ch4.E38"></a>

$$
n_{p}=\bigl{(}1+e^{(\epsilon_{p}-\epsilon_{\mathrm{F}})/kT}\bigr{)}^{-1}\;, \tag{4.38}
$$

其中 $\epsilon_{p}$ 是 SCF 本征值（轨道能量），$T$ 是温度。在 **Q-Chem** 的实现中，费米能设为 $\epsilon_{\mathrm{F}}=(\epsilon_{\mathrm{HOMO}}+\epsilon_{\mathrm{LUMO}})/2$。为保证总电子数守恒，pFON 方法会对占据数重新缩放，使得 $\sum_{p}\;n_{p}=N_{\mathrm{el}}$。

有多个参数可用于在整个 pFON SCF 计算过程中控制电子温度 $T$。温度既可以保持为恒定的有限温度（$T_{\mathrm{init}}$ = $T_{\mathrm{final}}$），也可以让体系从较高温度逐步冷却至最终温度。目前尚未实现零温度外推。

OCCUPATIONS

### `OCCUPATIONS`

> **激活 pFON 计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 整数占据数
>     * 1
>     * 尚未实现
>     * 2
>     * 伪分数占据数（pFON）
> * **建议**: 对小能隙体系，使用 pFON 以改善收敛。

FON_T_START

### `FON_T_START`

> **FON 计算的初始电子温度（单位为 K）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1000`
> * **可选值**:
>     * 任意所需的初始温度。
> * **建议**: 选取温度时，要么用于复现实验条件（例如室温），要么尽可能低以逼近零温度。

FON_T_END

### `FON_T_END`

> **FON 计算的最终电子温度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 任意所需的最终温度。
> * **建议**: 选取温度时，要么用于复现实验条件（例如室温），要么尽可能低以逼近零温度。

FON_NORB

### `FON_NORB`

> **允许取分数占据的、位于费米能级之上和之下的轨道数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **可选值**:
>     * $n$
>     * 活性轨道数目
> * **建议**: 选择价层轨道的数目是一个合理的做法。

FON_T_SCALE

### `FON_T_SCALE`

> **决定冷却的步长。**
>
> * **类型**: `INTEGER`
> * **默认值**: `90`
> * **可选值**:
>     * $n$
>     * 温度在每一循环中按
>     * $0.01\cdot n$
>     * 进行缩放（冷却方式 1）
>     * $n$
>     * 温度在每一循环中降低 n K（冷却方式 2）
> * **建议**: 冷却速率不宜过慢也不宜过快。过慢可能导致最终能量对应于不理想的高温状态；过快则可能导致收敛问题。对方式 1 和方式 2，合理的取值分别为 98 和 50。如有疑虑，请使用恒温方式。

FON_E_THRESH

### `FON_E_THRESH`

> **当 DIIS 误差低于该值时，占据数将被保持恒定。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **可选值**:
>     * $n$
>     * 当 DIIS 误差低于
>     * $10^{-n}$
>     * 时冻结占据数
> * **建议**: 该值应比期望的 SCF 收敛阈值大一到两个数量级。

FON_T_METHOD

### `FON_T_METHOD`

> **选择冷却算法。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * 1
>     * 温度在每一循环中按某一因子缩放
>     * 2
>     * 温度在每一循环中减少一个恒定的数值
> * **建议**: 我们使用恒定冷却速率的经验略好一些。不过，如有疑虑，请选择恒温方式。

???+ example "示例 4.11: 金属团簇的 pFON 计算。"
    ```qchem
    $molecule
       0 1
       Pt   -0.20408    1.19210    0.54029
       Pt    2.61132    1.04687    0.66196
       Pt    0.83227    0.03296   -1.49084
       Pt    0.95832   -1.05360    0.92253
       Pt   -1.66760   -1.07875   -1.02416
    $end
    
    $rem
       METHOD          pbe
       MAX_SCF_CYCLES  200
       ECP             fit-lanl2dz
       BASIS           lanl2dz
       OCCUPATIONS     2    ! pseudo-fractional occupation numbers
       FON_NORB        10   ! 10 fractionally occupied orbitals above and below the Fermi level
       FON_T_START     1000 ! starting electronic temperature: 1000 K
       FON_T_END       0    ! final electronic temperature: 0 K
       FON_T_METHOD    2    ! constant cooling scheme
       FON_T_SCALE     25   ! reduce the temperature by 25 K per cooling step
       FON_E_THRESH    5    ! freeze occupation numbers once DIIS error is 10-5
       GEN_SCFMAN        false
       INTEGRAL_SYMMETRY false
    $end
    
    ```
