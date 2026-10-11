---
title: "7.2.2 Configuration Interaction with Single Substitutions (CIS)"
---

## 7.2.2 Configuration Interaction with Single Substitutions (CIS)

(July 4, 2026)

## 7.2.2.1 Theory

The derivation of the CI-singles (CIS) energy and wave
function[[312]](../bib_references/bib.md#bib316)
 begins by selecting the HF
single-determinant wave function as reference for the ground state of the system:

<a id="eq600"></a>
$$
\Psi_{\mathrm{HF}}=\frac{1}{\sqrt{n!}}\det\left\{{\chi_{1}\chi{}_{2}\cdots\chi_{i}\chi{}_{j}\cdots\chi_{n}}\right\} \tag{7.1}
$$

where $n$ is the number of electrons, and the spin orbitals

<a id="eq601"></a>
$$
\chi_{i}=\sum\limits_{\mu}^{N}{c_{\mu i}\phi_{\mu}} \tag{7.2}
$$

are expanded in a finite basis of $N$ atomic orbital basis functions. Molecular
orbital coefficients $\{c_{\mu i}\}$ are usually found by SCF procedures which
solve the Hartree-Fock equations

<a id="eq602"></a>
$$
\mathbf{FC}=\bm{\varepsilon}\mathbf{SC}\;, \tag{7.3}
$$

where **S** is the overlap matrix, **C** is the matrix of molecular
orbital coefficients, $\varepsilon$ is a diagonal matrix of orbital
eigenvalues and **F** is the Fock matrix with elements

<a id="eq603"></a>
$$
F_{\mu\upsilon}=H_{\mu\upsilon}+\sum\limits_{\lambda\sigma}{\sum\limits_{i}{c_{\mu i}c_{\upsilon i}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)}} \tag{7.4}
$$

involving the core Hamiltonian and the anti-symmetrized two-electron integrals

<a id="Ch7.E5"></a>
$$
(\mu\mu||\lambda\sigma)=\int\int\phi_{\mu}(\mathbf{r}_{1})\phi_{\nu}(\mathbf{r}_{2})\left(\frac{1}{r_{12}}\right)\bigl{[}\phi_{\lambda}(\mathbf{r}_{1})\phi_{\sigma}(\mathbf{r}_{2})-\phi_{\sigma}(\mathbf{r}_{1})\phi_{\lambda}(\mathbf{r}_{2})\bigr{]}\;d\mathbf{r}_{1}\,d\mathbf{r}_{2} \tag{7.5}
$$

On solving Eq. ([7.3](#eq602)), the total energy of the ground state single
determinant can be expressed as

<a id="eq605"></a>
$$
E_{\mathrm{HF}}=\sum\limits_{\mu\upsilon}{P_{\mu\upsilon}^{\mathrm{HF}}H_{\mu\upsilon}}+\frac{1}{2}\sum\limits_{\mu\upsilon\lambda\sigma}{P_{\mu\upsilon}^{\mathrm{HF}}P_{\lambda\sigma}^{\mathrm{HF}}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)}+V_{\mathrm{nuc}} \tag{7.6}
$$

where $P^{\mathrm{HF}}$ is the HF density matrix and $V_{\mathrm{nuc}}$ is the nuclear
repulsion energy.

Equation ([7.1](#eq600)) represents only one of many possible determinants made
from orbitals of the system; there are in fact $n(N-n)$ possible singly
substituted determinants constructed by replacing an orbital occupied in the
ground state ($i$, $j$, $k,\ldots$) with an orbital unoccupied in the ground
state ($a$, $b$, $c,\ldots$). Such wave functions and energies can be written

<a id="eq606"></a>
$$
\Psi_{i}^{a}=\frac{1}{\sqrt{n!}}\det\left\{{\chi_{1}\chi{}_{2}\cdots\chi_{a}\chi{}_{j}\cdots\chi_{n}}\right\} \tag{7.7}
$$

<a id="eq607"></a>
$$
E_{ia}=E_{\mathrm{HF}}+\varepsilon_{a}-\varepsilon_{i}-\left({ia}\right.||\left.{ia}\right) \tag{7.8}
$$

where we have introduced the anti-symmetrized two-electron integrals in the
molecular orbital basis

<a id="eq608"></a>
$$
\left({pq}\right.||\left.{rs}\right)=\sum\limits_{\mu\upsilon\lambda\sigma}{c_{\mu p}c_{\upsilon q}c_{\lambda r}c_{\sigma s}\left({\mu\lambda}\right.||\left.{\upsilon\sigma}\right)} \tag{7.9}
$$

These singly excited wave functions and energies could be considered crude
approximations to the excited states of the system. However, determinants of
the form Eq. ([7.7](#eq606)) are deficient in that they:

- •

do not yield pure spin states
- •

resemble more closely ionization rather than excitation
- •

are not appropriate for excitation into degenerate states

These deficiencies can be partially overcome by representing the excited
state wave function as a linear combination of *all* possible singly excited
determinants,

<a id="eq:CIS-wavefn"></a>
$$
|\Psi_{\text{CIS}}\rangle=\sum_{ia}a_{i}^{a}|\Psi_{i}^{a}\rangle \tag{7.10}
$$

where the coefficients $\{a_{i}^{a}\}$ can be obtained by diagonalizing the orbital Hessian
matrix $\mathbf{A}$, which is equivalent to the Hamiltonian in the space of single excitations
with the ground-state energy removed. Its matrix elements are

<a id="eq:orbital-Hessian"></a>
$$
A_{ia,jb}=\langle\Psi_{i}^{a}|\hat{H}-E_{\text{HF}}|\Psi_{j}^{b}\rangle=(\varepsilon_{a}-\varepsilon_{j})\delta_{ij}\delta_{ab}-(ja||ib)\;. \tag{7.11}
$$

According to Brillouin’s, theorem single substitutions do not interact directly
with a reference HF determinant, so the resulting eigenvectors from the CIS
excited state represent a treatment roughly comparable to that of the HF ground
state. The excitation energy is simply the difference between HF ground state
energy and CIS excited state energies, and the eigenvectors of **A**
correspond to the amplitudes of the single-electron promotions.

CIS calculations can be performed in **Q-Chem** using restricted
(RCIS),[[312]](../bib_references/bib.md#bib316)
 unrestricted (UCIS), or restricted
open-shell[[919]](../bib_references/bib.md#bib955)
 (ROCIS) spin orbitals. See Section [7.2.4](sec_CIS-jobcontrol.md)
for a list of CIS-related job control variables.

???+ example "Example 7.1: A basic CIS excitation energy calculation on formaldehyde at the
HF/6-31G* optimized ground state geometry, which is obtained in the first part
of the job. Above the first singlet excited state, the states have Rydberg
character, and therefore a basis with two sets of diffuse functions is used."
    ```qchem
    $molecule
       0  1
       C
       O  1  CO
       H  1  CH  2  A
       H  1  CH  2  A  3  D
    
       CO =   1.2
       CH =   1.0
       A  = 120.0
       D  = 180.0
    $end
    
    $rem
       JOBTYPE   =  opt
       EXCHANGE  =  hf
       BASIS     =  6-31G*
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE      =  hf
       BASIS         =  6-311(2+)G*
       CIS_N_ROOTS   =  15            Do 15 states
       CIS_SINGLETS  =  true          Do do singlets
       CIS_TRIPLETS  =  false         Don’t do Triplets
    $end
    ```

## 7.2.2.2 CIS Analytical Derivatives

While CIS excitation energies are relatively inaccurate, with errors of the
order of 1 eV, CIS excited state properties, such as structures and
frequencies, are much more useful. This is very similar to the manner in
which ground state Hartree-Fock (HF) structures and frequencies are much
more accurate than HF relative energies. Generally speaking, for low-lying
excited states, it is expected that CIS vibrational frequencies will be
systematically 10% higher or so relative to
experiment.[[1290]](../bib_references/bib.md#bib1348)
 If the excited states are of
pure valence character, then basis set requirements are generally similar to
the ground state. Excited states with partial Rydberg character require the
addition of one or preferably two sets of diffuse functions.

**Q-Chem** includes efficient analytical first and second derivatives of the CIS
energy,[[921]](../bib_references/bib.md#bib958)
 to yield analytical gradients, excited
state vibrational frequencies, force constants, polarizabilities, and infrared
intensities. Analytical gradients can be evaluated for any job where the CIS
excitation energy calculation itself is feasible, so that efficient
excited-state geometry optimizations and vibrational frequency calculations are
possible at the CIS level. In such cases, it is necessary to specify on which
Born-Oppenheimer potential energy surface the optimization should proceed, and
care must be taken to ensure that the optimization remains on the excited state
of interest, as state crossings may occur. (A state-tracking algorithm,
as discussed in Section [9.8.5](../ch09_opt/sec_state_following.md), can aid with this.[[1549]](../bib_references/bib.md#bib1615)
)

Sometimes it is precisely the crossings between Born-Oppenheimer potential
energy surfaces (*i.e.*, conical intersections) that are of interest, as these
intersections provide pathways for nonadiabatic transitions between electronic
states.[[916]](../bib_references/bib.md#bib952)
 A feature of **Q-Chem** that is not
otherwise widely available in an analytic implementation (for both CIS and
TDDFT) of the nonadiabatic couplings that define the topology around conical
intersections.[[378]](../bib_references/bib.md#bib383)
 Due to the
analytic implementation, these couplings can be evaluated at a cost that is not
significantly greater than the cost of a CIS or TDDFT analytic gradient
calculation,[[1547]](../bib_references/bib.md#bib1613)

and the availability of these couplings allows for much more
efficient optimization of minimum-energy crossing points along seams of conical
intersection, as compared to when only analytic gradients are
available.[[1547]](../bib_references/bib.md#bib1613)
 These features, including a brief overview of the
theory of conical intersections, can be found in Section [9.8.1](../ch09_opt/subsec_NACMEs_and_CIs.md).

In some applications, access to gradients of several CIS or TDDFT electronic states
is desirable, which can be achieved using CIS_STATE_MULTIGRAD
*$rem* variable within JOB_TYPE = force.

For CIS vibrational frequencies, a semi-direct algorithm similar to that used
for ground-state Hartree-Fock frequencies is available, whose computer time
scales as approximately ${\cal{O}}({N^{3}})$ for large molecules.[[920]](../bib_references/bib.md#bib956)

The main complication associated with analytical CIS frequency calculations is
ensuring that **Q-Chem** has sufficient memory to perform the calculations.
Default settings are adequate for many purposes but if a large calculation
fails due to a memory limitation, then the following additional information may be useful.

The memory requirements for CIS (and HF) analytic frequencies primarily come
from dynamic memory, defined as

dynamic memory = MEM_TOTAL $-$ MEM_STATIC    .

This quantity must be large enough to contain several arrays whose size is $3N_{\rm atoms}N_{\rm basis}^{2}$. Meanwhile the value of the *$rem* variable
MEM_STATIC, which obviously reduces the available dynamic memory,
must be sufficiently large to permit integral evaluation, else the job may
fail. For most purposes, setting MEM_STATIC to about 80 MB is
sufficient, and by default MEM_TOTAL is set to a larger value that
what is available on most computers, so that the user need not guess or
experiment about an appropriate value of MEM_TOTAL for low-memory
jobs. However, a memory allocation error will occur if the calculation demands
more memory than available.

**Note: 

Unlike **Q-Chem**’s MP2 frequency code, the analytic CIS second derivative
code currently does not support frozen core or virtual orbitals. These
approximations do not lead to large savings at the CIS level, as all
computationally-expensive steps are performed in the atomic orbital basis.
**

???+ example "Example 7.2: This example illustrates a CIS geometry optimization followed by a vibrational
frequency analysis on the lowest singlet excited state of formaldehyde. This $n\rightarrow\pi^{\ast}$ excited state is non-planar, unlike the ground state. The
optimization converges to a non-planar structure with zero forces, and all
frequencies real."
    ```qchem
    $molecule
       0 1
       C
       O  1  CO
       H  1  CH  2  A
       H  1  CH  2  A  3  D
    
       CO  =    1.2
       CH  =    1.0
       A   =  120.0
       D   =  150.0
    $end
    
    $rem
       JOBTYPE          =  opt
       EXCHANGE         =  hf
       BASIS            =  6-31+G*
       CIS_STATE_DERIV  =  1         Optimize state 1
       CIS_N_ROOTS      =  3         Do 3 states
       CIS_SINGLETS     =  true      Do do singlets
       CIS_TRIPLETS     =  false     Don’t do Triplets
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE          =  freq
       EXCHANGE         =  hf
       BASIS            =  6-31+G*
       CIS_STATE_DERIV  =  1         Focus on state 1
       CIS_N_ROOTS      =  3         Do 3 states
       CIS_SINGLETS     =  true      Do do singlets
       CIS_TRIPLETS     =  false     Don’t do Triplets
    $end
    ```

???+ example "Example 7.3: Evaluation of gradients of several electronic states in a single calculation.
Gradients of the reference DFT and SF-TDDFT states are produced."
    ```qchem
    $molecule
    0 3
       C   0.000000     0.000000     0.106788
       H  -0.989216     0.000000    -0.320363
       H   0.989216     0.000000    -0.320363
    $end
    
    $rem
    job_type force
    method       B5050LYP
    SYM_IGNORE  True
    UNRESTRICTED TRUE
    BASIS       6-31G*
    SCF_CONVERGENCE 8
    spin_flip true
    CIS_N_ROOTS       4
    CIS_STATE_MULTIGRAD = 2
    $end
    
    ```

## 7.2.2.3 Random Phase Approximation

The Random Phase Approximation (RPA),[[148]](../bib_references/bib.md#bib139)
 also known
as time-dependent Hartree-Fock (TD-HF) theory, is an alternative to CIS for
uncorrelated calculations of excited states. An RPA calculation is requested using the RPA
*$rem* variable that is described in Section [7.2.4.1](sec_CIS-jobcontrol.md#sec:CIS-jobcontrol:Basic).

RPA offers some advantages for
computing oscillator strengths, *e.g.*, exact satisfaction of the
Thomas-Reike-Kuhn sum rule,

 and is roughly comparable in
accuracy to CIS for singlet excitation energies, but is inferior for triplet
states. RPA energies are non-variational, and in moving around on excited-state
potential energy surfaces, this method can occasionally encounter singularities
(arising from triplet instabilities in the underlying reference state)
that prevent numerical solution of the RPA equations.[[268]](../bib_references/bib.md#bib269)

In **Q-Chem**, these instabilities are generally accompanied by an error message to the effect
that an imaginary root has been detected in the RPA equations.
This is mathematically impossible in CIS calculations, which decouple the excitation energy problem
from the stability problem.

## 7.2.2.4 DFT/CIS

DFT/CIS[[490]](../bib_references/bib.md#bib498)
 is a semi-empirical method that uses Kohn-Sham orbitals instead of Hartree-Fock orbitals with a CIS-like formalism.
This leads to added correlation energy from the Kohn-Sham orbitals and, perhaps more importantly, orbital energy differences
$\varepsilon_{a}-\varepsilon_{i}$ that better resemble excitation energies, and bound virtual orbitals that better approximate localized excited states
as compared to Hartree-Fock virtual orbitals, which are typically unbound.[[572]](../bib_references/bib.md#bib586)

Along with certain semi-empirical corrections, DFT/CIS significantly improves conventional Hartree–Fock-based CIS.
Two parameterizations of the DFT/CIS Hamiltonian are available in **Q-Chem**: Grimme’s original one,[[490]](../bib_references/bib.md#bib498)
 which is designed
for use with the B3LYP functional, and a new parameterization designed for CAM-B3LYP.[[879]](../bib_references/bib.md#bib914)

The latter (CAM-B3LYP/CIS) implementation has specific parameterizations aimed at accurately reproducing x-ray spectra,
whereas B3LYP/CIS is suitable only for valence excitations.
The nature of the parameterization limits use of DFT/CIS to the aforementioned two functionals, and primarily to two basis sets.
The CAM-B3LYP/CIS method is parameterized for use with def2-TZVPD while B3LYP/CIS is parameterized for use with TZVP.

The DFT/CIS method is controlled by the DFTCIS and DFTCIS_PARAMS job control variables that are
described in Section [7.2.4.1](sec_CIS-jobcontrol.md#sec:CIS-jobcontrol:Basic).

???+ example "Example 7.4: A DFT/CIS (B3LYP/CIS) calculation of the first five singlet excited states of water."
    ```qchem
    $molecule
    0 1
    O
    H  1 0.960652
    H  1 0.960652 2 103.913458
    $end
    
    $rem
    JOBTYPE        = sp
    METHOD         = b3lyp
    UNRESTRICTED   = false
    BASIS          = TZVP
    DFTCIS         = true
    DFTCIS_PARAMS  = 1 !0=CIS, 1=B3LYP/CIS, 2=CAM-B3LYP/CIS
    CIS_N_ROOTS    = 5
    CIS_TRIPLETS   = false
    SCF_ALGORITHM  = diis
    $end
    
    ```

The core/valence separation (CVS) approximation is implemented for use with the DFT/CIS method, which can therefore
be used to compute core-level excitation spectra at elemental K-, L-, or M-edges.[[879]](../bib_references/bib.md#bib914)

L-edge spectra require spin-orbit couplings, which are discussed in Section [7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc).
Example [7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc) in that section illustrates a DFT/CIS of an L-edge spectrum, including spin-orbit couplings.
The **Q-Chem** output file from this example can be read by the **pySETSOC** program[[882]](../bib_references/bib.md#bib1655)
and used to construct and diagonalize the Breit-Pauli Hamiltonian, which affords the coupled excited states and oscillator strengths.[[881]](../bib_references/bib.md#bib916)
