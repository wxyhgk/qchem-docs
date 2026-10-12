---
title: "11.7.2 FDE-Man"
---

## 11.7.2 FDE-Man

(July 4, 2026)

Several FDET-based methods are available in the FDE-Man module of **Q-Chem**.
The FDE-Man job control is accomplished in two sections, *$rem* and *$fde*.

The fragments are specified via the fragment descriptors (see
Section [12](../ch12_frag/chap_frag.md)) in the *$molecule* section, whereas the first fragment
corresponds to the embedded species (A), the second fragment represents
the environment (B).

**Note: 

The current implementation allows only for closed shell fragments.
**

### `FDE`

> **Turns density embedding on.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * `True`: Perform an FDET calculation.
>     * `False`: Don’t perform FDET calculation.
> * **Recommendation**: Set the $rem variable to TRUE to start a FDET calculation.

Enabling FDE-Man, the specification of the embedding method and other job control
parameters (thresholds, max. iterations *etc.*) should be set in the *$rem*
section.

### `METHOD`

> **Determines which FDET-based method should be used for the embedded wave function if FDE = TRUE .**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`: Use = NAME , where NAME is either HF for Hartree-Fock theory or else one of the DFT methods listed in Section 5.3.5 .
> * **Recommendation**: None

Other DFT functionals can also be requested with the EXCHANGE and CORRELATION keywords as described
in Section [5.4](../ch05_dft/sect_DFT_METHOD.md).

**Note: 

The current implementation is restricted to mean-field methods that are solved with the SCFMAN module.
**

The standard capabilities to use customized basis sets are also possible with the FDE-Man module.

## 11.7.2.1 FDE-ADC

FDE-ADC[[1121]](../bib_references/bib.md#bib1168)
 is a density embedding method based on the
combination of the Algebraic Diagrammatic Construction scheme for the
polarization propagator (ADC, Section [7.10](../ch07_excited/sect_exadc.md)) and Frozen-Density
Embedding Theory (FDET).
In this particular variant, the subsystem A is represented by a wave function
whereas subsystem B is described by a density. The FDE-ADC method uses the
linearized FDET approximation.[[1539]](../bib_references/bib.md#bib1603)

Similar to the other methods, the ADC specifications have to be done inside the
*$rem* section, as shown below.

### `METHOD`

> **Determines which FDET-based method should be used if FDE = TRUE .**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `adc(2)`: Perform an FDE-ADC(2)-s calculation.
>     * `adc(2)-x`: Perform an FDE-ADC(2)-x calculation.
>     * `adc(3)`: Perform an FDE-ADC(3) calculation (potential constructed with MP(2) density).
>     * `cvs-adc(2)`: Perform an FDE-ADC(2)-s calculation of core excitations.
>     * `cvs-adc(2)-x`: Perform an FDE-ADC(2)-x calculation of core excitations.
>     * `cvs-adc(3)`: Perform an FDE-ADC(3) calculation of core excitations.
> * **Recommendation**: None

FDE-ADC also supports the excited state analysis
(STATE_ANALYSIS) carried out by the **libwfa** module.
