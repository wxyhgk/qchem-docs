---
title: "9.1.4 Delocalized Internal Coordinates"
---

## 9.1.4 Delocalized Internal Coordinates

(July 4, 2026)

The choice of coordinate system can have a major influence on the rate of
convergence during a geometry optimization. For complex potential energy
surfaces with many stationary points, a different choice of coordinates can
even result in convergence to a different final structure.

The key attribute of a good set of coordinates for geometry optimization is the
degree of coupling between the individual coordinates. In general, the less
coupling the better, as variation of one particular coordinate will then have
minimal impact on the other coordinates. Coupling manifests itself primarily as
relatively large partial derivative terms between different coordinates. For
example, a strong harmonic coupling between two different coordinates, $i$ and
$j$, results in a large off-diagonal element, $H_{ij}$, in the Hessian
matrix. Normally this is the only type of coupling that can be
directly “observed” during an optimization, as third and higher derivatives
are ignored in almost all optimization algorithms.

In the early days of computational quantum chemistry geometry optimizations
were carried out in Cartesian coordinates. They are an obvious choice as
they can be defined for all systems and gradients and second derivatives are
calculated directly in Cartesian coordinates. Unfortunately, Cartesian
coordinates are often heavily coupled, making them a poor choice for
optimizations. Despite this, Cartesians have recently returned to favor
because of their generality, and because it has been clearly demonstrated that
if reliable second derivative information is available (*i.e.*, a good starting
Hessian) and the initial geometry is reasonable, then Cartesians can be as
efficient as any other coordinate set for small to medium-sized
molecules.[[62]](../bib_references/bib.md#bib47)
 Without good Hessian data, however,
Cartesians are inefficient, especially for long chain acyclic systems.

In the 1970s Cartesians were replaced by *Z*-matrix coordinates. Initially the
*Z*-matrix was used simply as a means of geometry input; it is far easier to
describe a molecule in terms of bond lengths, bond angles and dihedral angles
(the natural coordinates for a chemist) than to develop a suitable set of
Cartesian coordinates. It was subsequently found that optimization was
generally more efficient in *Z*-matrix coordinates than in Cartesians,
especially for acyclic systems. This is not always the case, and care must be
taken in constructing a suitable *Z*-matrix. A good general rule is ensure that
each variable is defined in such a way that changing its value will not change
the values of any of the other variables. A brief discussion concerning good
*Z*-matrix construction strategy is given by Schlegel.[[1211]](../bib_references/bib.md#bib1266)

In 1979 Pulay *et al.* published a key paper introducing what were termed
natural internal coordinates into geometry optimization.[[1133]](../bib_references/bib.md#bib1181)

These coordinates involve the use of individual bond displacements as
stretching coordinates, but linear combinations of bond angles and torsions as
deformational coordinates. Suitable linear combinations of bends and torsions
(the two are considered separately) are selected using group theoretical
arguments based on local pseudo-symmetry. For example, bond angles around an
$sp^{3}$ hybridized carbon atom are all approximately tetrahedral, regardless
of the groups attached, and idealized tetrahedral symmetry can be used to
generate deformational coordinates around the central carbon atom.

The major advantage of natural internal coordinates in geometry optimization is
their ability to significantly reduce the coupling, both harmonic and
anharmonic, between the various coordinates. Compared to natural internals,
*Z*-matrix coordinates arbitrarily omit some angles and torsions (to prevent
redundancy), and this can induce strong anharmonic coupling between the
coordinates, especially with a poorly constructed *Z*-matrix. Another advantage
of the reduced coupling is that successful minimizations can be carried out in
natural internals with only an approximate (*e.g.*, diagonal) Hessian provided
at the starting geometry. A good starting Hessian is still needed for a
transition state search.

Despite their clear advantages, natural internals have only become widely used
more recently. This is because, when used in the early programs, it was
necessary for the user to define them. This situation changed in 1992 with the
development of computational algorithms capable of automatically generating
natural internals from input Cartesians.[[396]](../bib_references/bib.md#bib405)
 For minimization,
natural internals have become the coordinates of first choice.[[396]](../bib_references/bib.md#bib405)

There are some disadvantages to natural internal coordinates as they are
commonly constructed and used:

- Algorithms for the automatic construction of natural internals are
complicated. There are a large number of structural possibilities, and to
adequately handle even the most common of them can take several thousand
lines of code.
- For the more complex molecular topologies, most assigning algorithms
generate more natural internal coordinates than are required to
characterize all possible motions of the system (*i.e.*, the generated
coordinate set contains redundancies).
- In cases with a very complex molecular topology (*e.g.*, multiply fused
rings and cage compounds) the assigning algorithm may be unable to
generate a suitable set of coordinates.

The redundancy problem has been addressed in an excellent paper by
Pulay and Fogarasi,[[1134]](../bib_references/bib.md#bib1184)
 who have developed a scheme for carrying
out geometry optimization directly in the redundant coordinate space.

Baker *et al.*[[63]](../bib_references/bib.md#bib50)
 developed a set of delocalized internal
coordinates that eliminate all of the above-mentioned
difficulties. Building on some of the ideas in the redundant optimization
scheme of Pulay and Fogarasi,[[1134]](../bib_references/bib.md#bib1184)
 delocalized internals form a
complete, non-redundant set of coordinates which are as good as, if not
superior to, natural internals, and which can be generated in a simple and
straightforward manner for essentially any molecular topology, no matter how
complex.

Consider a set of $n$ internal coordinates $\mathbf{q}=(q_{1},q_{2},\ldots q_{n})^{t}$
Displacements $\Delta\mathbf{q}$ in $\mathbf{q}$ are related to the corresponding
Cartesian displacements $\Delta\mathbf{x}$ by means of the usual
Wilson $\mathbf{B}$-matrix,

<a id="Ch9.E15"></a>

$$
\Delta\mathbf{q}=\mathbf{B}\Delta\mathbf{x} \tag{9.15}
$$

If any of the internal coordinates $\mathbf{q}$ are redundant, then the rows
of the $\mathbf{B}$-matrix will be linearly dependent.

Delocalized internal coordinates are obtained by constructing and
diagonalizing the matrix $\mathbf{G}=\mathbf{BB}^{t}$. Diagonalization of $\mathbf{G}$
results in two sets of eigenvectors; a set of $m$ (typically $3N-6$, where $N$
is the number of atoms) eigenvectors with eigenvalues $\lambda>0$, and a set
of $nm$ eigenvectors with eigenvalues $\lambda=0$ (to numerical precision).
In this way, any redundancies present in the original coordinate set $\mathbf{q}$
are isolated (they correspond to those eigenvectors with zero eigenvalues).
The eigenvalue equation of $\mathbf{G}$ can thus be written

<a id="eq:a13"></a>

$$
{\rm{\bf G}}({\rm{\bf UR}})=({\rm{\bf UR}})\left({{\begin{array}[]{*{2}c}\Lambda&0\\
0&0\\
\end{array}}}\right) \tag{9.16}
$$

where $\mathbf{U}$ is the set of non-redundant eigenvectors of $\mathbf{G}$ (those with
$\lambda>0$) and $\mathbf{R}$ is the corresponding redundant set.

The nature of the original set of coordinates $\mathbf{q}$ is unimportant, as long
as it spans all the degrees of freedom of the system under consideration. We
include in $\mathbf{q}$, all bond stretches, all planar bends and all proper
torsions that can be generated based on the atomic connectivity. These
individual internal coordinates are termed *primitives*. This blanket
approach generates far more primitives than are necessary, and the set $\mathbf{q}$
contains much redundancy. This is of little concern, as solution of
Eq. ([9.16](#eq:a13)) takes care of all redundancies.

Note that eigenvectors in both $\mathbf{U}$ and $\mathbf{R}$ will each be linear
combinations of potentially all the original primitives. Despite this apparent
complexity, we take the set of non-redundant vectors $\mathbf{U}$ as our working
coordinate set. Internal coordinates so defined are much more delocalized than
natural internal coordinates (which are combinations of a relatively small
number of bends or torsions) hence, the term delocalized internal coordinates.

It may appear that because delocalized internals are such a complicated
mixing of the original primitive internals, they are a poor choice for use
in an actual optimization. On the contrary, arguments can be made that
delocalized internals are, in fact, the “best” possible choice, certainly at
the starting geometry. The interested reader is referred to the original
literature for more details.[[63]](../bib_references/bib.md#bib50)

The situation for geometry optimization, comparing Cartesian, *Z*-matrix and
delocalized internal coordinates, and assuming a “reasonable” starting
geometry, is as follows:

- For small or very rigid medium-sized systems (up to about 15 atoms),
optimizations in Cartesian and internal coordinates (“good” *Z*-matrix or
delocalized internals) should perform similarly.
- For medium-sized systems (say 15–30 atoms) optimizations in Cartesians
should perform as well as optimizations in internal coordinates, provided
a reliable starting Hessian is available.
- For large systems (30+ atoms), unless these are very rigid, neither
Cartesian nor *Z*-matrix coordinates can compete with delocalized
internals, even with good quality Hessian information. As the system
increases, and with less reliable starting geometries, the advantage of
delocalized internals only increases.

There is one particular situation in which Cartesian coordinates may be the
best choice. Natural internal coordinates (and by extension delocalized
internals) show a tendency to converge to low energy structures.[[61]](../bib_references/bib.md#bib49)

This is because steps taken in internal coordinate space
tend to be much larger when translated into Cartesian space As a result,
higher-energy local minima tend to be “jumped over”, especially if there is
no reliable Hessian information available (which is generally not needed for a
successful optimization). Consequently, if the user is looking for a local
minimum (*i.e.*, a meta-stable structure) and has both a good starting geometry
and a decent Hessian, the user should carry out the optimization in Cartesian
coordinates.
