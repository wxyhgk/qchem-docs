---
title: "4.2.1 SCF and LCAO Approximations"
---

## 4.2.1 SCF and LCAO Approximations

(July 4, 2026)

The fundamental equation of non-relativistic quantum chemistry is the
time-independent Schrödinger equation,

<a id="eq400"></a>
$$
\hat{H}({\rm{\bf R}},{\rm{\bf r}})\;\Psi({\rm{\bf R}},{\rm{\bf r}})=E({\rm{\bf
R}})\;\Psi({\rm{\bf R}},{\rm{\bf r}}). \tag{4.1}
$$

In quantum chemistry, this equation is solved as a function of the electronic
variables ($\mathbf{r}$), for fixed values of the nuclear coordinates ($\mathbf{R}$).
The Hamiltonian operator in Eq. ([4.1](#eq400)) is

<a id="eq:Hamiltonian"></a>
$$
\hat{H}=-\frac{1}{2}\sum_{i=1}^{N}\hat{\nabla}_{i}^{2}-\frac{1}{2}\sum_{A=1}^{M}\frac{1}{M_{A}}\hat{\nabla}_{A}^{2}-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_{A}}{r_{iA}}+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}}+\sum_{A=1}^{M}\sum_{B>A}^{M}\frac{Z_{A}Z_{B}}{R_{AB}} \tag{4.2}
$$

in atomic units, where

<a id="eq402"></a>
$$
\hat{\nabla}^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\;. \tag{4.3}
$$

In Eq. ([4.2](#eq:Hamiltonian)), $Z$ is the nuclear charge, $M_{A}$ is the ratio
of the mass of nucleus $A$ to the mass of an electron, $R_{AB}=|\mathbf{R}_{A}-\mathbf{R}_{B}|$ is the distance between nuclei $A$ and $B$, $r_{ij}=|\mathbf{r}_{i}-\mathbf{r}_{j}|$ is the distance between the $i$th and $j$th electrons, $r_{iA}=|\mathbf{r}_{i}-\mathbf{R}_{A}|$ is the distance between the $i$th electron and the $A$th
nucleus, $M$ is the number of nuclei and $N$ is the number of electrons. The
total energy $E$ is an eigenvalue of $\hat{H}$, with a corresponding
eigenfunction (wave function), $\Psi$.

Separating the motions of the electrons from that of the nuclei, an idea
originally due to Born and Oppenheimer,[[147]](../bib_references/bib.md#bib138)
 yields the electronic Hamiltonian operator

<a id="eq403"></a>
$$
\hat{H}_{\mathrm{elec}}=-\frac{1}{2}\sum_{i=1}^{N}\hat{\nabla}_{i}^{2}-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_{A}}{r_{iA}}+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}} \tag{4.4}
$$

The solution of the corresponding electronic Schrödinger equation,

<a id="eq404"></a>
$$
\hat{H}_{\mathrm{elec}}\Psi_{\mathrm{elec}}=E_{\mathrm{elec}}\Psi_{\mathrm{elec}}\;, \tag{4.5}
$$

affords the total electronic energy, $E_{\mathrm{elec}}$, and electronic wave
function, $\Psi_{\mathrm{elec}}$, which describes the distribution of the electrons for
fixed nuclear positions. The total energy is obtained by simply adding the
nuclear–nuclear repulsion energy [the fifth term in Eq. ([4.2](#eq:Hamiltonian))] to the
total electronic energy:

<a id="eq405"></a>
$$
E_{\mathrm{tot}}=E_{\mathrm{elec}}+E_{\mathrm{nuc}}\;. \tag{4.6}
$$

Solving the eigenvalue problem in Eq. ([4.5](#eq404)) yields a set of
eigenfunctions ($\Psi_{0}$, $\Psi_{1}$, $\Psi_{2}\ldots$) with corresponding
eigenvalues $E_{0}\leq E_{1}\leq E_{2}\leq\ldots$.

Our interest lies in determining the lowest eigenvalue and associated
eigenfunction which correspond to the ground state energy and wave function of
the molecule. However, solving Eq. ([4.5](#eq404)) for other than the most
trivial systems is extremely difficult and the best we can do in practice is to
find approximate solutions.

The first approximation used to solve Eq. ([4.5](#eq404)) is the
independent-electron (mean-field) approximation, in which the wave function is
approximated as an antisymmetrized product of one-electron functions, namely,
the MOs. Each MO is determined by considering the electron as moving within an
average field of all the other electrons. This affords the well-known Slater
determinant wave function[[1266]](../bib_references/bib.md#bib1315)

<a id="eq406"></a>
$$
\Psi=\frac{1}{\sqrt{n!}}\left|{{\begin{array}[]{cccc}\chi_{1}(1)&\chi_{2}(1)&\cdots&\chi_{n}(1)\\
\chi_{1}(2)&\chi_{2}(2)&\cdots&\chi_{n}(2)\\
\vdots&\vdots&\hfil&\vdots\\
\chi_{1}(n)&\chi_{2}(n)&\cdots&\chi_{n}(n)\\
\end{array}}}\right| \tag{4.7}
$$

where $\chi_{i}$, a spin orbital, is the product of a molecular orbital $\psi_{i}$
and a spin function ($\alpha$ or $\beta$).

One obtains the optimum set of MOs by variationally minimizing the energy in
what is called a “self-consistent field” or SCF approximation to the
many-electron problem. The archetypal SCF method is the Hartree-Fock (HF)
approximation, but these SCF methods also include KS-DFT
(Chapter [5](../ch05_dft/chap_DFT.md)). All SCF methods lead to equations of the form

<a id="eq407"></a>
$$
\hat{f}(i)\,\chi(\mathbf{x}_{i})=\varepsilon\,\chi(\mathbf{x}_{i})\;, \tag{4.8}
$$

where the Fock operator $\hat{f}(i)$ for the $i$th electron is

<a id="eq408"></a>
$$
\hat{f}(i)=-\frac{1}{2}\hat{\nabla}_{i}^{2}+\upsilon_{\rm eff}(i)\;. \tag{4.9}
$$

Here $\mathbf{x}_{i}$ are spin and spatial coordinates of the $i$th electron, the
functions $\chi$ are spin orbitals and $\upsilon_{\rm eff}$ is the effective
potential “seen” by the $i$th electron, which depends on the spin orbitals of
the other electrons. The nature of the effective potential $\upsilon_{\rm eff}$
depends on the SCF methodology, *i.e.*, on the choice of density-functional
approximation.

The second approximation usually introduced when solving Eq. ([4.5](#eq404)) is
the introduction of an AO basis $\{\phi_{\mu}\}$ linear combinations of which
will then determine the MOs. There are many standardized, atom-centered
Gaussian basis sets and details of these are discussed in
Chapter [8](../ch08_basis/chap_basis.md).

After eliminating the spin components in Eq. ([4.8](#eq407)) and introducing a
finite basis,

<a id="eq409"></a>
$$
\psi_{i}=\sum_{\mu}{c_{\mu i}\phi_{\mu}}\;, \tag{4.10}
$$

Eq. ([4.8](#eq407)) reduces to the Roothaan-Hall matrix equation

<a id="eq:Roothaan-Hall"></a>
$$
\mathbf{FC}=\bm{\varepsilon}\mathbf{SC}\;. \tag{4.11}
$$

Here, $\mathbf{F}$ is the Fock matrix, $\mathbf{C}$ is a square matrix of molecular
orbital coefficients, $\mathbf{S}$ is the AO overlap matrix with elements

<a id="eq411"></a>
$$
S_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})}\phi_{\nu}({\rm{\bf r}})d{\rm{\bf r}} \tag{4.12}
$$

and $\bm{\varepsilon}$ is a diagonal matrix containing the orbital energies.
Generalizing to an unrestricted formalism by introducing separate spatial
orbitals for $\alpha$ and $\beta$ spin in Eq. ([4.7](#eq406)) yields the
Pople-Nesbet equations[[1116]](../bib_references/bib.md#bib1159)

<a id="A3.S8.EGx1"></a>
$$
\displaystyle\mathbf{F}^{\alpha}\mathbf{C}^{\alpha} \tag{4.13}
$$

In SCF methods, an initial guess is for the MOs is first determined, and from
this, an average field seen by each electron can be calculated. A new set of
MOs can be obtained by solving the Roothaan-Hall or Pople-Nesbet eigenvalue
equations, resulting in the restricted or unrestricted finite-basis SCF
approximation. This procedure is repeated until the new MOs differ negligibly
from those of the previous iteration. The Hartree-Fock approximation for the
effective potential in Eq. ([4.9](#eq408)) inherently neglects the instantaneous
electron-electron correlations that are averaged out by the SCF procedure, and
while the chemistry resulting from HF calculations often offers valuable
qualitative insight, quantitative energetics are often poor. In principle, the
DFT methodologies are able to capture all the correlation energy, *i.e.*, the
difference in energy between the HF energy and the true energy. In practice,
the best-available density functionals perform well but not perfectly, and
conventional post-HF approaches to calculating the correlation energy (see
Chapter [6](../ch06_correlation/chap_correlation.md)) are often required.

That said, because SCF methods often yield acceptably accurate chemical
predictions at low- to moderate computational cost, self-consistent field
methods are the cornerstone of most quantum-chemical programs and calculations.
The formal costs of many SCF algorithms is ${\cal{O}}({N^{4}})$, that is, they grow with
the fourth power of system size, $N$. This is slower than the growth of the
cheapest conventional correlated methods, which scale as ${\cal{O}}({N^{5}})$ or worse,
algorithmic advances available in **Q-Chem** can reduce the SCF cost to ${\cal{O}}({N})$
in favorable cases, an improvement that allows SCF methods to be applied to
molecules previously considered beyond the scope of *ab initio* quantum
chemistry.

Types of ground-state energy calculations currently available in **Q-Chem**
are summarized in Table [4.1](#tab:calculations).

| Calculation | $rem Variable JOBTYPE |  |
| --- | --- | --- |
| Single point energy (default) | SINGLE_POINT or SP |  |
| Force (energy + gradient) | FORCE |  |
| Equilibrium structure search | OPTIMIZATION or OPT | (Ch. 9 ) |
| Transition structure search | TS | (Ch. 9 ) |
| Intrinsic reaction pathway | RPATH | (Section 9.7 ) |
| Potential energy scan | PES_SCAN | (Section 9.6 ) |
| Vibrational frequency calculation | FREQUENCY or FREQ | (Section 10.8 ) |
| Polarizability and relaxed dipole | POLARIZABILITY , DIPOLE | (Section 10.13.2 ) |
| NMR chemical shift | NMR | (Section 10.11.2 ) |
| Indirect nuclear spin-spin coupling | ISSC | (Section 10.11.2 ) |
| Ab initio molecular dynamics | AIMD | (Section 9.9 ) |
| Ab initio path integrals | PIMD , PIMC | (Section 9.10 ) |
| BSSE (counterpoise) correction | BSSE | (Section 12.4 ) |
| Energy decomposition analysis | EDA | (Sections 12.5.3 and 12.6 ) |
| Symmetry-adapted perturbation theory | XSAPT | (Sections 12.9 and 12.10 ) |

Table 4.1: 
The type of calculation to be run by **Q-Chem** is controlled by the *$rem* variable JOBTYPE.
