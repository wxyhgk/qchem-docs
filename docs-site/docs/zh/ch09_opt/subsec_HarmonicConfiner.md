---
title: "9.4.7 原子约束势作为约束优化的替代方案"
---

## 9.4.7 原子约束势作为约束优化的替代方案

(July 4, 2026)

从原理上讲,使用固定原子进行的约束优化所能达到的相同效果,也可以通过如下形式的软谐振约束势（soft harmonic confining potential）来实现

<a id="eq:Vconf_cart"></a>

$$
V_{\text{conf}}(\mathbf{r}_{1},\mathbf{r}_{2},\ldots)=\frac{1}{2}\sum_{i}k\|\mathbf{r}_{i}-\mathbf{r}_{i}^{0}\|^{2}\;. \tag{9.42}
$$

该式表示一个外部势场,将第 *i* 个原子（坐标为 $\mathbf{r}_{i}$）约束在位置 $\mathbf{r}_{i}^{0}$ 附近。上述实现方式被称为*笛卡尔（cartesian）*约束器（confiner），因为它基于每个被约束原子的笛卡尔坐标。实现谐振约束器的另一种方式是使用如下形式的*成对（pairwise）*谐振约束势

<a id="eq:Vconf_pair"></a>

$$
V_{\text{conf}}(\mathbf{r}_{1},\mathbf{r}_{2},\ldots,\mathbf{r}_{N})=\frac{1}{2}\sum^{N}_{i>j}k\|\mathbf{r}_{ij}-\mathbf{r}_{ij}^{0}\|^{2}\;. \tag{9.43}
$$

该式表示一个外部势场,将第 $i$ 个与第 $j$ 个原子（二者间距离为 $\mathbf{r}_{ij}$）约束在初始（或指定的）距离 $\mathbf{r}_{ij}^{0}$ 上。在将团簇模型（cluster model）应用于酶体系（作为量子力学/分子力学（QM/MM）模拟的低成本替代方案）时,需要锁定某些原子使其保持在晶体学位置上,以便在气相或连续介质溶剂中弛豫几何结构,同时避免活性位点模型的塌缩。[[1253]](../bib_references/bib.md#bib1306)

在每个被约束原子的唯一原子对之间使用成对约束势,可以让优化以*非约束*方式进行,即为了提高效率而采用离域内坐标（delocalized internal coordinates）（而非笛卡尔坐标）,同时又能达到与酶反应团簇模型中广泛使用的传统固定原子方法相似的效果。通过将原子拴系（tether）在某个几何位置上,可以更好地模拟固定原子约束,但这样做就失去了在内坐标下进行优化的能力。[[1253]](../bib_references/bib.md#bib1306) 此外,使用谐振约束势还能减少困扰固定原子优化的虚频（imaginary frequency）数量,使得计算零点振动校正（zero-point vibrational correction）变得直接简便。[[302]](../bib_references/bib.md#bib307)

谐振约束势通过将 *$rem* 变量 HARM_OPT 设为 1 或 2 来激活,并在 *$harmonic_opt* 区块中列出被约束原子的索引。任何具体任务（job）只能使用一种类型的约束器。对于笛卡尔约束器,平衡位置（$\mathbf{r}_{i}^{0}$）必须在 *$coords* 区块中指定,如下例所示。

???+ example "示例 9.14: 使用笛卡尔约束势进行几何优化及随后的频率计算。"
    ```qchem
    $molecule
    0 1
      C         2.2847229688   -0.3069830925   -0.2968221397
      C         0.9156471557    0.1503924513    0.1693932675
      N        -0.0576877706   -0.7876400788    0.0645249649
      H         2.9837678662    0.5043669375   -0.1693203557
      H         2.2497378474   -0.5929607607   -1.3422589452
      H         2.6126794028   -1.1626691284    0.2825927880
      O         0.6966207559    1.2669942030    0.6077661092
      C        -1.4350712383   -0.4874947903    0.4670886412
      H         0.1463602169   -1.6783001309   -0.3307859180
      C        -2.1768099264    0.3412632672   -0.5936684676
      H        -1.3995705380    0.0636682083    1.3955334557
      H        -1.9421824240   -1.4270154508    0.6422037013
      H        -1.6624625664    1.2829541077   -0.7297597438
      H        -3.1943263155    0.5415731987   -0.2762358302
      H        -2.2051967614   -0.1880845317   -1.5391034623
    $end
    
    $rem
       JOBTYPE OPT
       BASIS  3-21G
       METHOD  HF
       point_group_symmetry false
       NO_REORIENT TRUE
       HARM_OPT 1 ! Turn on cartesian harmonic confining potential
       HOATOMS 2  ! No. of confined atoms
       HARM_FORCE 450 ! Force constant of the potential
    $end
    
    $harmonic_opt
    1 10 ! indices of the confined atoms
    $end
    
    $coords !coordinates of confined atoms
      C1    2.2847229688   -0.3069830925   -0.2968221397
     C10   -2.1768099264    0.3412632672   -0.5936684676
    $end
    
    $geom_opt
    initial_hessian = simple
    hessian_verify = recomputed !Recompute Exact Hessian for verification
    final_vibrational_analysis = true !Perform Vibrational Analysis on optimized Hessian
    $end
    
    ```

对于成对约束器,两个受约束原子之间的成对距离（$\mathbf{r}_{ij}^{0}$）可以选择性地放入 *$coords* 区块中；若未指定 $\mathbf{r}_{ij}^{0}$,则使用 *$molecule* 中给出的初始原子间距来计算平衡距离。下面展示了一个成对约束器优化及随后频率计算的示例。

???+ example "示例 9.15: 使用成对约束势进行几何优化及随后的频率计算。
注意频率计算中没有 $coords 区块。复合任务（compound job）会将平衡坐标从一个任务传递到下一个任务。而单独运行的成对约束器任务则需要指定 $coords,以维持相同的势能面。"
    ```qchem
    $molecule
    
    0 1
     H  -0.68168  -1.29335  0.69937
     C  -0.01515  -0.39524  0.63493
     N  1.06556  -0.59220  1.63009
     H  1.57017  -1.42548  1.41732
     H  1.68831  0.18821  1.62555
     C  -0.82092  0.86652  1.01181
     H  -1.07481  0.84874  2.09044
     H  -0.23531  1.78800  0.81958
     O  -1.99965  0.85940  0.24056
     H  -2.47074  1.65064  0.46275
     C  0.53081  -0.25778  -0.78386
     O  1.40105  0.49365  -1.18881
     O  -0.00029  -1.09878  -1.69507
     H  0.36786  -0.92650  -2.55634
    
    $end
    
    $rem
     JOBTYPE = OPT
     BASIS = MINIX
     METHOD = HF3c
    
     HARM_OPT = 2 ! Turn on pairwise harmonic confining potential
     HOATOMS = 2 ! No. of confined atoms
     HARM_FORCE = 50 ! force per spring (scaled by 1/1000)
    $end
    
    $harmonic_opt ! specifies which atoms to be confined
    3 11
    $end
    
    $coords ! optional for pairwise - specifies distance between pairs of atoms
     3 11 50.0
    $end
    
    @@@
    
    $molecule
     READ
    $end
    
    $rem
     JOBTYPE = FREQ
     BASIS = MINIX
     METHOD = HF3c
    
     HARM_OPT = 2
     HOATOMS = 2
     HARM_FORCE = 50
    $end
    
    $harmonic_opt
    3 11
    $end
    ```

每次使用成对谐振约束器完成几何优化后,*$coords* 区块都会打印在输出文件中 "Harmonic Coords Print:"（谐振坐标打印）标题之下。这使用户能够在不同任务之间维持相同的势能面。例如,使用成对约束器进行几何优化会生成一个 *$coords* 区块,随后可将其用于需要与优化任务受力相匹配的频率计算任务中。

HARM_OPT

### `HARM_OPT`

> **控制任务是否使用约束势**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不使用约束势
>     * 1
>     * 使用笛卡尔约束势
>     * 2
>     * 使用成对约束势
> * **推荐设置**: False

HOATOMS

### `HOATOMS`

> **控制被约束原子的数目**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * 用户自定义
> * **推荐设置**: None

HARM_FORCE

### `HARM_FORCE`

> **设置谐振约束器的力常数,单位为 N/m。对于成对约束器,力会除以 1000,因此设定值 5000 相当于对每个弹簧施加 5 N/m 的力常数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * 用户自定义
> * **推荐设置**: None
