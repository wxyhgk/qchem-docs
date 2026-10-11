---
title: "5.9.1 Overview"
---

## 5.9.1 Overview

(July 4, 2026)

Double-hybrid density functional
theory[[493]](../bib_references/bib.md#bib501)

(DH-DFT) has demonstrated tremendous potential for approaching the chemical
accuracy with a computational cost comparable to the second-order
Møller-Plesset perturbation theory (MP2). In a DH-DFT, a Kohn-Sham (KS) DFT
calculation is performed first, followed by a treatment of non-local orbital
correlation energy at the level of second-order Møller-Plesset perturbation
theory (MP2).[[957]](../bib_references/bib.md#bib998)
 This MP2 correlation correction includes a a
same-spin (ss) component, $E_{c}^{\mathrm{ss}}$, as well as an opposite-spin (os)
component, $E_{c}^{\mathrm{os}}$, which are added to the total energy obtained from
the KS-DFT calculation. Two scaling parameters, $c_{\mathrm{ss}}$ and $c_{\mathrm{os}}$, are
introduced in order to avoid double-counting correlation:

<a id="eq:dft2a"></a>
$$
E_{\text{DH-DFT}}=E_{\text{KS-DFT}}+c_{\mathrm{ss}}E_{c}^{\mathrm{ss}}+c_{\mathrm{os}}E_{c}^{\mathrm{os}} \tag{5.62}
$$

A starting point for understanding where a functional form like
Eq. ([5.62](#eq:dft2a)) might come from is the adiabatic connection formula that
provides a rigorous way to define double-hybrid functionals. One considers an
adiabatic path between the fictitious non-interacting KS reference system
($\lambda=0$) and the real physical system ($\lambda=1$), while holding the
electron density fixed at its value for the real system, for all $\lambda$.
Then

<a id="sung1"></a>
$$
E_{\rm XC}\left[\rho\right]=\int_{0}^{1}U_{{\rm XC},\lambda}[\rho]\;d\lambda\,, \tag{5.63}
$$

where $U_{{\rm XC},\lambda}$ is the exchange-correlation energy at a coupling
strength $\lambda$, meaning that the exchange-correlation energy if the
electron–electron terms in the Hamiltonian had the form $\lambda/r_{ij}$
rather than $1/r_{ij}$. Using a linear model of this quantity,

<a id="sung2"></a>
$$
U_{{\rm XC},\lambda}=a+b\lambda\;, \tag{5.64}
$$

one obtains the popular hybrid functional that includes the HF exchange (or
occupied orbitals) such as B3LYP.[[96]](../bib_references/bib.md#bib78)
 If one
further uses the Gorling-Levy’s perturbation theory (GL2) to define the initial
slope at $\lambda$= 0, one obtains the doubly hybrid functional form in
Eq. ([5.62](#eq:dft2a)) that includes MP2 type perturbative terms (PT2) involving virtual orbitals:[[684]](../bib_references/bib.md#bib710)

<a id="sung3"></a>
$$
U_{{\rm XC},\lambda}=\left.\frac{\partial U_{{\rm XC},\lambda}}{\lambda}\right|_{\lambda=0}=2E_{\rm C}^{\rm GL2}\,. \tag{5.65}
$$

The adiabatic connection formula has been used to develop double hybrid
functionals such as XYG3.[[1551]](../bib_references/bib.md#bib1610)
 Note that XYG3 as implemented in
**Q-Chem** uses B3LYP orbitals to generate the density and evaluate the PT2
terms. This is different from B2PLYP, an earlier doubly hybrid functional from
Grimme.[[493]](../bib_references/bib.md#bib501)
 The latter uses truncated KS orbitals while
XYG3 uses converged KS orbitals to evaluate the PT2 terms. The performance of
XYG3 is not only comparable to that of the G2 or G3 theory for thermochemistry,
but barrier heights and non-covalent interactions, including stacking
interactions, are also very well described by XYG3.[[1551]](../bib_references/bib.md#bib1610)

**Note: 

The recommended basis set for XYG3 is 6-311+G(3df,2p).
**

Due to the inclusion of PT2 terms, the cost of double-hybrid calculations is
formally ${\cal{O}}({N^{5}})$, as in conventional MP2, thereby not applicable to large
systems and partly losing DFT’s cost advantages. However, the highly successful
SOS-MP2 and local SOS-MP2 algorithms in **Q-Chem** can be leveraged to develop
double-hybrid functionals based on these ${\cal{O}}({N^{4}})$ methods. A version of
XYG3 that uses SOS-MP2 is the XYGJ-OS functional.[[1543]](../bib_references/bib.md#bib1611)
 This
functional has 4 parameters that are optimized using thermochemical data. It is
not only faster than XYG3, but comparable to XYG3 (or perhaps slightly better)
in accuracy. If the local SOS-MP2 algorithm is applied, the scaling of XYGJ-OS
is further reduced to ${\cal{O}}({N^{3}})$. Recently, XYGJ-OS became the first
double-hybrid functional whose analytic energy gradient has been derived and
implemented.[[642]](../bib_references/bib.md#bib666)

Other more empirical double-hybrid functionals have been implemented in
**Q-Chem**. Among the $\omega$B97 series of functionals,
$\omega$B97X-2[[225]](../bib_references/bib.md#bib221)
 is a long-range corrected double
hybrid that can greatly reduce the self-interaction errors (due to its high
fraction of HF exchange), and has been shown significantly superior to other
functionals for systems with both bonded and non-bonded interactions. Due to
the sensitivity of PT2 correlation energy with respect to the choices of basis
sets, $\omega$B97X-2 was parameterized with two different basis
sets: the $\omega$B97X-2(LP) was parameterized for use with
6-311++G(3df,3pd), while $\omega$B97X-2(TQZ) was parameterized with
the T/Q (triple-$\zeta$/quadruple-$\zeta$) extrapolation to the basis set
limit. A careful reading of Ref. [[225]](../bib_references/bib.md#bib221)
 is highly advised
before using either of these two functionals.

Job control variables for double-hybrid DFT are described below. Note that the
PT2 correlation energy can also be computed with the efficient
resolution-of-identity (RI) methods.
Since **Q-Chem** 5.2, RIMP2 can be invoked simply by specifying auxiliary basis set
using AUX_BASIS_CORR. See Section [6.6](../ch06_correlation/topic_rimp2.md).

DH

### `DH`

> **Controls the application of DH-DFT scheme.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE (or 0)
>     * Do not apply the DH-DFT scheme
>     * TRUE (or 1)
>     * Apply DH-DFT scheme
> * **Recommendation**: NONE

The following to *$rem* variables pertain to the
$\omega$B97X-2(LP) and $\omega$B97X-2(TQZ) functionals.

SSS_FACTOR

### `SSS_FACTOR`

> **Controls the strength of the same-spin component of PT2 correlation energy.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $c_{\mathrm{ss}}=n/10^{6}$
>     * in Eq. (
>     * 5.62
>     * ).
> * **Recommendation**: NONE

SOS_FACTOR

### `SOS_FACTOR`

> **Controls the strength of the opposite-spin component of PT2 correlation energy.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $c_{\mathrm{os}}=n/10^{6}$
>     * in Eq. (
>     * 5.62
>     * ).
> * **Recommendation**: NONE

???+ example "Example 5.18: Applications of the B2PLYP functional to LiH with and without using RI."
    ```qchem
    $molecule
       0 1
       H
       Li H 1.6
    $end
    
    $rem
       EXCHANGE    B2PLYP
       BASIS       cc-pvtz
       AUX_BASIS_CORR   rimp2-cc-pvtz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE    B2PLYP
       BASIS       cc-pvtz
    $end
    ```

???+ example "Example 5.19: Application of the $\omega$ B97X-2(TQZ) functional to LiH with and without RI"
    ```qchem
    $molecule
       0 1
       H
       Li H 1.6
    $end
    
    $rem
       EXCHANGE    omegaB97X-2(TQZ)
       BASIS       cc-pvqz
       AUX_BASIS_CORR   rimp2-cc-pvqz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE     omegaB97X-2(TQZ)
       BASIS        cc-pvqz
    $end
    ```

In the following example of XYG3, **Q-Chem** automatically performs a B3LYP
calculation first, then uses the resulting orbitals to evaluate the PT2
correlation terms. Once can also use XYG3 combined with the RI approximation;
use EXCHANGE = XYG3RI to do so, along with an appropriate choice of
auxiliary basis set.

???+ example "Example 5.20: XYG3 calculation of N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N      0.000000   0.000000   0.547775
       N      0.000000   0.000000  -0.547775
    $end
    
    $rem
       EXCHANGE  xyg3
       BASIS     6-311+G(3df,2p)
    $end
    ```

The next example illustrates XYGJ-OS. This functional uses the RI
approximation by default, so it is necessary to specify an auxiliary basis set.

???+ example "Example 5.21: XYGJ-OS calculation of N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N      0.000000   0.000000   0.547775
       N      0.000000   0.000000  -0.547775
    $end
    
    $rem
       EXCHANGE    xygjos
       BASIS       6-311+G(3df,2p)
       AUX_BASIS   rimp2-cc-pVTZ
       PURECART    1111
       TIME_MP2    true
    $end
    ```

The final example uses the local version of XYGJ-OS, which is the same as the
original XYGJ-OS but with the use of the attenuated Coulomb metric to solve the
RI coefficients. Here, the keyword omega determines the locality of
the metric.

???+ example "Example 5.22: Local XYGJ-OS calculation of N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N    0.000    0.000   0.54777500
       N    0.000    0.000  -0.54777500
    $end
    
    $rem
       EXCHANGE   lxygjos
       BASIS      6-311+G(3df,2p)
       AUX_BASIS  rimp2-cc-pVTZ
       OMEGA      200
       PURECART   1111
    $end
    ```
