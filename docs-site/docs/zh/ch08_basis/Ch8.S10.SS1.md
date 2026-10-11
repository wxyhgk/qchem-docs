---
title: "8.10.1 Introduction & Overview"
---

## 8.10.1 Introduction & Overview

(July 4, 2026)

The application of quantum chemical methods to elements in the lower half of
the Periodic Table is more difficult than for the lighter atoms. There are
two key reasons for this:

- •

the number of electrons in heavy atoms is large
- •

relativistic effects in heavy atoms are often non-negligible

Both of these problems stem from the presence of large numbers of core
electrons and, given that such electrons do not play a significant
*direct* role in chemical behavior, it is natural to ask whether it is
possible to model their effects in some simpler way. Such enquiries led to the
invention of Effective Core Potentials (ECPs) or pseudopotentials.
Many review articles discussing relativistic effects in chemistry are
available.[[250]](../bib_references/bib.md#bib249)
.

If we seek to replace the core electrons around a given nucleus by a
pseudopotential, while affecting the chemistry as little as possible, the
pseudopotential should have the same effect on nearby valence electrons as the
core electrons. The most obvious effect is the simple electrostatic repulsion
between the core and valence regions but the requirement that valence orbitals
must be orthogonal to core orbitals introduces additional subtler effects that cannot be neglected.

One of the key issues in the development of ECPs is the definition
of the “core”. So-called “large-core” ECPs include all shells except the
outermost one, but “small-core” ECPs include all except the outermost
*two* shells. Although the small-core ECPs are more expensive to use
(because more electrons are treated explicitly), it is often found that their
enhanced accuracy justifies their use.

When an ECP is constructed, it is usually based on either non-relativistic or
quasi-relativistic all-electron calculations. As one might expect, the
quasi-relativistic ECPs tend to yield better results than their
non-relativistic brethren, especially for atoms beyond the 3$d$ block

**Q-Chem**’s ECP package is integrated with its electron correlation and DFT
packages. Of course, no correlation or exchange-correlation energy due to the
core electrons is included when using an ECP in a DFT or correlated method, respectively.

The most widely used ECPs today are of the form first proposed by Kahn
*et al.* in the 1970s.[[661]](../bib_references/bib.md#bib685)
 These model the effects of the core by a
one-electron operator $U(r)$ whose matrix elements are simply added to the
one-electron Hamiltonian matrix. The ECP operator is given by

<a id="eq800"></a>
$$
U(r)=U_{L}(r)+\sum\limits_{\ell=0}^{L-1}{\sum\limits_{m=-l}^{+l}{\left|{Y_{\ell m}}\right\rangle U_{l}(r)\left\langle{Y_{\ell m}}\right|}} \tag{8.6}
$$

where the radial potentials have the form

<a id="eq:radpot"></a>
$$
U_{\ell}(r)=\sum_{k=1}^{K_{\ell}}D_{\ell_{k}}\,r^{n_{\ell_{k}}}e^{-\eta_{\ell_{k}}r^{2}} \tag{8.7}
$$

and $\sum_{m}\left|{Y_{\ell m}}\right\rangle\left\langle{Y_{\ell m}}\right|$ is the
spherical harmonic projector of angular momentum $\ell$. In practice,
$n_{\ell_{k}}=-2$, $-1$ or 0 and $L$ rarely exceeds 5. In addition, $U_{L}(r)$ contains a
Coulombic term $N_{c}/r$, where $N_{c}$ is the number of core electrons.
