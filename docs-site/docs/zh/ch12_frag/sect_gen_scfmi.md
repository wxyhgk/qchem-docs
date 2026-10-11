---
title: "12.6.2 Generalized SCF-MI Calculations and Additional Features"
---

## 12.6.2 Generalized SCF-MI Calculations and Additional Features

(July 4, 2026)

The original definition of the ALMOs used in SCF-MI calculations is based on the
fragment-blocking structure of the AO-to-MO transformation matrix, *i.e.*, for a
given fragment, the associated MOs can only be expanded by the AO basis
functions centered on the atoms that belong to the same fragment. Here we
propose a generalized definition for SCF-MI calculations: given a set of basis
vectors ($\mathbf{G}$) in which each of them is tagged to a fragment but is
allowed to be spanned by any AO basis function, it defines the working basis of
the SCF-MI problem. Then, within this basis, the locally projected SCF equations
can be solved in a similar way, with the constraint that the MO coefficient
matrix in the working basis ($\mathbf{G}$) is fragment-block-diagonal, while
the MO coefficient matrix in the AO basis does not necessarily retain the
blocking structure. The basis vectors in $\mathbf{G}$ can be either
non-orthogonal or orthogonal between fragments. More details on the generalized
SCF-MI equations are available in Ref. [[593]](../bib_references/bib.md#bib617)
.

This generalized SCF-MI scheme is implemented in GEN_SCFMAN (the original
AO-block based scheme is available in GEN_SCFMAN as well). It is used for
the variational optimization of the polarized (but CT-forbidden) intermediate
state in “EDA2” (see Section [12.6.3](sect_ferf.md)). Another preferable feature of
this generalized scheme is that the interfragment linear dependency in
$\mathbf{G}$ can be properly handled. Therefore, this scheme can be used to
replace the original AO-block based SCF-MI without becoming ill-defined when
interfragment linear dependency occurs. In contrast, the original ALMO-EDA
method that employs the AO-block based approach fails when the sum of the
number of orbitals on each fragment is not equal to the number of orbitals for
the super-system (the latter is determined by the total number of AO basis
functions and BASIS_LIN_DEP_THRESH), which often happens when
substantially large basis sets are used or when the super-system comprises a
large number of fragments.

SCF-MI calculations based on the GEN_SCFMAN implementation are triggered by
setting GEN_SCFMAN = TRUE and FRGM_METHOD =
STOLL or GIA (the other options of FRGM_METHOD are
not allowed). A subset of supported algorithms in GEN_SCFMAN are available
for restricted (R) and unrestricted (U) SCF-MI, including DIIS, GDM, GDM_LS, and
NEWTON_CG. While the DIIS algorithm iteratively solves for the
locally-projected SCF equations, the latter two methods use the energy
derivatives with respect to the on-fragment orbital rotations to minimize the
energy until the gradient reaches zero. As for standard calculations using
GEN_SCFMAN, internal stability analysis is also available for R- and U-SCF-MI,
and one can set FD_MAT_VEC_PROD to TRUE if the analytical
Hessian is not available for the employed density functional (note: for functionals
containing non-local correlation, one can always use FD_MAT_VEC_PROD = FALSE).

As in the original implementation, perturbative corrections can be applied on
top of the SCF-MI solution to approach the full SCF result, and this is still
controlled by FRGM_LPCORR. Note that among the options introduced in
Section [12.5.5](sect_old_almo_job.md), only ARS and RS are allowed
here since the exact SCF calculation is actually beyond the scope of SCF-MI.

In addition, with this more general implementation users are allowed to specify
some fragments to be frozen during the SCF-MI calculation, *i.e.*, intrafragment
relaxation does not occur on these fragments. This is achieved by specifying
the *$rem* variable SCFMI_FREEZE_SS. Such a calculation can be
interpreted as an active fragment being embedded in a frozen environment where
the interaction between them is treated quantum mechanically.

SCFMI_MODE

### `SCFMI_MODE`

> **Determine whether generalized SCF-MI is used and also the property of the working basis.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (“1” is used by basic “EDA2” calculations).`
> * **Options**:
>     * 0
>     * AO-block based SCF-MI (the original definition of ALMOs).
>     * 1
>     * Generalized SCF-MI with basis vectors that are non-orthogonal between fragments.
>     * 2
>     * Generalized SCF-MI with basis vectors that are orthogonal between fragments.
> * **Recommendation**: None

SCFMI_FREEZE_SS

### `SCFMI_FREEZE_SS`

> **Keep the first several fragments unrelaxed in an SCFMI calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (all fragments are active)`
> * **Options**:
>     * $n$
>     * Freeze the first
>     * $n$
>     * fragments.
> * **Recommendation**: None

???+ example "Example 12.12: Generalized SCF-MI calculation for the water dimer with single Roothaan-step
perturbative correction. For this specific case, the result is identical to
that given by AO-block based SCF-MI ( SCFMI_MODE = 0)."
    ```qchem
    $molecule
    0 1
    --
    0 1
    O  -1.551007  -0.114520   0.000000
    H  -1.934259   0.762503   0.000000
    H  -0.599677   0.040712   0.000000
    --
    0 1
    O   1.350625   0.111469   0.000000
    H   1.680398  -0.373741  -0.758561
    H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       METHOD           b3lyp
       GEN_SCFMAN       true
       BASIS            6-31+G(d)
       GEN_SCFMAN       true
       SCF_CONVERGENCE  8
       THRESH           14
       FRGM_METHOD      stoll
       FRGM_LPCORR      rs
       SCFMI_MODE       1 !gen scfmi (non-orthogonal)
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
