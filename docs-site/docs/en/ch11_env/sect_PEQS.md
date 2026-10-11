---
title: "11.2.11 Poisson Boundary Conditions"
---

## 11.2.11 Poisson Boundary Conditions

(July 4, 2026)

Each of the implicit solvation models described above is designed for
isotropic, bulk solvation—conditions that can be qualitatively described
using a scalar dielectric constant, $\varepsilon$. For an *anisotropic*
environment, such as a liquid/vapor interface, a more general approach is
to solve Poisson’s equation with a spatially-varying dielectric
*function*, $\varepsilon(\mathbf{r})$. Such an approach can be used, for
example, to model the air/water interface by describing certain regions
of space using $\varepsilon=1$ (air) and other regions using $\varepsilon=78$
(water).[[267]](../bib_references/bib.md#bib267)
 The atomistic region is described at the
SCF level. Construction of the dielectric function $\varepsilon(\mathbf{r})$
is based on a solute cavity, somewhat analogous to the solute cavity in a PCM
calculation but where the dielectric changes smoothly (rather than abruptly)
from $\varepsilon=1$ inside the cavity (in the atomistic QM region) to
$\varepsilon=\varepsilon_{\rm solvent}$ outside, in the continuum solvent.
Options for modeling a liquid/vapor interface are also available; see
Section [11.2.11.3](#sect:PEQS:job_control). In contrast to PCMs, which must
approximate the “volume polarization” due to penetration of the tails of the
QM charge density beyond the solute cavity, this effect is described exactly
under Poisson boundary conditions. The price to be paid for lifting this
approximation is that charge densities must be discretized and integrated over
three-dimensional space rather than simply a two-dimensional solute cavity surface.

**Q-Chem**’s implementation of the *Poisson Equation Solver* (PEqS) method was introduced in
Ref. [[267]](../bib_references/bib.md#bib267)
 and refined in Refs. [[266]](../bib_references/bib.md#bib268)
 and [[1046]](../bib_references/bib.md#bib1091)
.
Support for dielectric media with finite ionic strength was added in Ref. [[1305]](../bib_references/bib.md#bib1362)
.
Users of this methodology are asked to cite Refs. [[266]](../bib_references/bib.md#bib268)
 and [[1046]](../bib_references/bib.md#bib1091)
.

## 11.2.11.1 Theory

The most general formulation of Poisson’s equation, for a dielectric
*function* rather than a dielectric *constant*, is

<a id="eq:Poisson"></a>
$$
\hat{\bm{\nabla}}\bm{\cdot}\left[\varepsilon(\mathbf{r})\hat{\bm{\nabla}}\varphi_{\rm tot}(\mathbf{r})\right]=-4\pi\rho_{\rm sol}(\mathbf{r})\;. \tag{11.25}
$$

The solute’s charge density will be separated into nuclear and electronic components,

<a id="eq:rho"></a>
$$
\rho_{\rm sol}(\mathbf{r})=\rho_{\rm nuc}(\mathbf{r})+\rho_{\rm elec}(\mathbf{r})\;. \tag{11.26}
$$

The total electrostatic potential $\varphi_{\rm tot}$
is comprised of the solute’s electrostatic potential $\varphi_{\rm elec}+\varphi_{\rm nuc}$, which is obtained from the density
in Eq. ([11.26](#eq:rho)), plus the polarization potential induced in the medium:

<a id="eq:phi"></a>
$$
\varphi_{\rm tot}(\mathbf{r})=\varphi_{\rm elec}(\mathbf{r})+\varphi_{\rm nuc}(\mathbf{r})+\varphi_{\rm pol}(\mathbf{r})\;. \tag{11.27}
$$

To compute $\rho_{\rm elec}$, the electronic contribution to the electrostatic
potential in vacuum is first evaluated on a Cartesian grid,

<a id="eq:phi_elec"></a>
$$
\varphi_{\rm elec}(\mathbf{r}_{i})=\sum_{\mu\nu}^{N_{\rm basis}}P_{\mu\nu}\Bigl{\langle}g_{\mu}(\mathbf{r})\Bigl{|}\frac{1}{|\mathbf{r}-\mathbf{r}_{i}|}\Bigr{|}g_{\nu}(\mathbf{r})\Bigr{\rangle}\;. \tag{11.28}
$$

Here **P** is the one-electron density matrix, $g_{\mu}$ and $g_{\nu}$ are
atom-centered Gaussian basis functions, and the integration is over
$\mathbf{r}$. The electronic part of the solute’s charge density is
then obtained from

<a id="eq:rho_elec"></a>
$$
\rho_{\rm elec}(\mathbf{r})=-\frac{1}{4\pi}\hat{\nabla}^{2}\varphi_{\rm elec}(\mathbf{r})\;, \tag{11.29}
$$

where in practice the Laplacian of $\varphi_{\rm elec}$ is evaluated using an
eighth-order finite difference scheme.[[266]](../bib_references/bib.md#bib268)
 The nuclear charge
density $\rho_{\rm nuc}$ is described classically,

<a id="eq:rho_nuc"></a>
$$
\rho_{\rm nuc}(\mathbf{r})=-\sum_{A}^{N_{\rm atoms}}Z_{\!A}\ \delta\left(\mathbf{r}-\mathbf{R}_{A}\right)\;, \tag{11.30}
$$

but to avoid numerical problems the nuclear charges are smeared out over one
Cartesian grid voxel in practice. Operationally, this is achieved by adding
$Z_{A}/dV$ to the grid point nearest $\mathbf{R}_{A}$, where $dV$ is the volume of
a Cartesian voxel. The exact nuclear electrostatic potential in vacuum is
computed according to

<a id="eq:phi_nuke"></a>
$$
\varphi_{\rm nuc}(\mathbf{r})=-\frac{1}{4\pi}\sum_{A}^{N_{\rm atoms}}\frac{Z_{\!A}}{|\mathbf{r}-\mathbf{R}_{A}|}\;. \tag{11.31}
$$

The Dirac delta function in Eq. ([11.30](#eq:rho_nuc)) has dimensions of
(volume)${}^{-1}$ and therefore incorporates the aforementioned factor of $dV^{-1}$

Having computed the electronic and nuclear charge densities and the
electrostatic potentials in vacuum, one has in hand an exact solution of
Eq. ([11.25](#eq:Poisson)) for the case where $\varepsilon(\mathbf{r})=1$. The
induced polarization charge density and corresponding electrostatic potential
are then obtained iteratively, following closely the procedure outlined in
Refs. [[390]](../bib_references/bib.md#bib398)
 and [[48]](../bib_references/bib.md#bib31)
.
Equation ([11.25](#eq:Poisson)) is rewritten to appear as Poisson’s equation in
vacuum with an additional source charge density:

<a id="A3.S8.EGx104"></a>
$$
\displaystyle\begin{aligned} \displaystyle\hat{\nabla}^{2}\varphi_{\rm tot}(\mathbf{r})&\displaystyle=-4\pi\left[\frac{\rho_{\rm sol}(\mathbf{r})}{\varepsilon(\mathbf{r})}+\frac{\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi_{\rm tot}(\mathbf{r})}{4\pi}\right]\\
&\displaystyle=-4\pi\bigl{[}\rho_{\rm sol}(\mathbf{r})+\rho_{\rm pol}(\mathbf{r})\bigr{]}\;,\end{aligned} \tag{11.32}
$$

where the polarization charge density is

<a id="eq:rho_pol"></a>
$$
\rho_{\rm pol}(\mathbf{r})=\rho_{\rm iter}(\mathbf{r})+\left(\frac{1-\varepsilon(\mathbf{r})}{\varepsilon(\mathbf{r})}\right)\rho_{\rm sol}(\mathbf{r})\;. \tag{11.33}
$$

The iterative charge density $\rho_{\rm iter}(\mathbf{r})$ takes the form

<a id="eq:rho_iter1"></a>
$$
\rho_{\rm iter}^{(k+1)}(\mathbf{r})=\frac{\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi^{(k)}_{\rm tot}(\mathbf{r})}{4\pi} \tag{11.34}
$$

at iteration $k+1$. This function is nonzero only in transition regions where
the dielectric is being interpolated from vacuum to solvent. Note also that
the second term in Eq. ([11.33](#eq:rho_pol)) vanishes wherever
$\varepsilon(\mathbf{r})=1$. The quantity $\rho_{\mathrm{iter}}(\mathbf{r})$ is
iterated to convergence by performing updates $\rho_{\mathrm{iter}}^{(k)}(\mathbf{r})\rightarrow\rho_{\mathrm{iter}}^{(k+1)}(\mathbf{r})$ using Eq. ([11.34](#eq:rho_iter1)),
taking $\varphi^{(0)}_{\mathrm{tot}}(\mathbf{r})$ to be the solute’s electrostatic
potential in vacuum. Each time $\rho_{\rm iter}(\mathbf{r})$ is updated, a new
polarization charge density is generated and Eq. ([11.32](#eq:Poisson2)) is solved
to obtain a new total electrostatic potential. To stabilize the iterative
updates of $\rho_{\rm iter}(\mathbf{r})$, we use a damping procedure

<a id="A3.S8.EGx105"></a>
$$
\displaystyle\begin{aligned} \displaystyle\rho_{\rm iter}^{(k+1)}(\mathbf{r})&\displaystyle=\frac{\eta}{4\pi}\bigl{[}\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi^{(k)}_{\rm tot}(\mathbf{r})\bigr{]}+(1-\eta)\rho_{\rm iter}^{(k)}(\mathbf{r})\\
&\displaystyle=\eta\rho_{\rm iter}^{(k+1)}+(1-\eta)\rho_{\rm iter}^{(k)}(\mathbf{r})\end{aligned} \tag{11.35}
$$

rather than using Eq. ([11.34](#eq:rho_iter1)) as written. Following
Refs. [[390]](../bib_references/bib.md#bib398)
 and [[48]](../bib_references/bib.md#bib31)
, we use $\eta=0.6$.

Once the total charge density and electrostatic potential are iterated to
self-consistency, the free energy of solvation,

<a id="eq:Gpol"></a>
$$
G_{\rm pol}=\frac{1}{2}\int d\textbf{r}\;\varphi_{\rm pol}(\textbf{r})\;\rho_{\rm sol}(\mathbf{r})\;, \tag{11.36}
$$

is computed, where

<a id="eq:phi_pol"></a>
$$
\varphi_{\rm pol}(\textbf{r})=\varphi_{\rm tot}(\textbf{r})-\varphi_{\rm sol}(\mathbf{r})\;. \tag{11.37}
$$

Since $\varphi_{\mathrm{tot}}$ and $\rho_{\mathrm{tot}}$ are computed self-consistently
at each SCF iteration, the polarization effects must be incorporated into the
Fock matrix. This is accomplished by adding the correction term $\Delta\hat{F}=\delta G_{\mathrm{pol}}/\delta\rho_{\mathrm{elec}}$. The matrix form of this
correction in the atomic orbital basis is

<a id="eq:fock"></a>
$$
\Delta F_{\mu\nu}=\int d\textbf{r}\;\varphi_{\rm pol}(\textbf{r})\;g_{\mu}(\textbf{r})\;g_{\nu}(\textbf{r})\;. \tag{11.38}
$$

For additional details and a full description of the algorithm, see
Ref. [[266]](../bib_references/bib.md#bib268)
.

## 11.2.11.2 Nonequilibrium Solvation for Vertical Ionization

Nonequilibrium solvation within the framework of PCMs is discussed in
Section [11.2.3.3](topic_pcm-em.md#subsubsec:noneq-PCM), and that
methodology[[940]](../bib_references/bib.md#bib979)
 has been adapted for vertical ionization
processes in conjunction with Poisson boundary
conditions.[[267]](../bib_references/bib.md#bib267)
 A state-specific approach has been
implemented that requires solution of a nonlinear Schrödinger equation,
Eq. ([11.7](topic_pcm-em.md#eq:SS-sdeq)). For the reference state, corresponding to $i=0$ in
Eq. ([11.7](topic_pcm-em.md#eq:SS-sdeq)), this is equivalent to solving Eq. ([11.25](#eq:Poisson))
for the induced polarization potential and computing the solvation free energy
and Fock matrix correction according to
Eqs. ([11.36](#eq:Gpol)) and ([11.38](#eq:fock)), respectively. For the ionized state,
denoted by a subscript $i$, the solvent polarization is partitioned into fast
and slow components. Within the Marcus partitioning scheme,[[1530]](../bib_references/bib.md#bib1593)

Eq. ([11.32](#eq:Poisson2)) becomes[[266]](../bib_references/bib.md#bib268)

<a id="eq:neq1"></a>
$$
-\frac{1}{4\pi}\hat{\nabla}^{2}\varphi_{{\rm tot},i}(\mathbf{r})=\rho_{{\rm sol},i}(\mathbf{r})+\rho^{\rm slow}_{{\rm pol},0}(\mathbf{r})+\rho^{\rm fast}_{{\rm pol},i}(\mathbf{r})\;, \tag{11.39}
$$

where the fast polarization charge density of the ionized state, $\rho^{\rm fast}_{{\rm pol},i}$, is given by

<a id="eq:rho_pol_neq1"></a>
$$
\rho^{\rm fast}_{{\rm pol},i}(\mathbf{r})=\rho_{{\rm iter},i}(\mathbf{r})+\left(\frac{1-\varepsilon_{\rm opt}(\mathbf{r})}{\varepsilon_{\rm opt}(\mathbf{r})}\right)\bigl{[}\rho_{{\rm sol},i}(\mathbf{r})+\rho^{\rm slow}_{{\rm pol},0}(\mathbf{r})\bigr{]} \tag{11.40}
$$

and the fast polarization potential, $\varphi^{\rm fast}_{{\rm pol},i}$, is

<a id="eq:phi_pol_neq1"></a>
$$
\varphi^{\rm fast}_{{\rm pol},i}(\textbf{r})=\varphi_{{\rm tot},i}(\textbf{r})-\varphi_{{\rm sol},i}(\mathbf{r})-\varphi^{\rm slow}_{{\rm pol},0}(\mathbf{r})\;. \tag{11.41}
$$

Subscripts $i$ and 0 refer to the ionized state and the reference state,
respectively. The quantity $\varepsilon_{\rm opt}$ in
Eq. ([11.40](#eq:rho_pol_neq1)) is the solvent’s optical dielectric constant, and
$\rho_{{\rm iter},i}$ is computed using Eq. ([11.35](#eq:rho_iter2)) but with a
dielectric function constructed using $\varepsilon_{\rm opt}$ and with
$\varphi^{\rm fast}_{{\rm tot},i}$ substituted in place of $\varphi_{\rm tot}$. For the Marcus partitioning scheme, the slow component of the induced
solvent polarization charge density is computed as the three-dimensional
(volume charge rather than surface charge) analogue of Eq. ([11.9](topic_pcm-em.md#slow_q)).

## 11.2.11.3 Basic Job Control

A calculation using Poisson boundary conditions is requested by setting
SOLVENT_METHOD = PEQS in the *$rem* section. For computational
efficiency, the Poisson Equation Solver (PEqS) is typically not engaged until
the error in the vacuum SCF calculation falls below a specified threshold, taken to be $10^{3}~{}E_{h}$ by default and
user-controllable by means of the *$rem* variable PEQS_SWITCH.

**Note: 

When PEqS solvation is requested, symmetry and the standard nuclear orientation are disabled automatically,
equivalent to POINT_GROUP_SYMMETRY = FALSE and NO_REORIENT = TRUE.
Poisson’s equation is solved on a three-dimensional Cartesian grid and the energy need not be rotationally
invariant unless the grid spacing is very small.
**

PEQS_SWITCH

### `PEQS_SWITCH`

> **Inclusion of solvent effects begins when the SCF error falls below 10 ${}^{-\rm PEQS\_SWITCH}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$
>     * Corresponding to 10
>     * ${}^{-n}$
> * **Recommendation**: Use the default unless solvent effects need to be incorporated earlier in the SCF procedure.

Further job control for the Poisson equation solver (PEqS) routines is set up in two sections:
*$peqs_grid* and *$peqs*. (An optional third section, *$epsilon*, is discussed later.) The *$peqs_grid* section
is used to define the Cartesian discretization grid, as follows:

> ```qchem
> $peqs_grid
>    DimX <Nx> <Xmin> <Xmax>
>    DimY <Ny> <Ymin> <Ymax>
>    DimZ <Nz> <Zmin> <Zmax>
> $end
> ```

The Cartesian grid must be orthorhombic and `Nx`, `Ny`, and `Nz`
refer to the number of grid points for the $x$, $y$, and $z$ axes.

**Note: 

A fourth-order multigrid algorithm is used to accelerate convergence of
the conjugate gradient PEqS routine that solves
Eq. ([11.32](#eq:Poisson2)).[[266]](../bib_references/bib.md#bib268)
 This requires that the number of
grid points be odd, with the additional constraint that the quantities $N_{x}-1$,
$N_{y}-1$, and $N_{z}-1$ must all be divisible by 8.
**

Values in the last two columns of the *$peqs_grid* section specify the minimum
and maximum values of $x$, $y$, and $z$, in units of Ångstroms. The
length of the grid in the $x$ direction is $L_{x}=x_{\rm max}-x_{\rm min}$
and the grid spacing is $\Delta x=L_{x}/(N_{x}-1)$. The volume element discussed
in the context of Eq. ([11.30](#eq:rho_nuc)) is $dV=\Delta x\Delta y\Delta z$.

The *$peqs* section controls other aspects of a PEqS calculation, including
construction of the solute cavity and other required parameters for interfacial
or nonequilibrium solvation. The format is:

> ```qchem
> $peqs
>    <Keyword>  <parameter/option>
> $end
> ```

Available keywords are described below.

### `BatchSize`

> **Evaluate electrostatic potential integrals in batches over small parts of the Cartesian grid, rather than computing all integrals in a single batch. INPUT SECTION: $peqs**
>
> * **Type**: `INTEGER`
> * **Default**: `5000`
> * **Options**:
>     * $n$
>     * Corresponding to a batch size of
>     * $n$
>     * grid points.
> * **Recommendation**: For large grids ( $\geq 10^{6}$ grid points), a batch size $n\approx N_{x}N_{y}N_{z}/5$ is recommended.

### `MaxIter`

> **Sets the maximum number of iterations used in the conjugate gradient solver. INPUT SECTION: $peqs**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * User-defined.
> * **Recommendation**: Use the default unless the calculation fails to converge.

### `OpticalDielectric`

> **Sets the optical dielectric value of the solvent. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `1.7778`
> * **Options**:
>     * $\varepsilon_{\rm opt}$
>     * Desired value of
>     * $\varepsilon_{\text{opt}}$
>     * (dimensionless).
> * **Recommendation**: The optical dielectric is equal to the square of the index of refraction. The default value corresponds to water at 25 ${}^{\circ}$ C.

### `PolarIterScale`

> **Specifies the mixing parameter $\eta$ that is used in Eq. ( 11.35 ) to stabilize iterative solution for the polarization charge density. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `0.6`
> * **Options**:
>     * $\eta$
>     * Desired value of the dimensionless mixing parameter.
> * **Recommendation**: Use the default, which was tested in Refs. 390 Fisicaro G. et al. J. Chem. Phys. (2016) , 144 , pp. 014103 . Link and 48 Andreussi O., Dabo I., Marzari N. J. Chem. Phys. (2012) , 136 , pp. 064102 . Link , unless the calculation proves difficult to converge.

### `Print`

> **Specifies the level of printing in the output file. INPUT SECTION: $peqs**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Basic printing including some PEqS information at each SCF iteration.
>     * 1
>     * Additional printing include atomic vdW radii used in cavity construction.
>     * 2
>     * Debugging information.
> * **Recommendation**: Use 0 or 1.

### `SoluteCavity`

> **Specifies the type of solute cavity, which determines the form of the dielectric function $\varepsilon(\mathbf{r})$ . INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `Vacuum`
> * **Options**:
>     * Vacuum
>     * Perform calculation in vacuum,
>     * $\varepsilon(\mathbf{r})\equiv 1$
>     * .
>     * RigidVDW
>     * Create a cavity using spherically symmetric error functions.
>     * Spherical
>     * Create a single spherical cavity around the solute.
>     * Arbitrary
>     * Create a user-defined dielectric cavity as obtained from the
>     * $epsilon
>     * input section.
> * **Recommendation**: None.

### `SolventDielectric`

> **Sets the dielectric value for the solvent. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `78.39`
> * **Options**:
>     * $\varepsilon$
>     * Desired value of
>     * $\varepsilon$
>     * (dimensionless).
> * **Recommendation**: The default value corresponds to water at 25 ${}^{\circ}$ C.

### `SolverThresh`

> **The electrostatic potential is considered converged when the error falls below 10 ${}^{-\rm PEQSolverThresh}$ . INPUT SECTION: $peqs**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$
>     * Corresponding to 10
>     * ${}^{-n}$
> * **Recommendation**: Use the default unless a tighter convergence criterion is desired, at greater computational cost.

## 11.2.11.4 Cavity Construction

In conventional PCMs the solute cavity is a rigid two-dimensional surface
constructed from a union of atomic spheres, the radii of which are generally
take to be equal to the van der Waals radius ($r_{\text{vdW}}$) scaled by a
factor of 1.2; see Section [11.2.4](subsec_PCM_job_control.md).[[561]](../bib_references/bib.md#bib576)
This cavity is rigid in the sense that once the atomic coordinates are
specified, it remains unchanged during the SCF cycles. (The isodensity cavity
discussed in Section [11.2.6](subsec_SS_V_PE.md) is an exception, but is not available
for the PEqS method.) Furthermore, there is an abrupt and discontinuous change
in the dielectric constant at the solute/continuum boundary. A
three-dimensional analogue of this cavity, using continuous and differentiable
spherically-symmetric error functions, has been implemented for PEqS
calculations, following the procedure in Ref. [[390]](../bib_references/bib.md#bib398)
. The
permittivity function, which depends parametrically on the nuclear positions $\mathbf{R}_{A}$, is

<a id="eq:rigidvdw"></a>
$$
\varepsilon(\mathbf{r};\{\mathbf{R}_{A}\})=\bigl{(}\varepsilon_{\rm solvent}-1\bigr{)}\ \left\{\prod_{A}^{N_{\rm atoms}}h(d_{A},\Delta;\lvert\mathbf{r}-\mathbf{R}_{A}\rvert)\right\}\;, \tag{11.42}
$$

where

<a id="eq:h_func"></a>
$$
h(d_{A},\Delta;\lvert\mathbf{r}-\mathbf{R}_{A}\rvert)=\frac{1}{2}\left[1+{\rm
erf}\left(\frac{\lvert\mathbf{r}-\mathbf{R}_{A}\rvert-d_{A}}{\Delta}\right)\right]\;. \tag{11.43}
$$

Equation ([11.42](#eq:rigidvdw)) smoothly interpolates between $\varepsilon=1$ and
$\varepsilon=\varepsilon_{\rm solvent}$, over a length scale of $\approx 4\Delta$. The value of $\Delta$ is specified using the **RigidScale**
keyword. The quantity $d_{A}$ in Eqs. ([11.42](#eq:rigidvdw)) and ([11.43](#eq:h_func))
sets radius of the atomic sphere for atom $A$. By default, $d_{A}=1.2\,r_{\rm vdW}$ but this can be controlled as described below.

### `Radii`

> **Sets the choice of atomic vdW radii, $r_{\text{vdW}}$ . INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `Bondi`
> * **Options**:
>     * Bondi
>     * Use the modified Bondi set (Ref.
>     * 1186
>     * Rowland R. S., Taylor R.
>     * J. Phys. Chem.
>     * (1996)
>     * ,
>     * 100
>     * ,
>     * pp. 7384
>     * .
>     * Link
>     * ).
>     * UFF
>     * Universal Force Field radii (Ref.
>     * 1146
>     * Rappé A. K. et al.
>     * J. Am. Chem. Soc.
>     * (1992)
>     * ,
>     * 114
>     * ,
>     * pp. 10024
>     * .
>     * Link
>     * ).
>     * Read
>     * User-defined radii from a
>     * $van_der_waals
>     * input section.
> * **Recommendation**: None. The Read option works in the same way as the corresponding keyword in the $pcm section, which is described in Section 11.2.4.1 with the format of the $van_der_waals input section described in Section 11.2.10 .

### `RigidScale`

> **Sets the length scale on which the error function employed in the rigid vdW cavity construction interpolates the dielectric value from vacuum to solvent. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `0.265 Å`
> * **Options**:
>     * $\Delta$
>     * Specifies the desired value (in Å); see Eq. (
>     * 11.43
>     * ).
> * **Recommendation**: Use the default value, which was tuned in Ref. 390 Fisicaro G. et al. J. Chem. Phys. (2016) , 144 , pp. 014103 . Link so that errors in small-molecule solvation energies were $\approx 1$ kcal/mol.

### `VDWtype`

> **Specifies details for the rigid vdW cavity construction. INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `Scaled`
> * **Options**:
>     * Unscaled
>     * $d_{A}=r_{\mathrm{vdW}}$
>     * Scaled
>     * $d_{A}=r_{\mathrm{vdW}}\times scale$
>     * Shifted
>     * $d_{A}=(r_{\mathrm{vdW}}+shift)\times scale$
> * **Recommendation**: None. The values of $scale$ and $shift$ are set with the VDWscale and VDWshift keywords, respectively.

### `VDWscale`

> **Sets the empirical scale factor applied to the atomic van der Waals radius. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `1.2`
> * **Options**:
>     * $scale$
>     * Specifies the desired dimensionless scaling factor for the atomic vdW radii.
> * **Recommendation**: Use the default value.

### `VDWshift`

> **Adjusts the center of the spherically-symmetric error functions when constructing the rigid vdW cavity. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `0.0 Ångstroms`
> * **Options**:
>     * $shift$
>     * Specifies the desired shift (in Å).
> * **Recommendation**: If VDWtype is set to Shifted , the vdW scale factor is set to 1.0 by default. This can be adjusted using the VDWScale keyword.

Setting the **SoluteCavity** keyword to **Spherical** requests the
construction of a spherical cavity around the solute, and the dielectric is
smoothly interpolated from vacuum to solvent using a hyperbolic tangent function:[[267]](../bib_references/bib.md#bib267)

<a id="eq:hyperbolic"></a>
$$
\varepsilon(r)=\frac{1}{2}\Bigl{\{}(\varepsilon_{\mathrm{solvent}}+1)+(\varepsilon_{\mathrm{solvent}}-1)\ \mbox{tanh}\bigl{[}\alpha(r-r_{\mathrm{mid}})\bigr{]}\Bigr{\}}\;. \tag{11.44}
$$

Here, $r_{\mathrm{mid}}$ is the distance where the dielectric assumes the value
$\varepsilon(r_{\mathrm{mid}})=(\varepsilon_{\mathrm{solvent}}+1)/2$.
The value of $r_{\mathrm{mid}}$ is taken to be the sum of the sphere radius, $R$, and
half of the interpolation length, $L$: $r_{\mathrm{mid}}=R+L/2$.
The sphere radius and interpolation length are controlled with the
**SphereRadius** and **InterpolLength** keywords described below.
The parameter $\alpha$ controls the sharpness of the switching process, with
$\alpha=4/L$ by default.

### `SphereRadius`

> **Sets the radius of the spherical solute cavity. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `No default.`
> * **Options**:
>     * $R$
>     * Desired spherical cavity radius (in Å).
> * **Recommendation**: None. See the Supporting Information of Ref. 267 Coons M. P., You Z.-Q., Herbert J. M. J. Am. Chem. Soc. (2016) , 138 , pp. 10879 . Link for more information.

### `InterpolLength`

> **Sets the length scale on which the dielectric is smoothly interpolated from vacuum to solvent. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `No default.`
> * **Options**:
>     * $L$
>     * Desired interpolation length (in Å).
> * **Recommendation**: None.

### `InterpolScale`

> **For a given interpolation length ( $L$ ), ( $\alpha$ ) sets the sharpness of the dielectric transition from vacuum to solvent. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `$\alpha$`
> * **Options**:
>     * $\alpha$
>     * Desired interpolation scale factor (in Å
>     * ${}^{-1}$
>     * ).
> * **Recommendation**: Use the default unless a broader (smaller $\alpha$ ) or narrower (larger $\alpha$ ) transition region is desired.

### `Interface`

> **Perform a solvation calculation at a solvent/vacuum interface. INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Modify the dielectric function to simulate an interface between solvent and vacuum.
>     * False
>     * Perform a solvation calculation in bulk solvent.
> * **Recommendation**: The user will also need to specify the length scale on which the dielectric is smoothly interpolated from the bulk solvent value to vacuum, and the location of the Gibbs dividing surface (see below).

By setting **Interface** = **True**, the dielectric function on the Cartesian grid is
further modified to mimic a solvent/vacuum interface. First, the solute cavity
is constructed as specified by the **SoluteCavity** keyword as discussed
above. Then, the dielectric function is smoothly interpolated in the $z$ direction
across the Gibbs dividing surface ($z\equiv z_{\mathrm{GDS}}$) using the following hyperbolic
tangent switching function:[[267]](../bib_references/bib.md#bib267)

<a id="eq:hyperbolic2"></a>
$$
\varepsilon(z)=\frac{1}{2}\Bigl{\{}(\varepsilon_{\rm solvent}+1)+(1-\varepsilon_{\rm solvent})\ \mbox{tanh}\bigl{[}\beta(z-z_{\mathrm{GDS}})\bigr{]}\Bigr{\}}\;. \tag{11.45}
$$

This interpolates the dielectric function over the interface length $L_{\rm interface}$, centered at the Gibbs dividing surface, $z\equiv z_{\mathrm{GDS}}$.
Both of these values are controlled by the keywords **InterfaceLength**
and **GibbsDS**, respectively. Similar to the parameter $\alpha$ used in
the spherical cavity construction, the parameter $\beta=4/L_{\rm interface}$
controls the sharpness of the interpolation across the Gibbs dividing surface.

### `InterfaceLength`

> **Sets the length scale over which the dielectric function is smoothly transitioned from bulk solvent to vacuum in the $z$ direction INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `None`
> * **Options**:
>     * $L_{\rm interface}$
>     * Desired interface length (in Å).
> * **Recommendation**: This sets the value $\beta=4/L_{\rm interface}$ in Eq. ( 11.45 ). See the Supporting Information of Ref. 267 Coons M. P., You Z.-Q., Herbert J. M. J. Am. Chem. Soc. (2016) , 138 , pp. 10879 . Link for a full description of the solvent/vacuum interface construction.

### `GibbsDS`

> **Sets the location of the Gibbs dividing surface, in the $z$ direction. INPUT SECTION: $peqs**
>
> * **Type**: `FLOAT`
> * **Default**: `None`
> * **Options**:
>     * $z_{\mathrm{GDS}}$
>     * Desired location of the Gibbs dividing surface (in Å).
> * **Recommendation**: Consult the literature. One such way to determine this value is to compute a density profile of the solvent as a function of $z$ and set this location to be where the solvent density has decreased to 50% of the bulk value. Usually $z_{\mathrm{GDS}}\approx L_{\rm interface}/2$ .

### `NonequilJob`

> **Obtain the nonequilibrium free energy of solvation for a vertical ionization process. INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Compute the nonequilibrium free energy for a vertical ionization process.
>     * False
>     * Compute the equilibrium solvation free energy.
> * **Recommendation**: None.

### `NonequilPartition`

> **Specifies the manner in which the solvent response is partitioned into fast and slow components. INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `Marcus`
> * **Options**:
>     * Marcus
>     * Employ the Marcus partitioning scheme.
>     * Pekar
>     * Employ the Pekar partitioning scheme.
> * **Recommendation**: Use the default. Although the fast and slow solvation responses are different between the two approaches, the total solvation free energy is the same, 1530 You Z.-Q. et al. J. Chem. Phys. (2015) , 143 , pp. 204104 . Link but the Pekar scheme is computationally more expensive than the Marcus scheme.

### `NonequilState`

> **Specifies the state of interest for a nonequilibrium vertical ionization. INPUT SECTION: $peqs**
>
> * **Type**: `STRING`
> * **Default**: `Reference`
> * **Options**:
>     * Reference
>     * The reference (initial) state, from which an electron will be removed.
>     * Ionized
>     * The final (ionized) state.
> * **Recommendation**: None. Both values will be needed in a compound input job, in order to compute the nonequilibrium response to vertical ionization; see Example 11.2.11.5 .

Lastly, by setting **SoluteCavity** to **Arbitrary** in the *$peqs* input section, the user may choose to specify a
completely user-defined permittivity function $\varepsilon(\mathbf{r})$,[[31]](../bib_references/bib.md#bib15)

which must be generated externally and input into
**Q-Chem** pointwise on the PEqS grid, using a *$epsilon* section in the input file.
The format for that section consists of Cartesian grid points
$(x_{i},y_{i},z_{i})$ following by $\varepsilon(x_{i},y_{i},z_{i})$, as shown below.

```qchem
$epsilon
x1  y1  z1    eps(x1,y1,z1)
x1  y1  z2    eps(x1,y1,z2)
. . .
x1  y1  zNz   eps(z1,y1,zNz)
x1  y2  z1    eps(x1,y2,z1)
. . .
x1  y2  zNz   eps(z1,y2,zNz)
. . .
. . .
xNx  yNy  zNz    eps(xNx,yNy,zNz)
$end
```

## 11.2.11.5 Examples

The following example computes the solvation free energy of a water molecule
immersed in water. The Cartesian grid is cubic with a side length of 15.0 Å and 73 grid points in each direction. A rigid vdW cavity is used based on
scaled vdW radii for the atomic spheres. The dielectric is not set, so takes
the default value of 78.39.

???+ example "Example 11.20: Free energy of solvation of water in water."
    ```qchem
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       EXCHANGE          wB97X-V
       BASIS             6-31+G*
       SCF_CONVERGENCE   5
       THRESH            14
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY RIGIDVDW
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```

The next example illustrates calculation of the solvation free energy of a
water molecule at a water/vacuum interface, with the Gibbs dividing
surface placed at $z=0.50$ Å. The length of the interface is set to $L_{\rm interface}=2.75$ Å  and the dielectric is interpolated from bulk solvent to
vacuum in the positive $z$ direction across the Gibbs dividing surface. The
Cartesian grid, solute cavity, and solvent dielectric are the same as in the
previous example.

???+ example "Example 11.21: Free energy of solvation of water at a water/vacuum interface."
    ```qchem
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          wB97X-V
       BASIS             6-31+G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY RIGIDVDW
       INTERFACE TRUE
       INTERFACELENGTH 2.75
       GIBBSDS 0.50
       INTERFACEDIRECTION POSITIVE
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```

The final example illustrates a nonequilibrium (**NonEquilJob** =
**True**) solvation calculation for the vertical ionization of $\rm H_{2}O^{-}$ in bulk water.
This is a compound job that first calculates the equilibrium solvation free
energy of the anionic state (**NonEquilState** = **Reference**), then
computes the nonequilibrium energy correction for the ionized state
(**NonEquilState** = **Ionized**). The two jobs are separated by
“`@@@`”. The Cartesian grid and solvent dielectric are the same as the
previous examples, but the solute cavity is chosen to be spherical with a
radius of 2.0 Å. The Marcus scheme (**NonEquilPartition** =
**Marcus**) is used to partition the solvent response into fast and slow
components. Since this is the default method, the **NonEquilPartition**
keyword is omitted.

???+ example "Example 11.22: Nonequilibrium free energy of solvation for the vertical ionization of $\rm H_{2}O^{-}$"
    ```qchem
    $molecule
       -1 2
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          HF
       BASIS             6-31++G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY   SPHERICAL
       SPHERERADIUS   2.00
       NONEQUILJOB    TRUE
       NONEQUILSTATE  REFERENCE
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    
    @@@
    
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          HF
       BASIS             6-31++G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY   SPHERICAL
       SPHERERADIUS   2.00
       NONEQUILJOB    TRUE
       NONEQUILSTATE  IONIZED
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```
