---
title: "11.5.2 Theoretical Background"
---

## 11.5.2 Theoretical Background

(July 4, 2026)

The total energy of the system consists of the interaction energy of the
effective fragments ($E^{\text{ef-ef}}$) and the energy of the *ab initio*
(*i.e.*, QM) region in the field of the fragments. The former includes
electrostatics, polarization, dispersion and exchange-repulsion contributions
(the charge transfer term, which might be important for description of the
ionic and highly polar species, is omitted in the current implementation):

<a id="Ch11.E61"></a>

$$
E^{\text{ef-ef}}=E_{\text{elec}}+E_{\text{pol}}+E_{\text{disp}}+E_{\text{ex-rep}}\;. \tag{11.61}
$$

The QM-EF interactions are computed as follows. The electrostatics (Coulomb) and
polarization parts of the EFP potential contribute to the quantum Hamiltonian
via one-electron terms,

<a id="eq:H-EFP"></a>

$$
H^{\prime}_{pq}=H_{pq}+\langle p|\hat{V}^{\text{Coul}}+\hat{V}^{\text{pol}}|q\rangle \tag{11.62}
$$

whereas dispersion and exchange-repulsion QM-EF interactions are treated as
additive corrections to the total energy.

The electrostatic component of the EFP energy accounts for Coulomb
interactions. In molecular systems with hydrogen bonds or polar molecules, this
is the leading contribution to the total intermolecular interaction
energy.[[169]](../bib_references/bib.md#bib163)
 An accurate representation of the electrostatic
potential is achieved by using multipole expansion (obtained from the Stone’s
distributed multipole analysis) around atomic centers and bond midpoints
(*i.e.*, the points with high electronic density) and truncating this expansion
at octupoles.[[1316]](../bib_references/bib.md#bib1372)
 The
fragment-fragment electrostatic interactions consist of charge–charge,
charge–dipole, charge–quadrupole, charge–octupole, dipole–dipole,
dipole–quadrupole, and quadrupole–quadrupole terms, as well as terms describing
interactions of electronic multipoles with the nuclei and nuclear repulsion energy.

The multipole representation of the electrostatic density of a fragment breaks
down when the fragments are too close. The multipole interactions become too
repulsive due to significant overlap of the electronic densities and the
charge-penetration effect. The magnitude of the charge-penetration effect is
usually around 15% of the total electrostatic energy in polar systems,
however, it can be as large as 200% in systems with weak electrostatic
interactions.[[1270]](../bib_references/bib.md#bib1323)
 To account for the charge-penetration
effect, the simple exponential damping of the charge-charge term is
used.[[406]](../bib_references/bib.md#bib415)
 The charge-charge screened energy
between the expansion points $k$ and $l$ is given by the following expression,
where $\alpha_{k}$ and $\alpha_{l}$ are the damping parameters associated with the
corresponding expansion points:

<a id="eq:EFP-elec-damp"></a>

$$
E^{\text{ch-ch}}_{kl}=\begin{cases}\left[1-(1+\alpha_{k}R_{kl}/2)e^{-\alpha_{k}R_{kl}}\right]\frac{q^{k}q^{l}}{R_{kl}}&\text{if $\alpha_{k}=\alpha_{l}$}\\
\left[1-\left({\alpha_{l}^{2}\over\alpha_{l}^{2}-\alpha_{k}^{2}}\right)e^{-\alpha_{k}R_{kl}}-\left({\alpha_{k}^{2}\over\alpha_{k}^{2}-\alpha_{l}^{2}}\right)e^{-\alpha_{l}R_{kl}}\right]\frac{q^{k}q^{l}}{R_{kl}}&\text{if $\alpha_{k}\neq\alpha_{l}$}\\
\end{cases}\;. \tag{11.63}
$$

Alternatively, one can obtain the short-range charge-penetration energy using
the spherical Gaussian overlap (SGO) approximation:[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:overlap-damping"></a>

$$
E^{\text{pen}}_{kl}=-2\left({1\over{-2ln|S_{kl}|}}\right)^{1/2}\frac{S^{2}_{kl}}{R_{kl}} \tag{11.64}
$$

where $S_{kl}$ is the overlap integral between localized MOs $k$ and $l$,
calculated for the exchange-repulsion term, Eq. ([11.76](#eq:ex_rep)). This
charge-penetration energy is calculated and printed separately from the rest of
the electrostatic energy. Using overlap-based damping generally results in a
more balanced description of intermolecular interactions and is recommended,
except possibly where short-range repulsive interactions are of interest.[[198]](../bib_references/bib.md#bib195)

Electrostatic interaction between an effective fragment and the QM part is
described by perturbation $\hat{V}^{\text{Coul}}$ of the *ab initio* Hamiltonian
[see Eq.  ([11.62](#eq:H-EFP))]. The perturbation enters the one-electron part of
the Hamiltonian as a sum of contributions from the expansion points of the
effective fragments. Contribution from each expansion point consists of four
terms originating from the electrostatic potential of the corresponding
multipole (charge, dipole, quadrupole, and octupole):

<a id="eq:QM-EFP-elec"></a>

$$
V^{\text{Coul}}_{k}(x)=q_{k}T(r_{kx})-\sum^{x,y,z}_{a}\mu^{k}_{a}T_{a}(r_{kx})+\frac{1}{3}\sum^{x,y,z}_{ab}\Theta^{k}_{ab}T_{ab}(r_{kx})-\frac{1}{15}\sum^{x,y,z}_{abc}\Omega^{k}_{abc}T_{abc}(r_{kx})\;, \tag{11.65}
$$

where $q$, $\mu$, $\Theta$ and $\Omega$ are the net charge, dipole, quadrupole
and octupole, respectively, located at multipole expansion points $k$ (all atoms and bond midpoints).
$T$ are the electrostatic tensors of ranks zero to three.
Interaction of the QM electronic density with multipole charges can be also augmented by
gaussian-type damping function,[[504]](../bib_references/bib.md#bib517)
 such
that Eq. ([11.65](#eq:QM-EFP-elec)) becomes

<a id="A3.S8.EGx106"></a>

$$
\displaystyle\begin{aligned} \displaystyle V^{\text{Coul}}_{k}(x)=\big{[}q_{k}^{\text{nuc}}+q_{k}^{\text{ele}}(1-\exp{(-\beta_{k}r^{2}_{kx})}\big{]}T(r_{kx})&\displaystyle-\sum^{x,y,z}_{a}\mu^{k}_{a}\;T_{a}(r_{kx})+\frac{1}{3}\sum^{x,y,z}_{ab}\Theta^{k}_{ab}\;T_{ab}(r_{kx})\\
&\displaystyle-\frac{1}{15}\sum^{x,y,z}_{abc}\Omega^{k}_{abc}\;T_{abc}(r_{kx})\;,\end{aligned} \tag{11.66}
$$

where $q_{k}^{\text{nuc}}$ is the nuclear charge and $q_{k}^{\text{ele}}$ is the electronic charge
on multipole point $k$, respectively. Thus, only the electronic charges are damped (smeared) by gaussians.
Damping parameters $\alpha$ and $\beta$ in Eqs. ([11.63](#eq:EFP-elec-damp))
and ([11.66](#eq:QM-EFP-elec-damp)) are determined by minimizing the difference
between the electrostatic potentials from the damped multipole expansion and
the electronic wave function in the parameter-generating calculation for each fragment.
(See Section [11.5.9](sec_makefp.md).)

Polarization accounts for the intramolecular charge redistribution in response
to external electric field. It is the major component of many-body interactions
responsible for cooperative molecular behavior. EFP employs distributed
polarizabilities placed at the centers of valence LMOs. Unlike the isotropic
total molecular polarizability tensor, the distributed polarizability tensors are anisotropic.

The polarization energy of a system consisting of an *ab initio* and
effective fragment regions is[[309]](../bib_references/bib.md#bib314)

<a id="eq:pol_energy"></a>

$$
E^{\text{pol}}=-\frac{1}{2}\sum_{k}\sum^{x,y,z}_{a}\mu^{k}_{a}\big{(}F^{\text{mult},k}_{a}+F^{\text{ai,nuc},k}_{a}\big{)}+\frac{1}{2}\sum_{k}\sum^{x,y,z}_{a}\bar{\mu}^{k}_{a}\;F^{\text{ai,elec},k}_{a} \tag{11.67}
$$

where $\mu^{k}$ and $\bar{\mu}^{k}$ are the induced dipole and the conjugated
induced dipole at the distributed point $k$; $F^{\text{mult},k}$ is the
external field due to static multipoles and nuclei of other fragments, and
$F^{\text{ai,elec},k}$ and $F^{\text{ai,nuc},k}$ are the fields due to the
electronic density and nuclei of the *ab initio* part, respectively.

The induced dipoles at each polarizability point $k$ are computed as

<a id="eq:ind_dip"></a>

$$
\mu^{k}=\alpha^{k}F^{\text{total},k} \tag{11.68}
$$

where $\alpha^{k}$ is the distributed polarizability tensor at $k$.
The total field $F^{\text{total},k}$ comprises from the static field and the
field due to other induced dipoles, $F^{\text{ind}}_{k}$, as well as the field due
to nuclei and electronic density of the *ab initio* region:

<a id="eq:pol_total_field"></a>

$$
F^{\text{ai,total},k}=F^{\text{mult},k}+F^{\text{ind},k}+F^{\text{ai,elec},k}+F^{\text{ai,nuc},k}\;. \tag{11.69}
$$

As follows from the above equation, the induced dipoles on a particular
fragment depend on the values of the induced dipoles of all other fragments.
Moreover, the induced dipoles on the effective fragments depend on the
*ab initio* electronic density, which, in turn, is affected by the field
created by these induced dipoles through a one electron contribution to the Hamiltonian:

<a id="eq:hamilt_pol"></a>

$$
\hat{V}^{\text{pol}}_{k}(x)=\frac{1}{2}\sum_{a}^{x,y,z}\big{(}\mu_{a}^{k}+\bar{\mu}_{a}^{k}\big{)}\;T_{a}(r_{kx}) \tag{11.70}
$$

where $k$ are the polarizability expansion points. The total polarization
contribution is computed self-consistently using a two level iterative procedure. The
objectives of the higher and lower levels are to converge the wave function and
induced dipoles for a given fixed wave function, respectively. In the absence of
the *ab initio* region, the induced dipoles of the EF system are iterated
until self-consistency with each other.

Self-consistent treatment of polarization accounts for many-body interaction
effects. Polarization energy between EFP fragments is augmented by
gaussian-like damping functions with default parameter $\alpha=\beta=0.6$,
applied to electric field $F$:[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:pol_damp_1"></a>

$$
F=F_{0}f^{\mathrm{damp}} \tag{11.71}
$$

<a id="eq:pol_damp_2"></a>

$$
f^{\text{damp}}=1.0-\big{(}1+\sqrt{\alpha\beta}r^{2}\big{)}e^{-(\alpha\beta)^{1/2}r^{2}} \tag{11.72}
$$

Dispersion provides a leading contribution to van der Waals and $\pi$-stacking
interactions,[[197]](../bib_references/bib.md#bib190)
 and its leading-order contribution is

<a id="eq:disp_basic"></a>

$$
E^{\text{disp}}=\sum_{n}\frac{C_{6}}{R^{6}} \tag{11.73}
$$

where coefficients $C_{6}$ are derived from the frequency-dependent distributed
polarizabilities with expansion points located at the LMO centroids, *i.e.*, at
the same centers as the polarization expansion points. The higher-order
dispersion terms (induced dipole-induced quadrupole, induced quadrupole/induced quadrupole, *etc.*) are approximated as $1/3$ of the $C_{6}$ term.[[21]](../bib_references/bib.md#bib5)

For small distances between effective fragments, dispersion interactions are
corrected for charge penetration and electronic density overlap effect either with the
Tang-Toennies damping formula[[1342]](../bib_references/bib.md#bib1400)
 with parameter $b=1.5$,

<a id="eq:disp_TT_damp"></a>

$$
C_{6}^{kl}\rightarrow\left(1-e^{-bR}\sum_{k=0}^{6}{{(bR)^{k}}\over{k!}}\right)C_{6}^{kl}\;, \tag{11.74}
$$

or else using interfragment overlap (so-called overlap-based damping):[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:disp_overlap_damp"></a>

$$
C_{6}^{kl}\rightarrow\left(1-S_{kl}^{2}\left(1-2\log|S_{kl}|+2\log^{2}|S_{kl}|\right)\right)C_{6}^{kl}\;. \tag{11.75}
$$

**Note: 

QM/EFP dispersion interactions are currently disabled.
**

Exchange-repulsion originates from the Pauli exclusion principle, which states
that the wave function of two identical fermions must be anti-symmetric. In
traditional classical force fields, exchange-repulsion is introduced as a
positive (repulsive) term, *e.g.*, $R^{-12}$ in the Lennard-Jones potential. In
contrast, EFP uses a wave function-based formalism to account for this
inherently quantum-mechanical effect.

The exchange-repulsion interaction is derived as an expansion in the
intermolecular overlap, truncated at the quadratic
term,[[638]](../bib_references/bib.md#bib658)
 which requires that each effective fragment
carries a basis set that is used to calculate overlap and kinetic one-electron
integrals for each interacting pair of fragments. The
exchange-repulsion contribution from each pair of localized orbitals $i$ and
$j$ belonging to fragments $A$ and $B$, respectively, is:

<a id="A3.S8.EGx107"></a>

$$
\displaystyle\begin{aligned} \displaystyle E^{\text{exch}}_{ij}=&\displaystyle-4\sqrt{-2\ln|S_{ij}|\over\pi}{S^{2}_{ij}\over R_{ij}}\\
&\displaystyle-2S_{ij}\left(\sum_{k\in A}F^{A}_{ik}S_{kj}+\sum_{l\in B}F^{B}_{jl}S_{il}-2T_{ij}\right)\\
&\displaystyle+2S^{2}_{ij}\left(\sum_{J\in B}{-Z_{J}R^{-1}_{iJ}}+2\sum_{l\in B}{R^{-1}_{il}}+\sum_{I\in A}{-Z_{I}R^{-1}_{Ij}}+2\sum_{k\in A}{R^{-1}_{kj}}-R^{-1}_{ij}\right)\end{aligned} \tag{11.76}
$$

where $i$, $j$, $k$ and $l$ are the LMOs, $I$ and $J$ are the nuclei, $S$ and
$T$ are the intermolecular overlap and kinetic energy integrals, and $F$ is the Fock matrix element.

The expression for the $E^{\text{exch}}_{ij}$ involves overlap and kinetic energy
integrals between pairs of localized orbitals. In addition, since
Eq. ([11.76](#eq:ex_rep)) is derived within an infinite basis set approximation, it
requires a reasonably large basis set to be accurate.
[The 6-311++G(3df,2p) basis set is recommended and 6-31+G* is considered to be the smallest
acceptable basis set.] These
factors make exchange-repulsion the most computationally expensive part of an EFP energy
calculation for systems of moderate size.

Large systems require additional considerations. Since total exchange-repulsion
energy is given by a sum of terms in Eq. ([11.76](#eq:ex_rep)) over all the
fragment pairs, its computational cost formally scales as ${\cal{O}}({N^{2}})$ with
the number of effective fragments $N$. However, exchange-repulsion is a
short-range interaction; the overlap and kinetic energy integrals decay
exponentially with the inter-fragment distance. Therefore, by employing a
distance-based screening, the number of overlap and kinetic energy integrals
scales as ${\cal{O}}({N})$. Consequently, for large systems exchange-repulsion may
become less computationally expensive than the long-range components of EFP
(such as Coulomb interactions).

**Note: 

The QM/EFP exchange-repulsion energy is currently disabled.
**
