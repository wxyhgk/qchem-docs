---
title: "5.7.2 Non-Local Correlation (NLC) Functionals"
---

## 5.7.2 Non-Local Correlation (NLC) Functionals

(July 4, 2026)

From the standpoint of the electron density, the vdW interaction is a non-local
one: even for two non-overlapping, spherically-symmetric charge densities (two
argon atoms, say), the presence of molecule B in the non-covalent A$\cdots$B
complex induces ripples in the tail of A’s charge distribution, which are the
hallmarks of non-covalent interactions.[[265]](../bib_references/bib.md#bib266)
 (This is
the fundamental idea behind the non-covalent interaction plots described in
Section [10.5.6](../ch10_properties/NCI-plots.md); the vdW interaction manifests as large density
gradients in regions of space where the density itself is small.) Semi-local
GGAs that depend only on the density and its gradient cannot describe this
long-range, correlation-induced interaction, and meta-GGAs at best describe it
at middle-range via the Laplacian of the density and/or the kinetic
energy density. A proper description of *long-range* electron correlation
requires a non-local functional, *i.e.*, an exchange-correlation potential having the form

<a id="Ch5.E23"></a>

$$
v_{\rm c}^{\rm nl}(\mathbf{r})=\int f(\mathbf{r},\mathbf{r^{\prime}})\,d\mathbf{r^{\prime}}\;. \tag{5.23}
$$

In this way, a perturbation at a point $\mathbf{r^{\prime}}$ (due to B, say) then
induces an exchange-correlation potential at a (possibly far-removed) point
$\mathbf{r}$ (on A).

**Q-Chem** includes four such functionals that can describe dispersion interactions:

- •

vdW-DF-04, developed by Langreth, Lundqvist, and
coworkers,[[327]](../bib_references/bib.md#bib331)
 implemented as described in
Ref. [[1417]](../bib_references/bib.md#bib1474)
.
- •

vdW-DF-10 (also known as vdW-DF2), which is a
re-parameterization of vdW-DF-04.[[786]](../bib_references/bib.md#bib822)
- •

VV09, developed[[1414]](../bib_references/bib.md#bib1475)
 and implemented[[1415]](../bib_references/bib.md#bib1476)

by Vydrov and Van Voorhis.
- •

VV10 by Vydrov and Van Voorhis.[[1416]](../bib_references/bib.md#bib1477)
- •

rVV10 by Sabatini and coworkers.[[1192]](../bib_references/bib.md#bib1247)

Each of these functionals is implemented in a self-consistent manner, and
analytic gradients with respect to nuclear displacements are
available.[[1417]](../bib_references/bib.md#bib1474)
 The non-local
correlation is governed by the *$rem* variable NL_CORRELATION, which
can be set to one of the four values: vdW-DF-04, vdW-DF-10,
VV09, or VV10. The vdW-DF-04, vdW-DF-10, and VV09
functionals are used in combination with LSDA correlation, which must be
specified explicitly. For instance, vdW-DF-10 is invoked by the following
keyword combination:

> ```qchem
> $rem
>    CORRELATION        PW92
>    NL_CORRELATION     vdW-DF-10
>    ...
> $end
> ```

VV10 is used in combination with PBE correlation, which must be added
explicitly. In addition, the values of two parameters, $C$ and $b$ (see
Ref. [[1417]](../bib_references/bib.md#bib1474)
), must be specified for VV10. These parameters
are controlled by the *$rem* variables NL_VV_C and
NL_VV_B, respectively. For instance, to invoke VV10 with
$C=0.0093$ and $b=5.9$, the following input is used:

> ```qchem
> $rem
>    CORRELATION        PBE
>    NL_CORRELATION     VV10
>    NL_VV_C            93
>    NL_VV_B            590
>    ...
> $end
> ```

The variable NL_VV_C may also be specified for VV09, where it has
the same meaning. By default, $C=0.0089$ is used in VV09 (*i.e.*
NL_VV_C is set to 89). However, in VV10 neither $C$ nor $b$
are assigned a default value and must always be provided in the input.

Unlike local (LSDA) and semi-local (GGA and meta-GGA) functionals, for
non-local functionals evaluation of the correlation energy requires a double
integral over the spatial variables, as compared to the single integral [Eq. ([5.8](sec_Kohn-Sham.md#E_XC))]
required for semi-local functionals:

<a id="Ch5.E24"></a>

$$
E_{\rm c}^{\rm nl}=\int v_{\rm c}^{\rm nl}(\mathbf{r})\;d\mathbf{r}=\int f(\mathbf{r},\mathbf{r^{\prime}})\,\rho(\mathbf{r})\;d\mathbf{r}\;d\mathbf{r^{\prime}}. \tag{5.24}
$$

In practice, this double integration is performed numerically on a quadrature
grid.[[1417]](../bib_references/bib.md#bib1474)
 By default, the SG-1
quadrature (described in Section [5.5.3](sect_standard-quad.md) below) is used to
evaluate $E_{\rm c}^{\rm nl}$, but a different grid can be requested via the
*$rem* variable NL_GRID. The non-local energy is rather insensitive
to the fineness of the grid such that SG-1 or even SG-0 grids can be
used in most cases, but a finer grid may be required to integrate other
components of the functional. This is controlled by the XC_GRID
variable discussed in Section [5.5.3](sect_standard-quad.md).

The two functionals originally developed by Vydrov and Van Voorhis can be
requested by specifying METHOD = VV10 or METHOD
LC-VV10. In addition, the combinatorially-optimized functionals of
Mardirossian and Head-Gordon ($\omega$B97X-V, B97M-V, and $\omega$B97M-V) make
use of non-local correlation and can be invoked by setting METHOD to
wB97X-V, B97M-V, or wB97M-V. Now, the VV10 codes
have been rewrited and the feature of NMR chemical shielding and analytical
second derivative are added. If you want to use the old codes, please set
USE_LIBNLQ to false.

???+ example "Example 5.12: Geometry optimization of the methane dimer using VV10 with rPW86 exchange."
    ```qchem
    $molecule
       0 1
       C   0.000000  -0.000140   1.859161
       H  -0.888551   0.513060   1.494685
       H   0.888551   0.513060   1.494685
       H   0.000000  -1.026339   1.494868
       H   0.000000   0.000089   2.948284
       C   0.000000   0.000140  -1.859161
       H   0.000000  -0.000089  -2.948284
       H  -0.888551  -0.513060  -1.494685
       H   0.888551  -0.513060  -1.494685
       H   0.000000   1.026339  -1.494868
    $end
    
    $rem
       JOBTYPE            opt
       BASIS              aug-cc-pVTZ
       EXCHANGE           rPW86
       CORRELATION        PBE
       XC_GRID            2
       NL_CORRELATION     VV10
       NL_GRID            1
       NL_VV_C            93
       NL_VV_B            590
    $end
    ```

In the above example, the SG-2 grid is used to evaluate the rPW86 exchange
and PBE correlation, but a coarser SG-1 grid is used for the
non-local part of VV10. Furthermore, the above example is identical to
specifying METHOD = VV10.

### `NL_CORRELATION`

> **Specifies a non-local correlation functional that includes non-empirical dispersion.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `None`: No non-local correlation
>     * `vdW-DF-04`: the non-local part of vdW-DF-04
>     * `vdW-DF-10`: the non-local part of vdW-DF-10 (also known as vdW-DF2)
>     * `VV09`: the non-local part of VV09
>     * `VV10`: the non-local part of VV10
> * **Recommendation**: Do not forget to add the LSDA correlation (PW92 is recommended) when using vdW-DF-04, vdW-DF-10, or VV09. VV10 should be used with PBE correlation. Choose exchange functionals carefully: HF, rPW86, revPBE, and some of the LRC exchange functionals are among the recommended choices.

### `NL_VV_C`

> **Sets the parameter $C$ in VV09 and VV10. This parameter is fitted to asymptotic van der Waals $C_{6}$ coefficients.**
>
> * **Type**: `INTEGER`
> * **Default**: `89`
> * **Options**:
>     * $n$: Corresponding to $C=n/10000$
> * **Recommendation**: $C=0.0093$ is recommended when a semi-local exchange functional is used. $C=0.0089$ is recommended when a long-range corrected (LRC) hybrid functional is used. For further details see Ref. 1416 Vydrov O. A., Van Voorhis T. J. Chem. Phys. (2010) , 133 , pp. 244103 . Link .

### `NL_VV_B`

> **Sets the parameter $b$ in VV10. This parameter controls the short range behavior of the non-local correlation energy.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$: Corresponding to $b=n/100$
> * **Recommendation**: The optimal value depends strongly on the exchange functional used. $b=5.9$ is recommended for rPW86. For further details see Ref. 1416 Vydrov O. A., Van Voorhis T. J. Chem. Phys. (2010) , 133 , pp. 244103 . Link .

### `USE_RVV10`

> **Used to turn on the rVV10 NLC functional**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Use VV10 NLC (the default for NL_CORRELATION )
>     * `TRUE`: Use rVV10 NLC
> * **Recommendation**: Set to TRUE if the rVV10 NLC is desired.

### `USE_LIBNLQ`

> **Turn on the use of LIBNLQ for calculating nonlocal correlation funcitonal.**
>
> * **Type**: `LOGICAL`
> * **Default**: `True`
> * **Options**:
>     * `False`
>     * `True`
> * **Recommendation**: Use the default
