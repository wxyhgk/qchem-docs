---
title: "6.19.2 Perfect Pairing (PP)"
---

## 6.19.2 Perfect Pairing (PP)

(July 4, 2026)

To be more specific, the coupled cluster PP wave function is written as

<a id="eqn:PP"></a>
$$
\left|\Psi\right\rangle=\exp\left({\sum_{i=1}^{n_{\mathrm{active}}}{t_{i}\hat{a}_{i\ast}^{{\dagger}}\hat{a}_{\bar{i}\ast}^{{\dagger}}\hat{a}_{\bar{i}}\hat{a}_{i}}}\right)\left|\Phi\right\rangle \tag{6.84}
$$

where $n_{\mathrm{active}}$ is the number of active electrons, and the $t_{i}$ are the
linear number of unknown cluster amplitudes, corresponding to exciting the two
electrons in the $i$th electron pair from their bonding orbital pair to their
anti-bonding orbital pair. In addition to $t_{i}$, the core and the active orbitals
are optimized as well to minimize the PP energy. The algorithm used for this is
a slight modification of the GDM method, described for SCF calculations in
Section [4.5.7](../ch04_scf/sect_gdm.md). Despite the simplicity of the PP wave function, with
only a linear number of correlation amplitudes, it is still a useful
theoretical model chemistry for exploring strongly correlated systems.
This is because it is exact for a single electron pair in the PP active space,
and it is also exact for a collection of non-interacting electron pairs in
this active space. Molecules, after all, are in a sense a collection of
interacting electron pairs! In practice, PP on molecules recovers between 60%
and 80% of the correlation energy in its active space.

If the calculation is perfect pairing (CORRELATION = PP), it is
possible to look for unrestricted solutions in addition to restricted ones.
Unrestricted orbitals are the default for molecules with odd numbers of
electrons, but can also be specified for molecules with even numbers of
electrons. This is accomplished by setting GVB_UNRESTRICTED = TRUE.
Given a restricted guess, this will, however usually converge to a restricted
solution anyway, so additional REM variables should be specified to ensure an
initial guess that has broken spin symmetry. This can be accomplished by using
an unrestricted SCF solution as the initial guess, using the techniques
described in Chapter [4](../ch04_scf/chap_scf.md). Alternatively a restricted set of guess
orbitals can be explicitly symmetry broken just before the calculation starts
by using GVB_GUESS_MIX, which is described below. There is also the
implementation of Unrestricted-in-Active Pairs (UAP),[[774]](../bib_references/bib.md#bib807)
 which
is the default unrestricted implementation for GVB methods. This method
simplifies the process of unrestriction by optimizing only one set of ROHF MO
coefficients and a single rotation angle for each occupied-virtual pair. These
angles are used to construct a series of $2\times 2$ Givens rotation matrices which
are applied to the ROHF coefficients to determine the $\alpha$ spin MO
coefficients and their transpose is applied to the ROHF coefficients to
determine the $\beta$ spin MO coefficients. This algorithm is fast and
eliminates many of the pathologies of the unrestricted GVB methods near the
dissociation limit. To generate a full potential curve we find it is best to
start at the desired UHF dissociation solution as a guess for GVB and follow it
inwards to the equilibrium bond distance.

GVB_UNRESTRICTED

### `GVB_UNRESTRICTED`

> **Controls restricted versus unrestricted PP jobs. Usually handled automatically.**
>
> * **Type**: `LOGICAL`
> * **Default**: `same value as UNRESTRICTED`
> * **Options**:
>     * TRUE/FALSE
> * **Recommendation**: Set this variable explicitly only to do a UPP job from an RHF or ROHF initial guess. Leave this variable alone and specify UNRESTRICTED = TRUE to access the new unrestricted-in-active-pairs GVB code which can return an RHF or ROHF solution if used with GVB_DO_ROHF

GVB_DO_ROHF

### `GVB_DO_ROHF`

> **Sets the number of Unrestricted-in-Active Pairs to be kept restricted.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * User-Defined
> * **Recommendation**: If $n$ is the same value as GVB_N_PAIRS returns the ROHF solution for GVB, only works with the UNRESTRICTED = TRUE implementation of GVB with GVB_OLD_UPP = 0 (its default value)

GVB_OLD_UPP

### `GVB_OLD_UPP`

> **Which unrestricted algorithm to use for GVB.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use Unrestricted-in-Active Pairs described in Ref.
>     * 774
>     * Lawler K. V., Small D. W., Head-Gordon M.
>     * J. Phys. Chem. A
>     * (2010)
>     * ,
>     * 114
>     * ,
>     * pp. 2930
>     * .
>     * Link
>     * 1
>     * Use Unrestricted Implementation described in Ref.
>     * 110
>     * Beran G. J. O. et al.
>     * J. Phys. Chem. A
>     * (2005)
>     * ,
>     * 109
>     * ,
>     * pp. 9183
>     * .
>     * Link
> * **Recommendation**: Only works for Unrestricted PP and no other GVB model.

GVB_GUESS_MIX

### `GVB_GUESS_MIX`

> **Similar to SCF_GUESS_MIX , it breaks alpha/beta symmetry for UPP by mixing the alpha HOMO and LUMO orbitals according to the user-defined fraction of LUMO to add the HOMO. 100 corresponds to a 1:1 ratio of HOMO and LUMO in the mixed orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * User-defined,
>     * $0\leq n\leq 100$
> * **Recommendation**: 25 often works well to break symmetry without overly impeding convergence.

Whilst all of the description in this section refers to PP solved via
projection, it is also possible, as described in Section [6.19.3](subsec_CCVB.md) below,
to solve variationally for the PP energy. This variational PP solution is the
reference wave function for the CCVB method. In most cases use of spin-pure
CCVB is preferable to attempting to improve restricted PP by permitting the
orbitals to spin polarize.
