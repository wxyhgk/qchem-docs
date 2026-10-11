---
title: "6.12.5 Stochastic CC2 and CCSD"
---

## 6.12.5 Stochastic CC2 and CCSD

(July 4, 2026)

An implementation of stochastic RI-CC2 (sRI-CC2) is available in **libgmbpt**.
Currently, codes support RI-CC2 and sRI-CC2 property calculations, including ground- and excited-state (singlet and triplet) energies, analytical gradients for ground and excited states, oscillator strengths, and derivative couplings.
The main advantage of sRI-CC2 is its reduced scaling (${\cal{O}}({N^{3}})$, to be compared
with ${\cal{O}}({N^{5}})$ of RI-CC2), which facilitates applications to much larger molecules.
These codes are under development. Users are advised to refer to the sample jobs
named `libgmbpt_sricc$\ast$` and `libgmbpt_thc_sricc$\ast$` for guidance.

**Note: 

sRI-CC2 currently does not support frozen core: N_FROZEN_CORE must be set to zero.
**

**Note: 

sRI-CC2 currently does not support geometry optimization and can only be used with JOBTYPE=SP.
**

RI-CC2 and sRI-CC2 are deployed by setting METHOD = CC2 *and* specifying
AIX_BASIS appropriately.
SRI-CC2 is only available in **libgmbpt**, so one should set CCMAN2 = -1 in the *$rem* section, and add
do_sri = 1 in the *$development* section.
Then, in the *$development* section, add the keyword sri to control the use of sRI: 0 for deterministic
RI calculations, 1 for sRI calculations with an ${\cal{O}}({N^{3}})$ scaling, and 2 for partial sRI calculations.
In some cases, such as gradient calculations, the sRI approach introduces significant noise.
To mitigate such problems, one can use the partial sRI scheme with a suboptimal ${\cal{O}}({N^{4}})$ scaling but improved
accuracy.

The keyword sri_ntheta indicates the number of sRI orbitals. It acts as a prefactor in the scaling and
larger values give better accuracy.

???+ example "Example 6.31: sRI-CC2 excitation energy of the water molecule."
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2        -1                ! use code in libgmbpt
        method        CC2
        BASIS         cc-pvdz
        AUX_BASIS     RIMP2-cc-pVDZ
        EE_SINGLETS   [1]
        N_FROZEN_CORE 0                 ! frozen core (FC) electrons
    $end
    
    ! below for sRI development
    $development
        do_sri        1
        sri           1                 ! if use sRI, 0-RI, 1-complete sRI, 2-partial sRI
        nsinglets     1                 ! number of singlet states
    !    ntriplets    0                 ! number of triplet states
        sri_ntheta    5000              ! number of stochastic orbitals
        sri_nseed     0                 ! index to generate stochastic seed : 0~23
    $end
    
    ```

Further improvements of sRI-CC2 are afforded by a tensor hypercontraction implementation (THC-sRI-CC2)
with an ${\cal{O}}({N^{3}})$ scaling and reduced stochastic noise for the same set of properties.
THC-sRI-CC2 is invoked by adding thc = $1$ in the *$rem* section and setting sri = $2$
in the *$development* section. The rest of the keywords are the same as in sRI-CC2.

???+ example "Example 6.32: THC-sRI-CC2 ground-state analytical gradient of the water molecule."
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2        -1                ! use code in libgmbpt
        method        CC2
        BASIS         cc-pvdz
        AUX_BASIS     RIMP2-cc-pVDZ
        N_FROZEN_CORE 0                 ! frozen core (FC) electrons, n
        CC_EOM_PROP   true              ! properties calculation
        thc           1                 ! if use THC
    $end
    
    ! below for sRI development
    $development
        do_sri 1
        sri 2                           ! 2-THC-sRI
        sri_ntheta 5000                 ! number of stochastic orbitals for energy
        sri_grad_ntheta 5000            ! number of stochastic orbitals for gradient solution
        sri_nseed 0                     ! index to generate stochastic seed : 0~23
        gradient_gs 1                   ! ground_state gradient calculation
    $end
    
    ```

Finally, THC-sRI-CCSD is available for calculations of
ground- and excited-state energies with an ${\cal{O}}({N^{3}})$ scaling.
One can invoke THC-sRI-CCSD by adding sriccsd = 1 in the *$development* section.

???+ example "Example 6.33: THC-sRI-CCSD ground-state energy of the water molecule."
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2         -1                ! use code in libgmbpt
        method         CC2
        BASIS          cc-pvdz
        AUX_BASIS      RIMP2-cc-pVDZ
        N_FROZEN_CORE  0                 ! frozen core (FC) electrons, n
        CC_CONVERGENCE 6
        thc            1                 ! if use THC
    $end
    
    ! below for sRI development
    $development
        do_sri         1
        sri            2                 ! if use sri, 0-THC, 2-THC-sRI
        sri_ntheta     5000              ! number of stochastic orbitals
        sri_nseed      0                 ! index to generate stochastic seed : 0~23
        sriccsd        1                 ! CCSD
    $end
    
    ```

For further technical details, see Refs. [[1554]](../bib_references/bib.md#bib1632)
.
