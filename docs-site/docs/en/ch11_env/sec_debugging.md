---
title: "11.5.8 Debugging EFP Jobs"
---

## 11.5.8 Debugging EFP Jobs

(July 4, 2026)

The key advantage of the QM/EFP models is a polarizable self-consistent description
of a system. However, achieving self-consistent polarization might also create a challenge.
Polarization catastrophe (induced dipoles on some of the fragments increase infinitely)
is a frequent scenario in calculations of polar systems. In most cases, however,
the polarization catastrophe happens due to bad structures (e.g., structures with
overlapping or closely spaced atoms) or due to bad parameters of effective fragments
(diverging multipoles, large polarizability values). Keyword EFP_PRINT
controls the amount of information about the progress of EFP calculation and information
about fragments. Specifically, EFP_PRINT=1 prints a small number of additional
details about timings of individual EFP-related steps and convergence of induced dipoles, while
EFP_PRINT=2 prints warnings in case of large induced dipoles on particular
fragments and large fragment-fragment electrostatic energies, which might suggest unphyscially
close contacts between fragments.

Keywords EFP_POL_DAMP and EFP_POL_DAMP_TT_VALUE control polarization
damping parameters of all fragments in the system. The default value of polarization
damping (the parameter that takes care of screening electrostatic and polarization fields at
small inter-fragment distances) is set to 0.6 (see [[1271]](../bib_references/bib.md#bib1324)
 and
Eq. [11.71](sec_theory.md#eq:pol_damp_1)). EFP_POL_DAMP_TT_VALUE overwrites this default setting,
with smaller values providing more screening. Polarization damping of individual fragments
might be further adjusted in fragment parameter file via POLAB setting
(see `https://libefp2.github.io/parameters.html#additional-efp-parameters`) for detail.
