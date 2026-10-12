---
title: "4.6.4 Incremental and Variable Thresh Fock Matrix Building"
---

## 4.6.4 Incremental and Variable Thresh Fock Matrix Building

(July 4, 2026)

The use of a variable integral threshold, operating for the first few cycles of
an SCF, is justifiable on the basis that the MO coefficients are usually of
poor quality in these cycles. In **Q-Chem**, the integrals in the first iteration
are calculated at a threshold of $10^{-6}$ (for an anticipated final integral
threshold greater than, or equal to $10^{-6}$) to ensure the error in the first
iteration is solely sourced from the poor MO guess. Following this, the
integral threshold used is computed as

<a id="eq441"></a>

$$
t=10^{-\mathrm{VARTHRESH}}\times(\text{DIIS error}) \tag{4.48}
$$

where the DIIS error is that calculated from the previous cycle, VARTHRESH
is the variable threshold set by the program (by default) and $t$ is
the temporary threshold used for integral evaluation. Each cycle requires
recalculation of all integrals. The variable integral threshold procedure has
the greatest impact in early SCF cycles.

In an incremental Fock matrix build,[[41]](../bib_references/bib.md#bib25)
$\mathbf{F}$ is computed recursively as

<a id="eq442"></a>

$$
{\rm{\bf F}}^{\rm{\bf m}}={\rm{\bf F}}^{{\rm{\bf m}}-{\rm{\bf 1}}}+\Delta{\rm{\bf J}}^{{\rm{\bf m}}-{\rm{\bf 1}}}-\frac{1}{2}\Delta{\rm{\bf K}}^{{\rm{\bf m}}-{\rm{\bf 1}}} \tag{4.49}
$$

where $m$ is the SCF cycle, and $\Delta$**J${}^{m}$** and $\Delta$**K${}^{m}$** are computed using the difference density

<a id="eq443"></a>

$$
\Delta{\rm{\bf P}}^{\rm{\bf m}}={\rm{\bf P}}^{\rm{\bf m}}-{\rm{\bf P}}^{{\rm{\bf m}}-{\rm{\bf 1}}} \tag{4.50}
$$

Using Schwartz integrals and elements of the difference density, **Q-Chem** is
able to determine at each iteration which ERIs are required, and if necessary,
recalculated. As the SCF nears convergence, $\Delta\mathbf{P}^{m}$ becomes sparse and
the number of ERIs that need to be recalculated declines dramatically, saving
the user large amounts of computational time.

Incremental Fock matrix builds and variable thresholds are only used when the
SCF is carried out using the direct SCF algorithm and are clearly complementary
algorithms. These options are controlled by the following input parameters,
which are only used with direct SCF calculations.

### `INCFOCK`

> **Iteration number after which the incremental Fock matrix algorithm is initiated**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * User-defined (0 switches INCFOCK off)
> * **Recommendation**: May be necessary to allow several iterations before switching on INCFOCK.

### `RESET_INCFOCK`

> **Iteration number after which the incremental Fock matrix algorithm is reset**
>
> * **Type**: `INTEGER`
> * **Default**: `15`
> * **Options**:
>     * User-defined (0 switches RESET_INCFOCK off)
### `VARTHRESH`

> **Controls the temporary integral cut-off threshold, $t=10^{-\mathrm{VARTHRESH}}\times(\text{DIIS error})$**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined threshold
> * **Recommendation**: 3 has been found to be a practical level, and can slightly speed up SCF evaluation.

???+ example "Example 4.20: Q-Chem input for a large single point energy calculation. This would be
appropriate for a medium-sized molecule, but for truly large calculations, the
CFMM and LinK algorithms are far more efficient."
    ```qchem
    $comment
       HF/3-21G single point calculation on a large molecule
       read in the molecular coordinates from file
    $end
    
    $molecule
       read base_pair.inp
    $end
    
    $rem
       METHOD          HF      Hartree-Fock
       BASIS           3-21G   Basis set
       INCFOCK         5       Incremental Fock after 5 cycles
       VARTHRESH       3       1.0d-03 variable threshold
       MAX_SCF_CYCLES  100
    $end
    ```
