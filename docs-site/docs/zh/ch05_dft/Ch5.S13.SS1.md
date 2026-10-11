---
title: "5.13.1 Introduction"
---

## 5.13.1 Introduction

(July 4, 2026)

Modeling metastable electronic states such as temporary anions poses a challenge for self-consistent field (SCF) methods.
These anions are subject to autodetachment (AB${}^{-}\ \rightarrow\$AB $+$ e${}^{-}$)
and the autodetaching unbound electron is often placed in a very diffuse molecular orbital.
The final SCF solution then represents the neutral molecule and an isolated electron rather than the desired temporary anion.
One approach for overcoming this issue is augmenting the molecular Hamiltonian $\hat{H}$ with a Complex Absorbing Potential (CAP, see also Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)):
$\hat{H}\rightarrow\hat{H}_{\eta}=\hat{H}-\text{i}\eta\hat{W}$.
Here, $\hat{W}$ and $\eta$ determine the CAP shape and strength respectively.

The combination of CAPs and Density Functional Theory methods (CAP-DFT)
allows for modeling large temporary anions which are out of reach of post-Hartree-Fock methods,
and at a higher accuracy as compared to CAP-Hartree Fock (CAP-HF) theory.[[1359]](../bib_references/bib.md#bib1419)

Building upon the theoretical work by Ernzerhof and Zhou,
who reported CAP-DFT calculations using Local Density Approximation,[[372]](../bib_references/bib.md#bib376)

the current implementation in **Q-Chem** offers a selection of functionals from the Local Density Approximation,
Generalized Gradient Approximation and Hybrid Functional rungs (see Section [5.13.3](sub_XCfuncs_CAP.md)).
