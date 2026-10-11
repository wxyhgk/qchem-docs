---
title: "10.8.7 Vibrationally-Resolved Electronic and Resonance Raman Spectra"
---

## 10.8.7 Vibrationally-Resolved Electronic and Resonance Raman Spectra

(July 4, 2026)

Optical spectroscopy is the study of the interaction between the light and
matter, and the study that encompasses a wide range of physical and chemical
behavior, which can be directly recorded by the spectrometers. Contemporary
spectroscopic techniques have been applied to widespread research fields
and have served as a popular tool to obtain the information of structural and
dynamical features of the matter.
However, the experimentally-measured spectra can’t straightforwardly give the
microscopic information of the matter. The theoretical calculations of the
spectra can serve as a supplementary tool to the experimental measurements
and provide a deeper understanding on the underlying physical and
chemical phenomena.[[1060]](../bib_references/bib.md#bib1105)

One can easily determine geometrical, electronic and dynamical features of
matters through a comparison between the experimental results and the calculated
values. Moreover, the role of different effects in spectroscopic properties can
also be quantified by the calculations.

Vibrationally-resolved one-photon absorption (OPA) and emission (OPE)
spectra and resonance Raman scattering (RRS) spectra, each of which involves
simultaneous changes in the vibrational and electronic states of a molecule,
can reveal a reliable molecular structure–property relationship. Theoretical
prediction of these spectra needs to combine both the electronic
structure theories and quantum dynamics methods to obtain the structure
parameters and describe quantum dynamics,
respectively.[[1288]](../bib_references/bib.md#bib1343)

For RRS simulation using the IMDHO model (which neglects Duschinsky rotation), see Section [10.8.6](subsec_RR-IMDHO.md).

## 10.8.7.1 Time-dependent approach to simulating spectra

On the basis of perturbation theory, the transition rate of one- or two-photon
transition processes from the initial state $|I\rangle$ to the final state
$|F\rangle$ is proportional to $k_{IF}=|\langle F|\hat{M}|I\rangle|^{2}\delta(\Delta\omega)$, where $\delta(\Delta\omega)$ is the line shape
function with $\Delta\omega=\omega_{i}-\omega_{FI}$ for a one-photon
transition and $\Delta\omega=\omega_{1}+\omega_{2}-\omega_{FI}$ for a
two-photon process. Here $\omega_{i}$, $\omega_{1}$, and $\omega_{2}$ denote the
incident photon frequencies and the operator $\hat{M}$ is given by

<a id="Ch10.E82"></a>
$$
\hat{M}=\begin{cases}\hat{\mu}&\text{(one-photon transition)}\\
\sum_{L}\left[\frac{{\bf\mu}\cdot\hat{e}_{2}|L\rangle\langle L|{\bf\mu}\cdot\hat{e}_{1}}{(\omega_{1}-\omega_{LI})}+\frac{{\bf\mu}\cdot\hat{e}_{1}|L\rangle\langle L|{\bf\mu}\cdot\hat{e}_{2}}{(\omega_{2}-\omega_{LI})}\right]&\text{(two-photon transition)}\end{cases}\;. \tag{10.82}
$$

In the two-photon case there are intermediate or “virtual” states $|L\rangle$.

Raman scattering is a two-photon process. In this process, one photon with
the frequency $\omega_{i}$ is absorbed, another photon with the frequency
$\omega_{S}$ is emitted, and the transition from the initial to the final
vibrational states takes place. Based on perturbation theory, the transition
rate of the Raman process is proportional to
$S(\omega_{i},\omega_{S})=|\langle F|\hat{M}|I\rangle|^{2}\delta(\Delta\omega)$, where

<a id="A3.S8.EGx80"></a>
$$
\displaystyle\hat{M}=\sum_{L}\left[\dfrac{\mu\cdot\hat{e}_{2}|L\rangle\langle L|\mu\cdot\hat{e}_{1}}{(\omega_{i}-\omega_{LI})}-\dfrac{\mu\cdot\hat{e}_{1}|L\rangle\langle L|\mu\cdot\hat{e}_{2}}{(\omega_{S}+\omega_{LI})}\right] \tag{10.83}
$$

and $\Delta\omega=\omega_{S}-\omega_{i}+\omega_{FI}$.
The differential photon scattering cross section
is given by[[35]](../bib_references/bib.md#bib18)

<a id="rrs1"></a>
$$
\sigma(\omega_{i},\omega_{S})\propto\frac{4\omega_{i}\omega_{S}^{3}}{9c^{4}}S(\omega_{i},\omega_{S}). \tag{10.84}
$$

RRS spectroscopy is a type of vibrational Raman spectroscopy in which the
incident laser frequency is close to an electronic transition of the molecule
or crystal studied. As the adiabatic energy gap $\omega_{LI}$ between the $L$
state and the initial $I$ state is close to the laser frequency $\omega_{i}$, the
intermediate $L$ state will make the dominant contribution to RRS. Under the
“resonant” condition, the contributions from the non-resonant electronic
states can be neglected.

One may evaluate $M_{IF}=\langle\Phi_{F}|\hat{M}|\Phi_{I}\rangle$ by making use of
the Herzberg-Teller (HT) expansion, *i.e.*, one expands the integrals about the
nuclear equilibrium configuration $Q=0$. Writing the pure-spin Born–Oppenheimer (psBO)
functions as products of an electronic wave function
$\Psi$ and a vibrational wave function $\Lambda$

<a id="Ch10.E85"></a>
$$
\Phi_{n}(q,Q)=\Psi_{n}(q,Q)\Lambda_{n}(Q)\;, \tag{10.85}
$$

we have

<a id="A3.S8.EGx81"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Psi_{n}(q,Q)&\displaystyle=\Psi_{n}(q,0)+[\partial{\Psi_{n}(q,0)}/{\partial Q}]_{Q=0}Q+\cdots\;,\\
\displaystyle M_{IF}&\displaystyle=M_{IF}(Q=0)+[\partial{M_{IF}}/{\partial Q}]_{Q=0}Q+\cdots\;.\end{aligned} \tag{10.86}
$$

The second term in Eq. ([10.86](#HT1)) origins from the HT expansion. If we
truncate the expansions after the lowest-order non-vanishing term, $M_{IF}$ can
be written as

<a id="A3.S8.EGx82"></a>
$$
\displaystyle M_{IF} \tag{10.87}
$$

If the first term, the direct transition, vanishes, this process is orbitally forbidden.

To evaluate the vibrational terms in the remaining part of the vibronic matrix
elements, we can use the harmonic oscillator approximation. Then the
vibrational part of the wave function is written as
$\Lambda_{n}=\prod^{N}_{k=1}\chi_{k}^{(n)}(\nu_{n})$,
where $N$ is the total number of normal modes $\chi_{k}$ and $\nu_{n}$
the vibrational quantum number associated with mode
$k$ in state $|n\rangle$.

The delta function $\delta(\Delta\omega)$ can be expressed as the Fourier integral

<a id="eq4"></a>
$$
\delta(\Delta\omega)=\frac{1}{2\pi\hbar}\int_{-\infty}^{+\infty}\mathrm{e}^{(i\Delta\omega)t/\hbar}\,dt\;, \tag{10.88}
$$

and then the transition rate from the initial state to the final state becomes

<a id="eq:rate2"></a>
$$
k_{IF}=\int_{-\infty}^{+\infty}\exp[i(\omega_{0}+E_{i}-E_{f})t/\hbar-\gamma t]C_{i}(t)dt \tag{10.89}
$$

where $\gamma$ is a damping factor and

<a id="Ch10.E90"></a>
$$
C_{i}(t)=\frac{\mbox{tr}[e^{-\beta\hat{H}_{i}}\mathrm{e}^{i\hat{H}_{i}t/\hbar}\hat{M}e^{-iH_{f}t/\hbar}\hat{M})}{\mbox{tr}[\mathrm{e}^{-\beta\hat{H}_{i}}]}\;. \tag{10.90}
$$

Here $\beta=1/k_{B}T$, $\omega_{0}=\omega_{i}$ in one-photon absorption and
emission processes, $\omega_{0}=\omega_{i}-\omega_{S}$ in Raman scattering process. The notation
$\mbox{tr}(\cdots)$ represents a trace over nuclear and electronic
degrees of freedom, and $\hat{M}=|\Lambda_{i}\rangle M_{IF}\langle\Lambda_{f}|+|\Lambda_{f}\rangle M_{FI}\langle\Lambda_{i}|$. The quantities
$\hat{H}_{i}$ and $\hat{H}_{f}$ denote the nuclear Hamiltonians of electronic ground
and excited states, respectively.

The Hamiltonian of vibrational motions on the ground and excited states can be written as

<a id="Ch10.E91"></a>
$$
\displaystyle H_{g} \tag{10.91a}
$$

where $P$ and $Q$ are the momenta and coordinates of vibrational normal modes,
respectively. The normal mode coordinates of ground and excited states are
correlated by the Duschinsky rotation matrix $\bar{D}$,

with $Q_{e}=\bar{D}Q_{g}+\bar{\Delta}$. The quantity $\bar{\Delta}$ is the displacement of
normal mode coordinates between ground and excited states, *i.e.*, the same quantity that appears in the
IMDHO theory of Section [10.8.6](subsec_RR-IMDHO.md), Eq. ([10.76](subsec_RR-IMDHO.md#eq:Delta_k)). The dimensionless
forms are correspondingly $\Delta_{j}=(\omega_{j}^{e})^{1/2}\bar{\Delta}_{j}$ and
$D_{ij}=(\omega_{i}^{e}/\omega_{j}^{g})^{1/2}\bar{D}_{ij}$.
From the above, the transition rate can be calculated directly in the time
domain using the correlation function approach. This time-dependent approach
has been implemented to calculate vibronic spectra.[[867]](../bib_references/bib.md#bib902)

It is obvious that ground and excited electronic states have different potential energy surfaces leading
to different vibrational frequencies and normal modes. The relation between mass-weighted Cartesian displacement
coordinates $x$ and normal mode coordinates $Q$ is given by

<a id="A3.S8.EGx84"></a>
$$
\displaystyle\begin{aligned} \displaystyle x^{g}-x_{0}^{g}&\displaystyle=L_{g}Q_{g}\;,\\
\displaystyle x^{e}-x_{0}^{e}&\displaystyle=L_{e}Q_{e}\;,\end{aligned} \tag{10.92}
$$

where $x_{0}^{g}$ and $x_{0}^{e}$ are the equilibrium structures of ground and excited
states. For an ideal $N$-dimensional harmonic oscillator, the normal mode
coordinates of ground and excited states are related by

<a id="A3.S8.EGx85"></a>
$$
\displaystyle\begin{aligned} \displaystyle Q_{e}&\displaystyle=(L_{e})^{\top}L_{g}Q_{g}+(L_{e})\top(x_{0}^{g}-x_{0}^{e})\\
&\displaystyle=\bar{D}Q_{g}+\bar{\Delta}\;.\end{aligned} \tag{10.93}
$$

The minimum points on the potential surface and the Hessian matrix are required to calculate
the Duschinsky rotation matrix and displacement vector. It can be time-consuming to
calculate the excited-state potential surface, especially for large molecules, and often problematic due to state
crossings. The linear coupling model (LCM), which is also known as the vertical gradient (VG) approximation, has been
proposed to avoid this issue.[[219]](../bib_references/bib.md#bib214)
 Assuming that the excited-state potential surface
is approximated by a shift in the ground state PES, namely $\omega_{j}^{e}=\omega_{j}^{g}$ and $L_{e}=L_{g}$,
the displacement of $Q_{j}$ can be calculated by the excited-state energy gradient
$(\partial E/\partial Q)_{j}$ and $\Delta^{\!\text{VG}}$ can be written as

<a id="eq:VG"></a>
$$
\Delta_{j}^{\!\text{VG}}=(\omega_{j}^{g})^{-3/2}\left(\frac{\partial E}{\partial Q}\right)_{j}=\sum\limits_{i}(\omega_{j}^{g})^{-3/2}\left(\frac{\partial E}{\partial x_{i}}\right)L^{ij}_{g}. \tag{10.94}
$$

The VG approximation is equivalent to the IMDHO approximation that is discussed in
Section [10.8.6](subsec_RR-IMDHO.md).[[665]](../bib_references/bib.md#bib689)

Generally, the Franck-Condon (FC) approximation is accurate enough for
strongly one- or two-photon allowed transitions, while it breaks down for
forbidden or weakly allowed transitions, and the FC term becomes nearly zero.
In this situation, a correction to this deviation should be introduced by
including the Herzberg-Teller (HT) or non-Condon
effect.[[831]](../bib_references/bib.md#bib863)

HT-type vibronic coupling comes from the normal mode-coordinate dependence of
the transition moments. When these quantities are expanded
in terms of the normal mode coordinates, the contribution of the
linear-coordinate-dependent terms is commonly called HT effect.[[35]](../bib_references/bib.md#bib18)

Many works, whether or not they
account for the mode-mixing or Duschinsky rotation (DR)
effect or not, have shown the importance of the HT
effect in OPA, OPE, and RRS spectra.[[824]](../bib_references/bib.md#bib862)

To predict OPA, OPE and RRS spectra, electronic structure calculations on ground
and excited states should be performed. The necessary jobs at different level of
approximation are summarized in the following:

- •

FC. This is available for OPA, OPE, and RRS spectra.

1. 1.

$x_{0}^{g}\neq x_{0}^{e}$, $L_{g}=L_{e}$, and $\omega^{g}=\omega^{e}$. Geometry
optimization on excited state potential surface is performed, followed by ground state
optimization and frequency analysis.
2. 2.

$x_{0}^{g}\neq x_{0}^{e}$, $L_{g}\neq L_{e}$, and $\omega^{g}\neq\omega^{e}$.
Geometry optimization and frequency calculation are needed on both
ground and excited states.
- •

FCHT. This is available for OPA, OPE, and RRS spectra.

- •

$x_{0}^{g}\neq x_{0}^{e}$, $L_{g}\neq L_{e}$, and $\omega^{g}\neq\omega^{e}$. It is similar to the second kind of FC calculation, in which
transition dipole derivative is obtained via frequency calculation on
excited state. Geometry optimization and frequency calculation are
needed on both ground and excited states.
- •

VG. This is available for OPA and RRS spectra.

- •

$x_{0}^{g}=x_{0}^{e}$, $L_{g}=L_{e}$, and $\omega^{g}=\omega^{e}$.
Only the geometry optimization and frequency calculation of the ground
state is involved. Frequencies and normal modes of excited state are
assumed to be the same as ground state. The displacement vector is
approximated by Eq. ([10.94](#eq:VG)), in which the gradient of excited
state potential surface is produced by excited state force job. Of course VG model has
only contribution from FC term.

## 10.8.7.2 Job Control

Since both ground state and excited state parameters are required, the routines
to predict vibronic spectra are designed to have two steps. Firstly excited
state calculation is performed and information about excited state will be
saved in `$QCSCRATCH/savename`. Then the vibronic spectra utility is
called to simulate the requested spectra after frequency analysis on ground
state. POINT_GROUP_SYMMETRY should be set to FALSE in order to prevent the
molecular geometry being transformed to the standard orientation.
Therefore the vibronic spectra job input can be set up in two ways. First, the
multiple jobs can be separated by the string `@@@` as described in
Section [3.5](../ch03_inputs/sec_multiple_jobs.md). Or, jobs can be separated into individual inputs
using `$QCSCRATCH/savename` as described below and
given as examples [10.8.7.3](#ex:VibronicPFB1) and [10.8.7.3](#ex:VibronicPFB1).

> ```qchem
> qchem infile_excited_state outfile_excited_state savename
> qchem infile_ground_state outfile_ground_state savename
> ```

There are two *$rem* variables and one section *$vibronic*
involved in vibronic spectra calculations.

SAVE_VIBRONIC_PARAMS

### `SAVE_VIBRONIC_PARAMS`

> **Save information about excited state which is requested in vibronic spectra simulation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
> * **Recommendation**: TRUE

VIBRONIC_SPECTRA

### `VIBRONIC_SPECTRA`

> **Specifies which type of vibronic spectra will be predicted. Should be used in a frequency job (jobtype = Freq).**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * No vibronic spectra is predicted.
>     * 1
>     * OPA spectra is calculated.
>     * 2
>     * OPE spectra is calculated.
>     * 3
>     * RRS spectra is calculated.
> * **Recommendation**: Use the default.

Variables in the *$vibronic* section:

### `MODEL`

> **Specifies which kind of model will be used to simulate the vibronic spectra. INPUT SECTION: $vibronic**
>
> * **Type**: `INTEGER`
> * **Default**: `-1`
> * **Options**:
>     * 1
>     * FC.
>     * 2
>     * FCHT.
>     * 3
>     * VG.
> * **Recommendation**: User defined

### `TEMPERATURE`

> **Specifies the temperature in the vibronic spectra simulation. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT`
> * **Default**: `$298.15$`
> * **Options**:
>     * $t$
>     * temperature, in K.
> * **Recommendation**: User defined

### `FREQ_RANGE`

> **Specifies the frequency range of vibronic spectra. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT`
> * **Default**: `$1.0\ 40000.0\ 10.0$`
> * **Options**:
>     * $\nu_{\text{min}}\ \nu_{\text{max}}\ \delta\nu$
>     * minimum, maximum and step size, in
>     * $\text{cm}^{-1}$
>     * .
> * **Recommendation**: User defined

### `TIME_RANGE`

> **Specifies the step size and the number of steps in time domain propagation. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT and INTEGER`
> * **Default**: `$1.0\ 40000$`
> * **Options**:
>     * $\delta t\ n_{\text{step}}$
>     * time step size in a.u., and the number of steps.
> * **Recommendation**: User defined

### `DAMPING`

> **Specifies the damping factor. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT`
> * **Default**: `$300.0$`
> * **Options**:
>     * $\gamma$
>     * damping factor, in
>     * $\text{cm}^{-1}$
>     * .
> * **Recommendation**: User defined

### `FREQ_SCALE_FACTOR`

> **Specifies the frequency scale factors. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT`
> * **Default**: `$1.0\ 1.0\ 1.0\ 1.0$`
> * **Options**:
>     * $\lambda_{\text{H}}^{g}\ \lambda_{\text{H}}^{e}\ \lambda_{\text{ZPE}}^{g}\ \lambda_{\text{ZPE}}^{e}$
>     * scale factor for ground state harmonic frequency,
>     * for excited state harmonic frequency, for ground state zero-point energy,
>     * and for excited state zero-point energy
> * **Recommendation**: User defined

### `EPSILON`

> **Specifies the spectral broadening factor. It is available only for RRS spectra simulation. INPUT SECTION: $vibronic**
>
> * **Type**: `FLOAT`
> * **Default**: `$25.0$`
> * **Options**:
>     * $\varepsilon$
>     * broadening factor, in
>     * $\text{cm}^{-1}$
>     * .
> * **Recommendation**: User defined

## 10.8.7.3 Vibronic Job Examples

???+ example "Example 10.45: Input files for OPA spectra in the FCHT approximation of formaldehyde
corresponding to the $S_{0}\rightarrow S_{1}$ transition. In the first step,
frequency analysis at the $S_{1}$ equilibrium geometry. Then run a ground
state frequency analysis on the $S_{0}$ ground state optimized structure."
    ```qchem
    $molecule
      0 1
      O    -0.0367447359    -0.0007590817     0.6963163574
      C     0.1461299638     0.0026846285    -0.5839700302
      H    -0.0732270514     0.9340547891    -1.1138640182
      H    -0.0391581765    -0.9359803358    -1.1140167891
    $end
    
    $rem
      JOBTYPE                freq
      METHOD                 b3lyp
      BASIS                  def2-TZVP
      CIS_STATE_DERIV        1
      CIS_SINGLETS           true
      CIS_TRIPLETS           false
      CIS_N_ROOTS            10
      SAVE_VIBRONIC_PARAMS   true ! enables saving information of S1 state
      MEM_TOTAL              5000
      POINT_GROUP_SYMMETRY   false
    $end
    
    @@@
    
    $molecule
       0 1
       O    0.0000000000     0.0000000000     0.6637077571
       C    0.0000000000     0.0000000000    -0.5351027012
       H    0.0000000000     0.9394749352    -1.1220697679
       H    0.0000000000    -0.9394749352    -1.1220697679
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-TZVP
       VIBRONIC_SPECTRA     1 !enables vibronic_spectra and reads saved information
       MEM_TOTAL            5000
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       model        2
       freq_range   20000. 60000. 10.
       time_range   1. 40000
       damping      40.
    $end
    ```

???+ example "Example 10.46: Vibrationally resolved fluorescence, i.e. , OPE with the first kind of FC model,
is calculated as following. The emission from $D_{1}$ to $D_{0}$ of p -fluorobenzyl radical is used as an example. This is the first job
of the total vibronic spectra simulation, by running the excited state
geometry optimization retaining information in $QCSCRATCH/savename .
Information from this job will be needed to complete the simulation in
Example 10.8.7.3 ."
    ```qchem
    $molecule
       0 2
       C         1.4840482200    0.0000338155    0.0000000000
       C         0.7160497031    0.0000524901   -1.2119311870
       C        -0.7159596058    0.0000542629   -1.2126930961
       C        -1.4043236629    0.0000543088    0.0000000000
       C        -0.7159596058    0.0000542629    1.2126930961
       C         0.7160497031    0.0000524901    1.2119311870
       C         2.8748450131    0.0000120580    0.0000000000
       H         1.2370230923    0.0000896598   -2.1693859212
       H        -1.2717579173    0.0000412967   -2.1497435961
       H        -1.2717579173    0.0000412967    2.1497435961
       H         1.2370230923    0.0000896598    2.1693859212
       H         3.4346492051    0.0000003003   -0.9330758768
       H         3.4346492051    0.0000003003    0.9330758768
       F        -2.7508602624    0.0000394216    0.0000000000
    $end
    
    $rem
       JOBTYPE                opt
       METHOD                 b3lyp
       BASIS                  def2-SVP
       CIS_STATE_DERIV        1
       CIS_N_ROOTS            10
       SAVE_VIBRONIC_PARAMS   true !saved into $QCSCRATCH/savename
       POINT_GROUP_SYMMETRY   false
    $end
    ```

???+ example "Example 10.47: The final job for obtaining vibrationally resolved fluorescence of the $D_{1}$ to $D_{0}$ transition of p -fluorobenzyl radical using OPE with
the first kind of FC model from Example 10.8.7.3 ."
    ```qchem
    $molecule
       0 2
       C       1.4578807306     0.0130092784     0.0000000000
       C       0.7102753558     0.0082793447    -1.2194714816
       C      -0.6772053823    -0.0007923729    -1.2210832164
       C      -1.3603507249    -0.0052928605     0.0000000000
       C      -0.6772053834    -0.0007923730     1.2210832170
       C       0.7102753546     0.0082793447     1.2194714789
       C       2.8669152234     0.0219746232     0.0000000000
       H       1.2502372081     0.0119050313    -2.1697312391
       H      -1.2498963812    -0.0045285858    -2.1510495277
       H      -1.2498963822    -0.0045285858     2.1510495285
       H       1.2502372136     0.0119050313     2.1697312323
       H       3.4299577819     0.0255536038    -0.9358170827
       H       3.4299577814     0.0255536038     0.9358170860
       F      -2.7010161586    -0.0142661666     0.0000000000
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-SVP
       VIBRONIC_SPECTRA     2
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       model        1
       temperature  0.
       freq_range   1. 40000. 10.
       time_range   1. 40000
       damping      20.
    $end
    ```

???+ example "Example 10.48: RRS spectra of phenoxyl radical ( $D_{0}\rightarrow D_{3}$ transition) with the VG
approximation. Therefore the first job calculates the $D_{3}$ state force at the
ground state optimized geometry, followed by the ground state frequency
analysis. The excited state forces and ground state frequencies are
calculated in the ground state equilibrium geometry."
    ```qchem
    $molecule
       0 2
       C       0.0000000000     1.2271514002    -1.0879472096
       C       0.0000000000     0.0000408897    -1.7873074655
       C       0.0000000000    -1.2270324440    -1.0880160727
       C       0.0000000000    -1.2409681161     0.2924435676
       C       0.0000000000    -0.0000313560     1.0551142042
       C       0.0000000000     1.2409428316     0.2924458686
       H       0.0000000000     2.1656442172    -1.6487551860
       H       0.0000000000    -0.0001767539    -2.8803293768
       H       0.0000000000    -2.1655968771    -1.6487220344
       H       0.0000000000    -2.1715667156     0.8648121894
       H       0.0000000000     2.1714692701     0.8649813475
       O       0.0000000000     0.0001236541     2.3063351676
    $end
    
    $rem
       JOBTYPE                force
       METHOD                 b3lyp
       BASIS                  def2-SVP
       CIS_STATE_DERIV        3
       CIS_N_ROOTS            10
       SAVE_VIBRONIC_PARAMS   true
       POINT_GROUP_SYMMETRY   false
    $end
    
    @@@
    
    $molecule
       read !VG approximation uses the same geometry for ground and excited state
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-SVP
       VIBRONIC_SPECTRA     3
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       MODEL         3
       TEMPERATURE   0.
       FREQ_RANGE    1. 4000. 1.
       TIME_RANGE    1. 40000
       DAMPING       100.
       EPSILON       25.
    $end
    ```
