---
title: "10.8.3 Treatment of Low-Frequency Vibrational Modes"
---

## 10.8.3 Treatment of Low-Frequency Vibrational Modes

(July 4, 2026)

Low-frequency vibrational modes usually emerge due to hindered or near-free rotations around a single bond within a molecule. The harmonic approximation is problematic for such internal rotations and yields an infinite vibrational entropy $S_{\mathrm{vib}}$ in the limit of vanishing frequencies.

 To fix this issue, Grimme[[496]](../bib_references/bib.md#bib507)
 proposed to enforce a finite vibrational entropy by interpolating between the entropy of the free rotor $S_{\mathrm{FR}}$ and the harmonic vibrational entropy $S_{\mathrm{HO}}$ as

<a id="eq:Grimme_interpolation"></a>

$$
S_{\mathrm{vib}}(\nu_{i})=\big{(}1-\omega(\nu_{i})\big{)}S_{\mathrm{FR}}(\nu_{i})+\omega(\nu_{i})S_{\mathrm{HO}}(\nu_{i}), \tag{10.71}
$$

where

<a id="eq:Chai_MHG_interpolator"></a>

$$
\omega(\nu_{i})=\frac{1}{1+(\nu_{0}/\nu_{i})^{\alpha}} \tag{10.72}
$$

is the damping function of Chai and Head-Gordon,[[224]](../bib_references/bib.md#bib219)

with $\alpha$ and $\nu_{0}$ as fixed parameters.
It is used as a weighting function and allows for a smooth transition from the free rotor entropy at small frequencies
to the harmonic vibrational entropy for frequencies $\nu_{i}$ above the cutoff $\nu_{0}$.
This was later extended to interpolate the vibrational enthalpy contributions between a free rotor
$H_{\mathrm{FR}}$ and a harmonic oscillator $H_{\mathrm{HO}}$ with zero-point vibrational energy
$H_{\mathrm{ZPVE}}$, as[[822]](../bib_references/bib.md#bib853)

<a id="eq:MHG_interpolation"></a>

$$
H_{\mathrm{vib}}(\nu_{i})=\big{[}1-\omega(\nu_{i})\big{]}H_{\mathrm{FR}}(\nu_{i})+\omega(\nu_{i})\big{[}H_{\mathrm{HO}}(\nu_{i})+H_{\mathrm{ZPVE}}(\nu_{i})\big{]}\;. \tag{10.73}
$$

This again reduces the error associated with treating translational and rotational degrees of freedom as
low-frequency vibrations, which is especially important for the adsorption or association of larger molecules.
This procedure is known as the quasi-rigid-rotor-harmonic-oscillator (qRRHO) approach.

The qRRHO scheme is the default in **Q-Chem**, and all thermodynamic quantities are printed for the RRHO (without interpolations) and qRRHO schemes at standard temperature and pressure (298.15 K
and 1.00 atm). To change the latter, the user can specify an *$isotopes* section (see examples and Section [10.8.2](ex_Isotope-Mass.md) for details). $\alpha$ and $\omega_{0}$ for both interpolator functions can be modified through QRRHO_ALPHA and QRRHO_OMEGA_CUTOFF respectively.

### `QRRHO_ALPHA`

> **Specifies the exponent in the damping function of Chai and Head-Gordon, used for interpolating the vibrational enthalpy and entropy in the qRRHO scheme. Specify MRRHO_ALPHA to change the exponent for the entropy interpolation separately.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $\alpha$: Dimensionless interpolator exponent used in the qRRHO scheme.
> * **Recommendation**: Use the default.

### `QRRHO_OMEGA_CUTOFF`

> **Sets the frequency cutoff in the Chai-Head-Gordon damping function for interpolating the vibrational enthalpy and entropy in the qRRHO scheme. Specify MRRHO_OMEGA_CUTOFF to change the frequency cutoff for the entropy interpolation separately.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $\omega_{0}$: Interpolator cutoff frequency used in the qRRHO scheme in cm ${}^{-1}$ .
> * **Recommendation**: Use the default.

???+ example "Example 10.41: Harmonic vibrational analysis at the HF/3-21G level of theory, where the thermodynamic properties for RRHO and
qRRHO are printed at 298.15 K and 1.00 atm."
    ```qchem
    $molecule
    0 1
    C     1.682185104800      0.240320237000      0.000000000000
    O     0.894276382600      1.089998584000      0.000000000000
    O     2.480949717100     -0.590833069200      0.000000000000
    C    -1.682185094800     -0.240320333400      0.000000000000
    O    -0.894276273900     -1.089998812500      0.000000000000
    O    -2.480949835800      0.590833394100      0.000000000000
    $end
    
    $rem
    JOBTYPE         opt
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    JOBTYPE         freq
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 10.42: Harmonic vibrational analysis at the HF/3-21G level of theory, where the thermodynamic properties for RRHO and
qRRHO are printed at standard temperature and pressure as well as two additional temperatures (273.15 K and 313.15 K).
Please see Section 10.8.2 for further details on the $isotopes section."
    ```qchem
    $molecule
    0 1
    C     1.682185104800      0.240320237000      0.000000000000
    O     0.894276382600      1.089998584000      0.000000000000
    O     2.480949717100     -0.590833069200      0.000000000000
    C    -1.682185094800     -0.240320333400      0.000000000000
    O    -0.894276273900     -1.089998812500      0.000000000000
    O    -2.480949835800      0.590833394100      0.000000000000
    $end
    
    $rem
    JOBTYPE         opt
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    JOBTYPE         freq
    METHOD          hf
    BASIS           3-21G
    ISOTOPES        true
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    $isotopes
    2 1
    0 273.15 1.0
    0 313.15 1.0
    $end
    ```
