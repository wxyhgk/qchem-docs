---
title: "10.11.4 其他与磁场相关的性质"
---

## 10.11.4 其他与磁场相关的性质

(July 4, 2026)

除核磁共振（NMR）化学屏蔽常数和自旋-自旋耦合常数之外，**Q-Chem** 还可计算其他一些磁学性质，包括

- •

超精细相互作用张量（hyperfine interaction tensors），
- •

由电场梯度（Electric Field Gradient, EFG）张量得到的核四极相互作用（nuclear quadrupole interaction），以及
- •

电子 *g*-张量（electronic *g*-tensor），

## 10.11.4.1 超精细相互作用

超精细相互作用张量描述未配对电子自旋与原子核自旋能级之间的相互作用：

<a id="eq:hyperfine-hamiltonian"></a>
$$
\hat{H}_{\text{HFI}}/h=\mathbf{\hat{S}}\cdot\mathbf{A}\cdot\mathbf{\hat{I}}, \tag{10.119}
$$

该张量可分解为费米接触（Fermi Contact, FC）项、自旋-偶极（spin-dipole, SD）项以及轨道塞曼/自旋-轨道耦合（OZ/SOC）项：

<a id="eq:hyperfine-tensor"></a>
$$
A_{ab}^{\text{tot}}(N)=A_{ab}^{\text{FC}}(N)\delta_{ab}+A_{ab}^{\text{SD}}(N)+A_{ab}^{\text{OZ/SOC}}, \tag{10.120}
$$

其中费米接触（FC）贡献为

<a id="eq:hyperfine-fermi-contact"></a>
$$
A^{\text{FC}}(N)=\frac{\alpha}{2}\frac{1}{S}\frac{8\pi}{3}g_{\text{e}}g_{N}\mu_{N}\sum_{\mu\nu}P_{\mu\nu}^{\alpha-\beta}\left\langle\chi_{\mu}|\delta(\mathbf{r}_{N})|\chi_{\nu}\right\rangle \tag{10.121}
$$

自旋-偶极（SD）贡献为

<a id="eq:hyperfine-spin-dipole"></a>
$$
A_{ab}^{\text{SD}}(N)=\frac{\alpha}{2}\frac{1}{S}g_{e}g_{N}\mu_{N}\sum_{\mu\nu}P_{\mu\nu}^{\alpha-\beta}\left\langle\chi_{\mu}\left|\frac{3r_{N,a}r_{N,b}-\delta_{ab}r_{N}^{2}}{r_{N}^{5}}\right|\chi_{\nu}\right\rangle \tag{10.122}
$$

式中 $N$ 为某个原子核。轨道塞曼/自旋-轨道耦合交叉项（OZ/SOC）目前尚不可用。

超精细相互作用张量对所有基于自洽场（SCF）的方法均可用，但要求采用非限制（unrestricted，而非限制开壳层 restricted open-shell）参考。后 Hartree-Fock（Post-HF）方法不可用。

激发态（CIS/TDA-TDDFT）单重态–三重态超精细耦合常数同样可以计算，但其输出格式与基态非限制方法的结果不同。激发态耦合常数按每一对激发态以及每个自旋算符 $S_{x},S_{y},S_{z}$ 的 FC 与 SD 贡献分别打印。对于该方法，通过对核自旋态取平均得到最终的耦合贡献。[[44]](../bib_references/bib.md#bib961)

## 10.11.4.2 核四极相互作用

探测分子中各个原子核所处环境的另一种灵敏探针是核四极相互作用（Nuclear Quadrupole Interaction, NQI），它衡量核四极矩与局部电场梯度的相互作用：

<a id="eq:nqi-hamiltonian"></a>
$$
\hat{H}_{\text{NQI}}/h=\mathbf{\hat{I}}\cdot\mathbf{Q}\cdot\mathbf{\hat{I}}, \tag{10.123}
$$

<a id="eq:nqi-tensor"></a>
$$
\displaystyle Q_{ab}(N) \tag{10.124}
$$

式中 $N$ 为某个原子核。对该张量对角化可得到三个主值，按 $|Q_{1}|\leq|Q_{2}|\leq|Q_{3}|$ 排序，它们是不对称参数（asymmetry parameter）eta 的组成部分：

<a id="eq:nqi-eta"></a>
$$
\eta=\frac{Q_{1}-Q_{2}}{Q_{3}} \tag{10.125}
$$

## 10.11.4.3 电子 *g*-张量

电子 *g*-张量描述未配对电子自旋与外磁场的耦合，由唯象哈密顿量表示

<a id="Ch10.E126"></a>
$$
\hat{H}^{\text{g-tensor}}=\mu_{\text{B}}\mathbf{S}\cdot\mathbf{g}\cdot\mathbf{B}, \tag{10.126}
$$

其中 $\mu_{\text{B}}$ 为玻尔磁子（Bohr magneton），$\mathbf{S}$ 为分子内禀自旋矢量，$\mathbf{B}$ 为入射磁场矢量。

$g$-张量由自旋–塞曼（spin–Zeeman）项以及 $g$-张量平移（shift）组成，后者包括相对论质量校正 $\mathbf{g}^{\text{rmc}}$、抗磁自旋-轨道耦合 $\mathbf{g}^{\text{dso}}$ 和顺磁自旋–轨道耦合 $\mathbf{g}^{\text{pso}}$ 项：

<a id="Ch10.E127"></a>
$$
\mathbf{g}=g_{\text{e}}\mathbf{I}+\mathbf{g}^{\text{rmc}}+\mathbf{g}^{\text{dso}}+\mathbf{g}^{\text{pso}}\;. \tag{10.127}
$$

对于自旋–塞曼项，其贡献是各向同性的，等于自由电子 $g$-因子 $g_{\text{e}}$。相对论相互作用项按照 Breit-Pauli *ansatz* 以微扰方式加入，得到如下表达式。相对论质量校正平移项 $g^{\text{rmc}}$ 为

<a id="Ch10.E128"></a>
$$
g^{\text{rmc}}_{pq}=-\frac{\alpha^{2}g_{\text{e}}}{2S}\delta_{pq}\sum_{\mu\nu}P^{\alpha-\beta}_{\mu\nu}T_{\mu\nu} \tag{10.128}
$$

其中 $\alpha$ 为精细结构常数，$P^{\alpha-\beta}_{\mu\nu}$ 为自旋密度矩阵，$T_{\mu\nu}$ 为动能积分。抗磁自旋-轨道项 $g^{\text{dso}}$ 目前尚未在 **Q-Chem** 中实现，因此被排除在外；不过对于较轻元素或第一至第二过渡系的金属体系，该项通常也只具有次要的重要性。

顺磁自旋-轨道耦合项 $g^{\text{pso}}$ 是微扰级数中的二阶项，但构成了 $g$-张量平移的主要贡献

<a id="Ch10.E129"></a>
$$
g^{\text{pso}}=\frac{1}{\alpha S}\sum_{N}\frac{\left\langle\Psi_{0}\left|h^{\text{SO}}\right|\Psi_{N}\right\rangle\left\langle\Psi_{N}\left|h^{\text{OZ}}\right|\Psi_{0}\right\rangle}{E_{N}-E_{0}} \tag{10.129}
$$

其中 $h^{\text{SO}}$ 为自旋-轨道耦合相互作用，默认采用自旋-轨道平均场（spin-orbit mean-field）方法，[[364]](../bib_references/bib.md#bib370)
 而 $h^{\text{OZ}}$ 为轨道塞曼相互作用，

<a id="Ch10.E130"></a>
$$
h^{\text{OZ}}=\mu_{\text{B}}\mathbf{L}\cdot\mathbf{B}\;, \tag{10.130}
$$

其中 $\mathbf{L}$ 为角动量。

在本实现中，顺磁自旋-轨道耦合项采用响应理论（response theory）方法进行求值，该方法最早由 Gauss *et al.* 演示，[[432]](../bib_references/bib.md#bib444)

但其计算方法遵循 **Q-Chem** 极化率代码中所使用的方案。[[978]](../bib_references/bib.md#bib1019)

目前 $g$-张量仅在耦合簇单双（CCSD）级别上实现。

## 10.11.4.4 作业控制与示例

只需在 *$rem* 段中设置一个关键字即可激活磁学性质模块。

G_TENSOR

### `MAGNET`

> **激活磁学性质模块。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE（或 0）
>     * 不激活磁学性质模块。
>     * TRUE（或 1）
>     * 激活磁学性质模块。
> * **建议**：无。

所有其他选项均通过 *$magnet* 输入段进行控制，该段与 *$rem* 段具有相同的键-值格式（见第 [3.4](../ch03_inputs/sect_rem.md) 节）。
当前选项有：

### `Hyperfine`

> **激活超精细相互作用张量的计算。输入段：$magnet**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE（或 0）
>     * 不计算超精细相互作用张量。
>     * TRUE（或 1）
>     * 计算超精细相互作用张量。
> * **建议**：无。由于该性质需要自旋密度，对于限制（RHF）参考而言没有意义。仅支持 UHF（不支持 ROHF）。

### `Electric`

> **激发电场梯度张量的计算。输入段：$magnet**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE（或 0）
>     * 不计算 EFG 张量和核四极参数。
>     * TRUE（或 1）
>     * 计算 EFG 张量和核四极参数。
> * **建议**：无。

对于超精细张量和 EFG 张量，均会自动计算所有原子核的结果。

### `Hyperfine_Full`

> **激活激发态超精细耦合常数的计算。输入段：$magnet**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * False（或 0）
>     * 不计算激发态超精细耦合常数。
>     * True（或 1）
>     * 计算激发态超精细耦合常数。
> * **建议**：无。

### `Hyperfine_Full_NRoots`

> **指定激发态超精细计算的根数。输入段：$magnet**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * n
>     * 计算最低 n 个 CIS/TDA-TDDFT 态之间的超精细耦合常数。
> * **建议**：无。

### `Hyperfine_Full_Root_Offset`

> **指定激发态超精细计算根数的偏移量。输入段：$magnet**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * m
>     * 计算最低 n 个 CIS/TDA-TDDFT 态之间的超精细耦合常数，从第 m
>     * ${}^{\text{th}}$
>     * 个根开始。
> * **建议**：无。

### `Hyperfine_Full_Singlet_Other_Singlet`

> **指定是否计算单重激发态之间的耦合。输入段：$magnet**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * False（或 0）
>     * 不计算单重态之间的激发态超精细耦合常数。
>     * True（或 1）
>     * 计算单重态之间的激发态超精细耦合常数。
> * **建议**：无。

### `Hyperfine_Full_Triplet_Other_Triplet`

> **指定是否计算三重激发态之间的耦合。输入段：$magnet**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * False（或 0）
>     * 不计算三重态之间的激发态超精细耦合常数。
>     * True（或 1）
>     * 计算三重态之间的激发态超精细耦合常数。
> * **建议**：无。

通过在 *$rem* 段中指定 G_TENSOR 关键字来激活 $g$-张量的计算。
示例 [10.11.4.4](#ex:CCSD-gtensor) 演示了水阳离子的 $g$-张量计算。

MAGNET

### `G_TENSOR`

> **激活 $g$-张量计算。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE（或 0）
>     * 不计算 $g$-张量
>     * TRUE（或 1）
>     * 计算 $g$-张量。
> * **建议**：无。

???+ example "示例 10.62：计算甘氨酸阳离子的超精细张量和 EFG 张量。"
    ```qchem
    $molecule
       1 2
       N     0.0000000000     0.0000000000     0.0000000000
       C     1.4467530000     0.0000000000     0.0000000000
       C     1.9682482963     0.0000000000     1.4334965024
       O     1.2385450522     0.0000000000     2.4218667010
       H     1.7988742211    -0.8959881458    -0.5223754133
       H     1.7997303368     0.8930070757    -0.5235632630
       H    -0.4722340827    -0.0025218132     0.8996536532
       H    -0.5080000000     0.0766867527    -0.8765335943
       O     3.3107284257    -0.0000000000     1.5849828121
       H     3.9426948542    -0.0000000000     0.7289954096
    $end
    
    $rem
       METHOD                hf
       BASIS                 def2-sv(p)
       SCF_CONVERGENCE       11
       THRESH                14
       MAGNET                true
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    $magnet
       HYPERFINE  true
       ELECTRIC   true
    $end
    ```

???+ example "示例 10.63：计算水阳离子的 $g$-张量。"
    ```qchem
    $molecule
       1 2
       O    0.00000000   0.00000000   0.13475163
       H    0.00000000  -1.70748899  -1.06930309
       H    0.00000000   1.70748899  -1.06930309
    $end
    
    $rem
       INPUT_BOHR      = true
       METHOD          = ccsd
       BASIS           = 3-21g
       CC_REF_PROP     = true
       G_TENSOR        = true
       N_FROZEN_CORE   = 0
       NO_REORIENT     = true
       SCF_CONVERGENCE = 12
       CC_CONVERGENCE  = 12
       POINT_GROUP_SYMMETRY = false
    $end
    
    $gauge_origin
    0.000000 0.000000  0.0172393
    $end
    ```

激发态超精细耦合常数（HFC）值的打印格式为

> `Nucleus: IDX`
> 
> 
> …
> 
> 
> `STATE1 / STATE2`
> 
> 
> `FC: S_x_contribution S_y_contribution S_z_contribution`
> 
> 
> `SD: S_x_contribution S_y_contribution S_z_contribution`
> 
> 
> …

???+ example "示例 10.64：计算芘-二甲基苯胺（Pyrene-Dimethylaniline）自由基对的激发态超精细耦合常数。"
    ```qchem
    $molecule
       READ    pydma_xyz.txt
    $end
    
    $rem
       EXCHANGE             wb97x-d3
       BASIS                def2-svpd
       CIS_SINGLETS         true
       CIS_TRIPLETS         true
       CIS_MULLIKEN         true
       CIS_N_ROOTS          15        ! 15 TDA-TDDFT roots for each spin state
       RPA                  false
       MAGNET               true      ! Turn on magnetman
       CC_PRINT_PREC        12        ! Print precision affects precision of printed hfc
       POINT_GROUP_SYMMETRY false
       CIS_MAX_CYCLES       500
       SCF_MAX_CYCLES       500
       SCF_CONVERGENCE      10
       CIS_CONVERGENCE      8
       XC_GRID              3
    $end
    
    $magnet
       HYPERFINE_FULL                       true  ! Activate excited state hfc calculation
       HYPERFINE_FULL_NROOTS                30    ! Calculate all roots
       HYPERFINE_FULL_SINGLET_OTHER_SINGLET false ! Neglect singlet-singlet couplings
       HYPERFINE_FULL_TRIPLET_OTHER_TRIPLET false ! Neglect triplet-triplet couplings
    $end
    ```
