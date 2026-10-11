---
title: "5.11.1 Introduction"
---

## 5.11.1 Introduction

(July 4, 2026)

Under certain circumstances it is desirable to apply constraints to the
electron density during an SCF calculation. For example, in a transition metal
complex it may be desirable to constrain the net spin density on a particular
metal atom to integrate to a value consistent with the $M_{S}$ value expected
from ligand field theory. Similarly, in a donor/acceptor complex one might be
interested in constraining the total density on the acceptor group so that the
formal charge on the acceptor is either neutral or negatively charged,
depending as the molecule is in its neutral or its charge-transfer state. In
these situations, one is interested in controlling the average value of some
observable, $O(\mathbf{r})$, to take on a given value, $N$:

<a id="Ch5.E69"></a>
$$
\int\rho(\mathbf{r})\,O(\mathbf{r})\;d\mathbf{r}=N \tag{5.69}
$$

There are of course many states that satisfy such a constraint, but in practice
one is usually looking for the lowest energy such state. To solve the
resulting constrained minimization problem, one introduces a Lagrange
multiplier, $V$, and solves for the stationary point of

<a id="Ch5.E70"></a>
$$
V[\rho,V]=E[\rho]-V\left(\int\rho(\mathbf{r})\,O(\mathbf{r})\;d\mathbf{r}-N\right) \tag{5.70}
$$

where $E[\rho]$ is the energy of the system described using density functional
theory (DFT). At convergence, the functional $W$ gives the density, $\rho$,
that satisfies the constraint exactly (*i.e.*, it has exactly the prescribed
number of electrons on the acceptor or spins on the metal center) but has the
lowest energy possible. The resulting self-consistent procedure can be
efficiently solved by ensuring at every SCF step the constraint is satisfied
exactly. The **Q-Chem** implementation of these equations closely parallels
those in Ref. [[1499]](../bib_references/bib.md#bib1557)
.

The first step in any constrained DFT calculation is the specification of the
constraint operator, $O(\mathbf{r})$. Within **Q-Chem**, the user is free to
specify any constraint operator that consists of a linear combination of the
Becke’s atomic partitioning functions[[94]](../bib_references/bib.md#bib73)
 or else the fragment-based
Hirshfeld partition:[[1160]](../bib_references/bib.md#bib1214)

<a id="Ch5.E71"></a>
$$
O(\mathbf{r})=\sum_{A}^{\rm atoms}\sum_{\sigma=\alpha,\beta}C^{\sigma}_{A}\,w_{A}(\mathbf{r}) \tag{5.71}
$$

Here the summation runs over the atoms in the system and over electron spins.
The weight function $w_{A}$ is designed to be $\approx 1$ near the nucleus of
atom $A$ and rapidly fall to zero near the nucleus of any other atom in the system.[[94]](../bib_references/bib.md#bib73)

The original implementation of cDFT in **Q-Chem** used a Becke partition in which the
Voronoi polyhedra are defined by the midpoints of the internuclear vectors,[[1497]](../bib_references/bib.md#bib1561)

but this affords unphysical results.[[556]](../bib_references/bib.md#bib579)

As such,the default value of BECKE_SHIFT
is now set to use the “atomic size corrections” suggested by Becke,[[94]](../bib_references/bib.md#bib73)

in which a set of empirical atomic radii[[1268]](../bib_references/bib.md#bib1321)
 are used to shift the Voronoi
polyhedra away from the bond midpoints and towards
something more realistic for bonds between atoms
of very different size. This correction is most important for cDFT calculations that
are sensitive to the charges on the hydrogen atoms, and cDFT with Becke populations
should probably never be used with these atomic size corrections.[[564]](../bib_references/bib.md#bib582)

The user-specified coefficients $C^{\sigma}_{A}$ are
input using a *$cdft* input section having the following format.

> ```qchem
> $cdft
>    CONSTRAINT_VALUE_X
>    COEFFICIENT1_X       FIRST_ATOM1_X       LAST_ATOM1_X    TYPE1_X
>    COEFFICIENT2_X       FIRST_ATOM2_X       LAST_ATOM2_X    TYPE2_X
>    ...
>    CONSTRAINT_VALUE_Y
>    COEFFICIENT1_Y       FIRST_ATOM1_Y       LAST_ATOM1_Y    TYPE1_Y
>    COEFFICIENT2_Y       FIRST_ATOM2_Y       LAST_ATOM2_Y    TYPE2_Y
>    ...
> $end
> ```

Here, each CONSTRAINT_VALUE is a real number that specifies the
desired average value ($N$) of the ensuing linear combination of atomic
partition functions. Each COEFFICIENT specifies the coefficient of a partition
function or group of partition functions in the constraint operator $O$. For
each coefficient, all the atoms between the integers FIRST_ATOM and
LAST_ATOM contribute with the specified weight in the constraint
operator. Finally, TYPE specifies the type of constraint being
applied—either “CHARGE” or “SPIN”. For a CHARGE constraint the spin up
and spin down densities contribute equally ($C_{A}^{\alpha}=C_{A}^{\beta}=C_{A}$)
yielding the total number of electrons on the atom A. For a SPIN constraint,
the spin up and spin down densities contribute with opposite sign
($C_{A}^{\alpha}-C_{A}^{\beta}=C_{A}$) resulting in a measure of the net spin on
the atom A. Each separate CONSTRAINT_VALUE creates a new operator
whose average is to be constrained—for instance, the example above includes
several independent constraints: `X`, `Y`, $\ldots$. **Q-Chem** can handle an
arbitrary number of constraints and will minimize the energy subject to all of
these constraints simultaneously.

If an atom is not included in a particular operator, then the coefficient of
that atoms partition function is set to zero for that operator. The TYPE
specification is optional, and the default is to perform a charge constraint.
Further, note that any charge constraint is on the *net* atomic charge.
That is, the constraint is on the difference between the average number of
electrons on the atom and the nuclear charge. Thus, to constrain CO to be
negative, the constraint value would be 1 and not 15.

**Note: 

Constraint in *$cdft* specifies the number of excess electrons on a
fragment, not the total charge, *i.e.*, the value 1.0 means charge $=-1$,
whereas charge constraint of $-$1.0 corresponds to the total $+$1 charge.
**

The choice of which atoms to include in different constraint regions is left
entirely to the user and in practice must be based somewhat on chemical
intuition. Thus, for example, in an electron transfer reaction the user must
specify which atoms are in the “donor” and which are in the “acceptor”. In
practice, the most stable choice is typically to make the constrained region as
large as physically possible. Thus, for the example of electron transfer
again, it is best to assign *every* atom in the molecule to one or the
other group (donor or acceptor), recognizing that it makes no sense to assign
any atoms to both groups. On the other end of the spectrum, constraining the
formal charge on a single atom is highly discouraged. The problem is that
while our chemical intuition tells us that the lithium atom in LiF should have
a formal charge of +1, in practice the quantum mechanical charge is much closer
to +0.5 than +1. Only when the fragments are far enough apart do our intuitive
pictures of formal charge actually become quantitative.

Note that the atomic populations that **Q-Chem** prints out are Mulliken
populations, not the Becke weight populations. As a result, the printed
populations will not generally add up to the specified constrained values, even
though the constraint is exactly satisfied. The *$rem* variable CDFT_BECKE_POP
requests that the Becke populations be printed as well, so that the user may confirm that
the computed states have the desired charge and/or spin character.

Finally, we note that SCF convergence is typically more challenging in
constrained DFT calculations as compared to their unconstrained counterparts.
This effect arises because applying the constraint typically leads to a broken
symmetry, diradicaloid state. As SCF convergence for these cases is known to
be difficult even for unconstrained states, it is perhaps not surprising that
there are additional convergence difficulties in this case. See
Section [4.5](../ch04_scf/sect_convergence.md) on SCF convergence algorithms for ideas on how
to improve convergence for constrained calculations. Also, CDFT is more
sensitive to grid size than ground-state DFT, so sometimes increasing the
integration grid improves the convergence. If convergence is problematic,
try using the SG-2 or SG-3 grid (Section [5.5.3](sect_standard-quad.md)).

**Note: 

1.

To improve convergence, use the fewest possible constraints. For
example, if your system consists of two fragments, specify the constrains
for one of them only. The overall charge and multiplicity will force the
“unconstrained” fragment to attain the right charge and multiplicity.

2.

The direct minimization methods are not available for constrained
calculations. Hence, some combination of DIIS and RCA must be used to
obtain convergence. Further, it is often necessary to break symmetry in
the initial guess (using SCF_GUESS_MIX) to ensure that the
lowest energy solution is obtained.

**

Analytic gradients are available for constrained DFT
calculations.[[1500]](../bib_references/bib.md#bib1558)
 Second derivatives are only available by finite
difference of analytic gradients. For details on how to apply constrained DFT
to compute magnetic exchange couplings, see Ref. [[1187]](../bib_references/bib.md#bib1241)
. For
details on using constrained DFT to compute electron transfer parameters, see
Ref. [[1501]](../bib_references/bib.md#bib1559)
.
