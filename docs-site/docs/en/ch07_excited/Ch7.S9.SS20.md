---
title: "7.9.20 Non-Hartree–Fock Orbitals in EOM Calculations"
---

## 7.9.20 Non-Hartree–Fock Orbitals in EOM Calculations

(July 4, 2026)

In cases of problematic open-shell references, *e.g.*, strongly spin-contaminated
doublet, triplet or quartet states, one may choose to use DFT orbitals. This
can be achieved by first doing DFT calculation and then
reading the orbitals and turning Hartree–Fock off (by setting SCF_GUESS = READ and
MAX_SCF_CYCLES = 0 in the CCMAN or CCMAN2 job).
In CCMAN, a more convenient way is just to
specify EXCHANGE, *e.g.*, if EXCHANGE = B3LYP, B3LYP orbitals will
be computed and used. See Section [6.15](../ch06_correlation/sec_AltOrbs.md) for additional discussion of alternative
orbital choices in correlated wave function calculations.

**Note: 

Using non-HF exchange in CCMAN2 is not possible.
**
