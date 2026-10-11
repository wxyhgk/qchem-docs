---
title: "9.3.2 Freezing String Method"
---

## 9.3.2 Freezing String Method

(July 4, 2026)

Perhaps the most significant difficulty in locating transition states is to
obtain a good initial guess of the geometry to feed into a surface-walking
algorithm. This difficulty becomes especially relevant for large systems, for
which the dimensionality of the search space is large. Interpolation
algorithms are promising for locating good guesses of the minimum-energy
pathway connecting reactant and product states as well as approximate
saddle-point geometries. For example, the
*nudged elastic band method*[[949]](../bib_references/bib.md#bib990)

and the *string method*[[360]](../bib_references/bib.md#bib365)
 start from a certain initial reaction pathway
connecting the reactant and the product state, and then optimize in discretized
path space towards the minimum-energy pathway. The highest-energy point on the
approximate minimum-energy pathway becomes a good initial guess for the
saddle-point configuration that can subsequently be used with any local
surface-walking algorithm.

Inevitably, the performance of any interpolation method heavily relies on the
choice of the initial reaction pathway, and a poorly-chosen initial pathway can
cause slow convergence, or possibly convergence to an incorrect pathway. The
growing-string method[[1079]](../bib_references/bib.md#bib1124)
 and freezing-string
method[[104]](../bib_references/bib.md#bib91)
 offer solutions to this problem, in which
two string fragments (one representing the reactant state and the other
representing the product state) are “grown” (*i.e.*, increasingly-finely
defined) until the two fragments join. The freezing-string method offers a
choice between Cartesian interpolation and linear synchronous transit (LST)
interpolation. It also allows the user to choose between conjugate gradient
and quasi-Newton optimization techniques.

Freezing-string calculations are requested by setting JOBTYPE =
FSM in the *$rem* section. Additional job-control keywords are
described below, along with examples. Consult Refs. [[104]](../bib_references/bib.md#bib91)
 and
[[1245]](../bib_references/bib.md#bib1296)
 for a guide to a typical use of this method.

FSM_NNODE

### `FSM_NNODE`

> **Specifies the number of nodes along the string**
>
> * **Type**: `INTEGER`
> * **Default**: `12`
> * **Options**:
>     * $N$
>     * number of nodes in FSM calculation
> * **Recommendation**: $N=15$ . Use 10 to 20 nodes for a typical calculation. Reaction paths that connect multiple elementary steps should be separated into individual elementary steps, and one FSM job run for each pair of intermediates. Use a higher number when the FSM is followed by an approximate-Hessian based transition state search (Section 9.3.3 ).

FSM_NGRAD

### `FSM_NGRAD`

> **Specifies the number of perpendicular gradient steps used to optimize each node**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $N$
>     * Number of perpendicular gradients per node
> * **Recommendation**: Anything between 2 and 6 should work, where increasing the number is only needed for difficult reaction paths.

FSM_MODE

### `FSM_MODE`

> **Specifies the method of interpolation**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 1
>     * Cartesian
>     * 2
>     * LST
> * **Recommendation**: In most cases, LST is superior to Cartesian interpolation.

FSM_OPT_MODE

### `FSM_OPT_MODE`

> **Specifies the method of optimization**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 1
>     * Conjugate gradients
>     * 2
>     * Quasi-Newton method with BFGS Hessian update
> * **Recommendation**: The quasi-Newton method is more efficient when the number of nodes is high.

An example input appears below. Note that the *$molecule* section includes
geometries for two optimized intermediates, separated by `****`. The
order of the atoms is important, as **Q-Chem** assumes that the $n$th atom in the
reactant moves toward the $n$th atom in the product. The FSM string is printed
out in the file `stringfile.txt`, which contains Cartesian coordinates of
the structures that connect reactant to product. Each node along the path is
labeled in this file, and its energy is provided. The geometries and energies
are also printed at the end of the **Q-Chem** output file, where they are labeled:

```qchem
----------------------------------------
   STRING
----------------------------------------
```

Finally, if MOLDEN_FORMAT is set to TRUE, then geometries
along the string are printed in a **MolDen**-readable format at the end of the
**Q-Chem** output file. The highest-energy node can be taken from this file and
used to run a transition structure search as described in
Section [9.1.1](topic_ts_Overview.md). If the string returns a pathway that is unreasonable,
check whether the atoms in the two input geometries are in the correct order.

???+ example "Example 9.9: Example of the freezing-string method."
    ```qchem
    $molecule
       0  1
       Si   1.028032  -0.131573  -0.779689
       H    0.923921  -1.301934   0.201724
       H    1.294874   0.900609   0.318888
       H   -1.713989   0.300876  -0.226231
       H   -1.532839   0.232021   0.485307
    ****
       Si   0.000228  -0.000484  -0.000023
       H    0.644754  -1.336958  -0.064865
       H    1.047648   1.052717   0.062991
       H   -0.837028   0.205648  -1.211126
       H   -0.855603   0.079077   1.213023
    $end
    
    $rem
       JOBTYPE        fsm
       FSM_NGRAD      3
       FSM_NNODE      12
       FSM_MODE       2
       FSM_OPT_MODE   2
       METHOD         b3lyp
       BASIS          6-31G
    $end
    ```
