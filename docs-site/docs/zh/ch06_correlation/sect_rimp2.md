---
title: "6.6.2 RI-MP2 Energies and Gradients."
---

## 6.6.2 RI-MP2 Energies and Gradients.

(July 4, 2026)

Following common convention, the MP2 energy evaluated approximately using an
auxiliary basis is referred to as “resolution of the identity” MP2, or RI-MP2
for short. RI-MP2 energy and gradient calculations are enabled simply by
specifying the AUX_BASIS keyword discussed above. As discussed above,
RI-MP2 energies[[387]](../bib_references/bib.md#bib395)
 and
gradients[[1440]](../bib_references/bib.md#bib1500)
 are significantly faster than the
best conventional MP2 energies and gradients, and cause negligible loss of
accuracy, when an appropriate standardized auxiliary basis set is employed.
Therefore they are recommended for jobs where turnaround time is an issue. Disk
requirements are very modest; one merely needs to hold various 3-index arrays.
Memory requirements grow more slowly than our conventional MP2
algorithms—only quadratically with molecular size. The minimum memory
requirement is approximately 3$X^{2}$, where $X$ is the number of auxiliary
basis functions, for both energy and analytical gradient evaluations, with some
additional memory being necessary for integral evaluation and other small
arrays.

In fact, for molecules that are not too large (perhaps no more than 20 or 30
heavy atoms) the RI-MP2 treatment of electron correlation is so efficient that
the computation is dominated by the initial Hartree-Fock calculation. This is
despite the fact that as a function of molecule size, the cost of the RI-MP2
treatment still scales more steeply with molecule size (it is just that the
pre-factor is so much smaller with the RI approach). Its scaling remains
5th order with the size of the molecule, which only dominates the
initial SCF calculation for larger molecules. Thus, for RI-MP2 energy
evaluation on moderate size molecules (particularly in large basis sets), it is
desirable to use the dual basis HF method to further improve execution times
(see Section [4.7](../ch04_scf/sect_dualbasis.md)).

For the size of required memory, the following need to be considered.

MEM_STATIC

### `MEM_STATIC`

> **Sets the memory for AO-integral evaluations and their transformations in Q-Chem 4.1 or older versions.**
>
> * **Type**: `INTEGER`
> * **Default**: `192`
> * **Options**:
>     * $n$
>     * User-defined number of megabytes.
> * **Recommendation**: For RI-MP2 calculations using Q-Chem 4.1 or older versions, $150(ON+V)$ of is required. Because a number of matrices with $N^{2}$ size also need to be stored, 32–160 MB of additional is needed.

MEM_TOTAL

### `MEM_TOTAL`

> **Sets the total memory available to Q-Chem , in megabytes.**
>
> * **Type**: `INTEGER`
> * **Default**: `2000`
> * **Options**:
>     * $n$
>     * User-defined number of megabytes.
> * **Recommendation**: Use the default, or set to the physical memory of your machine. The minimum requirement is $3X^{2}$ .

???+ example "Example 6.4: Q-Chem input for an RI-MP2 geometry optimization."
    ```qchem
    $molecule
       0 1
       O
       H  1  0.9
       F  1  1.4  2  100.
    $end
    
    $rem
       JOBTYPE       opt
       METHOD        rimp2
       BASIS         cc-pvtz
       AUX_BASIS     rimp2-cc-pvtz
       INTEGRAL_SYMMETRY false
    $end
    ```
