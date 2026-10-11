---
title: "7.7.5 Squared-Gradient Minimization"
---

## 7.7.5 Squared-Gradient Minimization

(July 4, 2026)

The squared-gradient minimization (SGM) algorithm[[511]](../bib_references/bib.md#bib526)
 sidesteps
the challenge of optimizing a saddle point in the space of orbital rotation
variables $\vec{\theta}$, by instead minimizing the square of the energy
gradient with respect to those variables. Ground-state SCF methods seek to
minimize the energy $E$ with respect to $\vec{\theta}$ and therefore the
gradient $\hat{\bm{\nabla}}_{\vec{\theta}}E$ must be zero at convergence. It is
therefore possible to obtain the same result by minimizing
$\Delta(\vec{\theta})=\|\hat{\bm{\nabla}}_{\vec{\theta}}E\|^{2}$ to zero.
However, all stationary points of $E$ are minima of $\Delta(\vec{\theta})$, not
just the ground state. It is therefore possible to optimize excited-state
orbitals by starting from a reasonable guess (such as a non-*aufbau*
configuration corresponding to the excitation) and minimizing
$\Delta(\vec{\theta})$. This avoids all the pitfalls of attempting to optimize
unstable stationary points in $E$ and thus averts variational collapse.

The SGM algorithm in **Q-Chem** can be used to optimize orbitals for two different
excited state approaches: $\Delta$SCF and ROKS. The former simply attempts to
minimize the energy of a single Slater determinant, which is often sufficient
for many challenging excitations (including many double
excitations).[[75]](../bib_references/bib.md#bib59)
 However, many
excitations (including all single excitations from a closed shell ground state)
break electron pairs, leading to states that cannot be described with a single
determinant. It is possible to spin-purify the energy of a spin-contaminated,
non-*aufbau* determinant *a posteriori*, but this requires at least
two separate orbital optimizations. An alternative is ROKS (as described in
Section [7.7.4](ex_ESROKS.md), which requires optimization of only a single set of
orbitals, for which the spin-purified energy is stationary. Analytic nuclear
gradients are available for both $\Delta$SCF and ROKS, permitting geometry
optimizations and *ab initio* molecular dynamics. Analytic frequencies are
available for $\Delta$SCF, including functionals that contain VV10 nonlocal correlation.

There are some slight differences between use of SGM for different orbital
classes due to ease of implementation. The $\Delta$SCF procedure with
restricted closed-shell (R) and unrestricted (U) orbitals can be run with
SCF_ALGORITHM = SGM_LS or SCF_ALGORITHM =
SGM_QLS, with initial orbital occupation specified by the *$occupied* block (as described in Section [7.7.2](ex_OpSing.md) and in Examples 7.7.5
and 7.7.5 below). A $\Delta$SCF calculation with restricted
open-shell (RO) orbitals or an ROKS calculation can be performed via
SCF_ALGORITHM = SGM or SCF_ALGORITHM =
SGM_LS, and a re-ordering of orbitals to ensure that the unpaired
ones lie at the frontier. (See Examples 7.7.5 and
7.7.5 below.) The gradient of $\Delta(\vec{\theta})$ is
computed analytically (except in the case of functionals that contain VV10
nonlocal correlation), for R-, U- and RO-$\Delta$SCF, at a cost equal to a
single Fock build. However, the gradient $\Delta(\vec{\theta})$ in the ROKS
case, and for functionals containing VV10, is computed with a finite-difference
approach [see Eq. ([4.47](../ch04_scf/sub_stability_analysis.md#eq:fd_mat_vec))]. In those cases, the cost is equal
to that of two Fock builds. Cumulatively, a single SGM iteration costs twice
as much as a single GDM iteration when the analytic $\Delta(\vec{\theta})$
gradient is available, and three times as much if the finite difference
construction must be used, although this does not affect the asymptotic scaling
of the calculation with respect to system size.

Excited-state orbital optimization sometimes requires more iterations than what
is typical for ground-state SCF calculations, so MAX_SCF_CYCLES
should be set to a large value (perhaps 200), rather than the default value of
50. A loose convergence threshold of SCF_CONVERGENCE = 4 is also
permissible if only energies are desired, as long as it is explicitly confirmed
that the variation in energy over several iterations is much less than the
desired accuracy after job completion. (A variation greater than
$10^{-3}~{}E_{h}$ or 0.03 eV would be quite problematic, for example.) Further
reduction of SCF_CONVERGENCE likely compromises properties such as
dipole moments or nuclear gradients, and is not recommended.

SCF_ALGORITHM

### `SCF_ALGORITHM`

> **Algorithm used for converging the SCF.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * SGM
>     * SGM_LS
>     * SGM_QLS
> * **Recommendation**: SGM should be used for RO- $\Delta$ SCF or ROKS calculations only. SGM_LS is recommended for R- or U- $\Delta$ SCF, though it can also be used for RO- $\Delta$ SCF or ROKS. SGM_QLS is a slower but more robust option for R- and U- $\Delta$ SCF calculations.

DELTA_GRADIENT_SCALE

### `DELTA_GRADIENT_SCALE`

> **Scales the gradient of $\Delta$ by $N$ /100, which can be useful for cases with troublesome convergence by reducing step size.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $N$
> * **Recommendation**: Use default. For problematic cases, $N=$ 50, 25, 10 or even $N=1$ could be useful.

ROKS

### `ROKS`

> **Controls whether ROKS calculation will be performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * ROKS is not performed.
>     * TRUE
>     * ROKS will be performed.
> * **Recommendation**: Set to TRUE if ROKS calculation is desired. UNRESTRICTED = FALSE should also be ensured.

???+ example "Example 7.52: Restricted $\Delta$ SCF double excitation from $2s$ to $2p$ of Be atom, using SGM_QLS and the ground
state orbitals as an initial guess."
    ```qchem
    $comment
       Calculates Delta-SCF excitation energy for the 2s^2 -> 2p^2 excitation of Be
       using SCAN and SGM_QLS scf convergence
    $end
    
    $molecule
       0 1
       Be
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     diis
       XC_GRID           000099000590
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_ALGORITHM     sgm_qls
       SCF_GUESS         read
       XC_GRID           000099000590
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $occupied
       1 3
       1 3
    $end
    ```

???+ example "Example 7.53: ROKS single excitation from HOMO to LUMO for an NH ${}_{3}$ $\cdots$ F ${}_{2}$ model complex,
which describes electron transfer from NH ${}_{3}$ to F ${}_{2}$ . Ground
state orbitals are used as an initial guess."
    ```qchem
    $molecule
       0 1
       N  0.0000   0.0000    0.0000
       H  0.0000  -0.9377   -0.3816
       H  0.8121   0.4689   -0.3816
       H -0.8121   0.4689   -0.3816
       F  0.0000   0.0000    6.0000
       F  0.0000   0.0000    7.4120
    $end
    
    $rem
       METHOD            pbe0
       BASIS             cc-pVDZ
       SCF_CONVERGENCE   8
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY False
    $end
    
    @@@
    
    $comment
       The reorder section is superfluous here since the excitation is HOMO to LUMO
       and thus the unpaired electron orbitals are already at the frontier.
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            pbe0
       BASIS             cc-pVDZ
       SCF_ALGORITHM     sgm
       ROKS              true
       SCF_GUESS         read
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $reorder_mo
       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    $end
    ```

???+ example "Example 7.54: Unrestricted $\Delta$ SCF single excitation from HOMO $-1$ to LUMO $+1$ for the HCHO molecule
using SGM_LS SCF convergence algorithm and the ground
state orbitals as an initial guess."
    ```qchem
    $comment
       Calculates Delta-SCF excitation energy for the HOMO-1 -> LUMO+1
       excitation of HCHO using SCAN and SGM_LS convergence
    $end
    
    $molecule
       0 1
       O1     0.0000   0.0000   1.2050
       C2     0.0000   0.0000   0.0000
       H3     0.0000   0.9429  -0.5876
       H4     0.0000  -0.9429  -0.5876
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     diis
       XC_GRID           000099000590
       GEN_SCFMAN        true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_ALGORITHM     sgm_ls
       SCF_GUESS         read
       XC_GRID           000099000590
       GEN_SCFMAN        true
       UNRESTRICTED      true
       SCF_CONVERGENCE   7
       MAX_SCF_CYCLES    500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $occupied
       1 2 3 4 5 6 8 10
       1 2 3 4 5 6 7 8
    $end
    ```

???+ example "Example 7.7.55: Combined RO- $\Delta$ SCF core-ionization and $1s\rightarrow\text{LUMO}+1$ ROKS core-excited state."
    ```qchem
    $molecule
       0 1
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       method            scan
       basis             aug-cc-pCVTZ
       integral_symmetry false
    $end
    
    @@@
    
    $comment
       Calculates the RO-DeltaSCF core ionized state. The reorder section pushes F1s
       (first by energy) to the frontier, instead of the HOMO (5th orbital).
    $end
    
    $molecule
       1 2
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pCVTZ
       UNRESTRICTED      false
       SCF_GUESS         read
       SCF_ALGORITHM     sgm
       INTEGRAL_SYMMETRY false
    $end
    
    $reorder_mo
       2 3 4 5 1
       2 3 4 5 1
    $end
    
    @@@
    
    $comment
       Calculates the ROKS core excited state. The O1s orbital is in the place of the HOMO
       from the previous reordering. The present reorder section pushes the LUMO+1 orbital
       (the 7th orbital) to the frontier, instead of the LUMO (6th orbital).
    $end
    
    $molecule
       0 1
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       METHOD           scan
       ROKS             true
       BASIS            aug-cc-pCVTZ
       SCF_GUESS        read
       SCF_ALGORITHM    sgm
       MAX_SCF_CYCLES   200
       INTEGRAL_SYMMETRY false
    $end
    
    $reorder_mo
       1 2 3 4 5 7 6
       1 2 3 4 5 7 6
    $end
    ```
