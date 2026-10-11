---
title: "12.6.4 Further Decomposition of the Frozen Energy"
---

## 12.6.4 Further Decomposition of the Frozen Energy

(July 4, 2026)

The frozen interaction energy in ALMO-EDA is defined as the energy difference
between the unrelaxed frozen (Heitler-London) wave function and the isolated
fragments. In other literature,[[1408]](../bib_references/bib.md#bib1467)
 this
interaction is often decomposed in a classical fashion:

<a id="eq:cls_decomp"></a>

$$
\Delta E_{\mathrm{frz}}=\Delta E_{\mathrm{elec}}^{\mathrm{cls}}+\Delta E_{\mathrm{Pauli}}^{\mathrm{cls}}, \tag{12.8}
$$

where the contribution from permanent electrostatics is defined as the Coulomb
interaction between isolated fragment charge distributions:

<a id="eq:cls_elec"></a>

$$
\Delta E_{\mathrm{elec}}^{\mathrm{cls}}=\sum_{A<B}\int_{r_{1}}\int_{r_{2}}\rho_{A}^{\mathrm{tot}}({\textbf{r}_{1}})\frac{1}{{\textbf{r}_{12}}}\rho_{B}^{\mathrm{tot}}({\textbf{r}_{2}})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2} \tag{12.9}
$$

and the remainder constitutes the Pauli (or exchange) term. Such a
decomposition (referred to as the classical decomposition below) is associated
with two issues: (i) the evaluation of permanent electrostatics makes use of
the “promolecule” state (whose density is the simple sum of monomer densities)
rather than a properly anti-symmetrized wave function; (ii) when
dispersion-corrected density functionals are used, the Pauli term contains
dispersion interaction and thus loses its original meaning.

Horn *et al.*[[595]](../bib_references/bib.md#bib619)
 proposed a new scheme to further decompose the frozen term into
contributions from permanent electrostatics (ELEC), Pauli repulsion (PAULI) and dispersion (DISP):

<a id="eq:new_decomp"></a>

$$
\Delta E_{\mathrm{frz}}=\Delta E_{\mathrm{elec}}+\Delta E_{\mathrm{Pauli}}+\Delta E_{\mathrm{disp}} \tag{12.10}
$$

This approach is compatible with the use of all kinds of density functionals
except double hybrids, and all three components of the FRZ term are computed
with the antisymmetrized frozen wave function. The key step of this method is
the orthogonal decomposition of the 1PDM associated with the frozen wave
function into contributions from individual fragments:
$\mathbf{P}_{\mathrm{frz}}=\sum_{A}\tilde{\mathbf{P}}_{A}$. This is achieved by
minimizing an objective function as follows:

<a id="eq:kep_obj"></a>

$$
\Omega=\sum_{A}E_{A}[\tilde{\mathbf{P}}_{A}]-E_{A}[\mathbf{P}_{A}] \tag{12.11}
$$

while interfragment orthogonality is enforced between fragment density matrices
$\tilde{\mathbf{P}}_{A}$; see Ref. [[595]](../bib_references/bib.md#bib619)
.

The ELEC term is then defined as the Coulomb interaction between distorted
fragment densities ($\tilde{\rho}_{A}(\mathbf{r})$):

<a id="eq:eda_elec"></a>

$$
\Delta E_{\mathrm{elec}}=\sum_{A<B}\int_{r_{1}}\int_{r_{2}}\tilde{\rho}_{A}^{\mathrm{tot}}({\textbf{r}_{1}})\frac{1}{{\textbf{r}_{12}}}\tilde{\rho}_{B}^{\mathrm{tot}}({\textbf{r}_{2}})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}. \tag{12.12}
$$

The DISP term is evaluated by subtracting the dispersion-free part of the total
exchange-correlation (XC) interaction, where an auxiliary “dispersion-free”
XC (DFXC) functional is used in company with the primary (target) XC functional:

<a id="eq:eda_disp"></a>

$$
\Delta E_{\mathrm{disp}}=\left(E_{\mathrm{xc}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}[\tilde{\mathbf{P}}_{A}]\right)-\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\tilde{\mathbf{P}}_{A}]\right). \tag{12.13}
$$

It has been suggested[[896]](../bib_references/bib.md#bib933)
 that HF is an appropriate DFXC for use with
dispersion-inclusive or dispersion-corrected hybrid functionals such as $\omega$B97M-V or B3LYP-D3, while
revPBE is appropriate for semi-local functionals such as B97M-V.

The remainder of the frozen interaction goes into the PAULI term, which
includes the net repulsive interaction given by Eq. ([12.11](#eq:kep_obj)) and the “dispersion-free” part of the XC interaction:

<a id="eq:eda_pauli"></a>

$$
\Delta E_{\mathrm{Pauli}}=\sum_{A}(E_{A}[\tilde{\mathbf{P}}_{A}]-E_{A}[\mathbf{P}_{A}])+\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\tilde{\mathbf{P}}_{A}]\right). \tag{12.14}
$$

The PAULI term and the ELEC term can also be combined together and reported as
the dispersion-free frozen (DFFRZ) term if desired.

In **Q-Chem**’s implementation of “EDA2”, the classical frozen decomposition and
the new scheme defined by Eqs. ([12.12](#eq:eda_elec))–([12.14](#eq:eda_pauli)) are both
computed by default. The classical ELEC term only depends on monomer
properties and the distances between fragments, therefore, it can be
particularly useful for scenarios such as force field development (as the
reference for permanent electrostatics). When the DISP term calculated by the
new scheme is available, a modified classical Pauli term[[893]](../bib_references/bib.md#bib927)
 is
also reported, which is simply defined as

<a id="Ch12.E15"></a>

$$
\Delta E_{\mathrm{Pauli}}^{\mathrm{mod}}=\Delta E_{\mathrm{Pauli}}^{\mathrm{cls}}-\Delta E_{\mathrm{disp}}\;. \tag{12.15}
$$

That is, the dispersion contribution is removed from the classical Pauli term
computed using its original definition. The overall decomposition of the frozen
energy with the classical scheme is given by

<a id="Ch12.E16"></a>

$$
\Delta E_{\mathrm{frz}}=\Delta E^{\mathrm{cls}}_{\mathrm{elec}}+\Delta E^{\mathrm{mod}}_{\mathrm{Pauli}}+\Delta E_{\mathrm{disp}}\;. \tag{12.16}
$$

Alternatively, this can also be achieved without performing the orthogonal
decomposition, by setting EDA_CLS_DISP to TRUE.
This also evaluates the DISP term via
Eq. ([12.13](#eq:eda_disp)) except that undistorted monomer densities
($\{\mathbf{P}_{A}\}$) are used instead of their distorted counterparts
($\{\tilde{\mathbf{P}}_{A}\}$):

<a id="Ch12.E17"></a>

$$
\Delta E_{\mathrm{disp}}=\left(E_{\mathrm{xc}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}[\mathbf{P}_{A}]\right)-\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{A}]\right). \tag{12.17}
$$

FRZ_ORTHO_DECOMP

### `FRZ_ORTHO_DECOMP`

> **Perform the decomposition of frozen interaction energy based on the orthogonal decomposition of the 1PDM associated with the frozen wave function.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE (automatically set to`
> * **Options**:
>     * FALSE
>     * Do not perform the orthogonal decomposition.
>     * TRUE
>     * Perform the frozen energy decomposition using orthogonal fragment densities.
> * **Recommendation**: Use default value automatically set by “EDA2”. Note that users are allowed to turn off the orthogonal decomposition by setting to $-1$ . Also, for calculations that involve ECPs, it is automatically set to FALSE since unreasonable results will be produced otherwise.

FRZ_ORTHO_DECOMP_CONV

### `FRZ_ORTHO_DECOMP_CONV`

> **Convergence criterion for the minimization problem that gives the orthogonal fragment densities.**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$
>     * $10^{-n}$
> * **Recommendation**: Use the default unless tighter convergence is preferred.

EDA_CLS_ELEC

### `EDA_CLS_ELEC`

> **Perform the classical decomposition of the frozen term.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE (automatically set to`
> * **Options**:
>     * FALSE
>     * Do not compute the classical ELEC and PAULI terms.
>     * TRUE
>     * Perform the classical decomposition.
> * **Recommendation**: TRUE

EDA_CLS_DISP

### `EDA_CLS_DISP`

> **Compute the DISP contribution without performing the orthogonal decomposition, which will then be subtracted from the classical PAULI term.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Use the DISP term computed with orthogonal decomposition (if available).
>     * TRUE
>     * Use the DISP term computed using undistorted monomer densities.
> * **Recommendation**: Set it to TRUE when orthogonal decomposition is not performed.

DISP_FREE_X

### `DISP_FREE_X`

> **Specify the employed “dispersion-free” exchange functional.**
>
> * **Type**: `STRING`
> * **Default**: `HF`
> * **Options**:
>     * Exchange functionals (
>     * e.g.
>     * revPBE) or exchange-correlation functionals (
>     * e.g.
>     * B3LYP)
>     * supported by
>     * Q-Chem
>     * .
> * **Recommendation**: HF is recommended for hybrid (primary) functionals ( e.g. $\omega$ B97X-V) and revPBE for semi-local ones ( e.g. B97M-V). Other reasonable options ( e.g. B3LYP for B3LYP-D3) can also be applied.

DISP_FREE_C

### `DISP_FREE_C`

> **Specify the employed “dispersion-free” correlation functional.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * Correlation functionals supported by
>     * Q-Chem
>     * .
> * **Recommendation**: Put the appropriate correlation functional paired with the chosen exchange functional ( e.g. put PBE if DISP_FREE_X is revPBE); put NONE if DISP_FREE_X is set to an exchange-correlation functional.
