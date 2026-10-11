---
title: "5.7.4 Exchange-Dipole Model (XDM)"
---

## 5.7.4 Exchange-Dipole Model (XDM)

(July 4, 2026)

## 5.7.4.1 Theory

Becke and Johnson have proposed an *exchange dipole model* (XDM) of
dispersion.[[87]](../bib_references/bib.md#bib83)

The attractive dispersion energy
arises in this model via the interaction between the instantaneous dipole
moment of the exchange hole in one molecule, and the induced dipole moment in
another. This is a conceptually simple yet powerful approach that has been
shown to yield very accurate dispersion coefficients without fitting
parameters. This allows the calculation of both intermolecular and
intramolecular dispersion interactions within a single DFT framework. The
implementation and validation of this method in the **Q-Chem** code is described
in Ref. [[707]](../bib_references/bib.md#bib739)
, with an updated set of damping parameters[[1027]](../bib_references/bib.md#bib1070)

added in **Q-Chem** v. 6.1.1.[[483]](../bib_references/bib.md#bib494)

The dipole moment of the exchange hole function
$h_{\sigma}(\mathbf{r},\mathbf{r}^{\prime})$ is given at point $\mathbf{r}$ by

<a id="Ch5.E40"></a>

$$
d_{\sigma}(\mathbf{r})=-\mathbf{r}-\int h_{\sigma}(\mathbf{r},\mathbf{r}^{\prime})\;\mathbf{r}^{\prime}\;d\mathbf{r}^{\prime}\;, \tag{5.40}
$$

where $\sigma=\alpha,\beta$. This depends on a model of the exchange hole, and
the implementation in **Q-Chem** uses the Becke-Roussel (BR)
model.[[91]](../bib_references/bib.md#bib75)
 In most implementations the BR model, $h_{\sigma}$ is
not available in analytic form and its value must be numerically at each grid
point. **Q-Chem** developed for the first time an analytical expression for this
function,[[707]](../bib_references/bib.md#bib739)
 based on non-linear interpolation and spline
techniques, which greatly improves efficiency as well as the numerical
stability.

Two different damping functions have been used with XDM. One of them relies
only the intermolecular $C_{6}$ coefficient,
and its implementation in **Q-Chem** is denoted as “XDM6”. In this version, the dispersion energy is[[87]](../bib_references/bib.md#bib83)

<a id="eq:XDM6"></a>

$$
E_{\text{vdW}}^{\text{XDM6}}=\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}E_{\text{vdW},AB}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\frac{C_{6,AB}}{R_{AB}^{6}+\kappa\,C_{6,AB}/E^{\text{corr}}_{AB}}\;. \tag{5.41}
$$

The term $\kappa\,C_{6,AB}/E^{\text{corr}}_{AB}$ in the denominator prevents short-range divergence.
The quantity $E_{AB}^{\text{corr}}$ is the sum of
the absolute values of the correlation energies of the free atoms $A$ and $B$, whereas
$\kappa$ is a damping parameter that is universal in the sense that it is independent of the choice of functional.[[87]](../bib_references/bib.md#bib83)

The dispersion coefficients $C_{6,AB}$ is computed according to[[87]](../bib_references/bib.md#bib83)

<a id="Ch5.E42"></a>

$$
C_{6,ij}=\frac{\langle d_{\rm X}^{2}\rangle_{\!A}\langle d_{\rm X}^{2}\rangle_{\!B}\;\alpha_{\!A}\,\alpha_{B}}{\langle d_{\text{X}}^{2}\rangle_{\!A}\,\alpha_{B}+\langle d_{\text{X}}^{2}\rangle_{\!B}\,\alpha_{A}} \tag{5.42}
$$

where $\langle d_{\rm X}^{2}\rangle_{\!A}$ is the square of the exchange-hole
dipole moment of atom $A$, whose effective polarizability (in the molecule) is $\alpha_{\!A}$.

The XDM6 scheme can be further generalized to include higher-order dispersion
coefficients,[[89]](../bib_references/bib.md#bib86)
 which leads to the “XDM10” model in **Q-Chem**:

<a id="eq:XDM10"></a>

$$
E_{\rm vdW}^{\text{XDM10}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left(\frac{C_{6,AB}}{R_{{\rm vdW},AB}^{6}+R_{AB}^{6}}+\frac{C_{8,AB}}{R_{{\rm
vdW},AB}^{8}+R_{AB}^{8}}+\frac{C_{10,AB}}{R_{{\rm vdW},AB}^{10}+R_{AB}^{10}}\right)\;. \tag{5.43}
$$

The higher-order dispersion coefficients are computed using higher-order
multipole moments of the exchange hole.[[651]](../bib_references/bib.md#bib675)

The quantity $R_{{\rm vdW},AB}$ prevents short-range divergence and is nominally equal to
the sum of effective atomic radii for atoms $A$ and $B$. In practice it is determined from the formula[[651]](../bib_references/bib.md#bib675)

<a id="eq:Rvdw-damp"></a>

$$
R_{{\rm vdW},AB}=a_{1}R_{{\text{crit}},AB}+a_{2} \tag{5.44}
$$

with a critical distance

<a id="Ch5.E45"></a>

$$
R_{{\text{crit}},AB}=\frac{1}{3}\left[\left(\frac{C_{8,AB}}{C_{6,AB}}\right)^{1/2}+\left(\frac{C_{10,AB}}{C_{6,AB}}\right)^{1/4}+\left(\frac{C_{10,AB}}{C_{8,AB}}\right)^{1/2}\right] \tag{5.45}
$$

and two parameters, $a_{1}$ and $a_{2}$. These were originally fitted using Hartree-Fock exchange[[651]](../bib_references/bib.md#bib675)

but were later optimized for several different exchange-correlation functionals:
PW86PBE, PBE, BLYP, B97-1, B3LYP, B3P86, B3PW91, PBE0, BHHLYP,
LRC-$\omega$PBE, and CAM-B3LYP.[[1027]](../bib_references/bib.md#bib1070)

Parameters for this set of functionals are implemented in **Q-Chem**.[[483]](../bib_references/bib.md#bib494)

**Note: 

For functionals other than the ones specified above, Hartree-Fock values of the parameters $a_{1}$ and
$a_{2}$ are used, although this may not be optimal.
**

## 5.7.4.2 Job Control

As in DFT-D, the van der Waals energy is added as a post-SCF correction.
Analytic gradients and Hessians are available for both XDM6 and XDM10.
The dispersion correction
is requested by setting XDM = TRUE in the *$rem* section.
All other job control variables belong in the *$xdm* input section, as described below. Of these,
only **NAtoms_Mol1** is required, as this determined which part of the *$molecule* section
corresponds to monomer $A$, with the rest corresponding to monomer $B$. It is required that
all atoms for $A$ are grouped together in the *$molecule* section.

XDM

### `XDM`

> **Controls whether to add XDM dispersion to an SCF calculation**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not apply the XDM scheme.
>     * 1
>     * Add XDM dispersion as a correction to the SCF energy (and gradient, if appropriate).
>     * 2
>     * Add dispersion as a DFT functional and do full SCF.
> * **Recommendation**: The second (self-consistent) option is only available for XDM6.

### `NAtomsMol1`

> **Sets the size of monomer $A$ . INPUT SECTION: $xdm**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $N$
>     * Monomer
>     * $A$
>     * consists of the first
>     * $N$
>     * atoms in the
>     * $molecule
>     * section.
> * **Recommendation**: This is the only required keyword in the $xdm section. The two monomers must be grouped together in the $molecule section; note that Q-Chem ’s fragment-based input format does not work with XDM.

### `Method`

> **Controls which XDM method to use. INPUT SECTION: $xdm**
>
> * **Type**: `STRING`
> * **Default**: `XDM10`
> * **Options**:
>     * XDM6
>     * Use the
>     * $C_{6}$
>     * -only model of Eq. (
>     * 5.41
>     * ).
>     * XDM10
>     * Use the model that includes
>     * $C_{8}$
>     * and
>     * $C_{10}$
>     * , Eq. (
>     * 5.43
>     * ).
> * **Recommendation**: The XDM10 is generally more accurate and is now the preferred approach.

### `Damp_C6_K`

> **Set the damping parameter $\kappa$ in Eq. ( 5.41 ). INPUT SECTION: $xdm**
>
> * **Type**: `FLOAT`
> * **Default**: `0.8`
> * **Options**:
>     * $x$
>     * Set
>     * $\kappa=x$
>     * .
> * **Recommendation**: The default value is taken from Ref. Becke:2005a and is intended to be universal.

### `Damp_A1`

> **Sets the parameter $a_{1}$ in Eq. ( 5.44 ). INPUT SECTION: $xdm**
>
> * **Type**: `FLOAT`
> * **Default**: `Various`
> * **Options**:
>     * $x$
>     * Set
>     * $a_{1}=x$
>     * .
> * **Recommendation**: Functional-specific defaults are available for HF, PW86PBE, PBE, BLYP, B97-1, B3LYP, B3P86, B3PW91, PBE0, BHHLYP, LRC- $\omega$ PBE, and CAM-B3LYP, taken from Ref. 1027 Otero-de-la-Roza A., Johnson E. R. J. Chem. Phys. (2013) , 138 , pp. 204109 . Link . For other functionals, the HF values (Ref. 651 Johnson E. R., Becke A. D. J. Chem. Phys. (2006) , 124 , pp. 174104 . Link ) are used by default, although Q-Chem will print a warning that this may not be optimal.

### `Damp_A2`

> **Sets the parameter $a_{2}$ in Eq. ( 5.44 ). INPUT SECTION: $xdm**
>
> * **Type**: `FLOAT`
> * **Default**: `Various`
> * **Options**:
>     * $x$
>     * Set
>     * $a_{2}=x$
>     * .
> * **Recommendation**: The same comments apply (regarding functional-specific values) as in the case of Damp_A1 .

### `Print`

> **Controls the print level for the XDM procedure. INPUT SECTION: $xdm**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * No printing.
>     * 1
>     * Minimal printing.
>     * 2
>     * Debug-level printing.
> * **Recommendation**: None

### `Use_Elec_Drv`

> **Specify whether to add the gradient correction to the XDM energy. INPUT SECTION: $xdm**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Use the gradient correction.
>     * FALSE
>     * Do not use the gradient correction.
> * **Recommendation**: This is only valid with Becke’s $C_{6}$ damping function using the interpolated BR89 model.

???+ example "Example 5.14: Sample input illustrating a frequency calculation of a vdW complex He $\cdots$ N ${}_{2}$ using the XDM dispersion correction."
    ```qchem
    $molecule
       0 1
       He 0.000000  0.00000   3.800000
       N  0.000000  0.000000  0.546986
       N  0.000000  0.000000 -0.546986
    $end
    
    $rem
       JOBTYPE             FREQ
       IDERIV              2
       EXCHANGE            B3LYP
       INCDFT              0
       SCF_CONVERGENCE     8
       BASIS               6-31G*
       XDM                 TRUE
    $end
    
    $xdm
      method      xdm6
      natoms_mol1 1
    $end
    ```
