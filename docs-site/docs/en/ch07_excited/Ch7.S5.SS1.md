---
title: "7.5.1 Introduction"
---

## 7.5.1 Introduction

(July 4, 2026)

Systems such as transition metals, open-shell species, and molecules with
highly-stretched bonds often exhibit multiple, near-degenerate solutions to the
SCF equations. Multiple solutions can be located using SCF metadynamics
(Section [4.9.2](../ch04_scf/sec_SCF-meta-dyn.md)), but given the approximate nature of the SCF
calculation in the first place, there is in such cases no clear reason to
choose one of these solutions over another. These SCF solutions are not
subject to any non-crossing rule, and often do cross (*i.e.*, switch energetic
order) as the geometry is changed. Consequently, the lowest energy state may switch
abruptly with consequent discontinuities in the energy gradients. It is
therefore desirable to have a method that treats all of these near-degenerate
SCF solutions on an equal footing and might yield a smoother, qualitatively
correct potential energy surface. This can be achieved by using multiple SCF
solutions (obtained, *via* *e.g.* SCF metadynamics) as a basis for a
configuration interaction (CI) calculation. Since the various SCF solutions
are not orthogonal to one another — meaning that one solution cannot be
constructed as a single determinant composed of orbitals from another
solution — this CI is a bit more complicated and is denoted as a non-orthogonal
CI (NOCI).[[1356]](../bib_references/bib.md#bib1417)

NOCI can be viewed as an alternative to CASSCF within an “active space”
consisting of the SCF states of interest, and has the advantage that the SCF
states, and thus the NOCI wave functions, are size-consistent. In common with
CASSCF, it is able to describe complicated phenomena such as avoided crossings
(where states mix instead of passing through each other) as well as conical
intersections (whereby via symmetry or else accidental reasons, there is no
coupling between the states, and they pass cleanly through each other at a
degeneracy).

Another use for a NOCI calculation is that of symmetry restoration. At some
geometries, the SCF states break spatial or spin symmetry to achieve a lower
energy single determinant than if these symmetries were conserved. As these
symmetries still exist within the proper electronic Hamiltonian, its exact
eigenfunctions should preserve them. In the case of spin, this manifests as
spin contamination, while for spatial symmetries it usually manifests as
artefactual localization. To recover a (yet lower energy) wave function
retaining the correct symmetries, one can include these broken-symmetry states
(with all relevant symmetry permutations) in a NOCI calculation; the resultant
eigenfunction will have the true symmetries restored, as a linear combination
of the broken-symmetry states.

A common example occurs in the case of a spin-contaminated UHF reference state.
Performing a NOCI calculation in a basis consisting of this state, plus a
second state in which all $\alpha$ and $\beta$ orbitals have been switched,
often reduces spin contamination in the same way as the half-projected
Hartree-Fock method,[[924]](../bib_references/bib.md#bib960)
 although there is no guarantee that the
resulting wave function is an eigenfunction of $\hat{S}^{2}$. Another example
consists of using a UHF wave function with $M_{S}=0$, along with its
spin-exchanged version (wherein all $\alpha\leftrightarrow\beta$ orbitals are
switched), resulting in two new NOCI eigenfunctions, one with even $S$ (a
mixture of $S=0,2,\ldots$), and one with odd $S$ (mixing $S=1,3,\ldots$).
These may be used to approximate singlet and triplet wave functions.

NOCI can be enabled by specifying CORRELATION = NOCI, and will
automatically use all of the states located with SCF metadynamics. Two
spin-exchanged versions of a UHF wave function can be requested simply by
*not* turning on metadynamics. For more customization, a *$noci* input
section can be included having, *e.g.*, the following format:

> ```qchem
> $noci
>    1 2 -2 4
>    2
> $end
> ```

In this particular case, the first line specifies that states 1, 2, and 4 are
to be included in the NOCI calculation, along with state “$-$2”, which
indicates the spin-exchanged version of state 2. The second (optional) line
indicates which eigenvalue is to be returned to **Q-Chem**, with the convention
that 0 indicates the lowest state so the *$noci* input section above is
requesting the third state.

Analytic gradients are not available for NOCI but geometry optimizations (if requested) will be
performed automatically using finite-difference gradients.
