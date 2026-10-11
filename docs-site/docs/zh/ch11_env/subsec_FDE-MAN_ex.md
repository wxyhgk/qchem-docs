---
title: "11.7.6 Examples"
---

## 11.7.6 Examples

(July 4, 2026)

???+ example "Example 11.48: Input for a FDE-HF/cc-pVDZ calculation with monomer expansion of CO
embedded in one water molecule, using LDA functionals for the embedding potential."
    ```qchem
    $molecule
       0 1
    --
       0 1
       C    -3.618090    1.376803   -0.020795
       O    -4.735683    1.525556    0.115023
    --
       0 1
       O    -7.956372    1.485406    0.116792
       H    -6.992316    1.421133    0.177470
       H    -8.105846    2.442220    0.111599
    $end
    
    $rem
    point_group_symmetry = False
       METHOD       = hf
       BASIS        = cc-pvdz
       FDE          = true
       MEM_STATIC   = 1024
       MEM_TOTAL    = 2200
    $end
    
    $fde
       T_Func       TF
       X_Func       Slater
       C_Func       VWN5
       expansion    mono
       rhoB_method  HF
    $end
    ```

???+ example "Example 11.49: Input for a superposition of molecular densities with HF/cc-pVDZ of 5 water molecules."
    ```qchem
    $rem
       METHOD        = HF
       BASIS         = cc-pvdz
       FDE           = true
       MEM_STATIC    = 1024
       MEM_TOTAL     = 4000
    point_group_symmetry = False
    $end
    
    $molecule
      0 1
    --
      0 1
      O       8.67400    -66.68200    -88.40400
      H       8.90400    -65.96300    -89.01800
      H       9.36700    -67.38600    -88.67300
    --
      0 1
      O      10.22000    -68.60400    -89.71700
      H      10.40700    -68.14800    -90.58500
      H       9.58700    -69.25100    -90.08700
    --
      0 1
      O       8.20100    -70.34800    -90.56300
      H       8.40300    -71.24600    -90.20800
      H       8.75700    -70.28300    -91.32900
    --
      0 1
      O       4.44400    -62.52200    -85.97300
      H       5.18300    -62.60300    -86.58400
      H       4.88700    -62.11200    -85.22800
    --
      0 1
      O       5.71200    -65.65900    -83.58300
      H       5.98900    -65.59500    -84.50500
      H       4.99900    -66.31400    -83.64900
    $end
    
    $fde
       T_Func           TF
       XC_Func          PBE
       expansion        mono
       Superposition_B  true
       rhoB_method      HF
    $end
    ```

???+ example "Example 11.50: Input for a FDE-ADC(2)/cc-pVDZ calculation in supermolecular expansion of CO
embedded in one water molecule. For the embedding potential, the selected functionals are:
Thomas-Fermi kinetic energy, and PBE for the exchange-correlation term."
    ```qchem
    $molecule
       0 1
    --
       0 1
       C    -3.618090    1.376803   -0.020795
       O    -4.735683    1.525556    0.115023
    --
       0 1
       O    -7.956372    1.485406    0.116792
       H    -6.992316    1.421133    0.177470
       H    -8.105846    2.442220    0.111599
    $end
    
    $rem
       METHOD               = adc(2)
       BASIS                = cc-pvdz
       EE_STATES            = 2
       FDE                  = true
       MEM_STATIC           = 1024
       MEM_TOTAL            = 16000
       ADC_DAVIDSON_MAXITER = 100
       ADC_DAVIDSON_CONV    = 5
    point_group_symmetry = False
    $end
    
    $fde
       T_Func       TF
       XC_Func      PBE
       expansion    super
       rhoB_method  HF
    $end
    ```

???+ example "Example 11.51: Input for a Externally generated potential file to be read in any DFT calculation."
    ```qchem
    $comment
    First: Generates the DFTGRID for the the projection of the potential indicating
    use_libqints     true // This command will generate the DFTGRIDS.txt
    SYM_IGNORE       true //
    no_reorient      true // Orientation should not change in all job runs
    Warning: basis set used to generate the dftgrid must be same when external
    potential is read.
    Second: Run first inital job without PROJ_CAP and then with PROJ_CAP
    $end
    
    $molecule
    0 1
            O         0.0000000000    0.0000000000    0.1210550360
            H        -0.7527950783    0.0000000000   -0.4706429710
            H         0.7527950783    0.0000000000   -0.4706429710
    $end
    
    $rem
    jobtype               sp
    exchange              b3lyp
    correlation           none
    basis                 6-31G*
    scf_convergence       8
    max_scf_cycles        5000
    mem_static            4000
    mem_total             42000
    molden_format         false
    SYM_IGNORE            true
    no_reorient           true
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
    jobtype               sp
    exchange              b3lyp
    correlation           none
    basis                 6-31G*
    scf_convergence       8
    max_scf_cycles        5000
    mem_static            4000
    mem_total             42000
    molden_format         false
    PROJ_CAP              -10
    SYM_IGNORE            true
    no_reorient           true
    $end
    ```
