---
title: "7.10.12 Frozen-Density Embedding: FDE-ADC methods"
---

## 7.10.12 Frozen-Density Embedding: FDE-ADC methods

(July 4, 2026)

FDE-ADC[[1121]](../bib_references/bib.md#bib1168)
 is a method to include interactions between an
embedded species and its environment into an ADC($n$) calculation based on
Frozen Density Embedding Theory (FDET).[[1453]](../bib_references/bib.md#bib1515)

FDE-ADC supports ADC and CVS-ADC methods of orders 2s,2x and 3 and regular ADC
job control keywords also apply.

The FDE-ADC method starts with generating an embedding potential using a
MP($n$) density for the embedded system (A) and a DFT or HF density for
the environment (B). A Hartree-Fock calculation is then carried out during
which the embedding potential is added to the Fock operator. The embedded
Hartree-Fock orbitals act as an input for the subsequent ADC calculation which
yields the embedded properties (vertical excitation energies, oscillator
strengths, etc.). Further information on the FDE-ADC method and FDE-ADC job
control are described in Section [11.7.2.1](../ch11_env/subsec_FDE_MAN.md#subsubsec:FDE_ADC).
