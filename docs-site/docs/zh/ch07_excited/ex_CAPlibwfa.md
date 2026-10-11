---
title: "7.9.19 示例"
---

## 7.9.19 示例

（2026 年 7 月 4 日）

???+ example "示例 7.94：甲醛单重激发态的 EOM-EE-OD 与 EOM-EE-CCSD 计算。"
    ```qchem
    $molecule
       0 1
       O
       C  1  R1
       H  2  R2  1  A
       H  2  R2  1  A  3  180.
    
       R1  =  1.4
       R2  =  1.0
       A   =  120.
    $end
    
    $rem
       METHOD      eom-od
       BASIS       6-31+g
       EE_STATES   [2,2,2,2]
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD        eom-ccsd
       BASIS         6-31+g
       EE_SINGLETS   [2,2,2,2]
       EE_TRIPLETS   [2,2,2,2]
    $end
    ```

???+ example "示例 7.95：使用 Cholesky 分解进行水的单重激发态 EOM-EE-CCSD 计算。"
    ```qchem
    $comment
    EOM-EE with Cholesky
    $end
    
    $molecule
       0 1
       O           0.000000    0.000000   -0.069336
       H          -0.759081    0.000000   -0.665332
       H           0.759081    0.000000   -0.665332
    $end
    
    $rem
       METHOD          eom-ccsd
       BASIS           aug-cc-pVDZ
       PURECART        1112
       N_FROZEN_CORE   fc
       CC_T_CONV       4
       CC_E_CONV       6
       CHOLESKY_TOL    2    using CD/1e-2 threshold
       EE_SINGLETS     [2,2,0,0]
    $end
    ```

???+ example "示例 7.96：从自旋三重态 ${}^{3}$ B ${}_{2}$ 参考出发的亚甲基（methylene）EOM-SF-CCSD 计算。"
    ```qchem
    $molecule
       0 3
       C
       H  1   1.1167
       H  1   1.1167   2   102.07
    $end
    
    $rem
       METHOD      eom-ccsd
       BASIS       6-31G*
       SCF_GUESS   core
       SF_STATES   [2,0,0,2]   Two singlet A1 states and singlet and triplet B2 states
    $end
    ```

???+ example "示例 7.97：从自旋三重态 ${}^{3}$ B ${}_{2}$ 参考出发的 SiH ${}_{2}$ EOM-SF-MP2 计算。同时计算能量和性质。"
    ```qchem
    $molecule
       0 3
       Si
       H  1 1.5145
       H  1 1.5145 2 92.68
    $end
    
    $rem
       BASIS            = cc-pVDZ
       UNRESTRICTED     = true
       SCF_CONVERGENCE  = 8
       METHOD           = eom-mp2
       SF_STATES        = [1,1,0,0]
       CC_EOM_PROP_TE   = true   ! Compute <S^2> of excited states
    $end
    ```

???+ example "示例 7.98：使用闭壳层阴离子参考对 NO ${}_{3}$ 进行 EOM-IP-CCSD 计算。"
    ```qchem
    $molecule
       -1 1
       N
       O  1  r1
       O  1  r2   2 A2
       O  1  r2   2 A2    3 180.0
    
       r1 = 1.237
       r2 = 1.237
       A2 = 120.00
    $end
    
    $rem
       METHOD       eom-ccsd
       BASIS        6-31G*
       IP_STATES    [1,1,2,1]    ground and excited  states of the radical
    $end
    ```

???+ example "示例 7.99：使用 FNO、OCCT=99% 的 EOM-IP-CCSD 计算。"
    ```qchem
    $molecule
       0 1
       O
       H  1  1.0
       H  1  1.0  2  100.
    $end
    
    $rem
       METHOD          eom-ccsd
       BASIS           6-311+G(2df,2pd)
       IP_STATES       [3,0,0,0]
       CC_FNO_THRESH   9900        99% of the total natural population recovered
    $end
    ```

???+ example "示例 7.100：使用 CCMAN2 和 Cholesky 分解对水进行 EOM-EE-CC2、EOM-EA-CC2、EOM-IP-CC2 计算。"
    ```qchem
    $molecule
    0 1
       O     0.00000000    0.00000000   -0.69415386
       H    -1.34476814    0.00000000    0.34707675
       H     1.34476814    0.00000000    0.34707675
    $end
    
    $rem
       INPUT_BOHR      ¯¯true
       METHOD          ¯¯eom-cc2
       BASIS           ¯¯6-31g
       CHOLESKY_TOL         3
       EE_STATES        ¯¯[1,1,1,1]
       EA_STATES        ¯¯[1,0,1,1]
       IP_STATES        ¯¯[1,0,1,1]
    $end
    
    ```

???+ example "示例 7.101：使用 LIBGMBPT 模块、RI 近似和自旋标度对水进行 EOM-EE-CC2 计算。"
    ```qchem
    $molecule
    0 1
       O     0.00000000    0.00000000   -0.69415386
       H    -1.34476814    0.00000000    0.34707675
       H     1.34476814    0.00000000    0.34707675
    $end
    
    $rem
       INPUT_BOHR      ¯¯true
       METHOD          ¯¯eom-cc2
       CCMAN2               -1
       BASIS                cc-pvdz
       aux_basis            rimp2-cc-pvdz
       EE_SINGLETS      ¯¯2
       SCS                  1
    $end
    
    ```

???+ example "示例 7.102：H ${}_{2}$ 激发能的 EOM-EE-MP2T 计算。"
    ```qchem
    $molecule
       0 1
       H   0.0000   0.0000   0.0000
       H   0.0000   0.0000   0.7414
    $end
    
    $rem
       THRESH     16
       BASIS      cc-pvdz
       METHOD     eom-mp2t
       EE_STATES  [3,0,0,0,0,0,0,0]
    $end
    ```

???+ example "示例 7.103：苯酚盐阴离子三个低能电离态的 EOM-IP-MP2 计算。"
    ```qchem
    $molecule
       0 1
       C    -0.189057    -1.215927    -0.000922
       H    -0.709319    -2.157526    -0.001587
       C     1.194584    -1.155381    -0.000067
       H     1.762373    -2.070036    -0.000230
       C     1.848872     0.069673     0.000936
       H     2.923593     0.111621     0.001593
       C     1.103041     1.238842     0.001235
       H     1.595604     2.196052     0.002078
       C    -0.283047     1.185547     0.000344
       H    -0.862269     2.095160     0.000376
       C    -0.929565    -0.042566    -0.000765
       O    -2.287040    -0.159171    -0.001759
       H    -2.663814     0.725029     0.001075
    $end
    
    $rem
       METHOD      eom-mp2
       BASIS       6-31+g(d)
       THRESH      14
       IP_STATES   [3]
    $end
    ```

???+ example "示例 7.104：使用用户指定初始猜测的 CN EOM-EA-CCSD 计算。"
    ```qchem
    $molecule
       +1 1
       C
       N  1  1.1718
    $end
    
    $rem
       METHOD          = eom-ccsd
       BASIS          = 6-311+g*
       EA_STATES      = [1,1,1,1]
       CC_EOM_PROP    = true
       EOM_USER_GUESS = true   ! attach to HOMO, HOMO+1, and HOMO+3
    $end
    
    $eom_user_guess
       1  2  4
    $end
    ```

???+ example "示例 7.105：以自旋五重态参考出发的亚甲基 DSF-CIDT 计算。"
    ```qchem
    $molecule
       0 5
       C
       H 1 CH
       H 1 CH 2 HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       METHOD               cisdt
       BASIS                6-31G
       DSF_STATES           [0,2,2,0]
       EOM_NGUESS_SINGLES   0
       EOM_NGUESS_DOUBLES   2
       CCMAN2               0
    $end
    ```

???+ example "示例 7.107：带电荷笼（charged cage）稳定化的亚甲基 EOM-DIP-CCSD 计算。"
    ```qchem
    $molecule
       -2 1
       C   0.000000     0.000000     0.106788
       H  -0.989216     0.000000    -0.320363
       H   0.989216     0.000000    -0.320363
    $end
    
    $rem
       METHOD                   = eom-ccsd
       BASIS                    = 6-311g(d,p)
       SCF_ALGORITHM            = diis_gdm
       CC_SYMMETRY              = false
       DIP_SINGLETS             = [1]  ! Compute one EOM-DIP singlet state
       DIP_TRIPLETS             = [1]  ! Compute one EOM-DIP triplet state
       EOM_DAVIDSON_CONVERGENCE = 5
       CC_EOM_PROP              = true ! Compute excited state properties
       ADD_CHARGED_CAGE         = 2    ! Install a charged sphere around the molecule
       CAGE_RADIUS              = 225  ! Radius = 2.25 A
       CAGE_CHARGE              = 500  ! Charge = +5 a.u.
       CAGE_POINTS              = 100  ! Place 100 point charges
       CC_MEMORY                = 256  ! Use 256Mb of memory, increase for larger jobs
       INTEGRAL_SYMMETRY        = false
    $end
    ```

???+ example "示例 7.106：氰基阳离子（cyano cation）的 EOM-EA-CCSD 计算。我们首先在一个含一个极端弥散轨道的基组中对阳离子进行 Hartree–Fock 计算（ EOM_FAKE_IPEA ），并在第二个作业中使用这些轨道。需要确保该弥散轨道被占据（使用 OCCUPIED 关键字）。由于弥散电子与分子实（core）之间不发生耦合，因此不执行 SCF 迭代。所附着的态表现为电子从弥散轨道被激发到分子轨道的"激发"态。"
    ```qchem
    $molecule
       +1 1
       C
       N 1 bond
    
       bond   1.1718
    $end
    
    $rem
       METHOD            hf
       BASIS             6-311+G*
       PURECART          111
       SCF_CONVERGENCE   8
       EOM_FAKE_IPEA     true
       THRESH            11
       S2THRESH          11
    $end
    
    @@@
    
    $molecule
       0 2
       C
       N 1 bond
    
       bond   1.1718
    $end
    
    $rem
       BASIS            6-311+G*
       PURECART         111
       SCF_GUESS        read
       MAX_SCF_CYCLES   0
       METHOD           eom-ccsd
       CC_DOV_THRESH    2501   use thresh for CC iters with convergence problems
       EE_STATES        [2,0,0,0]
       EOM_FAKE_IPEA    true
    $end
    
    $occupied
       1 2 3 4 5 6 14
       1 2 3 4 5 6
    $end
    ```

???+ example "示例 7.108：使用标度核电荷稳定化方法计算 NO ${}^{-}$ 激发态的 EOM-EE-CCSD 计算。"
    ```qchem
    $molecule
       -1 1
        N  -1.08735    0.0000    0.0000
        O   1.08735    0.0000    0.0000
    $end
    
    $rem
       METHOD               = eom-ccsd
       BASIS                = 6-31g
       INPUT_BOHR           = true
       CC_SYMMETRY          = false
       EE_SINGLETS          = [2]  ! Compute two EOM-EE singlet excited states
       EE_TRIPLETS          = [2]  ! Compute two EOM-EE triplet excited states
       CC_REF_PROP          = true ! Compute ground state properties
       CC_EOM_PROP          = true ! Compute excited state properties
       CC_MEMORY            = 256  ! Use 256Mb of memory, increase for larger jobs
       SCALE_NUCLEAR_CHARGE = 180  ! Adds +1.80e charge to the molecule
       INTEGRAL_SYMMETRY    = false
    $end
    ```

???+ example "示例 7.109：使用 EOM_PRECONV_DOUBLES 对臭氧进行的 EOM-DEA-CCSD 计算。"
    ```qchem
    $molecule
       +2 1
       O
       O 1 1.2724
       O 2 1.2724 1 116.8
    $end
    
    $rem
       METHOD              = eom-ccsd
       BASIS               = 6-31G*
       DEA_SINGLETS        = [1,0,0,0]
       DEA_TRIPLETS        = [0,0,0,1]
       EOM_PRECONV_DOUBLES = true
    $end
    ```

???+ example "示例 7.110：甲酰胺（formamide）的 EOM-EE-CCSD 计算，使用用户指定初始猜测，请求从占据轨道编号 12（2 $A^{\prime\prime}$ ）到虚轨道编号 1（11 $A^{\prime}$ ）的 EE 跃迁。"
    ```qchem
    $molecule
       0 1
       N         1.0706214490   -0.1462996030    0.0000000000
       C        -0.1838756809    0.3832287690    0.0000000000
       O        -1.2178351723   -0.2734201303    0.0000000000
       H         1.8945772136    0.4351761203    0.0000000000
       H         1.1761147729   -1.1515954431    0.0000000000
       H        -0.1740335498    1.4879608698    0.0000000000
    $end
    
    $rem
       METHOD                     EOM-CCSD
       BASIS                      6-31+G(d,p)
       CC_MEMORY                  3000   ccman2 memory
       MEM_STATIC                 250
       CC_T_CONV                  4      T-amplitudes convergence threshold
       CC_E_CONV                  6      Energy convergence threshold
       EE_STATES                  [0,1]  Calculate 1 A" states
       EOM_DAVIDSON_CONVERGENCE   5      Convergence threshold for the Davidson procedure
       !EOM_USER_GUESS             true   Use user guess from $eom_user_guess section
    $end
    
    $eom_user_guess
       12
       1
    $end
    ```

???+ example "示例 7.111：使用投影（projector）技术计算对应于 He* + Ar 的 He-Ar 复合物内价层（inner-valence）激发态。"
    ```qchem
    $comment
    Inner-valence excited states of He-Ar complex, corresponding to He* + Ar
    $end
    
    $molecule
    0 1
    Ar      0.0     0.0     4.0
    He      0.0     0.0     0.0
    $end
    
    
    $rem
    jobtype = sp
    method = ccsd
    basis = aug-cc-pVTZ
    ee_triplets [2,0,1,1]
    ee_singlets [1,0,0,0]
    eom_davidson_convergence = 6
    eom_ee_iv_proj = 2 ! Two orbitals in the inner-valence active space
    cc_eom_prop = 1
    $end
    
    ```

???+ example "示例 7.112：使用投影技术（不施加冻结核）计算水中 O(1s) 电离能的 EOM-IP-CCSD 计算。"
    ```qchem
    $comment
    Ionization of O(1s) orbital in H2O without applying the frozen core
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    $rem
    jobtype = sp
    method = ccsd
    basis = aug-cc-pVTZ
    ip_states [1,0,0,0]
    eom_davidson_convergence = 6
    eom_ip_iv_proj = 1 ! One orbital (O(1s)) in the inner-valence active space
    cc_eom_prop = 1
    n_frozen_core = 0 ! No frozen core orbitals
    $end
    
    ```

???+ example "示例 7.113：N ${}_{2}^{-}$ 的 CAP 增强 EOM-EA-CCSD 计算。aug-cc-pVTZ 基组在质心（COM）处添加了 3 $s$ 3 $p$ 3 $d$ 弥散函数。针对 CAP 强度 $\eta=0.002$ 计算两个 EA 态。"
    ```qchem
    $molecule
       0 1
       N   0.0  0.0 -0.54875676501
       N   0.0  0.0  0.54875676501
       Gh  0.0  0.0  0.0
    $end
    
    $rem
       COMPLEX_CCMAN     1             engage complex_ccman
       METHOD            EOM-CCSD
       BASIS             gen           use general basis
       EA_STATES         [0,0,2,0,0,0,0,0]  compute electron attachment energies
       CC_MEMORY         2000          ccman2 memory
       MEM_TOTAL         4000
       CC_EOM_PROP       true          compute excited state properties
       FORCE_SYMMETRY_ON true
    $end
    
    $complex_ccman
       CS_HF           1     Use complex HF
       CAP_ETA         200   Set strength of CAP potential 0.002
       CAP_X           2760  Set length of the box along x dimension
       CAP_Y           2760  Set length of the box along y dimension
       CAP_Z           4880  Set length of the box along z dimension
       CAP_TYPE        1     Use cuboid CAP
    $end
    
    $basis
    N    0
    aug-cc-pvtz
    ****
    Gh   0
    S    1    1.000000
       2.88000000E-02    1.00000000E+00
    S    1    1.000000
       1.44000000E-02    1.00000000E+00
    S    1    1.000000
       0.72000000E-02    1.00000000E+00
    P    1    1.000000
       2.45000000E-02    1.00000000E+00
    P    1    1.000000
       1.22000000E-02    1.00000000E+00
    P    1    1.000000
       0.61000000E-02    1.00000000E+00
    D    1    1.000000
       0.755000000E-01   1.00000000E+00
    D    1    1.000000
       0.377500000E-01   1.00000000E+00
    D    1    1.000000
       0.188750000E-01   1.00000000E+00
    ****
    $end
    ```

???+ example "示例 7.114：水的 CAP-EOM-EE 计算，包含态性质与跃迁性质的波函数分析。"
    ```qchem
    $molecule
       0 1
       O   0.00000000     0.00000000     0.13594219
       H   0.00000000    -1.44761450    -1.07875060
       H   0.00000000     1.44761450    -1.07875060
    $end
    
    $rem
       METHOD                     eom-ccsd
       BASIS                      6-31G**
       CC_MEMORY                  2000
       MEM_TOTAL                  2500
       SCF_CONVERGENCE            12
       CC_CONVERGENCE             11
       EOM_DAVIDSON_CONVERGENCE   11
       CC_EOM_PROP                TRUE
       CC_FULLRESPONSE            FALSE
       CC_TRANS_PROP              TRUE
       COMPLEX_CCMAN              1
       EE_STATES                  [1,0,2,0]
       INPUT_BOHR                 TRUE
       ! WFA KEYWORDS
       STATE_ANALYSIS             true
       MOLDEN_FORMAT              true
       NTO_PAIRS                  4
       POP_MULLIKEN               true
    $end
    
    $complex_ccman
    CS_HF           1
    CAP_TYPE        1
    CAP_ETA         10000
    CAP_X           2000
    CAP_Y           2500
    CAP_Z           2500
    $end
    ```

???+ example "示例 7.115：使用光滑 Voronoi CAP 计算 CO ${}^{-}$ 中 $\pi^{*}$ 形状共振（shape resonance）的 CAP-EOM-EA-CCSD 计算。"
    ```qchem
    $molecule
       0  1
       C    0.0000   0.0000    0.564
       O    0.0000   0.0000   -0.564
       Gh   0.0000   0.0000    0.000
    $end
    
    $rem
       METHOD             eom-ccsd
       BASIS              gen
       EA_STATES          [0,0,5,0]
       COMPLEX_CCMAN      1
       XC_GRID            000099000590
       N_FROZEN_CORE      fc
       FORCE_SYMMETRY_ON  true
    $end
    
    $complex_ccman
       CS_HF      1
       CAP_TYPE   2
       CAP_ETA    640
       CAP_X      2765
    $end
    
    $basis
    C     0
    S    8    1.000000
       8.23600000E+03    5.31000000E-04
       1.23500000E+03    4.10800000E-03
       2.80800000E+02    2.10870000E-02
       7.92700000E+01    8.18530000E-02
       2.55900000E+01    2.34817000E-01
       8.99700000E+00    4.34401000E-01
       3.31900000E+00    3.46129000E-01
       3.64300000E-01   -8.98300000E-03
    S    8    1.000000
       8.23600000E+03   -1.13000000E-04
       1.23500000E+03   -8.78000000E-04
       2.80800000E+02   -4.54000000E-03
       7.92700000E+01   -1.81330000E-02
       2.55900000E+01   -5.57600000E-02
       8.99700000E+00   -1.26895000E-01
       3.31900000E+00   -1.70352000E-01
       3.64300000E-01    5.98684000E-01
    S    1    1.000000
       9.05900000E-01    1.00000000E+00
    S    1    1.000000
       1.28500000E-01    1.00000000E+00
    S    1    1.000000
       4.40200000E-02    1.00000000E+00
    P    3    1.000000
       1.87100000E+01    1.40310000E-02
       4.13300000E+00    8.68660000E-02
       1.20000000E+00    2.90216000E-01
    P    1    1.000000
       3.82700000E-01    1.00000000E+00
    P    1    1.000000
       1.20900000E-01    1.00000000E+00
    P    1    1.000000
       3.56900000E-02    1.00000000E+00
    D    1    1.000000
       1.09700000E+00    1.00000000E+00
    D    1    1.000000
       3.18000000E-01    1.00000000E+00
    D    1    1.000000
       1.00000000E-01    1.00000000E+00
    F    1    1.000000
       7.61000000E-01    1.00000000E+00
    F    1    1.000000
       2.68000000E-01    1.00000000E+00
    ****
    O     0
    S    8    1.000000
       1.53300000E+04    5.08000000E-04
       2.29900000E+03    3.92900000E-03
       5.22400000E+02    2.02430000E-02
       1.47300000E+02    7.91810000E-02
       4.75500000E+01    2.30687000E-01
       1.67600000E+01    4.33118000E-01
       6.20700000E+00    3.50260000E-01
       6.88200000E-01   -8.15400000E-03
    S    8    1.000000
       1.53300000E+04   -1.15000000E-04
       2.29900000E+03   -8.95000000E-04
       5.22400000E+02   -4.63600000E-03
       1.47300000E+02   -1.87240000E-02
       4.75500000E+01   -5.84630000E-02
       1.67600000E+01   -1.36463000E-01
       6.20700000E+00   -1.75740000E-01
       6.88200000E-01    6.03418000E-01
    S    1    1.000000
       1.75200000E+00    1.00000000E+00
    S    1    1.000000
       2.38400000E-01    1.00000000E+00
    S    1    1.000000
       7.37600000E-02    1.00000000E+00
    P    3    1.000000
       3.44600000E+01    1.59280000E-02
       7.74900000E+00    9.97400000E-02
       2.28000000E+00    3.10492000E-01
    P    1    1.000000
       7.15600000E-01    1.00000000E+00
    P    1    1.000000
       2.14000000E-01    1.00000000E+00
    P    1    1.000000
       5.97400000E-02    1.00000000E+00
    D    1    1.000000
       2.31400000E+00    1.00000000E+00
    D    1    1.000000
       6.45000000E-01    1.00000000E+00
    D    1    1.000000
       2.14000000E-01    1.00000000E+00
    F    1    1.000000
       1.42800000E+00    1.00000000E+00
    F    1    1.000000
       5.00000000E-01    1.00000000E+00
    ****
    Gh      0
    S   1   1.00
          0.0588900              1.0000000
    S   1   1.00
          0.0294450              1.0000000
    S   1   1.00
          0.0147225              1.0000000
    P   1   1.00
          0.0238575              1.0000000
    P   1   1.00
          0.01192875             1.0000000
    P   1   1.00
          0.005964375            1.0000000
    D   1   1.00
          0.0785000              1.0000000
    D   1   1.00
          0.0392500              1.0000000
    D   1   1.00
          0.0196250              1.0000000
    ****
    $end
    ```

???+ example "示例 7.116：H ${}_{2}$ 的投影 CAP-EOM-EE-CCSD 计算，CAP 在 CCSD 步骤中加入。"
    ```qchem
    $molecule
       0 1
       H   0.0000   0.0000   0.0000
       H   0.0000   0.0000   0.7414
    $end
    
    $rem
       METHOD          eom-ccsd
       BASIS           cc-pvdz
       EE_STATES       [5,0,0,0,0,0,0,0]
       COMPLEX_CCMAN   1
       THRESH          16
    $end
    
    $complex_ccman
       PROJ_CAP  1
       CS_HF     0
       CAP_ETA   1000
       CAP_X     2000
       CAP_Y     2000
       CAP_Z     2000
    $end
    ```

???+ example "示例 7.117：H ${}_{2}^{-}$ 前三个态的投影 CAP-EOM-EA-MP2T $\eta-$ 轨迹生成，CAP 在 EOM 步骤施加。"
    ```qchem
    $molecule
       0 1
       H   0.0000   0.0000   0.0000
       H   0.0000   0.0000   0.7414
    $end
    
    $rem
       METHOD          eom-mp2t
       BASIS           cc-pvdz
       EA_STATES       [3,0,0,0,0,0,0,0]
       COMPLEX_CCMAN   1
       THRESH          16
    $end
    
    $complex_ccman
       PROJ_CAP  2
       ETA_STEP  100      ETA step
       CAP_ETA   1000      Initial ETA value
       NSTEPS    20         Number of steps along the trajectory
       CAP_X     2000
       CAP_Y     2000
       CAP_Z     2000
    $end
    ```

???+ example "示例 7.118：投影 CAP-EOM-EA $\eta-$ 轨迹生成。CAP 投影到 N ${}_{2}^{-}$ 的前五个态上。"
    ```qchem
    $molecule
       0 1
       N   0.0  0.0 -0.54875676501
       N   0.0  0.0  0.54875676501
       Gh  0.0  0.0  0.0
    $end
    
    $rem
       COMPLEX_CCMAN     1
       METHOD            EOM-CCSD
       BASIS             gen
       EA_STATES         [0,0,5,0,0,0,0,0]
       FORCE_SYMMETRY_ON true
    $end
    
    $complex_ccman
       PROJ_CAP        3      Project CAP onto set of real EOM eigenvectors
       !PROJ_PROP      1      Request first-order perturbative correction for each point
       CAP_ETA         50
       ETA_STEP        50
       NSTEPS          100
       CAP_X           2760
       CAP_Y           2760
       CAP_Z           4880
       CAP_TYPE        1
    $end
    
    $basis
    N    0
    aug-cc-pvtz
    ****
    Gh   0
    S    1    1.000000
       2.88000000E-02    1.00000000E+00
    S    1    1.000000
       1.44000000E-02    1.00000000E+00
    S    1    1.000000
       0.72000000E-02    1.00000000E+00
    P    1    1.000000
       2.45000000E-02    1.00000000E+00
    P    1    1.000000
       1.22000000E-02    1.00000000E+00
    P    1    1.000000
       0.61000000E-02    1.00000000E+00
    D    1    1.000000
       0.755000000E-01   1.00000000E+00
    D    1    1.000000
       0.377500000E-01   1.00000000E+00
    D    1    1.000000
       0.188750000E-01   1.00000000E+00
    ****
    $end
    ```

???+ example "示例 7.119：水的 CBF-EOM-EA-CCSD 计算。"
    ```qchem
    $molecule
    0 1
    H          0.00000        0.53835       -0.78304
    O          0.00000       -0.01840        0.00000
    H          0.00000        0.53835        0.78304
    $end
    
    $rem
       METHOD                       ccsd
       BASIS                        cc-pvdz ! important: use gen basis set
       COMPLEX_BASIS                aug-cc-pvdz ! important: use gen basis set
       PURECART                     1111
       EA_STATES                    [1,0,0,1]
       COMPLEX_CCMAN                true
       COMPLEX_EXPONENTS            true
       COMPLEX_THETA                100
       COMPLEX_SCF                  1
       COMPLEX_SCF_GUESS            true
       GEN_SCFMAN                   true
       COMPLEX_METSCF               true
       COMPLEX_N_ELECTRONS          false
       N_FROZEN_CORE                false
       SCF_CONVERGENCE              11
       CC_CONVERGENCE               10
       EOM_DAVIDSON_CONVERGENCE     10
       THRESH                       14
    $end
    
    $complex_ccman
    cs_alpha 100
    $end
    ```

???+ example "示例 7.120：使用分辨率恒等（Resolution-of-the-Identity）近似的水的 CAP-EOM-EE-CC2 计算。"
    ```qchem
    $molecule
       0 1
       H          0.00000        0.53835       -0.78304
       O          0.00000       -0.01840        0.00000
       H          0.00000        0.53835        0.78304
    $end
    
    $rem
       METHOD                       cc2
       BASIS                        cc-pvdz
       AUX_BASIS                    rimp2-cc-pvdz
       EA_STATES                    [1,0,0,1]
       COMPLEX_CCMAN                true
       N_FROZEN_CORE                false
       SCF_CONVERGENCE              11
       CC_CONVERGENCE               10
       EOM_DAVIDSON_CONVERGENCE     10
    $end
    
    $complex_ccman
    CS_HF     1
    CAP_ETA   1000
    CAP_X     2760
    CAP_Y     2760
    CAP_Z     4970
    CAP_TYPE  1
    $end
    ```

???+ example "示例 7.121：使用 LIBGMBPT 模块对 N ${}_{2}^{-}$ 进行 CAP-RI-EA-CC2 计算。计算共振态所实际使用基组的详细信息可见参考文献 1382 Utku C., Paran G. P., Jagau T.C. J. Chem. Phys. (2025) , 163 , pp. 244103 . 链接 。"
    ```qchem
    $molecule
    0 1
    N   0.0000000000 0.0000000000  0.5487567500
    N   0.0000000000 0.0000000000 -0.5487567500
    $end
    
    $rem
    jobtype           sp
    mem_total         10000
    ccman2            -1
    complex_ccman     1
    method            cc2
    ea_states         8
    n_frozen_core     0
    basis             gen ! aug-cc-pVDZ + 3s3p(A)
    aux_basis         gen ! rimp2-aug-cc-pVDZ
    scf_convergence   10
    cc_convergence    10
    eom_davidson_convergence  8
    eom_davidson_maxvectors   300
    eom_davidson_max_iter     200
    $end
    
    $complex_ccman
    cs_hf          1
    cap_eta        150
    cap_x          2760
    cap_y          2760
    cap_z          4880
    cap_type       1
    $end
    
    $basis
    N     0
    S   9   1.00
          9.046000D+03           7.000000D-04
          1.357000D+03           5.389000D-03
          3.093000D+02           2.740600D-02
          8.773000D+01           1.032070D-01
          2.856000D+01           2.787230D-01
          1.021000D+01           4.485400D-01
          3.838000D+00           2.782380D-01
          7.466000D-01           1.544000D-02
          2.248000D-01          -2.864000D-03
    S   9   1.00
          9.046000D+03          -1.530000D-04
          1.357000D+03          -1.208000D-03
          3.093000D+02          -5.992000D-03
          8.773000D+01          -2.454400D-02
          2.856000D+01          -6.745900D-02
          1.021000D+01          -1.580780D-01
          3.838000D+00          -1.218310D-01
          7.466000D-01           5.490030D-01
          2.248000D-01           5.788150D-01
    S   1   1.00
          2.248000D-01           1.000000D+00
    S   1   1.00
          0.0612400              1.0000000
    S   1   1.00
          0.0306200              1.0000000
    S   1   1.00
          0.0153100              1.0000000
    S   1   1.00
          0.0076550              1.0000000
    P   4   1.00
          1.355000D+01           3.991900D-02
          2.917000D+00           2.171690D-01
          7.973000D-01           5.103190D-01
          2.185000D-01           4.622140D-01
    P   1   1.00
          2.185000D-01           1.000000D+00
    P   1   1.00
          0.0561100              1.0000000
    P   1   1.00
          0.0280550              1.0000000
    P   1   1.00
          0.0140275              1.0000000
    P   1   1.00
          0.00701375             1.0000000
    D   1   1.00
          8.170000D-01           1.0000000
    D   1   1.00
          0.2300000              1.0000000
    ****
    $end
    
    $aux_basis
    N     0
    S   1   1.00
         87.6864                 1.0000000
    S   1   1.00
         20.4679                 1.0000000
    S   1   1.00
          7.62436                1.0000000
    S   1   1.00
          2.34426                1.0000000
    S   1   1.00
          1.12324                1.0000000
    S   1   1.00
          0.723539               1.0000000
    S   1   1.00
          0.327261               1.0000000
    S   1   1.00
          0.10361182811          1.0000000
    P   1   1.00
         29.2373                 1.0000000
    P   1   1.00
          8.55299                1.0000000
    P   1   1.00
          2.53364                1.0000000
    P   1   1.00
          1.09461                1.0000000
    P   1   1.00
          0.461104               1.0000000
    P   1   1.00
          0.16968199389          1.0000000
    D   1   1.00
         12.3278                 1.0000000
    D   1   1.00
          3.42816                1.0000000
    D   1   1.00
          1.28537                1.0000000
    D   1   1.00
          0.47785                1.0000000
    D   1   1.00
          0.13349941560          1.0000000
    F   1   1.00
          3.40118                1.0000000
    F   1   1.00
          1.33473                1.0000000
    F   1   1.00
          0.41976031664          1.0000000
    ****
    $end
    ```

???+ example "示例 7.122：使用 LIBGMBPT 模块对 N ${}_{2}^{-}$ 进行 CBF-RI-EA-CC2 计算。计算共振态所实际使用基组的详细信息可见参考文献 1382 Utku C., Paran G. P., Jagau T.C. J. Chem. Phys. (2025) , 163 , pp. 244103 . 链接 。"
    ```qchem
    $molecule
    0 1
    N     0.0   0.0   -0.54875676501
    N     0.0   0.0    0.54875676501
    $end
    
    $rem
    MEM_TOTAL               10000
    COMPLEX_CCMAN           1
    CCMAN2                  1
    METHOD                  CC2
    BASIS                   gen ! aug-cc-pvtz+1s1p1d(A)
    COMPLEX_BASIS           gen ! aug-cc-pvtz+3s3p3d(A)
    AUX_BASIS               gen ! rimp2-aug-cc-pvtz
    COMPLEX_AUX_BASIS       gen ! rimp2-aug-cc-pvtz
    PURECART                111111
    EA_STATES               [0,0,3,0,0,0,0,0]
    SCF_CONVERGENCE         10
    CC_CONVERGENCE          10
    EOM_DAVIDSON_CONV       8
    N_FROZEN_CORE           0
    THRESH                  14
    complex_exponents       1
    complex_theta           270
    complex_scf             1
    complex_scf_guess       1
    complex_n_electrons     0
    $end
    
    $complex_ccman
    cs_alpha                1000
    $end
    
    $basis ! aug-cc-pvtz+1s1p1d(A)
    N     0
    S   10   1.00
          1.142000D+04           5.230000D-04
          1.712000D+03           4.045000D-03
          3.893000D+02           2.077500D-02
          1.100000D+02           8.072700D-02
          3.557000D+01           2.330740D-01
          1.254000D+01           4.335010D-01
          4.644000D+00           3.474720D-01
          1.293000D+00           4.126200D-02
          5.118000D-01          -8.508000D-03
          1.787000D-01           2.384000D-03
    S   1   1.00
          1.293000D+00           1.000000D+00
    S   10   1.00
          1.142000D+04          -1.150000D-04
          1.712000D+03          -8.950000D-04
          3.893000D+02          -4.624000D-03
          1.100000D+02          -1.852800D-02
          3.557000D+01          -5.733900D-02
          1.254000D+01          -1.320760D-01
          4.644000D+00          -1.725100D-01
          1.293000D+00           1.518140D-01
          5.118000D-01           5.999440D-01
          1.787000D-01           3.874620D-01
    S   1   1.00
          1.787000D-01           1.000000D+00
    S   1   1.00
          0.0576000              1.0000000
    P   1   1.00
          5.550000D-01           1.000000D+00
    P   5   1.00
          2.663000D+01           1.467000D-02
          5.948000D+00           9.176400D-02
          1.742000D+00           2.986830D-01
          5.550000D-01           4.984870D-01
          1.725000D-01           3.370230D-01
    P   1   1.00
          1.725000D-01           1.000000D+00
    P   1   1.00
          0.0491000              1.0000000
    D   1   1.00
          1.654000D+00           1.000000D+00
    D   1   1.00
          4.690000D-01           1.000000D+00
    D   1   1.00
          0.1510000              1.0000000
    F   1   1.00
          1.093000D+00           1.0000000
    F   1   1.00
          0.3640000              1.0000000
    S   1   1.00
          0.0288000              1.0000000
    P   1   1.00
          0.0245500              1.0000000
    D   1   1.00
          0.0755000              1.0000000
    ****
    $end
    
    $zbasis ! aug-cc-pvtz+3s3p3d(A)
    N  0
    S   10   1.00
          1.142000D+04           5.230000D-04
          1.712000D+03           4.045000D-03
          3.893000D+02           2.077500D-02
          1.100000D+02           8.072700D-02
          3.557000D+01           2.330740D-01
          1.254000D+01           4.335010D-01
          4.644000D+00           3.474720D-01
          1.293000D+00           4.126200D-02
          5.118000D-01          -8.508000D-03
          1.787000D-01           2.384000D-03
    S   1   1.00
          1.293000D+00           1.000000D+00
    S   10   1.00
          1.142000D+04          -1.150000D-04
          1.712000D+03          -8.950000D-04
          3.893000D+02          -4.624000D-03
          1.100000D+02          -1.852800D-02
          3.557000D+01          -5.733900D-02
          1.254000D+01          -1.320760D-01
          4.644000D+00          -1.725100D-01
          1.293000D+00           1.518140D-01
          5.118000D-01           5.999440D-01
          1.787000D-01           3.874620D-01
    S   1   1.00
          1.787000D-01           1.000000D+00
    S   1   1.00
          0.0576000              1.0000000
    P   1   1.00
          5.550000D-01           1.000000D+00
    P   5   1.00
          2.663000D+01           1.467000D-02
          5.948000D+00           9.176400D-02
          1.742000D+00           2.986830D-01
          5.550000D-01           4.984870D-01
          1.725000D-01           3.370230D-01
    P   1   1.00
          1.725000D-01           1.000000D+00
    P   1   1.00
          0.0491000              1.0000000
    D   1   1.00
          1.654000D+00           1.000000D+00
    D   1   1.00
          4.690000D-01           1.000000D+00
    D   1   1.00
          0.1510000              1.0000000
    F   1   1.00
          1.093000D+00           1.0000000
    F   1   1.00
          0.3640000              1.0000000
    S   1   1.00
          0.0288000              1.0000000
    S   1   1.00
          0.0144000              1.0000000
    S   1   1.000
          0.0072000              1.0000000
    P   1   1.00
          0.0245500              1.0000000
    P   1   1.00
          0.0122750              1.0000000
    P   1   1.000
          0.0061375              1.0000000
    D   1   1.00
          0.0755000              1.0000000
    D   1   1.00
          0.0377500              1.0000000
    D   1   1.000
          0.0188750              1.0000000
    ****
    $end
    
    $aux_basis
    N     0
    S   1   1.00
        287.50926947             1.0000000
    S   1   1.00
         64.276030898            1.0000000
    S   1   1.00
         21.681924016            1.0000000
    S   1   1.00
          7.9068743193           1.0000000
    S   1   1.00
          2.4319673913           1.0000000
    S   1   1.00
          1.2226681474           1.0000000
    S   1   1.00
          0.76674827356          1.0000000
    S   1   1.00
          0.31158846994          1.0000000
    S   1   1.00
          0.10109736226          1.0000000
    P   1   1.00
         34.965027371            1.0000000
    P   1   1.00
         10.323896648            1.0000000
    P   1   1.00
          2.8981582643           1.0000000
    P   1   1.00
          1.4077404555           1.0000000
    P   1   1.00
          0.85083386536          1.0000000
    P   1   1.00
          0.37353274145          1.0000000
    P   1   1.00
          0.14810183674          1.0000000
    D   1   1.00
         13.908637089            1.0000000
    D   1   1.00
          4.5847232531           1.0000000
    D   1   1.00
          2.2101848651           1.0000000
    D   1   1.00
          0.83768301209          1.0000000
    D   1   1.00
          0.41948375608          1.0000000
    D   1   1.00
          0.13410649139          1.0000000
    F   1   1.00
          3.4730665788           1.0000000
    F   1   1.00
          1.5589463548           1.0000000
    F   1   1.00
          0.84677638239          1.0000000
    F   1   1.00
          0.28858743337          1.0000000
    G   1   1.00
          1.7764066281           1.0000000
    G   1   1.00
          0.59981188305          1.0000000
    ****
    $end
    
    $aux_zbasis
    N     0
    S   1   1.00
        287.50926947             1.0000000
    S   1   1.00
         64.276030898            1.0000000
    S   1   1.00
         21.681924016            1.0000000
    S   1   1.00
          7.9068743193           1.0000000
    S   1   1.00
          2.4319673913           1.0000000
    S   1   1.00
          1.2226681474           1.0000000
    S   1   1.00
          0.76674827356          1.0000000
    S   1   1.00
          0.31158846994          1.0000000
    S   1   1.00
          0.10109736226          1.0000000
    P   1   1.00
         34.965027371            1.0000000
    P   1   1.00
         10.323896648            1.0000000
    P   1   1.00
          2.8981582643           1.0000000
    P   1   1.00
          1.4077404555           1.0000000
    P   1   1.00
          0.85083386536          1.0000000
    P   1   1.00
          0.37353274145          1.0000000
    P   1   1.00
          0.14810183674          1.0000000
    D   1   1.00
         13.908637089            1.0000000
    D   1   1.00
          4.5847232531           1.0000000
    D   1   1.00
          2.2101848651           1.0000000
    D   1   1.00
          0.83768301209          1.0000000
    D   1   1.00
          0.41948375608          1.0000000
    D   1   1.00
          0.13410649139          1.0000000
    F   1   1.00
          3.4730665788           1.0000000
    F   1   1.00
          1.5589463548           1.0000000
    F   1   1.00
          0.84677638239          1.0000000
    F   1   1.00
          0.28858743337          1.0000000
    G   1   1.00
          1.7764066281           1.0000000
    G   1   1.00
          0.59981188305          1.0000000
    ****
    $end
    ```

???+ example "示例 7.123：甲醛，计算 3 个价层电离态的 EOM-IP-CCSD-S(D) 和 EOM-IP-MP2-S(D) 能量。"
    ```qchem
    $molecule
       0 1
       C
       H  1  1.096135
       H  1  1.096135  2  116.191164
       O  1  1.207459  2  121.904418  3  -180.000000 0
    $end
    
    $rem
       METHOD       eom-ccsd-s(d)
       BASIS        6-31G*
       IP_STATES    [1,0,1,1]
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD       eom-mp2-s(d)
       BASIS        6-31G*
       IP_STATES    [1,0,1,1]
    $end
    ```

???+ example "示例 7.124：甲醛，使用 C-PCM 方法计算 EOM-EE-CCSD 态。"
    ```qchem
    $molecule
       0 1
       O
       C   1  1.4
       H   2  1.0  1  120.
       H   2  1.0  1  120.  3  180.0
    $end
    
    $rem
       METHOD           eom-ccsd
       BASIS            cc-pvdz
       EE_STATES        [4]
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       theory          cpcm
    $end
    
    $solvent
       dielectric      4.34
       dielectric_infi 1.829
    $end
    ```

???+ example "示例 7.125：NO ${}_{2}^{-}$ ，使用 C-PCM 方法计算 EOM-IP-CCSD 态。"
    ```qchem
    $molecule
       -1 1
       N1
       O2 N1 RNO
       O3 N1 RNO O2 AONO
    
       RNO  = 1.305
       AONO = 106.7
    $end
    
    $rem
       METHOD           eom-ccsd
       BASIS            cc-pvdz
       IP_STATES        [2]
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       theory          cpcm
    $end
    
    $solvent
       dielectric      4.34
       dielectric_infi 1.829
    $end
    ```
