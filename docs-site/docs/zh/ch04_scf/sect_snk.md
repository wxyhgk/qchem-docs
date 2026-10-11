---
title: "4.6.9 Seminumerical Exchange (SNK) Matrix Evaluation"
---

## 4.6.9 Seminumerical Exchange (SNK) Matrix Evaluation

(July 4, 2026)

Seminumerical exchange (SNK) is an alternative method for evaluation
of the exchange matrix. SNK is particularly efficient for large systems and
basis sets due to its formal ${\cal{O}}({N^{3}})$ scaling with system size and
${\cal{O}}({N_{\text{basis}}^{2}})$ scaling with basis set size. In addition, asymptotic
linear scaling is possible for sparse systems. In SNK, the two-electron
integrals are decomposed by means of numerical quadrature; one integration
is performed on a grid:

<a id="A3.S8.EGx10"></a>
$$
\displaystyle(\mu\sigma|\nu\lambda)=\sum_{g}w_{g}\chi_{\mu}(\mathbf{r}_{g})(\nu\lambda|g)\chi_{\sigma}(\mathbf{r}_{g}) \tag{4.59}
$$

while the second integration

<a id="A3.S8.EGx11"></a>
$$
\displaystyle(\nu\lambda|g)=\int d\mathbf{r}\frac{\chi_{\nu}(\mathbf{r})\chi_{\lambda}(\mathbf{r})}{|\mathbf{r}-\mathbf{r}_{g}|} \tag{4.60}
$$

is evaluated analytically (3c-1e). The exchange matrix is computed in three steps:

<a id="A3.S8.EGx12"></a>
$$
\displaystyle F_{\lambda g} \tag{4.61}
$$

With integral screening, the number of required 3c-1e integrals can be
dramatically reduced. **Q-Chem** performs this screening based on contributions of
a given shellpair on a given batch of grid points to both the exchange energy and the
exchange matrix, defining two thresholds $\theta_{E}$ and $\theta_{K}$.[[769]](../bib_references/bib.md#bib801)

Further speedups are attained by evaluating those integrals which are less significant
but non-negligible in single precision (fp32),[[768]](../bib_references/bib.md#bib802)
 defining a second
set of thresholds $\theta_{E}^{\text{fp32}}$ and $\theta_{K}^{\text{fp32}}$. These thresholds are
related to $\theta_{E}$ and $\theta_{K}$ by a multiplier $\theta_{i}^{\text{fp32}}=M^{\text{fp32}}\theta_{i}$.
Additionally, basis functions which are not significant for a given batch of grid points
may also be screened by a threshold $\theta_{B}$.

SNK is particularly efficient on hardware supporting OpenMP parallelism and single-instruction-multiple-data vector instructions.

SNK is currently available for HF exchange, global hybrids, and range-separated hybrids. SNK
may be invoked by setting SNK to be 1. The grid and thresholds may also be set via
the rem variables discussed below.

SNK

### `SNK`

> **Controls the use of seminumerical exchange in the construction of the exchange matrix.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Use SNK.
> * **Recommendation**: Use for large systems/basis sets.

SNK_GRID

### `SNK_GRID`

> **Specifies the type of grid to use for SNK.**
>
> * **Type**: `INTEGER`
> * **Default**: `Use SG-1; Use DFT grid (`
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
>     * is the number of angular points, where possible numbers of Lebedev angular
>     * points must be allowed values from Table
>     * 5.2
>     * in
>     * Section
>     * 5.5
>     * .
> * **Recommendation**: Use the default unless numerical integration problems arise or grid errors become unacceptable. Note that Gauss-Legendre grids ( $-XY$ ) are not available for SNK.

SNK_BATCH_SIZE

### `SNK_BATCH_SIZE`

> **Specifies the target grid batch size to use for SNK.**
>
> * **Type**: `INTEGER`
> * **Default**: `128`
> * **Options**:
>     * $n$
>     * Use grid batch sizes of
>     * $n$
>     * grid points.
> * **Recommendation**: Use the default. Larger batch sizes may lead to poorer screening.

SNK_THRESH_B

### `SNK_THRESH_B`

> **Cutoff for neglect of basis functions on a given grid batch, defined via a threshold of $10^{-\mbox{{\small SNK\_THRESH\_B}}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `14`
> * **Options**:
>     * $n$
>     * for a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default unless higher accuracy (increase) or better performance (decrease) is desired.

SNK_THRESH_E

### `SNK_THRESH_E`

> **Cutoff for neglect of integral contributions to the exchange energy, defined via a threshold of $10^{-\mbox{{\small SNK\_THRESH\_E}}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$
>     * for a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default unless higher accuracy (increase) or better performance (decrease) is desired.

SNK_THRESH_K

### `SNK_THRESH_K`

> **Cutoff for neglect of integral contributions to the exchange matrix, defined via a threshold of $10^{-\mbox{{\small SNK\_THRESH\_K}}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$
>     * for a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default unless higher accuracy (increase) or better performance (decrease) is desired.

SNK_THRESH_FP32_M

### `SNK_THRESH_FP32_M`

> **Multiplies SNK_THRESH_E and SNK_THRESH_K to determine cutoffs for evaluating integrals in single precision (fp32), defined via a factor of $10^{\mbox{{\small SNK\_THRESH\_FP32\_M}}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$
>     * for a factor of
>     * $10^{n}$
>     * .
> * **Recommendation**: For most systems, the default gives appreciable speedups with insignificant losses to accuracy. In some rare cases, the use of mixed precision may result in infs/nans due to fp32 overflow. In this case, mixed precision integrals may be disabled with $\mbox{{\small SNK\_THRESH\_FP32\_M}}=0$ . Note that if an inf/nan is detected in the SNK exchange energy, the SCF will proceed with mixed precision disabled.

SNK_PRINT_TIMING

### `SNK_PRINT_TIMING`

> **Print the time required for one SNK exchange build for each SCF cycle.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Print timing information.
> * **Recommendation**: No recommendation.

???+ example "Example 4.22: Q-Chem input for an energy calculation with $\omega$ B97M-V/SNK."
    ```qchem
    $molecule
    0 1
    O 0.0000000000  0.0000000000  0.21981483259
    H 0.0000000000  1.4194772274 -0.87926122007
    H 0.0000000000 -1.4194772274 -0.87926122007
    $end
    
    $rem
    input_bohr = true
    jobtype = sp
    method = wB97M-V
    basis = cc-pvtz
    scf_convergence = 8
    
    snk 1
    snk_batch_size 256
    snk_thresh_b 12
    snk_thresh_e 10
    snk_thresh_k 7
    snk_thresh_fp32_m 5
    
    $end
    ```
