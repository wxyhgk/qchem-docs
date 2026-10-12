---
title: "5.7.6 Many-Body Dispersion (MBD) Method"
---

## 5.7.6 Many-Body Dispersion (MBD) Method

(July 4, 2026)

Unlike earlier DFT-D methods that were strictly (atomic) pairwise-additive,
DFT-D3 includes three-body (triatomic) corrections. These terms are
significant for non-covalent complexes assembled from large
monomers,[[764]](../bib_references/bib.md#bib798)
 especially those that contain a large number of
polarizable centers.[[345]](../bib_references/bib.md#bib346)
 The *many-body dispersion* (MBD)
method of Tkatchenko *et al.*[[1360]](../bib_references/bib.md#bib1422)
 represents a
more general and less empirical approach that goes beyond the pairwise-additive
treatment of dispersion. This is accomplished by including $n$-body
contributions to the dispersion energy up to the number of atoms, and
polarization screening contributions to infinite order. Even in small systems
such as benzene dimer, the MBD approach consistently outperforms other popular
vdW methods.[[133]](../bib_references/bib.md#bib123)

The essential idea behind MBD is to approximate the dynamic response of a
system by that of dipole-coupled quantum harmonic oscillators (QHOs), each of
which represents a fragment of the system of interest. The correlation energy
of such a system can then be evaluated exactly by diagonalizing the
corresponding Hamiltonian:[[574]](../bib_references/bib.md#bib590)

<a id="eq:mbdhamil"></a>

$$
\hat{H}_{\text{MBD}}=\frac{1}{2}\sum^{\text{atoms}}_{A}\hat{\nabla}^{2}_{\xi_{A}}+\frac{1}{2}\sum^{\text{atoms}}_{A}\omega^{2}_{A}\xi^{2}_{A}+\frac{1}{2}\sum^{\text{atoms}}_{A,B}\omega_{A}\omega_{B}(\alpha_{A}^{0}\alpha_{B}^{0})^{1/2}\xi_{A}T_{AB}\xi_{B}. \tag{5.52}
$$

Here, $\xi_{A}=m_{A}^{1/2}|\mathbf{r}_{A}-\mathbf{R}_{A}|$ is the mass-weight displacement of oscillator $A$ from its center
$\mathbf{R}_{A}$, $\omega_{A}$ is the characteristic frequency, and $\alpha_{A}^{0}$ is the static polarizability. $T_{AB}$
is the dipole potential between the oscillators $A$ and $B$.
The MBD Hamiltonian is obtained through coarse-graining of the long-range correlation (through the long-range dipole tensor $\mathbf{T}_{\mathrm{lr}}$) and approximating the short-range polarizability via the adiabatic connection fluctuation-dissipation formula:

<a id="eq:lrmbdcorr"></a>

$$
E^{\mathrm{MBD}}_{c,\text{lr}}=-\sum_{n=2}^{\infty}\frac{(-1)^{n}}{n}\int_{0}^{\infty}\frac{\mathrm{d}u}{2\pi}\sum_{AB}\mbox{tr}\Bigl{[}\bigl{\langle}(\mathbf{\alpha}_{\mathrm{eff}}\mathbf{T}_{\mathrm{lr}})^{n}\bigl{\rangle}_{\!AB}(iu)\Bigr{]}\;. \tag{5.53}
$$

This approximation expresses the dynamic polarizability
$\mathbf{\alpha}_{\mathrm{eff}}$ (of a given fragment) in terms of the
polarizability of the corresponding QHO,

<a id="Ch5.E54"></a>

$$
\alpha_{A}^{\mathrm{QHO}}(u)=\frac{q_{A}^{2}}{m_{A}(\omega_{A}^{2}-u^{2}-i\delta u)} \tag{5.54}
$$

in which $q_{A}$ is the charge, $m_{A}$ the mass, and $\omega_{A}$ the characteristic
frequency of the oscillator. The integration in the frequency domain in
Eq. ([5.53](#eq:lrmbdcorr)) can be done analytically, leading to the so-called
plasmon pole formula for the correlation energy,

<a id="eq:mbdplasmon"></a>

$$
E_{c}=\frac{1}{2}\sum_{p=1}^{3N}(\bar{\omega}_{p}-\omega_{p}) \tag{5.55}
$$

in which $N$ is the number of fragments, $\bar{\omega}_{p}$ are the frequencies of
the interacting (dipole-coupled) system, and $\omega_{p}$ are the frequencies of
the non-interacting system (*i.e.*, the collection of independent QHOs).
The sum runs over all $3N$ characteristic frequencies of the system.

A particular method within the MBD framework is defined by the models for the
static polarizability ($\alpha_{\text{eff},A}^{0}$), the non-interacting
characteristic frequencies ($\omega_{A}$), and the damping function [$f(R)$] used
to define $\mathbf{T}_{\text{lr}}$. In **Q-Chem**, the MBD method is implemented
following the “MBD@rsSCS” approach, where “rsSCS” stands for
range-separated self-consistent screening.[[43]](../bib_references/bib.md#bib27)
 In this
approach, $\alpha_{\text{eff},A}^{0}$ is obtained in a two-step process:

1. 1.

The free-volume scaling approach is applied to the free-atom
polarizabilities, using the Hirshfeld-partitioned molecular electron
density. This is the same procedure used in the TS-vdW method described in Section [5.7.5](sect_TS.md).
2. 2.

The short-range atomic polarizabilities
$\mathrm{\alpha}_{\mathrm{sr},AB}(iu)$ are obtained by applying a Dyson-like
screening on only the short range part of the polarizabilities.
The same range-separation will later be used to define
$\mathbf{T}_{\mathrm{lr}}$.

The short-range atomic polarizabilities are summed up along one fragment
coordinate to obtain the local effective dynamic polarizability, *i.e.*,
$\mathrm{\alpha}_{\mathrm{eff},A}^{0}=\sum_{B}\mathrm{\alpha}_{\mathrm{sr},AB}$,
and are then spherically averaged. The range-separation (damping) function
$f(R)$ used to construct $\mathrm{\alpha}_{\mathrm{sr},AB}(iu)$ and
$\mathbf{T}_{\mathrm{lr}}$ is the same as that in Eq. ([5.47](sect_TS.md#eq:fdamp_TS-vdW)),
except with $d=6$ instead of $d=20$, and again $s_{R}$ for a given functional
obtained by fitting to interaction energies for non-bonded complexes. The MBD
energy is than calculated by diagonalizing the Hamiltonian
Eq. ([5.52](#eq:mbdhamil)) and using the plasmon-pole formula,
Eq. ([5.55](#eq:mbdplasmon)).

|  | BOP | B97-3 | B97 | BPW91 | revPBE | TPSS | BP86 | mPW91 | PBE | PBE0 | PW91 | SVWN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $s_{R}$ | 0.42 | 0.45 | 0.50 | 0.53 | 0.54 | 0.56 | 0.64 | 0.68 | 0.83 | 0.85 | 0.91 | 1.19 |

Table 5.5: 
Optimized values of the dimensionless range-separation parameter $s_{R}$
[Eq. ([5.47](sect_TS.md#eq:fdamp_TS-vdW))] for the MBD-vdW model,
from Ref. [[43]](../bib_references/bib.md#bib27)
.
(This is the parameter called $\beta$ in Ref. [[43]](../bib_references/bib.md#bib27)
.)

The MBD-vdW approach greatly improves the accuracy of the interaction energies
for S66[[1161]](../bib_references/bib.md#bib1213)
 test set, even if a simple functional like PBE is
used, with a mean absolute error of 0.3 kcal/mol and a maximum error of
1.3 kcal/mol, as compared to 2.3 kcal/mol (mean) and 7.2 kcal/mol (max) for
plain PBE. In general, the MBD-vdW method is superior to pairwise *a
posteriori* dispersion corrections.[[574]](../bib_references/bib.md#bib590)

As mentioned above in the context of the TS-vdW method (Section [5.7.5](sect_TS.md)),
the **FHI-aims** or **Quantum Espresso** codes cannot perform exact unrestricted SCF
calculations for the atoms and this leads to inconsistent free-atom volumes as
compared to the spherical ones computed in **Q-Chem**, and thus inconsistent
values for the vdW correction. Since the parameters of the TS-vdW and MBD-vdW
models were fitted for use with **FHI-aims** and **Quantum Espresso**, results obtained
using these codes are slightly closer to S66 benchmarks and thus scalar
modifiers are available for the internally-computed Hirshfeld volume ratios in
**Q-Chem**. For S66, the use of these modifiers leads to negligible differences
between results obtained from all three codes.

The MBD-vdW correction is requested by setting MBDVDM = TRUE
in the *$rem* section. Other job control variables, including the
aforementioned modifiers for the free-atom volume ratios, are the same as those
for the TS-vdW method and are described in Section [5.7.5](sect_TS.md).

The current implementation of MBD in Q-Chem is based on LibMBD,[[575]](../bib_references/bib.md#bib591)

a portable Fortran library interfaced to a multitude of quantum chemical codes, with
calculations requesting SCF gradients are done by a **Q-Chem**-specific code.

### `MBDVDW`

> **Flag to switch on the MBD-vdW method**
>
> * **Type**: `STRING`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not calculate MBD.
>     * `MBD_SP`: Calculate the MBD-vdW contribution to the energy.
>     * `MBD_FORCES`: Calculate the MBD-vdW contribution to the energy and the nuclear gradient.
>     * `MBD_SCF`: Calculate the MBD-vdW contribution to the energy, the nuclear as well as the SCF gradient.
> * **Recommendation**: NONE

### `MBDVDW_BETA`

> **Set custom value of the $s_{R}$ ( $\beta$ ) damping parameter**
>
> * **Type**: `INTEGER`
> * **Default**: `no default value defined`
> * **Options**:
>     * $n$: Corresponding to $n\cdot 10^{-4}$
> * **Recommendation**: Use predefined values for supported functionals, otherwise consult Ref. 43 Ambrosetti A. et al. J. Chem. Phys. (2014) , 140 , pp. 18A508 . Link and other relevant literature.

???+ example "Example 5.16: Sample input illustrating a calculation of a water molecule, including the
MBD-vdW energy."
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
       MBDVDW           MBD_SP !vdw settings, single point MBD correction
       HIRSHFELD_CONV   6 ! sets SCF_CONVERGENCE for single atom calculations
       HIRSHMOD         4 ! Apply modifiers to the free-atom volumes for H, C, N, and O
    $end
    ```
