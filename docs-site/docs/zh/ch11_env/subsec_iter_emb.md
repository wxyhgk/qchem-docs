---
title: "11.6.4 Iterative Approach for Supermolecular Properties"
---

## 11.6.4 Iterative Approach for Supermolecular Properties

(July 4, 2026)

The iterative embedding method is a useful approach for the computation of supermolecular
properties.[[383]](../bib_references/bib.md#bib391)
 The keyword for requesting an iterative embedding calculation is EMB_ITER.
In this approach, different parts of a system are chosen as active fragment in subsequent embedding calculations.
The property is then expressed as the sum of contributions from the individual fragments.
The high-level calculation must be repeated for each fragment, but this is computationally cheaper
than treating the entire system at once.

It is possible to compute supermolecular static polarizabilities using the iterative embedding method. Within this approach,
an element $\alpha_{xy}$ of the polarizability tensor $\mathbb{\alpha}$ is computed as

<a id="Ch11.E118"></a>
$$
\alpha_{xy}=\sum_{A}{(\alpha_{xy})_{A}} \tag{11.118}
$$

where the sum over active fragments A includes the entire system.
This method can also be used to compute supermolecular dipole moments. A component $\mu_{x}$ of the dipole moment vector
$\mathbb{\mu}$ is obtained as

<a id="Ch11.E119"></a>
$$
\mu_{x}=\sum_{A}{(\mu_{x})_{A}} \tag{11.119}
$$

The keywords for triggering these features are EMB_POL and EMB_DIPOLE, respectively.

EMB_ITER

### `EMB_ITER`

> **Turns iterative projection-based density embedding on**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not iterate over different fragments.
>     * TRUE
>     * Turn on iterative density embedding.
> * **Recommendation**: None

EMB_POL

### `EMB_POL`

> **Triggers the computation of the iterative polarizability tensor**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not compute the iterative polarizability tensor
>     * TRUE
>     * Compute the iterative polarizability tensor
> * **Recommendation**: None

EMB_DIPOLE

### `EMB_DIPOLE`

> **Triggers the computation of the iterative dipole moment**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not compute the iterative dipole moment
>     * TRUE
>     * Compute the iterative dipole moment
> * **Recommendation**: None
