---
title: "12.6.8 采用非微扰极化与电荷转移分析的 ALMO-EDA"
---

## 12.6.8 采用非微扰极化与电荷转移分析的 ALMO-EDA

（2026 年 7 月 4 日）

**Q-Chem** 还通过 eda2 驱动程序，在第二代 ALMO-EDA 框架中支持非微扰（变分）的能量与电荷分解分析[[1396]](../bib_references/bib.md#bib1457)。与微扰电荷转移（CT）分析方法相比，该方法的优势在于能量分解和电荷分解都是精确的，不会留下任何高阶项。目前，该方法已针对受限与非受限自洽场（SCF）计算实现，可用于分析分子间相互作用中的极化（POL）[[1249]](../bib_references/bib.md#bib1301) 与电荷转移（CT）过程。分别设置 EDA_POL_A = TRUE 和 EDA_VCT_A = TRUE，即可启用非微扰的 POL 与 CT 分析。POL 分析[[1249]](../bib_references/bib.md#bib1301) 采用了新近发展的片段密度矩阵连接方法，能够将 POL 过程中的能量降低与电荷偏移精确地拆分为按片段可加的和式。CT 分析将以矩阵形式输出片段之间的成对能量与电荷变化，片段标签从 1 开始，其顺序与 Q-Chem 片段输入中的顺序一致。其解读方式为：能量降低和电荷转移源于由行标签所指片段向列标签所指片段的电子供与。

默认的轨道分析方法是互补占据-虚轨道对（COVP）方法。要筛选出显著的 COVP，可设置 EDA_COVP_THRESH = $N$，以打印出对能量降低贡献超过 $0.001\times N$ kJ/mol 的 COVP，默认值设为 500。若要可视化 COVP，可同时设置 EDA_SAVE_COVP = TRUE、MAKE_CUBE_FILES = TRUE 和 PLOTS = TRUE，将轨道保存为 cube 文件，随后可使用 IQmol、VMD 或其他可视化软件进行查看。化学价自然轨道（NOCV）分析也可通过设置 EDA_NOCV = TRUE 来执行。要筛选出显著的 NOCV，可设置 EDA_NOCV_THRESH = $N$，以打印出对能量降低贡献超过 $0.001\times N$ kJ/mol 的 NOCV，默认值同样为 500。NOCV 分析包含 POL 过程、CT 过程，以及将 POL 与 CT 过程合并的传统 NOCV 结果。正如文献[[1250]](../bib_references/bib.md#bib1300) 中所指出的，ETS-NOCV 方法仅用一组求积（quadrature）来近似有效 Fock 矩阵的积分，该项由 EDA_NOCV_QUADRATURE =1 设置；**Q-Chem** 还支持针对密度变化显著体系的五组求积方式。作为对 NOCV 的改进，新近提出的化学价占据-虚轨道（OVOCV）[[1248]](../bib_references/bib.md#bib1302) 同样可用于分析 CT 步骤。OVOCV 将密度差算符分块对角化为 $2 \times 2$ 块，每个块由初始态中被占据的一能级（占据 OVOCV）和空置的一能级（虚 OVOCV）张成，因此比 NOCV 更易于解读。关于 OVOCV 分析更详细的介绍，请参见 [10.3.4](../ch10_properties/sect_ovocv-analysis.md)。要启用 OVOCV 分析，请设置 OVOCV_ANALYSIS = 1 以及 OVOCV_THRESH = $N$，以打印出对能量降低贡献超过 $0.001\times N$ kJ/mol 的 OVOCV。

若至少有一个片段为开壳层结构，则 will 采用非受限分析。也可以通过设置 UNRESTRICTED=TRUE 来强制使用非受限分析。

### `EDA_POL_A`

> **对极化过程执行能量分解分析（EDA）**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不对极化过程执行 EDA
>     * `TRUE`: 对极化过程执行 EDA
> * **建议**: 设置为 TRUE 以对极化过程执行 EDA

### `EDA_VCT_A`

> **执行非微扰 CT 分析**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行非微扰 CT 分析
>     * `TRUE`: 执行非微扰 CT 分析。
> * **建议**: 设置为 TRUE 以执行非微扰 CT 分析

### `EDA_COVP_THRESH`

> **指定保存 COVP 时所需的显著性阈值**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **选项**:
>     * $N$: 对能量降低贡献超过 $0.001\times N$ kJ/mol 的 COVP 将被保存
> * **建议**: 无

### `EDA_SAVE_COVP`

> **是否保存重要的 COVP**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不保存重要的 COVP
>     * `TRUE`: 保存重要的 COVP
> * **建议**: 设置为 TRUE 以保存 COVP。注意还需要设置用于绘制 cube 文件的 REM 选项

### `EDA_NOCV`

> **是否执行 NOCV 分析**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行 NOCV 分析
>     * `TRUE`: 执行 NOCV 分析
> * **建议**: 无

### `EDA_NOCV_THRESH`

> **指定保存 NOCV 所对应的显著性阈值**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **选项**:
>     * $N$: 能量降低贡献超过 $0.001\times N$ kJ/mol 的 NOCV 将被保存
> * **建议**: 无

### `EDA_SAVE_NOCV`

> **是否保存重要的 NOCV**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不保存重要的 NOCV
>     * `1`: 保存重要的 NOCV
> * **建议**: 设置为 1 以保存 NOCV。注意还需要设置用于绘制 cube 文件的 REM 选项

### `EDA_NOCV_QUADRATURE`

> **用于积分有效 Fock 矩阵的求积（quadrature）数目**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `1`: 使用 1 个求积
>     * `5`: 使用 5 个求积
> * **建议**: 大多数情况下，一个求积就足够了。然而，当 NOCV 的能量降低与对应的 COVP 结果差异很大时，建议增加求积数目。

### `OVOCV_ANALYSIS`

> **是否执行 OVOCV 分析**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行 OVOCV 分析
>     * `TRUE`: 执行 OVOCV 分析
> * **建议**: 无

### `OVOCV_THRESH`

> **指定保存 OVOCV 所对应的显著性阈值**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **选项**:
>     * $N$: 能量降低贡献超过 $0.001\times N$ kJ/mol 的 OVOCV 将被保存
> * **建议**: 无

### `SAVE_OVOCV`

> **是否保存重要的 OVOCV**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不保存重要的 OVOCV
>     * `1`: 保存重要的 OVOCV
> * **建议**: 设置为 1 以保存 OVOCV。注意还需要设置用于绘制 cube 文件的 REM 选项

???+ example "示例 12.20: 采用非微扰 POL 与 CT 分析对 H ${}_{2}$ O-Na ${}^{+}$ 体系进行限制 EDA 计算。"
    ```qchem
    $molecule
    1 1
    --
    0 1
    H         -0.73946        0.94887        0.78379
    O         -1.16910        0.63297       -0.02844
    H         -2.12156        0.70793        0.14730
    --
    1 1
    Na        -0.17266       -0.04338       -1.86190
    $end
    
    $comment
    EDA2 (R) calculation with variational POL and CT analyses
    based on the eda2 driver
    $end
    
    $rem
    jobtype              eda
    eda2                 1
    method               B3LYP
    scf_print_frgm       1
    basis                6-31G*
    scf_algorithm        diis
    thresh               12
    incfock              false
    mem_total            16000
    scf_convergence      7
    scf_final_print      2
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      500
    eda_save_covp        0
    make_cube_files      true
    plots                true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 50 50 50
    $end
    
    ```

???+ example "示例 12.21: 采用非微扰 POL 与 CT 分析对 CH ${}_{3}$ -Na ${}^{+}$ 体系进行非限制 EDA 计算。"
    ```qchem
    $molecule
    1 2
    --
    0 2
    C¯-1.447596 -0.000023  0.000019
    H¯-1.562749  0.330361 -1.023835
    H¯-1.561982  0.721445  0.798205
    H¯-1.561187 -1.052067  0.225866
    --
    1 1
    Na¯ 1.215591  0.000036 -0.000032
    $end
    
    $comment
    EDA2 (U) calculation with variational POL and CT analyses
    based on the eda2 driver
    $end
    
    $rem
    jobtype              eda
    eda2                 1
    method               B3LYP
    scf_print_frgm       true
    basis                aug-cc-PVTZ
    scf_algorithm        diis
    thresh               12
    incfock              false
    mem_total            16000
    scf_convergence      7
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      500
    eda_save_covp        0
    make_cube_files      true
    plots                true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 50 50 50
    $end
    
    ```

???+ example "示例 12.22: 采用非微扰 POL 与 CT 分析及 NOCV 分析对 Rn ${}^{+}$ -CH ${}_{4}$ 体系进行非限制 EDA 计算"
    ```qchem
    $molecule
    1 2
    --
    0 1
    C         0.0551597051    0.0364080371   -0.0375528310
    H        -0.0563410694   -1.0144740143   -0.3153331540
    H        -0.0537558345    0.7868509829   -0.8318467516
    H        -0.8718690962    0.2438110339    0.5677588397
    H         1.0408273042    0.1810559688    0.4109829953
    --
    1 2
    Rn       -0.2646060092    0.6373989916    3.0026329017
    $end
    
    $rem
    jobtype             eda
    eda2                1
    method              b3lyp
    scf_print_frgm      1
    basis               def2-tzvp
    ecp                 def2-ecp
    scf_algorithm       diis
    thresh              12
    incfock             0
    mem_total           16000
    scf_final_print     2
    iprint              20000000
    scf_convergence     7
    eda_pol_a           1
    eda_vct_a           1
    eda_save_covp       0
    eda_nocv            1
    eda_save_nocv       0
    eda_covp_thresh     500
    eda_nocv_thresh     500
    eda_nocv_quadrature 1
    make_cube_files     true
    plots               true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 100 100 100
    $end
    
    ```

???+ example "示例 12.23: 采用非微扰 POL 与 CT 分析对乙烯- $[\text{PtCl}_{3}]^{-}$ 体系进行限制 EDA 计算。
已为 CT 分析启用 OVOCV 分析。"
    ```qchem
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
    jobtype              eda
    eda2                 1
    eda_bsse             0
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
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      10000
    eda_save_covp        0
    eda_nocv             1
    eda_save_nocv        0
    eda_nocv_thresh      10000
    eda_nocv_quadrature  5
    ovocv_analysis       1
    ovocv_thresh         10000
    save_ovocv           0
    make_cube_files      true
    plots                true
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```
