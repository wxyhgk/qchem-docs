---
title: "7.9.4 EOM-XX-CC2"
---

## 7.9.4 EOM-XX-CC2

(July 4, 2026)

A more economical flavor of EOM-CCSD is CC2 linear response theory,[[249]](../bib_references/bib.md#bib250)

which can also be interpreted as EOM-CC2. The double amplitudes
for the reference state are approximated using the CC2 equations (see Section [6.12.4](../ch06_correlation/topic_cc2.md))
and the equations for the target states are modified accordingly. This means that
Eqs. [7.97](sec_EOMEE.md#eq747) to [7.99](sec_EOMEE.md#eq749) are valid for EOM-XX-CC2 as well
but the elements of $\bar{H}$ are defined differently. CC2 calculations can be run in the same way as CCSD calculations by setting METHOD to CC2 or EOM-CC2.

There are two different implementations of CC2 available in **Q-Chem**: one in the CCMAN2 suite for coupled-cluster methods and one in LIBGMBPT for general many-body perturbation theory methods. In CCMAN2, the code structure is similar to that of CCSD, whereas LIBGMBPT uses a partitioned form of the doubles equations avoiding the need to store the double amplitudes.[[532]](../bib_references/bib.md#bib546)
 Combined with the resolution-of-the-identity (RI) approximation, this brings the memory cost down to $\mathcal{O}\left(N^{3}\right)$ instead of $\mathcal{O}\left(N^{4}\right)$ and reduces the computational cost. For smaller molecules, CCMAN2 may deliver a faster performance (especially for systems with symmetry), whereas for larger systems we recommend
using LIBGMBPT implementation.

In CCMAN2, the following CC2 features are available with a RHF, UHF or ROHF references and
using point-group symmetry:

- Energies for EOM-EE/SF/EA/IP-CC2[[1040]](../bib_references/bib.md#bib1085)
;
- One-electron properties for the CC2 reference state and the EOM-EE/SF-CC2 states with and without amplitude response;
- Transition dipole moments for transitions of type CC2 $\leftrightarrow$ EOM-EE-CC2, EOM-EE-CC2 $\leftrightarrow$ EOM-EE-CC2 and EOM-SF-CC2 $\leftrightarrow$ EOM-SF-CC2;
- Dyson orbitals (see section [7.9.29](topic_dyson.md)) for transitions of type CC2 $\leftrightarrow$ EOM-EA/IP-CC2 and EOM-EE/SF-CC2 $\leftrightarrow$ EOM-EA/IP-CC2;
- Resonance energies with EOM-EE/EA-CC2 using a CAP, CS or CBFs[[1382]](../bib_references/bib.md#bib1443)
 (see Section [7.9.10](sub_cc_cs_cap.md)).

The electron repulsion integrals (ERIs) can be approximated by using the
resolution-of-the-identity approximation or Cholesky decomposition or canonical ERIs can
be used. In addition, single-precision execution can be used to further reduce the cost of the calculations.

The LIBGMBPT implementation of CC2 only uses the RI approximation. It does not
exploit point group symmetry or single-precision execution. The following features
are available:

- Energies with EOM-EE-CC2 with RHF or UHF references;
- Energies with EOM-SF-CC2 with UHF references[[1040]](../bib_references/bib.md#bib1085)
;
- Energies with EOM-EA/IP-CC2 with RHF references[[1041]](../bib_references/bib.md#bib1086)
;
- Resonance energies with EOM-EA-CC2 with RHF references by using a CAP, CS or
CBFs[[1382]](../bib_references/bib.md#bib1443)
 (see section [7.9.10](sub_cc_cs_cap.md));
- Spin-scaling (see Section [6.6.5](../ch06_correlation/topic_sbmp2.md)) is available for real-valued EOM-EE-CC2
for singlet excited states and for both real- and complex-valued EOM-EA-CC2.

For bound states LIBGMBPT uses a mixed Davidson/DIIS solver to solve the EOM eigenvalue problem.[[532]](../bib_references/bib.md#bib546)
 For resonances only the Davidson solver is used.[[1382]](../bib_references/bib.md#bib1443)
 Changing the default parameters for the Davidson algorithm can be done with EOM_DAVIDSON_CONVERGENCE, EOM_DAVIDSON_MAX_ITER and EOM_DAVIDSON_MAXVECTORS (as for CCMAN2) while the DIIS parameters can be changed with EOM_DIIS_CONVERGENCE, EOM_DIIS_MAX_ITER and EOM_DIIS_MAXVECTORS (see section [7.9.18](sub_ccjobcontol.md)).

The LIBGMBPT implementation is invoked by setting CCMAN2 to -1; the default for CC2 is currently CCMAN2. The stochastic versions of RI-CC2 are also available
(see Section [6.12.5](../ch06_correlation/sec_Stochastic_CC2.md)).
