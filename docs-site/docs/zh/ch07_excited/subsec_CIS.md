---
title: "7.2.2 单激发组态相互作用（Configuration Interaction with Single Substitutions, CIS）"
---

## 7.2.2 单激发组态相互作用（CIS）

（2026 年 7 月 4 日）

## 7.2.2.1 理论

单激发组态相互作用（CI-singles, CIS）能量与波函数的推导[[312]](../bib_references/bib.md#bib316)
 始于选取 Hartree-Fock（HF）单行列式波函数作为体系基态的参考：

<a id="eq600"></a>

$$
\Psi_{\mathrm{HF}}=\frac{1}{\sqrt{n!}}\det\left\{{\chi_{1}\chi{}_{2}\cdots\chi_{i}\chi{}_{j}\cdots\chi_{n}}\right\} \tag{7.1}
$$

其中 $n$ 为电子数，自旋轨道

<a id="eq601"></a>

$$
\chi_{i}=\sum\limits_{\mu}^{N}{c_{\mu i}\phi_{\mu}} \tag{7.2}
$$

由 $N$ 个原子轨道基函数构成的有限基组展开得到。分子轨道系数 $\{c_{\mu i}\}$ 通常通过自洽场（Self-Consistent Field, SCF）程序求解 Hartree-Fock 方程

<a id="eq602"></a>

$$
\mathbf{FC}=\bm{\varepsilon}\mathbf{SC}\;, \tag{7.3}
$$

求得，其中 **S** 是重叠矩阵，**C** 是分子轨道系数矩阵，$\varepsilon$ 是轨道本征值构成的对角矩阵，**F** 是 Fock 矩阵，其元素为

<a id="eq603"></a>

$$
F_{\mu\upsilon}=H_{\mu\upsilon}+\sum\limits_{\lambda\sigma}{\sum\limits_{i}{c_{\mu i}c_{\upsilon i}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)}} \tag{7.4}
$$

式中涉及核心哈密顿量以及反对称化的双电子积分

<a id="Ch7.E5"></a>

$$
(\mu\mu||\lambda\sigma)=\int\int\phi_{\mu}(\mathbf{r}_{1})\phi_{\nu}(\mathbf{r}_{2})\left(\frac{1}{r_{12}}\right)\bigl{[}\phi_{\lambda}(\mathbf{r}_{1})\phi_{\sigma}(\mathbf{r}_{2})-\phi_{\sigma}(\mathbf{r}_{1})\phi_{\lambda}(\mathbf{r}_{2})\bigr{]}\;d\mathbf{r}_{1}\,d\mathbf{r}_{2} \tag{7.5}
$$

求解方程 ([7.3](#eq602)) 后，基态单行列式的总能量可表示为

<a id="eq605"></a>

$$
E_{\mathrm{HF}}=\sum\limits_{\mu\upsilon}{P_{\mu\upsilon}^{\mathrm{HF}}H_{\mu\upsilon}}+\frac{1}{2}\sum\limits_{\mu\upsilon\lambda\sigma}{P_{\mu\upsilon}^{\mathrm{HF}}P_{\lambda\sigma}^{\mathrm{HF}}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)}+V_{\mathrm{nuc}} \tag{7.6}
$$

其中 $P^{\mathrm{HF}}$ 是 HF 密度矩阵，$V_{\mathrm{nuc}}$ 是核排斥能。

方程 ([7.1](#eq600)) 只是由体系轨道构成的众多可能行列式中的一个；事实上，通过将基态中占有的轨道（$i$、$j$、$k,\ldots$）替换为基态中未占有的轨道（$a$、$b$、$c,\ldots$），可以构造出 $n(N-n)$ 个可能的单替换行列式。这类波函数与能量可写为

<a id="eq606"></a>

$$
\Psi_{i}^{a}=\frac{1}{\sqrt{n!}}\det\left\{{\chi_{1}\chi{}_{2}\cdots\chi_{a}\chi{}_{j}\cdots\chi_{n}}\right\} \tag{7.7}
$$

<a id="eq607"></a>

$$
E_{ia}=E_{\mathrm{HF}}+\varepsilon_{a}-\varepsilon_{i}-\left({ia}\right.||\left.{ia}\right) \tag{7.8}
$$

这里引入了分子轨道基下的反对称化双电子积分

<a id="eq608"></a>

$$
\left({pq}\right.||\left.{rs}\right)=\sum\limits_{\mu\upsilon\lambda\sigma}{c_{\mu p}c_{\upsilon q}c_{\lambda r}c_{\sigma s}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)} \tag{7.9}
$$

这些单激发波函数与能量可以被看作体系激发态的粗略近似。然而，形如方程 ([7.7](#eq606)) 的行列式存在以下缺陷：

- 不能给出纯自旋态
- 更接近电离而非激发
- 不适合用于向简并态的激发

这些缺陷可以部分地通过将激发态波函数表示为*所有*可能单激发行列式的线性组合来克服，

<a id="eq:CIS-wavefn"></a>

$$
|\Psi_{\text{CIS}}\rangle=\sum_{ia}a_{i}^{a}|\Psi_{i}^{a}\rangle \tag{7.10}
$$

其中系数 $\{a_{i}^{a}\}$ 可通过对轨道 Hessian 矩阵 $\mathbf{A}$ 对角化获得。$\mathbf{A}$ 等价于在单激发空间中扣除基态能量后的哈密顿量。其矩阵元为

<a id="eq:orbital-Hessian"></a>

$$
A_{ia,jb}=\langle\Psi_{i}^{a}|\hat{H}-E_{\text{HF}}|\Psi_{j}^{b}\rangle=(\varepsilon_{a}-\varepsilon_{j})\delta_{ij}\delta_{ab}-(ja||ib)\;. \tag{7.11}
$$

根据 Brillouin 定理，单替换不与参考 HF 行列式直接相互作用，因此由 CIS 激发态得到的本征矢量所对应的处理精度大体与 HF 基态相当。激发能就是 HF 基态能量与 CIS 激发态能量之差，而 **A** 的本征矢量对应单电子跃迁的振幅。

**Q-Chem** 中可以限制（RCIS）[[312]](../bib_references/bib.md#bib316)
、非限制（UCIS）或开壳层限制[[919]](../bib_references/bib.md#bib955)
（ROCIS）自旋轨道进行 CIS 计算。CIS 相关作业控制变量列表见第 [7.2.4](sec_CIS-jobcontrol.md)
节。

???+ example "示例 7.1：在 HF/6-31G* 优化得到的基态几何结构上进行甲醛（formaldehyde）的基本 CIS 激发能计算，
该基态几何结构在作业的第一部分获得。高于第一单重激发态的各激发态具有 Rydberg（里德堡）
特征，因此使用带有两组弥散函数的基组。"
    ```qchem
    $molecule
       0  1
       C
       O  1  CO
       H  1  CH  2  A
       H  1  CH  2  A  3  D
    
       CO =   1.2
       CH =   1.0
       A  = 120.0
       D  = 180.0
    $end
    
    $rem
       JOBTYPE   =  opt
       EXCHANGE  =  hf
       BASIS     =  6-31G*
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE      =  hf
       BASIS         =  6-311(2+)G*
       CIS_N_ROOTS   =  15            Do 15 states
       CIS_SINGLETS  =  true          Do do singlets
       CIS_TRIPLETS  =  false         Don’t do Triplets
    $end
    ```

## 7.2.2.2 CIS 解析导数

虽然 CIS 激发能相对不够准确，误差约为 1 eV 量级，但 CIS 激发态性质——如结构和频率——则有用得多。这与基态 Hartree-Fock（HF）结构和频率远比 HF 相对能量准确的情形非常相似。一般而言，对于低能激发态，预期 CIS 振动频率会比实验值系统性地高约 10%[[1290]](../bib_references/bib.md#bib1348)
。若激发态为纯价态（valence）特征，则基组需求通常与基态相近；具有部分 Rydberg 特征的激发态则需要添加一组、最好是两组弥散函数。

**Q-Chem** 提供了高效的 CIS 能量解析一阶与二阶导数[[921]](../bib_references/bib.md#bib958)
，可给出解析梯度、激发态振动频率、力常数、极化率以及红外强度。只要 CIS 激发能计算本身可行，即可计算解析梯度，从而在 CIS 级别上进行高效的激发态几何优化和振动频率计算。在这类计算中，必须指定优化在哪个 Born-Oppenheimer 势能面上进行，并且需要注意确保优化保持在所关心的激发态上，因为可能发生态交叉（一种态追踪算法——见第 [9.8.5](../ch09_opt/sec_state_following.md)
节讨论——可以协助完成这一操作[[1549]](../bib_references/bib.md#bib1615)
）。

有时人们关注的恰恰是 Born-Oppenheimer 势能面之间的交叉（*即*，锥形交叉，conical intersection），因为这些交叉提供了电子态之间非绝热跃迁的通道[[916]](../bib_references/bib.md#bib952)
。**Q-Chem** 具备一项在其他程序中并不广泛提供的功能：对 CIS 和 TDDFT 均以解析方式实现定义锥形交叉点周围拓扑结构的非绝热耦合[[378]](../bib_references/bib.md#bib383)
。由于采用解析实现，这些耦合的计算成本不会明显高于 CIS 或 TDDFT 解析梯度计算的成本[[1547]](../bib_references/bib.md#bib1613)

，而这些耦合的可用性使得沿锥形交叉接缝（seam）优化最低能量交叉点（MECP）比仅有解析梯度时高效得多[[1547]](../bib_references/bib.md#bib1613)
。这些功能（包括锥形交叉理论的简要概述）见第 [9.8.1](../ch09_opt/subsec_NACMEs_and_CIs.md)
节。

在某些应用中，希望同时获得多个 CIS 或 TDDFT 电子态的梯度，这可以在 JOB_TYPE = force 下通过 *$rem* 变量 CIS_STATE_MULTIGRAD 实现。

对于 CIS 振动频率，可采用一种与基态 Hartree-Fock 频率类似的半直接（semi-direct）算法，对大分子其计算时间大致按 ${\cal{O}}({N^{3}})$
标度[[920]](../bib_references/bib.md#bib956)

。

解析 CIS 频率计算的主要难点在于确保 **Q-Chem** 有足够的内存来完成计算。默认设置对许多用途已经足够，但若大型计算因内存不足而失败，则以下附加信息可能有用。

CIS（以及 HF）解析频率的内存需求主要来自动态内存，其定义为

动态内存 = MEM_TOTAL $-$ MEM_STATIC   。

该数值必须足够大，以容纳若干大小为 $3N_{\rm atoms}N_{\rm basis}^{2}$ 的数组。与此同时，*$rem* 变量
MEM_STATIC 的取值（它显然会减少可用的动态内存）必须足够大以允许积分求值，否则作业可能失败。对大多数用途而言，将 MEM_STATIC 设为约 80 MB 即可，而默认情况下 MEM_TOTAL 被设置为高于多数计算机可用内存的值，因此用户无需为低内存作业猜测或试验合适的 MEM_TOTAL 取值。不过，如果计算所需内存超过可用内存，就会发生内存分配错误。

!!! note "注意"
    与 **Q-Chem** 的 MP2 频率代码不同，解析 CIS 二阶导数代码目前不支持冻结芯层或虚拟轨道（frozen core / frozen virtual）近似。由于所有计算量大的步骤都在原子轨道基下进行，这些近似在 CIS 级别上并不能带来显著的计算节省。


???+ example "示例 7.2：本示例演示在甲醛最低单重激发态上先进行 CIS 几何优化，随后进行振动频率分析。与基态不同，该 $n\rightarrow\pi^{\ast}$
激发态是非平面的。优化收敛到受力为零的非平面结构，且所有频率均为实频。"
    ```qchem
    $molecule
       0 1
       C
       O  1  CO
       H  1  CH  2  A
       H  1  CH  2  A  3  D
    
       CO  =    1.2
       CH  =    1.0
       A   =  120.0
       D   =  150.0
    $end
    
    $rem
       JOBTYPE          =  opt
       EXCHANGE         =  hf
       BASIS            =  6-31+G*
       CIS_STATE_DERIV  =  1         Optimize state 1
       CIS_N_ROOTS      =  3         Do 3 states
       CIS_SINGLETS     =  true      Do do singlets
       CIS_TRIPLETS     =  false     Don’t do Triplets
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE          =  freq
       EXCHANGE         =  hf
       BASIS            =  6-31+G*
       CIS_STATE_DERIV  =  1         Focus on state 1
       CIS_N_ROOTS      =  3         Do 3 states
       CIS_SINGLETS     =  true      Do do singlets
       CIS_TRIPLETS     =  false     Don’t do Triplets
    $end
    ```

???+ example "示例 7.3：在单次计算中评估多个电子态的梯度。
输出参考 DFT 态和 SF-TDDFT 态的梯度。"
    ```qchem
    $molecule
    0 3
       C   0.000000     0.000000     0.106788
       H  -0.989216     0.000000    -0.320363
       H   0.989216     0.000000    -0.320363
    $end
    
    $rem
    job_type force
    method       B5050LYP
    SYM_IGNORE  True
    UNRESTRICTED TRUE
    BASIS       6-31G*
    SCF_CONVERGENCE 8
    spin_flip true
    CIS_N_ROOTS       4
    CIS_STATE_MULTIGRAD = 2
    $end
    
    ```

## 7.2.2.3 无规相位近似

无规相位近似（Random Phase Approximation, RPA）[[148]](../bib_references/bib.md#bib139)
，亦称含时 Hartree-Fock（TD-HF）理论，是 CIS 之外另一种用于激发态非关联计算的替代方案。通过 RPA
*$rem* 变量即可请求 RPA 计算，该变量在第 [7.2.4.1](sec_CIS-jobcontrol.md#sec:CIS-jobcontrol:Basic)
节中描述。

在计算振子强度方面，RPA 具有某些优势，*例如*严格满足 Thomas-Reike-Kuhn 求和规则，

其单重激发能的精度与 CIS 大致相当，但对三重态则较差。RPA 能量不是变分的，在激发态势能面上移动时，该方法偶尔会遇到奇点（源于底层参考态中的三重态不稳定性），从而使 RPA 方程无法数值求解[[268]](../bib_references/bib.md#bib269)

。在 **Q-Chem** 中，这些不稳定性通常伴随一条错误信息，指出在 RPA 方程中检测到虚根。
这在 CIS 计算中在数学上是不可能出现的，因为 CIS 将激发能问题与稳定性问题解耦合。

## 7.2.2.4 DFT/CIS

DFT/CIS[[490]](../bib_references/bib.md#bib498)
 是一种半经验方法，它采用 CIS 类似的形式体系，但用 Kohn-Sham 轨道取代 Hartree-Fock 轨道。
这得益于 Kohn-Sham 轨道带来的额外关联能，并且（可能更重要的是）与通常未束缚（unbound）的 Hartree-Fock 虚拟轨道相比，其轨道能量差
$\varepsilon_{a}-\varepsilon_{i}$ 更接近激发能，且其束缚的（bound）虚拟轨道能更好地近似定域激发态[[572]](../bib_references/bib.md#bib586)

。
配合某些半经验修正，DFT/CIS 显著改进了传统的基于 Hartree–Fock 的 CIS。
**Q-Chem** 中提供两种 DFT/CIS 哈密顿量的参数化方案：Grimme 的原始方案[[490]](../bib_references/bib.md#bib498)
，专为配合 B3LYP 泛函使用而设计；以及为 CAM-B3LYP 设计的新参数化方案[[879]](../bib_references/bib.md#bib914)

。后者（CAM-B3LYP/CIS）的实现具有专门针对精确再现 X 射线谱的参数化，
而 B3LYP/CIS 仅适用于价激发。
参数化的本质将 DFT/CIS 的使用限制在上述两种泛函，并且主要用于两种基组。
CAM-B3LYP/CIS 方法针对 def2-TZVPD 基组参数化，而 B3LYP/CIS 针对 TZVP 基组参数化。

DFT/CIS 方法由作业控制变量 DFTCIS 和 DFTCIS_PARAMS 控制，详见第 [7.2.4.1](sec_CIS-jobcontrol.md#sec:CIS-jobcontrol:Basic)
节。

???+ example "示例 7.4：用 DFT/CIS（B3LYP/CIS）计算水的前五个单重激发态。"
    ```qchem
    $molecule
    0 1
    O
    H  1 0.960652
    H  1 0.960652 2 103.913458
    $end
    
    $rem
    JOBTYPE        = sp
    METHOD         = b3lyp
    UNRESTRICTED   = false
    BASIS          = TZVP
    DFTCIS         = true
    DFTCIS_PARAMS  = 1 !0=CIS, 1=B3LYP/CIS, 2=CAM-B3LYP/CIS
    CIS_N_ROOTS    = 5
    CIS_TRIPLETS   = false
    SCF_ALGORITHM  = diis
    $end
    
    ```

芯层/价层分离（core/valence separation, CVS）近似已实现并可与 DFT/CIS 方法配合使用，因此该方法可用于计算元素 K、L、M 边上的芯层激发谱[[879]](../bib_references/bib.md#bib914)

。
L 边谱需要自旋-轨道耦合，相关讨论见第 [7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc)
节。
该节中的示例 [7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc)
演示了包含自旋-轨道耦合的 L 边谱 DFT/CIS 计算。
本示例生成的 **Q-Chem** 输出文件可由 **pySETSOC** 程序[[882]](../bib_references/bib.md#bib1655)
读取，用于构造并对角化 Breit-Pauli 哈密顿量，从而得到耦合后的激发态和振子强度[[881]](../bib_references/bib.md#bib916)
。
