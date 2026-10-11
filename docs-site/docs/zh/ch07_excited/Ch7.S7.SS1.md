---
title: "7.7.1 Introduction"
---

## 7.7.1 Introduction

(July 4, 2026)

Standard TDDFT is prone to catastrophic failure in regimes where there is a substantial
difference in density between ground and excited states, such as charge-transfer, Rydberg,
or core excitations.[[351]](../bib_references/bib.md#bib357)
 This can be greatly ameliorated via
inclusion of orbital relaxation beyond linear response, via explicit optimization of
excited-state orbitals in a manner analogous to a ground-state SCF calculation, and several
methods for doing so are described in this section. Several of these methods recognize that
a single-determinant description of any singlet excited state cannot be spin pure, and the
minimal description of an open-shell singlet state requires two determinants. This can be
handled in a computationally tractable manner using restricted open-shell Kohn-Sham (ROKS)
calculation, as described in Section [7.7.4](ex_ESROKS.md). For open-shell singlet states
(*i.e.*, biradicals), a simplified version of this approach is approximate spin purification
as described in Section [7.7.3](sect_OpSing.md).

Excited-state orbital optimization is generally more challenging as compared to the ground-
state SCF problem because excited-state solutions of the SCF equations are generally not
local minima in the orbital rotation space, but are instead typically saddle points.
Traditional orbital optimizers like DIIS or GDM often fail to locate these excited-state,
non-aufbau solutions to the SCF equations, and instead collapse to lower-energy
solutions (usually the ground state). This problem of “variational collapse” restricts
the utility of excited-state orbital-optimization methods. The maximum overlap method
(MOM, Section [7.7.2](ex_OpSing.md)) can prevent this in many cases, but is constrained
by the convergence issues stemming from the underlying SCF algorithm. **Q-Chem** includes
two alternative procedures that tend to be more robust as compared to MOM and can be
used to find excited-state solutions to the SCF equations: squared-gradient minimization
(Section [7.7.5](ex_BEDSCF.md)),[[511]](../bib_references/bib.md#bib526)
 and state-targeted energy projection
(Section [7.7.8](ex_ROSTEP.md)).[[196]](../bib_references/bib.md#bib189)
 Both methods can be used on their
own to produce a single-determinant “$\Delta$SCF” estimate of an excitation
energy,

 using ground-state machinery, or else combined with the ROKS
procedure in order to avoid the spin contamination problems associated with the $\Delta$SCF approach.
