---
title: "7.11.9 librassf Effective Hamiltonian Analysis"
---

## 7.11.9 **librassf** Effective Hamiltonian Analysis

(July 4, 2026)

The Bloch effective Hamiltonian can be used in conjunction with a
RAS-1SF calculation to determine the magnetic couplings of multi-site
systems. The **librassf** module provides a variational version of the earlier
perturbative approaches in the CASMAN code. [[927]](../bib_references/bib.md#bib966)

Note that this implementation is still in beta.

Doing the analysis within **librassf** is a two-step process.
First, one must localize the active space orbitals using a Boys localization,
indicated by setting CAS_LOCAL_ALGO and CAS_LOCAL to 1.
(One can alternately use Pipek-Mezey by setting CAS_LOCAL to 2.)
The localized RAS2 orbitals are automatically printed in Molden file
format in the output file. The user can then visualize the localized
orbitals and assign orbitals to sites manually as needed.

Once orbital assignment is complete, one can run a Bloch effective Hamiltonian
calculation. This is done by setting RASSF_DO_BLOCH to true, and
defining orbital assignments in the *$rassf_bloch_sites* section.
This section has three lines. The first line specifies the total number of sites,
the second line specifies the number of orbitals per site,
and the third line is an ordered list of the orbitals belonging to each site.
Note that orbital ordering starts at one. For a dichromium complex, where
orbitals 3, 4, and 5 are localized on the first Cr atom and 1, 2, and 6 are
on the second Cr, the section should therefore be defined as follows:

> ```qchem
> $rassf_bloch_sites
> 2
> 3 3
> 3 4 5 1 2 6
> $end
> ```
