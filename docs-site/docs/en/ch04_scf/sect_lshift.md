---
title: "4.5.5 Level-Shifting"
---

## 4.5.5 Level-Shifting

(July 4, 2026)

Level-shifting is an old technique that may facilitate SCF convergence in
systems having small HOMO/LUMO
gaps.[[578]](../bib_references/bib.md#bib599)
 If the gap is small, a simple
Fock matrix diagonalization (Roothaan step) may alter the energetic ordering of
the molecular orbitals, so that after re-populating the electrons according to
the *aufbau* principle, the overall effect is a discontinuous switch in
the electron configuration, and the SCF process fails to converge. To remedy
this fluctuating SCF behavior, one can shift the diagonal elements of the
virtual block of the Fock matrix (“level-shifting”) to increase the
calculated HOMO/LUMO gap before diagonalization. With proper
level-shifting, the energetic ordering of the molecular orbitals is preserved
during diagonalization and thus the shapes of the orbitals are changed in a
continuous way at each SCF cycle, leading to a stable iterative process. Using
perturbation theory, one can show that a proper level shift guarantees that the
total energy is lowered after Fock matrix
diagonalization.[[578]](../bib_references/bib.md#bib599)
 It is important to note,
however, that SCF solutions obtained via level-shifting are not necessarily
stable ground states. To check the stability of the converged electronic
state, we recommend invoking the keywords STABILITY_ANALYSIS or
INTERNAL_STABILITY (see Section [4.3.3](sub_SCF_addOps.md) and
Section [4.5.17](sub_stability_analysis.md)).

In cases where DIIS or some other SCF algorithm converges quickly, application
of a level shift usually slows down convergence. In addition, experiences show
that level-shifting can converge difficult SCF cases to moderate thresholds
such as $10^{-5}$, but becomes less efficient as the convergence threshold is
tightened, say, to $10^{-8}$. To obtain tightly-converged solutions,
level-shifting should be combined with DIIS or another convergence algorithm.
For difficult SCF cases, invoking level-shifting in the early SCF iterations
and then turning it off later (in favor of DIIS, say) is often the best
strategy. As such, **Q-Chem** offers a hybrid SCF algorithm that combines
level-shifting with DIIS. This is invoked by setting SCF_ALGORITHM =
LS_DIIS. Level-shifting can also be used on its own (without DIIS),
by means of the following *$rem* variables.

LEVEL_SHIFT

### `LEVEL_SHIFT`

> **Determine whether to invoke level-shifting or not together with DIIS.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Apply level shifting.
>     * FALSE
>     * Do not apply level shifting.
> * **Recommendation**: Use TRUE if level-shifting is necessary to accelerate SCF convergence.

GAP_TOL

### `GAP_TOL`

> **HOMO/LUMO gap threshold to control whether to shift the diagonal elements of the virtual block of the Fock matrix or not. If the HOMO/LUMO gap is less than this threshold, at a given SCF iteration, then the diagonal elements of the virtual block of the Fock matrix are shifted. Otherwise no level-shift is applied.**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * User-defined
> * **Recommendation**: The input number must be an integer between 0 and 9999. The threshold applied is set to /1000 Eh. The default value is provided to make the level-shifting calculation run and should not be taken as optimal for any specific problem. Trial and error may be required to find the optimal threshold. Larger values of generally lead to level-shifting being used more frequently during the SCF convergence process.

LSHIFT

### `LSHIFT`

> **Constant shift applied to all diagonal elements of the virtual block of the Fock matrix.**
>
> * **Type**: `INTEGER`
> * **Default**: `200`
> * **Options**:
>     * User-defined
> * **Recommendation**: The input number must be an integer between 0 and 9999. The actual shift is equal to /1000 Eh. The default value is provided to make the level-shifting calculation run and should not be taken as optimal for any specific problem. Trial and error may be required to find the optimal threshold. Larger level shifts make the SCF process more stable but also slow down convergence, thus requiring more SCF cycles.

**Note: 

If either GAP_TOL or LSHIFT or both are explicitly
specified, then LEVEL_SHIFT is automatically set to TRUE.
Setting LEVEL_SHIFT = FALSE disables any values of
GAP_TOL and LSHIFT. Invoking the LS_DIIS algorithm also
disables any setting of LEVEL_SHIFT.
**

MAX_LS_CYCLES

### `MAX_LS_CYCLES`

> **The maximum number of DIIS iterations with level-shifting when SCF_ALGORITHM = LS_DIIS . See also THRESH_LS_SWITCH .**
>
> * **Type**: `INTEGER`
> * **Default**: `MAX_SCF_CYCLES`
> * **Options**:
>     * 1
>     * Only a single DIIS step with level-shifting, and no level-shifting for the remaining DIIS steps.
>     * $n$
>     * $n$
>     * DIIS iterations with level-shifting before turning level-shifting off.
> * **Recommendation**: None

THRESH_LS_SWITCH

### `THRESH_LS_SWITCH`

> **The threshold for turning off level-shifting in DIIS is $10^{-\mbox{{\small THRESH\_LS\_SWITCH}}}$ when SCF_ALGORITHM is set to LS_DIIS . See also MAX_LS_CYCLES .**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * User-defined.
> * **Recommendation**: None

???+ example "Example 4.9: Input for a RKS calculation using DIIS with level-shifting on a uranium compound."
    ```qchem
    $molecule
    0 1
      U   -0.7734808   -0.8815596   -0.8853446
      O   -1.3090665   -2.1863261   -2.7399692
      O   -1.6134743    1.0032462   -1.9673881
      O   -0.2537507    0.4215612    0.9749395
      O    0.0643962   -2.7662217    0.1985884
      O   -2.4384926   -1.2003830   -0.1700214
      O    0.8915310   -0.5627363   -1.6006679
      H   -0.5266214   -2.1731728   -3.3131242
      H   -2.5519330    1.0551966   -1.7276040
      H    0.6520521    0.7395638    0.8360306
      H   -0.6807322   -3.1486006    0.6879451
    $end
    
    $rem
       METHOD          = B3LYP
       BASIS           = LANL2DZ
       ECP             = fit-LANL2DZ
       MAX_SCF_CYCLES  = 200
       THRESH          = 10
       LEVEL_SHIFT     = TRUE
       GAP_TOL         = 200
       LSHIFT          = 200
       SCF_CONVERGENCE = 5
    $end
    ```

???+ example "Example 4.10: Input for a UKS calculation using LS_DIIS on a cobalt compound."
    ```qchem
    $molecule
       6 2
       O    0.7515076    1.2954050    1.0605230
       O    0.7506760   -1.2982554    1.0594277
       Co   0.0016554   -0.0007951    0.0017848
       O   -1.4949030   -0.0008880    1.0616115
       O    1.4981395   -0.0006773   -1.0578583
       O   -0.7482665   -1.2970503   -1.0566523
       O   -0.7473745    1.2963844   -1.0559284
    $end
    
    $rem
       METHOD             = B3LYP
       BASIS              = 6-31G
       SCF_ALGORITHM      = LS_DIIS
       MAX_SCF_CYCLES     = 200
       GUI                = 2
       GAP_TOL            = 100
       LSHIFT             = 200
       SCF_CONVERGENCE    = 8
       STABILITY_ANALYSIS = TRUE
    $end
    ```
