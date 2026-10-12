---
title: "10.5.3 Visualization of Natural Transition Orbitals"
---

## 10.5.3 Visualization of Natural Transition Orbitals

(July 4, 2026)

For excited states calculated using the CIS, RPA, TDDFT, EOM-CC, and ADC
methods, construction of Natural Transition Orbitals (NTOs), as described in
Sections [7.13.3](../ch07_excited/sect_NTOs.md) and [10.2.12](ex_StateAnal_MolDen.md), is requested using the
*$rem* variable NTO_PAIRS. This variable also determines the number
of hole/particle NTO pairs that are output for each excited state and the
number of natural orbitals or natural difference orbitlas. Although the total
number of hole/particle pairs is equal to the number of occupied MOs, typically
only a very small number of these pairs (often just one pair) have significant
amplitudes. (Additional large-amplitude NTOs may be encountered in cases of
strong electronic coupling between multiple chromophores or where there is
significant multireference character in the excited state.[[572]](../bib_references/bib.md#bib586)
)

### `NTO_PAIRS`

> **Controls the writing of hole/particle NTO pairs for excited state.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$: Write $N$ NTO pairs per excited state.
> * **Recommendation**: If activated ( $N>0$ ), a minimum of two NTO pairs will be printed for each state. Increase the value of $N$ if additional NTOs are desired.

When NTO_PAIRS $>0$, **Q-Chem** will generate the NTOs in **MolDen**
format. The NTOs are state-specific, in the sense that each excited state has
its own NTOs, and therefore a separate **MolDen** file is required for each
excited state. These files are written to the job’s scratch directory, in a
sub-directory called *NTOs*, so to obtain the NTOs the scratch directory
must be saved using the *–save* option that is described in
Section [2.2](../ch02_install/sect_running.md). The output files in the *NTOs* directory have
an obvious file-naming convention. The “hole” NTOs (which are linear
combinations of the occupied MOs) are printed to the **MolDen** files in order
of increasing importance, with the corresponding excitation amplitudes
replacing the canonical MO eigenvalues. (This is a formatting convention only;
the excitation amplitudes are unrelated to the MO eigenvalues.) Following the
holes are the “particle” NTOs, which represent the excited electron and are
linear combinations of the virtual MOs. These are written in order of
decreasing amplitude. To aid in distinguishing the two sets within the
**MolDen** files, the amplitudes of the holes are listed with negative signs,
while the corresponding NTO for the excited electron has the same amplitude
with a positive sign.

Due to the manner in which the NTOs are constructed (see
Section [7.13.3](../ch07_excited/sect_NTOs.md)), NTO analysis is available only when the number of
virtual orbitals exceeds the number of occupied orbitals, which may not be the
case for minimal basis sets.

???+ example "Example 10.23: Generating MolDen -formatted natural transition orbitals
for several excited states of uracil."
    ```qchem
    $molecule
       0 1
       N    -2.181263     0.068208     0.000000
       C    -2.927088    -1.059037     0.000000
       N    -4.320029    -0.911094     0.000000
       C    -4.926706     0.301204     0.000000
       C    -4.185901     1.435062     0.000000
       C    -2.754591     1.274555     0.000000
       N    -1.954845     2.338369     0.000000
       H    -0.923072     2.224557     0.000000
       H    -2.343008     3.268581     0.000000
       H    -4.649401     2.414197     0.000000
       H    -6.012020     0.301371     0.000000
       H    -4.855603    -1.768832     0.000000
       O    -2.458932    -2.200499     0.000000
    $end
    
    $rem
       METHOD          B3LYP
       BASIS           6-31+G*
       CIS_N_ROOTS     3
       NTO_PAIRS       2
    $end
    ```
