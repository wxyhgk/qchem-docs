---
title: "5.5.4 Consistency Check and Cutoffs"
---

## 5.5.4 Consistency Check and Cutoffs

(July 4, 2026)

Whenever **Q-Chem** calculates numerical density functional integrals, the
electron density itself is also integrated numerically as a test of the quality
of the numerical quadrature. The extent to which this numerical result differs
from the number of electrons is an indication of the accuracy of the other
numerical integrals. A warning message is printed whenever the relative error
in the numerical electron count reaches 0.01%, indicating that the numerical
XC results may not be reliable. If the warning appears on the first SCF cycle
it is probably not serious, because the initial-guess density matrix is
sometimes not idempotent. This is the case with the SAD guess discussed in
Section [4.4](../ch04_scf/sect_initialguess.md), and also with a density matrix that is taken
from a previous geometry optimization cycle, and in such cases the problem will
likely correct itself in subsequent SCF iterations. If the warning persists,
however, then one should consider either using a finer grid or else selecting
an alternative initial guess.

By default, **Q-Chem** will estimate the magnitude of various XC contributions on
the grid and eliminate those determined to be numerically insignificant.
**Q-Chem** uses specially-developed cutoff procedures which permits evaluation of
the XC energy and potential in only ${\cal{O}}({N})$ work for large molecules. This is
a significant improvement over the formal ${\cal{O}}({N^{3}})$ scaling of the XC cost,
and is critical in enabling DFT calculations to be carried out on very large
systems. In rare cases, however, the default cutoff scheme can be too
aggressive, eliminating contributions that should be retained; this is almost
always signaled by an inaccurate numerical density integral. An example of when
this could occur is in calculating anions with multiple sets of diffuse
functions in the basis. A remedy may be to increase the size of the quadrature
grid.
