---
title: "5.12.1 Density-Corrected DFT"
---

## 5.12.1 Density-Corrected DFT

(July 4, 2026)

It is well known that self-interaction error (SIE) in DFT leads to over-delocalization of unpaired spins in open-shell molecules.[[262]](../bib_references/bib.md#bib263)

This has a variety of deleterious effects, including overstabilization of three-center, two-electron “hemibonds”,[[1145]](../bib_references/bib.md#bib1195)

fractional charges in well-separated chemical moieties (*i.e.*, upon dissociation),[[1553]](../bib_references/bib.md#bib1607)

and too-low reaction barriers, the latter of which was largely the motivation for the introduction of hybrid density
functionals.[[866]](../bib_references/bib.md#bib901)
 Although various *ad hoc* self-interaction correction schemes have been introduced
over the years, none of them is entirely satisfactory.[[630]](../bib_references/bib.md#bib653)

Density-corrected (DC-)DFT[[1412]](../bib_references/bib.md#bib1472)
 represents a revival of an old
idea[[1017]](../bib_references/bib.md#bib1058)
 to avoid SIE by evaluating a DFT functional non-self-consistently using self-consistent Hartree-Fock density,
which is SIE-free. Self-consistent iterations at the DFT level are avoided as this would re-introduce SIE into the density. If $E_{\text{DFT}}[\rho]$
represents the user’s chosen density functional and $E_{\text{HF}}[\rho]$ represents the Hartree-Fock functional, then the DC-DFT energy functional
is[[1143]](../bib_references/bib.md#bib1197)

<a id="Ch5.E75"></a>

$$
E_{\text{DC-DFT}}[\rho]=E_{\text{DFT}}\Big{[}\operatorname*{arg\,min}_{\rho}\big{(}E_{\text{HF}}[\rho]\big{)}\Big{]} \tag{5.75}
$$

DC-DFT affords barrier heights that are comparable in accuracy to those obtained with hybrid functionals, even if $E_{\text{DFT}}[\rho]$ is a semilocal
functional.[[629]](../bib_references/bib.md#bib652)
 This does not really reduce the cost of hybrid DFT calculations since the Hartree-Fock
calculation must be iterated to self-consistency, nevertheless DC-DFT may serve as a useful diagnostic tool. If the DC-DFT result with a given
functional is qualitatively different than the self-consistent DFT result with the same functional, then density-driven SIE may be affecting the results.
This diagnostic capacity has been used, for example, to detect unrealistic delocalization of polaron (spin) defects in metal oxides.[[1144]](../bib_references/bib.md#bib1196)

Users of **Q-Chem**’s implementation of DC-DFT are asked to cite Ref. [[1144]](../bib_references/bib.md#bib1196)
.
Analytic energy gradients for DC-DFT are available,[[1144]](../bib_references/bib.md#bib1196)
 but because the
functional $E_{\text{DC-DFT}}$ is not iterated to self-consistency evaluation of the gradient $dE_{\text{DC-DFT}}/dx$ requires solution
of coupled-perturbed ($Z$-vector) equations,[[1399]](../bib_references/bib.md#bib1459)
 which makes the gradient somewhat more expensive
than a traditional DFT gradient.

**Note: 

At present, the coupled-perturbed equtions for DC-DFT are solved in serial, meaning that while the SCF iterations are parallelized
the $Z$-vector iterations are not.
**

To perform a DC-DFT calculation, set use METHOD in the *$rem* section to select the functional of choice, and also set
DC_DFT = TRUE. Note that because $E_{\text{DFT}}[\rho]$ is never diagonalized, any subsequent properties that are
computed at the end of the SCF procedure are based on the Hartree-Fock density. This includes one-particle energy levels, Mulliken charges,
multipole moments, etc.

DC_DFT

### `DC_DFT`

> **Controls whether to use DC-DFT.**
>
> * **Type**: `Boolean`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not do DC-DFT.
>     * TRUE
>     * Iterate the density to self-consistency at the Hartree-Fock level and then perform
>     * evaluate
>     * $E_{\text{DFT}}[\rho_{\text{HF}}]$
>     * using the functional specified with
>     * METHOD
>     * .
> * **Recommendation**: Use if desired. Analytic gradients are available but are a serial bottleneck in the present implementation.
