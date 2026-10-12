---
title: "7.9.23 EOM-CCSDT for High Accuracy (CCMAN2 only)"
---

## 7.9.23 EOM-CCSDT for High Accuracy
(CCMAN2 only)

(July 4, 2026)

The equation-of-motion singles, doubles and triples (EOM-CCSDT) method[[884]](../bib_references/bib.md#bib917)

is an extension of EOM-CCSD method in which
full triples are included both at the CC and EOM levels (in addition to singles and doubles).
Conceptually, EOM-CCSD and EOM-CCSDT are similar; the difference lies only in
the truncation level.
The CC Hamiltonian matrix being non-Hermitian, the left and right eigenvectors
are not Hermitian conjugates of each other but can be chosen to form
a mutually biorthogonal set. Using Eq. ([7.97](sec_EOMEE.md#eq747)), the right eigenvectors
can be obtained and this is sufficient for obtaining energies (and excitation
energies) of
the corresponding target states. For gradients and properties, one must in addition
solve for the left eigenvectors of the respective states.

In EOM-CCSDT, the CCSDT Hamiltonian matrix is constructed up to the triples block
so as to give one-, two-, and three-body eigenvectors of the CC Hamiltonian.
As a result, the EOM-CCSDT computed energies and properties
are highly accurate as compared even to
the EOM-CCSD ones, by almost an order of magnitude. For example,
EOM-CCSDT provides an accuracy of $\sim 0.01$ eV for singly excited states and single
bond-breaking, and an accuracy of 0.1–0.2 eV for doubly excited states. In contrast,
at the EOM-CCSD levels these errors are on the order of 0.1–0.2 eV and $>1$ eV, respectively.
EOM-CCSDT has ${\cal{O}}({N^{8}})$ scaling versus ${\cal{O}}({N^{6}})$ for EOM-CCSD.
Unlike EOM-CC(2,3), the EOM-CCSDT approach is rigorously size-intensive, as is EOM-CCSD,
but it is expensive enough that it can only be used with careful memory management.
Currently, the SF, EE, IP, EA, DIP, and DEA
variants of EOM-CCSDT are available,[[884]](../bib_references/bib.md#bib917)

for single point energy computations only, and can be requested by setting
METHOD = EOM-CCSDT. EOM-CCSDT is implemented within the new
coupled-cluster suite (CCMAN2) both within double and within singe precision.
Other job-control variables are similar to EOM-CCSD ones.

Illustrative examples employing EOM-CCSDT for computing excitation energies are given below.

!!! note "Note"
    For non-trivial calculations we recommend using
    CC_BACKEND=XM.


???+ example "Example 7.152: Computation of first excited singlet (B ${}_{1}$ ) and first excited triplet (B ${}_{2}$ )
energies of BH using EOM-EE-CCSDT/STO-3G
in a single-precision setup."
    ```qchem
    $comment
    Computation of energies singlet and a triplet excited states of BH
    using EOM-EE-CCSDT/STO-3G
    $end
    
    $molecule
    0 1
    B
    H  1  1.234347
    $end
    
    $rem
    basis=sto-3g
    job_type=sp
    method eom-ccsdt
    cc_single_prec=1
    eom_single_prec=1
    n_frozen_core fc
    ee_singlets=[0,0,1,0]
    ee_triplets=[0,0,0,1]
    $end
    
    ```

???+ example "Example 7.153: Computation of singlet ground state and lowest triplet state
energies of BH using EOM-SF-CCSDT/STO-3G
in a double-precision setup."
    ```qchem
    $comment
    Computation of spin-flipping excitation energies of
    BH using EOM-SF-CCSDT/STO-3G, UHF reference
    $end
    
    $molecule
    0 3
    B
    H 1 1.191857
    $end
    
    $rem
    jobtype=sp
    method eom-ccsdt
    basis=sto-3g
    sf_states=[1,0,0,1]
    eom_nguess_singles=4
    n_frozen_core fc
    $end
    ```

Illustrative examples employing EOM-CCSDT method for computing ionization energies/electron affinities
are given below.

???+ example "Example 7.154: Computation of the singlet ground state and lowest four IP state
energies of N ${}_{2}$ using EOM-IP-CCSDT/6-31G*
in a double-precision setup."
    ```qchem
    $molecule
    0 1
    N
    N 1  1.097685
    $end
    
    $rem
    method=eom-ccsdt
    IP_states=[4]
    basis=6-31G*
    cc_symmetry=false
    EOM_davidson_convergence=6
    job_type=sp
    $end
    ```

???+ example "Example 7.155: Computation of singlet ground state and lowest four EA state
energies of C ${}_{2}$ using EOM-EA-CCSDT/6-31G*
in a double-precision setup."
    ```qchem
    $molecule
    0 1
    C
    C 1  1.243
    $end
    
    $rem
    method=eom-ccsdt
    EA_states=[4]
    basis=6-31G*
    cc_symmetry=false
    EOM_davidson_convergence=6
    job_type=sp
    $end
    ```

???+ example "Example 7.156: Computation of singlet ground state and lowest two DIP state
energies of O using EOM-DIP-CCSDT/6-31G
in a double-precision setup."
    ```qchem
    $molecule
    -2 1
    O
    $end
    
    $rem
    method=eom-ccsdt
    basis=6-31g
    DIP_STATES=[2]
    cc_symmetry=false
    $end
    
    ```

???+ example "Example 7.157: Computation of singlet ground state and lowest two DEA state
energies of C using EOM-DEA-CCSDT/6-31G
in a double-precision setup."
    ```qchem
    $molecule
    2  1
    C
    $end
    
    $rem
    method=eom-ccsdt
    basis=6-31g
    DEA_STATES=[2]
    cc_symmetry=false
    $end
    
    ```
