---
title: "5.3.5 Exchange-Correlation Functionals"
---

## 5.3.5 Exchange-Correlation Functionals

(July 4, 2026)

**Note: 

All exchange-correlation functionals in this section can be invoked using
the *$rem* variable METHOD. For backwards compatibility, all of the
exchange-correlation functionals *except* for the ones marked with an
asterisk can be used with the *$rem* variable EXCHANGE. Popular
and/or recommended functionals within each class are listed first and
indicated in bold. The rest are in alphabetical order.
**

- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

**SPW92***: Slater LSDA exchange + PW92 LSDA correlation
- $\bullet$

LDA: Slater LSDA exchange + VWN5 LSDA correlation
- $\bullet$

SVWN5*: Slater LSDA exchange + VWN5 LSDA correlation
- $\circ$

Generalized Gradient Approximation (GGA)

- $\bullet$

**B97-D3(0)**: B97-D with a fitted DFT-D3(0) tail instead of the original DFT-D2 tail[[486]](../bib_references/bib.md#bib504)
- $\bullet$

**B97-D**: 9-parameter dispersion-corrected (DFT-D2) functional by Grimme[[494]](../bib_references/bib.md#bib502)
- $\bullet$

**PBE***: PBE GGA exchange + PBE GGA correlation
- $\bullet$

**BLYP***: B88 GGA exchange + LYP GGA correlation
- $\bullet$

**revPBE***: revPBE GGA exchange + PBE GGA correlation
- $\bullet$

BEEF-vdW: 31-parameter semi-empirical exchange functional developed via a Bayesian error estimation
framework paired with PBE correlation and vdW-DF-10 NLC[[1449]](../bib_references/bib.md#bib1510)
- $\bullet$

BOP: B88 GGA exchange + BOP “one-parameter progressive” GGA correlation[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

BP86*: B88 GGA exchange + P86 GGA correlation
- $\bullet$

BP86VWN*: B88 GGA exchange + P86VWN5 GGA correlation
- $\bullet$

BPBE*: B88 GGA exchange + PBE GGA correlation
- $\bullet$

EDF1: Modification of BLYP to give good performance in the 6-31+G* basis set[[25]](../bib_references/bib.md#bib9)
- $\bullet$

EDF2: Modification of B3LYP to give good performance in the cc-pVTZ basis set for frequencies[[828]](../bib_references/bib.md#bib864)
- $\bullet$

GAM: 21-parameter non-separable gradient approximation functional by Truhlar and coworkers[[1534]](../bib_references/bib.md#bib1596)
- $\bullet$

HCTH93 (HCTH/93): 15-parameter functional trained on 93 systems by Handy and coworkers[[516]](../bib_references/bib.md#bib530)
- $\bullet$

HCTH120 (HCTH/120): 15-parameter functional trained on 120 systems by Boese *et al.*[[137]](../bib_references/bib.md#bib127)
- $\bullet$

HCTH147 (HCTH/147): 15-parameter functional trained on 147 systems by Boese *et al.*[[137]](../bib_references/bib.md#bib127)
- $\bullet$

HCTH407 (HCTH/407): 15-parameter functional trained on 407 systems by Boese and Handy[[138]](../bib_references/bib.md#bib128)
- $\bullet$

HLE16 – HCTH/407 exchange functional enhanced by a factor of 1.25 + HCTH/407 correlation functional
enhanced by a factor of 0.5[[1400]](../bib_references/bib.md#bib1460)
- $\bullet$

KT1: GGA functional designed specifically for shielding constant calculations[[674]](../bib_references/bib.md#bib699)
- $\bullet$

KT2: GGA functional designed specifically for shielding constant calculations[[674]](../bib_references/bib.md#bib699)
- $\bullet$

KT3: GGA functional with improved results for main-group nuclear magnetic resonance shielding constants[[675]](../bib_references/bib.md#bib700)
- $\bullet$

mPW91*: mPW91 GGA exchange + PW91 GGA correlation
- $\bullet$

N12: 21-parameter non-separable gradient approximation functional by Peverati and Truhlar[[1086]](../bib_references/bib.md#bib1132)
- $\bullet$

OLYP*: OPTX GGA exchange + LYP GGA correlation
- $\bullet$

PBEOP: PBE GGA exchange + PBEOP “one-parameter progressive” GGA correlation[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

PBEsol*: PBEsol GGA exchange + PBEsol GGA correlation
- $\bullet$

PW91*: PW91 GGA exchange + PW91 GGA correlation
- $\bullet$

RPBE*: RPBE GGA exchange + PBE GGA correlation
- $\bullet$

rVV10*: rPW86 GGA exchange + PBE GGA correlation + rVV10 non-local correlation[[1192]](../bib_references/bib.md#bib1247)
- $\bullet$

SOGGA*: SOGGA GGA exchange + PBE GGA correlation
- $\bullet$

SOGGA11: 20-parameter functional by Peverati, Zhao, and Truhlar[[1089]](../bib_references/bib.md#bib1128)
- $\bullet$

VV10: rPW86 GGA exchange + PBE GGA correlation + VV10 non-local correlation[[1416]](../bib_references/bib.md#bib1477)
- $\circ$

Meta-Generalized Gradient Approximation (meta-GGA)

- $\bullet$

**B97M-V**: 12-parameter combinatorially-optimized, dispersion-corrected (VV10) functional by
Mardirossian and Head-Gordon[[904]](../bib_references/bib.md#bib938)
- $\bullet$

**B97M-rV***: B97M-V density functional with the VV10 NLC functional replaced by the rVV10 NLC
functional[[907]](../bib_references/bib.md#bib940)
- $\bullet$

**M06-L**: 34-parameter functional by Zhao and Truhlar[[1565]](../bib_references/bib.md#bib1624)
- $\bullet$

**TPSS***: TPSS meta-GGA exchange + TPSS meta-GGA correlation
- $\bullet$

**revTPSS***: revTPSS meta-GGA exchange + revTPSS meta-GGA correlation
- $\bullet$

B97MV-D3s(BJ): B97M-V density functional with the VV10 NLC functional replaced by DFT-D3s(BJ) (s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959)
- $\bullet$

B97MV-D4: B97M-V density functional with the VV10 NLC functional replaced by DFT-D4 (s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487)
- $\bullet$

BLOC*: BLOC meta-GGA exchange + TPSSloc meta-GGA correlation
- $\bullet$

M11-L: 44-parameter dual-range functional by Peverati and Truhlar[[1085]](../bib_references/bib.md#bib1131)
- $\bullet$

mBEEF: 64-parameter exchange functional paired with the PBEsol correlation functional[[1448]](../bib_references/bib.md#bib1511)
- $\bullet$

MGGA_MS0: MGGA_MS0 meta-GGA exchange + regTPSS GGA correlation[[1328]](../bib_references/bib.md#bib1384)
- $\bullet$

MGGA_MS1: MGGA_MS1 meta-GGA exchange + regTPSS GGA correlation[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MS2: MGGA_MS2 meta-GGA exchange + regTPSS GGA correlation[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MVS: MGGA_MVS meta-GGA exchange + regTPSS GGA correlation[[1326]](../bib_references/bib.md#bib1386)
- $\bullet$

MN12-L: 58-parameter meta-nonseparable gradient approximation functional by Peverati and Truhlar[[1087]](../bib_references/bib.md#bib1133)
- $\bullet$

MN15-L: 58-parameter meta-nonseparable gradient approximation functional by Yu, He, and Truhlar[[1533]](../bib_references/bib.md#bib1598)
- $\bullet$

oTPSS*: oTPSS meta-GGA exchange + oTPSS meta-GGA correlation
- $\bullet$

PKZB*: PKZB meta-GGA exchange + PKZB meta-GGA correlation
- $\bullet$

revM06-L: 31-parameter revised M06-L functional
- $\bullet$

SCAN*: SCAN meta-GGA exchange + SCAN meta-GGA correlation
- $\bullet$

rSCAN: rSCAN exchange + rSCAN correltaion
- $\bullet$

r++SCAN: r++SCAN exchange + r++SCAN correlation
- $\bullet$

r2SCAN: r2SCAN exchange + r2SCAN correlation
- $\bullet$

r4SCAN: r4SCAN exchange + r2SCAN correlation
- $\bullet$

revSCAN: revSCAN exchange + revSCAN correlation
- $\bullet$

t-HCTH ($\tau$-HCTH): 16-parameter functional by Boese and Handy[[139]](../bib_references/bib.md#bib129)
- $\bullet$

TM*: TM meta-GGA exchange + TM meta-GGA correlation[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

revTM: revTM exchange + revTM correlation
- $\bullet$

regTM: regTM exchange + regTPSS correlation
- $\bullet$

rregTM: regTM exchange + rregTM correlation
- $\bullet$

TASK: TASK exchange + PW92 correlation
- $\bullet$

mTASK: mTASK exchange + PW92 correlation
- $\bullet$

VSXC: 21-parameter functional by Voorhis and Scuseria[[1393]](../bib_references/bib.md#bib1448)
- $\circ$

Global Hybrid Generalized Gradient Approximation (GH GGA)

- $\bullet$

**B3LYP**: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange + 19% VWN1RPA
LSDA correlation + 81% LYP GGA correlation[[96]](../bib_references/bib.md#bib78)
- $\bullet$

**PBE0**: 25% HF exchange + 75% PBE GGA exchange + PBE GGA correlation[[19]](../bib_references/bib.md#bib3)
- $\bullet$

**revPBE0**: 25% HF exchange + 75% revPBE GGA exchange + PBE GGA correlation
- $\bullet$

**B97**: Becke’s original 10-parameter density functional with 19.43% HF exchange[[99]](../bib_references/bib.md#bib81)
- $\bullet$

B1LYP: 25% HF exchange + 75% B88 GGA exchange + LYP GGA correlation[[17]](../bib_references/bib.md#bib1)
- $\bullet$

B1PW91: 25% HF exchange + 75% B88 GGA exchange + PW91 GGA correlation[[17]](../bib_references/bib.md#bib1)
- $\bullet$

B3LYP5: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange + 19% VWN5 LSDA
correlation + 81% LYP GGA correlation[[96]](../bib_references/bib.md#bib78)
- $\bullet$

B3P86: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange+ 19% VWN1RPA LSDA
correlation + 81% P86 GGA correlation
- $\bullet$

B3PW91: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange+ 19% PW92
LSDA correlation + 81% PW91 GGA correlation[[96]](../bib_references/bib.md#bib78)
- $\bullet$

B5050LYP: 50% HF exchange + 8% Slater LSDA exchange + 42% B88 GGA exchange + 19% VWN5
LSDA correlation + 81% LYP GGA correlation[[1239]](../bib_references/bib.md#bib1294)
- $\bullet$

B97-1: Self-consistent parameterization of Becke’s B97 density functional with 21% HF exchange[[516]](../bib_references/bib.md#bib530)
- $\bullet$

B97-2: Re-parameterization of B97 by Tozer and coworkers with 21% HF exchange[[1477]](../bib_references/bib.md#bib1539)
- $\bullet$

B97-3: 16-parameter version of B97 by Keal and Tozer with $\approx$ 26.93% HF exchange[[676]](../bib_references/bib.md#bib701)
- $\bullet$

B97-K: Re-parameterization of B97 for kinetics by Boese and Martin with 42% HF exchange[[140]](../bib_references/bib.md#bib130)
- $\bullet$

BHHLYP: 50% HF exchange + 50% B88 GGA exchange + LYP GGA correlation, sometimes called BH&H-LYP[[484]](../bib_references/bib.md#bib496)
- $\bullet$

HFLYP*: 100% HF exchange + LYP GGA correlation
- $\bullet$

MPW1K: 42.8% HF exchange + 57.2% mPW91 GGA exchange + PW91 GGA correlation[[865]](../bib_references/bib.md#bib900)
- $\bullet$

MPW1LYP: 25% HF exchange + 75% mPW91 GGA exchange + LYP GGA correlation[[18]](../bib_references/bib.md#bib2)
- $\bullet$

MPW1PBE: 25% HF exchange + 75% mPW91 GGA exchange + PBE GGA correlation[[18]](../bib_references/bib.md#bib2)
- $\bullet$

MPW1PW91: 25% HF exchange + 75% mPW91 GGA exchange + PW91 GGA correlation[[18]](../bib_references/bib.md#bib2)
- $\bullet$

O3LYP: 11.61% HF exchange + $\approx$ 7.1% Slater LSDA exchange + 81.33% OPTX GGA exchange + 19%
VWN5 LSDA correlation + 81% LYP GGA correlation[[586]](../bib_references/bib.md#bib609)
- $\bullet$

PBEh-3c: Low-cost composite scheme of Grimme and coworkers for use with the def2-mSVP basis set only[[487]](../bib_references/bib.md#bib508)
- $\bullet$

PBE50: 50% HF exchange + 50% PBE GGA exchange + PBE GGA correlation[[114]](../bib_references/bib.md#bib101)
- $\bullet$

SOGGA11-X: 21-parameter functional with 40.15% HF exchange by Peverati and Truhlar[[1083]](../bib_references/bib.md#bib1129)
- $\bullet$

WC04: Hybrid density functional optimized for the computation of ${}^{13}$C chemical shifts[[1469]](../bib_references/bib.md#bib285)
- $\bullet$

WP04: Hybrid density functional optimized for the computation of ${}^{1}$H chemical shifts[[1469]](../bib_references/bib.md#bib285)
- $\bullet$

X3LYP: 21.8% HF exchange + 7.3% Slater LSDA exchange + $\approx$ 54.24% B88 GGA exchange + $\approx$ 16.66%
PW91 GGA exchange + 12.9% VWN1RPA LSDA correlation + 87.1% LYP GGA correlation[[1506]](../bib_references/bib.md#bib1567)
- $\circ$

Global Hybrid Meta-Generalized Gradient Approximation (GH meta-GGA)

- $\bullet$

**CF22D**: global functional with 46.2806% HF exchange
and an empirically damped dispersion term, developed using a supervised learning protocol by
Truhlar, Wang, He, and coworkers[[850]](../bib_references/bib.md#bib884)
- $\bullet$

**M06-2X**: 29-parameter functional with 54% HF exchange by Zhao and Truhlar[[1569]](../bib_references/bib.md#bib1628)
- $\bullet$

**TPSSh**: 10% HF exchange + 90% TPSS meta-GGA exchange + TPSS meta-GGA correlation[[1294]](../bib_references/bib.md#bib1350)
- $\bullet$

**revTPSSh**: 10% HF exchange + 90% revTPSS meta-GGA exchange + revTPSS meta-GGA correlation[[286]](../bib_references/bib.md#bib290)
- $\bullet$

M08-HX: 47-parameter functional with 52.23% HF exchange by Zhao and Truhlar[[1568]](../bib_references/bib.md#bib1627)
- $\bullet$

B1B95: 28% HF exchange + 72% B88 GGA exchange + B95 meta-GGA correlation[[98]](../bib_references/bib.md#bib80)
- $\bullet$

B3TLAP: 17.13% HF exchange + 9.66% Slater LSDA exchange + 72.6% B88 GGA exchange + PK06 meta-GGA
correlation[[1125]](../bib_references/bib.md#bib1173)
- $\bullet$

BB1K: 42% HF exchange + 58% B88 GGA exchange + B95 meta-GGA correlation[[1560]](../bib_references/bib.md#bib1618)
- $\bullet$

BMK: Boese-Martin functional for kinetics with 42% HF exchange[[140]](../bib_references/bib.md#bib130)
- $\bullet$

dlDF: Dispersion-less density functional (based on the M05-2X functional form) by Szalewicz and coworkers[[1078]](../bib_references/bib.md#bib1123)
- $\bullet$

M05: 22-parameter functional with 28% HF exchange by Zhao, Schultz, and Truhlar[[1561]](../bib_references/bib.md#bib1622)
- $\bullet$

M05-2X: 19-parameter functional with 56% HF exchange by Zhao, Schultz, and Truhlar[[1562]](../bib_references/bib.md#bib1623)
- $\bullet$

M06: 33-parameter functional with 27% HF exchange by Zhao and Truhlar[[1569]](../bib_references/bib.md#bib1628)
- $\bullet$

M06-HF: 32-parameter functional with 100% HF exchange by Zhao and Truhlar[[1566]](../bib_references/bib.md#bib1625)
- $\bullet$

M08-SO: 44-parameter functional with 56.79% HF exchange by Zhao and Truhlar[[1568]](../bib_references/bib.md#bib1627)
- $\bullet$

MGGA_MS2h: 9% HF exchange + 91 % MGGA_MS2 meta-GGA exchange + regTPSS GGA correlation[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MVSh: 25% HF exchange + 75 % MGGA_MVS meta-GGA exchange + regTPSS GGA correlation[[1326]](../bib_references/bib.md#bib1386)
- $\bullet$

MN15: 59-parameter functional with 44% HF exchange by Truhlar and coworkers[[1532]](../bib_references/bib.md#bib1597)
- $\bullet$

MPW1B95: 31% HF exchange + 69% mPW91 GGA exchange + B95 meta-GGA correlation[[1563]](../bib_references/bib.md#bib1619)
- $\bullet$

MPWB1K: 44% HF exchange + 56% mPW91 GGA exchange + B95 meta-GGA correlation[[1563]](../bib_references/bib.md#bib1619)
- $\bullet$

PW6B95: 6-parameter combination of 28 % HF exchange, 72 % optimized PW91 GGA exchange, and re-optimized
B95 meta-GGA correlation by Zhao and Truhlar[[1564]](../bib_references/bib.md#bib1621)
- $\bullet$

PWB6K: 6-parameter combination of 46 % HF exchange, 54 % optimized PW91 GGA exchange, and re-optimized
B95 meta-GGA correlation by Zhao and Truhlar[[1564]](../bib_references/bib.md#bib1621)
- $\bullet$

revM06: 32-parameter functional with 40.41% HF exchange[[1428]](../bib_references/bib.md#bib1489)
- $\bullet$

r2SCANh: 10% HF exchange + 90% r2SCAN meta-GGA exchange + r2SCAN meta-GGA correlation[[172]](../bib_references/bib.md#bib166)
- $\bullet$

r2SCAN0: 25% HF exchange + 75% r2SCAN meta-GGA exchange + r2SCAN meta-GGA correlation[[172]](../bib_references/bib.md#bib166)
- $\bullet$

r2SCAN50: 50% HF exchange + 50% r2SCAN meta-GGA exchange + r2SCAN meta-GGA correlation[[172]](../bib_references/bib.md#bib166)
- $\bullet$

SCAN0: 25% HF exchange + 75% SCAN meta-GGA exchange + SCAN meta-GGA correlation[[602]](../bib_references/bib.md#bib625)
- $\bullet$

t-HCTHh ($\tau$-HCTHh): 17-parameter functional with 15% HF exchange by Boese and Handy[[139]](../bib_references/bib.md#bib129)
- $\bullet$

TPSS0: 25% HF exchange + 75% TPSS meta-GGA exchange + TPSS meta-GGA correlation[[492]](../bib_references/bib.md#bib500)
- $\circ$

Range-Separated Hybrid Generalized Gradient Approximation (RSH GGA)

- $\bullet$

**wB97X-V** ($\omega$B97X-V): 10-parameter combinatorially-optimized, dispersion-corrected (VV10)
functional with 16.7% SR HF exchange, 100% LR HF exchange, and $\omega=0.3$[[903]](../bib_references/bib.md#bib937)
- $\bullet$

wB97XV-D3s(BJ) ($\omega$B97XV-D3s(BJ)): $\omega$B97X-V with the VV10 NLC functional replaced by DFT-D3s(BJ) (s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959)
- $\bullet$

wB97XV-D4 ($\omega$B97XV-D4): $\omega$B97X-V with the VV10 NLC functional replaced by DFT-D4 (s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487)
- $\bullet$

wB97X-D ($\omega$B97X-D): 15-parameter dispersion-corrected (DFT-CHG) functional with
$\approx$ 22.2% SR HF exchange, 100% LR HF exchange, and $\omega=0.2$[[224]](../bib_references/bib.md#bib219)
- $\bullet$

wB97X-D3 ($\omega$B97X-D3): 16-parameter dispersion-corrected (DFT-D3(0)) functional with
$\approx$ 19.57% SR HF exchange, 100% LR HF exchange, and $\omega=0.25$[[832]](../bib_references/bib.md#bib225)
- $\bullet$

KS-$\omega$B97X-D4 (see Example [5.6.3](ex_ks-wb97xd4.md) for the usage): 10-parameter combinatorially-optimized, dispersion-corrected (D4) functional with $\approx$ 18.7% SR HF exchange, 100% LR HF exchange, and $\omega=0.3$[[815]](../bib_references/bib.md#bib858)
- $\bullet$

CAM-B3LYP: Coulomb-attenuating method functional by Handy and coworkers[[1512]](../bib_references/bib.md#bib1575)
- $\bullet$

CAM-QTP00: Re-parameterized CAM-B3LYP designed to satisfy the IP-theorem for all occupied orbitals
of the water molecule[[1399]](../bib_references/bib.md#bib1459)
- $\bullet$

CAM-QTP01: Re-parameterized CAM-B3LYP optimized to satisfy the valence IPs of the water molecule,
34 excitation states, and G2-1 atomization energies[[643]](../bib_references/bib.md#bib667)
- $\bullet$

HSE-HJS: Screened-exchange “HSE06” functional with 25% SR HF exchange, 0% LR HF exchange, and $\omega$=0.11, using the updated HJS PBE exchange hole model[[721]](../bib_references/bib.md#bib753)
- $\bullet$

LC-rVV10*: LC-VV10 density functional with the VV10 NLC functional replaced by the rVV10 NLC functional[[907]](../bib_references/bib.md#bib940)
- $\bullet$

LC-VV10: 0% SR HF exchange + 100% LR HF exchange + $\omega$PBE GGA exchange + PBE GGA correlation
+ VV10 non-local correlation ($\omega$=0.45)[[1416]](../bib_references/bib.md#bib1477)
- $\bullet$

LC-wPBE08 (LC-$\omega$PBE08): 0% SR HF exchange + 100% LR HF exchange + $\omega$PBE GGA exchange +
PBE GGA correlation ($\omega$=0.45)[[1446]](../bib_references/bib.md#bib1508)
- $\bullet$

LRC-BOP (LRC-$\mu$BOP): 0% SR HF exchange + 100% LR HF exchange + $\mu$B88 GGA exchange +
BOP GGA correlation ($\omega$=0.47)[[1285]](../bib_references/bib.md#bib1337)
- $\bullet$

LRC-wPBE (LRC-$\omega$PBE): 0% SR HF exchange + 100% LR HF exchange + $\omega$PBE GGA exchange +
PBE GGA correlation ($\omega$=0.3)[[1177]](../bib_references/bib.md#bib1230)
- $\bullet$

LRC-wPBEh (LRC-$\omega$PBEh): 20% SR HF exchange + 100% LR HF exchange + 80% $\omega$PBE GGA
exchange + PBE GGA correlation ($\omega$=0.2)[[1178]](../bib_references/bib.md#bib1231)
- $\bullet$

N12-SX: 26-parameter non-separable GGA with 25% SR HF exchange, 0% LR HF exchange, and $\omega=0.11$[[1088]](../bib_references/bib.md#bib1134)
- $\bullet$

rCAM-B3LYP: Re-fit CAM-B3LYP with the goal of minimizing many-electron self-interaction error[[260]](../bib_references/bib.md#bib261)
- $\bullet$

wB97 ($\omega$B97): 13-parameter functional with 0% SR HF exchange, 100% LR HF exchange, and $\omega=0.4$[[223]](../bib_references/bib.md#bib218)
- $\bullet$

wB97X ($\omega$B97X): 14-parameter functional with $\approx$ 15.77% SR HF exchange, 100% LR HF exchange,
and $\omega=0.3$[[223]](../bib_references/bib.md#bib218)
- $\bullet$

wB97X-rV* ($\omega$B97X-rV): $\omega$B97X-V density functional with the VV10 NLC functional replaced by the
rVV10 NLC functional[[907]](../bib_references/bib.md#bib940)
- $\circ$

Range-Separated Hybrid Meta-Generalized Gradient Approximation (RSH meta-GGA)

- $\bullet$

**COACH**: Carefully optimized and appropriately constrained hybrid (COACH) functional
in the range-separated hybrid meta-GGA class with 22.878981% SR HF exchange, 100% LR HF exchange, and $\omega=0.27$,
with VV10 $b=5.5$, $C=0.01$, and a three-body D4-ATM correction with $s_{9}=1.0$, $a_{1}=0.215$, and $a_{2}=5.8$
- $\bullet$

**wB97M-V** ($\omega$B97M-V): 12-parameter combinatorially-optimized, dispersion-corrected (VV10)
functional with 15% SR HF exchange, 100% LR HF exchange, and $\omega=0.3$[[905]](../bib_references/bib.md#bib939)
- $\bullet$

wB97MV-D3s(BJ) ($\omega$B97M-D3s(BJ)): wB97M-V with the VV10 NLC functional replaced by DFT-D3s(BJ) (s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959)
- $\bullet$

wB97MV-D4 ($\omega$B97M-D4): wB97M-V with the VV10 NLC functional replaced by DFT-D4 (s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487)
- $\bullet$

GAS22: SyFES-evolved range-separated hybrid meta-GGA functional based on $\omega$B97M-V[[868]](../bib_references/bib.md#bib904)
- $\bullet$

M06-SX: local revM06-L functional with 33.5% SR HF exchange[[1429]](../bib_references/bib.md#bib1490)
- $\bullet$

M11: 40-parameter functional with 42.8% SR HF exchange, 100% LR HF exchange, and $\omega=0.25$[[1084]](../bib_references/bib.md#bib1130)
- $\bullet$

MN12-SX: 58-parameter non-separable meta-GGA with 25% SR HF exchange, 0% LR HF exchange,
and $\omega=0.11$[[1088]](../bib_references/bib.md#bib1134)
- $\bullet$

revM11: 22-parameter functional with 22.5% SR HF exchange, 100% LR HF exchange, and $\omega=0.4$[[1401]](../bib_references/bib.md#bib1461)
- $\bullet$

wB97M-rV* ($\omega$B97X-rV): $\omega$B97M-V density functional with the VV10 NLC functional replaced by the
rVV10 NLC functional[[907]](../bib_references/bib.md#bib940)
- $\bullet$

wM05-D ($\omega$M05-D): 21-parameter dispersion-corrected (DFT-CHG) functional with $\approx$ 36.96%
SR HF exchange, 100% LR HF exchange, and $\omega=0.2$[[833]](../bib_references/bib.md#bib224)
- $\bullet$

wM06-D3 ($\omega$M06-D3): 25-parameter dispersion-corrected [DFT-D3(0)] functional with $\approx$ 27.15%
SR HF exchange, 100% LR HF exchange, and $\omega=0.3$[[832]](../bib_references/bib.md#bib225)
- $\circ$

Double Hybrid Generalized Gradient Approximation (DH GGA)

**Note: 

In order to use the resolution-of-the-identity approximation for the MP2 component, specify an auxiliary basis set with the *$rem* variable AUX_BASIS_CORR
**

- $\bullet$

**wB97X-2(LP)** ($\omega$B97X-2(LP)): 13-parameter functional with $\approx$ 67.88% SR HF exchange,
100% LR HF exchange, $\approx$ 58.16% SS MP2 correlation, $\approx$ 47.80% OS MP2 correlation, and $\omega=0.3$[[225]](../bib_references/bib.md#bib221)
- $\bullet$

**wB97X-2(TQZ)** ($\omega$B97X-2(TQZ)): 13-parameter functional with $\approx$ 63.62% SR HF
exchange, 100% LR HF exchange, $\approx$ 52.93% SS MP2 correlation, $\approx$ 44.71% OS MP2 correlation, and $\omega=0.3$[[225]](../bib_references/bib.md#bib221)
- $\bullet$

**XYG3**: 80.33% HF exchange - 1.4% Slater LSDA exchange + 21.07% B88 GGA exchange + 67.89%
LYP GGA correlation + 32.11% MP2 correlation (evaluated with B3LYP orbitals)[[1551]](../bib_references/bib.md#bib1610)
- $\bullet$

**XYGJ-OS**: 77.31% HF exchange + 33.93% Slater LSDA exchange - 23.21% B88 GGA exchange + 32.68% VWN1RPA LSDA correlation
+ 27.54% LYP GGA correlation + 43.64% OS MP2 correlation (evaluated with B3LYP orbitals)[[1543]](../bib_references/bib.md#bib1611)
- $\bullet$

**XYG-OS5**: 89.28% HF exchange + 22.69% Slater LSDA exchange + 23.09% VWN1RPA LSDA correlation
- 6.35% LYP GGA correlation + 55.74% OS MP2 correlation (evaluated with B3LYP orbitals)[[1544]](../bib_references/bib.md#bib1616)
- $\bullet$

**wDSD72-PBEP86-D4** ($\omega$DSD72-PBEP86-D4): 0.72 HF range-separated exchange ($\omega$ = 0.13 bohr${}^{-1}$) + 0.28 PBE GGA exchange + 0.3425 P86 GGA correlation + 0.6904 OS MP2 correlation + 0.1343 SS MP2 correlation
with DFT-D4 (s6 = 0.4685, s8 = 0, s9 = 1.0, a1 = 0.1884, a2 = 5.0101) [[1196]](../bib_references/bib.md#bib949)
- $\bullet$

xDSD75-PBEP86-D4: 0.75 HF exchange + 0.25 PBE GGA exchange + 0.3517 (1.0 during SCF cycles) P86 GGA correlation + 0.6623 OS MP2 correlation + 0.1168 SS MP2 correlation
with DFT-D4 (s6 = 0.4246, s8 = 0, s9 = 1.0, a1 = 0.2828, a2 = 4.7204) [[1196]](../bib_references/bib.md#bib949)
- $\bullet$

revDOD-PBEP86-D4: 0.69 HF exchange + 0.31 PBE GGA exchange + 0.4301 P86 GGA correlation + 0.6131 OS MP2 correlation
with DFT-D4 (s6 = 0.6158, s8 = 0, s9 = 1.0, a1 = 0.344, a2 = 4.2427) [[1196]](../bib_references/bib.md#bib949)
- $\bullet$

revDSD-PBEP86-D4: 0.69 HF exchange + 0.31 PBE GGA exchange + 0.4224 P86 GGA correlation + 0.5935 OS MP2 correlation + 0.0566 SS MP2 correlation
with DFT-D4 (s6 = 0.5917, s8 = 0, s9 = 1.0, a1 = 0.371, a2 = 4.2014) [[1196]](../bib_references/bib.md#bib949)
- $\bullet$

DSD-PBEPBE-D3: 68% HF exchange + 32% PBE GGA exchange + 49% PBE GGA correlation +
13% SS MP2 correlation + 55% OS MP2 correlation with DFT-D3(BJ) tail[[715]](../bib_references/bib.md#bib747)
- $\bullet$

DSD-PBEP86-D3: 69% HF exchange + 31% PBE GGA exchange + 44% P86 GGA correlation + 22% SS MP2
correlation + 52% OS MP2 correlation with DFT-D3(BJ) tail[[715]](../bib_references/bib.md#bib747)
- $\bullet$

B2-PLYP: 53% HF exchange + 47% B88 GGA exchange + 73% LYP GGA correlation + 27% MP2 correlation[[493]](../bib_references/bib.md#bib501)
- $\bullet$

B2NC-PLYP: 0.81 HF exchange + 0.19 B88 GGA exchange + 0.45 LYP GGA correlation + 0.55 MP2 correlation[[1531]](../bib_references/bib.md#bib1595)
- $\bullet$

mPW2-PLYP: 0.55 HF exchange + 0.45 mPW GGA exchange + 0.75 LYP GGA correlation + 0.25 MP2 correlation[[1219]](../bib_references/bib.md#bib503)
- $\bullet$

mPW2NC-PLYP: 0.67 HF exchange + 0.33 mPW GGA exchange + 0.51 LYP GGA correlation + 0.49 MP2 correlation[[1531]](../bib_references/bib.md#bib1595)
- $\bullet$

B2GP-PLYP: 65% HF exchange + 35% B88 GGA exchange + 64% LYP GGA correlation + 36% MP2 correlation[[669]](../bib_references/bib.md#bib694)
- $\bullet$

LS1DH-PBE: 75% HF exchange + 25% PBE GGA exchange + 57.8125% PBE GGA correlation + 42.1875%
MP2 correlation[[1367]](../bib_references/bib.md#bib1427)
- $\bullet$

PBE-QIDH: 69.3361% HF exchange + 30.6639% PBE GGA exchange + 66.6667% PBE GGA correlation
+ 33.3333% MP2 correlation[[158]](../bib_references/bib.md#bib151)
- $\bullet$

PBE0-2: $\approx$ 79.37% HF exchange + $\approx$ 20.63% PBE GGA exchange + 50% PBE GGA correlation
+ 50% MP2 correlation[[226]](../bib_references/bib.md#bib223)
- $\bullet$

PBE0-DH: 50% HF exchange + 50% PBE GGA exchange + 87.5% PBE GGA correlation + 12.5% MP2 correlation[[157]](../bib_references/bib.md#bib150)
- $\bullet$

SOS0-PBE0-2: 0.79 HF exchange + 0.21 PBE GGA exchange + 0.5 PBE GGA correlation + 0.66667 OS MP2 correlation
- $\circ$

Double Hybrid Meta-Generalized Gradient Approximation (DH MGGA)

- $\bullet$

**wB97M(2)**: 14-parameter functional form including MP2 correlation based on $\omega$B97M-V
orbitals[[906]](../bib_references/bib.md#bib941)
- $\bullet$

**wB97M(OS)**: 13-parameter functional form including opposite-spin scaled MP2 correlation based on $\omega$B97M-V
orbitals
- $\bullet$

**PTPSS-D3**: 50% HF exchange + 50% Re-Fit TPSS meta-GGA exchange + 62.5% Re-Fit TPSS
meta-GGA correlation + 37.5% OS MP2 correlation with DFT-D3(0) tail[[463]](../bib_references/bib.md#bib476)
- $\bullet$

Pr2SCAN69-D4: 0.69 HF exchange + 0.31 r2SCAN meta-GGA exchange + 0.56 r2SCAN meta-GGA correlation + 0.592593 OS MP2 correlation
with DFT-D4 (s6 = 0.7167, s8 = 0, s9 = 1.0, a1 = 0.4644, a2 = 5.2563) [[1483]](../bib_references/bib.md#bib167)
- $\bullet$

Pr2SCAN50-D4: 0.5 HF exchange + 0.5 r2SCAN meta-GGA exchange + 0.75 r2SCAN meta-GGA correlation + 0.333333 OS MP2 correlation
with DFT-D4 (s6 = 0.7964, s8 = 0.3421, s9 = 1.0, a1 = 0.4663, a2 = 5.7916) [[1483]](../bib_references/bib.md#bib167)
- $\bullet$

wPr2SCAN50-D4 ($\omega$Pr2SCAN50-D4): 0.5 HF range-separated exchange ($\omega$ = 0.214 bohr${}^{-1}$) + 0.5 r2SCAN meta-GGA exchange + 0.65 r2SCAN meta-GGA correlation + 0.46667 OS MP2 correlation
with DFT-D4 (s6 = 0.8143, s8 = 0.3842, s9 = 1.0, a1 = 0.4135, a2 = 5.8773) [[1483]](../bib_references/bib.md#bib167)
- $\bullet$

DSD-PBEB95-D3: 66% HF exchange + 34% PBE GGA exchange + 55% B95 GGA correlation + 9%
SS MP2 correlation + 46% OS MP2 correlation with DFT-D3(BJ) tail[[715]](../bib_references/bib.md#bib747)
- $\bullet$

PWPB95-D3: 50% HF exchange + 50% Re-Fit PW91 GGA exchange + 73.1% Re-Fit B95 meta-GGA
correlation + 26.9% OS MP2 correlation with DFT-D3(0) tail[[463]](../bib_references/bib.md#bib476)
