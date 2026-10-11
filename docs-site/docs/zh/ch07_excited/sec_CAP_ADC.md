---
title: "7.10.9 CAP/ADC Methods for the Description of Metastable Electronic States"
---

## 7.10.9 CAP/ADC Methods for the Description of Metastable Electronic States

(July 4, 2026)

For the description of metastable electronic states and the calculation of
positions and widths of such electronic resonances, the *complex absorbing potential* (CAP)
methodology[[1175]](../bib_references/bib.md#bib1228)
 has been combined with all available non-CVS ADC methods
using a subspace projection approach.[[1284]](../bib_references/bib.md#bib1340)

In this approach, the CAP is projected onto the subspace spanned by a number of converged
(ADC, IP-ADC or EA-ADC) states. For this purpose one-electron state and state-to-state
transition densities computed using the second-order ISR are exploited.

The generation of CAP trajectories and determination of the resonance parameters can be
done *a posteriori* (see Ref. [[1198]](../bib_references/bib.md#bib1252)
 for details), *i.e.*, only a
single electronic structure calculation has to be performed. As a distinct feature of
this approach, a series of different CAP onsets can be handled in a single ADC calculation.

CAP/ADC calculations are invoked by setting ADC_CAP = 1, automatically implying
a CAP strength of $\eta=1$ (or CAP_ETA = 100000). Different CAP types
can be employed, however, it is generally recommended to use a smoothed Voronoi
CAP,[[1283]](../bib_references/bib.md#bib1341)
 which is requested by setting CAP_TYPE = 2.
For this CAP type, a series of different onsets can be controlled using the
CAP_X, CAP_X_STEP and CAP_X_END keywords. For example,
subspace-projected CAP/ADC output for onset values of 2.0, 3.0 and 4.0 a.u. can be
obtained by
setting CAP_X = 2000, CAP_X_STEP = 1000 and
CAP_X_END = 4000.

For further details on different CAP types and their control, also see
Section [7.9.10](sub_cc_cs_cap.md).
