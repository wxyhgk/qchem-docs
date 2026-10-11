---
title: "5.7.5 Tkatchenko-Scheffler van der Waals Model (TS-vdW)"
---

## 5.7.5 Tkatchenko-Scheffler van der Waals Model (TS-vdW)

(July 4, 2026)

Tkatchenko and Scheffler[[1361]](../bib_references/bib.md#bib1421)
 have developed a pairwise method
for van der Waals (vdW, *i.e.*, dispersion) interactions, based on a scaling
approach that yields *in situ* atomic polarizabilities ($\alpha$),
dispersion coefficients ($C_{6}$), and vdW radii ($R_{\text{vdW}}$) that reflect
the local electronic environment. These are based on scaling the free-atom
values of these parameters in order to account for how the volume of a given
atom is modified by its molecular environment. The size of an atom in a
molecule is determined using the Hirshfeld partition of the electron density.
(Hirshfeld or “stockholder” partitioning, which also affords one measure of
atomic charges in a molecule, is described in Section [10.2.2](../ch10_properties/subsec_pop_anal.md)).
In the resulting “TS-vdW” approach, only a single empirical range-separation
parameter ($s_{R}$) is required, which depends upon the underlying
exchange-correlation functional.

**Note: 

The parameter $s_{R}$ is currently implemented only
for the PBE, PBE0, BLYP, B3LYP, revPBE, M06L, and M06 functionals.
**

The TS-vdW energy expression is based on a pairwise-additive model for the dispersion energy,

<a id="eq:ts_energy"></a>
$$
E_{\text{vdW}}^{\text{TS}}=-\frac{1}{2}\sum^{\text{atoms}}_{A}\sum^{\text{A}}_{B\neq A}\left(\frac{C_{6,AB}^{\text{eff}}}{R_{AB}^{6}}\right)f_{\text{damp}}(R_{AB})\;. \tag{5.46}
$$

As in DFT-D the $R^{-6}$ potentials in Eq. ([5.46](#eq:ts_energy)) must be damped
at short range, and the TS-vdW model uses the damping function

<a id="eq:fdamp_TS-vdW"></a>
$$
f_{\text{damp}}(R_{AB})=\frac{1}{1+\exp\bigl{[}-d(R_{AB}/s_{R}R_{\mathrm{vdW,}AB}^{\text{eff}}-1)\bigr{]}} \tag{5.47}
$$

with $d=20$ and an empirical parameter $s_{R}$ that is optimized in a
functional-specific way to reproduce intermolecular interaction
energies.[[1361]](../bib_references/bib.md#bib1421)
 Optimized values for several different
functionals are listed in Table [5.4](#table:sR_TS-vdW-1).

|  | PBE | PBE0 | BLYP | B3LYP | revPBE | M06L | M06 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $s_{R}$ | 0.94 | 0.96 | 0.62 | 0.84 | 0.60 | 1.26 | 1.16 |

Table 5.4: 
Optimized damping parameters [Eq. ([5.46](#eq:ts_energy))] for the TS-vdW model,
from Ref. [[1361]](../bib_references/bib.md#bib1421)
.

The pairwise coefficients $C_{6,AB}^{\text{eff}}$ in Eq. ([5.46](#eq:ts_energy))
are constructed from the corresponding atomic parameters $C_{6,A}^{\text{eff}}$
via

<a id="Ch5.E48"></a>
$$
C_{6,AB}^{\text{eff}}=\frac{2C_{6,A}^{\text{eff}}C_{6,B}^{\text{eff}}}{\bigl{(}\alpha_{B}^{\text{0,eff}}/\alpha_{A}^{\text{0,eff}}\bigr{)}\,C_{6,A}^{\text{eff}}+\bigl{(}\alpha_{A}^{\text{0,eff}}/\alpha_{B}^{\text{0,eff}}\bigr{)}\,C_{6,B}^{\text{eff}}}\;, \tag{5.48}
$$

as opposed to the simple geometric mean that is used for $C_{6,AB}$ parameters
in the empirical DFT-D methods [Eq. ([5.27](subsec_DFT-D.md#eq:C_6AB))]. These are “effective”
$C_{6}$ coefficients in the sense that they account for the local electronic
environment. As indicated above, this is accomplished by scaling the
corresponding free-atom values, *i.e.*,

<a id="Ch5.E49"></a>
$$
C_{6,A}^{\text{eff}}=C_{6,A}^{\text{free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right)^{\!2} \tag{5.49}
$$

where $V_{A,\text{eff}}$ is the effective volume of atom $A$ in the molecule,
as determined using Hirshfeld partitioning. Effective atomic polarizabilities
and vdW radii are obtained analogously:

<a id="Ch5.E50"></a>
$$
\alpha^{\text{0,eff}}_{A}=\alpha_{A}^{\text{0,free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right) \tag{5.50}
$$

<a id="Ch5.E51"></a>
$$
R_{\text{vdW,}A}^{\text{eff}}=R_{\text{vdW,}A}^{\text{free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right)^{\!1/3}\;. \tag{5.51}
$$

All three of these atom-specific parameters are therefore functionals of the
electron density.

As with DFT-D, the cost to evaluate the dispersion correction in
Eq. ([5.46](#eq:ts_energy)) is essentially zero in comparison to the cost of a DFT
calculation. A recent review[[574]](../bib_references/bib.md#bib590)
 shows that the performance of
the TS-vdW model is on par with that of other pairwise dispersion corrections.
For example, for intermolecular interaction energies in the S66 data
set,[[1161]](../bib_references/bib.md#bib1213)

the TS-vdW correction added to PBE affords a mean absolute error of
0.4 kcal/mol and a maximum error of 1.5 kcal/mol, whereas the corresponding
errors for PBE alone are 2.2 kcal/mol (mean) and 7.2 kcal/mol (maximum).

During the implementation of the TS-vdW scheme in **Q-Chem**, it was noted that
evaluation of the free-atom volumes affords substantially different results as
compared to the implementations in the **FHI-aims** and **Quantum Espresso** codes, *e.g.*,
$V_{\text{H,free}}$ = 8.68 a.u. (**Q-Chem**), 10.32 a.u. (**FHI-aims**), and
10.39 a.u. (**Quantum Espresso**) for hydrogen atom using the PBE
functional.

 These discrepancies were traced to different
implementations of Hirshfeld partitioning. In **Q-Chem**, the free-atom volumes
are computed from an unrestricted atomic SCF calculation and then spherically
averaged to obtain spherically-symmetric atomic densities. In **FHI-aims** and
**Quantum Espresso** they are obtained by solving a one-dimensional radial
Schrödinger equation, which automatically affords spherically-symmetric
atomic densities but must be used with fractional occupation numbers for open-shell atoms.
These differences could likely be ameliorated by reparameterizing the
damping function in Eq. ([5.47](#eq:fdamp_TS-vdW)) for use with atomic volumes calculated
self-consistently using **Q-Chem**, wherein the representation of the electronic structure is quite
different as compared to that in either **FHI-aims** or **Quantum Espresso**.
This has not been done, however, and the parameters were simply taken from a
previous implementation.[[1361]](../bib_references/bib.md#bib1421)

In order to reproduced TS-vdW dispersion energies obtained with **FHI-aims** or **Quantum Espresso**,
it is possible to use this code in **Q-Chem** with scaling factors for the atomic Hirshfeld volumes,
recommended values for which are obtained by linear regression, comparing **Q-Chem** atomic volumes to those
obtained in **FHI-aims**. For full self-consistency, however, these scaling factors should not be used.

The TS-vdW dispersion energy is requested by setting TSVDW =
TRUE. Energies and analytic gradients are available.

TSVDW

### `TSVDW`

> **Flag to switch on the TS-vdW method**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not apply TS-vdW.
>     * 1
>     * Apply the TS-vdW method to obtain the TS-vdW energy.
>     * 2
>     * Apply the TS-vdW method to obtain the TS-vdW energy and corresponding gradients.
> * **Recommendation**: Since TS-vdW is itself a form of dispersion correction, it should not be used in conjunction with any of the dispersion corrections described in Section 5.7.3 .

TSVDW_SR

### `TSVDW_SR`

> **Set custom value of the $s_{R}$ damping parameter**
>
> * **Type**: `INTEGER`
> * **Default**: `no default value defined`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n\cdot 10^{-4}$
> * **Recommendation**: Use predefined values for supported functionals, otherwise consult Ref. 1361 Tkatchenko A., Scheffler M. Phys. Rev. Lett. (2009) , 102 , pp. 073005 . Link and other relevant literature.

HIRSHFELD_CONV

### `HIRSHFELD_CONV`

> **Set different SCF convergence criterion for the calculation of the single-atom Hirshfeld calculations**
>
> * **Type**: `INTEGER`
> * **Default**: `same as SCF_CONVERGENCE`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $10^{-n}$
> * **Recommendation**: 5

HIRSHMOD

### `HIRSHMOD`

> **Apply modifiers to the free-atom volumes used in the calculation of the scaled TS-vdW parameters**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * 0
>     * Do not apply modifiers to the Hirshfeld volumes.
>     * 1
>     * Apply built-in modifier to H.
>     * 2
>     * Apply built-in modifier to H and C.
>     * 3
>     * Apply built-in modifier to H, C and N.
>     * 4
>     * Apply built-in modifier to H, C, N and O
> * **Recommendation**: Use the default

???+ example "Example 5.15: Sample input illustrating a calculation of a water molecule, including the
TS-vdW energy."
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 1 0.95 2 104.5
    $end
    
    $rem
       BASIS            6-31G*
       METHOD           PBE
       TSVDW            TRUE  !vdw settings
       HIRSHFELD_CONV   6 ! sets SCF_CONVERGENCE for single atom calculations
       HIRSHMOD         4 ! Apply modifiers to the free-atom volumes for H, C, N, and O
    $end
    ```
