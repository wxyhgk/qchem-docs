---
title: "5.8.1 Overview"
---

## 5.8.1 Overview

(July 4, 2026)

This section describes DFT-C,[[1482]](../bib_references/bib.md#bib1542)
 an empirical correction for
basis set superposition error (BSSE) in DFT calculations that is an adaptation
of Grimme’s geometrical counterpoise (gCP) correction.[[722]](../bib_references/bib.md#bib754)
 Unlike
the traditional Boys-Bernardi counterpoise correction
(Section [8.9](../ch08_basis/sec_BSSE.md)),[[151]](../bib_references/bib.md#bib148)
 the cost of the DFT-C correction
is essentially zero (on the scale of a DFT calculation), and the latter
provides an estimate of both inter- and *intra*molecular BSSE. The form
of this correction is

<a id="Ch5.E56"></a>
$$
E_{\text{DFT-C}}=\sigma\sum^{\text{atoms}}_{A}c_{A}\sum^{\text{atoms}}_{B\neq A}g_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})\;h_{AB^{\ast}}(\{A,B,\ldots\}) \tag{5.56}
$$

where $g_{AB^{\ast}}^{\text{DFT-C}}$ is a damped, pairwise BSSE correction,

<a id="Ch5.E57"></a>
$$
g_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})=d(R_{AB})\;f_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})+\bigl{[}1-d(R_{AB})\bigr{]}f_{AB^{\ast}}^{\text{DFT-C}}(R_{\text{cov},AB})\;. \tag{5.57}
$$

The quantity

<a id="Ch5.E58"></a>
$$
f_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})=c_{AB}\exp\bigl{(}-\alpha_{AB}R_{AB}^{2}+\beta_{AB}R_{AB}\bigr{)} \tag{5.58}
$$

is the undamped pairwise BSSE and

<a id="Ch5.E59"></a>
$$
d(R_{AB})=\frac{1}{1+k_{1,AB}(R_{AB}/R_{0,AB})^{-k_{2,AB}}} \tag{5.59}
$$

is a damping function. The quantity
$h_{AB^{\ast}}(\{A,B,...\})$ is a many-body correction to the two-body BSSE correction, given by

<a id="3b"></a>
$$
h_{AB^{\ast}}(\{A,B,...\})=\left[1+\sum_{C\neq A,B}\frac{N_{C}^{\text{virt}}}{N_{B}^{\text{virt}}}\operatorname{terfc}\left(R_{AC},R_{AB}\right)\operatorname{terfc}\left(R_{BC},R_{AB}\right)\right]^{-1} \tag{5.60}
$$

where

<a id="terfc"></a>
$$
\operatorname{terfc}(x,y)=1-\frac{1}{2}\big{[}\mathrm{erf}(x+y)+\mathrm{erf}(x-y)\bigr{]}\;. \tag{5.61}
$$

The parameters $c_{A}$, $c_{AB}$, $\alpha_{AB}$, and $\beta_{AB}$ are
basis-set-dependent, and the overall scaling parameter $\sigma$ is loosely
method-dependent. All of these parameters are set internally based on the
method and basis *$rem* specifications.

**Note: 

Currently, only the def2-SVPD basis set is supported for use with DFT-C.
**

The DFT-C correction is governed by the following *$rem* variable:

DFT_C

### `DFT_C`

> **Controls whether the DFT-C empirical BSSE correction should be added.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * (or 0) Do not apply the DFT-C correction
>     * TRUE
>     * (or 1) Apply the DFT-C correction
> * **Recommendation**: NONE

The DFT-C method can be applied to any local, GGA, or meta-GGA density
functional, as in the following example.

???+ example "Example 5.17: Geometry optimization of the methane dimer using B97M-V-C/def2-SVPD, i.e. ,
the B97M-V functional with the DFT-C BSSE correction in the def2-SVPD basis set."
    ```qchem
    $molecule
       0 1
       C   0.000000  -0.000140   1.859161
       H  -0.888551   0.513060   1.494685
       H   0.888551   0.513060   1.494685
       H   0.000000  -1.026339   1.494868
       H   0.000000   0.000089   2.948284
       C   0.000000   0.000140  -1.859161
       H   0.000000  -0.000089  -2.948284
       H  -0.888551  -0.513060  -1.494685
       H   0.888551  -0.513060  -1.494685
       H   0.000000   1.026339  -1.494868
    $end
    
    $rem
       JOBTYPE            opt
       BASIS              def2-SVPD
       METHOD             b97m-v
       DFT_C              true
    $end
    ```
