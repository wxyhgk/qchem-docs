---
title: "9.12.1 Introduction"
---

## 9.12.1 Introduction

(July 4, 2026)

The potential energy landscape of atomic and molecular clusters can be very
complex with many minima which can have similar energies, and this complexity
increases rapidly as the size of the clusters increases. Determining the global
minimum of these clusters is challenging since it requires extensive searching
over the potential energy surface. One approach to finding the low energy
structures of these clusters is to perform many geometry optimizations starting
at different initial coordinates. **Q-Chem** is able to perform such random
searches for molecular clusters containing up to two different molecule types.
In these searches the molecules are subjected to translations and rotations of
their structure to generate a new starting structure. These searches are
initiated by the JOBTYPE = RAND and it is necessary to
specify the number of molecules of the different types and the number of atoms
in the different types of molecules. For the optimization of atomic clusters,
SEARCH_ATOMIC = TRUE and the number of atom swops performed
in the structure generation (N_SWOP) can be specified. Some care has
to be taken with the specification of the input structure in the
*$molecule* section. All the atoms of the molecules of molecule type 1
must come before those of molecule type 2. Furthermore, the atoms of the same
molecule should be together. For examples of these studies see
Refs. [[338]](../bib_references/bib.md#bib343)
.

???+ example "Example 9.52: A random search geometry optimization of the NO ${}^{+}$ .H ${}_{2}$ O cluster."
    ```qchem
    $molecule
       1 1
       N    0.5682008336    0.1585044954   -0.9009280260
       O   -0.3450383302   -0.5598328271   -0.4634299478
       O    1.7303273568    0.3403569345    0.4364171165
       H    2.5236300547   -0.2494576134    0.1485689942
       H    2.1020812302    1.2823911654    0.2570156558
    $end
    
    $rem
       JOBTYPE                     RAND
       METHOD                      B3LYP
       BASIS                       STO-3G
       SCF_CONVERGENCE             6
       MAX_SCF_CYCLES              100
       NSEARCH                     10
       N_MOL_TYPE                  2
       NMOL1                       1
       N_ATOM_TYPE_1               2
       NMOL2                       1
       N_ATOM_TYPE_2               3
       N_MOVES                     20
       MAXBOX                      10000
       MIN_SEPARATION              25
       MAX_DISPLACE                25
       SCF_NOCRASH                 TRUE
       TIGHTEN_CONVERG             TRUE
       GEOM_OPT_MAX_CYCLES         200
       GEOM_OPT_COORDS             0
       GEOM_OPT_TOL_DISPLACEMENT   1000
       GEOM_OPT_TOL_GRADIENT       300
       GEOM_OPT_TOL_ENERGY         100
    $end
    ```

???+ example "Example 9.53: A random search geometry optimization of the He ${}_{3}$ Ne ${}_{3}$ cluster."
    ```qchem
    $molecule
       0 1
       He   -1.3590894    3.0177788   -0.1662522
       He   -2.9853158    1.1444488    0.1036005
       He    0.5068109    1.3795209   -0.2168151
       Ne   -1.1002149   -0.5693061    0.0381894
       Ne    0.5981676    1.8697812    1.4685618
       Ne   -1.2376457    1.2597811   -0.0756066
    $end
    
    $rem
       JOBTYPE                     RAND
       METHOD                      B3LYP
       DFT_D                       EMPIRICAL_GRIMME
       BASIS                       STO-3G
       SCF_CONVERGENCE             6
       MAX_SCF_CYCLES              100
    
       NSEARCH                     10
       SEARCH_ATOMIC               TRUE
       N_SWOP                      4
       N_MOL_TYPE                  2
       NMOL1                       3
       N_ATOM_TYPE_1               1
       NMOL2                       3
       N_ATOM_TYPE_2               1
       N_MOVES                     20
       MAXBOX                      10000
       MIN_SEPARATION              25
       MAX_DISPLACE                25
       SCF_NOCRASH                 TRUE
       TIGHTEN_CONVERG             TRUE
       USE_INITIAL                 TRUE
    
       GEOM_OPT_MAX_CYCLES         200
       GEOM_OPT_COORDS             0
       GEOM_OPT_TOL_DISPLACEMENT   1000
       GEOM_OPT_TOL_GRADIENT       3000
       GEOM_OPT_TOL_ENERGY         1000
    $end
    ```

Basin hopping (BH) is a more advanced technique for locating
the global minimum on complex potential energy surfaces.[[1421]](../bib_references/bib.md#bib1481)

The BH algorithm is essentially a combination of the Metropolis sampling technique and a
gradient-based local search method. This has the effect of sampling the energy
basins, where an energy basin is a certain part of the configuration space
around a minimum on the PES that contains all the configurations that will
relax into this minimum using downhill relaxations, instead of sampling the
configuration space. To enhance the efficiency of the method, BH with
occasional jumping is used,[[616]](../bib_references/bib.md#bib639)
 which incorporates a jumping
move in addition to the standard Monte Carlo (MC) moves. Jumping is a MC move
without local minimization at infinite temperature and, consequently, is always
accepted. When the usual MC moves are rejected a number of times, the system
is judged to be trapped at the local minimum. The temperature is raised to $T=\infty$,
and the MC jumping moves are executed several times to allow the
system to escape from the local minimum. This provides an efficient way to
escape from a local minimum and to explore the next basin of the valley when it
is separated by high barriers. Depending on the size and complexity of the
system being studied, a large number of MC_STEPS and/or
MC_CYCLES to ensure the global minimum is found.

???+ example "Example 9.54: A basin hopping search for the NO ${}^{+}$ (H ${}_{2}$ O) cluster."
    ```qchem
    $molecule
       1 1
       N     0.5682008336    0.1585044954   -0.9009280260
       O    -0.3450383302   -0.5598328271   -0.4634299478
       O     1.7303273568    0.3403569345    0.4364171165
       H     2.5236300547   -0.2494576134    0.1485689942
       H     2.1020812302    1.2823911654    0.2570156558
    $end
    
    $rem
      JOBTYPE          BH
      METHOD           B3LYP
      BASIS            STO-3G
      SCF_CONVERGENCE  6
      MAX_SCF_CYCLES   100
    
      MC_CYCLES             4
      MC_STEPS              5
      MC_TEMP               300
      MAX_DISPLACE          25
      MIN_SEPARATION        25
      MAXBOX                5000
      N_MOVES               20
    
      N_MOL_TYPE       2
      NMOL1            1
      N_ATOM_TYPE_1    2
      NMOL2            1
      N_ATOM_TYPE_2    3
      N_MOVES          20
      MAXBOX           10000
      MIN_SEPARATION   25
      MAX_DISPLACE     25
      SCF_NOCRASH      TRUE
    
      GEOM_OPT_MAX_CYCLES       200
      GEOM_OPT_COORDS           0
      GEOM_OPT_TOL_DISPLACEMENT 2000
      GEOM_OPT_TOL_GRADIENT     4000
      GEOM_OPT_TOL_ENERGY       400
    $end
    ```
