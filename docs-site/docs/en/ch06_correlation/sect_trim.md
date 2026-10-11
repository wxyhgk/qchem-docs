---
title: "6.5.1 Local Triatomics in Molecules (TRIM) Model"
---

## 6.5.1 Local Triatomics in Molecules (TRIM) Model

(July 4, 2026)

The development of what may be called “fast methods” for evaluating electron
correlation is a problem of both fundamental and practical importance, because
of the unphysical increases in computational complexity with molecular size
which afflict “exact” implementations of electron correlation methods.
Ideally, the development of fast methods for treating electron correlation
should not impact either model errors or numerical errors associated with the
original electron correlation models. Unfortunately this is not possible at
present, as may be appreciated from the following rough argument. *Spatial locality*
is what permits re-formulations of electronic structure methods that
yield the same answer as traditional methods, but faster. The one-particle
density matrix decays exponentially with a rate that relates to the HOMO/LUMO
gap in periodic systems. When length scales longer than this characteristic
decay length are examined, sparsity will emerge in both the one-particle
density matrix and also pair correlation amplitudes expressed in terms of
localized functions. Very roughly, such a length scale is about 5 to 10 atoms
in a line, for good insulators such as alkanes. Hence sparsity emerges beyond
this number of atoms in 1-D, beyond this number of atoms squared in 2-D, and
this number of atoms cubed in 3-D. Thus for three-dimensional systems,
locality only begins to emerge for systems of between hundreds and thousands of atoms.

If we wish to accelerate calculations on systems below this size regime, we
must therefore introduce additional errors into the calculation, either as
numerical noise through looser tolerances, or by modifying the theoretical
model, or perhaps both. **Q-Chem**’s approach to local electron correlation is
based on modifying the theoretical models describing correlation with an
additional well-defined local approximation. We do not attempt to accelerate
the calculations by introducing more numerical error because of the
difficulties of controlling the error as a function of molecule size, and the
difficulty of achieving reproducible significant results. From this
perspective, local correlation becomes an integral part of specifying the
electron correlation treatment. This means that the considerations necessary
for a correlation treatment to qualify as a well-defined theoretical model
chemistry apply equally to local correlation modeling. The local approximations should be

- •

*Size-consistent:* meaning that the energy of a super-system of two
non-interacting molecules should be the sum of the energy obtained from
individual calculations on each molecule.
- •

*Uniquely defined:* Require no input beyond nuclei, electrons, and
an atomic orbital basis set. In other words, the model should be uniquely
specified without customization for each molecule.
- •

*Yield continuous potential energy surfaces:* The model
approximations should be smooth, and not yield energies that exhibit
jumps as nuclear geometries are varied.

To ensure that these model chemistry criteria are met, **Q-Chem**’s local MP2
methods[[790]](../bib_references/bib.md#bib819)
 express the double substitutions (*i.e.*, the
pair correlations) in a redundant basis of atom-labeled functions. The
advantage of doing this is that local models satisfying model chemistry
criteria can be defined by performing an *atomic truncation* of the double
substitutions. A general substitution in this representation will then involve
the replacement of occupied functions associated with two given atoms by empty
(or virtual) functions on two other atoms, coupling together four different
atoms. We can force one occupied to virtual substitution (of the two that
comprise a double substitution) to occur only between functions on the same
atom, so that only three different atoms are involved in the double
substitution. This defines the *triatomics in molecules* (TRIM) local
model for double substitutions. The TRIM model offers the potential for
reducing the computational requirements of exact MP2 theory by a factor
proportional to the number of atoms. We could also force each occupied to
virtual substitution to be on a given atom, thereby defining a more drastic
*diatomics in molecules* (DIM) local correlation model.

The simplest atom-centered basis that is capable of spanning the occupied
space is a *minimal basis* of core and valence atomic orbitals on each
atom. Such a basis is necessarily redundant because it also contains sufficient
flexibility to describe the empty valence anti-bonding orbitals necessary to
correctly account for non-dynamical electron correlation effects such as
bond-breaking. This redundancy is actually important for the success of the
atomic truncations because occupied functions on adjacent atoms to some extent
describe the same part of the occupied space. The minimal functions we use to
span the occupied space are obtained at the end of a large basis set
calculation, and are called *extracted polarized atomic orbitals*
(EPAOs).[[789]](../bib_references/bib.md#bib820)
 We discuss them briefly below. It is even possible to
explicitly perform an SCF calculation in terms of a molecule-optimized minimal
basis of *polarized atomic orbitals* (PAOs); see Chapter [4](../ch04_scf/chap_scf.md).
To span the virtual space, we use the full set of atomic orbitals,
appropriately projected into the virtual space.

We summarize the situation. The number of functions spanning the occupied
subspace will be the minimal basis set dimension, $M$, which is greater than
the number of occupied orbitals, $O$, by a factor of up to about two. The
virtual space is spanned by the set of projected atomic orbitals whose number
is the atomic orbital basis set size $N$, which is fractionally greater than
the number of virtuals $VNO$. The number of double substitutions in such a
redundant representation will be typically three to five times larger than the
usual total. This will be more than compensated by reducing the number of
retained substitutions by a factor of the number of atoms, $A$, in the local
triatomics in molecules model, or a factor of $A^{2}$ in the diatomics in
molecules model.

The local MP2 energy in the TRIM and DIM models are given by the following
expressions, which can be compared against the full MP2 expression given
earlier in Eq. ([6.13](Ch6.S3.SS1.md#eq512)). First, for the DIM model:

<a id="eq516"></a>
$$
E_{\mathrm{DIM\,MP2}}=-\frac{1}{2}\sum_{\bar{P},\bar{Q}}\frac{(\bar{P}|\bar{Q})(\bar{P}||\bar{Q})}{\Delta_{\bar{P}}+\Delta_{\bar{Q}}} \tag{6.17}
$$

The sums run over the linear number of atomic single excitations after they
have been canonicalized. Each term in the denominator is thus an energy
difference between occupied and virtual levels in this local basis.
Similarly, the TRIM model corresponds to the following local MP2 energy:

<a id="eq517"></a>
$$
E_{\mathrm{TRIM\,MP2}}=-\sum_{\bar{P},jb}\frac{(\bar{P}|jb)(\bar{P}||jb)}{\Delta_{\bar{P}}+\varepsilon_{b}-\varepsilon_{j}}-E_{\mathrm{DIM\,MP2}} \tag{6.18}
$$

where the sum is now mixed between atomic substitutions $\bar{P}$, and non-local
occupied $j$ to virtual $b$ substitutions. See
Refs. [[790]](../bib_references/bib.md#bib819)
 for a full derivation and discussion.

The accuracy of the local TRIM and DIM models has been tested in a series of
calculations.[[790]](../bib_references/bib.md#bib819)
 In particular, the TRIM model
has been shown to be quite faithful to full MP2 theory via the following tests:

- •

The TRIM model recovers around 99.7% of the MP2 correlation energy for
covalent bonding. This is significantly higher than the roughly 98–99%
correlation energy recovery typically exhibited by the Saebo-Pulay local
correlation method.[[1194]](../bib_references/bib.md#bib1249)
 The DIM model recovers around
95% of the correlation energy.
- •

The performance of the TRIM model for relative energies is very robust,
as shown in Ref. [[790]](../bib_references/bib.md#bib819)
 for the challenging case of
torsional barriers in conjugated molecules. The RMS error in these
relative energies is only 0.031 kcal/mol, as compared to around 1
kcal/mol when electron correlation effects are completely neglected.
- •

For the water dimer with the aug-cc-pVTZ basis, 96% of the MP2
contribution to the binding energy is recovered with the TRIM model, as
compared to 62% with the Saebo-Pulay local correlation method.
- •

For calculations of the MP2 contribution to the G3 and G3(MP2) energies
with the larger molecules in the G3-99 database,[[294]](../bib_references/bib.md#bib300)

introduction of the TRIM approximation results in an RMS error relative
to full MP2 theory of only 0.3 kcal/mol, even though the absolute
magnitude of these quantities is on the order of tens of kcal/mol.
