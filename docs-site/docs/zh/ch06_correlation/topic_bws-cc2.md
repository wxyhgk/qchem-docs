---
title: "6.12.6 Size-Consistent Brillouin-Wigner Second-Order Approximate Coupled Cluster Singles and Doubles (BWs-CC2)"
---

## 6.12.6 Size-Consistent Brillouin-Wigner Second-Order Approximate Coupled Cluster Singles and Doubles (BWs-CC2)

(July 4, 2026)

Choosing to approximate the Hamiltonian in the CCSD equations using the unperturbed Møller-Plesset
Hamiltonian is a popular, but not unique choice. Instead, it is possible to use the unperturbed
size-consistent Brillouin-Wigner Hamiltonian[[195]](../bib_references/bib.md#bib196)

during evaluation of the Doubles equation. For a definition of this Hamiltonian, see Section [6.8](topic_bws2.md).

Compared to regular (MP-)CC2, BWs-CC2 is a *regular* theory, i. e. for positive regularisation
strength, it does not diverge for vanishing HOMO/LUMO gaps. It can therefore be applied to dissociated
bonds and few-reference systems whose dominating determinants are coupled by double excitations.[[337]](../bib_references/bib.md#bib340)

In order to invoke this method, set METHOD = RIBWS2 in the REM section,
and EXC_METHOD = CC2 in the *$bws2* section. BWs-CC2 is available for all
partitions, recommended is the use of either BW-s2 or MPR-BWs2. Currently, only the electronic
ground state is implemented. For general purposes it is recommended to employ MPR-BWs2 with
$A_{0}=2$ and $B_{0}=0$ in BWs-CC2 calculations, though the optimal parameter set is
dependent on the system and chemical quantity of interest.
