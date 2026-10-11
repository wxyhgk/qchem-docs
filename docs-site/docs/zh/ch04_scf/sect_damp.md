---
title: "4.5.4 Damping"
---

## 4.5.4 Damping

(July 4, 2026)

damping

Damping may be the oldest SCF acceleration scheme which was proposed by Hartree
in the early days of applying quantum mechanics to study atomic
structure.

 In this simple scheme, the density matrix (or
Fock matrix) of the current SCF iteration is linearly mixed with the density
matrix of the previous iteration to generate a damped density matrix as the
input for the next SCF iteration:

<a id="Ch4.E36"></a>
$$
P_{n}^{\text{damped}}=(1-\alpha)P_{n}+\alpha P_{n-1}, \tag{4.36}
$$

where $\alpha$ is the mixing factor with $0\leqslant\alpha\leqslant 1$.
During the SCF process, if density matrix changes drastically between
consecutive iterations (usually this happens in the early stage of the SCF
process), the total energy and occupied molecular orbitals are also strongly
fluctuating, which may lead to slow SCF convergence or even divergence. In this
scenario mixing the density (or Fock) matrix with its counterpart in the last
iteration could reduce (damp) the energy and molecular orbital fluctuation and
stabilize the SCF process. On the other hand, if the SCF process converges
smoothly and quickly, apply damping would only slow down its convergence.
Therefore damping is seldom applied solely in the full SCF process and often
invoked only in the early stage of the SCF process and turned off later.

Density matrix damping is offered as an option (the DAMP algorithm) to
handle difficult SCF cases in **Q-Chem** (RHF and UHF only). Damping is often
combined with DIIS and GDM (the DP_DIIS and DP_GDM
algorithms) in practical calculations. In order to invoke damping, the *$rem*
variable SCF_ALGORITHM should be set to DAMP,
DP_DIIS or DP_GDM. The other relevant *$rem* variables are
as the following:

NDAMP

### `NDAMP`

> **Determine the mixing coefficient. $\alpha$ = /100.**
>
> * **Type**: `INTEGER`
> * **Default**: `75`
> * **Options**:
>     * User-defined. Integers between 0 and 100.
> * **Recommendation**: Increase if strong fluctuations happen during the SCF process.

MAX_DP_CYCLES

### `MAX_DP_CYCLES`

> **The maximum number of SCF iterations with damping when SCF_ALGORITHM = DP_DIIS and DP_GDM . See also THRESH_DP_SWITCH .**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * 1
>     * Only a single SCF step with damping, and no damping for the remaining SCF steps.
>     * $n$
>     * $n$
>     * SCF iterations with damping before turning damping off.
> * **Recommendation**: Increase this number if strong fluctuation continues after damping is turned off.

THRESH_DP_SWITCH

### `THRESH_DP_SWITCH`

> **The threshold for turning off damping in SCF iterations is $10^{-\mbox{{\small THRESH\_DP\_SWITCH}}}$ when SCF_ALGORITHM is set to DP_DIIS or DP_GDM . See also MAX_DP_CYCLES .**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * User-defined.
> * **Recommendation**: None

???+ example "Example 4.8: Input for a UKS calculation of water cation using DIIS after damping in the early stage of the SCF process."
    ```qchem
    $molecule
      1 2
       O    1.9158048   -5.3106212    3.9451654
       H    2.8858048   -5.3106212    3.9451654
       H    1.5924750   -5.6945720    3.1151415
    $end
    
    $rem
       METHOD             B3LYP
       BASIS              3-21G
       SCF_ALGORITHM      DP_DIIS
       THRESH_DP_SWITCH   3
       MAX_DP_CYCLES      20
       NDAMP              50
    $end
    ```
