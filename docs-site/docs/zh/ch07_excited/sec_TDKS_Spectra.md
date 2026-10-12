---
title: "7.4.3 吸收光谱的计算"
---

## 7.4.3 吸收光谱的计算

（2026 年 7 月 4 日）

## 7.4.3.1 理论

沿 $\kappa$ 方向偏振的光（$\kappa\in\{x,y,z\}$）的吸收截面 $\sigma_{\kappa\kappa}(\omega)$ 可由频率相关极化率 $\alpha_{\kappa\kappa}(\omega)$ 的虚部（$\Im$）获得:[[1578]](../bib_references/bib.md#bib1641)

<a id="Ch7.E65"></a>

$$
\sigma_{\kappa\kappa}(\omega)=\left(\frac{4\pi\omega}{c}\right)\Im\bigl{[}\alpha_{\kappa\kappa}(\omega)\bigr{]}\;. \tag{7.65}
$$

在电偶极近似下，旋转平均后的吸收光谱 $A(\omega)$ 即为

<a id="eq:RT-TDDFT_spectrum"></a>

$$
A(\omega)=\tfrac{1}{3}\bigl{[}\sigma_{xx}(\omega)+\sigma_{yy}(\omega)+\sigma_{zz}(\omega)\bigr{]}\;. \tag{7.66}
$$

频率相关极化率张量 $\bm{\alpha}(\omega)$ 的各分量 $\alpha_{\kappa\lambda}(\omega)$ 可由时间依赖偶极矩分量 $\mu_{\kappa}(t)$ 的傅里叶变换（$\mathcal{F}$）获得，其中微扰场 $\mathcal{E}_{\lambda}$ 沿 $\lambda$ 方向:[[1578]](../bib_references/bib.md#bib1641)

<a id="eq:TDKS-FT"></a>

$$
\alpha_{\kappa\lambda}(\omega)=\frac{\mathcal{F}\bigl{[}\mu_{\kappa}(t)\bigr{]}}{\mathcal{F}\bigl{[}\mathcal{E}_{\lambda}(t)\bigr{]}}\;. \tag{7.67}
$$

要计算式 ([7.66](#eq:RT-TDDFT_spectrum)) 中的光谱，需要沿 $x$、$y$、$z$ 三个方向分别施加微扰，否则若某些激发的跃迁偶极矩严格垂直于所施加的外场，其矩阵元 $\langle\Psi_{n}|\mathcal{E}_{\lambda}|\Psi_{0}\rangle$ 将为零，从而导致这些激发缺失。不过，这三个微扰 $\mathcal{E}_{x}$、$\mathcal{E}_{y}$ 和 $\mathcal{E}_{z}$ 可以在单次计算中同时施加，以生成一个叠加态，其中包含从基态出发的所有可能激发。

## 7.4.3.2 傅里叶变换脚本

提供了两个不同的脚本，用于在 TDKS 模拟完成后获得光谱：

- •

`$QC/bin/tools/tdks_fft.py`
- •

`$QC/bin/tools/tdks_pade.py`

第一个脚本直接使用式 ([7.67](#eq:TDKS-FT)) 中的傅里叶变换方法，而第二个脚本利用 Padé 近似，以更短的传播时间获得可比拟的光谱。[[566]](../bib_references/bib.md#bib585)

这些脚本可以按如下方式运行：

> ```qchem
> $QC/bin/tools/tdks_fft.py output spectrum.txt
> $QC/bin/tools/tdks_pade.py output spectrum.txt
> ```

处理脚本生成的 `spectrum.txt` 文件将包含两列：频率（eV）和强度（任意单位）。
这些数据可以作为 $(x,y)$ 图进行可视化，以查看光谱。

???+ example "示例 7.35: 使用连续波（CW）场和复吸收势（CAP）的 TDKS 计算"
    ```qchem
    $molecule
       0 1
       H    0.000000   0.000000   0.000000
       H    0.000000   0.000000   0.750000
    $end
    
    $rem
       BASIS                6-31G
       METHOD               lrc-wpbe
       TDKS                 true
       LRC_DFT              true
       OMEGA                300
       SCF_CONVERGENCE      9
       INTEGRAL_SYMMETRY    false
    $end
    
    $tdks
       DT                   0.10
       MAXITER              5
       PROPAGATOR           MMUT
       FIELD_VECTOR         1 1 1
       FIELD_TYPE           cw
       FIELD_FREQUENCY      1.55
       FIELD_AMP            0.0001
       DO_CAP               true
       CAP_TYPE             atom_centered_spherical
       CAP_R0               18.5  ! units are bohr
       CAP_ETA              0.1   ! units are hartree/bohr^2
    $end
    ```

## 7.4.3.3 偶极过滤（Dipole Filtering）

TDKS 宽带光谱计算中一个重要但未被充分认识的方面是，它们可能被对应于向高能虚分子轨道（MO）跃迁的连续态伪影所污染。[[1514]](../bib_references/bib.md#bib1584)

对于核心能级（core-level）光谱而言，这可能尤为棘手，因为某个 X 射线吸收边可能出现源自更低能量吸收边的伪影。
例如，N(1s) $\to$ 连续态的跃迁可能出现在与由 O(1s) $\to$ 价层跃迁构成的氧 K 边相当的能量处。[[566]](../bib_references/bib.md#bib585)

这一点令人遗憾，因为 X 射线光谱学是实时方法一个潜在有用的应用领域，而逐态方法（如 LR-TDDFT 或任何其他基于本征值的方法）可能需要计算数百个单独的激发态才能得到收敛的光谱。TDKS 方法几乎总是（显著地）比 LR-TDDFT 更昂贵，[[566]](../bib_references/bib.md#bib585)

但前者不存在后者所面临的大内存瓶颈。

幸运的是，出现在 TDKS 光谱中的人为态可以通过偶极过滤技术加以消除，[[1514]](../bib_references/bib.md#bib1584)

尽管这确实需要事先对预期出现的跃迁有一定了解。关键在于认识到偶极矩是密度矩阵的线性函数，

<a id="Ch7.E68"></a>

$$
\mu_{\lambda}(t)=\text{tr}\big{[}\mathbf{P}(t)\;\mathbf{D}_{\lambda}(t)\big{]}\;. \tag{7.68}
$$

这里，$\lambda\in\{x,y,z\}$ 表示偶极矩的笛卡尔分量，$\mathbf{D}_{\lambda}$ 是偶极矩算符 $\hat{\mu}_{\lambda}$ 在 MO 基组下的矩阵表示。对占位 MO $k$ 的求和使我们能够将 $\mu_{\lambda}$ 分解为来自每个 MO 的独立贡献。为此，定义矩阵

<a id="Ch7.E69"></a>

$$
\mathbf{D}_{\lambda,k}=\left(\begin{array}[]{ccccc}0&\cdots&(\mathbf{D}_{\lambda})_{1,k}&\cdots&0\\
\vdots&&\vdots&&\vdots\\
(\mathbf{D}_{\lambda})_{k,1}&\cdots&(\mathbf{D}_{\lambda})_{k,k}&\cdots(\mathbf{D}_{\lambda})_{k,n_{\text{occ}}}\\
\vdots&&\vdots&&\vdots\\
0&\cdots&(\mathbf{D}_{\lambda})_{n_{\text{occ}},k}&\cdots&0\\
\end{array}\right) \tag{7.69}
$$

其中除 $\mathbf{D}_{\lambda}$ 的第 $k$ 行和第 $k$ 列之外的所有元素均被置为零。于是

<a id="eq:dipole-filter"></a>

$$
\mu_{\lambda}(t)=\sum_{k}^{\text{occ}}\mu_{\lambda,k}(t) \tag{7.70}
$$

其中

<a id="Ch7.E71"></a>

$$
\mu_{\lambda,k}(t)=\text{tr}\big{[}\mathbf{P}(t)\;\mathbf{D}_{\lambda,k}(t)\big{]}\;. \tag{7.71}
$$

对时间序列 $\mu_{\lambda,k}(t)$ 取傅里叶变换，即可得到第 $k$ 个 MO 的光谱贡献，而所有此类贡献之和便给出了完整的 TDKS 光谱。这一步骤不必逐个轨道进行；相反，可以将若干 MO 分组的贡献加在一起，代表式 ([7.70](#eq:dipole-filter)) 中求和的不同划分方式。例如，通过让对 $k$ 的求和仅包含 O(1s) 轨道，就可以获得不含 N(1s) $\to$ 连续态跃迁污染的氧 K 边光谱。

上述技术是将完整 TDKS 光谱分解为各个占位 MO 或其分组贡献的一种方式。可以计算任意分组，但只有当这些 MO 分组为非不相交（non-disjoint）时，各傅里叶变换之和才等于完整的 TDKS 光谱。通过这种方式，可以将不同占位 MO 的影响从光谱中剔除，既用于查找（并去除）伪影，也用于通过确定谱峰来源的占位 MO 来指认光谱特征。

偶极过滤通过在 *$tdks* 输入段中添加关键字 **active_groups** 来实现。
其格式示例为

```qchem
¯         active_groups  k1 k2 k3 | k4 k5 | k6 k7 k8
```

这请求将光谱分解为三组占位 MO，第一组的指标为 $\{k_{1},k_{2},k_{3}\}$，
第二组为 $\{k_{4},k_{5}\}$，第三组为 $\{k_{6},k_{7},k_{8}\}$。（各分组的指标之间以“`|`”符号分隔。）
对于非限制（unrestricted）计算，必须分别列出 active groups 的 $\alpha$ 自旋和 $\beta$ 自旋 MO 指标，
使用关键字 **active_alpha_groups** 和 **active_beta_groups**，二者的格式均与 **active_groups** 相同。

### `active_groups`

> **为偶极过滤指定活跃 MO 指标分组。输入段：$tdks**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **选项**:
>     * $k_{1}~{}k_{2}\cdots\text{|}k_{3}~{}k_{4}\cdots$: 定义分组 $\{k_{1},k_{2},\ldots\}$ 以及 $\{k_{3},k_{4},\ldots\}$。
> * **建议**: 按需使用。除了完整的偶极矩函数 $\bm{\mu}(t)$ 之外，每个分组的独立偶极矩函数也会被写入临时（scratch）目录。对于非限制 SCF 计算，请改用 active_alpha_groups 和 active_beta_groups。

以下示例演示了如何将 TiO${}_{2}$ 的吸收光谱分解为来自 Ti(1s)、Ti(2s)、O(1s) 和 Ti(2p) 轨道的贡献。要设置此计算，必须先执行一次 SCF 计算，以确定哪些指标对应于所关注的 MO。

???+ example "示例 7.36: TDKS 偶极过滤示例。注意，对于真实模拟，传播时间（ maxiter ）需要长得多。"
    ```qchem
    $comment
    TDKS with dipole filtering
    Decompose the spectrum into contributions from active groups of occupied MOs,
       1    |    2    |  3 4  |  5 6 7
     Ti(1s)    Ti(2s)   O(1s)   Ti(2p)
    $end
    
    $molecule
    0 1
    Ti  0.0000000 0.000000  0.6131572
    O  -1.3586178 0.000000 -0.3066726
    O   1.3586178 0.000000 -0.3066726
    $end
    
    $rem
    exchange src1-r1
    basis    def2-tzvpd
    tdks     true
    thresh   12
    scf_convergence 8
    sym_ignore      true
    $end
    
    $tdks
    active_groups  1 | 2 | 3 4 | 5 6 7
    dt 0.02
    maxiter 10
    Propagator MMUT
    field_vector 1 1 1
    field_type delta
    field_amp 0.0001
    $end
    
    ```

带偶极过滤的 TDKS 计算的相关输出会放置在临时目录中一个名为
`$QCSCRATCH/tdks-dipole` 的子目录下。计算完成后，该目录会被复制到包含输入文件和输出文件的同一目录下，并重命名为 `outFileName.tdks-dipole`，其中 `outFileName` 是 **Q-Chem** 输出文件的文件名。
对于限制（restricted）SCF 计算，`tdks-dipole` 目录中包含一个名为 `full.dat` 的文件，其内容为完整的偶极矩函数，按分量 $\mu_{x}(t)$、$\mu_{y}(t)$ 和 $\mu_{z}(t)$ 排列。在同一目录中还有名为
`group.n.dat` 的文件，其包含相同类型的信息，但仅限于第 $n$ 组 MO。对于非限制 SCF 计算，
`full.dat` 会被 `full-alpha.dat` 和 `full-beta.dat` 取代，而 `group.n.dat` 则被
`group-alpha.n.dat` 和 `group-beta.n.dat` 取代。可以对这些 `.dat` 文件中的数据分别进行傅里叶变换，以获得每个 MO 分组的光谱贡献。如果 MO 列表中没有遗漏也没有重复，那么各分组的谱线之和应等于完整光谱。例如，对于非限制 TDKS 计算，`full-alpha.dat` 和 `full-beta.dat` 共同提供了完整光谱。
