---
title: "4.8.3 Examples"
---

## 4.8.3 Examples

(July 4, 2026)

???+ example "Example 4.27: Input for a HFPC single-point calculation."
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       EXCHANGE     hf
       BASIS        cc-pVDZ  ! primary basis
       HFPT_BASIS   cc-pVQZ  ! secondary basis
       PURECART     1111     ! set to purecart of the target basis
       HFPT         true
       GEN_SCFMAN   false    ! runs in the old SCF code
    $end
    ```

???+ example "Example 4.28: Input for a DFPC single-point calculation."
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       METHOD           blyp               ! primary functional
       DFPT_EXCHANGE    b3lyp              ! secondary functional
       DFPT_XC_GRID     00075000302        ! secondary grid
       XC_GRID          0                  ! primary grid
       HFPT_BASIS       6-311++G(3df,3pd)  ! secondary basis
       BASIS            6-311G*            ! primary basis
       PURECART         1111
       HFPT             true
       GEN_SCFMAN       false
    $end
    ```
