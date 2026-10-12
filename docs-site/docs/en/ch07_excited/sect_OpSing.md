---
title: "7.7.3 Approximate Spin Purification"
---

## 7.7.3 Approximate Spin Purification

(July 4, 2026)

Singlet biradicals are an important special case, whose description within a single-determinant SCF formalism is typical
characterized by significant spin contamination, $\langle\hat{S}^{2}\rangle\approx 1$ (in atomic units), indicating an approximately
equal mixture of singlet ($\langle\hat{S}^{2}\rangle=0$) and triplet ($\langle\hat{S}^{2}\rangle=2$) wave functions. This is a result
of the fact that a proper description of two electrons in two half-filled orbitals requires a minimum of two determinants.
A simple means to correct for this is to use the approximate spin-purification
formula,[[1580]](../bib_references/bib.md#bib1643)

<a id="eq:OpSing"></a>

$$
E_{\text{OSS}}\approx 2E_{\text{BS}}-E_{\text{trip}}\;, \tag{7.78}
$$

which expresses the energy of the open-shell singlet state ($E_{\text{OSS}}$) in terms of the energy of the broken-symmetry
solution ($E_{\text{BS}}$, meaning the state with $\langle\hat{S}^{2}\rangle\approx 1$) and the triplet energy ($E_{\text{trip}}$).
This formula was originally suggested by Ziegler, Rauk, and Baerends,[[1580]](../bib_references/bib.md#bib1643)
 but was popularized by
Noodleman in application to metalloenzymes.

Evaluation of Eq. ([7.78](#eq:OpSing)) requires two separate SCF calculations and these can be performed together,
automatically, by specifying SPIN_PROJ = NOODLEMAN in the *$rem* section; see Example [7.7.2](ex_OpSing.md).
Analytic gradients have been implemented for this approximate spin-purification approach, which again requires
two separate SCF gradient computations. (Hessians are not available, however, even by finite-difference.)
For the specific case of open-shell singlets, the ROKS method that is discussed in Section [7.7.4](ex_ESROKS.md)
can be understood as a fully self-consistent or orbital-optimized version of the formula in
Eq. ([7.78](#eq:OpSing)),

 using a consistent set of orbitals for both terms in Eq. ([7.78](#eq:OpSing)).
In contrast, Noodleman’s approximate spin purification procedure performs two independent SCF
calculations with different orbitals in each.

### `SPIN_PROJ`

> **Controls whether approximate spin purification is performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Spin purification is not performed.
>     * `NOODLEMAN`: Spin purification is performed using Noodleman’s formula, Eq. ( 7.78 ).
> * **Recommendation**: Set to NOODLEMAN if spin purification is desired. Make sure that UNRESTRICTED is set to TRUE . Gradients are available but Hessians are not.
