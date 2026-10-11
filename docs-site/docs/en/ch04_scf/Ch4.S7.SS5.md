---
title: "4.7.5 Job Control and Example"
---

## 4.7.5 Job Control and Example

(July 4, 2026)

Dual-basis calculations are controlled with the following *$rem*.
DUAL_BASIS_ENERGY turns on the dual-basis approximation. Note that
use of BASIS2 without DUAL_BASIS_ENERGY *only* uses
basis set projection to generate the initial guess and does not invoke the
dual-basis approximation (see Section [4.4.5](sect_projection.md)).
OVPROJECTION is used as the default projection mechanism for
dual-basis calculations; it is not recommended that this be changed.
Specification of SCF variables (*e.g.*, THRESH) will apply to
calculations in both basis sets.

DUAL_BASIS_ENERGY

### `DUAL_BASIS_ENERGY`

> **Activates dual-basis SCF (HF or DFT) energy correction.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * Analytic first derivative available for HF and DFT (see
>     * JOBTYPE
>     * )
>     * Can be used in conjunction with MP2 or RI-MP2
>     * See BASIS, BASIS2, BASISPROJTYPE
> * **Recommendation**: Use dual-basis to capture large-basis effects at smaller basis cost. Particularly useful with RI-MP2, in which HF often dominates. Use only proper subsets for small-basis calculation.

## 4.7.5.1 Examples

???+ example "Example 4.23: Input for a dual-basis B3LYP single-point calculation."
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       METHOD              b3lyp
       BASIS               6-31G*
       BASIS2              r64G
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "Example 4.24: Input for a dual-basis B3LYP single-point calculation with a minimal 6-4G small basis."
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           rimp2-aug-cc-pVDZ
       BASIS               aug-cc-pVDZ
       BASIS2              racc-pVDZ
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "Example 4.25: Input for a dual-basis RI-MP2 geometry optimization."
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           rimp2-aug-cc-pVDZ
       BASIS               aug-cc-pVDZ
       BASIS2              racc-pVDZ
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "Example 4.26: Input for a dual-basis RI-MP2 single-point calculation with mixed basis sets."
    ```qchem
    $molecule
       0 1
       H
       O   1   1.1
       H   2   1.1  1  104.5
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           aux_mixed
       BASIS               mixed
       BASIS2              basis2_mixed
       DUAL_BASIS_ENERGY   true
    $end
    
    $basis
     H 1
     cc-pVTZ
     ****
     O 2
     aug-cc-pVTZ
     ****
     H 3
     cc-pVTZ
     ****
    $end
    
    $basis2
     H 1
     rcc-pVTZ
     ****
     O 2
     racc-pVTZ
     ****
     H 3
     rcc-pVTZ
     ****
    $end
    
    $aux_basis
     H 1
     rimp2-cc-pVTZ
     ****
     O 2
     rimp2-aug-cc-pVTZ
     ****
     H 3
     rimp2-cc-pVTZ
     ****
    $end
    ```
