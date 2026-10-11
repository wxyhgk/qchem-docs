---
title: "5.13.3 Density Functional Approximations Available for Use with Complex Absorbing Potentials"
---

## 5.13.3 Density Functional Approximations Available for Use with Complex Absorbing Potentials

(July 4, 2026)

The existing functionals defined for conventional real-valued electron densities
can be reused for complex-variable DFT calculations.[[1575]](../bib_references/bib.md#bib1638)

The functionals listed in this section are thus derived from the functionals already available in **Q-Chem** (see Section [5.3](sect_XCfuncs.md)),
but have been adapted for handling complex-valued electron densities.
Their names are taken from the original functional name with added prefix “cx_”.

## 5.13.3.1 Exchange functionals

**Note: 

All exchange functionals in this section can be invoked using the *$rem* variable EXCHANGE.
**

- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

cx_Slater: Slater-Dirac exchange functional (X$\alpha$ method with $\alpha=2/3$)[[329]](../bib_references/bib.md#bib333)
- $\circ$

Generalized Gradient Approximation (GGA)

- $\bullet$

cx_B88: Becke exchange functional from 1988[[95]](../bib_references/bib.md#bib74)
- $\bullet$

cx_PBE: Perdew, Burke, and Ernzerhof exchange functional[[1062]](../bib_references/bib.md#bib1112)

## 5.13.3.2 Correlation functionals

**Note: 

All correlation functionals in this section can be invoked using the *$rem* variable CORRELATION.
**

- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

cx_VWN5 / cx_VWN: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #5[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

cx_VWN1RPA: Vosko-Wilk-Nusair parameterization of the LSDA correlation energy #1 with RPA values[[1410]](../bib_references/bib.md#bib1470)
- $\circ$

Generalized Gradient Approximation

- $\bullet$

cx_PBE: Perdew, Burke, and Ernzerhof correlation functional[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

cx_LYP: Lee-Yang-Parr opposite-spin correlation functional[[780]](../bib_references/bib.md#bib813)

## 5.13.3.3 Exchange-Correlation Functionals

**Note: 

All exchange-correlation functionals in this section can be invoked using
the *$rem* variable METHOD.
**

- $\circ$

Local Spin-Density Approximation (LSDA)

- $\bullet$

cx_LDA / cx_SVWN5: Slater LSDA exchange + VWN5 LSDA correlation
- $\circ$

Generalized Gradient Approximation (GGA)

- $\bullet$

cx_PBE: PBE GGA exchange + PBE GGA correlation
- $\bullet$

cx_BLYP: B88 GGA exchange + LYP GGA correlation
- $\bullet$

cx_BPBE: B88 GGA exchange + PBE GGA correlation
- $\circ$

Global Hybrid Generalized Gradient Approximation (GH GGA)

- $\bullet$

cx_B1LYP: 25% HF exchange + 75% B88 GGA exchange + LYP GGA correlation[[17]](../bib_references/bib.md#bib1)
- $\bullet$

cx_B3LYP: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange + 19% VWN1RPA
LSDA correlation + 81% LYP GGA correlation[[96]](../bib_references/bib.md#bib78)
- $\bullet$

cx_B3LYP5: 20% HF exchange + 8% Slater LSDA exchange + 72% B88 GGA exchange + 19% VWN5 LSDA
correlation + 81% LYP GGA correlation[[96]](../bib_references/bib.md#bib78)
- $\bullet$

cx_B5050LYP: 50% HF exchange + 8% Slater LSDA exchange + 42% B88 GGA exchange + 19% VWN5
LSDA correlation + 81% LYP GGA correlation[[1239]](../bib_references/bib.md#bib1294)
- $\bullet$

cx_BHHLYP: 50% HF exchange + 50% B88 GGA exchange + LYP GGA correlation, sometimes called BH&H-LYP[[484]](../bib_references/bib.md#bib496)
- $\bullet$

cx_HFLYP: 100% HF exchange + LYP GGA correlation
- $\bullet$

cx_PBE0: 25% HF exchange + 75% PBE GGA exchange + PBE GGA correlation[[19]](../bib_references/bib.md#bib3)
- $\bullet$

cx_PBE50: 50% HF exchange + 50% PBE GGA exchange + PBE GGA correlation[[114]](../bib_references/bib.md#bib101)
