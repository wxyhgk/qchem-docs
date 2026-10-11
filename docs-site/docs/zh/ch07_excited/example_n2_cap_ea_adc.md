---
title: "7.10.14 示例"
---

## 7.10.14 示例

（2026 年 7 月 4 日）

???+ example "示例 7.181: 采用 $D_{2}$ 对称性对甲烷单重激发态进行 ADC(2)-s 计算的输入文件。共请求六个激发态，对应于不可约表示 $B_{1}$（$B_{2}$）的四个（两个）电子跃迁。"
    ```qchem
    $molecule
       0 1
       C
       H   1 r0
       H   1 r0   2  d0
       H   1 r0   2  d0   3  d1
       H   1 r0   2  d0   4  d1
    
       r0 = 1.085
       d0 = 109.4712206
       d1 = 120.0
    $end
    
    $rem
       METHOD              adc(2)
       BASIS               6-31g(d,p)
       MEM_TOTAL           4000
       MEM_STATIC          100
       EE_SINGLETS         [0,4,2,0]
    $end
    ```

???+ example "示例 7.182: 采用 $C_{1}$ 对称性并使用 DIIS 的非限制 RI-ADC(2)-s 计算的输入文件。此外，还计算了激发态性质及态-态（state-to-state）性质。"
    ```qchem
    $molecule
       0 2
       C    0.0    0.0   -0.630969
       N    0.0    0.0    0.540831
    $end
    
    $rem
       METHOD           adc(2)
       BASIS            aug-cc-pVDZ
       AUX_BASIS        rimp2-aug-cc-pVDZ
       MEM_TOTAL        4000
       MEM_STATIC       100
       CC_SYMMETRY      false
       EE_STATES        6
       ADC_DO_DIIS      true
       ADC_PROP_ES      true
       ADC_PROP_ES2ES   true
       ADC_PROP_TPA     true
    $end
    ```

???+ example "示例 7.183: 采用 $C_{1}$ 对称性、使用 4 个并行 CPU 核的限制性 CVS-ADC(2)-x 计算的输入文件。"
    ```qchem
    $molecule
       0 1
       N     1.0706214490   -0.1462996030    0.0000000000
       C    -0.1838756809    0.3832287690    0.0000000000
       O    -1.2178351723   -0.2734201303    0.0000000000
       H     1.8945772136    0.4351761203    0.0000000000
       H     1.1761147729   -1.1515954431    0.0000000000
       H    -0.1740335498    1.4879608698    0.0000000000
    $end
    
    $rem
       METHOD                      cvs-adc(2)-x
       BASIS                       6-31G*
       EE_SINGLETS                 5
       ADC_DAVIDSON_MAXSUBSPACE    60
       MEM_TOTAL                   10000
       MEM_STATIC                  1000
       THREADS                     4
       CC_SYMMETRY                 false
       ADC_DAVIDSON_THRESH         8
       ADC_DAVIDSON_MAXITER        900
       ADC_CVS                     true
       CC_REST_OCC                 4
       INTEGRAL_SYMMETRY           false
    $end
    ```

???+ example "示例 7.184: 在无点群对称性条件下对环丁二烯的前三个自旋翻转（spin-flip）目标态进行限制性 SF-ADC(2)-s 计算的输入文件。"
    ```qchem
    $molecule
       0 3
       C     0.000000     0.000000     0.000000
       C     1.439000     0.000000     0.000000
       C     1.439000     0.000000     1.439000
       C     0.000000     0.000000     1.439000
       H    -0.758726     0.000000    -0.758726
       H     2.197726     0.000000    -0.758726
       H     2.197726     0.000000     2.197726
       H    -0.758726     0.000000     2.197726
    $end
    
    $rem
       METHOD          adc(2)
       MEM_TOTAL       15000
       MEM_STATIC      1000
       CC_SYMMETRY     false
       BASIS           3-21G
       SF_STATES       3
    $end
    ```

???+ example "示例 7.185: 使用 BWs-ADC(2) 计算每个不可约表示的前 5 个单重态和三重态。正则化参数选取为 $A_{0}=4$ 和 $B_{0}=0$ 。"
    ```qchem
    $comment
    Calculation of the first 5 singlet and triplet states of formaldehyde.
    Method: BWs-ADC(2)
    
    The following regularisation parameters are used:
    A0: 4.0
    B0: 0.0
    $end
    
    $molecule
    0 1
    C      0.000000    0.000000    0.000000
    O      1.224631    0.000000    0.000000
    H     -0.587649   -0.044717   -0.930811
    H     -0.587649    0.044717    0.930811
    $end
    
    $rem
    ! Set the method to RIBWS2
    METHOD = RIBWS2
    
    ! Both BASIS and AUX_BASIS (or AUX_BASIS_CORR) are required
    BASIS = AUG-CC-PVTZ
    AUX_BASIS = RIMP2-AUG-CC-PVTZ
    
    ! Memory specifications for adcman
    MEM_TOTAL = 50000
    MEM_STATIC = 5000
    
    ! Specifying the number of excited states
    EE_SINGLETS = 5
    EE_TRIPLETS = 5
    $end
    
    $bws2
    METHOD = MPRBWS2        ! Activate the (A0, B0) model
    MPR_A0 = 4000           ! Set A0 = 4
    MPR_B0 = 0              ! Set B0 = 0
    EXC_METHOD = ADC(2)     ! Activate BWs-ADC(2)
    $end
    ```

下面的示例演示了对双氮阴离子（dinitrogen anion）的 ${}^{2}\Pi_{g}$ 共振态进行的
CAP/EA-ADC(3) 计算，其中采用了
$\Sigma(4+)$ 静态自能（static self-energy）。在该计算中，
一系列起始位置介于 2.0 a.u. 与 5.0 a.u. 之间的平滑 Voronoi 复吸收势（Complex Absorbing
Potential, CAP）被投影到 $B_{2g}$ 对称性下最低五个已收敛
EA-ADC(3) 向量的子空间中（计算使用了 $D_{\infty h}$ 的最大阿贝尔子群
$D_{2h}$）。
所用基组为氮原子上的 aug-cc-pVQZ，并在分子中心额外添加了
$3s3p3d$ 弥散函数。

???+ example "示例 7.186: 对双氮阴离子的 ${}^{2}\Pi_{g}$ 共振态进行标准 CAP/EA-ADC(3) 计算的输入文件。"
    ```qchem
    $molecule
       0 1
       N  0.0 0.0  0.548756750
       N  0.0 0.0 -0.548756750
       Gh 0.0 0.0  0.0
    $end
    
    $rem
       METHOD               adc(3)
       ADC_DENSITY_ORDER    4
       EA_STATES            [0,0,5,0,0,0,0,0]
       BASIS                gen
       ADC_CAP              1
       CAP_TYPE             2
       CAP_X                2000
       CAP_X_END            5000
       CAP_X_STEP           500
       MEM_TOTAL            100000
       ADC_DAVIDSON_CONV    5
       ADC_DAVIDSON_THRESH  14
       ADC_DAVIDSON_MAXITER 100
       ADC_NGUESS_SINGLES   20
       THREADS              12
       FORCE_SYMMETRY_ON    TRUE
    $end
    
    $basis
    N     0
    aug-cc-pVQZ
    ****
    Gh    0
    S   1   1.00
          0.0273200              1.0000000
    S   1   1.00
          0.0136600              1.0000000
    S   1   1.00
          0.0068300              1.0000000
    P   1   1.00
          0.0220100              1.0000000
    P   1   1.00
          0.0110050              1.0000000
    P   1   1.00
          0.0055025              1.0000000
    D   1   1.00
          0.0555000              1.0000000
    D   1   1.00
          0.0277500              1.0000000
    D   1   1.00
          0.0138750              1.0000000
    ****
    $end
    ```

下一个示例提供了具有 $C_{s}$ 对称性的水分子的限制性 ADC(2)-x 计算的输入文件。请求了四个单重态
$A^{\prime\prime}$ 激发态和两个三重态 $A^{\prime}$
激发态。对于前两个态（1 ${}^{1}\!A^{\prime\prime}$ 和
1 ${}^{3}\!A^{\prime}$），其跃迁密度（transition densities）以及附着和脱离密度（attachment and detachment
densities）被导出为 cube 文件。

???+ example "示例 7.187: 具有 $C_{s}$ 对称性的水分子的限制性 ADC(2)-x 计算。"
    ```qchem
    $molecule
       0 1
       O   0.000   0.000   0.000
       H   0.000   0.000   0.950
       H   0.896   0.000  -0.317
    $end
    
    $rem
       METHOD            adc(2)-x
       BASIS             6-31g(d,p)
       THREADS           2
       MEM_TOTAL         3000
       MEM_STATIC        100
       EE_SINGLETS       [0,4]
       EE_TRIPLETS       [2,0]
       ADC_PROP_ES       true
       MAKE_CUBE_FILES   true
    $end
    
    $plots
    Plot transition and a/d densities
       40 -3.0 3.0
       40 -3.0 3.0
       40 -3.0 3.0
       0 0 2 2
       1 2
       1 2
    $end
    ```

下一个示例提供了在乙醚（diethyl
ether）中对 $N,N$-二甲基硝基苯胺的五个最低单重激发态进行 ADC(2)-s/ptSS-PCM 计算的输入文件。PCM
设置除 **Theory** 外均采用默认值，其中 **Theory** 被设为 **IEFPCM**，而非默认的 **CPCM**。

???+ example "示例 7.188: 在乙醚中对 $N,N$ -二甲基硝基苯胺进行的 ADC(2)-s/ptSS-PCM 计算。"
    ```qchem
    $molecule
       0 1
       C   -4.263068      2.512843      0.025391
       C   -5.030982      1.361365      0.007383
       C   -4.428196      0.076338     -0.021323
       C   -3.009941      0.019036     -0.030206
       C   -2.243560      1.171441     -0.011984
       C   -2.871710      2.416638      0.015684
       H   -4.740854      3.480454      0.047090
       H   -2.502361     -0.932570     -0.052168
       H   -1.166655      1.104642     -0.020011
       H   -6.104933      1.461766      0.015870
       N   -5.178541     -1.053870     -0.039597
       C   -6.632186     -0.969550     -0.034925
       H   -6.998203     -0.462970      0.860349
       H   -7.038179     -1.975370     -0.051945
       H   -7.001616     -0.431420     -0.910237
       C   -4.531894     -2.358860     -0.066222
       H   -3.912683     -2.476270     -0.957890
       H   -5.298508     -3.126680     -0.075403
       H   -3.902757     -2.507480      0.813678
       N   -2.070815      3.621238      0.033076
       O   -0.842606      3.510489      0.025476
       O   -2.648404      4.710370      0.054545
    $end
    
    $rem
       THREADS                4
       METHOD                 adc(2)
       BASIS                  3-21G
       MEM_TOTAL              32000
       MEM_STATIC             2000
       ADC_PROP_ES            true
       ADC_PRINT              1
       EE_SINGLETS            5
       ADC_DAVIDSON_MAXITER   100
       PCM_PRINT              1       !increase print level
       SOLVENT_METHOD         pcm     !invokes PCM solvent model
    $end
    
    $pcm
       nonequilibrium         true
       theory                IEFPCM  !default is CPCM, IEFPCM is more accurate
       Solver                Inversion
       vdwScale              1.20
    $end
    
    $solvent
       dielectric            4.34  !epsilon of Et2O
       dielectric_infi       1.829 !n_square of Et2O
    $end
    ```

下一个作业需要一个相当复杂的复合输入文件。该示例作业计算水中过氧亚硝酸根（peroxinitrite）第一激发单重态的
ADC/SS-PCM EqS 溶剂场平衡，其结果可用于计算荧光能。第一个作业（使用较小的基组和较低的 ADC
收敛标准）生成起始点后，第二个作业持续进行溶剂场迭代直至收敛。第三个作业在第二个作业留在磁盘上的已收敛溶剂场中计算
ADC(2) 激发态。第四个作业额外计算 ADC(3)
激发态。一般而言，对此类混合方法应持极为谨慎的态度。若参考态的 self-ptSS 项过大（$>0.01$ eV）——正如本例中的情况——则应采用完全自洽的方法，即在 ADC(3)
级别下同样计算溶剂反应场（reaction field）。PCM 设置除 **Theory**
外均采用默认值，其中 **Theory** 被设为 IEFPCM，而非默认的 CPCM。

???+ example "示例 7.7.189: 水中过氧亚硝酸根第一激发单重态的 ADC/SS-PCM EQS 溶剂场平衡。"
    ```qchem
    $comment
       ADC(2)/ptSS-PCM to generate starting point for the EqS
       Step in the next Job
    $end
    
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       THREADS             2
       METHOD              adc(2)
       BASIS               3-21G !using a small basis to speed up this step
       MEM_TOTAL           6000
       MEM_STATIC          1000
       EE_SINGLETS         1
       ADC_PROP_ES         true
       ADC_DAVIDSON_CONV   4
       SOLVENT_METHOD      pcm
    $end
    
    $pcm
       nonequilibrium true
    $end
    
    $solvent !Water
       dielectric       78.4
       dielectric_infi   1.76
    $end
    
    @@@
    
    $comment
       ADC(2)/ptSS-PCM(EqS) solvent-field equilibration
       for the first excited state
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS          2
       METHOD           adc(2)
       BASIS            6-31G*
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      2 !compute 2 singlets during the equilibration
       ADC_PROP_ES      true
       SOLVENT_METHOD   pcm !activate PCM
    $end
    
    $pcm
       eqsolv      15    !maximum 15 steps, converges after 5
       eqstate     1     !Equilibrate 1st excited state
       eqs_conv    4     !Default convergence
       theory      iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric       78.4
       dielectric_infi   1.76
    $end
    
    @@@
    
    $comment
       Compute ADC(2) excited states in the converged solvent field
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS          2
       METHOD           adc(2)
       BASIS            6-31G*
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      6 !compute 6 singlets
       ADC_PROP_ES      true
       ADC_PROP_ES2ES   true !compute ES 2 ES transition moments for ESA
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       eqsolv   true !only one calculation with converged field
       eqstate  1    !Equilibrate 1st excited state
       theory   iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric      78.4
       dielectric_infi  1.76
    $end
    
    @@@
    
    $comment
       We can also compute ADC(3) excited states in the
       converged ADC(2) solvent field and use the self-
       ptSS term as diagnostic.
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS          2
       METHOD           adc(3)
       BASIS            6-31G*
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      3 !compute 3 singlets
       EE_TRIPLETS      1    !and 1 triplet
       ADC_PROP_ES      true
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       eqsolv   true !only one calculation with converged field
       eqstate  1    !Equilibrate 1st excited state
       theory   iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric      78.4
       dielectric_infi  1.76
    $end
    ```

下一个示例作业提供了在水中用过氧亚硝酸根五个最低激发态进行 RI-ADC(2)/ptSS-PCM(PTED)
计算的输入文件。第一个作业生成起始点，同时给出 ptSS(PTE) 和 ptSS(PTD)
结果以供比较；第二个作业针对 MP 密度对溶剂场进行平衡。在迭代过程中，为加快计算而关闭了激发态的求解。第三个作业在
RI-ADC(2)/ptSS(PTED)
理论水平下计算五个激发态。尽管该分子的 PTD 校正异常之大，但将第一个作业中 PTE、PTD 和 PTD*
的结果与第三个作业中的 PTED
结果进行比较，仍可以看出完全自洽的 PTED 方法与微扰式的 PTD 方法之间具有合理的一致性。第四个作业使用更大的基组计算激发态。此时 MP
基态的 self-ptSS 项会相当小，表明用较小的 SVP
基组计算的溶剂场是一个很好的近似。

???+ example "示例 7.7.190: 在水中用过氧亚硝酸根五个最低激发态进行的 RI-ADC(2)/ptSS-PCM(PTED) 计算。"
    ```qchem
    $comment
       RI-ADC(2)/ptSS-PCM to generate starting point for
       the PTED iterations in the next Job and provide
       PTE and PTD energies for comparing with PTED
    $end
    
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       THREADS          2
       METHOD           adc(2)
       BASIS            def2-SVP
       AUX_BASIS        rimp2-VDZ
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      5
       ADC_PROP_ES      true
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       nonequilibrium true
    $end
    
    $solvent !Water
       dielectric      78.4
       dielectric_infi  1.76
    $end
    
    @@@
    
    $comment
       RI-ADC(2)/ptSS-PTED solvent-field equilibration for
       the MP ground state. No excited states are computed
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS          2
       METHOD           adc(2)
       BASIS            def2-SVP
       AUX_BASIS        rimp2-VDZ
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      0 !dont compute ES
       ADC_PROP_ES      true
       SOLVENT_METHOD   pcm !activate PCM
    $end
    
    $pcm
       eqsolv     15    !maximum 15 steps
       eqstate    0     !Equilibrate MP ground state
       eqs_conv   5     !higher convergence
       theory     iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric      78.4
       dielectric_infi  1.76
    $end
    
    @@@
    
    $comment
       Compute ADC(2)/ptSS-PTED excited states in the
       converged solvent field
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS          2
       METHOD           adc(2)
       BASIS            def2-SVP
       AUX_BASIS        rimp2-VDZ
       MEM_TOTAL        6000
       MEM_STATIC       1000
       EE_SINGLETS      5 !compute 5 singlets
       ADC_PROP_ES      true
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       eqsolv   true !only one calculation with converged field
       eqstate  0    !Equilibrate MP ground state
       theory   iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric 78.4
       dielectric_infi 1.76
    $end
    
    
    @@@
    
    
    $comment
       We can also compute the ES in the converged field
       with a larger basis and without RI in the stored
       solvent-field.
    $end
    
    $molecule
       read
    $end
    
    $rem
       THREADS         2
       METHOD          adc(2)
       BASIS           def2-TZVP
       MEM_TOTAL       6000
       MEM_STATIC      1000
       EE_SINGLETS     3 !compute 3 singlets
       ADC_PROP_ES     true
       SOLVENT_METHOD  pcm
    $end
    
    $pcm
       eqsolv  true !only one calculation with converged field
       eqstate 0  !Equilibrate MP ground state
       theory iefpcm
       nonequilibrium true
    $end
    
    $solvent
       dielectric 78.4
       dielectric_infi  1.76
    $end
    ```
