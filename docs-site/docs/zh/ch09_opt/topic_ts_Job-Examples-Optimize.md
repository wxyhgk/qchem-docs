---
title: "9.2.4 Optimize Job Examples"
---

## 9.2.4 **Optimize** Job Examples

(July 4, 2026)

???+ example "Example 9.1: Optimization in $Z$ -matrix coordinates. The input must be specified in $Z$ -matrix format with coordinates specified. In the example below there are
two coordinates representing the bond length and bond angle of a water
molecule."
    ```qchem
    $molecule
       0 1
       O
       H 1 r
       H 1 r 2 ang
    
       r   0.95
       ang 104.5
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            HF
       BASIS             STO-3G
       GEOM_OPT_COORDS   2
    $end
    ```

???+ example "Example 9.2: Geometry optimization of a triflate anion that converges to an eclipsed
conformation, which is a first order saddle point. This is verified via the
finite difference Davidson method by setting GEOM_OPT_CHARAC to TRUE ."
    ```qchem
    $molecule
       -1 1
       C  0.00000 -0.00078  0.98436
       F -1.09414 -0.63166  1.47859
       S  0.00000  0.00008 -0.94745
       O  1.25831 -0.72597 -1.28972
       O -1.25831 -0.72597 -1.28972
       O  0.00000  1.45286 -1.28958
       F  1.09414 -0.63166  1.47859
       F  0.00000  1.26313  1.47663
    $end
    
    $rem
       JOBTYPE                    opt
       METHOD                     BP86
       GEOM_OPT_DMAX              50
       BASIS                      6-311+G*
       SCF_CONVERGENCE            8
       THRESH                     14
       GEOM_OPT_TOL_DISPLACEMENT  10
       GEOM_OPT_TOL_ENERGY        10
       GEOM_OPT_TOL_GRADIENT      10
       GEOM_OPT_CHARAC            TRUE
       INTEGRAL_SYMMETRY          FALSE
       POINT_GROUP_SYMMETRY       FALSE
    $end
    ```

???+ example "Example 9.3: TS search for alanine dipeptide rearrangement reaction beginning with a guess structure
converges correctly. The resulting TS structure is verified using the finite difference
Davidson method."
    ```qchem
    $molecule
       0    1
       C          3.21659       -1.41022       -0.26053
       C          2.16708       -0.35258       -0.59607
       N          1.21359       -0.16703        0.41640
       C          0.11616        0.82394        0.50964
       C         -1.19613        0.03585        0.74226
       N         -2.18193       -0.02502       -0.18081
       C         -3.43891       -0.74663        0.01614
       O          2.19596        0.25708       -1.63440
       C          0.11486        1.96253       -0.53088
       O         -1.29658       -0.59392        1.85462
       H          3.25195       -2.14283       -1.08721
       H          3.06369       -1.95423        0.67666
       H          4.20892       -0.93714       -0.22851
       H          1.24786       -0.78278        1.21013
       H          0.25990        1.31404        1.47973
       H         -2.02230        0.38818       -1.10143
       H         -3.60706       -1.48647       -0.76756
       H         -4.29549       -0.06423        0.04327
       H         -3.36801       -1.25875        0.98106
       H         -0.68664        2.66864       -0.27269
       H          0.01029        1.65112       -1.56461
       H          1.06461        2.50818       -0.45885
    $end
    
    $rem
       JOBTYPE              freq
       EXCHANGE             B3LYP
       BASIS                6-31G
       SCF_MAX_CYCLES       250
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE              ts
       SCF_GUESS            read
       GEOM_OPT_DMAX        100
       GEOM_OPT_MAX_CYCLES  1500
       EXCHANGE             B3LYP
       BASIS                6-31G
       MAX_SCF_CYCLES       250
       GEOM_OPT_HESSIAN     read
       GEOM_OPT_CHARAC      true
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
