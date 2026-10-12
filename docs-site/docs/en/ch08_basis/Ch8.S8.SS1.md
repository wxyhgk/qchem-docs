---
title: "8.8.1 Overview"
---

## 8.8.1 Overview

(July 4, 2026)

While atomic orbital standard basis sets are used to expand one-electron functions such
as molecular orbitals, *auxiliary basis sets* are also used in many **Q-Chem** jobs to
efficiently approximate products of one-electron functions, such as arise in electron
correlation methods.

For a molecule of fixed size, increasing the number of basis functions
*per atom*, $n$, leads to ${\cal{O}}({n^{4}})$ growth in the number of significant
four-center two-electron integrals, since the number of non-negligible
product charge distributions, $|\mu\nu\rangle$, grows as ${\cal{O}}({n^{2}})$. As a result,
the use of large (high-quality) basis expansions is computationally costly.
Perhaps the most practical way around this “basis set quality” bottleneck is
the use of auxiliary basis expansions.[[387]](../bib_references/bib.md#bib395)

The ability to use auxiliary
basis sets to accelerate a variety of electron correlation methods, including
both energies and analytical gradients, is a major feature of **Q-Chem**.

The auxiliary basis $\{|K\rangle\}$ is used to approximate products of Gaussian
basis functions:

<a id="Ch8.E2"></a>

$$
|\mu\nu\rangle\approx|\widetilde{\mu\nu}\rangle=\sum_{K}|K\rangle C_{\mu\nu}^{K} \tag{8.2}
$$

Auxiliary basis expansions were introduced long ago, and are now widely
recognized as an effective and powerful approach, which is sometimes
synonymously called resolution of the identity (RI) or density fitting (DF).
When using auxiliary basis expansions, the rate of growth of computational cost
of large-scale electronic structure calculations with $n$ is reduced to
approximately $n^{3}$.

If $n$ is fixed and molecule size increases, auxiliary basis expansions reduce
the pre-factor associated with the computation, while not altering the scaling.
The important point is that the pre-factor can be reduced by 5 or 10 times or
more. Such large speedups are possible because the number of auxiliary
functions required to obtain reasonable accuracy, $X$, has been shown to be
only about 3 or 4 times larger than $N$.

The auxiliary basis expansion coefficients, $\mathbf{C}$, are determined by
minimizing the deviation between the fitted distribution and the actual
distribution, $\langle\mu\nu-\widetilde{\mu\nu}|{\mu\nu-\widetilde{\mu\nu}}\rangle$, which leads to the following set of linear equations:

<a id="Ch8.E3"></a>

$$
\sum_{L}{\left\langle{K\left|L\right.}\right\rangle}C_{\mu\nu}^{L}=\left\langle{K\left|{\mu\nu}\right.}\right\rangle \tag{8.3}
$$

Evidently solution of the fit equations requires only two- and three-center
integrals, and as a result the (four-center) two-electron integrals can be
approximated as the following optimal expression for a given choice of
auxiliary basis set:

<a id="eq:riapprox"></a>

$$
\langle\mu\nu|\lambda\sigma\rangle\approx\langle\widetilde{\mu\nu}|\widetilde{\lambda\sigma}\rangle=\sum_{K,L}C_{\mu\nu}^{L}\langle L|K\rangle C_{\lambda\sigma}^{K} \tag{8.4}
$$

In the limit where the auxiliary basis is complete (*i.e.* all products of AOs
are included), the fitting procedure described above will be exact. However,
the auxiliary basis is invariably incomplete (as mentioned above,
$X\approx 3N)$ because this is essential for obtaining increased computational
efficiency.

More details on **Q-Chem**’s use of RI methods is given in
Section [6.6](../ch06_correlation/topic_rimp2.md) on RI-MP2 and related methods,
Section [6.19](../ch06_correlation/sect_pairing.md) on pairing methods, Section [6.12.10](../ch06_correlation/topic_ricc.md) on
coupled cluster methods, Section [4.6.6](../ch04_scf/sect_ri-DFT.md) on DFT methods, and
Section [7.11](../ch07_excited/topic_rasi.md) on restricted active space methods. In the remainder
of this section we focus on documenting the input associated with the
auxiliary basis itself.

**Q-Chem** contains a variety of built-in auxiliary basis sets, that can be
specified by the *$rem* keyword AUX_BASIS. These auxiliary basis
sets are listed in Table [8.9](#tab:auxbasis_corr) and specified in the *$rem* input section
by means of the job control variables that are listed below. Note that in addition to the
built-in auxiliary basis sets (Table [8.9](#tab:auxbasis_corr)), it is also possible to enter user-defined
auxiliary basis sets using an *$aux_basis* (or *$aux_basis_j*, *$aux_basis_k*, *$aux_basis_corr*)
input section, whose syntax generally follows
the *$basis* input section documented above in Section [8.4](sect_userbasis.md).

### `AUX_BASIS`

> **Sets the auxiliary basis set to be used**
>
> * **Type**: `STRING`
> * **Default**: `No default auxiliary basis set`
> * **Options**:
>     * `General, Gen`: User-defined. As for BASIS
>     * `Symbol`: Use standard auxiliary basis sets as in the table below
>     * `Mixed`: Use a combination of different basis sets
> * **Recommendation**: Consult literature and Basis Set Exchange to aid your selection.

### `AUX_BASIS_J`

> **Sets the auxiliary basis set for RI-J to be used or invokes RI-J**
>
> * **Type**: `STRING`
> * **Default**: `No default auxiliary basis set`
> * **Options**:
>     * `General, Gen`: User-defined. As for BASIS
>     * `Symbol`: Use standard auxiliary basis sets as in the table below
>     * `Mixed`: Use a combination of different basis sets
> * **Recommendation**: Consult literature and Basis Set Exchange to aid your selection.

### `AUX_BASIS_K`

> **Sets the auxiliary basis set for RI-K or occ-RI-K to be used or invokes occ-RI-K**
>
> * **Type**: `STRING`
> * **Default**: `No default auxiliary basis set`
> * **Options**:
>     * `General, Gen`: User-defined. As for BASIS
>     * `Symbol`: Use standard auxiliary basis sets as in the table below
>     * `Mixed`: Use a combination of different basis sets
> * **Recommendation**: Consult literature and Basis Set Exchange to aid your selection.

### `AUX_BASIS_CORR`

> **Sets the auxiliary basis set for RI-MP2 to be used or invokes RI-MP2 in case of double-hybrid DFT or MP2**
>
> * **Type**: `STRING`
> * **Default**: `No default auxiliary basis set`
> * **Options**:
>     * `General, Gen`: User-defined. As for BASIS
>     * `Symbol`: Use standard auxiliary basis sets as in the table below
>     * `Mixed`: Use a combination of different basis sets
> * **Recommendation**: Consult literature and Basis Set Exchange to aid your selection.

| Symbolic Name | Atoms Supported |
| --- | --- |
| RIJ-def2-XX ${}^{a}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIJK-def2-XX ${}^{a}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-XX ${}^{b}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-ma-XX ${}^{c}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-ha-XX ${}^{c}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-VDZ ${}^{d}$ | H, He, Li $\rightarrow$ F, Na $\rightarrow$ Cl, K $\rightarrow$ Br |
| RIMP2-TZVPP | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVDZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVTZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVQZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVDZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVTZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVQZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVDZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVTZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVQZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

- •

${}^{a}$XX includes SV(P), SVP, TZVP, TZVPP, QZVP, and QZVPP.
${}^{b}$XX includes SV(P), SVP, SVPD, TZVP, TZVPD, TZVPP, TZVPPD, QZVP, and QZVPPD.
${}^{c}$XX includes SVP, TZVP, TZVPP, and QZVPP, obtained by systematic pruning of diffuse functions.
For example, RIMP2-def2-ma-SVP is obtained from RIMP2-def2-SVPD by pruning in the same manner
that def2-ma-SVP is obtained from def2-SVPD.
${}^{d}$This is the original SVP fitting set from Ref. [[1439]](../bib_references/bib.md#bib1501)
.
${}^{e}$Where *cal* = may, jun, or jul. These are constructed from the corresponding RIMP2-aug-cc-pVXZ basis set by systematic
deletion of diffuse functions analogous to how the “calendar” basis set *cal*-cc-pVXZ is constructed from aug-cc-pVXZ.

Table 8.9: 
Built-in auxiliary basis sets available in **Q-Chem** for electron correlation.
