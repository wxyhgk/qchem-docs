---
title: "12.5.4 Perturbative Charge-Transfer Analysis Usinig Complementary Occupied/Virtual Pairs"
---

## 12.5.4 Perturbative Charge-Transfer Analysis Usinig Complementary Occupied/Virtual Pairs

(July 4, 2026)

In addition to quantifying the amount and energetics of intermolecular charge
transfer, it is often useful to have a simple description of orbital
interactions in intermolecular complexes. The polarized ALMOs obtained from the
SCF-MI procedure and used as a reference basis set in the decomposition
analysis do not directly show which occupied-virtual orbital pairs are of most
importance in forming intermolecular bonds. By performing rotations of the
polarized ALMOs within a molecule, it is possible to find a “chemist’s basis
set” that represents bonding between molecules in terms of just a few
localized orbitals called complementary occupied-virtual pairs (COVPs). This
orbital interaction model validates existing conceptual descriptions of
intermolecular bonding. For example, in the modified ALMO basis, hydrogen
bonding in water dimer is represented as an electron pair localized on an
oxygen atom donating electrons to the O–H $\sigma$-antibonding orbital on the
other molecule,[[681]](../bib_references/bib.md#bib708)
 and the description of synergic bonding
in metal complexes agrees well with simple Dewar-Chatt-Duncanson
model.[[257]](../bib_references/bib.md#bib258)

Set EDA_COVP to TRUE to perform the COVP analysis of the CT
term in an EDA job. COVP analysis is currently implemented only for
systems of two fragments. Set EDA_PRINT_COVP to TRUE to
print out localized orbitals that form occupied-virtual pairs. In this case,
MOs obtained in the end of the run (SCF-MI orbitals, SCF-MI(RA) orbitals,
converged SCF orbitals) are replaced by the orbitals of COVPs. Each orbital is
printed with the corresponding CT energy term in kJ/mol (instead of the energy
eigenvalues in hartrees). These energy labels make it easy to find
correspondence between an occupied orbital on one molecule and the virtual
orbital on the other molecule. The examples below show how to print COVP
orbitals. One way is to set *$rem* variable PRINT_ORBITALS, the other
is to set IANLTY to 200 and use the *$plots* section in the **Q-Chem**
input. In the first case, the orbitals can be visualized using MOLDEN (set
MOLDEN_FORMAT to TRUE). In the second case use
Visual Molecular Dynamics (VMD)[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)
or a similar third party program capable of making 3D plots.

???+ example "Example 12.10: COVP analysis of the CT term. The COVP orbitals are printed in the Q-Chem and MOLDEN formats."
    ```qchem
    $molecule
    0 1
    --
    0 1
    O          -1.521720    0.129941    0.000000
    H          -1.924536   -0.737533    0.000000
    H          -0.571766   -0.039961    0.000000
    --
    0 1
    O           1.362840   -0.099704    0.000000
    H           1.727645    0.357101   -0.759281
    H           1.727645    0.357101    0.759281
    $end
    
    $rem
       JOBTYPE         EDA
       EDA2            FALSE
       BASIS           6-31G
       PURECART        1112
       METHOD          B3LYP
       FRGM_METHOD     GIA
       FRGM_LPCORR     RS_EXACT_SCF
       EDA_COVP        TRUE
       EDA_PRINT_COVP  TRUE
       PRINT_ORBITALS  16
       MOLDEN_FORMAT   TRUE
    $end
    ```

???+ example "Example 12.11: COVP analysis of the CT term. Note that it is not necessary to run a full EDA
job. It is suffice to set FRGM_LPCORR to RS or ARS and EDA_COVP = TRUE to perform the COVP analysis. The
orbitals of the most significant occupied-virtual pair are printed into an
ASCII file called plot.mo which can be converted into a cube file and
visualized in VMD."
    ```qchem
    $molecule
    0 1
    --
    0 1
    O          -1.521720    0.129941    0.000000
    H          -1.924536   -0.737533    0.000000
    H          -0.571766   -0.039961    0.000000
    --
    0 1
    O           1.362840   -0.099704    0.000000
    H           1.727645    0.357101   -0.759281
    H           1.727645    0.357101    0.759281
    $end
    
    $rem
       BASIS           6-31G
       PURECART        1112
       METHOD          B3LYP
       FRGM_METHOD     GIA
       FRGM_LPCORR     RS
       IANLTY          200
       EDA_COVP        TRUE
       EDA_PRINT_COVP  TRUE
    $end
    
    $plots
    MOs
       80  -4.0  4.0
       60  -3.0  3.0
       60  -3.0  3.0
       2   0  0  0
       6  11
    $end
    ```
