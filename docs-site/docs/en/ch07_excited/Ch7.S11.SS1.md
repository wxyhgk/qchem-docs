---
title: "7.11.1 Introduction"
---

## 7.11.1 Introduction

(July 4, 2026)

The restricted active space spin-flip (RAS-SF) is a special form of
configuration interaction that is capable of describing the ground and
low-lying excited states with moderate computational cost in a single-reference
formulation,[[203]](../bib_references/bib.md#bib201)

including strongly correlated systems. The RAS-SF approach is essentially a
much lower computational cost alternative to Complete Active Space SCF (CASSCF)
methods. RAS-SF typically works by performing a full CI calculation within an
active space that is defined by the half-occupied orbitals of a restricted open
shell HF (ROHF) reference determinant. In this way the difficulties of
state-specific orbital optimization in CASSCF are bypassed. Single excitations
into (hole) and out of (particle) the active space provide state-specific
relaxation instead. Unlike most CI-based methods, RAS-SF is size-consistent,
as well as variational, and, the increase in computational cost with system
size is modest for a fixed number of spin flips. Beware, however, for the
increase in cost as a function of the number of spin-flips is exponential!
RAS-SF has been shown to be capable of tackling multiple low-lying electronic
states in polyradicals and reliably predicting ground state
multiplicities.[[203]](../bib_references/bib.md#bib201)

RAS-SF can also be viewed as one particular case of a more general RAS-CI
family of methods. For instance, instead of defining the active space via
spin-flipping as above, initial orbitals of other types can be read in, and
electronic excitations calculated this way may be viewed as a RAS-EE-CI method
(though size-consistency will generally be lost). Similar to EOM-CC approaches
(see Section [7.9](topic_eomcc.md)), other target RAS-CI wave functions can be
constructed starting from any electronic configuration as the reference and
using a general excitation-type operator. For instance, one can construct an
ionizing variant that removes an arbitrary number of particles that is
RAS-$n$IP-CI. An electron-attaching variant is RAS-$n$EA-CI.[[209]](../bib_references/bib.md#bib203)

**Q-Chem** features two versions of RAS-CI code with different, complementary,
functionality. One code (invoked by specifying CORRRELATION = RASCI)
has been written by David Casanova;[[209]](../bib_references/bib.md#bib203)
 below we will refer to
this code as RASCI1. The second implementation (invoked by specifying
CORRRELATION = RASCI2) is primarily due to Paul
Zimmerman;[[1584]](../bib_references/bib.md#bib1647)
 we will refer to it as RASCI2 below.
Both codes can be used to computed several state specific and interstate properties,
such as spin-orbit couplings (as described in Section [7.9.21.4](sec_EOMGRAD.md#sec:EOMSOC)).[[191]](../bib_references/bib.md#bib186)

The RASCI1 code uses an integral-driven implementation (exact integrals) and
spin-adaptation of the CI configurations which results in a smaller
diagonalization dimension. The current **Q-Chem** implementation of RASCI1
allows for the calculation of systems with any number of $\alpha$ and $\beta$
number of electrons, with the multiplicity ($\langle\hat{S}^{2}\rangle$) of each state
being printed alongside the state energy. Shared memory parallel execution
decreases compute time as all the underlying integrals routines are parallelized.

The RASCI2 code includes the ability to simulate closed and open shell systems
(*i.e.*, even and odd numbers of electrons), fast integral evaluation using the
resolution of the identity (RI) approximation, shared memory parallel
operation, and analysis of the $\langle\hat{S}^{2}\rangle$ values and natural
orbitals. The natural orbitals are stored in the `$QCSCRATCH` directory in a
folder called “`NOs`” in **MolDen**-readable format. Shared memory parallel is
invoked as described in Section [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel). A RASCI2 input requires the
specification of an auxiliary basis set analogous to RI-MP2 computations (see
Section [6.6.2](../ch06_correlation/sect_rimp2.md)). Otherwise, the active space as well as hole and
particle excitations are specified in the same way as in RASCI1.

!!! note "Note"
    Because RASCI2 uses the RI approximation, the total energies computed
    with the two codes will be slightly different. Energy differences
    between different states should closely match each other, however.

