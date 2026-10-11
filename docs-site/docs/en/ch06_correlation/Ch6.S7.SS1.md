---
title: "6.7.1 Overview"
---

## 6.7.1 Overview

(July 4, 2026)

MP2(attenuator, basis) approximates MP2 by splitting the Coulomb operator in
two pieces and preserving only short-range two-electron interactions, akin to
the CASE approximation,[[350]](../bib_references/bib.md#bib354)
 but without
modification of the underlying SCF calculation. While MP2 is a comparatively
efficient method for estimating the correlation energy, it converges slowly
with basis set size — and, even in the complete basis limit, contains
fundamentally inaccurate physics for long-range interactions. Basis set
superposition error and the MP2-level treatment of long-range interactions both
typically artificially increase correlation energies for non-covalent
interactions. Attenuated MP2 improves upon MP2 for inter- and intramolecular
interactions, with significantly better performance for relative and binding
energies of non-covalent complexes, frequently outperforming complete basis set
estimates of MP2.[[466]](../bib_references/bib.md#bib478)

Attenuated MP2, denoted MP2(attenuator, basis) is implemented in **Q-Chem** based
on the complementary terf function, below:

<a id="Ch6.E32"></a>

$$
\rm{s}(r)=\rm{terfc}(r,r_{0})=\frac{1}{2}\left\{\rm{erfc}\left[\omega(r-r_{0})\right]+\rm{erfc}\left[\omega(r+r_{0})\right]\right\} \tag{6.32}
$$

By choosing the terfc short-range operator, we optimally preserve the
short-range behavior of the Coulomb operator while smoothly and rapidly
switching off around the distance $r_{0}$. Since this directly addresses basis
set superposition error, parameterization must be done for specific basis sets.
This has been performed for the basis sets, aug-cc-pVDZ[[466]](../bib_references/bib.md#bib478)
 and
aug-cc-pVTZ.[[465]](../bib_references/bib.md#bib479)
 Other basis sets are not recommended for
general use until further testing has been done.

Energies and gradients are functional with and without the resolution of the
identity approximation using correlation keywords ATTMP2 and
ATTRIMP2.

???+ example "Example 6.21: Example of RI-MP2(terfc, aug-cc-pVDZ) energy evaluation"
    ```qchem
    $molecule
       0 1
       O    -1.551007   -0.114520    0.000000
       H    -1.934259    0.762503    0.000000
       H    -0.599677    0.040712    0.000000
    $end
    
    $rem
       METHOD          attrimp2
       BASIS           aug-cc-pvdz
       AUX_BASIS       rimp2-aug-cc-pvdz
    $end
    ```

???+ example "Example 6.22: Example of MP2(terfc, aug-cc-pVTZ) geometry optimization"
    ```qchem
    $molecule
       0 1
       H    0.0   0.0   0.0
       H    0.0   0.0   0.9
    $end
    
    $rem
       JOBTYPE         opt
       METHOD          attmp2
       BASIS           aug-cc-pvtz
    $end
    ```
