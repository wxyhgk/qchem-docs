---
title: "9.1.6 Constrained Optimization in Delocalized Internal Coordinates"
---

## 9.1.6 Constrained Optimization in Delocalized Internal Coordinates

(July 4, 2026)

Imposing constraints in delocalized internal coordinates is far simpler
than in Cartesian, so we will give no further details on the latter.

At first glance, imposing any constraints in delocalized coordinates appears
problematic, given that each coordinate is potentially a linear combination of
all possible primitives. However, this is deceptive, and in fact all standard
constraints can be imposed by a relatively simple Schmidt orthogonalization
procedure. Consider a unit vector with only one non-zero component
corresponding to the primitive internal (stretch, bend or torsion) that one
wishes to keep constant. This vector is projected on to the full set, $\mathbf{U}$,
of active delocalized coordinates and normalized. All $n$ delocalized
coordinates are then Schmidt orthogonalized with respect to this normalized,
projected constraint vector. The last coordinate orthogonalized in this way
will be linearly dependent on the constraint vector and previous $n-1$ active
vectors, and can be removed from the active space.

In more detail, the procedure is as follows (taken directly from
Ref. [[63]](../bib_references/bib.md#bib50)
). The initial (usually unit) constraint vector $\mathbf{C}$ is
projected on to the set $\mathbf{U}$ of delocalized internal coordinates according to

<a id="Ch9.E27"></a>
$$
\mathbf{C}^{\text{proj}}=\sum_{k=1}^{n}\bigl{\langle}\mathbf{C}\bigl{|}\mathbf{CU}_{k}\mathbf{U}_{k}\bigr{\rangle}\mathbf{U}_{k}\;, \tag{9.27}
$$

where the summation is over all active coordinates $\mathbf{U}_{k}$. The
projected vector $\mathbf{C}^{\rm proj}$ is then normalized and an $n+l$
dimensional vector space $\mathbf{V}$ is formed, comprising the normalized,
projected constraint vector together with all active delocalized coordinates

<a id="Ch9.E28"></a>
$$
\mathbf{V}=\left\{\mathbf{C}^{\rm proj},~{}\mathbf{U}_{k}(k=1,\ldots,n)\right\}\;. \tag{9.28}
$$

This set of vectors is Schmidt orthogonalized according to the standard procedure,

<a id="eq:a21"></a>
$$
\widetilde{\mathbf{V}}_{k}=\alpha_{k}\left(\mathbf{V}_{k}-\sum_{\ell=1}^{k-1}\bigl{\langle}\mathbf{V}_{k}\bigl{|}\mathbf{V}_{k}\widetilde{\mathbf{V}}_{\ell}\widetilde{\mathbf{V}}_{\ell}\bigr{\rangle}\widetilde{\mathbf{V}}_{\ell}\right)\;, \tag{9.29}
$$

where the first vector is $\mathbf{V}_{1}$, is taken to be $\mathbf{C}^{\rm proj}$.
The coefficient $\alpha_{k}$ is a normalization factor. As noted above, the last vector
taken, $\mathbf{V}_{n+1}\equiv\mathbf{U}_{k}$, will drop out, leaving a fully orthonormal set
of $n-1$ active vectors and one constraint vector.

After the Schmidt orthogonalization the constraint vector will contain all the
weight in the active space of the primitive to be fixed, which will have a zero
component in all of the other $n-1$ vectors. The fixed primitive has thus
been isolated entirely in the constraint vector which can now be removed from
the active subspace for the geometry optimization step.

Extension of the above procedure to multiple constraints is straightforward.
In addition to constraints on individual primitives, it is also possible to
impose combinatorial constraints. For example, if, instead of a unit vector,
one started the constraint procedure with a vector in which two components were
set to unity, then this would impose a constraint in which the sum of the two
relevant primitives were always constant. In theory any desired linear
combination of any primitives could be constrained.

Note further that imposed constraints are not confined to those primitive
internals generated from the initial atomic connectivity. If we wish to
constrain a distance, angle or torsion between atoms that are not formally
connected, then all we need to do is add that particular coordinate to our
primitive set. It can then be isolated and constrained in exactly the same way
as a formal connectivity constraint.

Everything discussed thus far regarding the imposition of constraints in
delocalized internal coordinates has involved isolating each constraint in one
vector which is then eliminated from the optimization space. This is very
similar in effect to a *Z*-matrix optimization, in which constraints are
imposed by elimination. This, of course, can only be done if the desired
constraint is satisfied in the starting geometry. We have already seen that the
Lagrange multiplier algorithm, used to impose distance, angle and torsion
constraints in Cartesian coordinates, can be used even when the constraint is
not satisfied initially. The Lagrange multiplier method can also be used with
delocalized internals, and its implementation with internal coordinates brings
several simplifications and advantages.

As already noted, standard internal constraints (bond distances, angles and
torsions) are non-linear functions of the Cartesian coordinates of the atoms
involved. A torsion, for example, which involves four atoms, is a function of
twelve different coordinates. In internals each constraint is a coordinate in
its own right and is therefore a simple linear function of a single coordinate.

If we denote a general internal coordinate by $R$, then the constraint function
$C_{i}(\mathbf{R})$ is a function of one coordinate, $R_{i}$, and it and its
derivatives can be written

<a id="eq:a22a"></a>
$$
C_{i}(R_{i})=R_{i}-R_{0} \tag{9.30}
$$

<a id="eq:a22b"></a>
$$
dC_{i}(R_{i})/dR_{i}=1;\quad dC_{i}(R_{i})/dR_{j}=0 \tag{9.31}
$$

<a id="eq:a22c"></a>
$$
d^{2}C_{i}(R_{i})/dR_{i}dR_{j}=0 \tag{9.32}
$$

where $R_{0}$ is the desired value of the constrained coordinate, and $R_{i}$ is
its current value. From Eq. ([9.31](#eq:a22b)) we see that the constraint normals,
$dC_{i}(\mathbf{R})/dR_{i}$, are simply unit vectors and the Lagrangian Hessian matrix,
Eq. ([9.21](sec_geom_opt_theory_constrained.md#eq:a17)), can be obtained from the normal Hessian matrix by adding
$m$ columns (and $m$ rows) of unit vectors.

A further advantage, in addition to the considerable simplification, is the
handling of $0^{\circ}$ and $180^{\circ}$ dihedral angle constraints. In
Cartesian coordinates it is not possible to formally constrain bond angles and
torsions to exactly $0^{\circ}$ or $180^{\circ}$ because the corresponding
constraint normal is a zero vector. Similar difficulties do not arise in
internal coordinates, at least for torsions, because the constraint normals are
unit vectors regardless of the value of the constraint; thus $0^{\circ}$ and
$180^{\circ}$ dihedral angle constraints can be imposed just as easily as any
other value. $180^{\circ}$ bond angles still cause difficulties, but
near-linear arrangements of atoms require special treatment even in
unconstrained optimizations. A typical solution involves replacing a near
$180^{\circ}$ bond angle by two special linear co-planar and perpendicular
bends,

 and modifying the torsions where necessary. A
linear arrangement can be enforced by constraining the co-planar and
perpendicular bends.

One other advantage over Cartesians is that in internals the constraint
coordinate can be eliminated once the constraint is satisfied to the desired
accuracy (the default tolerance is $10^{-6}$ in atomic units: bohr and
radians). This is not possible in Cartesians due to the functional form of the
constraint. In Cartesians, therefore, the Lagrange multiplier algorithm must be
used throughout the entire optimization, whereas in delocalized internal
coordinates it need only be used until all desired constraints are satisfied.
As constraints become satisfied they can be simply eliminated from the
optimization space and, once all constraint coordinates have been eliminated,
standard algorithms can be used in the space of the remaining unconstrained
coordinates. Unless the starting geometry is particularly poor, constraints are
usually satisfied early in the optimization and at more or less the same time
for multiple constraints. Therefore, Lagrange multipliers only need to be used
in the first half-dozen or so cycles of a constrained optimization in internal
coordinates.
