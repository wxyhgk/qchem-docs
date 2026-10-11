---
title: "12.8.3 Job Control Variables for XPol"
---

## 12.8.3 Job Control Variables for XPol

(July 4, 2026)

XPol calculations are enabled by setting the *$rem* variable XPOL to TRUE.
The XPol method can be used in combination with Hartree-Fock theory
and with most density functionals, a notable exception being that XPol is not
yet implemented for meta-GGA functionals (Section [5.3](../ch05_dft/sect_XCfuncs.md)).
Combination of XPol with solvation models (Section [11.2](../ch11_env/topic_solvation.md)) or external
charges (*$external_charges*) is also not supported. Analytic gradients are
available when Mulliken, Löwdin, or CM5 embedding charges are used, but not yet
available for ChElPG embedding charges.

XPOL

### `XPOL`

> **Perform a self-consistent XPol calculation.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform an XPol calculation.
>     * FALSE
>     * Do not perform an XPol calculation.
> * **Recommendation**: NONE

Other XPol options are specified via keywords contained in the *$xpol* section.
These keywords are given below.

### `embed`

> **Specifies which type of electrostatic embedding will be used. INPUT SECTION: $xpol**
>
> * **Type**: `STRING`
> * **Default**: `Charges`
> * **Options**:
>     * None
>     * No embedding charges.
>     * Charges
>     * Atomic point charges (standard XPol method).
>     * Density
>     * Fragment densities (as in the FMO method; see Sec.
>     * 12.12
>     * )
> * **Recommendation**: The standard XPol method uses atomic point charges.

### `charges`

> **Specifies which type of atomic point charges to use. INPUT SECTION: $xpol**
>
> * **Type**: `STRING`
> * **Default**: `CM5`
> * **Options**:
>     * Mulliken
>     * Mulliken charges
>     * Lowdin
>     * Löwdin charges
>     * CHELPG
>     * ChElPG charges
>     * CM5
>     * CM5 charges
> * **Recommendation**: Problems with Mulliken charges in extended basis sets can lead to XPol convergence failure. Löwdin charges tend to be somewhat more stable, while ChElPG charges are quite robust and provide an accurate electrostatic embedding. However, ChElPG charges are more expensive to compute and they perform slightly worse than CM5 charges in systems with charged monomers. The CM5 charges are a cost-effective and slightly more accurate choice. For XSAPT calculations (Section 12.10 ), CM5 charges are recommended. However, CM5 charges are not yet available for AIFDEM jobs (Section 12.14 ) and in that case ChElPG charges are recommended.

### `print`

> **Specifies the level of output for the XPol code. INPUT SECTION: $xpol**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * Desired print level
> * **Recommendation**: Higher values print additional information

Especially in the context of SAPT(KS) calculations (see
Section [12.9](topic_sapt.md)) and XSAPT(KS) calculations (Section [12.10](sect_XSAPT.md)),
in which a Kohn-Sham description of the monomers is combined with
symmetry-adapted perturbation theory (SAPT), it is essentially that the
Kohn-Sham density functional exhibit correct asymptotic
behavior.[[761]](../bib_references/bib.md#bib794)
 Most standard density functionals do
*not* satisfy this criterion, but it can be imposed by using a
range-separated hybrid functional in which the range-separation parameter
$\omega$ is tuned so as to satisfy the ionization potential theorem of DFT,
namely, $\mbox{IE}(\omega)=-\epsilon_{\rm HOMO}(\omega)$. This condition
should be enforced separately on each monomer within an XPol calculation, which
requires that a different value of $\omega$ be used for each monomer. This
functionality is requested by setting the **DFT-LRC** option in the
*$xpol* section. (Note that no value needs to be set with this keyword; if it
is present in the *$xpol* section then this option is enabled.)

### `DFT-LRC`

> **Specifies whether monomer-specific range-separated hybrid functionals are to be used INPUT SECTION: $xpol**
>
> * **Type**: `None`
> * **Default**: `Not specified`
> * **Options**:
>     * If the keyword is present, this option is enabled.
> * **Recommendation**: Placing this keyword into the $xpol section indicates that monomer-specific values of $\omega$ (the range-separation parameter) are to be used, which then requires a $lrc_omega input section.

If **DFT-LRC** is specified, then a *$lrc_omega* input section is also
required. This input section simply consists of the values $\omega_{1},\omega_{2},\ldots$ for each monomer, listed one per line in the order that the
monomers appear in the *$molecule* section. These values have the same units
as the *$rem* variable OMEGA that is used in range-separated hybrid
functional calculations, namely, $\omega=$ OMEGA/1000 in atomic
units. See Section [12.10.3](subsec_AO-XSAPT(KS)+D.md) for an example of how the
**DFT-LRC** option and the *$lrc_omega* input section are used in the
context of the XSAPT(KS) method.
