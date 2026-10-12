---
title: "6.8.2 BW-s2 Job Control"
---

## 6.8.2 BW-s2 Job Control

(July 4, 2026)

The BW-s2 approach has been implemented with the resolution-of-the-identity approximation
and is invoked with METHOD = RIBWS2.
The BW-s2 equation is iterative much like BW2, and keywords that give more
precise control over the self-consistent determination of the BW-s2 energy are
housed within a separate *$bws2* section.
Finally, the underlying algorithm that is used to solve the BW-s2 equation
can be used to solve for other forms of the correlation energy
such as MP2, BW2, size-extensive xBW2 (which is not size-consistent), or
second-order Bethe-Goldstone (BGE2)/independent electron pair approximation (IEPA).
While these methods are available for academic purposes, it is
advised to only use the BW2, xBW2, and BGE2/IEPA codes
for comparison as the first two are not size-consistent and the latter is
not orbital invariant. For MP2 calculations, the standard RI-MP2 code should be used.

### `METHOD`

> **Defines the correlation energy expression to be used. INPUT SECTION: $bws2**
>
> * **Type**: `STRING`
> * **Default**: `BWS2`
> * **Options**:
>     * BWS2, BW2, xBW2, BGE2, IEPA, or MP2
> * **Recommendation**: BW-s2 is the recommended method, but if comparisons with non-size-consistent methods like BW2 or xBW2 or non-orbital-invariant methods like BGE2/IEPA are desired, those options are available.

### `ALPHA`

> **Controls the extent of BW-s2( $\alpha$ ) regularization. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$: where $n/1000$ is the value of $\alpha$ .
> * **Recommendation**: The default is set to the original BW-s2 theory where $\alpha=1$ (corresponding to $n=1000$ ) is exact for a two-electron, two-orbital problem. For general applications $\alpha=4$ ( $n=4000$ ) is a broadly successful choice. Other values can be set based on the chemical problem at hand.

### `ENERGY_CONVERGENCE`

> **Defines the convergence threshold for the correlation energy. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `$n$`
> * **Options**:
>     * $n$: where the convergence threshold is set to $10^{-n}$
> * **Recommendation**: Use the default unless the cost of the calculation becomes prohibitive, then consider reducing to a slightly lower value.

### `AMPLITUDE_CONVERGENCE`

> **Defines the convergence threshold for the magnitude of the amplitude equation residual. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$: where the convergence threshold is set to $10^{-n}$
> * **Recommendation**: Use the default for small to medium sized molecules. Large molecules may require looser criteria.

### `MAX_CYCLES`

> **Defines maximum number of iterations to be used in determining the correlation energy. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `$n$`
> * **Options**:
>     * $n>0$
> * **Recommendation**: Use the default unless convergence is particularly slow, then increase the number of iterations accordingly.

### `PARAM_GRADIENT`

> **Controls whether or not to compute the derivative of the energy with respect to $\alpha$ . INPUT SECTION: $bws2**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Computes the iterative and non-iterative parameter gradient.
>     * `FALSE`: Does not compute the parameter gradient.
> * **Recommendation**: If required, set to TRUE.

???+ example "Example 6.23: Example of RI-BW-s2 on an acetylene pyridine complex"
    ```qchem
    $molecule
    0 1
    N   -0.083032490   0.000714589   1.055199987
    C   -0.202853764  -1.141725850   0.364933690
    H   -0.098485626  -2.055097952   0.937432624
    C   -0.446781438  -1.191763671  -1.004512261
    H   -0.533649208  -2.145855109  -1.504171553
    C   -0.574682087   0.003439534  -1.704309480
    H   -0.763683910   0.004480103  -2.768726700
    C   -0.453456753   1.197242545  -1.000916473
    H   -0.545630798   2.152272643  -1.497795085
    C   -0.209311108   1.144507590   0.368367296
    H   -0.110167072   2.056697259   0.943573961
    C    0.471836022  -0.006058187   5.541718960
    H    0.587246066  -0.005483995   6.596732782
    C    0.339766259  -0.006607922   4.335471660
    H    0.221618143  -0.006345494   3.270966186
    $end
    
    $rem
    method      ribws2
    basis       aug-cc-pvdz
    aux_basis   rimp2-aug-cc-pvdz
    scf_convergence 8
    thresh      14
    integral_symmetry   false
    $end
    
    ! METHOD keyword is not required for BW-s2
    ! MAX_CYCLES keyword is manually set to the default here
    $bws2
    alpha       400
    max_cycles  50
    $end
    ```
