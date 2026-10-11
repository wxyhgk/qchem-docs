---
title: "7.12.3 基于 Kohn-Sham 本征值的方法"
---

## 7.12.3 基于 Kohn-Sham 本征值的方法

（2026 年 7 月 4 日）

## 7.12.3.1 Koopmans 方法

对于 X 射线发射（x-ray emission），相较 TDDFT 更为简便的替代方案是利用 Kohn-Sham 本征值之差，

<a id="Ch7.E176"></a>

$$
\Delta E=\epsilon_{v}-\epsilon_{c}\;, \tag{7.176}
$$

其中 $\epsilon_{v}$ 和 $\epsilon_{c}$ 分别为价层（valence）与芯层（core）能级。振子强度（oscillator
strengths）由相应的跃迁偶极矩阵元求得，

<a id="eq:f-trans-dipole"></a>

$$
f_{c\to v}\propto\|\langle\phi_{c}|\hat{\bm{\mu}}|\phi_{v}\rangle\|^{2}\;. \tag{7.177}
$$

这种 Koopmans 定理类型的方法 somewhat 粗略，
因为它没有考虑芯激发态中的轨道弛豫（orbital relaxation），但其优点在于只需要进行一次基态计算，
因此该方法适用于大体系，[[522]](../bib_references/bib.md#bib538)

并且与短程校正（short-range corrected, SRC）泛函结合使用时，即使这一简单流程也能对跃迁能给出
合理的估计。[[521]](../bib_references/bib.md#bib535)
 该方法由 *$rem* 变量
NCORE_XES 和 NVAL_XES 控制，用于指定所考虑的芯层（$c$）和价层（$v$）
能级的数目，示例见示例 [7.12.3.1](#ex:XES-KSDFT)。将此方法推广到
共振 X 射线发射光谱（resonant x-ray emission spectroscopy，涉及激发电子态）也是可行的，方法是将该态
建模为 SCF 方程的非 *aufbau*（非构造原理）解，*e.g.*，使用诸如（第 [4.5.14](../ch04_scf/topic_mom.md) 节）、SGM（第 [4.5.15](../ch04_scf/sect_SGM-SCF.md) 节）或 STEP（第 [4.5.16](../ch04_scf/sect_STEP-SCF.md) 节）等算法。

NCORE_XES

### `NCORE_XES`

> **指定在 Koopmans 型 XES 计算中使用多少个芯层能级。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$
>     * 计算对应于最靠前（能量最低）的
>     * $n$
>     * 个芯层轨道
>     * $\phi_{c}$
>     * 的跃迁偶极矩。
> * **推荐**: 无

NVAL_XES

### `NVAL_XES`

> **指定在 Koopmans 型 XES 计算中使用多少个价层虚轨道能级。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$
>     * 计算对应于最高的
>     * $n$
>     * 个占据轨道
>     * $\phi_{v}$
>     * 的跃迁偶极矩。
> * **推荐**: 设置 $n=1$ 将在占据空间中包含 HOMO，$n=2$ 将包含 HOMO 和 $\text{HOMO}-1$，依此类推。

???+ example "示例 7.211: 使用短程校正（SRC）泛函的 Koopmans 方法计算水的 XES 谱。"
    ```qchem
    $molecule
       0 1
       C         0.0000000000    0.0000000000    0.5121520001
       O         0.0000000000    0.0000000000   -0.6942567610
       H         0.9377642813    0.0000000000    1.1074358558
       H        -0.9377642813    0.0000000000    1.1074358558
    $end
    
    $rem
       METHOD          src1r1
       BASIS           6-311G**
       NCORE_XES       2
       NVAL_XES        4
    $end
    ```

## 7.12.3.2 跃迁势 DFT（Transition-Potential DFT, TP-DFT）

*跃迁势*（transition potential, TP-）DFT 方法[[1308]](../bib_references/bib.md#bib1365)

是一种替代方案，它考虑了部分轨道弛豫，同时保留了基于 Kohn-Sham 本征值的框架，且只需进行一次基态计算。
该方法基于 Slater 的跃迁概念，[[1269]](../bib_references/bib.md#bib1322)

即在 SCF 计算中从占据轨道 $\phi_{i}$ 上移去分数个电子（原始取值为 $n_{i}=1/2$），
然后将该分子轨道（MO）的电离能（ionization energy）近似为

<a id="eq:TPDFT-ip"></a>

$$
\text{IE}_{i}\approx-\epsilon_{i}(n_{i}=1/2)\;. \tag{7.178}
$$

这一做法可以基于对轨道占据数的 Taylor 展开来加以论证。[[1269]](../bib_references/bib.md#bib1322)

激发能被近似为从分数电子 SCF 计算中得到的本征值之差 $\epsilon_{a}-\epsilon_{i}$，其中 $n_{i}=1/2$ 个电子
从 $\phi_{i}$ 被提升到 LUMO：

<a id="eq:TPDFT-ee"></a>

$$
\Delta E_{i\to a}=\epsilon_{a}(n_{i}=1/2,n_{\text{LUMO}}=1/2)-\epsilon_{i}(n_{i}=1/2,n_{\text{LUMO}}=1/2)\;, \tag{7.179}
$$

振子强度为 $f_{i\to a}\propto|\langle\phi_{i}|\hat{\bm{\mu}}|\phi_{a}\rangle|^{2}$，与式 ([7.177](#eq:f-trans-dipole)) 相同。

在 **Q-Chem** 中，TP-DFT 计算被设置为从由 TPDFT_ATOM 指定的原子的最低芯层轨道上移去 1/2 个电子。（关于更灵活、
更通用的分数电子 SCF 方案，参见第 [7.12.3.3](#ex:XAS-2) 节。）可选择使用 TPDFT_LUMO 来占据 LUMO，
对应于激发能计算 [式 ([7.179](#eq:TPDFT-ee))]；若省略该变量，则计算芯层电子结合能 [式 ([7.178](#eq:TPDFT-ip))]。

TPDFT_ATOM

### `TPDFT_ATOM`

> **通过指定要从中移去电子的原子来启用 TP-DFT。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$
>     * 从索引为
>     * $n$
>     * 的原子的最低能量轨道上移去一个电子。
> * **推荐**: 进行 TP-DFT 计算时务必设置 UNRESTRICTED = TRUE。

TPDFT_FRAC

### `TPDFT_FRAC`

> **指定要移去的 $n_{i}$ 的分数值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$
>     * 移去
>     * $n/100$
>     * 个电子，轨道由
>     * TPDFT_ATOM
>     * 指定。
> * **推荐**: 无

TPDFT_LUMO

### `TPDFT_LUMO`

> **指定要添加到 $n_{\text{LUMO}}$ 的分数值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 向 LUMO 添加
>     * $n/100$
>     * 个电子。
> * **推荐**: 进行芯层结合能计算时保持 = 0 [式 ( 7.178 )]，或使用 = 50 以实现式 ( 7.179 )。

???+ example "示例 7.212: TP-DFT 激发能计算，从 O(1s) 移去 $n_{i}=1/2$ 个电子并将其置于 LUMO 中。"
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 2 0.95 2 104.5
    $end
    
    $rem
       METHOD       b3lyp
       BASIS        aug-cc-pCVQZ
       UNRESTRICTED true
       TPDFT_ATOM   1
       TPDFT_FRAC   50
       TPDFT_LUMO   50 ! set to 0 for IE calculation
    $end
    
    ```

## 7.12.3.3 Slater 型分数电子方法

Jana 与 Herbert[[626]](../bib_references/bib.md#bib650)
 研究了一套更为通用的分数电子方法，既适用于芯层电离（*i.e.*，XPS），也适用于芯层激发
（XAS 以及 XES）。这些方法
推广了 Slater 的跃迁概念，[[1269]](../bib_references/bib.md#bib1322)
 允许从芯层分子轨道上移去任意分数个电子，并（可选地）将其放入虚分子轨道，具体由用户指定。
这些广义 Slater 型方法的使用由下文所述的 *$rem* 变量控制，并在随后的示例中加以说明。
对于 XAS，振子强度按式 ([7.177](#eq:f-trans-dipole)) 计算，而计算跃迁偶极矩所涉及的（占据，虚）轨道对 ($\phi_{i},\phi_{a}$)
通过 NCORE_XAS 和 NVAL_XAS 指定，如第 [7.12.3.1](#ex:XES-KSDFT) 节所述。
为收敛分数电子态，可能需要使用 MOM（第 [4.5.14](../ch04_scf/topic_mom.md) 节）、
SGM（第 [4.5.15](../ch04_scf/sect_SGM-SCF.md) 节）或 STEP（[4.5.16](../ch04_scf/sect_STEP-SCF.md)）等算法。
关于应选用哪一种广义 Slater 型方法的最佳实践，请参阅文献 [[626]](../bib_references/bib.md#bib650)
 和 [[627]](../bib_references/bib.md#bib651)
。

FRACTIONAL_ELECTRON

### `FRACTIONAL_ELECTRON`

> **指定要从占据空间中移去的电子分数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $-n$
>     * 移去
>     * $n/1000$
>     * 个电子。
> * **推荐**: 原始的 Slater 方法（$n_{i}=1/2$）对应 = $-$ 500，但也存在其他选择。

FRAC_VIR_ELEC

### `FRAC_VIR_ELEC`

> **指定要放入占据空间中的电子分数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 添加
>     * $n/1000$
>     * 个电子。
> * **推荐**: 对于激发（XAS 或 XES）应使用 $>0$ 的值，而默认值适用于电离（XPS）。

FRAC_ELEC_ORB

### `FRAC_ELEC_ORB`

> **指定要从中移去分数电子的占据轨道。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 从
>     * $\phi_{n}$
>     * 中移去。
> * **推荐**: 无

FRAC_VIR_ELEC_ORB

### `FRAC_VIR_ELEC_ORB`

> **指定要将分数电子添加到的虚轨道。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 添加到
>     * $\phi_{n}$
>     * 。
> * **推荐**: 仅当 FRAC_VIR_ELEC $>0$ 时才使用此项。

???+ example "示例 7.213: 用于氧 K 壳层 XPS 的原始 Slater 跃迁方法（STM），从 O(1s) 芯层轨道
移去 $n_{i}=1/2$ 个电子。
先通过常规 SCF 计算获得初始轨道组，随后进行分数电子计算，并使用 IMOM 算法使其收敛。"
    ```qchem
    $molecule
    0 1
    C  -0.00000000  0.00000000  0.07378202
    O   0.00000000  0.00000000  1.20921798
    $end
    
    $rem
     UNRESTRICTED  TRUE
     BASIS         def2-QZVP
     METHOD        B3LYP
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
     SCF_GUESS     READ
     METHOD        B3LYP
     BASIS         def2-QZVP
     UNRESTRICTED  TRUE
     FRAC_ELEC_ORB        1  ! lowest-energy orbital is O(1s)
     FRAC_VIR_ELEC_ORB    1
     FRACTIONAL_ELECTRON -500
     FRAC_VIR_ELEC        0
     MOM_START            1
     MOM_METHOD           IMOM
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    ```

???+ example "示例 7.214: 碳 K 边的 XAS 计算，使用 Slater 跃迁方法，从
C(1s) 移去 $n_{i}=1/2$ 个电子，并将 $n_{a}=1/2$ 个电子置于 LUMO 中。"
    ```qchem
    $molecule
     0 1
    C  -0.00000000  0.00000000  0.07378202
    O   0.00000000  0.00000000  1.20921798
    $end
    
    $rem
     UNRESTRICTED  TRUE
     BASIS         def2-QZVP
     METHOD        B3LYP
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
     SCF_GUESS     READ
     METHOD        B3LYP
     BASIS         def2-QZVP
     UNRESTRICTED  TRUE
     FRAC_ELEC_ORB        1  ! lowest-energy orbital is O(1s)
     FRAC_VIR_ELEC_ORB    1
     FRACTIONAL_ELECTRON -500
     FRAC_VIR_ELEC        0
     MOM_START            1
     MOM_METHOD           IMOM
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    ```
