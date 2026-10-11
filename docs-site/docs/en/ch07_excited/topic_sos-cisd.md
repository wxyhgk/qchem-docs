---
title: "7.8.4 SOS-CIS(D) Model"
---

## 7.8.4 SOS-CIS(D) Model

(July 4, 2026)

As in MP2 case, the accuracy of CIS(D) calculations can be improved by semi-empirically
scaling the opposite-spin components of CIS(D) expression:

<a id="Ch7.E91"></a>

$$
E^{\mathrm{SOS-CIS(D)}}=c_{U}\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{U_{2}^{\mathrm{OS}}\Psi^{\mathrm{HF}}}\right\rangle+c_{T}\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{T_{2}^{\mathrm{OS}}U_{1}\Psi^{\mathrm{{HF}}}}\right\rangle \tag{7.91}
$$

with the corresponding ground state energy

<a id="Ch7.E92"></a>

$$
E^{\mathrm{SOS-MP2}}=c_{T}\left\langle{\Psi^{\mathrm{HF}}}\right|V\left|{T_{2}^{\mathrm{OS}}\Psi^{\mathrm{HF}}}\right\rangle \tag{7.92}
$$

More importantly, this SOS-CIS(D) energy can be evaluated with the 4th power of
the molecular size by adopting Laplace transform technique.[[1162]](../bib_references/bib.md#bib1215)

Accordingly, SOS-CIS(D) can be applied to the calculations of excitation
energies for relatively large molecules.
