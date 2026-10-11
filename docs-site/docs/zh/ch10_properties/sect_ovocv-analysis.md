---
title: "10.3.4 用于化学价键分析的占据–虚轨道（Occupied–Virtual Orbitals for Chemical Valence Analysis）"
---

## 10.3.4 用于化学价键分析的占据–虚轨道

（2026 年 7 月 4 日）

## 10.3.4.1 概述

在平均场理论（如 HF 和 KS-DFT）中，量子态的能量完全由一阶约化密度矩阵（1-PDM）**P** 决定。因此，任意两个量子态之间的能量差可以完全由密度差 $\Delta\textbf{P}$ 决定。通过对 $\Delta\textbf{P}$ 进行本征分解，可以得到关于轨道相互作用的富有启发性的解释，由此得到的轨道称为化学价键自然轨道（natural orbitals for chemical valence, NOCV）[[954]](../bib_references/bib.md#bib995)
。NOCV 以成对的形式 $\{|\psi_{\pm i}\rangle\}$ 出现，对应的本征值为 $\pm\lambda_{i}$。然而，NOCV 是占据轨道与虚轨道的混合，这使得它们难以解释；此外，每对 NOCV 所对应的电荷量也被错误地放大了[[1250]](../bib_references/bib.md#bib1300)
。作为对 NOCV 的改进，最近提出的化学价键占据-虚轨道（occupied-virtual orbitals for chemical valence, OVOCV）[[1248]](../bib_references/bib.md#bib1302)
，其构造方法总结如下。

## 10.3.4.2 任意两个单行列式态之间的 OVOCV 分析

在初态 $I$ 的占据轨道与虚轨道的正交归一基下，$\hat{P}_{I}$ 的矩阵表示为

<a id="eq:P_I"></a>

$$
{\color[rgb]{0,0,0}P_{I}}=\begin{pmatrix}1&0\\
0&0\end{pmatrix} \tag{10.52}
$$

其中 $1$ 的维度为 $o\times o$，对角零矩阵的维度为 $v\times v$。在同一基下，末态密度算符 $P_{F}$ 的表示可由 $P_{I}$ 构造为 $P_{F}=\exp\{X\}P_{I}\exp\{-X\}$，其中

<a id="Ch10.E53"></a>

$$
X=\begin{pmatrix}0&X_{ov}\\
-X_{ov}^{T}&0\end{pmatrix} \tag{10.53}
$$

对 $X_{ov}$ 进行奇异值分解（SVD），

<a id="Xov_SVD"></a>

$$
X_{ov}=U\Sigma V^{T} \tag{10.54}
$$

其中 $\dim(U)=o\times o,\dim(\Sigma)=o\times v,\dim(V)=v\times v$，则可将 $\Delta P$ 写为

<a id="eq:delta_p"></a>

$$
\Delta P=\begin{pmatrix}U&0\\
0&V\end{pmatrix}\begin{pmatrix}-\sin^{2}{\Sigma^{\prime}}&-\cos{\Sigma^{\prime}}\sin{\Sigma^{\prime}}&0\\
-\sin{\Sigma^{\prime}}\cos{\Sigma^{\prime}}&\sin^{2}{\Sigma^{\prime}}&0\\
0&0&0\end{pmatrix}\begin{pmatrix}U^{T}&0\\
0&V^{T}\end{pmatrix} \tag{10.55}
$$

其中 $\Sigma^{\prime}=\mathrm{diag}(\sigma_{1},\sigma_{2},...,\sigma_{o})$，对角零矩阵的维度为 $v-o$（假设 $o<v$，这对大多数实际计算而言都成立）。

由于 $\Delta P$ 在 $U,V$ 表示下的各个分块中均被对角化，自然地，我们将这一选择定义为化学价键占据-虚轨道（Occupied-Virtual Orbitals for Chemical Valence, OVOCVs）。

<a id="A3.S8.EGx78"></a>

$$
\displaystyle|\phi^{i}_{\text{occ}}\rangle \tag{10.56}
$$

具体而言，$|\phi^{i}_{\text{occ}}\rangle$ 和 $|\phi^{i}_{\text{vir}}\rangle$ 分别是第 $i$ 对 OVOCV 的占据轨道和虚轨道。由于 OVOCVs 是通过对正交归一基进行幺正变换得到的，它们仍然构成一组正交归一基（维度要小得多，因为与密度形变无关的虚轨道已被剔除）。

在 OVOCV 基下，$\Delta P$ 为：

<a id="eq:delta_p_ovocv"></a>

$$
\Delta P=\begin{pmatrix}-\sin^{2}{\Sigma^{\prime}}&-\cos{\Sigma^{\prime}}\sin{\Sigma^{\prime}}\\
-\sin{\Sigma^{\prime}}\cos{\Sigma^{\prime}}&\sin^{2}{\Sigma^{\prime}}\end{pmatrix} \tag{10.58}
$$

（对角的）oo 分块是负半定的，对应于从 $o$ 个初始占据的 OVOCV 能级中第 $i$ 个能级损失 $\sin^{2}\sigma_{i}$ 个电子。与之相对，（对角的）vv 分块数值相等、符号相反，对应于将 $\sin^{2}\sigma_{i}$ 个电子提升（promotion）至 $o$ 个初始虚的 OVOCV 能级中第 $i$ 个能级。

任意两个单行列式态之间的能量差可表示为

<a id="Ch10.E59"></a>

$$
\Delta E=\text{Tr}\{\hat{F}^{\text{eff}}\Delta\hat{P}\}, \tag{10.59}
$$

其中 $\hat{F}^{\text{eff}}$ 是有效 Fock 算符，由对两态之间密度矩阵的线积分（line-integral）得到。利用 $\Delta\hat{P}$ 在 OVOCV 基下的分解，我们有

<a id="Ch10.E60"></a>

$$
\displaystyle\Delta E \tag{10.60}
$$

OVOCV 分析是针对自旋极化计算编写的，因此必须设置 UNRESTRICTED = TRUE。

OVOCV_ANALYSIS

### `OVOCV_ANALYSIS`

> **执行 OVOCV 分析**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * 0
>     * 不进行 OVOCV 分析
>     * 1
>     * 进行 OVOCV 分析
> * **建议**: 无

OVOCV_QUADRATURE

### `OVOCV_QUADRATURE`

> **用于 $\hat{F}^{\text{eff}}$ 线积分的求积点（quadrature points）数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **取值选项**:
>     * -1
>     * 出于调试目的的调试输出
>     * 5
>     * 5 点求积
>     * 9
>     * 9 点求积
>     * 13
>     * 13 点求积
>     * 17
>     * 17 点求积
>     * 21
>     * 21 点求积
> * **建议**: 基态分析使用 5，激发态分析使用 9 或 13。增大求积点数可获得更高精度的 $\Delta E$

SAVE_OVOCV_INIT_DATA

### `SAVE_OVOCV_INIT_DATA`

> **为 OVOCV 分析保存初态数据**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * 0
>     * 不保存初态数据
>     * 1
>     * 保存初态数据
> * **建议**: 在初态计算中设置为 1

LOAD_OVOCV_INIT_DATA

### `LOAD_OVOCV_INIT_DATA`

> **加载初态数据用于 OVOCV 分析，然后以当前态作为末态执行 OVOCV 分析**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * 0
>     * 不加载初态数据
>     * 1
>     * 加载初态数据
> * **建议**: 在末态计算中设置为 1

OVOCV_THRESH

### `OVOCV_THRESH`

> **指定 OVOCV 保存所要求的显著性阈值**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **取值选项**:
>     * $N$
>     * 对能量降低的贡献超过
>     * $0.001\times N$
>     * kJ/mol 的 OVOCV 将被保存
> * **建议**: 无

SAVE_OVOCV

### `SAVE_OVOCV`

> **是否保存显著的 OVOCV**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * 0
>     * 不保存显著 OVOCV
>     * 1
>     * 保存显著 OVOCV
> * **建议**: 设置为 1 以保存 OVOCV。注意还需设置用于绘制 cube 文件的 REM 参数

???+ example "示例 10.10.16: 极化态与完全收敛的 SCF 态之间的 OVOCV 分析。"
    ```qchem
    $comment
    Calculate a polarized state
    $end
    
    $molecule
    -1 1
    --
    0 1
    C      -2.1241906261     0.4405879048    -0.6028769327
    H      -2.2759080470     0.1247332923    -1.6303256895
    H      -2.2970177347     1.4883974948    -0.3784045735
    C      -2.1383367135    -0.5060266611     0.4271962891
    H      -2.3004855320    -1.5544440597     0.1975704475
    H      -2.3216355550    -0.1916949240     1.4498166705
    --
    -1 1
    Pt     -0.1374350284    -0.0292366293    -0.0576671311
    Cl     -0.1541352882    -1.7330117528    -1.6304294395
    Cl      2.1808813192    -0.0260821423    -0.0234510188
    Cl     -0.2063937942     1.6741234771     1.5139773781
    $end
    
    $rem
    unrestricted        true
    method               wb97x-v
    scf_print_frgm       1
    sym_ignore           1
    symmetry             false
    basis                def2-svp
    ecp                  def2-ecp
    scf_algorithm        diis
    thresh               14
    incfock              0
    mem_total            16000
    scf_final_print      2
    scf_convergence      8
    frgm_method          stoll
    child_mp             true
    child_mp_orders      232
    ovocv_analysis       1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    unrestricted        true
    thresh              14
    scf_convergence     8
    scf_algorithm       diis
    method              wb97x-v
    basis               def2-svp
    ecp                 def2-ecp
    scf_guess           read
    sym_ignore          true
    symmetry            false
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    5
    ovocv_thresh        10000
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    ```

???+ example "示例 10.10.17: 具有 HF 密度的 DFT 态与具有 DFT 密度的 DFT 态之间的 OVOCV 分析。"
    ```qchem
    $comment
    SCF for fragmo to get initial density for HF
    $end
    
    $molecule
    1 2
    --
    0 1
    He 0 0 0
    --
    1 2
    He 0 0 3.0
    $end
    
    $rem
    method              hf
    scf_guess           fragmo
    frgm_method         stoll
    scf_convergence     7
    basis               6-31G**
    scf_algorithm       gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    internal_stability  true
    unrestricted        true
    $end
    
    @@@
    
    $comment
    HF calculation with frag density
    $end
    
    $molecule
    read
    $end
    
    $rem
    method              hf
    scf_guess           read
    scf_convergence     7
    basis               6-31G**
    scf_algorithm       gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    internal_stability  true
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $comment
    DFT calculation with HF density
    $end
    
    $molecule
    read
    $end
    
    $rem
    internal_stability  true
    unrestricted        true
    thresh              14
    scf_convergence     7
    scf_algorithm       gdm
    method              PBE
    basis               6-31G**
    scf_guess           read
    scf_max_cycles      500
    sym_ignore          true
    symmetry            false
    IQMOL_FCHK          False
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    17
    ovocv_thresh        500
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    ```

## 10.3.4.3 用于 OO-DFT 激发分析的 OVOCV 分析

随着针对非 aufbau（非构造原理）行列式的 SCF 算法的发展，通常可以用轨道优化密度泛函理论（Orbital-Optimized Density Functional Theory, OO-DFT）的单个 Slater 行列式来准确描述激发态，例如电荷转移态或双激发态。因此，使用 OVOCV 方法分析电子激发是自然而然的[[1247]](../bib_references/bib.md#bib1303)
，该方法给出由单对（双激发则为两对）OVOCV 对 $|\psi_{\text{D}}\rangle$（供体, donor）和 $|\psi_{\text{A}}\rangle$（受体, acceptor）所导致的主激发，并伴随许多极化对以解释轨道弛豫效应。
为了揭示轨道弛豫的重要性，我们引入一个中间冻结态（frozen state, FRZ），其密度是从基态密度 $\hat{P}_{\text{G}}$ 出发，通过供体轨道 $|\psi_{\text{D}}\rangle$ 完全排空和受体轨道 $|\psi_{\text{A}}\rangle$ 完全占据来构造的：

<a id="Ch10.E61"></a>

$$
\hat{P}_{\text{FRZ}}=\hat{P}_{\text{G}}-|\psi_{\text{D}}\rangle\langle\psi_{\text{D}}|+|\psi_{\text{A}}\rangle\langle\psi_{\text{A}}|. \tag{10.61}
$$

因此，$\hat{P}_{\text{G}}$ 与 $\hat{P}_{\text{FRZ}}$ 之间的联系揭示了主激发，而 $\hat{P}_{\text{FRZ}}$ 与 $\hat{P}_{\text{E}}$ 之间的联系则揭示了轨道弛豫效应。

OVOCV_EXCITE_ANALYSIS

### `OVOCV_EXCITE_ANALYSIS`

> **执行用于 OO-DFT 激发分析的 OVOCV 分析**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * 0
>     * 不进行 OVOCV OO-DFT 分析
>     * 1
>     * 进行 OVOCV OO-DFT 分析
> * **建议**: 无

OVOCV_EXCITE_TYPE

### `OVOCV_EXCITE_TYPE`

> **指定用于构造中间 FRZ 态的激发类型**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **取值选项**:
>     * 1
>     * 使用
>     * $\alpha$
>     * 空间中最大的 OVOCV 对构造 FRZ 态
>     * 2
>     * 使用
>     * $\beta$
>     * 空间中最大的 OVOCV 对构造 FRZ 态
>     * 3
>     * 使用
>     * $\alpha$
>     * 和
>     * $\beta$
>     * 空间中最大的 OVOCV 对构造 FRZ 态（用于双激发）
> * **建议**: 单激发使用 1 或 2，双激发使用 3

???+ example "示例 10.10.18: NH ${}_{3}$ 与 F ${}_{2}$ 之间长距离电荷转移的 OVOCV OO-DFT 分析。"
    ```qchem
    $molecule
    0 1
    N     0.000000000     0.000000000     -2.149985070
    H     -0.469826010     -0.813762490     -2.534400940
    H     -0.469826010     0.813762490     -2.534400940
    H     0.939652030     0.000000000     -2.534400940
    F     0.000000000     0.000000000     15.850014930
    F     0.000000000     0.000000000     17.275484090
    $end
    
    $comment
    IMOM we use for TRIPLET EXCITATIONS or MIXED-SPIN configurations
    $end
    
    $rem
    thresh              14
    scf_convergence     8
    method              hf
    basis               def2-TZVP
    scf_algorithm       diis_gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    XC_GRID             50000194
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $rem
    unrestricted        true
    thresh              14
    scf_convergence     6
    method              hf
    basis               def2-TZVP
    mom_method          imom
    mom_start           1
    scf_guess           read
    scf_max_cycles      500
    sym_ignore          true
    symmetry            false
    XC_GRID             50000194
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        15000
    ovocv_excite_analysis 1
    ovocv_excite_type     1
    save_ovocv            0
    $end
    
    $molecule
    read
    $end
    
    $occupied
    1 2 3 4 5 6 7 8 9 10 11 12 13 15
    1 2 3 4 5 6 7 8 9 10 11 12 13 14
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```

???+ example "示例 10.10.19: Fe(H ${}_{2}$ O) ${}^{3+}_{6}$ 中配体到金属电荷转移（LMCT）的 OVOCV OO-DFT 分析。"
    ```qchem
    $molecule
    +3 6
    --
    +3 6
    Fe     -0.5022247054     1.2927779200     0.0001938411
    --
    0 1
    H       2.1134166395     2.0808631740    -0.0009010689
    H      -0.5027205697    -1.3235141738    -0.7847973080
    H      -3.1183219511     2.0796505928    -0.0004236834
    H       0.2840444564     1.2933014045     2.6166394903
    H      -0.5027751731     3.9101762183     0.7846214605
    O       1.5358193871     1.2947592260    -0.0014374082
    H       2.1156949943     0.5103151332    -0.0009786075
    O      -0.5019595039     3.3312830798    -0.0005116891
    H      -0.5019009551     3.9098531329    -0.7858415694
    O      -0.5013746615     1.2930914301     2.0381118720
    H      -1.2864874118     1.2932385232     2.6170717164
    O      -2.5401948736     1.2938974534     0.0009627059
    H      -3.1195714968     0.5090879007     0.0019042859
    O      -0.5018840213    -0.7448372467     0.0005186723
    H      -0.5008290080    -1.3235744599     0.7857827770
    O      -0.5020354665     1.2915906981    -2.0378380237
    H       0.2835925140     1.2915440728    -2.6160740707
    H      -1.2869601935     1.2917959205    -2.6170203924
    $end
    
    $rem
    jobtype             sp
    method              wb97x-v
    basis               def2-tzvp
    scf_max_cycles      1000
    scf_algorithm       gdm
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $molecule
    +3 6
    --
    +2 5
    Fe     -0.5022247054     1.2927779200     0.0001938411
    --
    +1 2
    H       2.1134166395     2.0808631740    -0.0009010689
    H      -0.5027205697    -1.3235141738    -0.7847973080
    H      -3.1183219511     2.0796505928    -0.0004236834
    H       0.2840444564     1.2933014045     2.6166394903
    H      -0.5027751731     3.9101762183     0.7846214605
    O       1.5358193871     1.2947592260    -0.0014374082
    H       2.1156949943     0.5103151332    -0.0009786075
    O      -0.5019595039     3.3312830798    -0.0005116891
    H      -0.5019009551     3.9098531329    -0.7858415694
    O      -0.5013746615     1.2930914301     2.0381118720
    H      -1.2864874118     1.2932385232     2.6170717164
    O      -2.5401948736     1.2938974534     0.0009627059
    H      -3.1195714968     0.5090879007     0.0019042859
    O      -0.5018840213    -0.7448372467     0.0005186723
    H      -0.5008290080    -1.3235744599     0.7857827770
    O      -0.5020354665     1.2915906981    -2.0378380237
    H       0.2835925140     1.2915440728    -2.6160740707
    H      -1.2869601935     1.2917959205    -2.6170203924
    $end
    
    $rem
    jobtype             sp
    scf_guess           fragmo
    FRGM_METHOD         STOLL
    SCF_PRINT_FRGM      TRUE
    method              wb97x-v
    basis               def2-tzvp
    scf_max_cycles      1000
    scf_algorithm       gdm
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    unrestricted        true
    $end
    
    $rem_frgm
    SCF_CONVERGENCE     5
    SCF_ALGORITHM       DIIS_GDM
    THRESH              14
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    jobtype             sp
    method              wb97x-v
    basis               def2-tzvp
    scf_guess           read
    mom_method          imom
    mom_start           1
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    scf_max_cycles      2000
    unrestricted        true
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        20000
    ovocv_excite_analysis 1
    ovocv_excite_type     2
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```

???+ example "示例 10.10.20: 反式丁二烯（trans-butadiene）中双激发的 OVOCV OO-DFT 分析。"
    ```qchem
    $molecule
    0 1
    C       1.7631203268    -0.4019108032    -0.3481693109
    C       0.6037765052     0.2512052721    -0.3293638273
    C      -0.6037682643    -0.2511908395     0.3294491374
    C      -1.7631216007     0.4019093543     0.3482256846
    H      -2.6370356062    -0.0041538614     0.8460657302
    H      -1.8733953929     1.3678634226    -0.1376167636
    H       2.6369974511     0.0040901125    -0.8461249062
    H       1.8735775331    -1.3675549056     0.1382472290
    H      -0.5187645613    -1.2176355085     0.8243565706
    H       0.5187966092     1.2176897568    -0.8241975438
    $end
    
    $rem
    method              wB97X-V
    basis               def2-tzvp
    scf_algorithm       diis_gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    max_scf_cycles      200
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $rem
    unrestricted        true
    method              wB97X-V
    basis               def2-tzvp
    scf_guess           read
    scf_max_cycles      1000
    mom_method          imom
    mom_start           1
    sym_ignore          true
    symmetry            false
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        1000
    ovocv_excite_analysis 1
    ovocv_excite_type     3
    save_ovocv            0
    $end
    
    $molecule
    read
    $end
    
    $occupied
    1:14 16
    1:14 16
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```
