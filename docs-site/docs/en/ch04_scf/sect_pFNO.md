---
title: "4.5.6 Pseudo-Fractional Occupation Number Method (pFON)"
---

## 4.5.6 Pseudo-Fractional Occupation Number Method (pFON)

(July 4, 2026)

An alternative to level-shifting for cases exhibiting small (or zero)
HOMO/LUMO gaps is the pseudo-fraction occupation number (pFON)
approach,[[1140]](../bib_references/bib.md#bib1192)
 which corresponds to a “smearing out” of the
occupation numbers at the HOMO level. Often, this improves the stability and
accelerates the convergence by eliminating the discontinuous occupancy changes
(from one SCF iteration to the next) that can arise in small-gap systems.
Essentially, more than one electron configuration is allowed during the same
orbital optimization, with fractional occupancies. This is formally equivalent
to a finite-temperature formalism.

The pFON method introduces a density matrix

<a id="Ch4.E37"></a>
$$
P_{\mu\nu}=\sum_{p=1}^{N}\;n_{p}C_{\mu p}C_{\nu p} \tag{4.37}
$$

with occupancies $0\leq n_{p}\leq 1$ that can be fractional, whereas for a
conventional SCF calculation either $n_{p}=1$ (occupied) or $n_{p}=0$ (virtual).
In pFON, the occupation numbers follow a Fermi-Dirac distribution,

<a id="Ch4.E38"></a>
$$
n_{p}=\bigl{(}1+e^{(\epsilon_{p}-\epsilon_{\mathrm{F}})/kT}\bigr{)}^{-1}\;, \tag{4.38}
$$

where $\epsilon_{p}$ is an SCF eigenvalue (orbital energy) and $T$ is a
temperature. In **Q-Chem**’s implementation, the Fermi energy is set to
$\epsilon_{\mathrm{F}}=(\epsilon_{\mathrm{HOMO}}+\epsilon_{\mathrm{LUMO}})/2$. To
ensure conservation of the total number of electrons, the pFON approach
re-scales the occupation numbers so that $\sum_{p}\;n_{p}=N_{\mathrm{el}}$.

There are several parameters to control the electronic temperature $T$
throughout a pFON SCF run. The temperature can either be held constant at
finite temperature ($T_{\mathrm{init}}$ = $T_{\mathrm{final}}$), or the system can be cooled
from a higher temperature down to the final temperature. So far, no
zero-temperature extrapolation has been implemented.

OCCUPATIONS

### `OCCUPATIONS`

> **Activates pFON calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Integer occupation numbers
>     * 1
>     * Not yet implemented
>     * 2
>     * Pseudo-fractional occupation numbers (pFON)
> * **Recommendation**: Use pFON to improve convergence for small-gap systems.

FON_T_START

### `FON_T_START`

> **Initial electronic temperature (in K) for FON calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * Any desired initial temperature.
> * **Recommendation**: Pick the temperature to either reproduce experimental conditions ( e.g. room temperature) or as low as possible to approach zero-temperature.

FON_T_END

### `FON_T_END`

> **Final electronic temperature for FON calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * Any desired final temperature.
> * **Recommendation**: Pick the temperature to either reproduce experimental conditions ( e.g. room temperature) or as low as possible to approach zero-temperature.

FON_NORB

### `FON_NORB`

> **Number of orbitals above and below the Fermi level that are allowed to have fractional occupancies.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$
>     * number of active orbitals
> * **Recommendation**: The number of valence orbitals is a reasonable choice.

FON_T_SCALE

### `FON_T_SCALE`

> **Determines the step size for the cooling.**
>
> * **Type**: `INTEGER`
> * **Default**: `90`
> * **Options**:
>     * $n$
>     * temperature is scaled by
>     * $0.01\cdot n$
>     * in each cycle (cooling method 1)
>     * $n$
>     * temperature is decreased by n K in each cycle (cooling method 2)
> * **Recommendation**: The cooling rate should be neither too slow nor too fast. Too slow may lead to final energies that are at undesirably high temperatures. Too fast may lead to convergence issues. Reasonable choices for methods 1 and 2 are 98 and 50, respectively. When in doubt, use constant temperature.

FON_E_THRESH

### `FON_E_THRESH`

> **DIIS error below which occupations will be kept constant.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$
>     * freeze occupations below DIIS error of
>     * $10^{-n}$
> * **Recommendation**: This should be one or two numbers bigger than the desired SCF convergence threshold.

FON_T_METHOD

### `FON_T_METHOD`

> **Selects cooling algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * temperature is scaled by a factor in each cycle
>     * 2
>     * temperature is decreased by a constant number in each cycle
> * **Recommendation**: We have made slightly better experience with a constant cooling rate. However, choose constant temperature when in doubt.

???+ example "Example 4.11: pFON calculation of a metal cluster."
    ```qchem
    $molecule
       0 1
       Pt   -0.20408    1.19210    0.54029
       Pt    2.61132    1.04687    0.66196
       Pt    0.83227    0.03296   -1.49084
       Pt    0.95832   -1.05360    0.92253
       Pt   -1.66760   -1.07875   -1.02416
    $end
    
    $rem
       METHOD          pbe
       MAX_SCF_CYCLES  200
       ECP             fit-lanl2dz
       BASIS           lanl2dz
       OCCUPATIONS     2    ! pseudo-fractional occupation numbers
       FON_NORB        10   ! 10 fractionally occupied orbitals above and below the Fermi level
       FON_T_START     1000 ! starting electronic temperature: 1000 K
       FON_T_END       0    ! final electronic temperature: 0 K
       FON_T_METHOD    2    ! constant cooling scheme
       FON_T_SCALE     25   ! reduce the temperature by 25 K per cooling step
       FON_E_THRESH    5    ! freeze occupation numbers once DIIS error is 10-5
       GEN_SCFMAN        false
       INTEGRAL_SYMMETRY false
    $end
    
    ```
