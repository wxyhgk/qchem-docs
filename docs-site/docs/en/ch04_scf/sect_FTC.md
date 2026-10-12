---
title: "4.6.5 Fourier Transform Coulomb Method"
---

## 4.6.5 Fourier Transform Coulomb Method

(July 4, 2026)

The Coulomb part of the DFT calculations using ordinary Gaussian
representations can be sped up dramatically using plane waves as a secondary
basis set by replacing the most costly analytical electron repulsion integrals
with numerical integration techniques. The main advantages to keeping the
Gaussians as the primary basis set is that the diagonalization step is much
faster than using plane waves as the primary basis set, and all electron
calculations can be performed analytically.

The Fourier Transform Coulomb (FTC) technique[[423]](../bib_references/bib.md#bib431)
 is
precise and tunable and all results are practically identical with the
traditional analytical integral calculations. The FTC technique is at least
2–3 orders of magnitude more accurate then other popular plane wave based
methods using the same energy cutoff. It is also at least 2–3 orders of
magnitude more accurate than the density fitting (resolution-of-identity)
technique. Recently, an efficient way to implement the forces of the Coulomb
energy was introduced,[[425]](../bib_references/bib.md#bib433)
 and a new technique to localize
filtered core functions. Both of these features have been implemented within
**Q-Chem** and contribute to the efficiency of the method.

The FTC method achieves these spectacular results by replacing the analytical
integral calculations, whose computational costs scales as ${\cal{O}}({N^{4}})$ (where
$N$ is the number of basis function) with procedures that scale as only
${\cal{O}}({N^{2}})$. The asymptotic scaling of computational costs with system size is
linear versus the analytical integral evaluation which is quadratic. Research
at **Q-Chem** Inc. has yielded a new, general, and very efficient implementation
of the FTC method which work in tandem with the J-engine and the CFMM
(Continuous Fast Multipole Method) techniques.[[422]](../bib_references/bib.md#bib434)

In the current implementation the speed-ups arising from the FTC technique are
moderate when small or medium Pople basis sets are used. The reason is that the
J-matrix engine and CFMM techniques provide an already highly efficient
solution to the Coulomb problem. However, increasing the number of
polarization functions and, particularly, the number of diffuse functions
allows the FTC to come into its own and gives the most significant
improvements. For instance, using the 6-311G+(df,pd) basis set for a
medium-to-large size molecule is more affordable today then before. We found
also significant speed ups when non–Pople basis sets are used such as cc-pvTZ.
The FTC energy and gradients calculations are implemented to use up to $f$-type
basis functions.

### `FTC`

> **Controls the overall use of the FTC.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not use FTC in the Coulomb part
>     * `1`: Use FTC in the Coulomb part
> * **Recommendation**: Use FTC when bigger and/or diffuse basis sets are used.

### `FTC_SMALLMOL`

> **Controls whether or not the operator is evaluated on a large grid and stored in memory to speed up the calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Use a big pre-calculated array to speed up the FTC calculations
>     * `0`: Use this option to save some memory
> * **Recommendation**: Use the default if possible and use 0 (or buy some more memory) when needed.

### `FTC_CLASS_THRESH_ORDER`

> **Together with FTC_CLASS_THRESH_MULT , determines the cutoff threshold for included a shell-pair in the $dd$ class, i.e. , the class that is expanded in terms of plane waves.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: User specified
> * **Recommendation**: Use the default.

### `FTC_CLASS_THRESH_MULT`

> **Together with FTC_CLASS_THRESH_ORDER , determines the cutoff threshold for included a shell-pair in the $dd$ class, i.e. , the class that is expanded in terms of plane waves.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: User specified.
> * **Recommendation**: Use the default. If diffuse basis sets are used and the molecule is relatively big then tighter FTC classification threshold has to be used. According to our experiments using Pople-type diffuse basis sets, the default $5\times 10^{-5}$ value provides accurate result for an alanine5 molecule while $1\times 10^{-5}$ threshold value for alanine10 and $5\times 10^{-6}$ value for alanine15 has to be used.
