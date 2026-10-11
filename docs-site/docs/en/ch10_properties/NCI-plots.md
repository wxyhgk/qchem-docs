---
title: "10.5.6 Noncovalent Interactions (NCI) Plots"
---

## 10.5.6 Noncovalent Interactions (NCI) Plots

(July 4, 2026)

Weitao Yang and co-workers[[652]](../bib_references/bib.md#bib676)
 have shown
that the reduced density gradient,

<a id="Ch10.E62"></a>

$$
s(\mathbf{r})=\left(\frac{1}{2(3\pi^{2})^{1/3}}\right)\frac{\|\hat{\bm{\nabla}}\rho(\mathbf{r})\|}{\rho(\mathbf{r})^{4/3}} \tag{10.62}
$$

provides a convenient indicator of noncovalent interactions, which are
characterized by large density gradients in regions of space where the density
itself is small, leading to very large values of $s(\mathbf{r})$. **Q-Chem** can
generate noncovalent interactions (NCI) plots of the function $s(\mathbf{r})$
in three-dimensional space. To generate these, set the
PLOT_REDUCED_DENSITY_GRAD *$rem* variable to TRUE.
(See the `nci-c8h14.in` input example in `$QC/samples` directory.)
