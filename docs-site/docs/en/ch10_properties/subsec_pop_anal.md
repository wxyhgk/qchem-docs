---
title: "10.2.2 Atomic Partial Charges"
---

## 10.2.2 Atomic Partial Charges

(July 4, 2026)

## 10.2.2.1 Mulliken and Löwdin charges

The one-electron charge density,

<a id="eq1001"></a>

$$
\rho({\rm{\bf r}})=\sum\limits_{\mu\nu}{P_{\mu\nu}\,\phi_{\mu}({\rm{\bf r}})\,\phi_{\nu}({\rm{\bf r}})}\;, \tag{10.1}
$$

represents the probability of finding an electron at the point $\mathbf{r}$, but
implies little regarding the number of electrons associated with a given
nucleus in a molecule. However, since the number of electrons $N$ is related to
the occupied orbitals $\psi_{i}$ by

<a id="eq1002"></a>

$$
N=2\sum_{a}^{N/2}\bigl{|}\psi_{a}(\mathbf{r})\bigr{|}^{2} \tag{10.2}
$$

We can substitute the atomic orbital (AO) basis expansion of $\psi_{a}$ into
Eq. ([10.2](#eq1002)) to obtain

<a id="eq1003"></a>

$$
N=\sum_{\mu\nu}P_{\mu\nu}S_{\mu\nu}=\sum_{\mu}\left(\mathbf{PS}\right)_{\mu\mu}=\mathrm{tr}(\mathbf{PS}) \tag{10.3}
$$

where we interpret $(\mathbf{PS})_{\mu\mu}$ as the number of electrons associated
with $\phi_{\mu}$. If the basis functions are atom-centered, the number of
electrons associated with a given atom can be obtained by summing over all the
basis functions. This leads to the Mulliken formula for the net charge on atom $A$:

<a id="eq1004"></a>

$$
q_{A}=Z_{A}-\sum_{\mu\in A}\left(\mathbf{PS}\right)_{\mu\mu} \tag{10.4}
$$

where $Z_{A}$ is the atom’s nuclear charge. This is called *Mulliken population
analysis*,

 and it is performed by default.

Although conceptually simple, Mulliken population analyses suffer from a strong
dependence on the basis set used, as well as the possibility of producing
unphysical negative numbers of electrons. An alternative is that of *Löwdin
population analysis*,[[861]](../bib_references/bib.md#bib896)
 which uses the Löwdin symmetrically
orthogonalized basis set (which is still atom-tagged) to assign the electron
density. This shows a reduced basis set dependence, but maintains the same essential features.

While Mulliken and Löwdin population analyses are commonly employed, and can
be used to produce information about changes in electron density and also
localized spin polarizations, they should not be interpreted as oxidation
states of the atoms in the system. For such information we would recommend a
bonding analysis technique (LOBA or NBO).

POP_MULLIKEN

### `POP_MULLIKEN`

> **Controls running of Mulliken population analysis.**
>
> * **Type**: `LOGICAL/INTEGER`
> * **Default**: `TRUE (or 1)`
> * **Options**:
>     * FALSE (or 0)
>     * Do not calculate Mulliken populations.
>     * TRUE (or 1)
>     * Calculate Mulliken populations.
>     * 2
>     * Also calculate shell populations for each occupied orbital.
>     * 3
>     * Same output as 2 and also orbital densities at the nuclear centers.
>     * $-1$
>     * Calculate Mulliken charges for both the ground state and any CIS,
>     * RPA, or TDDFT excited states.
> * **Recommendation**: Leave as TRUE , unless excited-state charges are desired. Mulliken analysis is a trivial additional calculation, for ground or excited states.

LOWDIN_POPULATION

### `LOWDIN_POPULATION`

> **Run Löwdin population analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not calculate Löwdin populations.
>     * TRUE
>     * Run Löwdin population analysis.
> * **Recommendation**: None

## 10.2.2.2 Charges derived from the electrostatic potential

A more stable alternative to Mulliken or Löwdin charges are charges derived
from the electrostatic potential (ESP),

 of which there are
several different types. So-called “ChElPG” charges,[[159]](../bib_references/bib.md#bib152)

whose name is an acronym for “Charges from the Electrostatic Potential on a
Grid”, are perhaps the most conceptually straightforward of the various
ESP-derived charge schemes. By definition, the ChElPG atomic charges are the
ones that provide the best fit to the molecular electrostatic potential,
evaluated on a real-space grid outside of the van der Waals region and subject
to the constraint that the sum of the ChElPG charges must equal the molecular
charge. **Q-Chem**’s implementation of the ChElPG algorithm differs slightly
from the one originally algorithm described by Breneman and
Wiberg,[[159]](../bib_references/bib.md#bib152)
 in that **Q-Chem** weights the grid points with a
smoothing function to ensure that the ChElPG charges vary continuously as the
nuclei are displaced.[[560]](../bib_references/bib.md#bib574)
 (For any particular geometry,
however, numerical values of the charges are quite similar to those obtained
using the original algorithm.) Note also that the Breneman-Wiberg approach uses
a Cartesian grid and becomes expensive for large systems, especially when
ChElPG charges are used in QM/MM-Ewald calculations.[[590]](../bib_references/bib.md#bib612)

For that reason, an alternative procedure based on atom-centered Lebedev grids
is also available,[[590]](../bib_references/bib.md#bib612)
 which provides very similar charges using
far fewer grid points. In order to use the Lebedev grid implementation the
*$rem* variables CHELPG_H and CHELPG_HA must be set, which
specify the number of Lebedev grid points for the hydrogen atoms and the heavy
atoms, respectively.

CHELPG

### `CHELPG`

> **Controls the calculation of CHELPG charges.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not calculate ChElPG charges.
>     * TRUE
>     * Compute ChElPG charges.
> * **Recommendation**: Set to TRUE if desired. For large molecules, there is some overhead associated with computing ChElPG charges, especially if the number of grid points is large. Note that POP_MULLIKEN must also be set to TRUE (which is the default value) in order to get ChElPG charges.

CHELPG_HEAD

### `CHELPG_HEAD`

> **Sets the “head space” 159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link (radial extent) of the ChElPG grid.**
>
> * **Type**: `INTEGER`
> * **Default**: `28`
> * **Options**:
>     * $N$
>     * Corresponding to a head space of
>     * $N/10$
>     * , in Å.
> * **Recommendation**: Use the default, which is the value recommended by Breneman and Wiberg. 159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link

CHELPG_DX

### `CHELPG_DX`

> **Sets the rectangular grid spacing for the traditional Cartesian ChElPG grid or the spacing between concentric Lebedev shells (when the variables CHELPG_HA and CHELPG_H are specified as well).**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $N$
>     * Corresponding to a grid space of
>     * $N/20$
>     * , in Å.
> * **Recommendation**: Use the default, which corresponds to the “dense grid” of Breneman and Wiberg, 159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link , unless the cost is prohibitive, in which case a larger value can be selected. Note that this default value is set with the Cartesian grid in mind and not the Lebedev grid. In the Lebedev case, a larger value can typically be used.

CHELPG_HA

### `CHELPG_HA`

> **Sets the Lebedev grid to use for heavy (non-hydrogen) atoms.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $N$
>     * Use
>     * $N$
>     * Lebedev points per atom.
> * **Recommendation**: $N$ must be one of the defined values for a Lebedev grid; see Table 5.2 .

CHELPG_H

### `CHELPG_H`

> **Sets the Lebedev grid to use for hydrogen atoms.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $N$
>     * Use
>     * $N$
>     * Lebedev points per atom.
> * **Recommendation**: $N$ must be one of the defined values for a Lebedev grid; see Table 5.2 . Furthermore, must always be less than or equal to CHELPG_HA . If it is greater, it will automatically be set to the value of CHELPG_HA .

A closely-related set of ESP-derived charges are the so-called “Merz-Kollman" charges,[[1258]](../bib_references/bib.md#bib1310)

in which the atom-centered charges are fit to reproduce the ESP on a small number of concentric atomic spheres
(or van der Waals surfaces of the molecule), and in this respect the
Merz-Kollman algorithm is similar to **Q-Chem**’s Lebedev-based implementation of the ChElPG charges.
**Q-Chem**’s algorithm for computing Merz-Kollman charges uses surfaces constructed from atomic spheres whose radii
are 1.4$\times$, 1.6$\times$, 1.8$\times$, and 2.0$\times$ the atomic van der Waals radii.
Lebedev or spherical-harmonics grid points are placed on each surface with
a 0.5 Å default spacing between these grid points.
These charges can be restricted to satisfy “chemical symmetry”,
where chemically equivalent atoms have the same atomic charge value,
leading to the so-called “RESP” charges.[[270]](../bib_references/bib.md#bib271)

**Note: 

1.

When both ESP_CHARGES and RESP_CHARGES are turned
on, only the RESP charges will be calcualted

2.

Both ESP_CHARGES and RESP_CHARGES can be
used to compute the atomic charges of any singlet excited state
from a CIS or TDDFT calculation (RPA or TDA). For excited-state
popular analysis, it is recommended to turn on CIS_RELAXED_DENSITY.
Physically, the external electrostatic environment should feel the relaxed
excited state density not the unrelaxed density.

**

ESP_CHARGES

### `ESP_CHARGES`

> **Controls the calculations of Merz-Kollman ESP-derived charges.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * 1
>     * Use Lebedev grid points around each atom.
>     * 2
>     * Use spherical harmonics grid points around each atom.
> * **Recommendation**: NONE

RESP_CHARGES

### `RESP_CHARGES`

> **Controls the calculations of RESP charges, where chemically equivalent atoms are restricted to have the same atomic charge value.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * 1
>     * Use Lebedev grid points around each atom.
>     * 2
>     * Use spherical harmonics grid points around each atom.
> * **Recommendation**: NONE

ESP_SURFACE_DENSITY

### `ESP_SURFACE_DENSITY`

> **Controls the spacing between grid points on vdW surfaces.**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $n$
>     * Spacing of
>     * $0.001\times n$
>     * (in Å)
> * **Recommendation**: The default corresponds to 0.5 Å spacing.

## 10.2.2.3 Hirshfeld charges

Hirshfeld population analysis[[583]](../bib_references/bib.md#bib606)
 provides yet
another definition of atomic charges in a molecule:

<a id="eq:hirshfeld"></a>

$$
q_{A}=Z_{A}-\int d{\bf r}\left(\frac{\rho^{0}_{A}({\bf r})}{\sum_{B}\rho^{0}_{B}({\bf r})}\right)\rho({\bf r}), \tag{10.5}
$$

where $Z_{A}$ is the nuclear charge of $A$, $\rho^{0}_{B}$ is the isolated
ground-state atomic density of atom $B$, and $\rho$ is the molecular density.
The sum goes over all atoms in the molecule. Thus computing Hirshfeld charges
requires a self-consistent calculation of the isolated atomic densities (the
promolecule) as well as the total molecule. Prior to the SCF calculation, the
Hirshfeld atomic density matrix is constructed. After SCF convergence,
numerical quadrature is used to evaluate the integral in Eq. ([10.5](#eq:hirshfeld)).
Neutral ground-state atoms are used, as the choice
of appropriate reference for a charged molecule is ambiguous (such jobs will
crash). As numerical integration (with default quadrature grid) is used,
charges may not sum precisely to zero. A larger XC_GRID may be used
to improve the accuracy of the integration, but the magnitude of the Hirshfeld
charges should be largely independent of grid choice.

The charges (and corresponding molecular dipole moments) obtained using
Hirshfeld charges are typically underestimated as compared to other charge
schemes or experimental data. To correct this, Marenich *et al.* introduced
“Charge Model 5” (CM5),[[911]](../bib_references/bib.md#bib945)
 which employs a single set of
parameters to map the Hirshfeld charges onto a more reasonable representation
of the electrostatic potential. CM5 charges generally lead to more accurate
dipole moments as compared to the original Hirshfeld charges, at negligible
additional cost. CM5 is available for molecules composed of elements H–Ca,
Zn, Ge–Br, and I.

The use of neutral ground-state atoms to define the promolecular density in
Hirshfeld scheme has no strict theoretical basis and there is no unique way to
construct the promolecular densities. For example, Li${}^{0}$F${}^{0}$, Li${}^{+}$F${}^{-}$, or
Li${}^{-}$F${}^{+}$ could each be used to construct the promolecular densities for LiF.
Furthermore, the choice of appropriate reference for a charged molecule is
ambiguous, and for this reason Hirshfeld analysis is disabled in **Q-Chem** for
any molecule with a net charge. A solution for charged molecules is to use the
iterative “Hirshfeld-I” partitioning scheme proposed by Bultinck
*et al.*,[[170]](../bib_references/bib.md#bib164)
 in which the reference state is
not predefined but rather determined self-consistently, thus eliminating the
arbitrariness. The final self-consistent reference state for
Hirshfeld-I partitioning usually consists of non-integer atomic
populations.

In the first iteration, the Hirshfeld-I method uses neutral atomic
densities (as in the original Hirshfeld scheme), $\rho_{i}^{0}(\mathbf{r})$ with
electronic population $N_{i}^{0}=\int d\mathbf{r}\,\rho_{i}^{0}(\mathbf{r})=Z_{i}$.
This affords charges

<a id="eq:hirshc"></a>

$$
q_{i}^{1}=Z_{i}-\int d\mathbf{r}\left(\frac{\rho_{i}^{0}(\mathbf{r})}{\sum_{i}^{A}\rho_{i}^{0}(\mathbf{r})}\right)\rho(\mathbf{r})=Z_{i}-N_{i}^{1} \tag{10.6}
$$

on the first iteration. The new electronic population (number of electrons)
for atom $i$ is $N_{i}^{1}$, and is derived from the promolecular populations
$N_{i}^{0}$.
One then computes new isolated atomic densities with $N_{i}^{1}=\int d\mathbf{r}\,\rho_{i}^{1}(\mathbf{r}_{1})$ and uses them to construct the promolecular
densities in the next iteration. In general, the new weighting function for
atom $i$ in the $k$th iteration is

<a id="eq:weight2"></a>

$$
w_{i,\rm{HI}}^{k}(\mathbf{r})=\frac{\rho_{i}^{k-1}(\mathbf{r})}{\sum\limits_{i\in A}\rho_{i}^{k-1}(\mathbf{r})}\;. \tag{10.7}
$$

The atomic densities $\rho_{i}^{k}(\mathbf{r})$ with corresponding fractional
electron numbers $N_{i}^{k}$ are obtained by linear interpolation between
$\rho_{i}^{0,\lfloor N_{i}^{k}\rfloor}(\mathbf{r})$ and
$\rho_{i}^{0,\lceil N_{i}^{k}\rceil}(\mathbf{r})$ of the same atom:[[170]](../bib_references/bib.md#bib164)

<a id="eq:interpolate"></a>

$$
\rho_{i}^{k}(\mathbf{r})=\left(\lceil N_{i}^{k}\rceil-N_{i}^{k}\right)\,\rho_{i}^{0,\lfloor N_{i}^{k}\rfloor}(\mathbf{r})+\left(N_{i}^{k}-\lfloor N_{i}^{k}\rfloor\right)\,\rho_{i}^{0,\lceil N_{i}^{k}\rceil}(\mathbf{r})\;, \tag{10.8}
$$

where $\lfloor N_{i}^{k}\rfloor$ and $\lceil N_{i}^{k}\rceil$ denote the integers
that bracket $N_{i}^{k}.$ The two atomic densities on the right side of
Eq. ([10.8](#eq:interpolate)) are obtained from densities $\rho_{i}^{0,Z_{A}-2},\rho_{i}^{0,Z_{A}-1},\ldots,\rho_{i}^{0,Z_{A}+2}$ that are computed in
advance. (That is, the method uses the neutral atomic density along with the
densities for the singly- and doubly-charged cations and anions of the element
in equation.) The Hirshfeld-I iterations are converged once the
atomic populations change insignificantly between iterations, say
$|N_{i}^{k}-N_{i}^{k-1}|<0.0005e$.[[170]](../bib_references/bib.md#bib164)

The iterative Hirshfeld scheme generally affords more reasonable charges as
compared to the original Hirshfeld scheme. In LiF, for example, the original
Hirshfeld scheme predicts atomic charges of $\pm$0.57 while the iterative
scheme increases these charges to $\pm$0.93. The integral in
Eq. ([10.6](#eq:hirshc)) is evaluated by numerical quadrature, and the cost of
each iteration of Hirshfeld-I is equal to the cost of computing the
original Hirshfeld charges. The *$rem* variable POINT_GROUP_SYMMETRY must be set to FALSE for
Hirshfeld-I analysis.

HIRSHFELD

### `HIRSHFELD`

> **Controls running of Hirshfeld population analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate Hirshfeld populations.
>     * FALSE
>     * Do not calculate Hirshfeld populations.
> * **Recommendation**: None

HIRSHFELD_READ

### `HIRSHFELD_READ`

> **Switch to force reading in of isolated atomic densities.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Read in isolated atomic densities from previous Hirshfeld calculation from disk.
>     * FALSE
>     * Generate new isolated atomic densities.
> * **Recommendation**: Use the default unless system is large. Note, atoms should be in the same order with same basis set used as in the previous Hirshfeld calculation (although coordinates can change). The previous calculation should be run with the -save switch.

HIRSHFELD_SPHAVG

### `HIRSHFELD_SPHAVG`

> **Controls whether atomic densities should be spherically averaged in pro-molecule.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Spherically average atomic densities.
>     * FALSE
>     * Do not spherically average.
> * **Recommendation**: Use the default.

CM5

### `CM5`

> **Controls running of CM5 population analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate CM5 populations.
>     * FALSE
>     * Do not calculate CM5 populations.
> * **Recommendation**: None

HIRSHITER

### `HIRSHITER`

> **Controls running of iterative Hirshfeld population analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate iterative Hirshfeld populations.
>     * FALSE
>     * Do not calculate iterative Hirshfeld populations.
> * **Recommendation**: None

HIRSHITER_THRESH

### `HIRSHITER_THRESH`

> **Controls the convergence criterion of iterative Hirshfeld population analysis.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $N$
>     * Corresponding to the convergence criterion of
>     * $N/10000$
>     * , in
>     * $e$
>     * .
> * **Recommendation**: Use the default, which is the value recommended in Ref. 170 Bultinck P. et al. J. Chem. Phys. (2007) , 126 , pp. 144111 . Link

???+ example "Example 10.1: Iterative Hirshfeld population analysis for $\rm F^{-}(H_{2}O)$"
    ```qchem
    $molecule
     -1  1
      O     1.197566    -0.108087     0.000000
      H     1.415397     0.827014     0.000000
      H     0.134830    -0.084378     0.000000
      F    -1.236389     0.012239     0.000000
    $end
    
    $rem
    point_group_symmetry False
       METHOD      B3LYP
       BASIS       6-31G*
       HIRSHITER   true
    $end
    ```
