---
title: "6.6.6 Orbital-Optimized MP2"
---

## 6.6.6 Orbital-Optimized MP2

(July 4, 2026)

Brueckner orbitals (BOs) are highly desirable when one is unsure whether
artificial symmetry breaking occurs at the Hartree-Fock (HF) level. It is
*artificial* because this symmetry breaking merely reflects the lack of
dynamic correlation at the HF level, not the lack of strong correlation. On
the other hand, it is possible for a single-reference approach to attempt to
describe strongly correlated systems by *essential* symmetry breaking.
Therefore, it is often crucial to distinguish these two by obtaining orbitals
in the presence of electron correlation.[[783]](../bib_references/bib.md#bib826)

Since orbital-optimized coupled-cluster doubles (OOCCD) can be computationally
demanding ($\mathcal{O}(o^{2}v^{4})$), Rohini Lochan working with Martin
Head-Gordon proposed to obtain orbitals by optimizing the MP2 correlation
energy. To this end, BOs are introduced into SOSMP2 and MOSMP2 methods to
resolve the problems of symmetry breaking and spin contamination that are often
associated with Hartree-Fock orbitals. The molecular orbitals are optimized
with the mean-field energy plus a correlation energy taken as the opposite-spin
component of the second-order many-body correlation energy, scaled by an
empirically chosen parameter. This “optimized second-order opposite-spin”
(O2) method[[852]](../bib_references/bib.md#bib888)
 requires fourth-order computation on each
orbital iteration. O2 is shown to yield predictions of structure and
frequencies for closed-shell molecules that are very similar to scaled MP2
methods. However, it yields substantial improvements for open-shell molecules,
where problems with spin contamination and symmetry breaking are shown to be
greatly reduced.

???+ example "Example 6.12: Example of O2 methodology applied to ${\cal{O}}({N^{4}})$ SOSMP2"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       EXCHANGE          HF
       BASIS             sto-3g
       UNRESTRICTED      TRUE
       JOBTYPE           FORCE            Options are SP/FORCE/OPT
       DO_O2             1                O2 with O(N^4) SOS-MP2 algorithm
       SOS_FACTOR        1000000          Opposite Spin scaling factor = 1.0
       SCF_ALGORITHM     DIIS_GDM
       SCF_GUESS         GWH
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

???+ example "Example 6.13: Example of O2 methodology applied to ${\cal{O}}({N^{4}})$ MOSMP2"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       UNRESTRICTED      TRUE
       JOBTYPE           FORCE      ! Options are SP/FORCE/OPT
       EXCHANGE          HF
       DO_O2             2          ! O2 with O(N^4) MOS-MP2 algorithm
       OMEGA             600        ! Omega = 600/1000 = 0.6 a.u.
       SCF_ALGORITHM     DIIS_GDM
       SCF_GUESS         GWH
       BASIS             sto-3g
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

Although O2 (or OOMP2) was successful in numerous applications, there are two
limitations of this model. First of all, the energy optimization often runs
into a numerical instability caused by the singularity of the MP2 energy due to
a small energy denominator. Secondly, the disappearance of Coulson-Fischer
point hinders the use of *essential* symmetry breaking. This led David
Stück and Martin Head-Gordon to regularized OOMP2 where they employed a
linear level shift parameter, $\delta$, to stabilize small energy
denominators.[[1318]](../bib_references/bib.md#bib1376)
 The thermochemistry performance of
$\delta$-OOMP2 was found to be disappointing when one wishes to keep $\delta$
large enough to recover the Coulson-Fischer point.[[1155]](../bib_references/bib.md#bib1207)

Joonho Lee working with Martin Head-Gordon developed a new regularized OOMP2
suite of methods that utilizes an energy-dependent regularizer
($\kappa$-regularizer) unlike the $\delta$-regularizer.[[782]](../bib_references/bib.md#bib825)

The $\kappa$-regularizer modifies the MP2 correlation energy as follows:

<a id="eq:kmp2"></a>

$$
E_{\kappa-\text{MP2}}=-\frac{1}{4}\sum_{ijab}\frac{|\langle ij||ab\rangle|^{2}}{\Delta_{ij}^{ab}}\left(1-\exp(-\kappa\Delta_{ij}^{ab})\right)^{2} \tag{6.29}
$$

where the energy denominator $\Delta_{ij}^{ab}=\epsilon_{a}\epsilon_{b}-\epsilon_{i}-\epsilon_{j}$ and $\kappa$ controls the regularization strength.
Evidently, $\kappa=0$ gives zero correlation energy (*i.e.*, HF) and $\kappa\rightarrow\infty$ recovers the unregularized MP2 energy expression. In
$\kappa$-OOMP2, orbitals are then determined as a minimizer for $E_{\text{HF}}E_{\kappa-\text{MP2}}$. The $\kappa$ value of 1.45 $E_{h}^{-1}$ is recommended
due to its good balance between the Coulson-Fischer point recovery and
thermochemistry performance. It should be noted that $\kappa$-OOMP2 runs
through **Q-Chem**’s new SCF library, `libgscf`, and new MP2 library,
`libgmbpt`. The older OOMP2 code (written by Rohini Lochan and David
Stück) is no longer supported and should be used with a greater caution.
Furthermore, the new OOMP2 code can handle restricted (R), complex, restricted
(cR), unrestricted (U), generalized (G), and complex, generalized (cG) orbital
types. The complex, unrestricted (cU) orbital type is not yet supported due to
its limited applicability.

Summary of rem variables relevant to run $\kappa$-OOMP2:

| CORRELATION | None (default) |
| --- | --- |
| JOBTYPE | sp (default) single point energy evaluation; force (force supported); opt (geometry optimization supported) |
| BASIS | user’s choice (standard or user-defined: GENERAL or MIXED ) |
| GEN_SCFMAN_FINAL | TRUE (default if $\kappa$ -OOMP2 is requested) |
|  | FALSE (default for other SCF jobs) |
| SCF_ALGORITHM | GDM (default) |
|  | DIIS |
|  | GDM-LS |
| AUX_BASIS | corresponding auxiliary basis (standard or user-defined: |
|  | AUX_GENERAL or AUX_MIXED ) |
| REGULARIZED_O2 | 0 (no regularizer; default) |
|  | 1 ( $\delta$ -regularizer) |
|  | 2 ( $\kappa$ -regularizer; recommended) |
|  | 3 ( $\sigma$ -regularizer) |
| REG_PARAMETER | regularization parameter multiplied by 1e ${}^{3}$ ; no default |
|  | 1450 (Recommended value for $\kappa$ -OOMP2) |
| N_FROZEN_CORE | 0 (Code supports this functionality but it is not |
|  | recommended due to some convergence issues) |
| N_FROZEN_VIRTUAL | 0 (Code supports this functionality but it is not |
|  | recommended due to some convergence issues) |
| SCS | 0 (default) |
|  | 1 Turns on spin-component scaling with SCS-OOMP2, |
|  | 2 SOS-OOMP2, |
|  | 3 arbitrary SCS-OOMP2 |
| SSS_FACTOR | 1000000 (default) Specify same-spin-component scaling factor (multiplied by 1e ${}^{6}$ ) |
| SOS_FACTOR | 1000000 (default) Specify opposite-spin-component scaling factor (multiplied by 1e ${}^{6}$ ) |
| DO_S2 | 0 (default) |
|  | 1 (Compute $\langle\hat{S}^{2}\rangle$ at the MP2 level) |

???+ example "Example 6.14: Example of $\kappa$ -OOMP2 with the cG orbital type applied to OH"
    ```qchem
    $molecule
       0  2
       O  -2.766559046  0.187082886   0.566917837
       H  -3.696304300  1.179189102  -0.642506882
    $end
    
    $rem
       BASIS              cc-pvdz
       AUX_BASIS          rimp2-cc-pvdz
       EXCHANGE           hf
       THRESH             14
       INPUT_BOHR         true
       SCF_CONVERGENCE    8
       SCF_ALGORITHM      gdm
       MAXSCF             1000
       SCF_GUESS          sad
       GEN_SCFMAN         true
       GEN_SCFMAN_FINAL   true
       N_FROZEN_CORE      0      ! no frozen core
       N_FROZEN_VIRTUAL   0      ! no frozen virtual
       DO_O2              3      ! run OOMP2
       REGULARIZED_O2     2      ! use kappa-regularizer
       REG_VARIABLE       1450   ! set kappa = 1.45
       SCS                3      ! use arbitrary SCS
       SOS_FACTOR         883532 ! use cos = 0.883532
       SSS_FACTOR         883532 ! use css = 0.883532
       DO_S2              1      ! compute s^2 at the MP2 level
       UNRESTRICTED       true   ! use unrestricted
       GHF                true   ! use generalized
       COMPLEX            true   ! use complex
       INTEGRAL_SYMMETRY  false
    $end
    ```

???+ example "Example 6.15: Example of $\kappa$ -OOMP2 with the R orbital type applied to a water dimer"
    ```qchem
    $molecule
       0  1
       O    -2.766559046    0.187082886    0.566917837
       H    -3.696304300    1.179189102   -0.642506882
       H    -3.395837846   -1.509891173    0.389283582
       O     2.587035064    0.275900014   -0.746441819
       H     3.579141280    0.918406897    0.633058252
       H     0.852266482    0.311804811   -0.156847268
    $end
    
    $rem
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       EXCHANGE          hf
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     gdm
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN        true
       UNRESTRICTED      false  ! use restricted
       DO_O2             3      ! run OOMP2
       REGULARIZED_O2    2      ! use kappa-regularizer
       REG_VARIABLE      1450   ! set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```
