---
title: "5.7.3 Empirical Dispersion Corrections: DFT-D"
---

## 5.7.3 Empirical Dispersion Corrections: DFT-D

(July 4, 2026)

A major development in DFT during the mid-2000s was the recognition that, first
of all, semi-local density functionals do not properly capture dispersion (van
der Waals) interactions, a problem that has been addressed only much more
recently by the non-local correlation functionals discussed in
Section [5.7.2](sect_VV10.md); and second, that a cheap and simple solution to this
problem is to incorporate empirical potentials of the form $-C_{6}/R^{6}$, where
the $C_{6}$ coefficients are pairwise atomic parameters. This approach, which is
an alternative to the use of a non-local correlation functional, is known as
*dispersion-corrected DFT* (DFT-D).[[495]](../bib_references/bib.md#bib506)

There are currently three unique DFT-D methods in **Q-Chem**. These are
requested via the *$rem* variable DFT_D and are discussed below.

DFT_D

### `DFT_D`

> **Controls the empirical dispersion correction to be added to a DFT calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `None`
> * **Options**:
>     * FALSE
>     * (or 0) Do not apply the DFT-D2, DFT-CHG, or DFT-D3 scheme
>     * EMPIRICAL_GRIMME
>     * DFT-D2 dispersion correction from Grimme
>     * 494
>     * Grimme S.
>     * J. Comput. Chem.
>     * (2006)
>     * ,
>     * 27
>     * ,
>     * pp. 1787
>     * .
>     * Link
>     * EMPIRICAL_CHG
>     * DFT-CHG dispersion correction from Chai and Head-Gordon
>     * 224
>     * Chai J.-D., Head-Gordon M.
>     * Phys. Chem. Chem. Phys.
>     * (2008)
>     * ,
>     * 10
>     * ,
>     * pp. 6615
>     * .
>     * Link
>     * EMPIRICAL_GRIMME3
>     * DFT-D3(0) dispersion correction from Grimme (deprecated as
>     * of
>     * Q-Chem
>     * 5.0)
>     * D3_ZERO
>     * DFT-D3(0) dispersion correction from Grimme
>     * et al.
>     * 486
>     * Grimme S. et al.
>     * J. Chem. Phys.
>     * (2010)
>     * ,
>     * 132
>     * ,
>     * pp. 154104
>     * .
>     * Link
>     * D3S_ZERO
>     * DFT-D3S(0) dispersion correction from Tkachenko and Head-Gordon
>     * 1362
>     * Tkatchenko N. V., Head-Gordon M.
>     * J. Chem. Theory Comput.
>     * (2024)
>     * ,
>     * 20
>     * ,
>     * pp. 9741
>     * .
>     * Link
>     * D3_BJ
>     * DFT-D3(BJ) dispersion correction from Grimme
>     * et al.
>     * 488
>     * Grimme S., Ehrlich S., Goerigk L.
>     * J. Comput. Chem.
>     * (2011)
>     * ,
>     * 32
>     * ,
>     * pp. 1456
>     * .
>     * Link
>     * D3S_BJ
>     * DFT-D3S(BJ) dispersion correction from Tkachenko and Head-Gordon
>     * 1362
>     * Tkatchenko N. V., Head-Gordon M.
>     * J. Chem. Theory Comput.
>     * (2024)
>     * ,
>     * 20
>     * ,
>     * pp. 9741
>     * .
>     * Link
>     * D3_CSO
>     * DFT-D3(CSO) dispersion correction from Schröder
>     * et al.
>     * 1218
>     * Schröder H., Creon A., Schwabe T.
>     * J. Chem. Theory Comput.
>     * (2015)
>     * ,
>     * 11
>     * ,
>     * pp. 3163
>     * .
>     * Link
>     * D3_ZEROM
>     * DFT-D3M(0) dispersion correction from Smith
>     * et al.
>     * 1278
>     * Smith D. G. et al.
>     * J. Phys. Chem. Lett.
>     * (2016)
>     * ,
>     * 7
>     * ,
>     * pp. 2197
>     * .
>     * Link
>     * D3_BJM
>     * DFT-D3M(BJ) dispersion correction from Smith
>     * et al.
>     * 1278
>     * Smith D. G. et al.
>     * J. Phys. Chem. Lett.
>     * (2016)
>     * ,
>     * 7
>     * ,
>     * pp. 2197
>     * .
>     * Link
>     * D3_OP
>     * DFT-D3(op) dispersion correction from Witte
>     * et al.
>     * 1481
>     * Witte J. et al.
>     * J. Chem. Theory Comput.
>     * (2017)
>     * ,
>     * 13
>     * ,
>     * pp. 2043
>     * .
>     * Link
>     * D3
>     * Automatically select the “best” available D3 dispersion correction
>     * D4
>     * DFT-D4 dispersion correction from Caldeweyher
>     * et al.
>     * 178
>     * Caldeweyher E., Bannwarth C., Grimme S.
>     * J. Chem. Phys.
>     * (2017)
>     * ,
>     * 147
>     * ,
>     * pp. 034112
>     * .
>     * Link
>     * ,
>     * 179
>     * Caldeweyher E. et al.
>     * J. Chem. Phys.
>     * (2019)
>     * ,
>     * 150
>     * ,
>     * pp. 154122
>     * .
>     * Link
>     * ,
>     * 180
>     * Caldeweyher E. et al.
>     * Phys. Chem. Chem. Phys.
>     * (2020)
>     * ,
>     * 22
>     * ,
>     * pp. 8499
>     * .
>     * Link
> * **Recommendation**: Use D4 if the specified functional is avialable. Currently, only a subset of functionals in DFT-D4 is supported. It includes B3LYP, B97, B1LYP, PBE0, PW6B95, M06L, M06, WB97, WB97X, CAMB3LYP, PBE02, PBE0DH, MPW1K, MPWB1K, B1B95, B1PW91, B2GPPLYP, B2PLYP, B3P86, B3PW91, O3LYP, REVPBE, REVPBE0, REVTPSS, REVTPSSH, SCAN, TPSS0, TPSSH, X3LYP, TPSS, BP86, BLYP, BPBE, MPW1PW91, MPW1LYP, PBE, RPBE, and PW91.

The oldest of these approaches is DFT-D2,[[494]](../bib_references/bib.md#bib502)
 in which the
empirical dispersion potential has the aforementioned form, namely, pairwise
atomic $-C/R^{6}$ terms:

<a id="eqn:C6"></a>
$$
E^{\text{D2}}_{\text{disp}}=-s_{6}\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f^{\text{D2}}_{\text{damp}}(R_{AB})\;. \tag{5.25}
$$

This function is damped at short range, where $R_{AB}^{-6}$ diverges, via

<a id="Ch5.E26"></a>
$$
f^{\text{D2}}_{\text{damp}}(R_{AB})=\left[1+e^{-d(R_{AB}/R_{0,AB}-1)}\right]^{-1} \tag{5.26}
$$

which also helps to avoid double-counting of electron correlation effects,
since short- to medium-range correlation is included via the density
functional. (The quantity $R_{0,AB}$ is the sum of the van der Waals radii for
atoms $A$ and $B$, and $d$ is an additional parameter.) The primary parameters
in Eq. ([5.25](#eqn:C6)) are atomic coefficients $C_{6,A}$, from which the
pairwise parameters in Eq. ([5.25](#eqn:C6)) are obtained as geometric means, as
is common in classical force fields:

<a id="eq:C_6AB"></a>
$$
C_{6,AB}=\bigl{(}C_{6,A}C_{6,B}\bigr{)}^{1/2} \tag{5.27}
$$

The total energy in DFT-D2 is of course $E_{\text{DFT-D2}}=E_{\text{KS-DFT}}+E^{\text{D2}}_{\rm disp}$.

DFT-D2 is available in **Q-Chem** including analytic gradients and frequencies,
thanks to the efforts of David Sherrill’s group. The D2 correction can be used
with any density functional that is available in **Q-Chem**, although its use
with the non-local correlation functionals discussed in Section [5.7.2](sect_VV10.md)
seems inconsistent and is not recommended. The global parameter $s_{6}$ in
Eq. ([5.25](#eqn:C6)) was optimized by Grimme for four different
functionals,[[494]](../bib_references/bib.md#bib502)
 and **Q-Chem** uses these as the default values:
$s_{6}=0.75$ for PBE, $s_{6}=1.2$ for BLYP, $s_{6}=1.05$ for BP86, and $s_{6}=1.05$ for B3LYP. For all other functionals, $s_{6}=1$ by default. The D2
parameters, including the $C_{6,A}$ coefficients and the atomic van der Waals
radii, can be modified using a *$empirical_dispersion* input section. For example:

> ```qchem
> $empirical_dispersion
>    S6 1.1
>    D 10.0
>    C6 Ar 4.60 Ne 0.60
>    VDW_RADII Ar 1.60 Ne 1.20
> $end
> ```

Values not specified explicitly default to the values optimized by Grimme.

**Note: 

1.

DFT-D2 is only defined for elements up to Xe.

2.

B97-D is an exchange-correlation functional that automatically employs
the DFT-D2 dispersion correction when used via METHOD = B97-D.

**

An alternative to Grimme’s DFT-D2 is the empirical dispersion correction of
Chai and Head-Gordon,[[224]](../bib_references/bib.md#bib219)
 which uses the same form as
Eq. ([5.25](#eqn:C6)) but with a slightly different damping function:

<a id="A3.S8.EGx18"></a>
$$
\displaystyle f^{\text{CHG}}_{\text{damp}}(R_{AB})=\bigl{[}1+a(R_{AB}/R_{0,AB})^{-12}\bigr{]}^{-1} \tag{5.28}
$$

This version is activated by setting DFT_D = EMPIRICAL_CHG, and the
damping parameter $a$ is controlled by the keyword DFT_D_A.

DFT_D_A

### `DFT_D_A`

> **Controls the strength of dispersion corrections in the Chai–Head-Gordon DFT-D scheme, Eq. ( 5.28 ).**
>
> * **Type**: `INTEGER`
> * **Default**: `600`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $a=n/100$
>     * .
> * **Recommendation**: Use the default.

**Note: 

1.

DFT-CHG is only defined for elements up to Xe.

2.

The $\omega$B97X-D and $\omega$M05-D functionals automatically employ the
DFT-CHG dispersion correction when used via METHOD = wB97X-D or wM05-D.

**

Grimme’s DFT-D3 method[[486]](../bib_references/bib.md#bib504)
 constitutes an improvement
on his D2 approach, and is also available along with analytic first and second derivatives,
for any density functional that is available in **Q-Chem**. The D3 correction
includes a potential akin to that in D2 but including atomic $C_{8}$ terms as well:

<a id="eq:D3eqn"></a>
$$
E_{\text{D3,2-body}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left[s_{6}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f_{\text{damp,6}}(R_{AB})+s_{8}\left(\frac{C_{8,AB}}{R_{AB}^{8}}\right)f_{\text{damp,8}}(R_{AB})\right]\;. \tag{5.29}
$$

The total D3 dispersion correction consists of this plus a three-body term of
the Axilrod-Teller-Muto (ATM) triple-dipole variety, so that the total D3
energy is $E_{\text{DFT-D3}}=E_{\text{KS-DFT}}+E_{\text{D3,2-body}}+E_{\text{ATM,3-body}}$

Several versions of DFT-D3 are available as of **Q-Chem** 5.0, which differ in
the choice of the two damping functions. Grimme’s
formulation,[[486]](../bib_references/bib.md#bib504)
 which is now known as the “zero-damping”
version [DFT-D3(0)], uses damping functions of the form

<a id="eq:zero-damping"></a>
$$
f_{\text{damp},n}^{\text{D3(0)}}(R_{AB})=\left[1+6\left(\frac{R_{AB}}{s_{r,n}R_{0,AB}}\right)^{-\beta_{n}}\right]^{-1} \tag{5.30}
$$

for $n=6$ or 8, $\beta_{6}=14$, and $\beta_{8}=16$.[[486]](../bib_references/bib.md#bib504)
 The parameters $R_{0,AB}$
come from atomic van der Waals radii, $s_{r,6}$ is a functional-dependent
parameter, and $s_{r,8}=1$. Typically $s_{6}$ is set to unity and $s_{8}$ is
optimized for the functional in question.

The more recent Becke–Johnson-damping version of DFT-D3,[[488]](../bib_references/bib.md#bib505)

DFT-D3(BJ), is designed to be finite (but non-zero) as $R_{AB}\rightarrow 0$.
The damping functions used in DFT-D3(BJ) are

<a id="eq:bj-damping"></a>
$$
f_{\text{damp},n}^{\text{D3(BJ)}}(R_{AB})=\frac{R_{AB}^{n}}{R_{AB}^{n}+\left(\alpha_{1}R_{0,AB}+\alpha_{2}\right)^{n}} \tag{5.31}
$$

where $\alpha_{1}$ and $\alpha_{2}$ are adjustable parameters fit for each
density functional. As in DFT-D3(0), $s_{6}$ is generally fixed to unity and
$s_{8}$ is optimized for each functional. DFT-D3(BJ) generally outperforms the
original DFT-D3(0) version.[[488]](../bib_references/bib.md#bib505)

In addition to these original DFT-D3(BJ) and DFT-D3(0) variants, modified DFT-D3S versions have also been implemented. [[1362]](../bib_references/bib.md#bib1420)

The D3S scheme redefines the C${}_{6}^{AB}$ coefficients by introducing atom-pair-dependent $k_{3}$. The C${}_{6}^{AB}$ coefficients in
original DFT-D3 are introduced through the following expression:

<a id="eq:d3_c6"></a>
$$
C_{6}^{AB}(CN^{A},CN^{B})=\frac{\sum_{i=1}^{N_{A}}\sum_{j=1}^{N_{B}}C_{6,\text{ref}}^{AB}(CN_{i}^{A},CN_{j}^{B})L_{ij}}{\sum_{i=1}^{N_{A}}\sum_{j=1}^{N_{B}}L_{ij}} \tag{6}
$$

Here, $N_{A}$ and $N_{B}$ are the number of reference molecules for atoms A and B,
$C_{6,\text{ref}}^{AB}(CN_{i}^{A},CN_{j}^{B})$ are precomputed dispersion coefficients for the reference
molecules, and $CN_{i}^{A}$, $CN_{j}^{B}$ are the coordination numbers of the atoms A and B in their respective
reference molecules. The term $L_{ij}$ modulates the weight based on how different the coordination numbers
are from their reference points and is defined in the original D3 method as:

<a id="eq:d3_k3"></a>
$$
L_{ij}^{D3}=e^{-k_{3}\left[(CN^{A}-CN_{i}^{A})^{2}+(CN^{B}-CN_{j}^{B})^{2}\right]} \tag{7}
$$

where $CN^{A}$ and $CN^{B}$ are the coordination numbers of atoms A and B in the system of interest,
and $k_{3}$ is fixed at a value of 4. However, this fixed value can lead to unphysical local minima
on the potential energy surface, especially when the coordination numbers of atoms vary. To address this issue,
the D3S scheme introduces atom-pair-dependent $k_{3}^{AB}$ parameters, resulting in an expression:

<a id="eq:d3s_k3ab"></a>
$$
L_{ij}^{D3S}=e^{-k_{3}^{AB}\left[(CN^{A}-CN_{i}^{A})^{2}+(CN^{B}-CN_{j}^{B})^{2}\right]} \tag{8}
$$

Here, $k_{3}^{AB}$ is no longer a universal constant but is instead optimized individually for each atomic pair to
reduce the sharpness of the $C_{6}^{AB}(CN^{A},CN^{B})$ function. This optimization mitigates the formation of artifact local
minima on the PES that can arise with the original D3 formulation, even for purely organic molecules. The introduction of these
pairwise $k_{3}^{AB}$ parameters in the D3S scheme enhances the accuracy of PES particularly for processes where the atom coordination
numbers change significantly.[[1362]](../bib_references/bib.md#bib1420)

The $C_{6}$-only (CSO) approach of Schröder *et al.*[[1218]](../bib_references/bib.md#bib1272)
 discards
the $C_{8}$ term in Eq. ([5.29](#eq:D3eqn)) and uses a damping function with one
parameter, $\alpha_{1}$:

<a id="eq:cso-damping"></a>
$$
f_{\text{damp},6}^{\text{D3(CSO)}}(R_{AB})=\frac{C_{AB}^{6}}{R_{AB}^{6}+(2.5\mbox{\AA})^{6}}\left(s_{6}+\frac{\alpha_{1}}{1+\exp[R_{AB}-(2.5\mbox{\AA})R_{0,AB}]}\right)\;. \tag{5.32}
$$

The DFT-D3(BJ) approach was re-parameterized by Smith *et al.*[[1278]](../bib_references/bib.md#bib1331)
 to
yield the “modified” DFT-D3(BJ) approach, DFT-D3M(BJ), whose parameterization
relied heavily on non-equilibrium geometries. The same authors also introduces
a modification DFT-D3M(0) of the original zero-damping correction, which
introduces one additional parameter
($\alpha_{1}$) as compared to DFT-D3(0):

<a id="eq:zero-m-damping"></a>
$$
f_{\text{damp},n}^{\text{D3M(0)}}(R_{AB})=\left[1+6\left(\frac{R_{AB}}{s_{r,n}R_{0,AB}}+\alpha_{1}R_{0,AB}\right)^{-\beta_{n}}\right]^{-1}. \tag{5.33}
$$

Finally, optimized power approach of Witte *et al.*[[1481]](../bib_references/bib.md#bib1543)
 treats the
exponent, $\beta_{6}$, as an optimizable parameter, given by

<a id="eq:op-damping"></a>
$$
f_{\text{damp},n}^{\text{D3(op)}}(R_{AB})=\frac{R_{AB}^{\beta_{n}}}{R_{AB}^{\beta_{n}}+(\alpha_{1}R_{0,AB}+\alpha_{2})^{\beta_{n}}}\;. \tag{5.34}
$$

Note that $\beta_{8}=\beta_{6}+2$.

To summarize this bewildering array of D3 damping functions:

- •

**DFT-D3(0)** is requested by setting DFT_D = D3_ZERO. The
model depends on four scaling parameters ($s_{6}$, $s_{r,6}$, $s_{8}$, and $s_{r,8}$),
as defined in Eq. ([5.30](#eq:zero-damping)).
- •

**DFT-D3(BJ)** is requested by setting DFT_D = D3_BJ. The
model depends on four scaling parameters ($s_{6}$, $s_{8}$, $\alpha_{1}$, and
$\alpha_{2}$), as defined in Eq. ([5.31](#eq:bj-damping)).
- •

**DFT-D3(CSO)** is requested by setting DFT_D = D3_CSO. The
model depends on two scaling parameters ($s_{6}$ and $\alpha_{1}$), as defined in
Eq. ([5.32](#eq:cso-damping)).
- •

**DFT-D3M(0)** is requested by setting DFT_D = D3_ZEROM. The
model depends on five scaling parameters ($s_{6}$, $s_{8}$, $s_{r,6}$, $s_{r,8}$, and
$\alpha_{1}$), as defined in Eq. ([5.33](#eq:zero-m-damping)).
- •

**DFT-D3M(BJ)** is requested by setting DFT_D = D3_BJM. The
model depends on four scaling parameters ($s_{6}$, $s_{8}$, $\alpha_{1}$, and
$\alpha_{2}$), as defined in Eq. ([5.31](#eq:bj-damping)).
- •

**DFT-D3(op)** is requested by setting DFT_D = D3_OP. The
model depends on four scaling parameters ($s_{6}$, $s_{8}$, $\alpha_{1}$, $\alpha_{2}$,
and $\beta_{6}$), as defined in Eq. ([5.31](#eq:bj-damping)).

The scaling parameters in these damping functions can be modified using the
*$rem* variables described below. Alternatively, one may simply set
DFT_D = D3, and a D3 dispersion correction will be selected
automatically, if one is available for the selected functional.

**Note: 

1.

DFT-D3(0) is defined for elements up to Pu ($Z=94$).

2.

The B97-D3(0), $\omega$B97X-D3, $\omega$M06-D3 functionals automatically
employ the DFT-D3(0) dispersion correction when invoked by setting
METHOD equal to B97-D3, wB97X-D3, or
wM06-D3.

3.

The old way of invoking DFT-D3, namely through the use of
EMPIRICAL_GRIMME3, is still supported, though its use is
discouraged since D3_ZERO accomplishes the same thing but with
additional precision for the relevant parameters.

4.

When DFT_D = D3, parameters may not be overwritten,
with the exception of DFT_D3_3BODY; this is intended as a
user-friendly option. This is also the case when
EMPIRICAL_GRIMME3 is employed for a functional parameterized in
**Q-Chem**. When any of D3_ZERO, D3_BJ, etc. are
chosen, **Q-Chem** will automatically populate the parameters with their
default values, if they available for the desired functional, but these
defaults can still be overwritten by the user.

**

DFT_D3_S6

### `DFT_D3_S6`

> **The linear parameter $s_{6}$ in eq. ( 5.29 ). Used in all forms of DFT-D3.**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{6}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_RS6

### `DFT_D3_RS6`

> **The nonlinear parameter $s_{r,6}$ in Eqs. ( 5.30 ) and Eq. ( 5.33 ). Used in DFT-D3(0) and DFT-D3M(0).**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{r,6}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_S8

### `DFT_D3_S8`

> **The linear parameter $s_{8}$ in Eq. ( 5.29 ). Used in DFT-D3(0), DFT-D3(BJ), DFT-D3M(0), DFT-D3M(BJ), and DFT-D3(op).**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{8}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_RS8

### `DFT_D3_RS8`

> **The nonlinear parameter $s_{r,8}$ in Eqs. ( 5.30 ) and Eq. ( 5.33 ). Used in DFT-D3(0) and DFT-D3M(0).**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{r,8}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_A1

### `DFT_D3_A1`

> **The nonlinear parameter $\alpha_{1}$ in Eqs. ( 5.31 ), ( 5.32 ), ( 5.33 ), and ( 5.34 ). Used in DFT-D3(BJ), DFT-D3(CSO), DFT-D3M(0), DFT-D3M(BJ), and DFT-D3(op).**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\alpha_{1}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_A2

### `DFT_D3_A2`

> **The nonlinear parameter $\alpha_{2}$ in Eqs. ( 5.31 ) and ( 5.34 ). Used in DFT-D3(BJ), DFT-D3M(BJ), and DFT-D3(op).**
>
> * **Type**: `INTEGER`
> * **Default**: `100000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\alpha_{2}=n/100000$
>     * .
> * **Recommendation**: NONE

DFT_D3_POWER

### `DFT_D3_POWER`

> **The nonlinear parameter $\beta_{6}$ in Eq. ( 5.34 ). Used in DFT-D3(op). Must be greater than or equal to 6 to avoid divergence.**
>
> * **Type**: `INTEGER`
> * **Default**: `600000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\beta_{6}=n/100000$
>     * .
> * **Recommendation**: NONE

The three-body interaction term, $E^{(3)}$,[[486]](../bib_references/bib.md#bib504)
 must be
explicitly turned on, if desired.

DFT_D3_3BODY

### `DFT_D3_3BODY`

> **Controls whether the three-body interaction in Grimme’s DFT-D3 method should be applied (see Eq. (14) in Ref. 486 Grimme S. et al. J. Chem. Phys. (2010) , 132 , pp. 154104 . Link ).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE (or 0)
>     * Do not apply the three-body interaction term
>     * TRUE
>     * Apply the three-body interaction term
> * **Recommendation**: NONE

More recently, Grimme published an extended D3 model,
D4.[[178]](../bib_references/bib.md#bib173)
 The main feature
of D4 is that the coefficients are generated through Casimir-Polder integration
of the dynamic atomic polarizabilities $\alpha(i\omega)$ where electronic
density information is employed via atomic partial charges. Benchmark results
show that the proposed D4 model yields significantly lower error bars. The
DFT-D4 dispersion energy similar to D3 model is given by

<a id="eq:D4eqn"></a>
$$
E_{\text{D4,2-body}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left[s_{6}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f_{\text{BJ damp,6}}(R_{AB})+s_{8}\left(\frac{C_{8,AB}}{R_{AB}^{8}}\right)f_{\text{BJ damp,8}}(R_{AB})\right]\;. \tag{5.35}
$$

The Becke-Johnson damping is utilized as default. The coordination number
dependent $C_{6}^{\text{AB}}$ coefficients are obtained on-the-fly via
Casimir-Polder integration

<a id="eq:D4C6"></a>
$$
C_{6}^{\text{AB}}=\sum^{\text{N}^{A,\mathrm{ref}}}_{A,\mathrm{ref}=1}\sum^{\text{N}^{B,\mathrm{ref}}}_{B,\mathrm{ref}=1}\frac{3}{\pi}\int_{0}^{\infty}d\omega\alpha^{A,\mathrm{ref}}(i\omega,z^{A})\times W_{A}^{A,\mathrm{ref}}\alpha^{B,\mathrm{ref}}(i\omega,z^{B})W_{B}^{B,\mathrm{ref}}\;, \tag{5.36}
$$

where

<a id="eq:D4alpha"></a>
$$
\alpha^{A,\mathrm{ref}}(i\omega,z^{A})=\frac{1}{m}\left[\alpha^{A_{m}H_{n}}(i\omega)-\frac{n}{2}\alpha^{H_{2}}(i\omega)\times\zeta(z^{H_{A},\mathrm{ref}},z^{H_{2}})\right]\zeta(z^{A},z^{A,\mathrm{ref}})\; \tag{5.37}
$$

and

<a id="eq:D4zeta"></a>
$$
\zeta(z^{A},z^{A,\mathrm{ref}})=ba^{[1.47\text{exp}(z^{A}/z^{A,\mathrm{ref}})\text{log}_{10}(z^{A,\mathrm{ref}}/z^{A})]}\;. \tag{5.38}
$$

$\alpha^{A_{m}H_{n}}$ denotes the reference polarizailities which represents the
molecular polarizability of symmetric hydride systems $A_{m}H_{n}$.
$W_{A/B}^{A,\mathrm{ref}/B,\mathrm{ref}}$ are weighting factors determining the contributions of
all element specific reference systems $N^{A,\mathrm{ref}/B,\mathrm{ref}}$. $z^{H_{A}}$ describes
the effective charge of hydrogen connectd to atom A in the reference system
$A_{m}H_{n}$. The effective charge $z^{A}$ is computed self-consistently via Mulliken
charge $q^{A}$,

<a id="eq:D4za"></a>
$$
z^{A}=Z^{A}+q^{A}. \tag{5.39}
$$

The coefficients $a$ and $b$ are parametrized to match cationic static
polarzizabilies and TD-DFT derived molecular dispersion coefficients,
respectively.

DFT_D4_S6

### `DFT_D4_S6`

> **The linear parameter $s_{6}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{6}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_S8

### `DFT_D4_S8`

> **The linear parameter $s_{8}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{8}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_S10

### `DFT_D4_S10`

> **The linear parameter $s_{10}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{10}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_A1

### `DFT_D4_A1`

> **The nonlinear parameter $\alpha_{1}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\alpha_{1}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_A2

### `DFT_D4_A2`

> **The nonlinear parameter $\alpha_{2}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\alpha_{2}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_S9

### `DFT_D4_S9`

> **The linear parameter $s_{9}$ . Used in DFT-D4.**
>
> * **Type**: `INTEGER`
> * **Default**: `Optimized number for the specified functional`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $s_{9}=n/100000000$
>     * .
> * **Recommendation**: NONE

DFT_D4_WF

### `DFT_D4_WF`

> **Weighting factor for Gaussian weighting.**
>
> * **Type**: `INTEGER`
> * **Default**: `600000000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $wf=n/100000000$
>     * .
> * **Recommendation**: Use default

DFT_D4_GA

### `DFT_D4_GA`

> **Charge scaling**
>
> * **Type**: `INTEGER`
> * **Default**: `300000000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $ga=n/100000000$
>     * .
> * **Recommendation**: Use default

DFT_D4_GC

### `DFT_D4_GC`

> **Charge scaling**
>
> * **Type**: `INTEGER`
> * **Default**: `200000000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $gc=n/100000000$
>     * .
> * **Recommendation**: Use default

???+ example "Example 5.13: Applications of B3LYP-D3(0) with custom parameters to a methane dimer."
    ```qchem
    $comment
       Geometry optimization, followed by single-point calculations using a larger
       basis set.
    $end
    
    $molecule
       0 1
       C       0.000000    -0.000323     1.755803
       H      -0.887097     0.510784     1.390695
       H       0.887097     0.510784     1.390695
       H       0.000000    -1.024959     1.393014
       H       0.000000     0.001084     2.842908
       C       0.000000     0.000323    -1.755803
       H       0.000000    -0.001084    -2.842908
       H      -0.887097    -0.510784    -1.390695
       H       0.887097    -0.510784    -1.390695
       H       0.000000     1.024959    -1.393014
    $end
    
    $rem
       JOBTYPE         opt
       EXCHANGE        B3LYP
       BASIS           6-31G*
       DFT_D           D3_ZERO
       DFT_D3_S6       100000
       DFT_D3_RS6      126100
       DFT_D3_S8       170300
       DFT_D3_3BODY    FALSE
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE         sp
       EXCHANGE        B3LYP
       BASIS           6-311++G**
       DFT_D           D3_ZERO
       DFT_D3_S6       100000
       DFT_D3_RS6      126100
       DFT_D3_S8       170300
       DFT_D3_3BODY    FALSE
    $end
    ```
