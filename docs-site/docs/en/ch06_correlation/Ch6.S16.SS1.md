---
title: "6.16.1 Overview"
---

## 6.16.1 Overview

(July 4, 2026)

Analytic gradients are available for CCSD, OO-CCD/VOD, CCD, and QCCD/VQCCD
methods for both closed- and open-shell references (UHF and RHF only),
including frozen core and/or virtual functionality, as well as RI/Cholesky
representations of the electron-repulsion integrals.
Analytic gradients are available for CCVB-SD for only closed-shell references (RHF).
In addition, gradients for selected GVB models are available.

For the CCSD and OO-CCD wave functions, **Q-Chem** can also calculate dipole
moments, $\langle r^{2}\rangle$ (as well as $\langle x^{2}\rangle$, $\langle y^{2}\rangle$,
and $\langle z^{2}\rangle$ moments separately, which
is useful for assigning different Rydberg states, *e.g.*, $3p_{x}$ vs. $3s$,
*etc.*), and the $\langle\hat{S}^{2}\rangle$ values. Interface of the CCSD and (V)OO-CCD
codes with the NBO 5.0 package is also available. This code is closely related
to EOM-CCSD properties/gradient calculations (Section [7.9.21](../ch07_excited/sec_EOMGRAD.md)).
Solvent models available for CCSD are described in Chapter [11.2](../ch11_env/topic_solvation.md).
For CCSD, analytic calculation of g-tensors is also available (see Section [7.9.21](../ch07_excited/sec_EOMGRAD.md)).

Limitations: Gradients and fully relaxed properties for ROHF and non-HF (*e.g.*,
B3LYP or FNO) orbitals as well as RI approximation are not yet available.

**Note: 

If gradients or properties are computed with frozen core/virtual,
the algorithm will replace frozen orbitals to restricted. This will not affect
the energies, but will change the orbital numbering in the CCMAN printout.
**

### `CC_REF_PROP`

> **Whether or not the non-relaxed (expectation value) or full response (including orbital relaxation terms) one-particle CCSD properties will be calculated. The properties currently include permanent dipole moment, the second moments ( $\langle x^{2}\rangle$ , $\langle y^{2}\rangle$ , and $\langle z^{2}\rangle$ ) of the electron density along with $\langle r^{2}\rangle=\langle x^{2}\rangle+\langle y^{2}\rangle+\langle z^{2}\rangle$ . This option is incompatible with JOBTYPE = FORCE , OPT , or FREQ .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: Additional equations need to be solved ( $\lambda$ -CCSD equations) for properties with the cost approximately the same as CCSD equations. Use the default if you do not need properties. The cost of the properties calculation itself is low. The CCSD one-particle density can be analyzed with NBO package by specifying NBO = TRUE , = TRUE , and JOBTYPE = FORCE .

### `CC_REF_PROP_TE`

> **Request for calculation of non-relaxed two-particle CCSD properties. The two-particle properties currently include $\langle\hat{S}^{2}\rangle$ . The one-particle properties also will be calculated, since the additional cost of the one-particle properties calculation is small compared to the cost of $\langle\hat{S}^{2}\rangle$ . The variable CC_REF_PROP must be also set to TRUE .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: The two-particle properties are computationally expensive, since they require calculation and use of the two-particle density matrix (the cost is approximately the same as the cost of an analytic gradient calculation). Do not request the two-particle properties unless you really need them.

### `CC_FULLRESPONSE`

> **Fully relaxed properties (including orbital relaxation terms) will be computed. The variable CC_REF_PROP must be also set to TRUE .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: Not available for non UHF/RHF references and for the methods that do not have analytic gradients ( e.g. , QCISD).

???+ example "Example 6.50: CCSD geometry optimization of HHeF followed up by properties calculations"
    ```qchem
    $molecule
       0 1
       H    0.000000    0.000000   -1.886789
       He   0.000000    0.000000   -1.093834
       F    0.000000    0.000000    0.333122
    $end
    
    $rem
       JOBTYPE                     OPT
       METHOD                      CCSD
       BASIS                       aug-cc-pVDZ
       GEOM_OPT_TOL_GRADIENT       1
       GEOM_OPT_TOL_DISPLACEMENT   1
       GEOM_OPT_TOL_ENERGY         1
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           SP
       METHOD            CCSD
       BASIS             aug-cc-pVDZ
       SCF_GUESS         READ
       CC_REF_PROP       1
       CC_FULLRESPONSE   1
    $end
    ```
