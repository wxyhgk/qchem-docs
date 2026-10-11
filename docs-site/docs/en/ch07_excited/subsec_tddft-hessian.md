---
title: "7.3.8 Analytic Excited-State Hessian in TDDFT"
---

## 7.3.8 Analytic Excited-State Hessian in TDDFT

(July 4, 2026)

To carry out vibrational frequency analysis of an excited state with
TDDFT,[[842]](../bib_references/bib.md#bib873)
 an optimization of the excited-state geometry
is always necessary. Like the vibrational frequency analysis of the ground
state, the frequency analysis of the excited state should be also performed at
a stationary point on the excited state potential surface. The *$rem* variable
CIS_STATE_DERIV should be set to the excited state for which an
optimization and frequency analysis is needed, in addition to the *$rem*
keywords used for an excitation energy calculation.

Compared to the numerical differentiation method, the analytic calculation of
geometrical second derivatives of the excitation energy needs much less time
but much more memory. The computational cost is mainly consumed by the steps to
solve both the CPSCF equations for the derivatives of molecular orbital
coefficients C${}^{\mathrm{x}}$ and the CP-TDDFT equations for the derivatives of
the transition vectors, as well as to build the Hessian matrix. The memory
usages for these steps scale as ${\cal{O}}({3mN^{2}})$, where $N$ is the number of basis
functions and m is the number of atoms. For large systems, it is thus essential
to solve all the coupled-perturbed equations in segments. In this case, the
*$rem* variable CPSCF_NSEG is always needed.

In the calculation of the analytic TDDFT excited-state Hessian, one has to
evaluate a large number of energy-functional derivatives: the first-order to
fourth-order functional derivatives with respect to the density variables as
well as their derivatives with respect to the nuclear coordinates. Therefore,
a very fine integration grid for DFT calculation should be adapted to guarantee
the accuracy of the results.

Analytic TDDFT/C-PCM Hessian has been implemented in **Q-Chem**.
Normal mode analysis for a system in solution can be performed with the
frequency calculation by TDDFT/C-PCM method. The *$rem* and *$pcm*
variables for the excited state calculation with TDDFT/C-PCM included
in the vertical excitation energy example above are needed. When the properties
of large systems are calculated, you must pay attention to the memory limit.

???+ example "Example 7.18: B3LYP/6-31G* optimization in gas phase, followed by a frequency analysis for
the first excited state of the peroxy radical."
    ```qchem
    $molecule
       0 2
       C  1.004123  -0.180454   0.000000
       O -0.246002   0.596152   0.000000
       O -1.312366  -0.230256   0.000000
       H  1.810765   0.567203   0.000000
       H  1.036648  -0.805445  -0.904798
       H  1.036648  -0.805445   0.904798
    $end
    
    $rem
       JOBTYPE           opt
       EXCHANGE          b3lyp
       CIS_STATE_DERIV   1
       BASIS             6-31G*
       CIS_N_ROOTS       10
       CIS_SINGLETS      true
       CIS_TRIPLETS      false
       XC_GRID           000075000302
       RPA               0
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           freq
       EXCHANGE          b3lyp
       CIS_STATE_DERIV   1
       BASIS             6-31G*
       CIS_N_ROOTS       10
       CIS_SINGLETS      true
       CIS_TRIPLETS      false
       XC_GRID           000075000302
       RPA               0
    $end
    ```

???+ example "Example 7.19: Geometry optimization for a low-lying excited state of
cyclopentadienone in methanol, using TDDFT/C-PCM"
    ```qchem
    $molecule
       0 1
      C   -0.0000000    0.6920860    1.4656691
      C   -0.0000000   -0.6920860    1.4656691
      C   -0.0000000   -1.1528931    0.1065000
      C    0.0000000   -0.0000000   -0.7957576
      C    0.0000000    1.1528931    0.1065000
      O    0.0000000   -0.0000000   -2.0301721
      H   -0.0000000    1.3254423    2.3427356
      H   -0.0000000   -1.3254423    2.3427356
      H   -0.0000000   -2.1834532   -0.2231979
      H    0.0000000    2.1834532   -0.2231979
    $end
    
    $rem
       JOBTYPE             opt
       EXCHANGE            b3lyp
       CIS_N_ROOTS         5
       CIS_SINGLETS        true
       CIS_TRIPLETS        true
       CIS_STATE_DERIV     1   Lowest TDDFT state
       BASIS               6-311G*
       XC_GRID             3
       SOLVENT_METHOD      pcm
       THRESH              12
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric 32.613
    $end
    
    ```

???+ example "Example 7.20: Hessian calculation, using the optimized geometry from the previous example."
    ```qchem
    $molecule
       0 1
       C     0.0000000000    0.6940558365    1.4635362645
       C     0.0000000000   -0.6940558367    1.4635362652
       C     0.0000000000   -1.1539902580    0.1063088532
       C     0.0000000000    0.0000000000   -0.7890068343
       C     0.0000000000    1.1539902569    0.1063088524
       O     0.0000000000    0.0000000000   -2.0333287471
       H     0.0000000000    1.3287019844    2.3394236351
       H     0.0000000000   -1.3287019837    2.3394236361
       H     0.0000000000   -2.1861329696   -0.2193590119
       H     0.0000000000    2.1861329678   -0.2193590131
    $end
    
    $rem
       JOBTYPE           freq
       EXCHANGE          b3lyp
       CIS_N_ROOTS       5
       CIS_SINGLETS      true
       CIS_TRIPLETS      true
       CIS_STATE_DERIV   1   Lowest TDDFT state
       BASIS             6-311G*
       XC_GRID           3
       SOLVENT_METHOD    pcm
       MEM_STATIC        4000
       MEM_TOTAL         24000
       CPSCF_NSEG        3
       THRESH            12
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric  32.613
    $end
    ```
