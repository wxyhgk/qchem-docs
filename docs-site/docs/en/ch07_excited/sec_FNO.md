---
title: "7.9.14 Frozen Natural Orbitals in CC, IP-CC, and SF-CC Calculations"
---

## 7.9.14 Frozen Natural Orbitals in CC, IP-CC, and SF-CC Calculations

(July 4, 2026)

Large computational savings are possible if the virtual space is truncated
using the frozen natural orbital (FNO) approach (see Section [6.15.1](../ch06_correlation/sec_FNOCC.md)).
An extension of the FNO approach to ionized states within the EOM-CC formalism has
also been introduced and benchmarked.[[748]](../bib_references/bib.md#bib781)
 In addition to
ground-state coupled-cluster calculations, FNOs can also be used in
EOM-IP-CCSD, EOM-IP-CCSD(dT/fT), and EOM-IP-CC(2,3). In EOM-IP-CC the FNOs are
computed for the reference (neutral) state and then are used to describe
several target (ionized) states of interest. Different truncation scheme are
described in Section [6.15.1](../ch06_correlation/sec_FNOCC.md).

To reduce the cost of EOM-SF-CCSD calculations, a special variant of
FNO—open-shell frozen natural orbital approximation (OSFNO)—has been introduced.[[1104]](../bib_references/bib.md#bib1153)

This approach is a two-step scheme.
First, the open-shell orbitals of the reference are found by singular value decomposition of the overlap matrix of alpha occupied and beta virtual orbitals.
These orbitals contain the main amplitudes of the EOM-SF wave functions.
Then, after separation of the open-shell orbitals, the rest of the virtual space is transformed through singular value decomposition of the singlet part of the MP2 density matrix (in alpha-beta spin orbital pairs).
Benchmarks in Ref. [[1104]](../bib_references/bib.md#bib1153)
 show that this scheme achieves speedups similar to FNO, while introducing very small errors to the relative energies of both covalent and ionic EOM-SF states.
In particular, the errors in singlet–triplet gaps for single molecule magnets are less than 18 cm${}^{-1}$ for a typical OSFNO truncation at 99% of total population.
Properties also show small errors.
OSFNO is activated with CC_OSFNO = TRUE rem variable.
CC_FNO_THRESH and CC_FNO_USEPOP keywords have the same usage as in conventional FNO.

Because of the limitation of the implementation, point-group symmetry cannot be used with FNO/OSFNO and is disabled.
Please, adjust your input consistently with CC_SYMMETRY = FALSE.

OSFNO can be combined with orbital localization to produce effective Hamiltonians,
as described in the Section [13.6](../ch13_specialized/sec_EffHam.md).

CC_OSFNO

### `CC_OSFNO`

> **Activation of OSFNO. Available only for open-shell references.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * activate
> * **Recommendation**: Use for EOM-SF-CCSD calculations from open-shell references. Available in CCMAN2 only.

???+ example "Example 7.91: An EOM-SF-CCSD job, illustrating usage of OSFNO for energies and properties."
    ```qchem
    $molecule
       0 3
       C
       H 1 rCH
       H 1 rCH 2 aHCH
    
       rCH = 1.0775
       aHCH = 133.29
    $end
    
    $rem
       METHOD           eom-ccsd
       BASIS            cc-PVTZ
       SF_STATES        [4]
       CC_SYMMETRY      false
       CC_EOM_PROP      1
       CC_EOM_PROP_TE   1
       CC_OSFNO         true
       CC_FNO_THRESH    9900
    $end
    ```
