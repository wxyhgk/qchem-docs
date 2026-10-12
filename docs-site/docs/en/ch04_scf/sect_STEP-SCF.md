---
title: "4.5.16 State-Targeted Energy Projection (STEP)"
---

## 4.5.16 State-Targeted Energy Projection (STEP)

(July 4, 2026)

The maximum overlap method (Sec. [4.5.14](topic_mom.md)) is successful in many cases, but when optimizing
excited state orbitals it can be prone to variational collapse (falling from the target configuration to
the ground state). This behavior was improved with the “initial” MOM (IMOM) procedure, which
uses the initial guess molecular orbital coefficients as the reference for the overlap criterion
(see Sec. [7.7.2](../ch07_excited/ex_OpSing.md) for details). While IMOM lends a significant improvement to the MOM,
it occasionally also falls victim to variational collapse, incentivizing the
pursuit of alternatives to these methods.

One such alternative, proposed by Kevin Carter-Fenk and John Herbert, is the
state-targeted energy projection (STEP) procedure, which applies a simple level-shift
formalism to converge to the target state.[[196]](../bib_references/bib.md#bib189)

The STEP algorithm retains the cost-effectiveness of the MOM procedures
(about the same cost per cycle as a normal SCF), while simultaneously being
far more robust in converging to the target state.
Further details on the STEP procedure can be found in Section [7.7.8](../ch07_excited/ex_ROSTEP.md), and
for a complete account of the STEP algorithm the reader is referred to Ref. [[196]](../bib_references/bib.md#bib189)
.

The STEP-related *$rem* variables are the following:

### `STEP`

> **Activates the STEP procedure.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not apply the STEP level-shift algorithm.
>     * `TRUE`: Apply the STEP level-shift algorithm.
> * **Recommendation**: None

### `STEP_EPSILON`

> **Scales the size of the occupied/virtual gap imposed by the level-shift by $N$ /100 Hartree.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $N$
> * **Recommendation**: Use the default unless convergence issues arise, in which case a larger value can be used until the desired state is found. Be aware that increasing the occupied/virtual gap in level-shift algorithms slows convergence so it may be advisable to increase SCF_MAX_CYCLES if large shifts are required.

### `STEP_PRINT`

> **Controls the print level for STEP algorithm information.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: Do not print any information about STEP between SCF cycles.
>     * `1`: Print the level-shift applied at each SCF cycle (R- and U-STEP).
>     * `2`: Print the level-shift for both mixed and triplet states at each SCF cycle (RO-STEP).
> * **Recommendation**: Use the default. Level shifts of 0 indicate that an aufbau criterion is sufficient to determine orbital occupation, and shifts $>0$ imply non- aufbau selection of the occupied space.
