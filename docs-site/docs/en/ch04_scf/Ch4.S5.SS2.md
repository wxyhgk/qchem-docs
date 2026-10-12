---
title: "4.5.2 Basic Convergence Control Options"
---

## 4.5.2 Basic Convergence Control Options

(July 4, 2026)

See also more detailed options in the following sections, and note that the SCF
convergence criterion and the integral threshold must be set in a compatible
manner, (this usually means THRESH should be set to at least 3 higher
than SCF_CONVERGENCE).

### `MAX_SCF_CYCLES`

> **Controls the maximum number of SCF iterations permitted.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: $n>0$ User-selected.
> * **Recommendation**: Increase for slowly converging systems such as those containing transition metals.

### `SCF_ALGORITHM`

> **Algorithm used for converging the SCF.**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * `DIIS`: Pulay DIIS.
>     * `ROOTHAAN`: Roothaan repeated diagonalization
>     * `DM`: Direct minimizer.
>     * `L_BFGS`: Limited memory BFGS algorithm with line search
>     * `GDM`: Geometric Direct Minimization
>     * `GDM_LS`: Like GDM, but employs a line search in L-BFGS
>     * `GDM_QLS`: Like
>     * `GDM_LS`: , but uses a quadratic line search in L-BFGS
>     * `RCA`: Relaxed-constraint algorithm
>     * `ADIIS`: The combination of the ARH energy function and DIIS by Hu and Yang
>     * `NEWTON_CG`: Solve $\mathbf{Hd}=-\mathbf{g}$ using conjugated gradients to determine Newton steps (see also NEWTON_MINRES , which uses the MINRES algorithm to solve the linear equation)
>     * `DIIS_DM`: Uses DIIS initially, switching to direct minimizer for later iterations (See THRESH_DIIS_SWITCH , MAX_DIIS_CYCLES )
>     * `DIIS_GDM`: Use DIIS and then later switch to geometric direct minimization (See THRESH_DIIS_SWITCH , MAX_DIIS_CYCLES )
>     * `LS_DIIS`: Uses level-shifting initially, switching to DIIS for later iterations (See THRESH_LS_SWITCH , MAX_LS_CYCLES )
>     * `RCA_DIIS`: Use RCA initially, switching to DIIS for later iterations (See THRESH_RCA_SWITCH and MAX_RCA_CYCLES )
>     * `ADIIS_DIIS`: Use ADIIS initially, switching to DIIS for later iterations (See THRESH_ADIIS_SWITCH and MAX_ADIIS_CYCLES )
>     * `ROBUST`: New black-box workflow for robust convergence featuring tighter thresholds and a combination of algorithms (DIIS, ADIIS, and GDM).
>     * `ROBUST_STABLE`: Does stability analysis on top of the ROBUST procedure.
> * **Recommendation**: Use DIIS unless performing a restricted open-shell calculation, in which case GDM is recommended. If DIIS fails to find a reasonable approximate solution in the initial iterations, RCA_DIIS or ADIIS_DIIS are the recommended fallback options. If DIIS approaches the correct solution but fails to finally converge, DIIS_GDM is the recommended fallback. For systems with a small HOMO/LUMO gap, and where, DIIS fails to converge, LS_DIIS may help. If nothing works, try ROBUST or ROBUST_STABLE . Please report failed SCF convergence to the Q-Chem office, in order to help refine these workflows.

**Note**:
For usage of the ROBUST or ROBUST_STABLE algorithms, see Section [4.5.13](sub_scf_robust_pipelines.md).
For the Squared Gradient Minimization (SGM) and related algorithms, see Section [4.5.15](sect_SGM-SCF.md).

### `SCF_CONVERGENCE`

> **SCF is considered converged when the wave function error is $<10^{-\mathrm{SCF\_CONVERGENCE}}$ . Adjust the value of THRESH at the same time.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$
> * **Recommendation**: Tighter criteria for geometry optimization and vibration analysis. Larger values provide more significant figures, at greater computational cost.

In some cases besides the total SCF energy, one needs its separate energy
components, like kinetic energy, exchange energy, correlation energy, *etc.*
The values of these components are printed at each SCF cycle if one specifies
SCF_PRINT = 1 in the input.
