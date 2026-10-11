---
title: "9.8.1 Nonadiabatic Couplings"
---

## 9.8.1 Nonadiabatic Couplings

(July 4, 2026)

Conical intersections are degeneracies between Born-Oppenheimer potential
energy surfaces that facilitate nonadiabatic transitions between excited
states, *i.e.*, internal conversion and intersystem crossing processes, both of
which represent a breakdown of the Born-Oppenheimer
approximation.[[916]](../bib_references/bib.md#bib952)

Although simultaneous intersections between more than two electronic states are
possible,[[916]](../bib_references/bib.md#bib952)
 consider for convenience the two-state case, and let

<a id="eq:H_2x2"></a>

$$
\mathbf{H}=\left(\begin{array}[]{cc}H_{JJ}(\mathbf{R})&H_{JK}(\mathbf{R})\\
H_{JK}^{\ast}(\mathbf{R})&H_{KK}(\mathbf{R})\\
\end{array}\right)\;. \tag{9.48}
$$

denote the matrix representation of the vibronic (vibrational + electronic)
Hamiltonian [Eq. ([4.2](../ch04_scf/Ch4.S2.SS1.md#eq:Hamiltonian))] in a basis of two electronic states,
$J$ and $K$. (Electronic degrees of freedom have been integrated out of this
expression, and $\mathbf{R}$ represents the remaining, nuclear coordinates.)
By definition, the Born-Oppenheimer states are the ones that diagonalize
$\mathbf{H}$ at a particular molecular geometry $\mathbf{R}$, and thus two
conditions must be satisfied in order to obtain degeneracy in the
Born-Oppenheimer representation: $H_{JJ}=H_{KK}$ and $H_{JK}=0$. As
such, degeneracies between two Born-Oppenheimer potential energy surfaces exist
in subspaces of dimension $N_{\rm int}-2$, where $N_{\rm int}=3N_{\rm atoms}-6$ is the number of internal (vibrational) degrees of freedom (assuming
the molecule is non-linear). This ($N_{\rm int}-2$)-dimensional subspace is
known as the *seam space* because the two states are degenerate everywhere
within this space. In the remaining two degrees of freedom, known as the
*branching space*, the degeneracy between Born-Oppenheimer surfaces is
lifted by an infinitesimal displacement, which in a three-dimensional plot
resembles a double cone about the point of intersection, hence the name *conical intersection*.

The branching space is defined by the span of a pair of vectors
$\mathbf{g}_{JK}$ and $\mathbf{h}_{JK}$. The former is simply the
difference in the gradient vectors of the two states in question,

<a id="eq:gJK"></a>

$$
\mathbf{g}_{JK}=\frac{\partial E_{J}}{\partial\textbf{R}}-\frac{\partial E_{K}}{\partial\textbf{R}}\;, \tag{9.49}
$$

and is readily evaluated at any level of theory for which analytic energy
gradients are available (or less-readily, via finite difference, if they are
not!). The definition of the *nonadiabatic coupling vector*
$\mathbf{h}_{JK}$, on the other hand, is more involved and not directly
amenable to finite-difference calculations:

<a id="eq:hJK"></a>

$$
\mathbf{h}_{JK}=\left\langle\Psi_{J}\left|\left(\partial\hat{H}/\partial\mathbf{R}\right)\right|\Psi_{K}\right\rangle\;. \tag{9.50}
$$

This is closely related to the *derivative coupling* vector

<a id="eq:dJK"></a>

$$
\mathbf{d}_{JK}=\bigl{\langle}\Psi_{J}\bigl{|}\bigl{(}\partial/\partial\mathbf{R}\bigr{)}\bigr{|}\Psi_{K}\bigr{\rangle}=\frac{\mathbf{h}_{JK}}{E_{J}-E_{K}}\;. \tag{9.51}
$$

The latter expression for $\mathbf{d}_{JK}$ demonstrates that the coupling
between states becomes large in regions of the potential surface where the two
states are nearly degenerate. The relative orientation and magnitudes of the
vectors $\mathbf{g}_{JK}$ and $\mathbf{h}_{JK}$ determined the topography
around the intersection, *i.e.*, whether the intersection is “peaked” or “sloped”;[[54]](../bib_references/bib.md#bib37)

see Ref. [[565]](../bib_references/bib.md#bib577)
 for a pedagogical overview.

Algorithms to compute the nonadiabatic couplings $\mathbf{d}_{JK}$ are not
widely available in quantum chemistry codes, but thanks to the efforts of the
Herbert and Subotnik groups, they are available in **Q-Chem** when the wave
functions $\Psi_{J}$ and $\Psi_{K}$, and corresponding electronic energies $E_{J}$
and $E_{K}$, are computed at the CIS or TDDFT
level,[[378]](../bib_references/bib.md#bib383)
 or at the
corresponding spin-flip (SF) levels of theory (SF-CIS or SF-TDDFT). The
spin-flip implementation is particularly significant.[[1547]](../bib_references/bib.md#bib1613)

Only that approach—and not traditional spin-conserving CIS or
TDDFT—affords correct topology around conical intersections that involve the
ground state.

To understand why, suppose that $J$ in Eq. ([9.48](#eq:H_2x2))
represents the ground state; call it $J=0$ for definiteness. In linear
response theory (TDDFT) or in CIS (by virtue of Brillouin’s theorem), the
coupling matrix elements between the reference (ground) state and all of the
excited states vanish identically, hence $H_{0K}(\mathbf{R})\equiv 0$. This
means that there is only one condition to satisfy in order to obtain
degeneracy, hence the branching space is one- rather than two-dimensional, for
any conical intersection that involves the ground state.[[806]](../bib_references/bib.md#bib839)

(For intersections between two excited states, the topology should be correct.)
In the spin-flip approach, however, the reference state has a different spin
multiplicity than the target states; if the latter have spin quantum number
$S$, then the reference state has spin $S+1$. This has the effect that the
ground state of interest (spin $S$) is treated as an excitation, and thus on a
more equal footing with excited states of the same spin, and it rigorously
fixes the topology problem around conical intersections.[[1547]](../bib_references/bib.md#bib1613)

This can have consequences for simulation of internal conversion to the ground state,
where for example S${}_{1}$ lifetimes may be significantly affected by warping of the potential energy
surfaces around the S${}_{1}$/S${}_{0}$ intersection in conventional TDDFT.[[1550]](../bib_references/bib.md#bib1617)

Nonadiabatic (derivative) couplings are available for both CIS and TDDFT. The
CIS nonadiabatic couplings can be obtained from direct differentiation of the
wave functions with respect to nuclear positions.[[378]](../bib_references/bib.md#bib383)

For TDDFT, the same procedure can be
carried out to calculate the approximate nonadiabatic couplings, in what has
been termed the “pseudo-wave function” approach.[[1030]](../bib_references/bib.md#bib1071)

Formally more rigorous TDDFT nonadiabatic couplings derived from quadratic
response theory are also available, although they are subject to certain
undesirable, accidental singularities if for the two states $J$ and $K$ in
Eq. ([9.50](#eq:hJK)), the energy difference $|E_{J}-E_{K}|$ is quasi-degenerate
with the excitation energy $\omega_{I}=E_{I}-E_{0}$ for some third state,
$I$.[[1548]](../bib_references/bib.md#bib1614)
 As such, the pseudo-wave function method is
the recommended approach for computing nonadiabatic couplings with TDDFT,
although in the spin flip case the pseudo-wave function approach is rigorously
equivalent to the pseudo-wave function approach, and is free of singularities.[[1548]](../bib_references/bib.md#bib1614)

Finally, we note that there is mounting evidence that SF-TDDFT calculations are
most accurate when used with functionals containing $\sim$50% Hartree-Fock
exchange,[[1239]](../bib_references/bib.md#bib1294)

and many studies with this method have used the BH&HLYP functional; see
Refs. [[565]](../bib_references/bib.md#bib577)
 and 

 for reviews. The BH&H-LYP functional
combines LYP correlation is combined with Becke’s “half and half” exchange functional.[[484]](../bib_references/bib.md#bib496)

In **Q-Chem**, it is selected by setting METHOD = BHHLYP.
