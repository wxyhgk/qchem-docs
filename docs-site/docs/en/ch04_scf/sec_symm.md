---
title: "4.3.5 Symmetry"
---

## 4.3.5 Symmetry

(July 4, 2026)

Symmetry is a powerful branch of mathematics and is often exploited in quantum
chemistry, both to reduce the computational workload and to classify the final
results obtained.[[1338]](../bib_references/bib.md#bib1397)
**Q-Chem** is able
to determine the point group symmetry of the molecular nuclei and, on
completion of the SCF procedure, classify the symmetry of molecular orbitals,
and provide symmetry decomposition of kinetic and nuclear attraction energy
(see Chapter [10](../ch10_properties/chap_properties.md)).

Molecular systems possessing point group symmetry offer the possibility of
large savings of computational time, by avoiding calculations of integrals
which are equivalent *i.e.*, those integrals which can be mapped on to one
another under one of the symmetry operations of the molecular point group. The
**Q-Chem** default is to use symmetry to reduce computational time, when possible.

There are several keywords that are related to symmetry, which causes frequent
confusion. POINT_GROUP_SYMMETRY controls symmetry throughout all modules. The
default is TRUE. In some cases it may be desirable to turn off
symmetry altogether, for example if you do not want **Q-Chem** to reorient the
molecule into the standard nuclear orientation, or if you want to turn it off
for finite difference calculations. If the POINT_GROUP_SYMMETRY keyword is set
to FALSE then the coordinates will not be altered from the input, and
the point group will be set to $C_{1}$.

The INTEGRAL_SYMMETRY keyword controls symmetry in some integral routines. It
is set to TRUE by default. Note that setting it to FALSE
does not turn point group symmetry off, and does not disable symmetry in the
coupled-cluster suite (CCMAN and CCMAN2), which is controlled by
CC_SYMMETRY (see Chapters [6](../ch06_correlation/chap_correlation.md) and
[7](../ch07_excited/chap_excited.md)), although we noticed that sometimes it may interfere with
the determination of orbital symmetries, possibly due to numerical noise. In
some cases, INTEGRAL_SYMMETRY = TRUE can cause problems (poor
convergence and wildly incorrect SCF energies) and turning it off can avoid
these problems.

The symmetry is turned off when ghost atoms are used because their placement
may break the symmetry of the molecular structure. However, the user can force calculation to use symmetry by FORCE_SYMMETRY_ON keyword; this is illustrated in example [7.9.9.2](../ch07_excited/sub_cvs_eom.md#ex:cvsee1).

!!! note "Note"
    The user should be aware about different conventions for defining
    symmetry elements. The arbitrariness affects, for example, $C_{2v}$ point
    group. The specific choice affects how the irreducible representations in the affected groups are
    labeled. For example, $b_{1}$ and $b_{2}$ irreducible representations in $C_{2v}$ are flipped when
    using different conventions. **Q-Chem** uses non-Mulliken symmetry convention. See
    `https://iopenshell.usc.edu/resources/howto/symmetry`
    for detailed explanations.


### `INTEGRAL_SYMMETRY`

> **Controls the efficiency through the use of point group symmetry for calculating integrals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * `TRUE`: Use symmetry when available.
>     * `FALSE`: Do not use symmetry. This is always the case for RIMP2 jobs
> * **Recommendation**: Use the default unless benchmarking. Note that symmetry usage is disabled for RIMP2, FFT, and QM/MM jobs.

### `POINT_GROUP_SYMMETRY`

> **Controls whether or not Q-Chem determines the point group of the molecule and reorients the molecule to the standard orientation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: Use the default unless you do not want the molecule to be reoriented. Note that symmetry usage is disabled for RIMP2 jobs.

### `SYM_TOL`

> **Controls the tolerance for determining point group symmetry. Differences in atom locations less than $10^{-\mathrm{SYM\_TOL}}$ are treated as zero.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * `User defined.`
> * **Recommendation**: Use the default unless the molecule has high symmetry which is not being correctly identified. Note that relaxing this tolerance too much may introduce errors into the calculation. Misidentified point group symmetry can affect rotational symmetry numbers in thermochemical calculations.

### `FORCE_SYMMETRY_ON`

> **Overrides turning off symmetry in calculations using ghost atoms.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Force symmetry.
>     * `FALSE`: Do not use symmetry.
> * **Recommendation**: Use the default unless you know what you are doing.
