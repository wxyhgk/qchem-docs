---
title: "13.5.6 示例"
---

## 13.5.6 示例

（2026 年 7 月 4 日）

???+ example "示例 13.7：H ${}_{2}$ O 分子的 NEO-HF 计算输入，其中第二个质子按量子力学方式处理。电子基组为 cc-pVDZ，质子基组为未经缩合（uncontracted）的 2s2p2d 基组，指数为 4.0 和 8.0。"
    ```qchem
    $molecule
       0 1
       H   -3.5008791    1.2736107    0.7596000
       O   -3.9840791    1.3301107   -0.0574000
       H   -4.9109791    1.2967107    0.1521000
    $end
    
    $rem
       METHOD   hf
       BASIS    cc-pvdz
       NEO      true
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       8.0 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       8.0 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       8.0 1.0
    ****
    $end
    ```

???+ example "示例 13.8：CH ${}_{2}$ O 分子的 NEO-DFT/epc17-2 计算输入，两个质子均按量子力学方式处理，并采用同时 DIIS（simultaneous DIIS）算法执行 NEO-SCF。电子基组为 cc-pVDZ，质子基组为未经缩合的 1s1p 基组，指数为 4.0 和 4.0。在插值/外推构造下一轮初始猜测时，最多使用之前 10 个 Fock 矩阵；当以下三个判据全部满足时（均以原子单位计），认为 NEO 波函数已收敛：(1) 电子误差向量的最大元素低于截止阈值 $10^{-8}$ ，(2) 质子误差向量的最大元素低于截止阈值 $10^{-7}$ ，且 (3) 相邻两步之间的能量差低于 $10^{-8}$ 。"
    ```qchem
    $molecule
    0 1
      C        0.000000    0.000000    0.000000
      O        0.000000    0.000000    1.220000
      H        0.935307    0.0000000  -0.5400000
      H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
       JOBTYPE              SP
       SYM_IGNORE           TRUE
       INPUT_BOHR           FALSE
       BASIS                cc-pvdz
       NEO                  TRUE
       METHOD               pbe0
       xc_grid = 000099000302
       NEO_EPC              epc172
       NEO_N_SCF_CONVERGENCE = 7
       SCF_CONVERGENCE = 8
       NEO_E_CONV = 8
       SCF_ALGORITHM        DIIS
       NEO_SIMULTANEOUS_SCF TRUE
       NEO_STEPWISE_SCF_STEPS = 2
       DIIS_SUBSPACE_SIZE = 10
       DIIS_ERR_RMS         FALSE
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.9：CH ${}_{2}$ O 分子所有中心的 NEO-DFT/epc17-2 几何结构优化计算输入，两个质子均按量子力学方式处理。电子交换-关联泛函为 PBE0。电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。该计算采用具有 99 个径向和 302 个球面求积点的 DFT 网格，并结合 DIIS 算法。"
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000    0.000000
       O     0.000000    0.000000    1.220000
       H     0.935307    0.000000   -0.540000
       H    -0.935307    0.000000   -0.540000
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            pbe0
       BASIS             sto-3g
       NEO               true
       NEO_EPC           epc172
    point_group_symmetry False
       SCF_CONVERGENCE   11
       MAX_SCF_CYCLES    100
       SCF_ALGORITHM     diis
       XC_GRID           000099000302
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.10：仅对开壳层 OH 自由基分子的 NEO 中心进行几何结构优化的 NEO-DFT/epc19 计算输入，其中质子按量子力学方式处理。电子交换-关联泛函为 PBE0。电子基组为 6-31G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。该计算采用具有 99 个径向和 230 个球面求积点的 DFT 网格，并结合 DIIS 算法。"
    ```qchem
    $molecule
       0 2
       O    -4.511414   1.264878   0.000000
       H    -2.739325   1.866123   0.000000
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            pbe0
       BASIS             6-31g
       UNRESTRICTED      true
       INPUT_BOHR        true
       NEO               true
    point_group_symmetry False
       SCF_CONVERGENCE   6
       MAX_SCF_CYCLES    100
       SCF_ALGORITHM     diis
       NEO_EPC           epc19
       XC_GRID           000099000230
    $end
    
    $opt
       FIXED
       1 XYZ
       ENDFIXED
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.11：FHF ${}^{-}$ 的 NEO-MSDFT 计算输入，其中 F–F 距离固定为 2.70 Å。
两个 F 原子之间的质子被量子化，质子基函数中心在 NEO-MSDFT 基态上加以优化。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子交换-关联泛函为 B3LYP，电子-质子关联泛函为 epc17-2。
量子质子的第二个基函数中心以虚中心（ghost center）的形式输入。"
    ```qchem
    $molecule
    -1  1
    F      0.00000000     0.00000000    -1.35000000
    F      0.00000000     0.00000000     1.35000000
    H      0.00000000     0.00000000    -0.25220000
    @H     0.00000000     0.00000000     0.25220000
    $end
    
    $rem
    jobtype = opt
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    max_scf_cycles 500
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE 6
    NEO_E_CONV = 6
    SCF_ALGORITHM gdm
    $end
    
    $OPT
    FIXED
    1 XYZ
    2 XYZ
    ENDFIXED
    $END
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.12：甲酸二聚体固定平均反应物-产物结构的 NEO-MSDFT 计算输入，其中 C–C 距离为
3.86 Å，两个转移质子均被量子化。电子基组为 STO-3G，质子基组为未经缩合的
1s1p 基组，指数为 4.0。电子交换-关联泛函为 B3LYP，电子-质子关联泛函为
epc17-2。绝热态展开（adiabatic state expansion）中仅包含两个反式（trans）态（注意 $neo_msdft_diabat_control 段中 1 与 0 之间的空格）。每个量子质子的第二个中心以虚中心的形式输入。已启用基态和
第一激发态的质子密度绘图。"
    ```qchem
    $molecule
    0  1
    H        -3.0310572606    0.0000000000    0.0000000000
    H        -0.4438453003    1.0873992328    0.0000000000
    @H        0.4438452993    1.0873992291    0.0000000000
    O        -1.3616953972   -1.1310228162    0.0000000000
    O        -1.3616953971    1.1310228163    0.0000000000
    C        -1.9296657251    0.0000000000    0.0000000000
    H         3.0310572606    0.0000000000    0.0000000000
    H         0.4438452993   -1.0873992291    0.0000000000
    @H       -0.4438453003   -1.0873992328    0.0000000000
    O         1.3616953972    1.1310228162    0.0000000000
    O         1.3616953971   -1.1310228163    0.0000000000
    C         1.9296657251    0.0000000000    0.0000000000
    $end
    
    $rem
    jobtype = sp
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE = 6
    NEO_E_CONV = 6
    max_scf_cycles 500
    SCF_ALGORITHM GDM
    $end
    
    $neo_msdft
    denplt = 1
    $end
    
    $neo_msdft_diabat_control
    1 0 1 0
    0 1 0 1
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    8
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H   9
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.13：质子化水二聚体的 NEO-MSDFT 计算输入，其中 O–O 距离固定为 2.80 Å，
体系中所有质子均被量子化，但仅两个氧原子之间的质子被视为转移质子。
转移质子的两个中心在 $molecule 段中连续书写，第一个写成 H
原子中心，第二个写成虚 H 原子中心。其他中心没有对应的虚中心，
因此不会被识别为转移质子。电子基组为 STO-3G，质子基组为未经缩合的
1s1p 基组，指数为 4.0。电子交换-关联泛函为 B3LYP，电子-质子
关联泛函为 epc17-2。"
    ```qchem
    $molecule
    1  1
    O      -1.4000000000     0.0000000000     0.0000000000
    O       1.4000000000     0.0000000000     0.0000000000
    H      -0.3000000000     0.0000000000     0.0000000000
    @H      0.3000000000     0.0000000000     0.0000000000
    H       1.6600000000     0.7500000000    -0.5500000000
    H       1.6600000000    -0.7500000000    -0.5500000000
    H      -1.6600000000     0.7500000000     0.5500000000
    H      -1.6600000000    -0.7500000000     0.5500000000
    $end
    
    $rem
    jobtype = sp
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE = 6
    NEO_E_CONV = 6
    max_scf_cycles 500
    SCF_ALGORITHM GDM
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    5
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    6
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    7
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    8
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.14：水溶液 C-PCM 中 CH ${}_{2}$ O 分子的 NEO-DFT/epc17-2 几何结构优化计算输入。围绕固定的经典核点电荷位置以及两个量子氢的核基函数中心位置构建范德华（van der Waals）表面。
此处，在包围离域质子密度的球形空腔的构建中使用氢的 Bondi 半径，但用户可以选择在 $van_der_waals 输入段中指定自定义原子半径。整个空腔按因子 $\alpha_{\text{vdW}}=1.2$ 缩放，
随后通过 SwiG 方法进行离散化。"
    ```qchem
    $molecule
    0 1
      C        0.000000    0.000000    0.000000
      O        0.000000    0.000000    1.220000
      H        0.935307    0.0000000  -0.5400000
      H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    point_group_symmetry False
       JOBTYPE              OPT
       INPUT_BOHR           FALSE
       BASIS                sto-3g
       NEO                  TRUE
       METHOD               pbe0
       xc_grid = 000099000302
       NEO_EPC              epc172
       SCF_CONVERGENCE = 8
       NEO_E_CONV = 8
       SCF_ALGORITHM        GDM
       SOLVENT_METHOD       PCM
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $pcm
       Theory               CPCM
       Method               SWIG
       Solver               INVERSION
       HeavyPoints          194
       HPoints              194
       Radii                Bondi
       vdwScale             1.2
    $end
    
    $solvent
      Dielectric   78.39
    $end
    ```

???+ example "示例 13.15：Au ${}_{2}$ H、C ${}_{\infty\text{v}}$ 分子的 NEO-DFT/epc17-2 几何结构优化计算输入，金原子使用
fit-LANL2DZ 有效核势（effective core potential）。"
    ```qchem
    $molecule
    1 1
      Au       0.000000    0.000000    2.222000
      Au       0.000000    0.000000    5.502000
      H        0.000000    0.000000    3.842000
    $end
    
    $rem
       JOBTYPE                 OPT
       SYM_IGNORE             TRUE
       INPUT_BOHR            FALSE
       BASIS                 mixed
       NEO                    TRUE
       METHOD                b3lyp
       xc_grid      = 000099000302
       NEO_EPC              epc172
       NEO_N_SCF_CONVERGENCE   = 8
       SCF_CONVERGENCE         = 8
       NEO_E_CONV              = 8
       SCF_ALGORITHM           GDM
       ECP             fit-LANL2DZ
    $end
    
    $basis
    Au 1
    LANL2DZ
    ****
    Au 2
    LANL2DZ
    ****
    H 3
    def2-qzvp
    ****
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       5.973 1.0
    S    1    1.000000
       10.645 1.0
    S    1    1.000000
       17.943 1.0
    S    1    1.000000
       28.950 1.0
    P    1    1.000000
       7.604 1.0
    P    1    1.000000
       14.701 1.0
    P    1    1.000000
       23.308 1.0
    D    1    1.000000
       9.011 1.0
    D    1    1.000000
       19.787 1.0
    F    1    1.000000
       10.914 1.0
    F    1    1.000000
       20.985 1.0
    ****
    $end
    ```

???+ example "示例 13.16：HCN 分子的 NEO-HF 解析 Hessian（海森矩阵）计算输入，其中质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为 1s1p，指数为 4.0。"
    ```qchem
    $molecule
    0 1
      C         0.0000000000    0.0000000000    0.9684140792
      N         0.0000000000    0.0000000000   -1.2085828830
      H         0.0000000000    0.0000000000    2.9046475823
    $end
    
    $rem
    jobtyp = freq
    input_bohr = true
    point_group_symmetry = False
    method = hf
    basis = sto-3g
    neo = true
    SCF_ALGORITHM = gdm
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.17：使用 NEO-BOMD 在 NEO-DFT 振动基态面上模拟丙二醛（malonaldehyde）分子内质子转移的输入。注意包含了 $neo_gs_dynamics 、 $neo_gs_dynamics_donor_acceptor_indices 和 $neo_gs_dynamics_velocities 输入段。另外注意，质子基函数中心（$molecule 段的第一项）在 $neo_gs_dynamics_velocities 输入段中的速度为零。"
    ```qchem
    $molecule
    0 1
    H        -0.3982276484    4.7093371192    0.0000000000
    C        -2.2965024834    1.7761906527    0.0000000000
    C        -0.0778296218    0.4606600999    0.0000000000
    C         2.2683699385    1.8502803018    0.0000000000
    O        -2.4548505732    4.2439921132    0.0000000000
    O         2.3773400124    4.1728718529    0.0000000000
    H        -4.1386563233    0.8241552831    0.0000000000
    H        -0.0809127358   -1.5993342589    0.0000000000
    H         4.0571330701    0.7432112784    0.0000000000
    $end
    
    $rem
    NEO_BOMD                    TRUE
    SYM_IGNORE                  TRUE
    INPUT_BOHR                  TRUE
    METHOD                      b3lyp
    BASIS                       sto-3g
    SCF_ALGORITHM               DIIS
    MAX_SCF_CYCLES              1000
    NEO                         TRUE
    NEO_EPC                     EPC172
    NEO_PURECART                1111
    NEO_VPP                     FALSE
    NEO_SIMULTANEOUS_SCF        TRUE
    NEO_VPP                     FALSE
    NEO_E_CONV                  5
    NEO_N_SCF_CONVERGENCE       5
    SCF_CONVERGENCE             5
    $end
    
    $neo_gs_dynamics
    nsteps 1
    dt 0.2
    $end
    
    $neo_gs_dynamics_donor_acceptor_indices
    5 6
    $end
    
    $neo_gs_dynamics_velocities
      0.0000000000e+00        0.0000000000e+00        0.0000000000e+00
      2.9512420606e-05        7.9677231137e-05        0.0000000000e+00
      4.9086468803e-05       -1.2437450767e-04        0.0000000000e+00
     -1.2941243817e-04       -1.0648277856e-04        0.0000000000e+00
      3.6818304686e-04       -5.1390359408e-05        0.0000000000e+00
     -3.2247267387e-04        2.5782796687e-05        0.0000000000e+00
     -1.9003838357e-05        1.2271678408e-04        0.0000000000e+00
      2.9746441198e-05       -1.2106793256e-04        0.0000000000e+00
     -5.6394270736e-06        1.7513876629e-04        0.0000000000e+00
    $end
    
    $neo_basis
    H    1
    S   1   1.00
         4.0                  1.0
    P   1   1.00
         4.0                  1.0
    ****
    $end
    ```

???+ example "示例 13.18：使用 NEO-ELMD(4) 在 NEO-DFT 扩展振动基态面上模拟丙二醛分子内质子转移的输入。注意包含了 $neo_gs_dynamics 、 $neo_gs_dynamics_donor_acceptor_indices 和 $neo_gs_dynamics_velocities 输入段。另外注意，质子基函数中心（$molecule 段的第一项）在 $neo_gs_dynamics_velocities 输入段中的速度为零。"
    ```qchem
    $molecule
    0 1
    H        -0.3982276484    4.7093371192    0.0000000000
    C        -2.2965024834    1.7761906527    0.0000000000
    C        -0.0778296218    0.4606600999    0.0000000000
    C         2.2683699385    1.8502803018    0.0000000000
    O        -2.4548505732    4.2439921132    0.0000000000
    O         2.3773400124    4.1728718529    0.0000000000
    H        -4.1386563233    0.8241552831    0.0000000000
    H        -0.0809127358   -1.5993342589    0.0000000000
    H         4.0571330701    0.7432112784    0.0000000000
    $end
    
    $rem
    NEO_ELMD                    TRUE
    SYM_IGNORE                  TRUE
    INPUT_BOHR                  TRUE
    METHOD                      b3lyp
    BASIS                       sto-3g
    SCF_ALGORITHM               DIIS
    MAX_SCF_CYCLES              1000
    NEO                         TRUE
    NEO_EPC                     EPC172
    NEO_PURECART                1111
    NEO_VPP                     FALSE
    NEO_SIMULTANEOUS_SCF        TRUE
    NEO_VPP                     FALSE
    NEO_E_CONV                  5
    NEO_N_SCF_CONVERGENCE       5
    SCF_CONVERGENCE             5
    $end
    
    $neo_gs_dynamics
    nsteps 10
    dt 1.0
    ASPC 1
    ASPC_NDENMATS 4
    $end
    
    $neo_gs_dynamics_donor_acceptor_indices
    5 6
    $end
    
    $neo_gs_dynamics_velocities
      0.0000000000e+00        0.0000000000e+00        0.0000000000e+00
      2.9512420606e-05        7.9677231137e-05        0.0000000000e+00
      4.9086468803e-05       -1.2437450767e-04        0.0000000000e+00
     -1.2941243817e-04       -1.0648277856e-04        0.0000000000e+00
      3.6818304686e-04       -5.1390359408e-05        0.0000000000e+00
     -3.2247267387e-04        2.5782796687e-05        0.0000000000e+00
     -1.9003838357e-05        1.2271678408e-04        0.0000000000e+00
      2.9746441198e-05       -1.2106793256e-04        0.0000000000e+00
     -5.6394270736e-06        1.7513876629e-04        0.0000000000e+00
    $end
    
    $neo_basis
    H    1
    S   1   1.00
         4.0                  1.0
    P   1   1.00
         4.0                  1.0
    ****
    $end
    ```

???+ example "示例 13.19：HCN 分子的 NEO-HF(V) 计算输入，其中质子按量子力学方式处理。电子基组为 STO-3G，质子基组为 1s1p，指数为 4.0。"
    ```qchem
    $molecule
    0 1
      C         0.0000000000    0.0000000000    0.9684140792
      N         0.0000000000    0.0000000000   -1.2085828830
      H         0.0000000000    0.0000000000    2.9046475823
    $end
    
    $rem
    jobtyp = freq
    input_bohr = true
    point_group_symmetry = False
    method = hf
    SCF_ALGORITHM = gdm
    basis = sto-3g
    neo = true
    neo_scfv = 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.20：HCN 分子的 CNEO-DFT 解析 Hessian 计算输入，其中质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子交换-关联泛函为 BLYP，电子-质子关联泛函为 epc17-2。"
    ```qchem
    $molecule
    0 1
    H    0.000000    0.000000   -0.013880
    C    0.000000    0.000000    1.103384
    N    0.000000    0.000000    2.310496
    $end
    
    $rem
    jobtype     freq
    sym_ignore  true
    method      blyp
    basis       sto-3g
    neo         true
    neo_epc     epc172
    cneo        true
    $end
    
    $neo_basis
    H    1
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.21：CH ${}_{2}$ O 分子的 NEO-DFT 能量计算输入，两个质子使用核 Hartree 积（nuclear Hartree product）近似按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子交换-关联泛函为 BLYP，电子-质子关联泛函为 epc17-2。"
    ```qchem
    $molecule
    0 1
    C        0.000000    0.000000    0.000000
    O        0.000000    0.000000    1.220000
    H        0.935307    0.000000   -0.540000
    H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    jobtype         sp
    sym_ignore      true
    scf_algorithm   gdm
    method          blyp
    basis           sto-3g
    neo             true
    neo_epc         epc172
    neo_n_hartree_prod     true
    neo_n_scf_convergence  8
    scf_convergence        8
    neo_e_conv             8
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.22：CH ${}_{2}$ O 分子（两个质子均按量子力学方式处理）的前五个根的 LR-NEO-TDDFT/epc19 计算输入，使用 Davidson（戴维森）算法求解。电子交换-关联泛函为 PBE0。电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。该计算采用具有 99 个径向和 302 个球面求积点的 DFT 网格。"
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000    0.000000
       O     0.000000    0.000000    1.220000
       H     0.935307    0.000000   -0.540000
       H    -0.935307    0.000000   -0.540000
    $end
    
    $rem
       METHOD            pbe0
       BASIS             sto-3g
       THRESH            14
       XC_GRID           000099000302
       S2THRESH          12
       NEO               true
       NEO_EPC           epc172
       SET_ROOTS         5
       RPA               true
       SCF_CONVERGENCE   12
       NEO_E_CONV        12
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.23：FDF ${}^{-}$ 分子的 LR-NEO-TDHF 计算输入，其中量子核按氘处理，并启用 NO_VPP 选项。
电子基组为 cc-pVDZ，质子基组为未经缩合的等指数（even-tempered）8s8p 基组。"
    ```qchem
    $molecule
       -1 1
       F   0.000000   0.000000   -1.122987
       F   0.000000   0.000000    1.122987
       H   0.000000   0.000000    0.000000
    $end
    
    $rem
       METHOD            hf
       BASIS             cc-pvdz
       NEO               true
       SCF_ALGORITHM     GDM
       RPA               true
       CIS_N_ROOTS       100
       THRESH            14
       S2THRESH          12
       SCF_CONVERGENCE   11
       MAX_SCF_CYCLES    300
       NEO_VPP           0
       NEO_ISOTOPE       2
       NEO_E_CONV        11
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       2.828400 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.828400 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "示例 13.24：CH ${}_{2}$ 分子的 LR-NEO-TDDFT 解析梯度计算输入，两个质子均按量子力学方式处理。
共请求四个激发态，并对第 3 个激发态计算梯度。电子交换-关联
泛函为 CAM-B3LYP，并使用电子-质子关联泛函 epc17-2。电子基组为 STO-3G，质子基组为 1s1p，指数为 4.0。该计算采用具有 99 个径向和 302 个球面求积点的 DFT 网格，并结合 GDM
算法。"
    ```qchem
    $molecule
    0 3
    C  0.00000000000000e+00  0.00000000000000e+00 -5.63654429543699e-02
    H  1.81800983405161e+00  0.00000000000000e+00 -9.92269386019353e-01
    H -1.81800983405161e+00  0.00000000000000e+00 -9.92269386019353e-01
    $end
    
    $rem
    point_group_symmetry = false
    input_bohr           = true
    method               = cam-b3lyp
    basis                = sto-3g
    thresh               = 14
    s2thresh             = 12
    neo                  = true
    cis_n_roots          = 4
    rpa                  = true
    xc_grid              = 000099000302
    unrestricted         = 1
    neo_epc              = epc172
    scf_algorithm        = gdm
    cis_state_deriv      = 3
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.25：C ${}_{2}$ H ${}_{2}$ 分子的 LR-NEO-TDDFT 几何结构优化输入，两个质子均按量子力学方式处理。
共请求三个激发态，并对第 1 个激发态进行几何结构优化。
电子交换-关联泛函为 B3LYP，并使用电子-质子关联泛函 epc17-2。
电子基组为 STO-3G，质子基组为 1s1p，指数为 4.0。该计算采用具有 99 个径向
和 302 个球面求积点的 DFT 网格，并结合 GDM 算法。"
    ```qchem
    $molecule
    0 1
            C       0.4142076725     1.0563578037     0.0000000223
            C      -0.4142118956    -1.0563667882     0.0000000223
            H       1.1661939287     2.9673893099     0.0000000246
            H      -1.1661909474    -2.9673788285     0.0000000246
    $end
    
    $rem
    jobtype              = opt
    neo_set_opt          = true
    neo_epc              = epc172
    cis_state_deriv      = 1
    input_bohr           = true
    method               = b3lyp
    neo                  = true
    scf_algorithm        = gdm
    thresh               = 14
    s2thresh             = 12
    basis                = sto-3g
    rpa                  = true
    cis_n_roots          = 3
    xc_grid              = 000099000302
    point_group_symmetry = false
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "示例 13.26：C ${}_{2}$ H ${}_{2}$ 分子的 LR-NEO-TDDFT 计算输入，两个质子均按量子力学方式处理。共请求 12 个激发态。
基态质子密度和电子密度以 cube 文件形式输出。前两个以电子激发为主的振动态（vibronic）激发的质子与电子跃迁密度同样以 cube 文件形式输出。
电子交换-关联泛函为 B3LYP，并使用电子-质子关联泛函 epc17-2。
电子基组为 STO-3G，质子基组为 1s1p，指数为 4.0。该计算采用具有 99 个径向和
302 个球面求积点的 DFT 网格，并结合 GDM 算法。"
    ```qchem
    $molecule
    0 1
           C        -0.2315710674    1.2702261467    0.0000001295
           C         0.2315702809   -1.2702255666    0.0000001295
           H         1.2946585350    2.6676952886   -0.0000000923
           H        -1.2946589903   -2.6676943717   -0.0000000923
    $end
    
    $rem
    point_group_symmetry = False
    input_bohr = true
    method = b3lyp
    neo = true
    NEO_SET_ESTATE = 1
    SCF_ALGORITHM = gdm
    thresh = 14
    s2thresh = 12
    basis = sto-3g
    GEOM_OPT_MAX_CYCLES = 500
    rpa = true
    SET_ROOTS = 12
    xc_grid = 000099000302
    MAKE_CUBE_FILES = true
    plots = true
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $plots
    grid information to plot protonic and electronic ground state densities and transition densities for two eletronic dominant transitions
       100  -4.0 6.0
       100  -5.0 4.0
       100  -4.0 4.0
       0 1 2 0
       0
       0 1
    $end
    
    ```

???+ example "示例 13.27：使用 RT-NEO-TDHF 模拟的甲酸根离子（formate ion），并受到来自 $x$ 、 $y$ 、 $z$ 三个正交方向的高斯脉冲响应激发。"
    ```qchem
    $molecule
    -1 1
    C   0.000000  0.000000  0.316833
    H   0.000000  0.000000  1.430087
    O   0.000000  1.135580 -0.208193
    O   0.000000 -1.135580 -0.208193
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = cc-pvtz
    METHOD                = hf
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       5.973 1.0
    S    1    1.000000
       10.645 1.0
    S    1    1.000000
       17.943 1.0
    S    1    1.000000
       28.950 1.0
    P    1    1.000000
       7.604 1.0
    P    1    1.000000
       14.701 1.0
    P    1    1.000000
       23.308 1.0
    D    1    1.000000
       9.011 1.0
    D    1    1.000000
       19.787 1.0
    F    1    1.000000
       10.914 1.0
    F    1    1.000000
       20.985 1.0
    ****
    $end
    
    $neo_tdks
    METHOD              = realtime
    DT                  = 0.04
    MAXITER             = 20000
    FIELD_TYPE          = gaussian
    FIELD_AMP           = 0.02
    FIELD_PEAK          = 0.0
    FIELD_TAU           = 800.0
    FIELD_FREQUENCY     = 6.0
    FIELD_DIRECTION     = xyz
    FIELD_PARTICLE_TYPE = both
    $end
    ```

???+ example "示例 13.28：使用 RT-NEO-TDDFT-Ehrenfest 模拟的 $o$ -羟基苯甲醛（o-hydroxylbenzaldehyde）激发态分子内质子转移，
采用 B3LYP 电子交换-关联泛函和 epc17-2 电子-质子关联泛函。
沿质子转移路径添加了两个额外的基函数中心，总模拟时间
指定为 19.35 fs，并执行了电子 HOMO 到 LUMO 的交换以制备初始态。"
    ```qchem
    $molecule
    0 1
    C  -1.310008  1.258755  0.000000
    C   0.019289  0.780580  0.000000
    C   0.322586 -0.621636  0.000000
    C  -0.761283 -1.465586  0.000000
    C  -2.125342 -0.985468  0.000000
    C  -2.398971  0.362640  0.000000
    O   1.008708  1.658363  0.000000
    C   1.725826 -1.062678  0.000000
    O   2.682115 -0.219090  0.000000
    H  -3.414260  0.733314  0.000000
    H  -0.596742 -2.537818  0.000000
    H  -2.926679 -1.713458  0.000000
    H  -1.459388  2.331114  0.000000
    H   1.924136 -2.138192  0.000000
    H   1.844187  1.135044  0.000000
    @H  2.042593  0.928022  0.000000
    @H  2.241000  0.721000  0.000000
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = cc-pvtz
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    15
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    H    16
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    H    17
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD                  = ehrenfest
    DT                      = 0.04
    MAXITER                 = 20000
    ELECTRONIC_HOMO_TO_LUMO = true
    $end
    ```

???+ example "示例 13.29：使用 BO-RT-NEO-TDDFT-Ehrenfest 模拟的丙二醛基态分子内质子转移。作为原理验证，
采用了最小基组。注意由于电子动力学不再被传播（propagate），此处使用了 4.2 原子单位的大时间步长。"
    ```qchem
    $molecule
    0 1
    O   0.000000 -1.300873  2.045662
    O   0.000000  1.290832  2.045662
    C   0.000000 -1.216031  0.759259
    C   0.000000  1.205990  0.759259
    C   0.000000 -0.005020  0.053344
    H   0.000000 -0.005020 -1.024823
    H   0.000000 -2.163146  0.218967
    H   0.000000  2.153105  0.218967
    H   0.000000 -0.301012  2.355420
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = sto-3g
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    9
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD  = bo-ehrenfest
    DT      = 4.2
    MAXITER = 1335
    $end
    ```

???+ example "示例 13.30：使用 BO-RT-NEO-TDDFT-Ehrenfest 模拟的丙二醛基态分子内质子转移，
并采用带自定义参数的 B3LYP-D3(0) 经验色散校正。"
    ```qchem
    $molecule
    0 1
    O   0.000000 -1.300873  2.045662
    O   0.000000  1.290832  2.045662
    C   0.000000 -1.216031  0.759259
    C   0.000000  1.205990  0.759259
    C   0.000000 -0.005020  0.053344
    H   0.000000 -0.005020 -1.024823
    H   0.000000 -2.163146  0.218967
    H   0.000000  2.153105  0.218967
    H   0.000000 -0.301012  2.355420
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = sto-3g
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    DFT_D                 = D3_ZERO
    DFT_D3_S6             = 100000
    DFT_D3_RS6            = 126100
    DFT_D3_S8             = 170300
    DFT_D3_3BODY          = FALSE
    $end
    
    $neo_basis
    H    9
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD  = bo-ehrenfest
    DT      = 4.2
    MAXITER = 1335
    $end
    ```

???+ example "示例 13.31：H ${}_{2}$ O 分子的 NEO-RICCSD 计算输入，其中第二个质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子辅助基组（auxiliary basis set）为 RIMP2-aug-cc-pVDZ，质子辅助基组为未经缩合的等指数 8s8p 基组。"
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    neo = true
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    NEO_RICCSD 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "示例 13.32：CH ${}_{2}$ O 分子的 NEO-SCS ${}^{\prime}$ -MP2 计算输入，两个质子均按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子辅助基组为 RIMP2-aug-cc-pVDZ，质子辅助基组为未经缩合的等指数 8s8p 基组。
SCS 缩放对应 $c_{\text{ss}}=0.33$ 、 $c_{\text{os}}=1.2$ 和 $c_{\text{ep}}=1.2$ 。"
    ```qchem
    $molecule
    0 1
    C        0.000000    0.000000    0.000000
    O        0.000000    0.000000    1.220000
    H        0.935307    0.0000000  -0.5400000
    H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    method = hf
    basis = sto-3g
    neo = true
    sym_ignore = 1
    aux_basis = rimp2-cc-pVDZ
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_RIMP2 1
    SCS 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    H   4
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "示例 13.33：H ${}_{2}$ O 分子的 NEO-OOMP2 计算输入，其中第二个质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子辅助基组为 RIMP2-aug-cc-pVDZ，质子辅助基组为未经缩合的等指数 8s8p 基组。"
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    input_bohr = false
    method = hf
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    neo = true
    sym_ignore = 1
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_VPP 0
    NEO_RIMP2 2
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "示例 13.34：H ${}_{2}$ O 分子的 NEO-SOS ${}^{\prime}$ -OOMP2 计算输入，其中第二个质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
电子辅助基组为 RIMP2-aug-cc-pVDZ，质子辅助基组为未经缩合的等指数 8s8p 基组。
SOS 缩放对应 $c_{\text{ss}}=0.0$ 和 $c_{\text{os}}=1.2$ ，并采用自定义值 $c_{\text{ep}}=1.5$ 。"
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    input_bohr = false
    method = hf
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    neo = true
    sym_ignore = 1
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_VPP 0
    NEO_RIMP2 2
    SCS 2
    EP_FACTOR 1500000
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "示例 13.35：HCN 分子的 NEO-SOS ${}^{\prime}$ -CC2 激发态计算输入，其中质子按量子力学方式处理。
电子基组为 STO-3G，质子基组为未经缩合的 1s1p 基组，指数为 4.0。
SOS 缩放对应 $c_{\text{ss}}=0.0$ 和 $c_{\text{os}}=1.3$ ，基态电子–质子关联缩放 $c_{\text{ep}}=0.94$ ，激发态电子–质子关联缩放 $c^{\text{ex}}_{\text{ep}}=1.0$ 。设置为计算前六个激发态，它们对应于质子激发。"
    ```qchem
    $molecule
     0 1
     H  0.0000000000  0.0000000000  0.0000000000
     C  0.0000000000  0.0000000000  -1.058
     N  0.0000000000  0.0000000000  -2.207
    $end
    
    $rem
     neo = true
     purecart = 1111
     neo_purecart = 2222
     neo_vpp = 0
     method = hf
     basis = sto-3g
     scf_convergence = 11
     thresh = 14
     neo_n_scf_convergence = 11
     thresh = 14
     scf_algorithm = diis
     unrestricted = false
     neo_cc2 = 1
     scs = 2
     ep_factor = 940000
     ep_ex_factor = 1000000
     set_roots = 6
     direct_diag = 0
    $end
    
    $neo_basis
    H  1
    S  1  1.0
       4.0 1.0
    P  1  1.0
       4.0 1.0
    ****
    $end
    ```

???+ example "示例 13.36：HeHHe ${}^{+}$ 分子的 NEO-SA-MCSCF 计算输入，其中质子按量子力学方式处理。对 3 个态进行平均。NEO-CASSCF 使用 AH/GDM。"
    ```qchem
    $molecule
    1  1
    He    0.0000  0.0000  0.9000
    He    0.0000  0.0000 -0.9000
    H     0.0000  0.0000  0.0000
    $end
    
    $rem
    input_bohr = false
    mem_total = 32000
    method = hf
    basis = mixed
    use_libqints = 1
    print_general_basis = 0
    scf_algorithm = gdm
    neo_basis_lin_dep_thresh = 3
    neo = true
    neo_vpp = 0
    neo_purecart = 1111
    neo_mcscf = true
    neo_wf_e_docc = 0
    neo_wf_e_cas = 4
    neo_wf_n_cas = 87
    neo_mcscf_sa = true
    neo_mcscf_sa_nstates = 3
    neo_mcscf_nstates = 6
    neo_mcscf_opt_method = 2
    neo_mcscf_macro_conv_thresh = 6
    neo_mcscf_macro_max_iter = 100
    neo_mcscf_emc_conv_thresh = 8
    neo_mcscf_micro_conv_thresh = 8
    neo_mcscf_micro_max_iter = 100000
    neo_mcscf_micro_opt_max_iter = 5
    neo_mcscf_kspace_min = 8
    neo_mcscf_kspace_max = 20
    neo_mcscf_reorder_mos = false
    neo_mcscf_print_mos = false
    neo_mcscf_read_mos = false
    neo_mcscf_print_level = 0
    neo_mcscf_use_prev_ci_iter = 0
    $end
    
    $neo_basis
    H    3
    S    1    1.0
       2.8284  1.0
    S    1    1.0
       4.0000  1.0
    S    1    1.0
       5.6569  1.0
    S    1    1.0
       8.0000  1.0
    S    1    1.0
      11.3137  1.0
    S    1    1.0
      16.0000  1.0
    S    1    1.0
      22.6274  1.0
    S    1    1.0
      32.0000  1.0
    P    1    1.0
       2.8284  1.0
    P    1    1.0
       4.0000  1.0
    P    1    1.0
       5.6569  1.0
    P    1    1.0
       8.0000  1.0
    P    1    1.0
      11.3137  1.0
    P    1    1.0
      16.0000  1.0
    P    1    1.0
      22.6274  1.0
    P    1    1.0
      32.0000  1.0
    D    1    1.0
       2.8284  1.0
    D    1    1.0
       4.0000  1.0
    D    1    1.0
       5.6569  1.0
    D    1    1.0
       8.0000  1.0
    D    1    1.0
      11.3137  1.0
    D    1    1.0
      16.0000  1.0
    D    1    1.0
      22.6274  1.0
    D    1    1.0
      32.0000  1.0
    F    1    1.0
       2.8284  1.0
    F    1    1.0
       4.0000  1.0
    F    1    1.0
       5.6569  1.0
    F    1    1.0
       8.0000  1.0
    F    1    1.0
      11.3137  1.0
    F    1    1.0
      16.0000  1.0
    F    1    1.0
      22.6274  1.0
    F    1    1.0
      32.0000  1.0
    ****
    $end
    
    $basis
    He  1
    6-31g
    ****
    He  2
    6-31g
    ****
    H   3
    def2-QZVP
    ****
    $end
    ```

???+ example "示例 13.37：HeHHe ${}^{+}$ 分子的 NEO-SD ${}_{\text{en}}$ CI 计算输入，其中质子按量子力学方式处理，求解 7 个根。"
    ```qchem
    $molecule
    1  1
    He    0.0000  0.0000  0.9000
    He    0.0000  0.0000 -0.9000
    H     0.0000  0.0000  0.0000
    $end
    
    $rem
    input_bohr = false
    mem_total = 32000
    method = hf
    basis = mixed
    use_libqints = 1
    print_general_basis = 0
    scf_algorithm = gdm
    neo_basis_lin_dep_thresh = 3
    neo = true
    neo_vpp = 0
    neo_purecart = 1111
    neo_wf_e_docc = 2
    neo_wf_e_xlevel = 1
    neo_wf_n_cas = 1
    neo_wf_n_xlevel = 1
    neo_mrci = true
    neo_mrci_max_iter = 1000
    neo_mrci_num_roots = 7
    neo_mrci_kspace_min = 8
    neo_mrci_kspace_max = 15
    neo_mrci_prediag_routine = 1
    neo_mrci_prediag_dim = 1000
    neo_mrci_conv_thresh = 5
    $end
    
    $neo_basis
    H    3
    S    1    1.0
       2.8284  1.0
    S    1    1.0
       4.0000  1.0
    S    1    1.0
       5.6569  1.0
    S    1    1.0
       8.0000  1.0
    S    1    1.0
      11.3137  1.0
    S    1    1.0
      16.0000  1.0
    S    1    1.0
      22.6274  1.0
    S    1    1.0
      32.0000  1.0
    P    1    1.0
       2.8284  1.0
    P    1    1.0
       4.0000  1.0
    P    1    1.0
       5.6569  1.0
    P    1    1.0
       8.0000  1.0
    P    1    1.0
      11.3137  1.0
    P    1    1.0
      16.0000  1.0
    P    1    1.0
      22.6274  1.0
    P    1    1.0
      32.0000  1.0
    D    1    1.0
       2.8284  1.0
    D    1    1.0
       4.0000  1.0
    D    1    1.0
       5.6569  1.0
    D    1    1.0
       8.0000  1.0
    D    1    1.0
      11.3137  1.0
    D    1    1.0
      16.0000  1.0
    D    1    1.0
      22.6274  1.0
    D    1    1.0
      32.0000  1.0
    F    1    1.0
       2.8284  1.0
    F    1    1.0
       4.0000  1.0
    F    1    1.0
       5.6569  1.0
    F    1    1.0
       8.0000  1.0
    F    1    1.0
      11.3137  1.0
    F    1    1.0
      16.0000  1.0
    F    1    1.0
      22.6274  1.0
    F    1    1.0
      32.0000  1.0
    ****
    $end
    
    $basis
    He  1
    6-31g
    ****
    He  2
    6-31g
    ****
    H   3
    def2-QZVP
    ****
    $end
    ```
