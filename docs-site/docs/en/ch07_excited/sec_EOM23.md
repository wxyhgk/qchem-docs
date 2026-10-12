---
title: "7.9.24 EOM(2,3) Methods for Higher-Accuracy and Problematic Situations (CCMAN only)"
---

## 7.9.24 EOM(2,3) Methods for Higher-Accuracy and Problematic Situations
(CCMAN only)

(July 4, 2026)

In the EOM-CC(2,3) approach,[[581]](../bib_references/bib.md#bib603)
 the transformed Hamiltonian
$\bar{H}$ is diagonalized in the basis of the reference, singly, doubly, and
triply excited determinants, *i.e.*, the excitation operator $R$ is truncated at
triple excitations. The excitation operator $T$, however, is truncated at
double excitation level, and its amplitudes are found from the CCSD equations,
just like for EOM-CCSD [or EOM-CC(2,2)] method.

The accuracy of the EOM-CC(2,3) method closely follows that of full EOM-CCSDT
[which can be also called EOM-CC(3,3)], whereas computational cost of the
former model is less.

The inclusion of triple excitations is necessary for achieving chemical
accuracy (1 kcal/mol) for ground state properties. It is even more so for
excited states. In particular, triple excitations are crucial for doubly
excited states,[[581]](../bib_references/bib.md#bib603)
 excited states of some radicals and SF
calculations (diradicals, triradicals, bond-breaking) when a reference
open-shell state is heavily spin-contaminated. Accuracy of EOM-CCSD and
EOM-CC(2,3) is compared in Table  [7.3](#table:EOMvsEOM3).

| System | EOM-CCSD | EOM-CC(2,3) |
| --- | --- | --- |
| Singly-excited electronic states | 0.1–0.2 eV | 0.01 eV |
| Doubly-excited electronic states | $\geq$ 1 eV | 0.1–0.2 eV |
| Severe spin-contamination of the reference | $\sim$ 0.5 eV | $\leq$ 0.1 eV |
| Breaking single bond (EOM-SF) | 0.1–0.2 eV | 0.01 eV |
| Breaking double bond (EOM-2SF) | $\sim$ 1 eV | 0.1–0.2 eV |

Table 7.3: Performance of the EOM-CCSD and EOM-CC(2,3) methods

The applicability of the EOM-EE/SF-CC(2,3) models to larger systems can
be extended by using their active-space variants, in which triple excitations
are restricted to semi-internal ones.

Since the computational scaling of EOM-CC(2,3) method is ${\cal{O}}({N^{8}})$, these
calculations can be performed only for relatively small systems. Moderate size
molecules (10 heavy atoms) can be tackled by either using the active space
implementation or tiny basis sets. To achieve high accuracy for these systems,
energy additivity schemes can be used. For example, one can extrapolate
EOM-CCSDT/large basis set values by combining large basis set EOM-CCSD
calculations with small basis set EOM-CCSDT ones.

Running the full EOM-CC(2,3) calculations is straightforward, however, the
calculations are expensive with the bottlenecks being storage of the data on a
hard drive and the CPU time. Calculations with around 80 basis functions are
possible for a molecule consisting of four first row atoms (NO dimer). The
number of basis functions can be larger for smaller systems.

!!! note "Note"
    In EE calculations, one needs to always solve for at least one low-spin
    root in the first symmetry irrep in order to obtain the correlated EOM energy
    of the reference. The triples correction to the total reference energy must be
    used to evaluate EOM-(2,3) excitation energies.


!!! note "Note"
    EOM-CC(2,3) works for EOM-EE, EOM-SF, and EOM-IP/EA. In EOM-IP,
    “triples” correspond to $3h2p$ excitations, and the computational scaling of
    EOM-IP-CC(2,3) is less.

