---
title: "9.11.2 Finding Electronic Resonance States of Temporary Anions"
---

## 9.11.2 Finding Electronic Resonance States of Temporary Anions

(July 4, 2026)

We limit our discussion here to the HF method, but the general principles outlined also applies to higher level methods.

1. 1.

The correct description of the electronic state of temporary anions usually requires the use of extra diffuse
functions in the basis set. You may thus consider having enough extra diffuse functions in your basis set.
2. 2.

It is best you use the core Hamiltonian as guess for the CAP-HF SCF procedure
(*i.e.*, set SCF_GUESS = CORE).
3. 3.

For CAP calculations, **Q-Chem** first solves the SCF problem using the old SCF drivers in **Q-Chem**;
the solution is then used as the starting point for the CAP part of the calculation.
This preliminary SCF solution usually
leads to wrong CAP-HF solutions. You may avoid this issue by setting
SKIP_OLD_SCFMAN = TRUE in *$rem*.
See Example [9.11.3](ex_CAP_HF_energy_decomp.md).
4. 4.

Make sure the CAP contribution to the real and imaginary parts of the SCF solution found is negligible.
You can get these CAP contributions by asking for an energy decomposition of the complex energy by setting
CS_SCF_FINAL_PRINT = 1 in *$rem*.
An alternative is to look at how close the imaginary (and real) parts of the CAP-HF energy and the corrected CAP-HF
energy are; the ratio of the imaginary parts should be close to unity. See Example [9.11.3](ex_CAP_HF_energy_decomp.md).

For CAP-HF calculations, set the *$rem* variable CS_STRICT = TRUE
to print out the correct properties (*e.g.*, Mulliken charges and multipole moments) of the solution.
See Example [9.11.3](ex_CAP_HF_energy_decomp.md).
