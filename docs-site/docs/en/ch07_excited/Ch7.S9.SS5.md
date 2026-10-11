---
title: "7.9.5 Further approximate EOM-CC Methods"
---

## 7.9.5 Further approximate EOM-CC Methods

(July 4, 2026)

## 7.9.5.1 EOM-MP2 and EOM-MP2T

Approximate EOM-CCSD models with $T$-amplitudes obtained at the MP2 level offer
reduced computational cost compared to the full EOM-CCSD since the
computationally demanding ${\cal{O}}({N^{6}})$ CCSD step is eliminated from the
calculation. Two methods of this type are implemented in **Q-Chem**. The first is
invoked with the keyword METHOD = EOM-MP2. Its formulation and
implementation follow the original EOM-CCSD(2) approach developed by Stanton
and coworkers.[[1292]](../bib_references/bib.md#bib1347)
 The second method can be requested with
the METHOD = EOM-MP2T keyword and is similar to EOM-MP2, but it
accounts for the additional terms in $\bar{H}$ that appear because the MP2
$T$-amplitudes do not satisfy the CCSD equations. EOM-MP2 *ansatz* is
implemented for IP/EA/EE/SF energies, state properties, and interstate
properties (EOM-EOM, but not REF-EOM). EOM-MP2t is available for the IP/EE/EA energy calculations only.

## 7.9.5.2 EOM-CCSD-S(D) and EOM-MP2-S(D)

These are very light-weight EOM methods in which the EOM problem is solved in
the singles block and the effect of doubles is evaluated perturbatively. The
$\bar{H}$ is evaluated by using either CCSD or MP2 amplitudes, just as in the
regular EOM calculations. The EOM-MP2-S(D) method, which is similar in level
of correlation treatment to SOS-CIS(D), is particularly fast. These methods are
implemented for IP and EE states. For valence states, the
errors for absolute ionization or excitation energies against regular EOM-CCSD
are about 0.4 eV and appear to be systematically blue-shifted; the EOM-EOM
energy gaps look better. The calculations are set as in regular EOM-EE/IP, but
using METHOD = EOM-CCSD-SD(D) or METHOD = EOM-MP2-SD(D).
State properties and EOM-EOM transition properties can be computed using these
methods (reference-EOM properties are not yet implemented). These methods are designed
for treating core-level states.[[1193]](../bib_references/bib.md#bib1248)

**Note: 

These methods are still in the experimental stage.
**
