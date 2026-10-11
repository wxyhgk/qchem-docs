---
title: "6.13.5 Examples"
---

## 6.13.5 Examples

(July 4, 2026)

???+ example "Example 6.43: Two jobs that compare the correlation energy calculated via the standard
CCSD(T) method with the new CCSD(2) approximation, both using the frozen core
approximation. This requires that CC_INCL_CORE_CORR must be
specified as FALSE in the CCSD(2) input."
    ```qchem
    $molecule
       0  2
       O
       H  O  0.97907
    $end
    
    $rem
       METHOD          ccsd(t)
       BASIS           cc-pvtz
       N_FROZEN_CORE   fc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD              ccsd(2)
       BASIS               cc-pvtz
       N_FROZEN_CORE       fc
       CC_INCL_CORE_CORR   false
    $end
    ```

???+ example "Example 6.44: Using libpt for a standard CCSD(T) calculation"
    ```qchem
    $molecule
       0  2
       O
       H  O  0.97907
    $end
    
    $rem
       METHOD          ccsd(t)
       BASIS           cc-pvtz
       N_FROZEN_CORE   fc
       USE_LIBPT       true
    $end
    ```
