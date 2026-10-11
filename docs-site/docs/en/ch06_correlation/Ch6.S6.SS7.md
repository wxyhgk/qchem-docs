---
title: "6.6.7 Brueckner CC2"
---

## 6.6.7 Brueckner CC2

(July 4, 2026)

Brueckner orbitals (BOs) are shown to largely ameliorate the artificial
symmetry breaking that occurs at the Hartree-Fock (HF) level.[[783]](../bib_references/bib.md#bib826)

This can lead to improved results even in higher order wave function theories
that typically use HF orbitals as a starting point. Unfortunately, the cheapest
traditional Brueckner theory, Brueckner doubles (BD), is still quite
computationally demanding. Orbital optimized MP2 (OOMP2) was proposed as a
low scaling approximation to BD,[[852]](../bib_references/bib.md#bib888)
 due to its similarity to orbital
optimized coupled cluster doubles (OOCCD). Another possible source of
approximate BD orbitals is Bruckner CC2 (BCC2).[[30]](../bib_references/bib.md#bib14)

Rather than optimizing the energy as in OOMP2, BCC2 optimizes the orbitals
in order to reduce the CC2 t${}_{1}$ amplitudes to 0. In the absence of t${}_{1}$
amplitudes, the CC2 doubles amplitudes are exactly the same as MP2, and the
singles amplitude equations are as follows:

<a id="eq:bcc2"></a>

$$
\Omega_{i}^{a}=f_{ai}+\sum_{jb}f_{jb}t_{ij}^{ab}+\frac{1}{2}\sum_{jbc}\langle
ja||cb\rangle t_{ij}^{bc}+\frac{1}{2}\sum_{jkb}\langle jk||bi\rangle t_{jk}^{ab} \tag{6.30}
$$

BCC2 has a computational cost scaling as $\mathcal{O}(o^{2}v^{3})$ - a significant
improvement over OOCCD/BD, and can greatly improve the quality of orbitals over
HF in open-shell molecules due to the reduction of artificial spin contamination.

???+ example "Example 6.16: Example of BCC2 methodology"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       UNRESTRICTED      TRUE
       JOBTYPE           SP
       EXCHANGE          HF
       GEN_SCFMAN_FINAL  TRUE
       DO_BCC2           3                run BCC2
       SCF_ALGORITHM     DIIS
       SCF_GUESS         GWH
       BASIS             sto-3g
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

As CC2 is a perturbative approach similar to MP2, breakdowns occur in the
presence of orbital degeneracy. While BCC2 does not explicitly optimize the
energy and thereby drive orbitals toward degeneracy, results are still severely
hindered when orbital energy differences become small. The $\kappa$ regularizer
originally proposed by Joonho Lee and Martin Head-Gordon[[782]](../bib_references/bib.md#bib825)
 can be used in to
further improve the results of BCC2 in this case. The regularizer is applied by
modifying the $t_{ij}^{ab}$ amplitudes as follows:

<a id="eq:kbcc2"></a>

$$
t_{ij}^{ab}=\frac{-\langle ab||ij\rangle}{\Delta_{ij}^{ab}}\left(1-\exp(-\kappa\Delta_{ij}^{ab})\right)^{2} \tag{6.31}
$$

As in $\kappa$-OOMP2, the parameter $\kappa$ sets the regularization strength,
with $\kappa=0$ yielding HF, and $\kappa=\infty$ yielding unregularized BCC2.
A value of $\kappa=1.2$ $E_{h}^{-1}$ is suggested for most applications.
$\kappa$-BCC2 runs through `libgscf` and `libgmbpt`.
Currently, DIIS should be used to converge BCC2 orbitals, as the singles
residual is not an orbital gradient and cannot be used with gradient-based
algorithms. The BCC2 code can currently handle restricted (R) and unrestricted
(U) orbital types.

Summary of rem variables relevant to run $\kappa$-BCC2:

| CORRELATION | None (default) |
| --- | --- |
| JOBTYPE | sp (default) single point energy evaluation |
| BASIS | user’s choice (standard or user-defined: GENERAL or MIXED ) |
| GEN_SCFMAN_FINAL | TRUE |
| SCF_ALGORITHM | DIIS (gradient based algorithms currently unsupported) |
| AUX_BASIS | corresponding auxiliary basis (standard or user-defined: |
|  | AUX_GENERAL or AUX_MIXED ) |
| DO_BCC2 | 3 (run BCC2) |
| REGULARIZED_BCC2 | 0 (no regularizer; default) |
|  | 1 ( $\delta$ -regularizer) |
|  | 2 ( $\kappa$ -regularizer; recommended) |
|  | 3 ( $\sigma$ -regularizer) |
| REG_PARAMETER | regularization parameter multiplied by 1e ${}^{3}$ ; no default |
|  | 1200 (Recommended value for $\kappa$ -BCC2) |
| N_FROZEN_CORE | 0 (frozen core currently unsupported) |
| N_FROZEN_VIRTUAL | 0 (frozen core currently unsupported) |
| DO_S2 | 0 (default) |
|  | 1 (Compute $\langle\hat{S}^{2}\rangle$ at the MP2 level) |

???+ example "Example 6.17: Example of $\kappa$ -BCC2 with the R orbital type applied to a water dimer"
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
       EXCHANGE          hf
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN_FINAL  true
       UNRESTRICTED      false    use restricted
       DO_BCC2           3        run BCC2
       REGULARIZED_O2    2        use kappa-regularizer
       REG_VARIABLE      1450     set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "Example 6.18: Example of $\kappa$ -BCC2 with the U orbital type applied to an OH radical"
    ```qchem
    $molecule
    0  2
    O -2.766559046 0.187082886 0.566917837
    H -3.6963043 1.179189102 -0.642506882
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN_FINAL  true
       UNRESTRICTED      true   ! use unrestricted
       DO_BCC2           3      ! run BCC2
       REGULARIZED_O2    2      ! use kappa-regularizer
       REG_VARIABLE      1450   ! set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```
