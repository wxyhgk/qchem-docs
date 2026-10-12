---
title: "5.13.2 CAP-DFT Job Control"
---

## 5.13.2 CAP-DFT Job Control

(July 4, 2026)

## 5.13.2.1 *$rem* variables and keyword options

A CAP-DFT calculation can be requested by adding CAP_SCF = TRUE in *$rem*.
Currently, only a limited set of complex-variable functionals is available for combination with a CAP,
see Section [5.13.3](sub_XCfuncs_CAP.md) on how to specify the desired functional.

The CAP parameters should be specified in the *$rem* section.
The same keywords and keyword values apply as used for CAP-CC calculations:

- •

CAP_ETA, for setting the CAP strength $\eta$. 

The optimal value of $\eta$ is commonly determined through minimizing $\left|\eta dE/d\eta\right|$.
- •

CAP_TYPE, for specifying the CAP type (cubic, spherical or Voronoi).
- •

CAP_X/Y/Z, for specifying the CAP onset(s).

See Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md) for further details on these keywords.

The grid on which the CAP is integrated, can be specified using the CAP_GRID keyword.
Its possible keyword values (see below) are the same as for XC_GRID (Section [5.5](sect_quadrature.md)).
The CAP_GRID_SWITCH and CAP_NEW_GRID keywords can be used to invoke
re-evaluation of the CAP on a different grid during the course of the SCF iterations.
See below for details on these keywords.

**Note: 

The approach outlined here also works for CAP-HF calculations, by setting METHOD = HF instead of a complex-variable functional.
CAP-HF also remains accessible via the older implementation,
by setting CS_HF = 1 in *$complex_ccman* (see Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md));
however, this cannot be used for invoking CAP-DFT calculations,
and the keywords CAP_GRID, CAP_GRID_SWITCH and CAP_NEW_GRID will not be recognized.
**

### `CAP_SCF`

> **Invokes a CAP-SCF calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Invoke a CAP-SCF calculation using the more recent implementation that also allows for CAP-DFT calculations.
>     * `FALSE`: Do not invoke a CAP-SCF calculation using the more recent implementation.
> * **Recommendation**: Set to ‘TRUE’ for CAP-DFT calculations, or when re-evaluation of the CAP on a different grid during the SCF iterations is desired (see also CAP_GRID_SWITCH and CAP_NEW_GRID .)

### `CAP_GRID`

> **Specifies the type of grid to use for CAP integration. The options are the same as those of the $rem variable XC_GRID .**
>
> * **Type**: `INTEGER`
> * **Default**: `If`
> * **Options**:
>     * `0`: Use SG-0 for H, C, N, and O; SG-1 for all other atoms.
>     * $n$: Use SG-
>     * $n$: for all atoms, $n=1,2,$ or $3$ . $XY$ A string of two six-digit integers $X$ and $Y$ , where $X$ is the number of radial points and $Y$ is the number of angular points where possible numbers of Lebedev angular points, which must be an allowed value from Table 5.2 in Section 5.5 . $-XY$ Similar format for Gauss-Legendre grids, with the six-digit integer $X$ corresponding to the number of radial points and the six-digit integer $Y$ providing the number of Gauss-Legendre angular points, $Y=2N^{2}$ .
> * **Recommendation**: Employing a coarser CAP grid in the initial SCF iterations might facilitate finding the resonance state, while using a finer grid might improve convergence behavior. See also CAP_GRID_SWITCH and CAP_NEW_GRID .

### `CAP_GRID_SWITCH`

> **Specifies starting from which SCF iteration the CAP should be re-evaluated on a new grid. See also CAP_NEW_GRID .**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: Re-evaluate the CAP on a new grid starting from SCF interation
>     * $n$: .
> * **Recommendation**: The optimal value is system-dependent. Allow for a sufficient number of iterations with the initial CAP grid to ensure that the resonance state is found.

### `CAP_NEW_GRID`

> **Specifies the new grid on which the CAP is to be re-evaluated. Re-evaluation takes place starting from the $n^{\text{th}}$ SCF iteration indicated by CAP_GRID_SWITCH.**
>
> * **Type**: `INTEGER`
> * **Default**: `99000590`
> * **Options**:
>     * `The same options as`: CAP_GRID (see above).
> * **Recommendation**: Use a finer grid than CAP_GRID .

## 5.13.2.2 Finding Resonance States of Temporary Anions using CAP-DFT

Resonance states of temporary anions formally behave as excited electronic states in the electronic configuration space.
It is therefore not always straightforward for the SCF procedure to converge towards the desired state.
Additionally, CAP-DFT calculations were observed to be more difficult to converge compared to CAP-HF calculations.[[1359]](../bib_references/bib.md#bib1419)

This section therefore lists some tips for increasing the likelihood of convergence.

- •

It is crucial to provide a good SCF guess density matrix.
Examples include, but are certainly not limited to:

- **–**

a converged CAP-HF density matrix obtained at the same value of $\eta$.
- **–**

a converged CAP-DFT density matrix obtained using the same functional and at a similar value of $\eta$.
- **–**

a converged DFT density matrix obtained using the same functional
and employing charge stabilization with a small added charge.
See Section [7.9.13](../ch07_excited/sec_CAGE.md) for further details about the use of charge stabilization.
- **–**

a converged CAP-DFT density matrix obtained using the same functional, at the same value of $\eta$,
and employing charge stabilization with a small added charge.
- •

The use of the maximum overlap method (MOM, see Section [7.7.2](../ch07_excited/ex_OpSing.md)) is strongly recommended.
- •

CAP-DFT calculations were found to require a very fine grid for XC numerical quadrature,
finer than what would be needed for a conventional (real-variable) DFT calculation.
See Section [5.5](sect_quadrature.md) for details about setting the XC grid.
- •

Employing a coarser CAP grid in the initial SCF iterations might facilitate finding the resonance state,
while using a finer grid might improve convergence behavior.
For details about setting the CAP grid, see Section  5.13.2.
