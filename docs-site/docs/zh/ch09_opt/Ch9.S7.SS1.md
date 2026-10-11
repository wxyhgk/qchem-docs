---
title: "9.7.1 Overview"
---

## 9.7.1 Overview

(July 4, 2026)

The concept of a reaction path is chemically intuitive (a pathway from
reactants to products) yet somewhat theoretically ambiguous because most
mathematical definitions depend upon the chosen coordinate system. Stationary
points on a potential energy surface are independent of this choice, but the
path connecting them is not, and there exist various mathematical definitions
of a “reaction path”. **Q-Chem** uses the intrinsic reaction coordinate (IRC)
definition, as originally defined by Fukui,[[417]](../bib_references/bib.md#bib426)
 which has come to
be a fairly standard choice in quantum chemistry. The IRC is essentially
sequence of small, steepest-descent paths going downhill from the transition state.

The reaction path is most unlikely to be a straight line and so by taking a
finite step length along the direction of the gradient you will leave the
“true” reaction path. A series of small steepest descent steps will zig-zag
along the actual reaction path (a behavior known as “stitching”). Ishida
*et al.*[[615]](../bib_references/bib.md#bib638)
 developed a predictor-corrector algorithm, involving
a second gradient calculation after the initial steepest-descent step, followed
by a line search along the gradient bisector to get back on the path, and this
algorithm was subsequently improved by Schmidt *et al.*.[[1214]](../bib_references/bib.md#bib1268)

This is the method that **Q-Chem** adopts. It cannot be used for the first
downhill step from the transition state, since the gradient is zero, so instead
a step is taken along the Hessian mode whose frequency is imaginary.

The reaction path can be defined and followed in $Z$-matrix coordinates,
Cartesian coordinates or mass-weighted Cartesian coordinates. The latter
represents the “true” IRC as defined by Fukui.[[417]](../bib_references/bib.md#bib426)
 If the
rationale for following the reaction path is simply to determine which local
minima are connected by a given transition state, which, is arguably the major
use of IRC algorithms, then the choice of coordinates is irrelevant. In order
to use the IRC code, the transition state geometry and the exact Hessian must
be available. These must be computed via two prior calculations, with
JOBTYPE = TS (transition structure search) and
JOBTYPE = FREQ (Hessian calculation), respectively. Job
control variables and examples appear below.

An IRC calculation is invoked by setting JOBTYPE = RPATH in
the *$rem* section, and additional *$rem* variables are described below. IRC
calculations may benefit from the methods discussed in
Section [9.3](sec_better_TS_guess.md) for obtaining good initial guesses for
transition-state structures. The final pathway (in both forward and backward
directions) is printed at the end of the **Q-Chem** output file as a sequence of
Cartesian-coordinate geometries representing steps along the pathway. The format
for this output is a standard one that is readable, for example, by the
Visual Molecular Dynamics (VMD) program.[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)

RPATH_COORDS

### `RPATH_COORDS`

> **Determines which coordinate system to use in the IRC search.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * Use mass-weighted coordinates.
>     * 1
>     * Use Cartesian coordinates.
>     * 2
>     * Use
>     * Z
>     * -matrix coordinates.
> * **Recommendation**: Use the default. Note that use of $Z$ -matrix coordinates requires that geometries be input in $Z$ -matrix format.

RPATH_DIRECTION

### `RPATH_DIRECTION`

> **Determines the first direction of the eigenmode to follow. This will not usually be known prior to the Hessian diagonalization.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * Descend in the positive direction of the eigenmode, then restart in the negative direction.
>     * -1
>     * Descend in the negative direction of the eigenmode, then restart in the positive direction.
> * **Recommendation**: It is usually not possible to determine in which direction to go a priori , so both directions are automatically considered. A job that reads in the final geometry from the reaction path job will use the final step from the second direction.

RPATH_MAX_CYCLES

### `RPATH_MAX_CYCLES`

> **Specifies the maximum number of points to find on the reaction path.**
>
> * **Type**: `INTEGER`
> * **Default**: `20`
> * **Options**:
>     * $n$
>     * User-defined number of cycles.
> * **Recommendation**: Use more points if the minimum is desired, but not reached using the default.

RPATH_MAX_STEPSIZE

### `RPATH_MAX_STEPSIZE`

> **Specifies the maximum step size to be taken (in 0.001 a.u.).**
>
> * **Type**: `INTEGER`
> * **Default**: `150`
> * **Options**:
>     * $n$
>     * Step size =
>     * $n$
>     * /1000 a.u.
> * **Recommendation**: None.

RPATH_TOL_DISPLACEMENT

### `RPATH_TOL_DISPLACEMENT`

> **Specifies the convergence threshold for the step. If a step size is chosen by the algorithm that is smaller than this, the path is deemed to have reached the minimum.**
>
> * **Type**: `INTEGER`
> * **Default**: `5000`
> * **Options**:
>     * $n$
>     * User-defined. Tolerance =
>     * $n$
>     * /1000000 a.u.
> * **Recommendation**: Use the default. Note that this option only controls the threshold for ending the RPATH job and does nothing to the intermediate steps of the calculation. A smaller value will provide reaction paths that end closer to the true minimum. Use of smaller values without adjusting RPATH_MAX_STEPSIZE , however, can lead to oscillations about the minimum.

RPATH_PRINT

### `RPATH_PRINT`

> **Specifies the print output level.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * $n$
> * **Recommendation**: Use the default, as little additional information is printed at higher levels. Most of the output arises from the multiple single point calculations that are performed along the reaction pathway.

???+ example "Example 9.25: Reaction path search. Note that there are three required jobs: a TS search,
followed by a frequency (Hessian) calculation, and finally the IRC calculation."
    ```qchem
    $molecule
       0 1
       C
       H 1 1.20191
       N 1 1.22178 2 72.76337
    $end
    
    $rem
       JOBTYPE            ts
       BASIS              sto-3g
       METHOD             hf
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE            freq
       METHOD             hf
       BASIS              sto-3g
       SCF_GUESS          read
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE            rpath
       BASIS              sto-3g
       METHOD             hf
       SCF_GUESS          read
       RPATH_MAX_CYCLES   50
    $end
    ```
