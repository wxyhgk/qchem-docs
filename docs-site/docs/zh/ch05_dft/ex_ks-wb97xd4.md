---
title: "5.6.3 用户自定义 RSH 泛函"
---

## 5.6.3 用户自定义 RSH 泛函

(2026 年 7 月 4 日)

正如文献 [[352]](../bib_references/bib.md#bib356) 及其他场所指出的那样，
在密度泛函理论（density functional theory, DFT）（更准确地说，是第 [7.3](../ch07_excited/sect_tddft.md) 节讨论的含时 DFT，TDDFT）中描述电荷转移（charge-transfer）激发态，
至少在大供体–受体间距的极限下，需要完全的 (100%) 非局域 HF 交换。
然而，B3LYP[[96]](../bib_references/bib.md#bib78)
 和 PBE0[[20]](../bib_references/bib.md#bib4)
 等成熟且被广泛使用的杂化泛函分别仅采用了 20% 和 25% 的 HF
交换。虽然这些泛函对许多基态性质能给出极好的结果，但它们无法正确描述电荷转移激发能随距离的变化关系，而大多数常用密度泛函会极大地低估这些激发能。无论何种情形这都是一个严重问题，而在大分子和非共价团簇中这更是一个*灾难性*的问题——在这些体系中，TDDFT 常常预测出一堆虚假的、近乎连续的低能电荷转移态。[[750]](../bib_references/bib.md#bib783)
 TDDFT 在描述电荷转移方面的问题并不局限于大的供体–受体间距，早在 $\sim$2 Å 的间距下、在尿嘧啶–(H${}_{2}$O)${}_{4}$
这样小的体系中就有观测。[[750]](../bib_references/bib.md#bib783)
 标准 TDDFT 对里德堡（Rydberg）激发能的预测也往往被严重低估。

纠正这类问题的一种可能途径是对包含 100% HF 交换的泛函进行参数化，尽管迄今此类泛函为数不多。另一种选择是尝试在短程保留常用 GGA 和杂化泛函的形式（*即*，在 PBE0 中保留 25% 的 HF 交换），同时在长程引入 100% 的 HF 交换，这样可以对电荷转移激发能的长程距离依赖关系给出严格正确的描述，同时避免额外的 HF 交换污染短程交换-关联效应。这种分离借助于第 [5.3](sect_XCfuncs.md) 节中引入的范围分离（range-separation）*假定* 来实现。特别地，在长程使用 100% HF 交换的泛函（即 Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) 中 $c_{x,\rm LR}=1$）
被称为“长程校正”（long-range-corrected, LRC）泛函。例如，PBE0 的一个 LRC 版本将具有 $c_{x,\rm SR}=0.25$。

要完全确定一个 LRC 泛函，必须为 Eq. ([5.12](Ch5.S3.SS1.md#eq:erf_partition))
中的范围分离参数 $\omega$ 选择一个值。在极限
$\omega\rightarrow 0$ 下，Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA))
中的 LRC 泛函退化为一个非 RSH 泛函，其中不存在“SR”或“LR”之分，因为所有交换能和关联能都是使用完整的库仑算子 $r_{12}^{-1}$ 计算的。而 $\omega\rightarrow\infty$ 极限则对应于一个新泛函 $E_{xc}^{\rm RSH}=E_{c}+E_{x}^{\rm HF}$。完全的 HF 交换不适合与大多数当代 GGA 关联泛函配合使用，因此预期该极限的表现会相当差。根据基准测试，[[757]](../bib_references/bib.md#bib784)
 $\omega>1.0$ bohr${}^{-1}$ 的取值可能不值得考虑。

短程和长程 HF 交换能的计算是直接了当的，[[24]](../bib_references/bib.md#bib10)
 因此任何 RSH 泛函的关键在于短程 GGA 交换泛函的形式，**Q-Chem** 中提供了若干此类泛函。其中包括 Hirao 及其合作者描述的 B88 和
PBE 交换的短程变体，[[609]](../bib_references/bib.md#bib632)

在 **Q-Chem** 中称为 $\mu$B88 和 $\mu$PBE，[[1168]](../bib_references/bib.md#bib1221)
 以及 Scuseria 及其合作者提出的短程 PBE 交换的另一种表述形式，[[554]](../bib_references/bib.md#bib569)
 称为 $\omega$PBE。这些泛函之所以能在 **Q-Chem**
中使用，得益于 Herbert 课题组的努力。[[1177]](../bib_references/bib.md#bib1230)
 就记号而言，“$\mu$PBE”、“$\omega$PBE” *等* 术语仅指短程交换泛函，
即 Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) 中的 $E_{x,\rm SR}^{\rm DFT}$。这些泛函可以按第 [5.3](sect_XCfuncs.md)
节所述在“屏蔽交换（screened exchange）”模式下使用，例如 HSE03
泛函，[[576]](../bib_references/bib.md#bib595)
 因此，例如 “LRC-$\omega$PBE” 这一名称，只应在短程交换泛函 $\omega$PBE 与长程 100% Hartree-Fock 交换组合使用时才采用。

一般而言，已证明 LRC-DFT 泛函能够消除大规模 TDDFT 计算中出现的、近乎连续的虚假电荷转移激发态。[[757]](../bib_references/bib.md#bib784)
 然而，某些结果对范围分离参数
$\omega$ 的取值非常敏感，[[757]](../bib_references/bib.md#bib784)

尤其是在 TDDFT 计算中（第 [7.3](../ch07_excited/sect_tddft.md) 节），因此 LRC-DFT
计算的结果必须谨慎解读，并且很可能应在一系列 $\omega$ 取值下考察。这可以通过
请求一个包含某种短程 GGA 交换泛函（如上述示例中的 $\omega$PBE 或 $\mu$PBE）的泛函，
并结合设置 *$rem* 变量 LRC_DFT = TRUE 来实现，后者请求在长程添加 100% Hartree-Fock
交换。基本的任务控制变量及示例见下文。范围分离参数的取值随后由变量 OMEGA
控制，如下方示例所示。

### `LRC_DFT`

> **控制是否应用长程校正 DFT（long-range-corrected DFT）**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`（或 `0`）: 不应用长程校正。
>     * `TRUE`（或 `1`）: 在所请求的泛函上添加 100% 长程 Hartree-Fock 交换。
> * **建议**: 还必须指定 $rem 变量 OMEGA，以设置范围分离参数。

### `OMEGA`

> **设置基于 Hirao RSH 方案的泛函中的范围分离参数 $\omega$（也称为 $\mu$）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * $n$: 对应于 $\omega=n/1000$，单位为 bohr ${}^{-1}$
> * **建议**: 无

### `COMBINE_K`

> **控制短程与长程 K 矩阵是分别构建还是合并构建**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`（或 `0`）: 分别构建短程和长程 K 矩阵（开销为全局杂化泛函的两倍）
>     * `TRUE`（或 `1`）: 合并构建短程和长程 K 矩阵（$\approx$ 开销与全局杂化泛函相当）
> * **建议**: Q-Chem 中大多数预定义的范围分离杂化泛函默认使用此功能。然而，如果想要用户自定义的 RSH，则必须手动开启此功能。

### `HFK_SR_COEF`

> **设置短程 HF 交换的系数**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$: 对应于 $n/100000000$
> * **建议**: 无

### `HFK_LR_COEF`

> **设置长程 HF 交换的系数**
>
> * **类型**: `INTEGER`
> * **默认值**: `100000000`
> * **选项**:
>     * $n$: 对应于 $n/100000000$
> * **建议**: 无

???+ example "示例 5.6: LRC-$\mu$BOP 在 $\rm(H_{2}O)_{2}^{-}$ 上的应用。"
    ```qchem
    $comment
       The value of omega is 0.47 by default but can
       be overwritten by specifying OMEGA.
    $end
    
    $molecule
       -1 2
       O           1.347338    -0.017773    -0.071860
       H           1.824285     0.813088     0.117645
       H           1.805176    -0.695567     0.461913
       O          -1.523051    -0.002159    -0.090765
       H          -0.544777    -0.024370    -0.165445
       H          -1.682218     0.174228     0.849364
    $end
    
    $rem
       EXCHANGE      LRC-BOP
       BASIS         6-311(1+,2+)G*
       XC_GRID       2
       LRC_DFT       TRUE
       OMEGA         300      ! = 0.300 bohr**(-1)
    $end
    ```

Rohrdanz *等*[[1178]](../bib_references/bib.md#bib1231)
 发表了一项使用 LRC-$\omega$PBEh
泛函对基态和激发态性质进行全面基准研究的论文，其中 “h” 表示短程杂化（*即*，存在一定比例的短程 HF 交换）。经验优化得到的参数为
$c_{x,\rm SR}=0.2$（见 Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA))）和 $\omega=0.2$ bohr${}^{-1}$，[[1178]](../bib_references/bib.md#bib1231)
 这些参数被取作 LRC-$\omega$PBEh
的默认值。然而仍需格外谨慎，尤其是在大体系的 TDDFT 计算中，因为具有电荷转移特征的态的激发能对 $\omega$ 的精确取值可能相当敏感。[[752]](../bib_references/bib.md#bib785)
 在这类情形下（或许一般而言如此），推荐采用第 [5.6.4](subsubsec_w-tuning.md)
节描述的“调控（tuning）”流程。

???+ example "示例 5.7: LRC-$\omega$PBEh 在间距为 5 Å 的 $\rm C_{2}H_{4}$ – $\rm C_{2}F_{4}$ 二聚体上的应用。"
    ```qchem
    $comment
        This example uses the "optimal" parameter set discussed above.
        It can also be run by setting METHOD = LRC-wPBEh.
    $end
    
    $molecule
       0 1
       C           0.670604    0.000000    0.000000
       C          -0.670604    0.000000    0.000000
       H           1.249222    0.929447    0.000000
       H           1.249222   -0.929447    0.000000
       H          -1.249222    0.929447    0.000000
       H          -1.249222   -0.929447    0.000000
       C           0.669726    0.000000    5.000000
       C          -0.669726    0.000000    5.000000
       F           1.401152    1.122634    5.000000
       F           1.401152   -1.122634    5.000000
       F          -1.401152   -1.122634    5.000000
       F          -1.401152    1.122634    5.000000
    $end
    
    $rem
       EXCHANGE      GEN
       BASIS         6-31+G*
       LRC_DFT       TRUE
       OMEGA         200      ! = 0.2 a.u.
       CIS_N_ROOTS   4
       CIS_TRIPLETS  FALSE
    $end
    
    $xc_functional
       C  PBE   1.00
       X  wPBE  0.80
       X  HF    0.20
    $end
    ```

最近，Li 和 Chai 结合最新版半经验色散校正 D4，重新优化了 B97 型范围分离泛函。[[815]](../bib_references/bib.md#bib858)
 所得泛函记为 KS-$\omega$B97X-D4，其表现与 $\omega$B97M-V 相当，并在整个 GMTKN55 数据库上始终优于 $\omega$B97X-D3 和 $\omega$B97X-V。[[815]](../bib_references/bib.md#bib858)

???+ example "示例 5.8: 对 H ${}_{2}$ 分子进行 KS-$\omega$B97X-D4 计算"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    SCF_GUESS            = SAD
    GEN_SCFMAN           = FALSE
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 0
    TAO_DFT_THETA_NDP    = 0
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    SYMMETRY             = false
    SYM_IGNORE           = true
    DFT_D                = D4
    DFT_D4_A1            = 35000000
    DFT_D4_A2            = 500000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 139483100
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X HF                  0.186861
    X KS_wB97X            1.000000
    C KS_wB97X            1.000000
    $end
    ```

通过在渐近库仑算子上添加 100% Hartree-Fock 交换，LRC 泛函保证了电子和空穴感受到的渐近相互作用势为 $1/r$。
这对于气相分子是正确的，但若要模拟材料，人们可能希望渐近行为为 $1/(\varepsilon r)$，其中 $\varepsilon$ 是材料的（静态）介电常数。
结合第 [5.6.4](subsubsec_w-tuning.md) 节所述的范围分离参数“最优调控（optimal tuning）”，
已证明此类泛函能为有机光伏材料给出准确的基本带隙（fundamental gaps），[[719]](../bib_references/bib.md#bib752)
 并且自然可以与采用相同介电常数的极化连续介质模型（第 [11.2.3](../ch11_env/topic_pcm-em.md) 节）
结合使用。[[128]](../bib_references/bib.md#bib117)

这些泛函被称为*屏蔽* RSH（screened RSH, sRSH）泛函。[[719]](../bib_references/bib.md#bib752)

这类 XC 泛函可通用地表示为[[33]](../bib_references/bib.md#bib16)

<a id="eq:sRSH"></a>

$$
E_{xc}^{\textrm{sRSH}}=c_{x,{\rm SR}}E_{x,{\rm SR}}^{\textrm{HF}}+\varepsilon^{-1}E_{x,\rm LR}^{\textrm{HF}}+(\varepsilon^{-1}-c_{x,\rm SR})E_{x,\rm SR}^{\textrm{DFT}}+(1-\varepsilon^{-1})E_{x,\rm LR}^{\textrm{DFT}}+E_{c}^{\textrm{DFT}}\;, \tag{5.17}
$$

应将其与给出 RSH 泛函通用形式的 Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) 相比较。
尽管 RSH 形式允许长程 Hartree-Fock 交换项具有任意系数 $c_{x,\rm LR}$（如 Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) 所示），
但这意味着渐近电子–空穴相互作用的形式为 $c_{x,\rm LR}/r$ 而非 $1/r$。[[352]](../bib_references/bib.md#bib356)

因此，LRC 泛函是 RSH 泛函中 $c_{x,\rm LR}=1$ 的一个特殊类别，以保证在真空中的正确渐近行为。同理，sRSH 泛函取 $c_{x,\rm LR}=\varepsilon^{-1}$
以保证在介电材料中的正确渐近行为。利用 Eq. ([5.17](#eq:sRSH))，用户可以通过
*$xc_functional* 输入段来构造 sRSH 泛函。

---

翻译后的完整内容已同时保存至 `5.6.3_user-defined-rsh-functionals_zh.md`。
