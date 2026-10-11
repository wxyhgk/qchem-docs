---
title: "8.10.2 ECP Fitting"
---

## 8.10.2 ECP Fitting

(July 4, 2026)

The ECP matrix elements are arguably the most difficult one-electron integrals
in existence. Indeed, using current methods, the time taken to compute the ECP
integrals can exceed the time taken to compute the far more numerous electron
repulsion integrals. **Q-Chem** 5.0 implements a state-of-the-art ECP implementation[[933]](../bib_references/bib.md#bib972)

based on efficient recursion relations and upper bounds.
This method relies on a restricted radial potential $U_{\ell}(r)$, where the
radial power is only ever zero, *i.e.* $n=0$. Whilst true for some ECPs, such as
the Stuttgart-Bonn sets, many other ECPs have radial potentials containing $n=-2$ and $n=-1$ terms. To overcome this challenge, we fit these ECP
radial potentials using only $n=0$ terms. Each $n=-2$ and $n=-1$ term is
expanded as a sum of three $n=0$ terms, each with independent contraction
coefficient $D_{\ell_{k}}$ and Gaussian exponent $\eta_{\ell_{k}}$. The Gaussian
exponents are given by a predetermined recipe and the contraction coefficients
are computed in a least squares fitting procedure. The errors introduced by
the ECP fitting are insignificant and of the same order as those
introduced by numerical integration present in other ECP methods. For the built-in
ECPs, fitted variants of each are now provided in the `$QCAUX` directory, *e.g.*,
`fit-LANL2DZ`. For user-defined ECPs with $n=-2$ or $n=-1$ terms, **Q-Chem** will perform a fit
at run time with the additional rem keyword ECP_FIT = TRUE.
