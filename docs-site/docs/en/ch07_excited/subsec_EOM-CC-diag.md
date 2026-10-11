---
title: "7.9.16 EOM-CC Guess Formation and Iterative Diagonalization"
---

## 7.9.16 EOM-CC Guess Formation and Iterative Diagonalization

(July 4, 2026)

An EOM-CC eigenproblem is solved by an iterative diagonalization procedure
that avoids full diagonalization and only looks for several eigenstates, as
specified by the XX_STATES keywords.
The default procedure is based on the modified Davidson diagonalization algorithm.[[803]](../bib_references/bib.md#bib837)

In addition to several keywords that control the convergence of algorithm, memory usage, and
fine details of its execution, there are several important keywords that allow
user to specify how the target state selection is performed.

By default, the diagonalization looks for several lowest eigenstates, as
specified by XX_STATES. The guess vectors are generated as singly
excited determinants selected by using Koopmans’ theorem; the number of guess
vectors is equal to the number of target states. If necessary, the user can
increase the number of singly excited guess vectors
(EOM_NGUESS_SINGLES) and include doubly excited guess vectors
(EOM_NGUESS_DOUBLES).

**Note: 

In CCMAN2, if there is not enough singly excited guess vectors, the
algorithm adds doubly excited guess vectors. In CCMAN, doubly excited guess
vectors are generated only if EOM_NGUESS_DOUBLES is invoked.
**

The user can request to pre-converge singles (solve the equations in
singles-only block of the Hamiltonian. This is done by using
EOM_PRECONV_SINGLES. In EOM-DEA/DIP calculations,
one can pre-converge $2p$/$2h$ amplitudes by using EOM_PRECONV_DOUBLES.
In the CVS suite of methods, this option is invoked by
CVS_EOM_PRECONV_SINGLES.

**Note: 

In CCMAN, the user can pre-converge both singles and doubles blocks
(EOM_PRECONV_SINGLES and EOM_PRECONV_DOUBLES)
**.

If a state (or several states) of a particular character is desired (*e.g.*,
$\rm HOMO\rightarrow LUMO+10$ excitation or $\rm HOMO-10$ ionization), the user
can specify this by using EOM_USER_GUESS keyword and *$eom_user_guess* section, as illustrated by an example below. The algorithm will attempt to
find an eigenstate that has the maximum overlap with this guess vector. The
multiplicity of the state is determined as in the regular calculations, by
using the XX_SINGLETS and EE_TRIPLETS keywords. This
option is useful for looking for high-lying states such as core-ionized or
core-excited states. It is only available with CCMAN2.

The examples below illustrate how to use user-specified guess in EOM
calculations:

> ```qchem
> $eom_user_guess
>   4  Corresponds to 4(OCC)->5(VIRT) transition.
>   5
> $end
> ```

or

> ```qchem
> $eom_user_guess
>   1  5   Ex. states corresponding to 1(OCC)->5(VIRT) and 1(OCC)->6(VIRT)
>   1  6
> $end
> ```

In IP/EA calculations, only one set of orbitals is specified:

> ```qchem
> $eom_user_guess
>   4 5 6
> $end
> ```

If IP_STATES is specified, this will invoke calculation of the EOM-IP
states corresponding to the ionization from 4th, 5th, and 6th occupied MOs. If
EA_STATES is requested, then EOM-EA equations will be solved for a
root corresponding to electron-attachment to the 4th, 5th, and 6th virtual MOs.

For these options to work correctly, user should make sure that
XX_STATES requests a sufficient number of states. In case of symmetry,
one can request several states in each irrep, but the algorithm will only compute
those states which are consistent with the user guess orbitals.

Alternatively, the user can specify an energy shift by EOM_SHIFT.
In this case, the solver looks for the XX_STATES eigenstates
that are closest to this energy; the guess vectors are
generated accordingly, using Koopmans’ theorem. This option
is useful when highly excited states (*i.e.*, interior eigenstates) are desired.
