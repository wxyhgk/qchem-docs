---
title: "6.19.1 Introduction"
---

## 6.19.1 Introduction

(July 4, 2026)

The methods described below are related to valence bond theory and are handled by
the GVBMAN module. The following models are available:

### `CORRELATION`

> **Specifies the correlation level in GVB models handled by GVBMAN.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `PP`: CCVB GVB_IP GVB_SIP GVB_DIP OP NP 2P
> * **Recommendation**: As a rough guide, use PP for biradicaloids, and CCVB for polyradicaloids involving strong spin correlations. Consult the literature for further guidance.

Molecules where electron correlation is strong are characterized by small
energy gaps between the nominally occupied orbitals (that would comprise the
Hartree-Fock wave function, for example) and nominally empty orbitals. Examples
include so-called diradicaloid molecules,[[655]](../bib_references/bib.md#bib679)
 or molecules with
partly broken chemical bonds (as in some transition-state structures). Because
the energy gap is small, electron configurations other than the reference
determinant contribute to the molecular wave function with considerable
amplitude, and omitting them leads to a significant error.

Including all possible configurations however, is a vast overkill. It is common
to restrict the configurations that one generates to be constructed not from
all molecular orbitals, but just from orbitals that are either “core” or
“active”. In this section, we consider just one type of active space, which
is composed of two orbitals to represent each electron pair: one nominally
occupied (bonding or lone pair in character) and the other nominally empty, or
correlating (it is typically anti-bonding in character). This is usually called
the perfect pairing active space, and it clearly is well-suited to represent
the bonding/anti-bonding correlations that are associated with bond-breaking.

The quantum chemistry within this (or any other) active space is given by a
Complete Active Space SCF (CASSCF) calculation, whose exponential cost growth
with molecule size makes it prohibitive for systems with more than about 14
active orbitals. One well-defined coupled cluster (CC) approximation based on
CASSCF is to include only double substitutions in the valence space whose
orbitals are then optimized. In the framework of conventional CC theory, this
defines the valence optimized doubles (VOD) model,[[724]](../bib_references/bib.md#bib755)
 which
scales as ${\cal{O}}({N^{6}})$ (see Section [6.14.2](topic_vod.md)). This is still too
expensive to be readily applied to large molecules.

The methods described in this section bridge the gap between sophisticated but
expensive coupled cluster methods and inexpensive methods such as DFT, HF and
MP2 theory that may be (and indeed often are) inadequate for describing
molecules that exhibit strong electron correlations such as diradicals. The
coupled cluster perfect pairing (PP),[[287]](../bib_references/bib.md#bib291)
 imperfect
pairing[[1387]](../bib_references/bib.md#bib1449)
 (IP) and restricted coupled
cluster[[1390]](../bib_references/bib.md#bib1452)
 (RCC) models are local approximations to VOD that
include only a linear and quadratic number of double substitution amplitudes
respectively. They are close in spirit to generalized valence bond (GVB)-type
wave functions,[[461]](../bib_references/bib.md#bib474)
 because in fact they are all coupled
cluster models for GVB that share the same perfect pairing active space. The
most powerful method in the family, the Coupled Cluster Valence Bond (CCVB)
method,[[1274]](../bib_references/bib.md#bib1328)
 is a valence bond approach that
goes well beyond the power of GVB-PP and related methods, as discussed below in
Section [6.19.3](subsec_CCVB.md).
