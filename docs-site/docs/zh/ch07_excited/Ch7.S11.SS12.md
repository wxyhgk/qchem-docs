---
title: "7.11.12 Job Control Options for RASCI2"
---

## 7.11.12 Job Control Options for RASCI2

(July 4, 2026)

At present the RASCI1 and RASCI2 implementations employ different keywords
(which will be reconciled in a future version). This subsection applies to
RASCI2 (even and odd electron systems, determinant-driven algorithm using the
resolution of the identity approximation).

The use of the RAS-CI2 methodology is controlled by setting the
CORRELATION = RASCI2 and EXCHANGE = HF.
The minimum input also requires specifying the desired (non-zero) value for
RAS_N_ROOTS, and the number of active occupied and virtual orbital
comprising the “active” RAS2 space. RASCI2 calculations also require
specification of an auxiliary basis via AUX_BASIS.

RAS_N_ROOTS

### `RAS_N_ROOTS`

> **Sets the number of RAS-CI roots to be computed.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * $n>0$
>     * Compute
>     * $n$
>     * RAS-CI states
> * **Recommendation**: None. Only works with RASCI2

RAS_ACT_OCC

### `RAS_ACT_OCC`

> **Sets the number of occupied orbitals to enter the RAS active space.**
>
> * **Type**: `Integer`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * user defined integer
> * **Recommendation**: None. Only works with RASCI2

RAS_ACT_VIR

### `RAS_ACT_VIR`

> **Sets the number of virtual orbitals to enter the RAS active space.**
>
> * **Type**: `Integer`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * user defined integer
> * **Recommendation**: None. Only works with RASCI2.

RAS_ACT_DIFF

### `RAS_ACT_DIFF`

> **Sets the number of $\alpha$ versus $\beta$ electrons and therefore controls the level of excitations used in calculations.**
>
> * **Type**: `Integer`
> * **Default**: `None`
> * **Options**:
>     * 1
>     * odd number of electrons or cations
>     * 0
>     * even number of electrons
>     * $-1$
>     * anions
>     * $n$
>     * $n<-99$
>     * triggers RAS2-SF at DDCI level of excitations
>     * $n=-451$
>     * and
>     * $n=-452$
>     * triggers restart mechanism that restores the last best guess for each state to the number of states requested
> * **Recommendation**: Set to 0 would be appropriate for most singlet systems. Only works with RASCI2.

Note that other *$rem* variables that can be used to control the evaluation of
RASCI2 calculations are MAX_CIS_CYCLES for the maximum number of Davidson
iterations, and N_FROZEN_CORE and N_FROZEN_VIRTUAL to
exclude core and/or virtual orbitals from the RASCI2 calculation. Please see
the sample inputs below for more details.

RAS_CALC_SOC

### `RAS_CALC_SOC`

> **Controls whether to calculate the SOC constants for RAS2 jobs only.**
>
> * **Type**: `Integer/Logical`
> * **Default**: `False`
> * **Options**:
>     * False
>     * Do not perform the SOC calculation.
>     * True
>     * Perform the SOC calculation.
> * **Recommendation**: This $rem variable is used to control the spin-orbit coupling (SOC) analysis section.

Note: For SOC calculations, RASCI2 method by default computes both the
one-electron and two-electron mean-field contributions. SOC-NTO analyses can be
triggered after the SOC analysis. Two additional parameters,
MOLDEN_FORMAT and NTO_PAIRS, are needed for the NTO
analysis. Details of the two variables are provided in the following *$rem*
sections:

MOLDEN_FORMAT

### `MOLDEN_FORMAT`

> **Sets the output format of NTOs in RASCI2 SOC analysis to MolDen format.**
>
> * **Type**: `Logical`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Append
>     * MolDen
>     * input file at the end of the
>     * Q-Chem
>     * output file.
> * **Recommendation**: Currently, SOC-NTO analysis in RASCI2 only works with MolDen . Other visualization tools are not supported at the moment. Please see the Visualizing Orbitals Using MolDen section for more information.

NTO_PAIRS

### `NTO_PAIRS`

> **Controls the writing of hole/particle NTO pairs for SOC transitions calculated within the RASCI2 SOC analysis section.**
>
> * **Type**: `Integer`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * Write
>     * $N$
>     * NTO pairs per SOC transition.
> * **Recommendation**: If activated ( $N>0$ ), a minimum of two NTO pairs will be printed for each transition. Increase the value of $N$ if additional NTOs are desired. See Section 7.13.3 for information on visualizing NTOs.

RAS_PCM_INIT

### `RAS_PCM_INIT`

> **Triggers state-specific PCM solvation within RAS-SF.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * include solvation
> * **Recommendation**: This triggers the nonequilibrium version of state-specific solvation. Additional keywords are necessary for the equilibrium version.
