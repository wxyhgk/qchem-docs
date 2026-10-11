---
title: "4.5.13 Black-box Robust SCF Pipelines"
---

## 4.5.13 Black-box Robust SCF Pipelines

(July 4, 2026)

In the spirit of the User-Customized Hybrid SCF Algorithm in
Section [4.5.12](sub_custom_algorithm.md), starting v6.3.0, Q-Chem provides
two “black-box” pipelines for improving the robustness of the SCF convergence
for difficult use cases.
These pipelines can be used by setting SCF_ALGORITHM to ROBUST or ROBUST_STABLE
in conjunction to GEN_SCFMAN set to true.
The outline for the ROBUST pipeline is below:

- •

SCF converges when the DIIS error or RMS gradient
converges below the requested convergence threshold.
- •

The cutoff for the neglect of 2-electron integrals is set to $10^{-12}$
or a tighter user-specified value set using THRESH. Note that, by default,
THRESH = SCF_CONVERGENCE+4.
- •

The cutoff for the neglect of overlap integrals is set to $10^{-14}$ or a
tighter user-specified value set using S2THRESH to offset
any basis-set linear dependency problems.
- •

We define oscillatory behavior during the SCF procedure as
SCF_ROBUST_MIN_SIGN_CHANGES number of sign changes within a window of logarithms of
DIIS errors or RMS gradients.
- •

We define a plateau detection when the slopes of SCF_ROBUST_PLATEAU_WINDOWS windows of DIIS errors or RMS gradients
are less than SCF_ROBUST_SLOPE_THRESH.
- •

Throughout the pipeline, MAX_SCF_CYCLES corresponds to the maximum cycles allowed
for an SCF algorithm to run without any parameter changes.
- •

The pipeline starts with the DIIS algorithm. If a plateau or oscillatory behavior in the DIIS error is
detected after iteration #(2*SCF_ROBUST_WINDOW_SIZE+1), the incremental Fock algorithm,
if on, is switched off for good.
- •

At this point, if the DIIS error is less than 0.001, the algorithm is switched to ADIIS; otherwise,
DIIS is allowed to run for a further MAX_SCF_CYCLES iterations unless a plateau
or oscillatory trend is detected again at which point the algorithm switches to GDM.
For Q-Chem 7.0, if robust SCF is run with MPI+OMP parallelization, the switch to ADIIS is skipped.
- •

ADIIS is allowed to run for MAX_SCF_CYCLES iterations unless the DIIS error becomes smaller
than 0.001.
- •

DIIS is run again after ADIIS. The pipeline switches to GDM if a plateau or oscillatory trend is detected again after
iteration #(2*SCF_ROBUST_WINDOW_SIZE+1).
- •

GDM is allowed to run until convergence or maximum allowed number of iterations.

The ROBUST_STABLE pipeline performs a stability analysis on top of the ROBUST pipeline until a minimum is found.
Following the initial macroiteration run with ROBUST, only GDM is used in subsequent macroiterations
for stability analaysis.
The number of negative eigenvalues needs to decrease with each macroiteration as a necessary condition
for this pipeline to continue.

Below, we describe the internal *$rem* parameters of these robust pipelines.
The default values of these parameters are currently set to
experimental values and may not be optimal for all use cases;
so, the users are encouraged to share their settings with the Q-Chem Office,
if the defaults don’t yield convergence for their use cases.

SCF_ROBUST_WINDOW_SIZE

### `SCF_ROBUST_WINDOW_SIZE`

> **Controls the size of the window of logarithms of DIIS error or RMS gradients used for detecting oscillations or a plateau in robust SCF procedures.**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * n
>     * Customized.
> * **Recommendation**: None

SCF_ROBUST_MIN_SIGN_CHANGES

### `SCF_ROBUST_MIN_SIGN_CHANGES`

> **Controls the number of sign changes in a window of logarithms of DIIS error or RMS gradients used for detecting oscillations in robust SCF procedures.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * n
>     * Customized.
> * **Recommendation**: None

SCF_ROBUST_PLATEAU_WINDOWS

### `SCF_ROBUST_PLATEAU_WINDOWS`

> **Controls the number of windows of logarithms of DIIS error or RMS gradients used for detecting a plateau in robust SCF procedures.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * n
>     * Customized.
> * **Recommendation**: None

SCF_ROBUST_SLOPE_THRESH

### `SCF_ROBUST_SLOPE_THRESH`

> **Controls the slope threshold for a series of windows of logarithms of DIIS error or RMS gradients used for detecting a plateau in robust SCF procedures.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * n
>     * Customized to
>     * $10^{-n}$
>     * .
> * **Recommendation**: None
