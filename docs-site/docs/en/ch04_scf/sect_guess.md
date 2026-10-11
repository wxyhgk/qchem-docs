---
title: "4.4.2 Initial Guess Types"
---

## 4.4.2 Initial Guess Types

(July 4, 2026)

**Core Hamiltonian**

The core Hamiltonian guess simply obtains the
guess MO coefficients by diagonalizing the core Hamiltonian matrix
in Eq. ([4.19](Ch4.S2.SS2.md#eq417)). It is also commonly known as the one-electron
guess, as it completely ignores interelectronic
interactions. Although the guess is exact for one-electron systems,
the lack of repulsion effects leads to incorrect shell structure of
atoms as well as all electrons crowding onto the heaviest atom in
the system; see Ref. [[797]](../bib_references/bib.md#bib831)
 for a discussion. Due
to these effects, the core guess is typically extremely inaccurate
and should only be used as a last resort; much better alternatives
are provided by the various SAD and SAP guesses.

**Superposition of Atomic Densities (SAD)**

The SAD guess[[801]](../bib_references/bib.md#bib1446)

is constructed by
summing together pretabulated, spherically averaged atomic density
matrices. The SAD guess generally yields robust convergence, and its
use is particularly important when large basis sets and/or large
molecules are employed. There are three issues associated with the
SAD guess to be aware of:

1. **1.**

No molecular orbitals are obtained, which means that SCF
algorithms requiring orbitals (the direct minimization methods
discussed in Section [4.5](sect_convergence.md)) cannot directly use
the SAD guess. It can, however, be generated on-the-fly
for general basis sets (BASIS = GEN), as described below,
though not for mixed basis sets (BASIS = MIXED).
2. **2.**

The SAD guess is not available for general (read-in) basis
sets (pretabulated guesses exist for all internal basis sets); and
3. **3.**

The SAD guess is not idempotent and thus requires *at least*
two SCF iterations to ensure proper SCF convergence
(idempotency of the density).

**Purified Superposition of Atomic Densities (SADMO)**

The purified
SAD guess (called “SADMO” in Ref. [[797]](../bib_references/bib.md#bib831)
), is
otherwise the same as the SAD guess except that it removes the
issues [1](#sad-noorb) and [3](#sad-noid) above. The SADMO guess
obtains guess orbitals and corresponding occupation numbers by
diagonalizing the non-idempotent SAD density matrix, after which an
idempotent density matrix is recreated by aufbau occupation of the
SAD natural orbitals. Since the initial density matrix is created
with the SAD guess, the SADMO guess is not available for a general
(read-in) basis set, either.

**Superposition of Atomic Potentials (SAP)**

The SAP guess[[797]](../bib_references/bib.md#bib831)
 is a major improvement on
the core guess as it correctly describes atomic shell structure
while retaining a simple form. The SAP guess
introduces the interelectronic interactions missing from the core
guess with a superposition of pretabulated atomic potentials, which
have been derived with fully numerical
calculations;[[798]](../bib_references/bib.md#bib832)
 the atomic
potentials used in **Q-Chem** are derived from non-relativistic
exchange-only LDA calculations employing spherically averaged
densities.[[799]](../bib_references/bib.md#bib833)
 As suggested in
Ref. [[797]](../bib_references/bib.md#bib831)
, the atomic potential matrix is
evaluated through quadrature on a molecular grid analogous to the
one used in DFT calculations; the grid is controlled by the *$rem*
variable GUESS_GRID. Importantly, the SAP guess is noniterative,
available for all elements in the periodic table from H to Og, and
can be used with both internal and general (read-in) basis sets,
thereby offering reasonably accurate initial guesses also in the
case when the other options fail to work. Note SAP guess is not
available in the old SCF code but only in GEN_SCFMAN.

**On-the-fly (Automated) Superposition of Atomic Densities
(AUTOSAD)**

In contrast to the SAD option that relies on pretabulated
density matrices, the AUTOSAD guess provides a means of obtaining a
method-specific SAD guess on-the-fly by running separate atomic
calculations on all nonequivalent atoms in the system. As a SAD
guess, the AUTOSAD density matrix is not idempotent and the guess
will not produce molecular orbitals, so direct minimization methods
cannot be directly used. Unlike the SAD option, AUTOSAD can
be used for both internally defined and user-defined (general)
basis sets, but is currently unavailable for mixed
basis. Note that use of AUTOSAD is not necessary when using a single
internal basis set with wave function methods, as in this case the
AUTOSAD density is simply equivalent to the pretabulated SAD
density. The pretabulated SAD guess is based on Hartree-Fock atomic
densities whereas AUTOSAD uses the SCF method specified in *$rem*.

**Generalized Wolfsberg-Helmholtz (GWH)**

The GWH guess
procedure[[1487]](../bib_references/bib.md#bib1547)
 uses a combination of the overlap
matrix elements in Eq. ([4.12](Ch4.S2.SS1.md#eq411)), and the diagonal elements of
the core Hamiltonian matrix in Eq. ([4.19](Ch4.S2.SS2.md#eq417)). This initial
guess is usually even worse than the core Hamiltonian.[[797]](../bib_references/bib.md#bib831)

It is constructed according to

<a id="eq444"></a>
$$
H_{\mu\upsilon}=c_{x}S_{\mu\upsilon}(H_{\mu\mu}+\tfrac{1}{2}H_{\upsilon\upsilon})\;. \tag{4.29}
$$

where $c_{x}$ is a constant, typically $c_{x}=1.75$.

The selection of these choices (or whether to read in the orbitals) is
controlled by the following *$rem* variables:

SCF_GUESS

### `SCF_GUESS`

> **Specifies the initial guess procedure to use for the SCF.**
>
> * **Type**: `STRING`
> * **Default**: `SAD`
> * **Options**:
>     * CORE
>     * Diagonalize core Hamiltonian
>     * SAD
>     * Superposition of atomic density
>     * 801
>     * Lenthe J. H. Van et al.
>     * J. Comput. Chem.
>     * (2006)
>     * ,
>     * 27
>     * ,
>     * pp. 926
>     * .
>     * Link
>     * SAP
>     * Superposition of atomic potentials
>     * 797
>     * Lehtola S.
>     * J. Chem. Theory Comput.
>     * (2019)
>     * ,
>     * 15
>     * ,
>     * pp. 1593
>     * .
>     * Link
>     * (only available with
>     * GEN_SCFMAN
>     * =
>     * TRUE
>     * )
>     * AUTOSAD
>     * On-the-fly superposition of atomic densities
>     * SADMO
>     * Purified superposition of atomic densities (available only with
>     * standard basis sets)
>     * GWH
>     * Apply generalized Wolfsberg-Helmholtz approximation
>     * READ
>     * Read previous MOs from disk
>     * FRAGMO
>     * Superimposing converged
>     * fragment MOs (see Section
>     * 12.3
>     * )
> * **Recommendation**: SAD, AUTOSAD, or SADMO guess for standard basis sets. For either standard or user-customized general basis sets, AUTOSAD is recommended and used as default. If these options fail, use the SAP guess; try the GWH or core Hamiltonian guess only as a last resort. For mixed basis sets, only the AUTOSAD, SAP, GWH, and core Hamiltonian guesses are currently available. For ROHF it can be useful to READ guesses from an SCF calculation on the corresponding cation or anion. Note that because the density is made spherical, this may favor an undesired state for atomic systems, especially transition metals. Use FRAGMO in a fragment MO calculation.

SCF_GUESS_ALWAYS

### `SCF_GUESS_ALWAYS`

> **Switch to force the regeneration of a new initial guess for each series of SCF iterations (for use in geometry optimization).**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * False
>     * Do not generate a new guess for each series of SCF iterations in an
>     * optimization; use MOs from the previous SCF calculation for the guess,
>     * if available.
>     * True
>     * Generate a new guess for each series of SCF iterations in a geometry
>     * optimization.
> * **Recommendation**: Use the default unless SCF convergence issues arise

GUESS_GRID

### `GUESS_GRID`

> **Specifies the type of grid to use for SAP guess generation. The options are the same as those of the $rem variable XC_GRID .**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * Use SG-0 for H, C, N, and O; SG-1 for all other atoms.
>     * $n$
>     * Use SG-
>     * $n$
>     * for all atoms,
>     * $n=1,2$
>     * , or 3
>     * $XY$
>     * A string of two six-digit integers
>     * $X$
>     * and
>     * $Y$
>     * , where
>     * $X$
>     * is the number of radial points
>     * and
>     * $Y$
>     * is the number of angular points where possible numbers of Lebedev angular
>     * points, which must be an allowed value from Table
>     * 5.2
>     * in
>     * Section
>     * 5.5
>     * .
>     * $-XY$
>     * Similar format for Gauss-Legendre grids, with the six-digit integer
>     * $X$
>     * corresponding
>     * to the number of radial points and the six-digit integer
>     * $Y$
>     * providing the number of
>     * Gauss-Legendre angular points,
>     * $Y=2N^{2}$
>     * .
> * **Recommendation**: Larger grids may be required if the SAP guess is poor.
