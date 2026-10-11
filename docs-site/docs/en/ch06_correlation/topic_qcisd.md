---
title: "6.12.7 Quadratic Configuration Interaction (QCISD)"
---

## 6.12.7 Quadratic Configuration Interaction (QCISD)

(July 4, 2026)

Quadratic configuration interaction with singles and doubles (QCISD)
is a widely used alternative to CCSD,[[1113]](../bib_references/bib.md#bib1162)
 which shares its main
desirable properties of being size-consistent, exact for pairs of electrons,
as well as being also non variational. Its computational cost also scales in the
same way with molecule size and basis set as CCSD, although with slightly
smaller constants. While originally proposed independently of CCSD based on
correcting configuration interaction equations to be size-consistent, QCISD is
probably best viewed as approximation to CCSD. The defining equations are given
below (under the assumption of Hartree-Fock orbitals, which should always be
used in QCISD). The QCISD equations can clearly be viewed as the CCSD equations
with a large number of terms omitted, which are evidently not very numerically significant:

<a id="Ch6.E74"></a>

$$
\displaystyle E_{\text{QCISD}} \tag{6.74a}
$$

QCISD energies are available in **Q-Chem**, and are requested with the QCISD
keyword. As discussed in Section [6.13](topic_ccni.md), the non iterative QCISD(T)
correction to the QCISD solution is also available to approximately incorporate
the effect of higher substitutions.
