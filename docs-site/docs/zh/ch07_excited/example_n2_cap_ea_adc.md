---
title: "7.10.14 Examples"
---

## 7.10.14 Examples

(July 4, 2026)

???+ example "Example 7.181: Input for an ADC(2)-s calculation of singlet exited states of methane with D2
symmetry. In total six excited states are requested corresponding to four (two)
electronic transitions with irreducible representation $B_{1}$ ( $B_{2}$ )."
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

???+ example "Example 7.182: Input for an unrestricted RI-ADC(2)-s calculation with $C_{1}$ symmetry using
DIIS. In addition, excited state properties and state-to-state properties are
computed."
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

???+ example "Example 7.183: Input for a restricted CVS-ADC(2)-x calculation with $C_{1}$ symmetry using 4
parallel CPU cores."
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

???+ example "Example 7.184: Input for a restricted SF-ADC(2)-s calculation of the first three spin-flip
target states of cyclobutadiene without point group symmetry."
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

???+ example "Example 7.185: Computation of the first 5 singlet and triplet states of each irrep with BWs-ADC(2).
The regularisation parameters are chosen to be $A_{0}=4$ and $B_{0}=0$ ."
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

The following example demonstrates a CAP/EA-ADC(3)
calculation of the ${}^{2}\Pi_{g}$ resonance of the dinitrogen anion, employing the
$\Sigma(4+)$ static self-energy. In this
calculation, a series of smoothed Voronoi CAPs with onsets between 2.0 a.u. and 5.0 a.u. is projected onto the subspace of the lowest five converged
EA-ADC(3) vectors of $B_{2g}$ symmetry (the largest Abelian subgroup of
$D_{\infty h}$, which is $D_{2h}$, is used in the calculation).
The basis set employed is aug-cc-pVQZ on nitrogen and additional
$3s3p3d$ diffuse functions on the molecular center.

???+ example "Example 7.186: Input for a standard CAP/EA-ADC(3) calculation of the ${}^{2}\Pi_{g}$ resonance of the
dinitrogen anion."
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

The next example provides input for a restricted ADC(2)-x calculation of water
with $C_{s}$ symmetry. Four singlet $A^{\prime\prime}$ excited states and two triplet $A^{\prime}$
excited states are requested. For the first two states (1 ${}^{1}\!A^{\prime\prime}$ and
1 ${}^{3}\!A^{\prime}$) the transition densities as well as the attachment and detachment
densities are exported into cube files.

???+ example "Example 7.187: Restricted ADC(2)-x calculation of water with $C_{s}$ symmetry."
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

The next sample provides input for a ADC(2)-s/ptSS-PCM calculation of the
five lowest singlet-excited states of $N,N$-dimethylnitroaniline in diethyl
ether. The PCM settings are all default values except **Theory**, which
is set to **IEFPCM** instead of the default **CPCM**.

???+ example "Example 7.188: ADC(2)-s/ptSS-PCM calculation of $N,N$ -dimethylnitroaniline in diethyl ether."
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

The next job requires a rather complicated compound input file. The sample
job computes ADC/SS-PCM EqS solvent-field equilibration for the first
excited singlet state of peroxinitrite in water, which can be used to compute
the fluorescence energy. After generating a starting point in the first job
(using a smaller basis and lower ADC convergence criteria), the solvent-field
iterations are carried out until convergence in the second job. In the third
job, ADC(2) excited states are computed in the converged solvent field that was
left on disk by the second Job. In the fourth job, we additionally compute
ADC(3) excited states. This mixed approach should in general be used with great
caution. If the self-ptSS term of the reference state becomes too large
($>$0.01 eV) like it is the case here, the fully consistent approach should be
used, meaning that the solvent reaction field should also be computed at the
ADC(3) level. PCM settings are all default values except **Theory**, which
is set to IEFPCM instead of the default CPCM.

???+ example "Example 7.7.189: ADC/SS-PCM EQS solvent-field equilibration for the first excited singlet
state of peroxinitrite in water."
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

The next sample job provides the input for a RI-ADC(2)/ptSS-PCM(PTED)
calculation for the five lowest excited states of peroxinitrite in water. After
generating a starting point in the first job, which also provides the ptSS(PTE)
and ptSS(PTD) results for comparison, the solvent-field is equilibrated for the
MP density in the second job. During the iterations, the calculation of excited
states is disabled to speed up the calculation. In the third job, five excited
states are computed at the RI-ADC(2)/ptSS(PTED) level of theory. Although
the PTD corrections for this molecule are unusually large, a comparison of the
PTE, PTD and PTD* results from the first job with the PTED results from the
third job will reveal a reasonable agreement between the fully consistent PTED
and the perturbative PTD approaches. In the fourth job, excited states are
calculated with a larger basis set. The self-ptSS term of the MP ground state
will be quite small, showing that the solvent-field computed with the smaller
SVP basis is a good approximation.

???+ example "Example 7.7.190: RI-ADC(2)/ptSS-PCM(PTED) calculation for the five lowest excited states of
peroxinitrite in water."
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
       dielectric_infi 1.76
    $end
    ```
