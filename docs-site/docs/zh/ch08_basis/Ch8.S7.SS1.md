---
title: "8.7.1 Overview"
---

## 8.7.1 Overview

(July 4, 2026)

Complex basis function (CBF) methods for describing meta-stable electronic states (see Section [4.9.5](../ch04_scf/sec_cbfscf.md)) require the user to specify a basis set in which the most diffuse functions have a complex-scaled exponent. The real-valued basis functions are specified using the standard *$rem* keyword BASIS. The complex basis set is specified using the *$rem* keyword COMPLEX_BASIS, and it should be a superset of the real basis.
If the basis is specified as general or mixed, the user-defined basis should be entered in an an additional *$zbasis* input section in the same format as the *$basis* section.

**Q-Chem** will automatically determine the additional basis functions in the complex basis and scales the exponents of those functions. For example, if BASIS is specified as “cc-pVTZ” and COMPLEX_BASIS is specified as “aug-cc-pVTZ”, the augmenting functions will have complex-scaled exponents.
An alternative way to specify the scaled functions is the scaling variable in the *$complex_ccman* section. If a scaling independent of the BASIS is desired, this variable accepts a comma-separated list of the indices of the shells to be scaled. This requires the COMPLEX_CCMAN variable to be set to 1 so that the scaling string is recognized. The indices are referring to the order in which they appear in the basis set file or respectively, in the *$zbasis* section. Furthermore, in the case of multiple centers, basis functions on different centers are enumerated separately, in the order as the centers are listed in the *$molecule* section, which allows different scaling of basis functions even when centered at atoms of the same type. As an example, in a calculation with two atoms which each possess 10 shells, the shells of the first atom would be given the indices 1–10 and the shells of the second atom 11–20. The following *$complex_ccman* section is an example for this, in which the scaling of shells 5, 6, 15 and 16 is requested.

> ```qchem
> $rem
> ...
> complex_ccman 1
> ...
> $end
> 
> $complex_ccman
>    CS_THETA  0
>    CS_ALPHA  1000
>    scaling 5,6,15,16
> $end
> ```

The scaling is done according to

<a id="Ch8.E1"></a>
$$
\alpha\rightarrow\alpha e^{-2i\theta} \tag{8.1}
$$

where $\alpha$ is the exponent of a particular basis function and $\theta$ is specified by the *$rem* keyword COMPLEX_THETA.

COMPLEX_BASIS

### `COMPLEX_BASIS`

> **Defines the complex basis.**
>
> * **Type**: `STRING`
> * **Default**: `No default complex basis set`
> * **Options**:
>     * Symbol
>     * Use a standard basis set
>     * ZBASIS_GENERAL, ZBASIS_GEN
>     * User-defined. As for
>     * BASIS
>     * ZBASIS_MIXED
>     * User-defined mixed basis
> * **Recommendation**: Consult Ref. 1457 White A. F., Head-Gordon M., McCurdy C. W. J. Chem. Phys. (2015) , 142 , pp. 054103 . Link and the Basis Set Exchange.

COMPLEX_THETA

### `COMPLEX_THETA`

> **Sets the value of $\theta$ in degrees for a calculation with complex basis functions.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * $\theta=n/10$
>     * (degrees)
> * **Recommendation**: Consult Ref. 1457 White A. F., Head-Gordon M., McCurdy C. W. J. Chem. Phys. (2015) , 142 , pp. 054103 . Link . Usually calculations at several different values of $\theta$ (a “ $\theta$ -trajectory”) should be performed.
