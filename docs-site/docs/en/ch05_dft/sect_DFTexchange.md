---
title: "5.3.3 Exchange Functionals"
---

## 5.3.3 Exchange Functionals

(July 4, 2026)

!!! note "Note"
    All exchange functionals in this section can be invoked using the *$rem*
    variable EXCHANGE. Popular and/or recommended functionals within
    each class are listed first and indicated in bold. The rest are in alphabetical order.


- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

**Slater**: Slater-Dirac exchange functional (X$\alpha$ method with $\alpha=2/3$)[[329]](../bib_references/bib.md#bib333)
- $\bullet$

SR_LSDA (BNL): Short-range version of the Slater-Dirac exchange functional[[444]](../bib_references/bib.md#bib464)
- $\circ$

Generalized Gradient Approximation (GGA)

- $\bullet$

**PBE**: Perdew, Burke, and Ernzerhof exchange functional[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

**B88**: Becke exchange functional from 1988[[95]](../bib_references/bib.md#bib74)
- $\bullet$

**revPBE**: Zhang and Yang one-parameter modification of the PBE exchange functional[[1552]](../bib_references/bib.md#bib1606)
- $\bullet$

AK13: Armiento-Kümmel exchange functional from 2013[[52]](../bib_references/bib.md#bib35)
- $\bullet$

B86: Becke exchange functional (X$\alpha\beta\gamma$) from 1986[[92]](../bib_references/bib.md#bib71)
- $\bullet$

G96: Gill exchange functional from 1996[[453]](../bib_references/bib.md#bib463)
- $\bullet$

mB86: Becke “modified gradient correction” exchange functional from 1986[[93]](../bib_references/bib.md#bib72)
- $\bullet$

mPW91: modified version (Adamo and Barone) of the 1991 Perdew-Wang exchange functional[[18]](../bib_references/bib.md#bib2)
- $\bullet$

muB88 ($\mu$B88): Short-range version of the B88 exchange functional by Hirao and coworkers[[609]](../bib_references/bib.md#bib632)
- $\bullet$

muPBE ($\mu$PBE): Short-range version of the PBE exchange functional by Hirao and coworkers[[609]](../bib_references/bib.md#bib632)
- $\bullet$

srPBE: Short-range version of the PBE exchange functional by Goll and coworkers[[469]](../bib_references/bib.md#bib481)
- $\bullet$

optB88: Refit version of the original B88 exchange functional (for use with vdW-DF-04) by Michaelides and coworkers[[696]](../bib_references/bib.md#bib728)
- $\bullet$

OPTX: Two-parameter exchange functional by Handy and Cohen[[517]](../bib_references/bib.md#bib531)
- $\bullet$

PBEsol: PBE exchange functional modified for solids[[1067]](../bib_references/bib.md#bib1118)
- $\bullet$

PW86: Perdew-Wang exchange functional from 1986[[1073]](../bib_references/bib.md#bib1108)
- $\bullet$

PW91: Perdew-Wang exchange functional from 1991[[1063]](../bib_references/bib.md#bib1111)
- $\bullet$

RPBE: Hammer, Hansen, and Norskov exchange functional (modification of PBE)[[514]](../bib_references/bib.md#bib527)
- $\bullet$

rPW86: Revised version (Murray *et al.*) of the 1986 Perdew-Wang exchange functional[[969]](../bib_references/bib.md#bib1010)
- $\bullet$

SOGGA: Second-order GGA functional by Zhao and Truhlar[[1567]](../bib_references/bib.md#bib1626)
- $\bullet$

wPBE ($\omega$PBE): Henderson *et al.* model for the PBE GGA short-range exchange hole[[554]](../bib_references/bib.md#bib569)
- $\circ$

Meta-Generalized Gradient Approximation (meta-GGA)

- $\bullet$

**TPSS**: Tao, Perdew, Staroverov, and Scuseria exchange functional[[1344]](../bib_references/bib.md#bib1402)
- $\bullet$

**revTPSS**: Revised version of the TPSS exchange functional[[1066]](../bib_references/bib.md#bib1120)
- $\bullet$

BLOC: Minor modification of the TPSS exchange functional that works best with TPSSloc correlation
(both by Della Sala and coworkers)[[264]](../bib_references/bib.md#bib265)
- $\bullet$

modTPSS: One-parameter version of the TPSS exchange functional[[1069]](../bib_references/bib.md#bib1117)
- $\bullet$

oTPSS: TPSS exchange functional with 5 refit parameters (for use with oTPSS correlation)
by Grimme and coworkers[[462]](../bib_references/bib.md#bib475)
- $\bullet$

PBE-GX: First exchange functional based on a finite uniform electron gas (rather than an infinite UEG)
by Pierre-François Loos[[860]](../bib_references/bib.md#bib894)
- $\bullet$

PKZB: Perdew, Kurth, Zupan, and Blaha exchange functional[[1064]](../bib_references/bib.md#bib1114)
- $\bullet$

regTPSS: Regularized (fixed order of limits issue) version of the TPSS exchange functional[[1191]](../bib_references/bib.md#bib1246)
- $\bullet$

SCAN: Strongly Constrained and Appropriately Normed exchange functional[[1327]](../bib_references/bib.md#bib1387)
- $\bullet$

rSCAN: Regularized SCAN exchange[[83]](../bib_references/bib.md#bib68)
- $\bullet$

r++SCAN: Regularized SCAN with uniform density limit and coordinate scaling behavior[[421]](../bib_references/bib.md#bib430)
- $\bullet$

r2SCAN: Re-Regularized SCAN exchange[[419]](../bib_references/bib.md#bib428)
- $\bullet$

r4SCAN: Regularized SCAN with exact constraints obeyed by SCAN[[421]](../bib_references/bib.md#bib430)
- $\bullet$

revSCAN: Revised SCAN exchange[[944]](../bib_references/bib.md#bib984)
- $\bullet$

TM: Tao-Mo exchange functional derived via an accurate modeling of the conventional exchange hole[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

regTM: Regularized TM exchange[[1045]](../bib_references/bib.md#bib1090)
- $\bullet$

revTM: Revised TM exchange[[628]](../bib_references/bib.md#bib648)
- $\bullet$

TASK: TASK exchange functional[[53]](../bib_references/bib.md#bib36)
- $\bullet$

mTASK: Modified TASK exchange functional[[989]](../bib_references/bib.md#bib1031)
