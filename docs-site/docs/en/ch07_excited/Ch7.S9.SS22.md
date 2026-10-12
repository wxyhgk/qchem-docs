---
title: "7.9.22 EOM-CC Optimization and Properties Job Control"
---

## 7.9.22 EOM-CC Optimization and Properties Job Control

(July 4, 2026)

### `CC_STATE_TO_OPT`

> **Specifies which state to optimize (or from which state compute EOM-EOM inter-state properties).**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `None`
> * **Options**:
>     * `[`: $i$ , $j$ ] optimize the $j$ th state of the $i$ th irrep.
> * **Recommendation**: None

**Note: 

The state number should be smaller or equal to the number of excited
states calculated in the corresponding irrep.
**

**Note: 

If analytic gradients are not available, the finite difference
calculations will be performed and the symmetry will be turned off. In this
case, CC_STATE_TO_OPT should be specified assuming C${}_{1}$ symmetry,
*i.e.*, as [1,N] where N is the number of state to optimize (the EOM states are
numbered from 1).
**

### `CC_EOM_PROP`

> **Whether or not the non-relaxed (expectation value) one-particle EOM-CCSD target state properties will be calculated. Available properties currently include permanent dipole moment, angular momentum projections, the second moments ( $\langle x^{2}\rangle$ , $\langle y^{2}\rangle$ , and $\langle z^{2}\rangle$ ) of the electron density along with $\langle r^{2}\rangle=\langle x^{2}\rangle+\langle y^{2}\rangle+\langle z^{2}\rangle$ . This option is incompatible with JOBTYPE = FORCE , OPT , or FREQ .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (no one-particle properties will be calculated)`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: Additional equations (EOM-CCSD equations for the left eigenvectors) need to be solved for properties, approximately doubling the cost of calculation for each irrep. The cost of the one-particle properties calculation itself is low. The one-particle density of an EOM-CCSD target state can be analyzed with NBO or libwfa packages by specifying the state with CC_STATE_TO_OPT and requesting NBO = TRUE and = TRUE .

### `CC_TRANS_PROP`

> **Whether or not the transition dipole moment (in atomic units) and oscillator strength and rotatory strength (in atomic units) for the EOM-CCSD target states will be calculated. By default, the transition dipole moment, angular momentum matrix elements, and rotatory strengths are calculated between the CCSD reference and the EOM-CCSD target states. In order to calculate transition dipole moment, angular momentum matrix elements, and rotatory strengths between a set of EOM-CCSD states and another EOM-CCSD state, the CC_STATE_TO_OPT must be specified for this state.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (no transition properties will be calculated)`
> * **Options**:
>     * 1 (calculate transition properties between all computed EOM state and the reference state): 2 (calculate transition properties between all pairs of EOM states)
> * **Recommendation**: Additional equations (for the left EOM-CCSD eigenvectors plus lambda CCSD equations in case of transition properties between the CCSD reference and EOM-CCSD target states are requested) need to be solved for transition properties, approximately doubling the computational cost. The cost of the transition properties calculation itself is low.

**Note: 

When the *$trans_prop* section is present in the input, it overrides the
setting of the CC_TRANS_PROP *$rem* variable. However, for
*$trans_prop* to work, CC_TRANS_PROP *does* need to be set.
**

### `CC_EOM_ECD`

> **Whether or not the ECD transition moments will be calculated. By default, the transition moments are calculated between the CCSD reference and the EOM-CCSD target states. In order to calculate transition moments between a set of EOM-CCSD states and another EOM-CCSD state, the CC_STATE_TO_OPT must be specified for this state.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (do not compute ECD transition moments)`
> * **Options**:
>     * `TRUE`: Compute ECD transition moments.
> * **Recommendation**: Activate for chiral molecules only.

### `CC_EOM_2PA`

> **Whether or not the transition moments and cross-sections for two-photon absorption will be calculated. By default, the transition moments are calculated between the CCSD reference and the EOM-CCSD target states. In order to calculate transition moments between a set of EOM-CCSD states and another EOM-CCSD state, the CC_STATE_TO_OPT must be specified for this state. If 2PA NTO analysis is requested, the value is redundant as long as $>0$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (do not compute 2PA transition moments)`
> * **Options**:
>     * `1`: Compute 2PA using the fastest algorithm (use $\tilde{\sigma}$ -intermediates for canonical and $\sigma$ -intermediates for RI/CD response calculations).
>     * `2`: Use $\sigma$ -intermediates for 2PA response equation calculations.
>     * `3`: Use $\tilde{\sigma}$ -intermediates for 2PA response equation calculations.
> * **Recommendation**: Additional response equations (6 for each target state) will be solved, which increases the cost of calculations. The cost of 2PA moments is about 10 times that of energy calculation. Use the default algorithm. Setting $>0$ turns on CC_TRANS_PROP .

### `CC_EOM_2PA_XCONV`

> **Convergence criterion for the response vectors (norm of the difference) of the DIIS solver for damped response equations in 2PA and RIXS calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `5 Corresponding to`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion.
> * **Recommendation**: Use the default in double precision. May reduce in single precision.

### `DAMPED_DALTON_SOLVER`

> **Boolean for using the new Davidson-like solver ( Dalton ) for damped (CCSD polarizabilities and hyperpolarizabilities and EOM-CCSD 2PA and RIXS cross sections) response equations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE (Use the new`
> * **Options**:
>     * `FALSE`: If the old DIIS solver is desired for the above properties.
> * **Recommendation**: Use the new solver for faster convergence relative to DIIS.

### `DALTON_XCONV`

> **Convergence criterion for the residuals (square norm) of the Dalton solver for response equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `6 Corresponding to`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion.
> * **Recommendation**: Use the default in double precision. May reduce to 5 in single precision.

### `DALTON_MAXITER`

> **Maximum number of iteration allowed for the Dalton solver for response equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: User-defined number of iterations.
> * **Recommendation**: Default is usually sufficient

### `DALTON_MAXSPACE`

> **Specifies maximum number of vectors in the subspace for the Dalton solver for response equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `200`
> * **Options**:
>     * $n$: Up to
>     * $n$: vectors per root before the subspace is reset.
> * **Recommendation**: Larger values increase disk storage but accelerate and stabilize convergence.

### `DALTON_PRECOND_START`

> **Specifies the iteration number in the Dalton procedure for response equations from which the preconditioner is applied to the residuals.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$: User-defined iteration number.
> * **Recommendation**: Use default.

### `CALC_SOC`

> **Whether or not the spin-orbit couplings between CC/EOM/ADC/CIS/TDDFT electronic states will be calculated. In the CC/EOM-CC suite, by default the couplings are calculated between the CCSD reference and the EOM-CCSD target states. In order to calculate couplings between EOM states, CC_STATE_TO_OPT must specify the initial EOM state. If NTO analysis is requested, analysis of spinless transition density matrices will be performed and the spin-orbit integrals over NTO pairs will be printed.**
>
> * **Type**: `INTEGER/LOGICAL`
> * **Default**: `FALSE (no spin-orbit couplings will be calculated)`
> * **Options**:
>     * `0/FALSE`: (no spin-orbit couplings will be calculated)
>     * `1/TRUE`: Activates SOC calculation. EOM-CC/EOM-MP2 only: spin-orbit couplings will be computed with the new code with L+/L- averaging
>     * `2`: EOM-CC/EOM-MP2 only: spin-orbit couplings will be computed with the new code without L+/L- averaging
>     * `3`: EOM-CC/EOM-MP2 only: spin-orbit couplings will be computed with the legacy code
>     * `4`: One-electron spin-orbit couplings will be computed with effective nuclear charges (with L+/L- averaging for EOM-CC/MP2)
> * **Recommendation**: CCMAN2 supports several variants of SOC calculation for EOM-CC/EOM-MP2 methods. One-electron and mean-field two-electron SOCs will be computed by default. To enable full two-electron SOCs, two-particle EOM properties must be turned on (see CC_EOM_PROP_TE ).

### `CALC_NAC`

> **Whether or not nonadiabatic couplings will be calculated for the EOM-CC, CIS, and TDDFT wave functions.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (do not compute NAC)`
> * **Options**:
>     * `1`: NYI for EOM-CC
>     * `2`: Compute NACs using Szalay’s approach (this what needs to be specified for EOM-CC).
> * **Recommendation**: Additional response equations will be solved and gradients for all EOM states and for summed states will be computed, which increases the cost of calculations. Request only when needed and do not ask for too many EOM states.

### `CC_POL`

> **Specifies the approach for calculating the polarizability of the CCSD wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: (analytic-derivative or response-theory mixed symmetric-asymmetric approach)
>     * `2`: (analytic-derivative or response-theory asymmetric approach)
>     * `3`: (expectation-value approach with right response intermediates)
>     * `4`: (expectation-value approach with left response intermediates)
>     * `13`: (damped-response expectation-value approach with right response intermediates)
>     * `14`: (damped-response expectation-value approach with left response intermediates)
>     * `15`: (damped-response expectation-value approach with first-order response density matrices)
>     * `23`: (expectation-value approach with right response intermediates and imaginary frequencies)
> * **Recommendation**: CCSD polarizabilities are expensive since they require solving three/six (for static) or six/twelve (for dynamic) additional response equations. Do no request this property unless you need it.

### `EOM_POL`

> **Specifies the approach for calculating the polarizability of the EOM-CCSD wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: (analytic-derivative or response-theory mixed symmetric-asymmetric approach)
>     * `2`: (analytic-derivative or response-theory asymmetric approach)
>     * `3`: (expectation-value approach with right response intermediates)
>     * `4`: (expectation-value approach with left response intermediates)
>     * `23`: (expectation-value approach with right response intermediates and imaginary frequencies)
> * **Recommendation**: EOM-CCSD polarizabilities are expensive since they require solving three/nine (for static) or six/eighteen (for dynamic) additional response equations. Do no request this property unless you need it.

### `CC_1HPOL`

> **Specifies the approach for calculating the first hyperpolarizability of the CCSD wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: (damped-response expectation-value approach with only first-order response wave functions)
>     * `3`: (damped-response expectation-value approach with second-order response density matrices for wave-function and natural orbital analyses)
> * **Recommendation**: CCSD first hyperpolarizabilities are expensive since they require solving a huge number of first- and second-order response equations. Do no request this property unless you need it.

### `CC_EOM_PROP_TE`

> **Request for calculation of non-relaxed two-particle EOM-CC properties. The two-particle properties currently include $\langle\hat{S}^{2}\rangle$ . The one-particle properties also will be calculated, since the additional cost of the one-particle properties calculation is inferior compared to the cost of $\langle\hat{S}^{2}\rangle$ . The variable CC_EOM_PROP must be also set to TRUE . Alternatively, CC_CALC_SSQ can be used to request $\langle\hat{S}^{2}\rangle$ calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: The two-particle properties are computationally expensive since they require calculation and use of the two-particle density matrix (the cost is approximately the same as the cost of an analytic gradient calculation). Do not request the two-particle properties unless you really need them.

### `CC_FULLRESPONSE`

> **Fully relaxed properties (with or without orbital relaxation terms) will be computed. The variable CC_EOM_PROP must be also set to TRUE .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: (both amplitude and orbital response will be calculated)
>     * `2`: (only amplitude response will be calculated)
> * **Recommendation**: Not available for non-UHF/RHF references. Only available for EOM/CI methods for which analytic gradients are available.

### `CC_SYMMETRY`

> **Controls the use of symmetry in coupled-cluster calculations**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Use the point group symmetry of the molecule
>     * `FALSE`: Do not use point group symmetry (all states will be of $A$ symmetry).
> * **Recommendation**: It is automatically turned off for any finite difference calculations, e.g. second derivatives.

**Note: 

Only Abelian groups are supported. For molecules from non-Abelian groups,
USE_ABELIAN_SUBGROUP must be set to TRUE (this is currently a default for all CCMAN and CCMAN2 jobs).
**

### `STATE_ANALYSIS`

> **Activates excited state analyses using libwfa .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (no excited state analyses)`
> * **Options**:
>     * `TRUE, FALSE`
> * **Recommendation**: Set to TRUE if excited state analysis is required, but also if plots of densities or orbitals are needed. For details see Section 10.2.12 .

### `G_TENSOR`

> **Activates g-tensor calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Don’t calculate g-tensor
>     * `TRUE`（或 `1`）: Calculate g-tensor.
> * **Recommendation**: None.

**Note: 

g-Tensor calculations are only available for CCSD.
**

## 7.9.22.1 Examples

???+ example "Example 7.127: Geometry optimization for the excited open-shell singlet state, ${}^{1}$ B ${}_{2}$ , of
methylene followed by the calculations of the fully relaxed one-electron
properties using EOM-EE-CCSD."
    ```qchem
    $molecule
       0 1
       C
       H  1 rCH
       H  1 rCH 2 aHCH
    
       rCH    = 1.083
       aHCH   = 145.
    $end
    
    $rem
       JOBTYPE                   OPT
       METHOD                    EOM-CCSD
       BASIS                     cc-pVTZ
       SCF_GUESS                 CORE
       SCF_CONVERGENCE           9
       EE_SINGLETS               [0,0,0,1]
       EOM_NGUESS_SINGLES        2
       CC_STATE_TO_OPT           [4,1]
       EOM_DAVIDSON_CONVERGENCE  9    use tighter convergence for EOM amplitudes
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD               EOM-CCSD
       BASIS                cc-pVTZ
       SCF_GUESS            READ
       EE_SINGLETS          [0,0,0,1]
       EOM_NGUESS_SINGLES   2
       CC_EOM_PROP          1  calculate properties for EOM states
       CC_FULLRESPONSE      1  use fully relaxed properties
    $end
    ```

???+ example "Example 7.128: Property and transition property calculation on the lowest singlet
state of CH ${}_{2}$ using EOM-SF-CCSD."
    ```qchem
    $molecule
       0 3
       C
       H  1 rch
       H  1 rch 2 ahch
    
       rch  = 1.1167
       ahch = 102.07
    $end
    
    $rem
       METHOD             eom-ccsd
       BASIS              cc-pvtz
       SCF_GUESS          core
       SCF_CONVERGENCE    9
       SF_STATES          [2,0,0,3]   Get three 1^B2 and two 1^A1 SF states
       CC_EOM_PROP        1
       CC_TRANS_PROP      1
       CC_STATE_TO_OPT    [4,1] First EOM state in the 4th irrep
    $end
    ```

???+ example "Example 7.129: Calculation of EOM transition strength using length, momentum, and mixed gauges."
    ```qchem
    $comment
    EOM-CC oscillator strength using three gauges
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
        method = ccsd
        input_bohr = true
        ee_singlets [0,0,2,2]
        basis = 6-31g
        cc_trans_prop = true
        cc_ref_prop = 1
        cc_eom_prop = 1
    $end
    
    $trans_prop
      state_list
        ref
        ee_singlets 0 0
      end_list
      calc dipole linmom
    $end
    ```

???+ example "Example 7.130: Calculation of ECD using EOM-CCSD wave functions."
    ```qchem
    $comment
    Calculation of ECD  using EOM-CC wave-functions
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
    method = ccsd
    input_bohr = true
    ee_singlets [0,0,2,2]
    basis = 6-31g
    cc_trans_prop = true
    cc_ref_prop = 1
    cc_eom_prop = 1
    cc_eom_ecd  = 1 ! keyword to activate ECD
    $end
    
    @@@
    $comment
    Calculation of ECD  using EOM-CC wave-functions
    using trans_prop section
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
    method = ccsd
    input_bohr = true
    ee_singlets [0,0,2,2]
    basis = 6-31g
    cc_trans_prop = true
    cc_ref_prop = 1
    cc_eom_prop = 1
    $end
    
    $trans_prop
    state_list
        ref
        ee_singlets 0 0
        end_list
        calc ecd
    $end
    ```

???+ example "Example 7.7.131: Geometry optimization with tight convergence for the ${}^{2}$ A ${}_{1}$ excited state
of CH ${}_{2}$ Cl, followed by calculation of non-relaxed and fully relaxed permanent
dipole moment and $\langle\hat{S}^{2}\rangle$ ."
    ```qchem
    $molecule
       0 2
       H
       C   1  CH
       CL  2  CCL  1  CCLH
       H   2  CH   3  CCLH  1  DIH
    
       CH   = 1.096247
       CCL  = 2.158212
       CCLH = 122.0
       DIH  = 180.0
    $end
    
    $rem
       JOBTYPE                    OPT
       METHOD                     EOM-CCSD
       BASIS                      6-31G*  Basis Set
       SCF_GUESS                  SAD
       EOM_DAVIDSON_CONVERGENCE   9    EOM amplitude convergence
       CC_T_CONV                  9    CCSD amplitudes convergence
       EE_STATES                  [0,0,0,1]
       CC_STATE_TO_OPT            [4,1]
       EOM_NGUESS_SINGLES         2
       GEOM_OPT_TOL_GRADIENT      2
       GEOM_OPT_TOL_DISPLACEMENT  2
       GEOM_OPT_TOL_ENERGY        2
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD             EOM-CCSD
       BASIS              6-31G*  Basis Set
       SCF_GUESS          READ
       EE_STATES          [0,0,0,1]
       EOM_NGUESS_SINGLES  2
       CC_EOM_PROP        1   calculate one-electron properties
       CC_EOM_PROP_TE     1   and two-electron properties (S^2)
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD              EOM-CCSD
       BASIS               6-31G*  Basis Set
       SCF_GUESS           READ
       EE_STATES           [0,0,0,1]
       EOM_NGUESS_SINGLES  2
       CC_EOM_PROP         1  calculate one-electron properties
       CC_EOM_PROP_TE      1  and two-electron properties (S^2)CC_EXSTATES_PROP 1
       CC_FULLRESPONSE     1  same as above, but do fully relaxed properties
    $end
    ```

???+ example "Example 7.132: CCSD calculation on three A ${}_{2}$ and one B ${}_{2}$ state of formaldehyde.
Transition properties will be calculated between the third A ${}_{2}$ state and all
other EOM states."
    ```qchem
    $molecule
       0  1
       O
       C  1  1.4
       H  2  1.0  1  120
       H  2  1.0  1  120  3 180
    $end
    
    $rem
       BASIS             6-31+G
       METHOD            EOM-CCSD
       EE_STATES         [0,3,0,1]
       CC_STATE_TO_OPT   [2,3]
       CC_TRANS_PROP     true
    $end
    ```

???+ example "Example 7.133: EOM-IP-CCSD geometry optimization of X ${}^{2}$ B ${}_{2}$ state of $\rm H_{2}O^{+}$ ."
    ```qchem
    $molecule
       0 1
       H    0.774767     0.000000     0.458565
       O    0.000000     0.000000    -0.114641
       H   -0.774767     0.000000     0.458565
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            eom-ccsd
       BASIS             6-311G
       IP_STATES         [0,0,0,1]
       CC_STATE_TO_OPT   [4,1]
    $end
    ```

???+ example "Example 7.7.134: CAP-EOM-EA-CCSD geometry optimization of the ${}^{2}B_{1}$ anionic resonance state
of formaldehyde. The applied basis is aug-cc-pVDZ augmented by 3s3p diffuse
functions on heavy atoms."
    ```qchem
    $molecule
       0 1
       C       0.0000000000     0.0000000000     0.5721328608
       O       0.0000000000     0.0000000000    -0.7102635035
       H       0.9478180646     0.0000000000     1.1819748108
       H      -0.9478180646     0.0000000000     1.1819748108
    $end
    
    $rem
       JOBTYPE                    opt
       METHOD                     eom-ccsd
       BASIS                      gen
       N_FROZEN_CORE              0
       SCF_CONVERGENCE            9
       CC_CONVERGENCE             9
       EOM_DAVIDSON_CONVERGENCE   9
       EA_STATES                  [0,0,0,2]
       CC_STATE_TO_OPT            [4,1]
       XC_GRID                    000250000974
       COMPLEX_CCMAN              1
    $end
    
    $complex_ccman
       CS_HF 1
       CAP_TYPE 1
       CAP_ETA 60
       CAP_X 3850
       CAP_Y 2950
       CAP_Z 6100
    $end
    
    $basis
     H   0
     S   3  1.00
           13.0100000         0.196850000E-01
           1.96200000         0.137977000
          0.444600000         0.478148000
     S   1  1.00
          0.122000000          1.00000000
     P   1  1.00
          0.727000000          1.00000000
     S   1  1.00
          0.297400000E-01      1.00000000
     P   1  1.00
          0.141000000          1.00000000
     ****
     C   0
     S   8  1.00
           6665.00000         0.692000000E-03
           1000.00000         0.532900000E-02
           228.000000         0.270770000E-01
           64.7100000         0.101718000
           21.0600000         0.274740000
           7.49500000         0.448564000
           2.79700000         0.285074000
          0.521500000         0.152040000E-01
     S   8  1.00
           6665.00000        -0.146000000E-03
           1000.00000        -0.115400000E-02
           228.000000        -0.572500000E-02
           64.7100000        -0.233120000E-01
           21.0600000        -0.639550000E-01
           7.49500000        -0.149981000
           2.79700000        -0.127262000
          0.521500000         0.544529000
     S   1  1.00
          0.159600000          1.00000000
     P   3  1.00
           9.43900000         0.381090000E-01
           2.00200000         0.209480000
          0.545600000         0.508557000
     P   1  1.00
          0.151700000          1.00000000
     D   1  1.00
          0.550000000          1.00000000
     S   1  1.00
          0.469000000E-01     1.00000000
     P   1  1.00
          0.404100000E-01     1.00000000
     D   1  1.00
          0.151000000         1.00000000
     S   1  1.00
          0.234500000E-01      1.00000000
     S   1  1.00
          0.117250000E-01      1.00000000
     S   1  1.00
          0.058625000E-01      1.00000000
     P   1  1.00
          0.202050000E-01      1.00000000
     P   1  1.00
          0.101025000E-01      1.00000000
     P   1  1.00
          0.050512500E-01      1.00000000
     ****
     O   0
     S   8  1.00
           11720.0000         0.710000000E-03
           1759.00000         0.547000000E-02
           400.800000         0.278370000E-01
           113.700000         0.104800000
           37.0300000         0.283062000
           13.2700000         0.448719000
           5.02500000         0.270952000
           1.01300000         0.154580000E-01
     S   8  1.00
           11720.0000        -0.160000000E-03
           1759.00000        -0.126300000E-02
           400.800000        -0.626700000E-02
           113.700000        -0.257160000E-01
           37.0300000        -0.709240000E-01
           13.2700000        -0.165411000
           5.02500000        -0.116955000
           1.01300000         0.557368000
     S   1  1.00
          0.302300000          1.00000000
     P   3  1.00
           17.7000000         0.430180000E-01
           3.85400000         0.228913000
           1.04600000         0.508728000
     P   1  1.00
          0.275300000          1.00000000
     D   1  1.00
           1.18500000          1.00000000
     S   1  1.00
          0.789600000E-01      1.00000000
     P   1  1.00
          0.685600000E-01      1.00000000
     D   1  1.00
          0.332000000          1.00000000
     S   1  1.00
          0.394800000E-01      1.00000000
     S   1  1.00
          0.197400000E-01      1.00000000
     S   1  1.00
          0.098700000E-01      1.00000000
     P   1  1.00
          0.342800000E-01      1.00000000
     P   1  1.00
          0.171400000E-01      1.00000000
     P   1  1.00
          0.085700000E-01      1.00000000
     ****
    $end
    ```

???+ example "Example 7.135: Calculating resonant 2PA with degenerate photons."
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD         eom-ccsd
       BASIS          aug-cc-pvtz
       EE_SINGLETS    [1,0,0,0]   1A_1 state
       CC_TRANS_PROP  1    Compute transition properties
       CC_EOM_2PA     1    Calculate 2PA cross-sections using the fastest algorithm
    $end
    ```

???+ example "Example 7.136: Non-degenerate, resonant 2PA scan over a range of frequency pairs."
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD         eom-ccsd
       BASIS          aug-cc-pvdz
       EE_SINGLETS    [2,0,0,0]  !Two A_1 states
       CC_TRANS_PROP  1          !Calculate transition properties
       CC_EOM_2PA     1          !Calculate 2PA cross-sections using the fastest algorithm
    $end
    
    $2pa
       n_2pa_points 11
       omega_1 500000 5000
    $end
    ```

???+ example "Example 7.137: Resonant 2PA with degenerate photons between two excited states."
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD          eom-ccsd
       BASIS           aug-cc-pvtz
       EE_SINGLETS     [2,0,0,0] Two A_1 states
       CC_STATE_TO_OPT [1,1]     "Reference" state for transition properties is 1A_1 state
       CC_TRANS_PROP   1         Compute transition properties
       CC_EOM_2PA      1         Calculate 2PA cross-sections using the fastest algorithm
    $end
    ```

???+ example "Example 7.138: Calculation of 1st hyperpolarizability for CCSD wave function for LiH using the framework of damped response theory and
the expectation-value approach for a range of frequencies."
    ```qchem
    $comment
    Calculation of static and dynamical first hyperpolarizability for CCSD wave function
    for LiH with STO-3G basis set using the framework of damped response theory and
    the expectation-value approach.
    The property for the following set of photons is calculated:
    (omega_1, omega_2; omega_3) in cm-1
    (0, 0; 0), (2500, 0; -2500), (5000, 0; -5000), (0, 3500; -3500),
    (0, 7000; -7000), (2500, 3500; -6000), (2500, 7000; -9500),
    (5000, 3500; -8500), (5000, 7000; -12000)
    $end
    
    $molecule
    0 1
    H
    Li 1 1.6
    $end
    
    $rem
    METHOD           ccsd
    BASIS            sto-3g
    CC_REF_PROP      1         ! required for CCSD property calculation
    CC_1HPOL         1         ! computes first hyperpolarizability using first-order response wave functions only
    MEM_STATIC       400
    CC_MEMORY        2000
    THRESH           13
    SCF_CONVERGENCE  10
    CC_CONVERGENCE   9
    $end
    
    $1hpol
    omega_1 0 2500000 3 0.01  ! scans the first photon frequency from 0 cm-1 to 5000 cm-1 in 3-1=2 steps of 2500, corresponding damping is 0.01 hartrees
    omega_2 0 3500000 3 0.01  ! scans the second photon frequency from 0 cm-1 to 7000 cm-1 in 3-1=2 steps of 3500, corresponding damping is 0.01 hartrees
    omega_3 0.01              ! damping for the third photon is 0.01 hartrees
    $end
    
    ```

???+ example "Example 7.139: Mean-field spin-orbit calculation between two excited triplets in
acetylene-O intermediate."
    ```qchem
    $molecule
       0 1
       C        -0.0303943366   -0.3149506151   -0.0436827067
       H        -0.1031279784   -1.4353675705   -0.1647400816
       O         1.0178175761    0.2350702146    0.2517598501
       C        -1.3252768442    0.1905302054   -0.4205132671
       H        -2.0767072171    0.1461814657    0.3842573052
    $end
    
    $rem
       BASIS             cc-pvdz
       METHOD            eom-ccsd
    point_group_symmetry False
       SF_STATES         [2]
       CC_STATE_TO_OPT   [1,1]
       THRESH            14
       CALC_SOC          1
       CC_TRANS_PROP     1
    $end
    ```

???+ example "Example 7.140: Mean-field spin-orbit calculation between the reference singlet and excited
triplet states for acetylene-O intermediate."
    ```qchem
    $molecule
    0 1
      C        -0.0303943366   -0.3149506151   -0.0436827067
      H        -0.1031279784   -1.4353675705   -0.1647400816
      O         1.0178175761    0.2350702146    0.2517598501
      C        -1.3252768442    0.1905302054   -0.4205132671
      H        -2.0767072171    0.1461814657    0.3842573052
    $end
    
    $rem
       BASIS           cc-pvdz
       METHOD          eom-ccsd
    point_group_symmetry False
       EE_TRIPLETS     [1]
       THRESH          14
       CALC_SOC        1
       CC_TRANS_PROP   1
    $end
    ```

???+ example "Example 7.141: Computation of spin-orbit couplings between closed-shell singlet and $M_{S}=1$ triplet state in NH using EOM-SF-CCSD."
    ```qchem
    $molecule
       0 3
       N
       H N 1.0450
    $end
    
    $rem
       METHOD          = eom-ccsd
       BASIS           = 6-31g
       SF_STATES       = [1,2,0,0]
       CC_TRANS_PROP   = true
       CALC_SOC        = 3         ! legacy code
       CC_STATE_TO_OPT = [1,1]
    $end
    ```

???+ example "Example 7.142: SOC calculations between EOM-DEA states."
    ```qchem
    $comment
    SOC calculations between EOM-DEA states.
    $end
    
    $molecule
    +2 1
    Si
    H  1 1.530
    F  1 1.605 2 97.000
    $end
    
    $rem
    BASIS = 6-31G*
    jobtype = sp
    method = eom-ccsd
    n_frozen_core  0
    dea_singlets = [1,1]     Ms=0 triplet
    dea_triplets = [0,1]     Ms=-1 triplets
    CALC_SOC = 2             Activates SOC calculation with new code
    CC_EOM_PROP = 1
    CC_TRANS_PROP = true
    $end
    
    ```

???+ example "Example 7.143: Computation of spin-orbit couplings in neutral hextet (tpa)Fe complex (stripped ligands)
by EOM-EA-MP2 method using pseudopotentials and effective nuclear charges."
    ```qchem
    $comment
    Spin-orbit coupling calculation with SBKJC ecp using default effective nuclear
    charges.  Computes SOC in neutral hextet (tpa)Fe geometry (stripped ligands)
    by EOM-EA-MP2 method and high-spin reference.
    $end
    
    $molecule
    0 6
      N   -0.0330663   -0.2576466    1.3744726
      N    2.0052862   -0.4826730   -0.5758819
      N   -1.9801232   -0.6573608   -0.6407513
      N   -0.0634263    1.4157074   -0.9056826
     Fe    0.0133915   -0.5560750   -0.6002859
      H   -0.0630940   -1.1802863    1.8620650
      H   -0.8780689    0.2958440    1.6401738
      H    2.3459249   -0.6439674   -1.5498484
      H    2.3506743   -1.2708551    0.0162081
      H   -2.2816187   -0.8324531   -1.6252623
      H   -2.3957415    0.2480261   -0.3283621
      H    0.0565056    1.5985967   -1.9267087
      H    0.7257691    1.8766147   -0.3993792
      H    0.8165651    0.2643868    1.6852415
    $end
    
    $rem
       METHOD                = EOM-MP2
       EOM_EA_BETA           = [5]
       MAX_SCF_CYCLES        = 300
       SCF_ALGORITHM         = gdm
       SCF_GUESS             = autosad
       EOM_PRECONV_SINGLES   = 1
       CALC_SOC              = 4
       CC_TRANS_PROP         = 2
       BASIS  =   SBKJC           [  use effective charges of ecps in soc calculation]
       ECP = fit-SBKJC
    $end
    
    ```

???+ example "Example 7.144: Computation of
spin-orbit coupling in ClO using all-electron basis set,
user-provided effective nuclear charges, and
EOM-IP wave-functions."
    ```qchem
    $comment
    Spin-orbit coupling calculation using all-electron basis set
    and user-provided effective nuclear charges by
    using EOM-IP wave-functions.
    $end
    
    $molecule
    -1 1
      Cl   -0.9937913   -0.6696391   -1.9087016
      O    0.3415336   -0.1593825   -1.2619353
    $end
    
    $rem
    jobtype             = sp
    method              = eom-ccsd
    basis               = 6-31G
    print_general_basis = 1
    scf_convergence     = 12
    cc_convergence      = 10
    eom_davidson_conv   = 8
    eom_ip_alpha        = [0,0,1,1]
    cc_eom_prop         = 1
    cc_ref_prop         = 1
    cc_trans_prop       = 1
    cc_state_to_opt     = [3,1]
    calc_soc            = 4
    $end
    
    $soc_eff_charges
    8.0 6.0
    17.0 11.0
    $end
    ```

???+ example "Example 7.145: Computation of nonadiabatic couplings between EOM-EE states within triplet
(first job) and singlet (second job) manifolds."
    ```qchem
    $molecule
       +1 1
       H          0.00000        0.00000        0.0
       He         0.00000        0.00000        3.0
    $end
    
    $rem
       JOBTYPE                  = FORCE
       METHOD                   = EOM-CCSD
       BASIS                    = cc-pVDZ
       INPUT_BOHR               = true
       EE_TRIPLETS              = [2]
       CC_EOM_PROP              = true
       POINT_GROUP_SYMMETRY     = false Do not reorient molecule and turn off YYYYYYYYYYYY
       CALC_NAC                 = 2     Invoke Szalay NAC
       EOM_DAVIDSON_CONVERGENCE = 9     tight davidson convergence
       SCF_CONVERGENCE          = 9     Hartree-Fock convergence threshold 1e-9
       CC_CONVERGENCE           = 9
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE                  = FORCE
       METHOD                   = EOM-CCSD
       BASIS                    = cc-pVDZ
       INPUT_BOHR               = true
       EE_STATES                = [2]   singlets
       POINT_GROUP_SYMMETRY     = false Do not reorient molecule and turn off YYYYYYYYYYYY
       CALC_NAC                 = 2     Invoke Szalay NAC
       EOM_DAVIDSON_CONVERGENCE = 9     tight davidson convergence
       SCF_CONVERGENCE          = 9     Hartree-Fock convergence threshold 1e-9
       CC_CONVERGENCE           = 9
    $end
    ```

???+ example "Example 7.146: Calculation of the static dipole polarizability of the CCSD wave function of Helium."
    ```qchem
    $molecule
       0 1
       He
    $end
    
    $rem
       METHOD            ccsd
       BASIS             cc-pvdz
       CC_REF_PROP       1
       CC_POL            2
       CC_DIIS_SIZE      15
       CC_FULLRESPONSE   1
    $end
    ```

???+ example "Example 7.147: Water molecule: Calculating photoionization cross-section and photoelectron angular distribution
with averaging over molecular orientations."
    ```qchem
    $comment
    Calculating photoionization cross-section and photoelectron angular distribution
    with averaging over molecular orientations.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 6-31G*
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        DO_AVERAGE 1
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "Example 7.148: Water molecule:
Calculating photoionization cross-section, asymmetry parameter and photoelectron angular
distribution with a Z-polarized light."
    ```qchem
    $comment
    Calculating photoionization cross-section, asymmetry parameter, and PAD
    with a Z-polarized light.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        purecart = 1111
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        POL_X 0
        POL_Y 0
        POL_Z 100
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "Example 7.149: Water molecule: Calculating photoionization cross-section and photoelectron angular distribution
with averaging over molecular orientations."
    ```qchem
    $comment
    Calculating photoionization cross-section and PAD
    with averaging over molecular orientations.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 6-31G*
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        DO_AVERAGE 1
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "Example 7.150: Calculating photoionization cross-sections for the ionization of oxygen 1s (core)
of water with Z-polarized light."
    ```qchem
    $comment
    Calculating photoionization cross-sections for the ionization of oxygen 1s (core)
    of water with Z-polarized light.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        purecart = 1111
        CVS_IP_STATES = [1,0,0,0]
        N_FROZEN_CORE = FC
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        POL_X 0
        POL_Y 0
        POL_Z 100
        KE_MIN 10
        KE_MAX 1010
    $end
    ```

???+ example "Example 7.151: Calculating photoionization cross-section, asymmetry parameter, and
PAD with a circularly polarized light."
    ```qchem
    $comment
    Calculating photoionization cross-section, asymmetry parameter, and
    PAD with a circularly polarized light.
    $end
    
    $molecule
     0 1
    C -0.28956361 0.08176958 0.92701577
    C 1.93885200 -1.15600766 -0.10800484
    C -2.79852375 -0.19094696 -0.27656907
    O 1.53613696 1.47730615 -0.46998636
    H 1.71860882 -2.32670888 -1.80795335
    H 3.52273536 -1.64526642 1.13875511
    H -0.27744501 0.50560530 2.96417187
    H -2.56905279 -0.59002862 -2.30639911
    H -3.89960425 1.56511541 -0.07933409
    H -3.88892566 -1.73605572 0.59599929
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        INPUT_BOHR = TRUE
        EOM_IP_ALPHA = [2]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 15
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        CIRC_POL 1
        DO_AVERAGE 0
        KE_MIN 10
        KE_MAX 1010
    $end
    ```
