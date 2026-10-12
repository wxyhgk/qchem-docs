---
title: "4.3.3 Additional Options"
---

## 4.3.3 Additional Options

(July 4, 2026)

Listed below are a number of useful options to customize an SCF
calculation. This is only a short summary of the function of these *$rem*
variables. A full list of all SCF-related variables is provided in Appendix [B](../app_b_quickref/app_quick_ref.md).
Several important sub-topics are discussed separately, including ${\cal{O}}({N})$ methods for large molecules
(Section [4.6](sec_O_N.md)), customizing the initial guess (Section [4.4](sect_initialguess.md)), and converging
the SCF calculation (Section [4.5](sect_convergence.md)).

### `INTEGRALS_BUFFER`

> **Controls the size of in-core integral storage buffer.**
>
> * **Type**: `INTEGER`
> * **Default**: `15`
> * **Options**:
>     * `User defined size.`
> * **Recommendation**: Use the default, or consult your systems administrator for hardware limits.

### `DIRECT_SCF`

> **Controls direct SCF.**
>
> * **Type**: `LOGICAL`
> * **Default**: `Determined by program.`
> * **Options**:
>     * `TRUE`: Forces direct SCF.
>     * `FALSE`: Do not use direct SCF.
> * **Recommendation**: Use the default; direct SCF switches off in-core integrals.

### `METECO`

> **Sets the threshold criteria for discarding shell-pairs.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `1`: Discard shell-pairs four orders of magnitude below machine precision.
>     * `2`: Discard shell-pairs below 10 ${}^{-\mathrm{THRESH}}$ .
> * **Recommendation**: Use the default.

### `S2THRESH`

> **Cutoff for neglect of overlap integrals, defined via a two-electron shell-pair threshold of $10^{-\mathrm{S2THRESH}}$ ( $\leq 16$ ).**
>
> * **Type**: `INTEGER`
> * **Default**: `Same as`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$ .
> * **Recommendation**: Increase the value of if the program finds negative eigenvalues for the overlap matrix.

### `THRESH`

> **Cutoff for neglect of two electron integrals. $10^{-\mathrm{THRESH}}$ ( $\leq 16$ ).**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$ .
> * **Recommendation**: The value should satisfy $\geq$ 3 + SCF_CONVERGENCE , although = 4 + SCF_CONVERGENCE is the default (in most cases) since Q-Chem v. 6.0. See Ref. 479 Gray M., Bowling P. E., Herbert J. M. J. Phys. Chem. A (2024) , 128 , pp. 7739 . Link for recommended values of in the presence of diffuse basis functions, where tighter thresholds are often required and too-loose thresholds may lead to slower convergence or convergence failure.

### `STABILITY_ANALYSIS`

> **Performs stability analysis for a HF or DFT solution.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Perform stability analysis.
>     * `FALSE`: Do not perform stability analysis.
> * **Recommendation**: Set to TRUE when a HF or DFT solution is suspected to be unstable.

### `SCF_PRINT`

> **Controls level of output from SCF procedure to Q-Chem output file.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Minimal, concise, useful and necessary output.
>     * `1`: Level 0 plus component breakdown of SCF electronic energy.
>     * `2`: Level 1 plus density, Fock and MO matrices on each cycle.
>     * `3`: Level 2 plus two-electron Fock matrix components (Coulomb, HF exchange , orbital kinetic energies, and DFT exchange-correlation matrices) on each cycle.
> * **Recommendation**: Proceed with care; can result in extremely large output files at level 2 or higher. Output of all information is only available in scfman ( GEN_SCFMAN = FALSE). If GEN_SCFMAN is set to TRUE and > 1, only level 1 plus MO matrices are available in the output. These levels are primarily for program debugging.

### `SCF_FINAL_PRINT`

> **Controls level of output from SCF procedure to Q-Chem output file at the end of the SCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No extra print out.
>     * `1`: Orbital energies and break-down of SCF energy.
>     * `2`: Level 1 plus MOs and density matrices.
>     * `3`: Level 2 plus Fock matrix.
> * **Recommendation**: The break-down of energies is often useful (level 1).
