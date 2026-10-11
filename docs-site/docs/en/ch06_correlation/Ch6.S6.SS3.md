---
title: "6.6.3 OpenMP Implementation of RI-MP2"
---

## 6.6.3 OpenMP Implementation of RI-MP2

(July 4, 2026)

An OpenMP RI-MP2 energy algorithm is used by default in **Q-Chem** 4.1 onward.
This can be invoked by using CORR = PRIMP2 for older versions, but note
that in 4.01 and below, only RHF/RI-MP2 was supported. Now UHF/RI-MP2 and ROHF/RI-MP2 is supported, and the formation of the ‘B’ matrices as well as three
center integrals are parallelized. This algorithm uses the remaining memory
from the MEM_TOTAL allocation for all computation, which can
drastically reduce hard drive reads in the formation of t-amplitudes.
Since **Q-Chem** 5.2, RI-MP2 can be invoked by using method=mp2 and
proper auxiliary basis using AUX_BASIS_CORR. In case of double-hybrid,
adding AUX_BASIS_CORR will simply invoke RI-MP2.

???+ example "Example 6.5: Example of OpenMP-parallel RI-MP2 job."
    ```qchem
    $molecule
       0 1
       C1
       H1  C1    1.077260
       H2  C1    1.077260  H1  131.608240
    $end
    
    $rem
       EXCHANGE           HF
       CORRELATION        pRIMP2
       BASIS              cc-pVTZ
       AUX_BASIS          rimp2-cc-pVTZ
       PURECART           1111
       THRESH             12
       SCF_CONVERGENCE    8
       MAX_SUB_FILE_NUM   128
       INTEGRAL_SYMMETRY  false
    $end
    ```
