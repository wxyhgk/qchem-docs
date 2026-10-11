---
title: "6.14.1 Introduction"
---

## 6.14.1 Introduction

(July 4, 2026)

Electron correlation effects can be qualitatively divided into two classes.
The first class is static or non-dynamical correlation: long wavelength
low-energy correlations associated with other electron configurations that are
nearly as low in energy as the lowest energy configuration. These correlation
effects are important for problems such as homolytic bond breaking, and are the
hardest to describe because by definition the single configuration
Hartree-Fock description is not a good starting point. The second class is
dynamical correlation: short wavelength high-energy correlations associated
with atomic-like effects. Dynamical correlation is essential for
*quantitative* accuracy, but a reasonable description of static
correlation is a prerequisite for a calculation being *qualitatively* correct.

In the methods discussed in the previous several subsections, the objective was
to approximate the total correlation energy. However, in some cases, it is
useful to model directly the non-dynamical and dynamical correlation
energies separately. The reasons for this are pragmatic: with approximate
methods, such a separation can give a more balanced treatment of electron
correlation along bond-breaking coordinates, or reaction coordinates that
involve diradicaloid intermediates. The non-dynamical correlation energy is
conveniently defined as the solution of the Schrödinger equation within a
small basis set composed of valence bonding, anti-bonding and lone pair
orbitals: the so-called full valence active space. Solved exactly, this is
the so-called full valence complete active space SCF (CASSCF),[[1181]](../bib_references/bib.md#bib1234)

or equivalently, the fully optimized reaction space (FORS) method.[[1188]](../bib_references/bib.md#bib1242)

Full valence CASSCF and FORS involve computational complexity which increases
exponentially with the number of atoms, and is thus unfeasible beyond systems
of only a few atoms, unless the active space is further restricted on a
case-by-case basis. **Q-Chem** includes two relatively economical methods that
directly approximate these theories using a truncated coupled-cluster doubles
wave function with optimized orbitals.[[724]](../bib_references/bib.md#bib755)
 They are active space
generalizations of the OD and QCCD methods discussed previously in
Sections [6.12.8](topic_odcc.md) and [6.12.9](topic_qccd.md), and are discussed in the following two
subsections. By contrast with the exponential growth of computational cost with
problem size associated with exact solution of the full valence CASSCF problem,
these cluster approximations have only 6th-order growth of computational
cost with problem size, while often providing useful accuracy.

The full valence space is a well-defined theoretical chemical model. For these
active space coupled-cluster doubles methods, it consists of the union of
*valence* levels that are occupied in the single determinant reference,
and those that are empty. The occupied levels that are to be replaced can only
be the occupied valence and lone pair orbitals, whose number is defined by the
sum of the valence electron counts for each atom (*i.e.*, 1 for H, 2 for He, 1 for
Li, *etc.*.). At the same time, the empty virtual orbitals to which the double
substitutions occur are restricted to be empty (usually anti-bonding) valence
orbitals. Their number is the difference between the number of valence atomic
orbitals, and the number of occupied valence orbitals given above. This
definition (the full valence space) is the default when either of the
“valence” active space methods are invoked (VOD or VQCCD)

There is also a second useful definition of a valence active space, which we
shall call the 1:1 or perfect pairing active space. In this definition, the
number of occupied valence orbitals remains the same as above. The number of
empty correlating orbitals in the active space is defined as being exactly the
same number, so that each occupied orbital may be regarded as being associated
1:1 with a correlating virtual orbital. In the water molecule,
for example, this means that the lone pair electrons as well as the
bond-orbitals are correlated. Generally the 1:1 active space recovers more
correlation for molecules dominated by elements on the right of the periodic
table, while the full valence active space recovers more correlation for
molecules dominated by atoms to the left of the periodic table.

If you wish to specify either the 1:1 active space as described above, or
some other choice of active space based on your particular chemical problem,
then you must specify the numbers of active occupied and virtual orbitals.
This is done via the standard “window options”, documented earlier in this
Chapter.

Finally we note that the entire discussion of active spaces here leads only
to specific numbers of active occupied and virtual orbitals. The orbitals
that are contained within these spaces are optimized by minimizing the trial
energy with respect to all the degrees of freedom previously discussed: the
substitution amplitudes, and the orbital rotation angles mixing occupied and
virtual levels. In addition, there are new orbital degrees of freedom to be
optimized to obtain the best active space of the chosen size, in the sense
of yielding the lowest coupled-cluster energy. Thus rotation angles mixing
active and inactive occupied orbitals must be varied until the energy is
stationary. Denoting inactive orbitals by primes and active orbitals without
primes, this corresponds to satisfying

<a id="eq532"></a>

$$
\frac{\partial E_{\mathrm{CCD}}}{\partial\theta_{i}^{{j}^{\prime}}}=0 \tag{6.80}
$$

Likewise, the rotation angles mixing active and inactive virtual orbitals
must also be varied until the coupled-cluster energy is minimized with
respect to these degrees of freedom:

<a id="eq533"></a>

$$
\frac{\partial E_{\mathrm{CCD}}}{\partial\theta_{a}^{{b}^{\prime}}}=0 \tag{6.81}
$$
