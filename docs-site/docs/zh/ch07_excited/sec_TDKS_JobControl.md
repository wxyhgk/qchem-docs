---
title: "7.4.2 Job Control"
---

## 7.4.2 Job Control

(July 4, 2026)

Only two TDKS job-control variables belong in the *$rem* section: TDKS = TRUE to request such a
calculation, and (optionally) TDKS_RESTART = TRUE to resume a previous time propagation.
All other job control relies on a *$tdks* input section that is described below. The propagator algorithms are described
in detail in Ref. [[1578]](../bib_references/bib.md#bib1641)
 and the use of TDKS to obtain broadband spectra is described in
Refs. [[1578]](../bib_references/bib.md#bib1641)
 and [[566]](../bib_references/bib.md#bib585)
.

## 7.4.2.1 Basics: Propagators and Time Step

Assuming that TDKS_RESTART = FALSE, a
standard ground-state SCF calculation is performed first in order to obtain the density at $t=0$. For this calculation, the value of
SCF_CONVERGENCE needs to be set reasonably tightly because in the subsequent TDKS calculation the
density will be perturbed by an external field (to generate the time-dependent superposition state) so any convergence
error in the initial density needs to be smaller than the perturbation-induced fluctuations that one is trying to integrate
in the TDKS time-propagation steps. The use of incremental Fock builds (INCFOCK = TRUE) is
recommended to reduce the cost of the numerous Fock builds, which are closely spaced in time.
The input file for a basic TDKS propagation is illustrated in the following example. The basic job is relatively simple but
sophisticated jobs require additional input files, and generate additional output.

???+ example "Example 7.33: Basic TDKS job."
    ```qchem
    $molecule
       0 1
       O 0.000000 0.000000 0.000000
       H 0.758602 0.000000 0.504284
       H 0.758602 0.000000 -0.504284
    $end
    
    $rem
       METHOD            pbe0
       BASIS             6-31G*
       TDKS              true
       SCF_CONVERGENCE   7
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```

Numerous time steps are required for most practical applications of the TDKS approach and therefore a restart capability
is provided. A long dynamics simulation can therefore be executed in segments (*e.g.*, to sidestep wall-time limits on
shared computing resources), by setting TDKS_RESTART = TRUE in the *$rem* section.
Results from the previous job are stored in the scratch directory and the next job is started by reading the data from the
same directory, picking up where the previous time propagation left off. As such, the `-save` flag is required for the
subsequent **Q-Chem** job, and the scratch directory should be given the same name for both jobs.
By default, the intermediate results are automatically stored every 1,000 steps. If the job is stopped accidentally before
reaching the requested number of time steps, it can be easily be restarted from the last saved step.

TDKS_RESTART

### `TDKS_RESTART`

> **Restart the calculation by continuing the previous job**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * The TDKS calculation continues from the previous calculation.
>     * FALSE
>     * The TDKS calculation starts from the beginning.
> * **Recommendation**: None.

???+ example "Example 7.34: TDKS calculation illustrating restart capability."
    ```qchem
    $molecule
       0 1
       H    0.000000   0.000000   0.000000
       H    0.000000   0.000000   0.750000
    $end
    
    $rem
       METHOD            pbe
       BASIS             6-31G
       SCF_CONVERGENCE   9
       TDKS_RESTART      0
       TDKS              1
       INTEGRAL_SYMMETRY false
    $end
    
    $tdks
       dt                0.05
       maxiter           25
       propagator        MMUT
       field_vector      1 1 1
       field_type        delta
       field_amp         0.0001
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            pbe
       BASIS             6-31G
       SCF_CONVERGENCE   9
       TDKS_RESTART      1
       TDKS              1
       SCF_GUESS         read
       INTEGRAL_SYMMETRY false
    $end
    
    $tdks
       dt                0.05
       maxiter           25
       propagator        MMUT
       field_vector      1 1 1
       field_type        delta
       field_amp         0.0001
    $end
    ```

The remaining job control parameters belong in the *$tdks* input section.

### `dt`

> **The value for the time step $\Delta t$ , in atomic units. INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.02`
> * **Options**:
>     * $\Delta t>0$
> * **Recommendation**: $\Delta t=0.1$ a.u. for general-purpose calculation of broadband spectra at excitation energies $\hbar\omega<30$ eV. For higher energies, $\Delta t=\pi/(10\Delta E)$ (in atomic units) is a reliable choice.

### `MaxIter`

> **The max number of steps INPUT SECTION: $tdks**
>
> * **Type**: `INTEGER`
> * **Default**: `15000`
> * **Options**:
>     * $>0$
> * **Recommendation**: The total propagation length is $\Delta t\times\mbox{{\bf MaxIter}}$ .

### `Propagator`

> **Time propagation algorithm INPUT SECTION: $tdks**
>
> * **Type**: `STRING`
> * **Default**: `MMUT`
> * **Options**:
>     * EULER
>     * Euler method
>     * MMUT
>     * Modified mid-point unitary transformation method
>     * LFLPPC
>     * Linear Fock, linear density predictor/corrector method
>     * EPPC
>     * Exponential density predictor/corrector method
> * **Recommendation**: Use MMUT, LFLPPC, or EPPC. (The Euler method is not recommended.) The two predictor/corrector methods provide stable dynamics using larger time steps as compared to MMUT, and furthermore provide on-the-fly consistency checks on the stability of the dynamics, but these algorithms are more expensive than MMUT on a per-step basis.

### `PC_Fock_Thresh`

> **Fock matrix threshold for consistency checking in predictor/corrector algorithms. INPUT SECTION: $tdks**
>
> * **Type**: `INTEGER`
> * **Default**: `7 (for`
> * **Options**:
>     * > 0
> * **Recommendation**: None.

### `PC_Den_Thresh`

> **Density matrix threshold for consistency checking in predictor/corrector algorithms. INPUT SECTION: $tdks**
>
> * **Type**: `INTEGER`
> * **Default**: `7 (for`
> * **Options**:
>     * > 0
> * **Recommendation**: None.

### `PC_Max_Iter`

> **Maximum number of self-consistent iterations (per time step) for predictor-corrector methods INPUT SECTION: $tdks**
>
> * **Type**: `INTEGER`
> * **Default**: `20`
> * **Options**:
>     * > 0
> * **Recommendation**: None.

## 7.4.2.2 Perturbing Field

The TDKS approach is based on applying a perturbing electric field $\bm{\mathcal{E}}$ to a (previously field-free)
ground state $|\Psi_{0}\rangle$. The perturbation generates a
superposition of all symmetry-allowed excited states $|\Psi_{n}\rangle$, *i.e.*,
those having a non-vanishing matrix element $\langle\Psi_{n}|\bm{\mathcal{E}}|\Psi_{0}\rangle$. Several choices for the perturbing
field are available, and this choice is specified by means of the **Field_Type** keyword in the *$tdks* input section.
(Additional job control parameters are required for some field types, as described below.)

### `Field_Type`

> **The external applied field INPUT SECTION: $tdks**
>
> * **Type**: `STRING`
> * **Default**: `DELTA`
> * **Options**:
>     * DELTA
>     * $\delta$
>     * -function kick
>     * CW
>     * continuous-wave field
>     * IMPULSE
>     * impulse field (Gaussian envelope)
>     * IMPULSE2
>     * impulse field (cosine-squared envelope)
>     * STATIC
>     * static field
>     * NONE
>     * no field
> * **Recommendation**: None.

These choices for **Field_Type** can be summarized as follows.
Note that $\bm{\mathcal{E}}=(\mathcal{E}_{x},\mathcal{E}_{y},\mathcal{E}_{z})$ is a vector quantity whose magnitude is controlled
by **Field_Amp** and whose direction is controlled by **Field_Vector**.

- •

**Delta** simulates a Dirac $\delta$-function kick, with the field $\bm{\mathcal{E}}$ turned on (at a constant
amplitude) only during the first two time steps.
The amplitude is controlled by the **Field_Amp** keyword that is documented below.
In order to normalize across different choices of $\Delta t$, **Field_Amp** actually specifies the *integrated*
field intensity $\bm{\mathcal{E}}\Delta t$, meaning that the electric field intensity itself is
(**Field_Amp**)/$(\Delta t)$.[[566]](../bib_references/bib.md#bib585)

That way, **Field_Amp** controls the total amount of energy that is put into this system by the $\delta$-function impulse,
which is the only way that results from simulations with two different time steps can be compared side-by-side.
- •

**CW** simulates a continuous-wave electric field of the form
$\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\sin(\omega t)$, whose amplitude $\mathbf{A}_{0}$ and frequency $\omega$ are set using
the keywords **Field_Amp** and **Field_Frequency**, respectively, in the *$tdks* section.
- •

The **Impulse** field has a Gaussian envelope,

<a id="Ch7.E60"></a>
$$
\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\exp\left(\frac{(t-t_{\text{peak}})^{2}}{2\tau^{2}}\right)\sin(\omega t) \tag{7.60}
$$

with $\mathbf{A}_{0}$ and frequency $\omega$ set using **Field_Amp** and **Field_Frequency**, respectively.
The field parameters $\tau$ and $t_{\text{peak}}$ are set using **Field_Tau** and **Field_Peak**,
respectively, in the *$tdks* section. The direction $\mathbf{A}_{0}$ is set using **Field_Vector**.
- •

The **Impulse2** field has a cosine-squared envelope, with the field $\bm{\mathcal{E}}$ turned on initially and turned off at $t=2t_{\text{peak}}$. For $0\leq t\leq 2t_{\text{peak}}$,

<a id="Ch7.E61"></a>
$$
\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\cos^{2}\left[\frac{\pi}{2t_{\text{peak}}}(t_{\text{peak}}-t)\right]\cos[\omega(t-t_{\text{peak}})] \tag{7.61}
$$

with $\mathbf{A}_{0}$ and frequency $\omega$ set using **Field_Amp** and **Field_Frequency**, respectively.
The field parameter $t_{\text{peak}}$ is set using **Field_Peak**
in the *$tdks* section. The direction $\mathbf{A}_{0}$ is set using **Field_Vector**.

### `Field_Vector`

> **The direction of the external applied field vector INPUT SECTION: $tdks**
>
> * **Type**: `VECTOR`
> * **Default**: `1.0 1.0 1.0`
> * **Options**:
>     * NONE
> * **Recommendation**: NONE

### `Field_Amp`

> **The amplitude of the external field (in a.u.) INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.0001`
> * **Options**:
>     * NONE
> * **Recommendation**: Values of $10^{-3}$ – $10^{-4}$ a.u. correspond to weak fields and are appropriate for simulating absorption spectra ( i.e. , within the linear-response regime but without the root-by-root calculation that is required for LR-TDDFT. Larger field amplitudes correspond to strong-field dynamics, as for example in second harmonic generation.

### `Field_Frequency`

> **The frequency $\omega$ of the external field, in eV units. INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.001`
> * **Options**:
>     * NONE
> * **Recommendation**: The use of energy units is for convenience when using the TDKS to generate broadband spectra.

### `Field_Peak`

> **The peak position $t_{\text{peak}}$ (in a.u. of time) for the Gaussian or cosine-squared impulse field. INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.0`
> * **Options**:
>     * NONE
> * **Recommendation**: NONE

### `Field_Tau`

> **The value of $\tau$ (in a.u. of time) for the Gaussian impulse field. INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.7`
> * **Options**:
>     * NONE
> * **Recommendation**: NONE

## 7.4.2.3 Complex Absorbing Potential

Simulations of broadband spectra at high energies (*e.g.*, for x-ray absorption spectroscopy at the K-edge,
corresponding to 1s $\rightarrow$ virtual excitations), the requisite electron dynamics often corresponds to fluctuations
that take the density out to the edge of the region of space that is spanned by the Gaussian basis set. The edge of the
basis set imposes an artificial potential wall, and a time-dependent wave packet can reflect off of this wall and then
interfere with its own outgoing wave, in an artificial manner that simply reflects the finite-basis approximation.[[1579]](../bib_references/bib.md#bib1642)

In practice, this can introduce artificial oscillations into broadband spectra obtained from TDKS calculations.
The same is true in TDKS simulations of strong-field electron dynamics, such as high harmonic generation.[[1579]](../bib_references/bib.md#bib1642)

These unwanted artifacts can be removed by the introduction of a complex absorbing potential (CAP) that annihilates the
outgoing wave that encounters it.

For TDKS calculations, the CAP that is available is constructed from a sum of spherical, overlapping atom-centered
potentials.[[1579]](../bib_references/bib.md#bib1642)

Within each of these, the potential is zero within a cutoff radius $r_{0}$ around $\mathbf{R}_{k}$, the position of atom $k$. Outside of
that radius, the potential rises quadratically with curvature $\eta$.
This is implemented using a set of atom-centered CAP functions

<a id="eqn:fk_CAP"></a>
$$
f^{\text{CAP}}_{k}(\mathbf{r})=\begin{cases}0,&\|\mathbf{r}-\mathbf{R}_{k}\|<r_{0}\\
\eta\big{(}\|\mathbf{r}-\mathbf{R}_{k}\|-r_{0}\big{)}^{2},&\|\mathbf{r}-\mathbf{R}_{k}\|\geq r_{0}\end{cases}\;. \tag{7.62}
$$

At any point $\mathbf{r}$ in space, the value of the CAP is taken to be $\text{i}\upsilon_{\text{CAP}}(\mathbf{r})$, where
$\upsilon_{\text{CAP}}(\mathbf{r})$ is the minimum of the various atom-centered potentials and a cutoff
$E_{\text{max}}=10~{}E_{h}$, the latter of which is used to avoid numerical overflow problems. All together,

<a id="Ch7.E63"></a>
$$
\upsilon_{\text{CAP}}(\mathbf{r})=\min\big{\{}E_{\text{max}},f_{1}^{\text{CAP}}(\mathbf{r}),f_{2}^{\text{CAP}}(\mathbf{r}),\ldots,\big{\}}\;. \tag{7.63}
$$

The value of $r_{0}$ is user-specifiable and should probably be tested for specific applications.
(For simulating strong-field ionization dynamics, a value
$r_{0}=3.5\times R_{\text{vdW}}$ has been used,[[716]](../bib_references/bib.md#bib748)

where $R_{\text{vdW}}$ is a representative atomic van der Waals radius.)
Note that placing $r_{0}$ beyond the extent of the Gaussian basis functions themselves will have no effect.
For a Gaussian basis function with exponent $\zeta$, the full width at half maximum of that function is

<a id="Ch7.E64"></a>
$$
\text{FWHM}(\zeta)=2\left(\frac{\ln 2}{\zeta}\right)^{1/2}\;, \tag{7.64}
$$

and half that value is therefore a measure of the radial extent of the basis function in question.
This can be used to estimate the spatial extent of the basis, taking $\zeta$ to be the smallest (most diffuse) exponent.

Note that when basis function information is requested using
PRINT_GENERAL_BASIS = TRUE, the exponents $\zeta$ are printed in atomic units of $a_{0}^{-2}$.

The following variables in the *$tdks* input section control the use of a CAP in TDKS calculations.

### `Do_CAP`

> **Activate a complex absorbing potential for TDKS calculations INPUT SECTION: $tdks**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * TRUE
>     * Use a CAP
>     * FALSE
>     * Do not use a CAP
> * **Recommendation**: None.

### `CAP_R0`

> **Cutoff radius for the CAP (in a.u.) INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `0`
> * **Options**:
>     * > 0
> * **Recommendation**: A value greater than twice the largest atomic van der Waals radius is recommended and should be tested as needed.

### `CAP_Eta`

> **Specifies the curvature of the CAP INPUT SECTION: $tdks**
>
> * **Type**: `DOUBLE`
> * **Default**: `1.0`
> * **Options**:
>     * > 0
> * **Recommendation**: Values of 4.0–5.0 are typical but testing is recommended.
