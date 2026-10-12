---
title: "8.6.1 Overview"
---

## 8.6.1 Overview

(July 4, 2026)

There are several types of calculation that can be performed within **Q-Chem**
using *two* atomic orbital basis sets instead of just one as we have been
assuming in this chapter so far. Such calculations are said to involve
*dual* basis sets. Typically iterations are performed in a smaller,
primary, basis, which is specified by the *$rem* keyword BASIS2.
Examples of calculations that can be performed using dual basis sets include:

- An improved initial guess for an SCF calculation in the large basis. See
Section [4.4.5](../ch04_scf/sect_projection.md).
- Dual basis self-consistent field calculations (Hartree-Fock and density
functional theory). See discussion in Section [4.7](../ch04_scf/sect_dualbasis.md).
- Density functional perturbative corrections by “triple jumping”.
See Section [4.8](../ch04_scf/sect_HFPC.md).
- Dual basis MP2 calculations. See discussion in Section [6.6.2](../ch06_correlation/sect_rimp2.md).

### `BASIS2`

> **Defines the (small) second basis set.**
>
> * **Type**: `STRING`
> * **Default**: `No default for the second basis set.`
> * **Options**:
>     * `Symbol`: Use standard basis sets as for BASIS .
>     * `BASIS2_GEN`: General
>     * `BASIS2_MIXED`: Mixed
> * **Recommendation**: should be smaller than BASIS . There is little advantage to using a basis larger than a minimal basis when is used for initial guess purposes. Larger, standardized options are available for dual-basis calculations as discussed in Section 4.7 and summarized in Table 4.2 .

In addition to built-in basis sets for BASIS2, it is also possible to
enter user-defined second basis sets using an additional *$basis2* input
section, whose syntax generally follows the *$basis* input section documented
above in Section [8.4](sect_userbasis.md).
