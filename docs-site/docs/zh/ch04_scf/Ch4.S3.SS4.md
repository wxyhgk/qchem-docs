---
title: "4.3.4 Examples"
---

## 4.3.4 Examples

(July 4, 2026)

Provided below are examples of **Q-Chem** input files to run ground state, HF
single point energy calculations.

???+ example "Example 4.2: Example Q-Chem input for a single point energy calculation on water. Note
that the declaration of the single point $rem variable is redundant because
it is the same as the Q-Chem default."
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   1.2
       hoh = 120.0
    $end
    
    $rem
       JOBTYPE       sp       Single Point energy
       METHOD        hf       Hartree-Fock
       BASIS         sto-3g   Basis set
    $end
    ```

???+ example "Example 4.3: UHF/6-311G calculation on the Li atom. Note that correlation and the job type
were not indicated because Q-Chem defaults automatically to no correlation
and single point energies. Note also that, since the number of $\alpha$ and $\beta$ electron differ, MOs default to an unrestricted formalism."
    ```qchem
    $molecule
       0,2
       Li
    $end
    
    $rem
       METHOD     HF       Hartree-Fock
       BASIS      6-311G   Basis set
    $end
    ```

???+ example "Example 4.4: ROHF/6-311G calculation on the Lithium atom."
    ```qchem
    $molecule
       0,2
       3
    $end
    
    $rem
       METHOD         hf       Hartree-Fock
       UNRESTRICTED   false    Restricted MOs
       BASIS          6-311G   Basis set
    $end
    ```
