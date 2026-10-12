---
title: "5.3.4 Correlation Functionals"
---

## 5.3.4 Correlation Functionals

(July 4, 2026)

!!! note "Note"
    All correlation functionals in this section can be invoked using the
    *$rem* variable CORRELATION. Popular and/or recommended
    functionals within each class are listed first and indicated in bold. The rest
    are in alphabetical order.


- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

**PW92**: Perdew-Wang parameterization of the LSDA correlation energy from 1992[[1074]](../bib_references/bib.md#bib1110)
- $\bullet$

**VWN5** (VWN): Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #5[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

srVWN: Short-range version of the VWN correlation functional by Toulouse and coworkers[[1366]](../bib_references/bib.md#bib1426)
- $\bullet$

Liu-Parr: Liu-Parr $\rho^{1/3}$ model from the functional expansion formulation[[848]](../bib_references/bib.md#bib870)
- $\bullet$

PK09: Proynov-Kong parameterization of the LSDA correlation energy from 2009[[1127]](../bib_references/bib.md#bib1176)
- $\bullet$

PW92RPA: Perdew-Wang parameterization of the LSDA correlation energy from 1992 with RPA values[[1074]](../bib_references/bib.md#bib1110)
- $\bullet$

srPW92: Short-range version of the PW92 correlation functional by Paziani and coworkers[[1056]](../bib_references/bib.md#bib1101)
- $\bullet$

PZ81: Perdew-Zunger parameterization of the LSDA correlation energy from 1981[[1075]](../bib_references/bib.md#bib1107)
- $\bullet$

VWN1: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #1[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN1RPA: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #1 with RPA values[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN2: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #2[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN3: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #3[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN4: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #4[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

Wigner:Wigner correlation functional (simplification of LYP)[[1467]](../bib_references/bib.md#bib1530)
- $\circ$

Generalized Gradient Approximation (GGA)

- $\bullet$

BOP: “one-parameter progressive” correlation functional with parameters appropriate for B88 exchange[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

**PBE**: Perdew, Burke, and Ernzerhof correlation functional[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

**LYP**: Lee-Yang-Parr opposite-spin correlation functional[[780]](../bib_references/bib.md#bib813)
- $\bullet$

P86: Perdew-Wang correlation functional from 1986 based on the PZ81 LSDA functional[[1076]](../bib_references/bib.md#bib1109)
- $\bullet$

P86VWN5: Perdew-Wang correlation functional from 1986 based on the VWN5 LSDA functional[[1076]](../bib_references/bib.md#bib1109)
- $\bullet$

PBEloc: PBE correlation functional with a modified beta term by Della Sala and coworkers
- $\bullet$

PBEBOP: “one-parameter progressive” correlation functional with parameters appropriate for PBE exchange[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

PBEsol: PBE correlation functional modified for solids[[1067]](../bib_references/bib.md#bib1118)
- $\bullet$

srPBE: Short-range version of the PBE correlation functional by Goll and coworkers[[469]](../bib_references/bib.md#bib481)
- $\bullet$

PW91: Perdew-Wang correlation functional from 1991[[1063]](../bib_references/bib.md#bib1111)
- $\bullet$

regTPSS: Slight modification of the PBE correlation functional (also called vPBEc)[[1191]](../bib_references/bib.md#bib1246)
- $\circ$

Meta-Generalized Gradient Approximation (meta-GGA)

- $\bullet$

**TPSS**:Tao, Perdew, Staroverov, and Scuseria correlation functional[[1344]](../bib_references/bib.md#bib1402)
- $\bullet$

**revTPSS**: Revised version of the TPSS correlation functional[[1066]](../bib_references/bib.md#bib1120)
- $\bullet$

B95: Becke’s two-parameter correlation functional from 1995[[98]](../bib_references/bib.md#bib80)
- $\bullet$

oTPSS: TPSS correlation functional with 2 refit parameters (for use with oTPSS exchange) by Grimme and coworkers[[462]](../bib_references/bib.md#bib475)
- $\bullet$

PK06: Proynov-Kong “tLap” functional with $\tau$ and Laplacian dependence[[1125]](../bib_references/bib.md#bib1173)
- $\bullet$

PKZB: Perdew, Kurth, Zupan, and Blaha correlation functional[[1064]](../bib_references/bib.md#bib1114)
- $\bullet$

SCAN: Strongly Constrained and Appropriately Normed correlation functional[[1327]](../bib_references/bib.md#bib1387)
- $\bullet$

rSCAN: Regularized SCAN correlation[[83]](../bib_references/bib.md#bib68)
- $\bullet$

r++SCAN: Regularized SCAN with uniform density limit and coordinate scaling behavior[[421]](../bib_references/bib.md#bib430)
- $\bullet$

r2SCAN: Re-Regularized SCAN correlation[[419]](../bib_references/bib.md#bib428)
- $\bullet$

revSCAN: Revised SCAN correlation[[944]](../bib_references/bib.md#bib984)
- $\bullet$

TM: Tao-Mo correlation functional, representing a minor modification to the TPSS correlation functional[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

revTM: Revised TM correlation[[628]](../bib_references/bib.md#bib648)
- $\bullet$

rregTM: Revised regularized TM correlation[[625]](../bib_references/bib.md#bib649)
- $\bullet$

TPSSloc: The TPSS correlation functional with the PBE component replaced by the PBEloc correlation functional
