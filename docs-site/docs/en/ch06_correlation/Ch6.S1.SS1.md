---
title: "6.1.1 Overview"
---

## 6.1.1 Overview

(July 4, 2026)

The Hartree-Fock procedure, while often qualitatively correct, is frequently
quantitatively deficient. The deficiency is due to the underlying assumption of
the Hartree-Fock approximation: that electrons move *independently*
within molecular orbitals subject to an averaged field imposed by the remaining
electrons. The error that this introduces is called the correlation energy and
a wide variety of procedures exist for estimating its magnitude. The purpose of
this Chapter is to introduce the main wave function-based methods available in
**Q-Chem** to describe electron correlation.

Wave function-based electron correlation methods concentrate on the design of
corrections to the wave function beyond the mean-field Hartree-Fock
description. This is to be contrasted with the density functional theory
methods discussed in the previous Chapter. While density functional methods
yield a description of electronic structure that accounts for electron
correlation subject only to the limitations of present-day functionals (which,
for example, omit dispersion interactions), DFT cannot be systematically
improved if the results are deficient. Wave function-based approaches for
describing electron correlation[[16]](../bib_references/bib.md#bib20)

offer this main advantage. Their main disadvantage is relatively high
computational cost, particularly for the higher-level theories.

There are four broad classes of models for describing electron correlation that
are supported within **Q-Chem**. The first three directly approximate the full
time-independent Schrödinger equation. In order of increasing accuracy, and
also increasing cost, they are:

1. Perturbative treatment of pair correlations between electrons, typically
capable of recovering 80% or so of the correlation energy in stable
molecules.
2. Self-consistent treatment of pair correlations between electrons (most often
based on coupled-cluster theory),
capable of recovering on the order of 95% or so of the correlation
energy.
3. Non-iterative corrections for higher than double substitutions, which
can account for more than 99% of the correlation energy. They are the
basis of many modern methods that are capable of yielding chemical
accuracy for ground state reaction energies, as exemplified by the
G2[[296]](../bib_references/bib.md#bib297)
 and G3 methods.[[295]](../bib_references/bib.md#bib299)

These methods are discussed in the following subsections.

There is also a fourth class of methods supported in **Q-Chem**, which have a
different objective. These active space methods aim to obtain a balanced
description of electron correlation in highly correlated systems, such as
diradicals, or along bond-breaking coordinates. Active space methods are
discussed in Section [6.14](sect_ccactive.md). Finally, equation-of-motion (EOM)
methods provide tools for describing open-shell and electronically excited
species. Selected configuration interaction (CI) models are also available.

In order to carry out a wave function-based electron correlation calculation
using **Q-Chem**, three *$rem* variables need to be set:

- BASIS to specify the basis set (see Chapter [8](../ch08_basis/chap_basis.md))
- METHOD for treating correlation
- N_FROZEN_CORE frozen core electrons (FC default, optionally
FC, or $n$)

For wave function-based correlation methods, the default option for exchange
is Hartree-Fock. If desired, correlated calculations can employ DFT orbitals,
which should be set up using a pair of EXCHANGE and
CORRELATION keywords. EXCHANGE should be set to a specific
DFT method (see Section [6.15.2](sub_ccdft.md)).

Additionally, for EOM or CI calculations the number of target states of each type
(excited, spin-flipped, ionized, attached, *etc.*) in each
irreducible representation (irrep) should be specified (see Section
[7.9.18](../ch07_excited/sub_ccjobcontol.md)). The level of correlation of the target EOM states
may be different from that used for the reference, and can be specified by
EOM_CORR keyword.

The full range of ground and excited state wave function-based correlation
methods available (*i.e.* the recognized options to the METHOD keyword)
are as follows. Ground-state methods are also a valid option for
the CORRELATION keyword.

### `METHOD`

> **Specifies the level of theory, either DFT or wave function-based.**
>
> * **Type**: `STRING`
> * **Default**: `HF`
> * **Options**:
>     * `MP2`: Sections 6.3 and 6.4
>     * `RI-MP2`: Section 6.6
>     * `Local_MP2`: Section 6.5
>     * `RILMP2`: Section 6.6.2
>     * `ATTMP2`: Section 6.7
>     * `ATTRIMP2`: Section 6.7
>     * `ZAPT2`: A more efficient restricted open-shell MP2 method.
>     * `632`: Jayatilaka D., Lee T. J. Chem. Phys. Lett. (1992) ,
>     * `199`: , pp. 211 . Link
>     * `MP3`: Section 6.3
>     * `MP4SDQ`: Section 6.3
>     * `MP4`: Section 6.3
>     * `CCD`: Section 6.12
>     * `CCD(2)`: Section 6.13
>     * `CCSD`: Section 6.12
>     * `CCSDT`: Section 6.12.3
>     * `CC2`: Section 6.12
>     * `CCSD(T)`: Section 6.13
>     * `CCSD(2)`: Section 6.13
>     * `CCSD(fT)`: Section 6.13.3
>     * `CCSD(dT)`: Section 6.13.3
>     * `QCISD`: Section 6.12
>     * `QCISD(T)`: Section 6.13
>     * `OD`: Section 6.12
>     * `OD(T)`: Section 6.13
>     * `OD(2)`: Section 6.13
>     * `VOD`: Section 6.14
>     * `VOD(2)`: Section 6.14
>     * `QCCD`: Section 6.12
>     * `QCCD(T)`
>     * `QCCD(2)`
>     * `VQCCD`: Section 6.14
> * **Recommendation**: Consult the literature for guidance.
