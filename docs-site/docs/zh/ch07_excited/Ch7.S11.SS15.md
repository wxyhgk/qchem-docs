---
title: "7.11.15 示例"
---

## 7.11.15 示例

（2026 年 7 月 4 日）

???+ example "示例 7.191：使用 RASCI1 对 DDMX 四自由基的三个态进行 RAS-2SF-CI 计算的输入。活性空间（RAS2）包含 ROHF 五重态参考中 $4$ 个单占据轨道上的 $4$ 个电子。同时请求自然轨道占据数。"
    ```qchem
    $molecule
       0 5
       C      0.000000    0.000000    1.092150
       C     -1.222482    0.000000    0.303960
       C     -2.390248    0.000000    1.015958
       H     -2.344570    0.000000    2.095067
       H     -3.363161    0.000000    0.537932
       C     -1.215393    0.000000   -1.155471
       H     -2.150471    0.000000   -1.702536
       C      0.000000    0.000000   -1.769131
       C      1.215393    0.000000   -1.155471
       H      2.150471    0.000000   -1.702536
       C      1.222482    0.000000    0.303960
       C      2.390248    0.000000    1.015958
       H      2.344570    0.000000    2.095067
       H      3.363161    0.000000    0.537932
    $end
    
    $rem
       EXCHANGE        hf
       CORRELATION     rasci
       BASIS           6-31g
       UNRESTRICTED    false
       MEM_TOTAL       4000
       MEM_STATIC      100
       RAS_ROOTS       3
       RAS_ACT         4
       RAS_ELEC        4
       RAS_OCC         25
       RAS_SPIN_MULT   0
       RAS_NATORB      true
       SYMMETRY        true
    $end
    ```

???+ example "示例 7.192：使用 RASCI1 程序，以双阴离子闭壳层 F ${}_{2}^{2-}$ 作为参考行列式，对 F ${}_{2}$ 分子的三重态进行 RAS-2IP-CI 计算的输入。"
    ```qchem
    $molecule
       -2 1
       F
       F  1  1.4136
    $end
    
    $rem
       EXCHANGE        hf
       CORRELATION     rasci
       BASIS           cc-pVTZ
       MEM_TOTAL       4000
       MEM_STATIC      100
       RAS_ROOTS       2
       RAS_ACT         6
       RAS_ELEC        10
       RAS_OCC         4
       RAS_SPIN_MULT   3
    $end
    ```

???+ example "示例 7.193：对水分子进行 FCI/STO-3G 计算的输入，将 RAS2 空间扩展到整个分子轨道集合。使用 RAS-CI 程序。"
    ```qchem
    $molecule
       0 1
       O   0.000  0.000   0.120
       H  -0.762  0.000  -0.479
       H   0.762  0.000  -0.479
    $end
    
    $rem
       EXCHANGE        hf
       CORRELATION     rasci
       BASIS           sto-3g
       MEM_TOTAL       4000
       MEM_STATIC      100
       RAS_ROOTS       1
       RAS_ACT         7
       RAS_ELEC        10
       RAS_OCC         0
       RAS_SPIN_MULT   1
       RAS_DO_HOLE     false
       RAS_DO_PART     false
    $end
    ```

???+ example "示例 7.194：使用 RASCI2 对卡宾（亚甲基）进行单自旋翻转（single spin-flip）计算"
    ```qchem
    $molecule
       0 3
       C     0.0000000    0.0000000    0.0000000
       H    -0.8611113    0.0000000    0.6986839
       H     0.8611113    0.0000000    0.6986839
    $end
    
    $rem
       EXCHANGE       HF
       CORRELATION    RASCI2
       BASIS          cc-pVDZ
       AUX_BASIS      rimp2-cc-pVDZ
       UNRESTRICTED   false
       RAS_ACT_OCC    1    ! # alpha electrons
       RAS_ACT_VIR    1    ! # virtuals in active space
       RAS_ACT_DIFF   0    ! # set to 1 for odd # of e-s
       RAS_N_ROOTS    4
       MAX_CIS_CYCLES 25   ! number of iterations in RASCI
    $end
    ```

???+ example "示例 7.195：相距 10 Å 的两个卡宾（亚甲基）分子；使用 RASCI2 进行双自旋翻转（double spin-flip）计算。注意，在三重简并的基态下，此情形的 $\langle\hat{S}^{2}\rangle$ 值并非唯一定义。"
    ```qchem
    $molecule
       0 5
       C     0.0000000     0.0000000    0.0000000
       H    -0.8611113     0.0000000    0.6986839
       H     0.8611113     0.0000000    0.6986839
       C     0.0000000    10.0000000    0.0000000
       H    -0.8611113    10.0000000    0.6986839
       H     0.8611113    10.0000000    0.6986839
    $end
    
    $rem
       EXCHANGE       HF
       CORRELATION    RASCI2
       BASIS          cc-pVDZ
       AUX_BASIS      rimp2-cc-pVDZ
       RAS_ACT_OCC    2    ! # alpha electrons
       RAS_ACT_VIR    2    ! # virtuals in active space
       RAS_ACT_DIFF   0    ! # set to 1 for odd # of e-s
       UNRESTRICTED   false
       RAS_N_ROOTS    8
       MAX_CIS_CYCLES 25
    $end
    ```

???+ example "示例 7.196：使用双自旋翻转（double spin-flip）对氮分子阳离子进行 RASCI2 计算。"
    ```qchem
    $molecule
       1 6
       N
       N   1  4.5
    $end
    
    $rem
       EXCHANGE           HF
       CORRELATION        RASCI2
       BASIS              6-31G*
       AUX_BASIS          rimp2-VDZ
       RAS_ACT_OCC        3   ! # alpha electrons
       RAS_ACT_VIR        3   ! # virtuals in active space
       RAS_ACT_DIFF       1   ! # for odd # e-s, cation
       UNRESTRICTED       false
       N_FROZEN_CORE      2
       N_FROZEN_VIRTUAL   2
       RAS_N_ROOTS        8
       MAX_CIS_CYCLES     25
    $end
    ```

???+ example "示例 7.197：使用 casman 对氮双聚体进行 CAS-1SF 计算。"
    ```qchem
    $rem
     exchange                hf
     correlation             sf-cas
     cas_level_shift         0
     basis                   6-31g*
     aux_basis               rimp2-vdz
     unrestricted            0
     scf_guess               core
     integral_symmetry       0
     point_group_symmetry    false
    $end
    
    $molecule
    0 7
    N
    N,1,R1
    
    R1 2.5
    $end
    ```

???+ example "示例 7.198：使用 casman 对氮双聚体进行 RAS(3x)+D-1SF 计算。"
    ```qchem
    $rem
     exchange                hf
     correlation             sf-cas(3x)+D
     ras_roots               10
     basis                   6-31g*
     aux_basis               rimp2-vdz
     unrestricted            0
     scf_guess               read
     integral_symmetry       0
     point_group_symmetry    false
    $end
    
    $molecule
    0 7
    N
    N,1,R1
    
    R1 2.5
    $end
    ```

???+ example "示例 7.199：使用 casman 对氮双聚体阳离子进行自定义 SF-CAS(2x)2 计算。"
    ```qchem
    $rem
     exchange                hf
     correlation             sf-cas
     cas_do_2x               1
     cas_qdpt_order          2
     cas_level_shift         107
     ras_roots               10
     basis                   6-31g*
     aux_basis               rimp2-vdz
     unrestricted            0
     scf_guess               core
     integral_symmetry       0
     point_group_symmetry    false
    $end
    
    $molecule
    0 5
    O
    H,1,R1
    H,1,R1,2,109.5
    
    R1 2.0
    $end
    ```

???+ example "示例 7.200：使用 librassf 对氮双聚体的四重态进行 RAS(h,p)-1SF 计算。"
    ```qchem
    $molecule
       0 7
       N
       N   1   1.75
    $end
    
    $rem
       EXCHANGE            HF
       CORRELATION         RASCI2
       BASIS               cc-pvdz
       LIBRASSF            1
       RASSF_GUESS         1
       RASSF_DELTA_ALPHA   1
       RASSF_DELTA_BETA    1
       RAS_N_ROOTS         4
       RAS_DO_HOLE         1
       RAS_DO_PART         1
       RAS_NATORB          0
    $end
    ```

???+ example "示例 7.201：使用 librassf 对氮分子阳离子进行 RAS(h)-1SF-IP 计算。"
    ```qchem
    $molecule
       0 7
       N
       N   1   1.75
    $end
    
    $rem
       EXCHANGE            HF
       CORRELATION         RASCI2
       BASIS               cc-pvdz
       LIBRASSF            1
       RASSF_GUESS         1
       RASSF_DELTA_ALPHA   1
       RASSF_DELTA_BETA    1
       RAS_N_ROOTS         4
       RAS_DO_HOLE         1
       RAS_DO_PART         1
       RAS_NATORB          0
    $end
    ```

???+ example "示例 7.202：使用 RASCI2 方法（双自旋翻转）对 HSiCl 分子进行自旋-轨道耦合（SOC）计算。本示例中未请求自然跃迁轨道（NTO）分析。"
    ```qchem
    $molecule
       0 1
       Si    0.00000    0.00000    0.00000
       H     1.56100    0.00000    0.00000
       Cl   -0.45728    2.01271    0.00000
    $end
    
    $rem
       EXCHANGE          HF
       CORRELATION       RASCI2
       BASIS             cc-pVDZ
       AUX_BASIS         rimp2-cc-pVDZ
       UNRESTRICTED      false
       RAS_ACT_OCC       2    ! # alpha electrons
       RAS_ACT_VIR       2    ! # virtuals in active space
       RAS_ACT_DIFF      0    ! # set to 1 for odd # of e-s
       RAS_N_ROOTS       8
       MAX_CIS_CYCLES    25
       N_FROZEN_CORE     fc
       N_FROZEN_VIRTUAL  0
       RAS_CALC_SOC      true
    $end
    ```

???+ example "示例 7.203：使用 RASCI2 方法（双自旋翻转）对苯乙酮分子进行自旋-轨道耦合（SOC）计算，随后进行自然跃迁轨道（NTO）分析。"
    ```qchem
    $molecule
       0 1
       C   -2.517371    0.513126    0.001828
       C   -1.316451   -0.371636    0.001013
       C   -1.553894   -1.827349    0.000191
       C   -2.806559   -2.314044   -0.001563
       C   -3.962422   -1.432985   -0.002120
       C   -3.757473   -0.015730    0.000047
       C   -0.030094    0.202242    0.001108
       C    1.208765   -0.658368   -0.000434
       O    0.079290    1.457055    0.003022
       H    2.079440   -0.009753   -0.004191
       H   -0.705807   -2.494690    0.000993
       H   -2.970202   -3.383004   -0.002372
       H   -4.958256   -1.847303   -0.003648
       H   -4.620034    0.636483    0.000372
       H   -2.340078    1.575881    0.003550
       H    1.252514   -1.299975    0.880472
       H    1.247817   -1.304378   -0.878269
    $end
    
    $rem
       EXCHANGE          HF
       CORRELATION       RASCI2
       BASIS             cc-pVDZ
       AUX_BASIS         rimp2-cc-pVDZ
       UNRESTRICTED      false
       RAS_ACT_OCC       2    ! # alpha electrons
       RAS_ACT_VIR       2    ! # virtuals in active space
       RAS_ACT_DIFF      0    ! # set to 1 for odd # of e-s
       RAS_N_ROOTS       4
       MAX_CIS_CYCLES    25
       N_FROZEN_CORE     fc
       N_FROZEN_VIRTUAL  0
       RAS_CALC_SOC      true
       MOLDEN_FORMAT     true
       NTO_PAIRS         2
    $end
    ```
