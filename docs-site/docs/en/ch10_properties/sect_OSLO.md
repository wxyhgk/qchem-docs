---
title: "10.2.7 Oxidation State Localized Orbitals"
---

## 10.2.7 Oxidation State Localized Orbitals

(July 4, 2026)

Oxidation State Localized Orbitals (OSLO) is a new localization scheme focused
on molecular fragments for the purposes of oxidation state assignment.
[[455]](../bib_references/bib.md#bib468)
 The method has been developed to avoid some pitfalls
encountered in the LOBA method ([10.2.6](sect_LOBA.md)) where the Pipek-Mezey orbitals
can spread across many fragments without reaching the 60%
threshold[[456]](../bib_references/bib.md#bib467)
. OSLO starts by looking at fragments’ centers of
charge and localizing on the radial spread (in the real space) to those centers.
Then, it admits orbitals to its list of orbitals if they are above a slowly
increasing threshold of a criterion called the
*fragment orbital localization index* (FOLI). To understand this criterion,
one needs to know Pipek’s delocalization measure. This is defined as

<a id="pipek-deloc"></a>

$$
d_{i}=\left[\sum_{A}(N_{A}^{i})^{2}\right]^{-1} \tag{10.20}
$$

where the $N_{A}^{i}$ is the population of the $i$th orbital on center $A$ and the
summation runs over all centers. When an orbital is entirely localized on a
given center, its delocalization measure is $d_{i}=1$. If the orbital is perfectly
delocalized among two centers $A$ and $B$ then $N_{A}=N_{B}=1/2$ and the
delocalization measure is $d_{i}=2$, etc. The square helps make it less sensitive
to the ratio of the population to each other (insensitive to bond polarization)
compared to how many are related. In fact, minimizing the sum over all occupied
orbitals is precisely what leads to the Pipek-Mezey localization procedure.
[[1093]](../bib_references/bib.md#bib1138)
 However, for our purposes, out of the localized orbitals
generated from fragment $A$ with low delocalization measure, we are interested
in those that are also highly localized on fragment $A$. Defining the
*fragment orbital localization index* (FOLI),

<a id="foli"></a>

$$
d_{i}^{A}=\left(\frac{d_{i}}{N_{A}}\right)^{1/2}\;, \tag{10.21}
$$

it is easy to see $d_{i}^{A}$ tends to unity for fragment $A$ when orbital $i$ is
perfectly localized on $A$ ($d_{i}=N_{A}=1$), tends to 2 when the localized orbital
is perfectly delocalized over two fragments ($d_{i}=2,N_{A}=0.5$), and
gradually increases as the orbital becomes more delocalized as well as less
centered on fragment $A$. Thus, among the redundant set of $Mn_{occ}$ localized
orbitals, one selects all orbitals above the smallest FOLI by a threshold (0.01
by default) and assigns each orbital to the originator fragment. The orbitals
are then symmetrically orthogonalized and projected out from the remaining space
of (unassigned) occupied space. In case a set of orbitals is redundant due to
symmetry in the system or simple covalency, then the orbitals are split over all
contributing fragments (originators). After the iterative process, each
molecular fragment has an associated set of localized orbitals derived from the
simplest orbital spread criterion, which in turn determines the fragment’s
formal charge or oxidation state in a natural manner.

The new method expects fragments. Otherwise, it localizes on atomic centers
instead. Although this method was developed for oxidation state, it produces a
set of localized orbitals on fragments or atoms that can be used like any other
localization method.

OSLO

### `OSLO`

> **Triggers OSLO procedure after a converged SCF**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Don’t perform OSLO
>     * 1
>     * Perform the OSLO procedure
> * **Recommendation**: None

More precise control of OSLO goes under the *$loco* input section, with keywords that are introduced below.
See the example for reference.

### `OSLO_POPANALTYPE`

> **Specifies which population analysis is used for OSLOs. INPUT SECTION: $loco**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 0
>     * Mulliken
>     * 1
>     * Lowdin
>     * 2
>     * IAOs
> * **Recommendation**: Use IAOs since they are insenstive to the basis set. When using IAOs, use AUTOSAD = TRUE in the $loco input section to use the new AUTOSAD-IAO algorithm, which uses AUTOSAD atomic densities instead of some minimal basis.

### `OSLO_THRESH`

> **Specifies the threshold for FOLI when adding new orbitals for each iteration. INPUT SECTION: $loco**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use the default, 0.01
>     * $c$
>     * Use threshold of
>     * $c$
>     * /1000
> * **Recommendation**: Use the default

### `OSLO_BRANCHING`

> **Specifies which iteration with too much overlap between its orbitals and next sets orbitals to choose the next set. The input here can be $abcdf\ldots$ , which is a binary string for which iteration (only consider those with warning prints) to branch in, e.g. , 010011, means to branch in iterations 2, 5, and 6. INPUT SECTION: $loco**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $abcd\ldots$
>     * , for each digit:
>     * 0
>     * Follow the default behavior
>     * 1
>     * Favor the next set of orbitals over the current set
> * **Recommendation**: Use the default, and only worry about this if the system involves multiple Lewis structures

???+ example "Example 10.3: An OSLO job to analyze the oxidation state (or formal charges) of the water
molecule, $\rm H_{2}O$"
    ```qchem
    $molecule
    0 1
    --
    0 2
    H  0.7493679  0.000000   0.44243272
    --
    0 3
    O  0.0000000  0.000000  -0.16535063
    --
    0 2
    H -0.7493679  0.000000   0.44243272
    $end
    
    $rem
    jobtype       sp
    method        wB97X-V
    basis         def2-TZVP
    ecp           def2-ecp
    mem_total     64000
    mem_static    4000
    scf_algorithm DIIS
    scf_convergence 9
    thresh          14
    max_scf_cycles  1000
    oslo            6
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $loco
    autosad 1
    ibo_mem 500
    print_level 0
    oslo_popanaltype 2
    $end
    ```
