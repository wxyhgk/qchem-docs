---
title: "9.9.2 Overview and Basic Job Control"
---

## 9.9.2 Overview and Basic Job Control

(July 4, 2026)

Initial Cartesian coordinates and velocities must be specified for the
nuclei. Coordinates are specified in the *$molecule* section as usual,
while velocities can be specified using a *$velocity* section with the form:

> `$velocity` 
> 
> 
> $v_{x,1}~{}~{}~{}v_{y,1}~{}~{}~{}v_{z,1}$ 
> 
> 
> $v_{x,2}~{}~{}~{}v_{y,2}~{}~{}~{}v_{z,2}$ 
> 
> 
> $v_{x,N}~{}~{}~{}v_{y,N}~{}~{}~{}v_{z,N}$ 
> 
> 
> `$end`

Here $v_{x,i}$, $v_{y,i}$, and $v_{z,i}$ are the $x$, $y$, and $z$ Cartesian
velocities of the $i$th nucleus, specified in atomic units (bohrs per atomic
unit of time, where 1 a.u. of time is approximately 0.0242 fs). The
*$velocity* section thus has the same form as the *$molecule* section, but
without atomic symbols and without the line specifying charge and multiplicity.
The atoms must be ordered in the same manner in both the *$velocity* and
*$molecule* sections.

As an alternative to a *$velocity* section, initial nuclear velocities can be
sampled from certain distributions (*e.g.*, Maxwell-Boltzmann), using the
AIMD_INIT_VELOC variable described below.
AIMD_INIT_VELOC can also be set to QUASICLASSICAL, which
triggers the use of quasi-classical trajectory molecular dynamics (see
Section [9.9.6](subsec_QCT.md)).

The nuclear mass can be initialized by a *$mass* section with the form:

> `$mass` 
> 
> 
> $m_{1}~{}~{}~{}m_{2}$ 
> 
> 
> $m_{3}~{}~{}~{}$ ! mass of 3rd atom 
> 
> 
> $m_{4}$ 
> 
> 
> `$end`

The total number in the *$mass* section must be equal to number of atoms. Unit
is the atomic mass unit (amu), *e.g.*, mass of hydrogen-1 atom is 1.00783. If the
*$mass* section is not initialized, the default mass will be used.

Although the **Q-Chem** output file dutifully records the progress of any
*ab initio* molecular dynamics job, the most useful information is printed
not to the main output file but rather to a directory called “AIMD” that is a
subdirectory of the job’s scratch directory. (All *ab initio* molecular
dynamics jobs should therefore use the *–save* option described in
Section [2.2](../ch02_install/sect_running.md).) The AIMD directory consists of a set of files that
record, in ASCII format, one line of information at each time step. Each file
contains a few comment lines (indicated by “#”) that describe its contents
and which we summarize in the list below.

- •

`Cost`: Records the number of SCF cycles, the total CPU time, and the total
memory use at each dynamics step.
- •

`EComponents`: Records various components of the total energy (all in hartree).
- •

`Energy`: Records the total energy and fluctuations therein.
- •

`MulMoments`: If multipole moments are requested, they are printed here.
- •

`NucCarts`: Records the nuclear Cartesian coordinates $x_{1}$, $y_{1}$,
$z_{1}$, $x_{2}$, $y_{2}$, $z_{2}$, …, $x_{N}$, $y_{N}$, $z_{N}$
at each time step, in either bohrs or Ångstroms.
- •

`NucForces`: Records the Cartesian forces on the nuclei at each time step
(same order as the coordinates, but given in atomic units).
- •

`NucVeloc`: Records the Cartesian velocities of the nuclei at each time
step (same order as the coordinates, but given in atomic units).
- •

`TandV`: Records the kinetic and potential energy, as well as
fluctuations in each.
- •

`View.xyz`: Cartesian-formatted version of `NucCarts` for
viewing trajectories in an external visualization program.

For ELMD jobs, there are other output files as well:

- •

`ChangeInF`: Records the matrix norm and largest magnitude element of
$\Delta\mathbf{F}=\mathbf{F}(t+\delta t)-\mathbf{F}(t)$ in the basis of
Cholesky-orthogonalized AOs. The files ChangeInP, ChangeInL, and
ChangeInZ provide analogous information for the density matrix $\mathbf{P}$
and the Cholesky orthogonalization matrices $\mathbf{L}$ and $\mathbf{Z}$ defined
in Ref. [[558]](../bib_references/bib.md#bib572)
.
- •

`DeltaNorm`: Records the norm and largest magnitude element of the
curvy-steps rotation angle matrix $\Delta$ defined in
Ref. [[558]](../bib_references/bib.md#bib572)
. Matrix elements of $\Delta$ are the
dynamical variables representing the electronic degrees of freedom. The
output file DeltaDotNorm provides the same information for the electronic
velocity matrix $d\Delta/{dt}$.
- •

`ElecGradNorm`: Records the norm and largest magnitude element of the
electronic gradient matrix $\mathbf{FP}-\mathbf{PF}$ in the Cholesky basis.
- •

`dTfict:` Records the instantaneous time derivative of the fictitious kinetic
energy at each time step, in atomic units.

*Ab initio* molecular dynamics jobs are requested by specifying
JOBTYPE = AIMD. Initial velocities must be specified either
using a *$velocity* section or via the AIMD_INIT_VELOC keyword
described below. In addition, the following *$rem* variables must be specified
for any *ab initio* molecular dynamics job:

AIMD_METHOD

### `AIMD_METHOD`

> **Selects an ab initio molecular dynamics algorithm.**
>
> * **Type**: `STRING`
> * **Default**: `BOMD`
> * **Options**:
>     * BOMD
>     * Born-Oppenheimer molecular dynamics.
>     * CURVY
>     * Curvy-steps Extended Lagrangian molecular dynamics.
>     * QCMD
>     * Meyer-Miller nonadiabatic molecular dynamics.
> * **Recommendation**: BOMD yields exact classical molecular dynamics, provided that the energy is tolerably conserved. ELMD is an approximation to exact classical dynamics whose validity should be tested for the properties of interest. QCMD initiates Meyer-Miller nonadiabatic dynamics methods including the symmetric quasiclassical approach or the traditional Ehrenfest method.

TIME_STEP

### `TIME_STEP`

> **Specifies the molecular dynamics time step, in atomic units (1 a.u. = 0.0242 fs).**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * User-specified.
> * **Recommendation**: Smaller time steps lead to better energy conservation; too large a time step may cause the job to fail entirely. Make the time step as large as possible, consistent with tolerable energy conservation.

AIMD_TIME_STEP_CONVERSION

### `AIMD_TIME_STEP_CONVERSION`

> **Modifies the molecular dynamics time step to increase granularity.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * The molecular dynamics time step is
>     * TIME_STEP
>     * /
>     * $n$
>     * a.u.
> * **Recommendation**: None

AIMD_STEPS

### `AIMD_STEPS`

> **Specifies the requested number of molecular dynamics steps.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * User-specified.
> * **Recommendation**: None.

*Ab initio* molecular dynamics calculations can be quite expensive, and
thus **Q-Chem** includes several algorithms designed to accelerate such
calculations. At the self-consistent field (Hartree-Fock and DFT) level, BOMD
calculations can be greatly accelerated by using information from previous time
steps to construct a good initial guess for the new molecular orbitals or Fock
matrix, thus hastening SCF convergence. A Fock matrix extrapolation
procedure,[[559]](../bib_references/bib.md#bib573)
 based on a suggestion by Pulay and Fogarasi,[[1135]](../bib_references/bib.md#bib1185)

is available for this purpose.

The Fock matrix elements $F_{\mu\nu}$ in the atomic orbital basis are
oscillatory functions of the time $t$, and **Q-Chem**’s extrapolation procedure
fits these oscillations to a power series in $t$:

<a id="Ch9.E61"></a>

$$
F_{\mu\nu}(t)=\sum\limits_{n=0}^{N}{c_{n}\,}t^{n} \tag{9.61}
$$

The $N+1$ extrapolation coefficients $c_{n}$ are determined by a fit to a set of
$M$ Fock matrices retained from previous time steps. Fock matrix extrapolation
can significantly reduce the number of SCF iterations required at each time
step, but for low-order extrapolations, or if SCF_CONVERGENCE is set
too small, a systematic drift in the total energy may be observed. Benchmark
calculations testing the limits of energy conservation can be found in
Ref. [[559]](../bib_references/bib.md#bib573)
, and demonstrate that numerically exact classical
dynamics (without energy drift) can be obtained at significantly reduced cost.

Fock matrix extrapolation is requested by specifying values for $N$ and $M$, as
in the form of the following two *$rem* variables:

FOCK_EXTRAP_ORDER

### `FOCK_EXTRAP_ORDER`

> **Specifies the polynomial order $N$ for Fock matrix extrapolation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * Extrapolate using an
>     * $N$
>     * th-order polynomial (
>     * $N>0$
>     * ).
> * **Recommendation**: None

FOCK_EXTRAP_POINTS

### `FOCK_EXTRAP_POINTS`

> **Specifies the number $M$ of old Fock matrices that are retained for use in extrapolation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $M$
>     * Save
>     * $M$
>     * Fock matrices for use in extrapolation
>     * $(M>N)$
> * **Recommendation**: Higher-order extrapolations with more saved Fock matrices are faster and conserve energy better than low-order extrapolations, up to a point. In many cases, the scheme ( $N$ = 6, $M$ = 12), in conjunction with SCF_CONVERGENCE = 6, is found to provide about a 50% savings in computational cost while still conserving energy.

When nuclear forces are computed using underlying electronic structure methods
with non-optimized orbitals (such as MP2), a set of response equations must be
solved.[[29]](../bib_references/bib.md#bib13)
 While these equations are linear, their
dimensionality necessitates an iterative
solution,[[1115]](../bib_references/bib.md#bib1161)
 which, in practice, looks much like
the SCF equations. Extrapolation is again useful here,[[1304]](../bib_references/bib.md#bib1360)
 and
the syntax for $Z$-vector (response) extrapolation is similar to Fock extrapolation.

Z_EXTRAP_ORDER

### `Z_EXTRAP_ORDER`

> **Specifies the polynomial order $N$ for Z-vector extrapolation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * Extrapolate using an
>     * $N$
>     * th-order polynomial (
>     * $N>0$
>     * ).
> * **Recommendation**: None

Z_EXTRAP_POINTS

### `Z_EXTRAP_POINTS`

> **Specifies the number $M$ of old $Z$ -vectors that are retained for use in extrapolation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $M$
>     * Save
>     * $M$
>     * previous
>     * $Z$
>     * -vectors for use in extrapolation
>     * $(M>N)$
> * **Recommendation**: Using the default $Z$ -vector convergence settings, a $(M,N)=(4,2)$ extrapolation was shown to provide the greatest speedup. At this setting, a 2–3-fold reduction in iterations was demonstrated.

Assuming decent conservation, a BOMD calculation represents exact classical
dynamics on the Born-Oppenheimer potential energy surface. In contrast,
so-called extended Lagrangian molecular dynamics (ELMD) methods make an
approximation to exact classical dynamics in order to expedite the
calculations. ELMD methods—of which the most famous is Car–Parrinello
molecular dynamics—introduce a fictitious dynamics for the electronic
(orbital) degrees of freedom, which are then *propagated* alongside the
nuclear degrees of freedom, rather than *optimized* at each time step as
they are in a BOMD calculation. The fictitious electronic dynamics is
controlled by a fictitious mass parameter $\mu$, and the value of $\mu$
controls both the accuracy and the efficiency of the method. In the limit of
small $\mu$ the nuclei and the orbitals propagate adiabatically, and ELMD
mimics true classical dynamics. Larger values of $\mu$ slow down the
electronic dynamics, allowing for larger time steps (and more computationally
efficient dynamics), at the expense of an ever-greater approximation to true
classical dynamics.

**Q-Chem**’s ELMD algorithm is based upon propagating the density matrix,
expressed in a basis of atom-centered Gaussian orbitals, along
shortest-distance paths (geodesics) of the manifold of allowed density matrices
$\mathbf{P}$. Idempotency of $\mathbf{P}$ is maintained at every time step, by
construction, and thus our algorithm requires neither density matrix
purification, nor iterative solution for Lagrange multipliers (to enforce
orthogonality of the molecular orbitals). We call this procedure “curvy
steps” ELMD,[[558]](../bib_references/bib.md#bib572)
 and in a sense it is a time-dependent
implementation of the GDM algorithm (Section [4.5](../ch04_scf/sect_convergence.md)) for
converging SCF single-point calculations.

The extent to which ELMD constitutes a significant approximation to BOMD
continues to be debated. When assessing the accuracy of ELMD, the primary
consideration is whether there exists a separation of time scales between
nuclear oscillations, whose time scale $\tau_{\mathrm{nuc}}$ is set by the period
of the fastest vibrational frequency, and electronic oscillations, whose time
scale $\tau_{\mathrm{elec}}$ may be estimated according to[[558]](../bib_references/bib.md#bib572)

<a id="Ch9.E62"></a>

$$
\tau_{\mathrm{elec}}\geq\left(\frac{\mu}{\varepsilon_{\rm LUMO}-\varepsilon_{\rm HOMO}}\right)^{1/2} \tag{9.62}
$$

A conservative estimate, suggested in Ref. [[558]](../bib_references/bib.md#bib572)
, is that
essentially exact classical dynamics is attained when $\tau_{\mathrm{nuc}}>$ 10
$\tau_{\mathrm{elec}}$. In practice, we recommend careful benchmarking to insure
that ELMD faithfully reproduces the BOMD observables of interest.

Due to the existence of a fast time scale $\tau_{\mathrm{elec}}$, ELMD requires
smaller time steps than BOMD. When BOMD is combined with Fock matrix
extrapolation to accelerate convergence, it is no longer clear that ELMD
methods are substantially more efficient, at least in Gaussian basis
sets.[[559]](../bib_references/bib.md#bib573)

The following *$rem* variables are required for ELMD jobs:

AIMD_FICT_MASS

### `AIMD_FICT_MASS`

> **Specifies the value of the fictitious electronic mass $\mu$ , in atomic units, where $\mu$ has dimensions of (energy) $\times$ (time) ${}^{2}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * User-specified
> * **Recommendation**: Values in the range of 50–200 a.u. have been employed in test calculations; consult Ref. 558 Herbert J. M., Head-Gordon M. J. Chem. Phys. (2004) , 121 , pp. 11542 . Link for examples and discussion.

AIMD_PRINT

### `AIMD_PRINT`

> **Specifies the verbosity of the output in AIMD.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * User-specified
> * **Recommendation**: Higher values result in more verbose output.
