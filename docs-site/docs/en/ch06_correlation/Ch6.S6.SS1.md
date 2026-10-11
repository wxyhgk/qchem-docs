---
title: "6.6.1 Introduction"
---

## 6.6.1 Introduction

(July 4, 2026)

For a molecule of fixed size, increasing the number of basis functions
*per atom*, $n$, leads to ${\cal{O}}({n^{4}})$ growth in the number of significant
four-center two-electron integrals, since the number of non-negligible product
charge distributions, $|\mu\nu\rangle$, grows as ${\cal{O}}({n^{2}})$. As a result, the use
of large (high-quality) basis expansions is computationally costly. Perhaps
the most practical way around this “basis set quality” bottleneck is the use
of auxiliary basis expansions.[[387]](../bib_references/bib.md#bib395)

The ability to use auxiliary basis sets to accelerate a variety of electron
correlation methods, including both energies and analytical gradients, is a
major feature of **Q-Chem**.

The auxiliary basis $\{|K\rangle\}$ is used to approximate products of Gaussian
basis functions:

<a id="Ch6.E25"></a>

$$
|\mu\nu\rangle\approx|\widetilde{\mu\nu}\rangle=\sum_{K}|K\rangle C_{\mu\nu}^{K} \tag{6.25}
$$

Auxiliary basis expansions were introduced long ago, and are now widely
recognized as an effective and powerful approach, which is sometimes
synonymously called resolution of the identity (RI) or density fitting (DF).
When using auxiliary basis expansions, the rate of growth of computational cost
of large-scale electronic structure calculations with $n$ is reduced to
approximately $n^{3}$.

If $n$ is fixed and molecule size increases, auxiliary basis expansions reduce
the pre-factor associated with the computation, while not altering the
scaling. The important point is that the pre-factor can be reduced by 5 or 10
times or more. Such large speedups are possible because the number of
auxiliary functions required to obtain reasonable accuracy, $X$, has been shown
to be only about 3 or 4 times larger than $N$.

The auxiliary basis expansion coefficients, $\mathbf{C}$, are determined by
minimizing the deviation between the fitted distribution and the actual
distribution, $\langle\mu\nu-\widetilde{\mu\nu}|{\mu\nu-\widetilde{\mu\nu}}\rangle$, which leads to the following set of linear equations:

<a id="Ch6.E26"></a>

$$
\sum_{L}{\left\langle{K\left|L\right.}\right\rangle}C_{\mu\nu}^{L}=\left\langle{K\left|{\mu\nu}\right.}\right\rangle \tag{6.26}
$$

Evidently solution of the fit equations requires only two- and three-center
integrals, and as a result the (four-center) two-electron integrals can be
approximated as the following optimal expression for a given choice of
auxiliary basis set:

<a id="Ch6.E27"></a>

$$
\langle\mu\nu|\lambda\sigma\rangle\approx\langle\widetilde{\mu\nu}|\widetilde{\lambda\sigma}\rangle=\sum_{K,L}C_{\mu\nu}^{L}\langle L|K\rangle C_{\lambda\sigma}^{K} \tag{6.27}
$$

In the limit where the auxiliary basis is complete (*i.e.* all products of
AOs are included), the fitting procedure described above will be exact.
However, the auxiliary basis is invariably incomplete (as mentioned above,
$X\approx 3N)$ because this is essential for obtaining increased computational
efficiency.

Standardized auxiliary basis sets have been developed by the Karlsruhe group
for second-order perturbation (MP2) calculations of the correlation
energy.[[1439]](../bib_references/bib.md#bib1501)
 Using these basis sets, absolute
errors in the correlation energy are small (*e.g.*, below 60 $\mu$Hartree per
atom), and errors in relative energies are smaller still At the same time,
speedups of 3–30$\times$ are realized. This development has made the routine
use of auxiliary basis sets for electron correlation calculations possible.

Correlation calculations that can take advantage of auxiliary basis expansions
are described in the remainder of this section (MP2, and MP2-like methods) and
in Section [6.19](sect_pairing.md) (simplified active space coupled cluster methods
such as PP, PP(2), IP, RP). These methods automatically employ auxiliary basis
expansions when a valid choice of auxiliary basis set is supplied using the
AUX_BASIS_CORR or
AUX_BASIS keyword which is used in the same way as the BASIS
keyword.
The PURECART *$rem* is no longer needed here, even if using
a auxiliary basis that does not have a predefined value. There
is a built-in automatic procedure that provides the effect
of the PURECART *$rem* in these cases by default.
