---
title: "5.11.5 Configuration Interaction with Constrained DFT (CDFT-CI)"
---

## 5.11.5 Configuration Interaction with Constrained DFT (CDFT-CI)

(July 4, 2026)

There are some situations in which a system is not well-described by a
DFT calculation on a single configuration. For example, transition
states are known to be poorly described by most functionals, with
the computed barrier being too low. We can, in particular, identify
homolytic dissociation of diatomic species as situations where static
correlation becomes extremely important. Existing DFT functionals
have proved to be very effective in capturing dynamic correlation,
but frequently exhibit difficulties in the presence of strong
static correlation. Configuration interaction (CI), well known in
wave function methods, is a multireference approach that is
well-suited for capturing static correlation; the CDFT-CI technique
allows for CI calculations on top of DFT calculations, harnessing
both static and dynamic correlation methods.

Constrained DFT is used to compute densities (and Kohn-Sham wave functions) for
two or more diabatic-like states; these states are then used to build a CI
matrix. Diagonalizing this matrix yields energies for the ground *and*
excited states within the configuration space. The coefficients of the
initial diabatic states are printed, to show the characteristics of the
resultant states.

Since DFT only gives converged densities, not actual wave functions, computing
the off-diagonal coupling elements $H_{12}$ is not completely straightforward,
as the physical meaning of the Kohn-Sham wave function is not entirely clear.
We can, however, perform the following manipulation:[[1502]](../bib_references/bib.md#bib1560)

<a id="A3.S8.EGx20"></a>

$$
\displaystyle\begin{aligned} \displaystyle H_{12}&\displaystyle=\frac{1}{2}\Bigl{[}\langle 1|H+V_{C_{1}}\omega_{C_{1}}-V_{C1}\omega_{C_{1}}|2\rangle+\langle 1|H+V_{C_{2}}\omega_{C_{2}}-V_{C_{2}}\omega_{C_{2}}|2\rangle\Bigr{]}\\
&\displaystyle=\frac{1}{2}\Bigl{[}\left(E_{1}+V_{C_{1}}N_{C_{1}}+E_{2}+V_{C_{2}}N_{C_{2}}\right)\langle 1|2\rangle-V_{C_{1}}\langle 1|\omega_{C_{1}}|2\rangle-V_{C_{2}}\langle 1|\omega_{C_{2}}|2\rangle\Bigr{]}\end{aligned} \tag{5.74}
$$

where the converged states $|i\rangle$ are assumed to be the
ground state of $H+V_{C_{i}}\omega_{C_{i}}$ with eigenvalue $E_{i}+V_{C_{i}}N_{C_{i}}$).
This manipulation eliminates the two-electron integrals from the
expression, and experience has shown that the use of Slater determinants
of Kohn-Sham orbitals is a reasonable approximation for the
quantities $\langle 1|2\rangle$ and $\langle 1|\omega_{C_{i}}|2\rangle$.

Note that since these constrained states are eigenfunctions of different
Hamiltonians (due to different constraining potentials), they are *not*
orthogonal states, and we must set up our CI matrix as a generalized eigenvalue
problem. Symmetric orthogonalization is used by default, though the overlap
matrix and Hamiltonian in non-orthogonal basis are also printed at higher print
levels so that other orthogonalization schemes can be used after-the-fact. In
a limited number of cases, it is possible to find an orthogonal basis for the
CDFT-CI Hamiltonian, where a physical interpretation can be assigned to the
orthogonal states. In such cases, the matrix representation of the Becke
weight operator is diagonalized, and the (orthogonal) eigenstates can be
characterized.[[1497]](../bib_references/bib.md#bib1561)
 This matrix is printed as the “CDFT-CI
Population Matrix” at increased print levels.

In order to perform a CDFT-CI calculation, the $N$ interacting states must be
defined, which is accomplished using a *$cdft* input section in a fashion
similar to the specification of CDFT states:

> ```qchem
> $cdft
> STATE_1_CONSTRAINT_VALUE_X
> COEFFICIENT1_X       FIRST_ATOM1_X       LAST_ATOM1_X    TYPE1_X
> COEFFICIENT2_X       FIRST_ATOM2_X       LAST_ATOM2_X    TYPE2_X
> ...
> STATE_1_CONSTRAINT_VALUE_Y
> COEFFICIENT1_Y       FIRST_ATOM1_Y       LAST_ATOM1_Y    TYPE1_Y
> COEFFICIENT2_Y       FIRST_ATOM2_Y       LAST_ATOM2_Y    TYPE2_Y
> ...
> ---
> STATE_2_CONSTRAINT_VALUE_X
> COEFFICIENT1_X       FIRST_ATOM1_X       LAST_ATOM1_X    TYPE1_X
> COEFFICIENT2_X       FIRST_ATOM2_X       LAST_ATOM2_X    TYPE2_X
> ...
> STATE_2_CONSTRAINT_VALUE_Y
> COEFFICIENT1_Y       FIRST_ATOM1_Y       LAST_ATOM1_Y    TYPE1_Y
> COEFFICIENT2_Y       FIRST_ATOM2_Y       LAST_ATOM2_Y    TYPE2_Y
> ...
> $end
> ```

Each state is specified with the CONSTRAINT_VALUE and the
corresponding weights on sets of atoms whose average value should be the
constraint value. Different states are separated by a single line containing
three or more dash characters.

If it is desired to use an unconstrained state as one of the interacting
configurations, charge and spin constraints of zero may be applied to the atom
range from 0 to 0.

!!! note "Note"
    It is mandatory to specify a spin constraint corresponding to every
    charge constraint (and it must be immediately following that charge constraint
    in the input deck), for reasons described below.


In addition to the *$cdft* input section of the input file, a CDFT-CI
calculation must also set the CDFTCI flag to TRUE for the calculation
to run. Note, however, that the CDFT flag is used internally by
CDFT-CI, and should *not* be set in the input deck. The variable
CDFTCI_PRINT may also be set manually to control the level of output.
The default is 0, which will print the energies and weights (in the diabatic
basis) of the $N$ CDFT-CI states. Setting it to 1 or above will also print the
CDFT-CI overlap matrix, the CDFT-CI Hamiltonian matrix before the change of
basis, and the CDFT-CI Population matrix. Setting it to 2 or above will also
print the eigenvectors and eigenvalues of the CDFT-CI Population matrix.
Setting it to 3 will produce more output that is only useful during application
debugging.

For convenience, if CDFTCI_PRINT is not set in the input
file, it will be set to the value of SCF_PRINT.

As mentioned in the previous section, there is a disparity between our chemical
intuition of what charges should be and the actual quantum-mechanical charge.
The example was given of LiF, where our intuition gives the lithium atom a
formal charge of $+1$; we might similarly imagine performing a CDFT-CI
calculation on $\text{H}_{2}$, with two ionic states and two spin-constrained
states. However, this would result in attempting to force both electrons of
$\text{H}_{2}$ onto the same nucleus, and this calculation is impossible to
converge (since by the nature of the Becke weight operators, there will be some
non-zero amount of the density that gets proportioned onto the other atom, at
moderate internuclear separations). To remedy problems such as this, we have
adopted a mechanism by which to convert the formal charges of our chemical
intuition into reasonable quantum-mechanical charge constraints. We use the
formalism of “promolecule” densities, wherein the molecule is divided into
fragments (based on the partitioning of constraint operators), and a DFT
calculation is performed on these fragments, completely isolated from each
other.[[1497]](../bib_references/bib.md#bib1561)
 (This step is why both spin and charge constraints are
required, so that the correct partitioning of electrons for each fragment may
be made.) The resulting promolecule densities, converged for the separate
fragments, are then added together, and the value of the various weight
operators as applied to this new density, is used as a constraint for the
actual CDFT calculations on the interacting states. The promolecule density
method compensates for the effect of nearby atoms on the actual density that
will be constrained.

The comments about SCF convergence for CDFT calculations also apply to the
calculations used for CDFT-CI, with the addition that if the SCF converges but
CDFT does not, it may be necessary to use a denser integration grid or reduce
the value of CDFT_THRESH.

Analytic gradients are not available. Many of the CDFT-related *$rem* variables
are also applicable to CDFT-CI calculations. For details on using CDFT-CI to
calculate reaction barrier heights, see Ref. [[1498]](../bib_references/bib.md#bib1562)
.
