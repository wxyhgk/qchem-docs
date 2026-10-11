---
title: "9.2.6 Libopt3 Job Examples"
---

## 9.2.6 **Libopt3** Job Examples

(July 4, 2026)

???+ example "Example 9.4: As outlined, the rate of convergence of the iterative optimization process is
dependent on a number of factors, one of which is the use of an initial
analytic Hessian. This is easily achieved by instructing Q-Chem to calculate
an analytic Hessian and proceed then to determine the required critical point.
This job runs within Libopt3 driver which retains the reading of
analytical Hessian feature."
    ```qchem
    $molecule
       0  1
       O
       H  1  oh
       H  1  oh 2 hoh
    
       oh  = 1.1
       hoh = 104
    $end
    
    $rem
       JOBTYPE    freq   Calculate an analytic Hessian
       METHOD     hf
       BASIS      6-31g(d)
    $end
    
    $comment
    Now proceed with the optimization making sure to read in the analytic
    Hessian (use other available information too).
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE            opt
       METHOD             hf
       BASIS              6-31g(d)
       SCF_GUESS          read
       GEOM_OPT_HESSIAN   read   Have the initial Hessian
    $end
    
    @@@
    
    $comment
    LIBOPT3 driver does not require the need for two jobs, as the exact analytic
    Hessian can be computed from the optimization job.  LIBOPT3 still retains the
    reading of Hessian for users who wish to split the jobs.
    $end
    
    $molecule
       0  1
       O
       H  1  oh
       H  1  oh 2 hoh
    
       oh  = 1.1
       hoh = 104
    $end
    
    $rem
       JOBTYPE    opt
       METHOD     hf
       BASIS      6-31g(d)
    $end
    
    $geom_opt
    initial_hessian exact !Start with analytic Hessian
    $end
    
    ```

???+ example "Example 9.5: Libopt3 has the capability to provide recomputation of the Hessian
during optimization. This is useful for difficult optimization jobs, but comes
with the additional computational cost of calculating Hessians, every N-cycles."
    ```qchem
    $comment
    Recompute Hessian during BFGS geometry optimization.
    $end
    
    $molecule
    0 1
    ¯7          3.79442        2.45076       -4.34277
    ¯6          3.02868        3.04864       -3.23778
    ¯6          2.04275        1.98420       -2.78714
    ¯6          2.91776        0.76144       -2.89342
    ¯6          3.54332        1.00509       -4.25717
    ¯1          2.53337        3.99823       -3.53031
    ¯1          3.72326        3.26015       -2.39028
    ¯1          1.21899        1.90515       -3.53349
    ¯1          1.60572        2.16457       -1.78197
    ¯1          2.38404       -0.20872       -2.80429
    ¯1          3.70935        0.81472       -2.11094
    ¯1          2.79274        0.75455       -5.04001
    ¯1          4.45076        0.38822       -4.43647
    ¯1          4.81196        2.64598       -4.19025
    $end
    
    
    $rem
    basis sto-3g
    exchange hf
    jobtype opt
    $end
    
    $geom_opt
    initial_hessian = exact !Start with Exact Hessian
    recompute_hessian = recompute  !Recompute Hessian
    !recompute_hessian_cycles = 5  !Recompute Hessian every N cycles
    $end
    
    ```

???+ example "Example 9.6: Optimize a structure and then perform vibrational analysis from the recomputed
Hessian."
    ```qchem
    $comment
    Optimize Ethanol then perform vibrational analysis on final structure.
    $end
    
    $molecule
    0 1
    ¯  1    0.0000000   -0.3967597    2.0821274
    ¯  6    0.0000000    0.2658586    1.2077483
    ¯  1   -0.8835614    0.9134896    1.2808899
    ¯  1    0.8835614    0.9134896    1.2808899
    ¯  6    0.0000000   -0.5475180   -0.0737199
    ¯  1    0.8913993   -1.2035918   -0.1244915
    ¯  1   -0.8913993   -1.2035918   -0.1244915
    ¯  8    0.0000000    0.3545729   -1.1566766
    ¯  1    0.0000000   -0.1696628   -1.9456823
    $end
    
    
    $rem
    basis sto-3g
    exchange hf
    jobtype opt
    $end
    
    $geom_opt
    hessian_verify = recomputed !Recompute Exact Hessian for verification
    final_vibrational_analysis = true !Perform Vibrational Analysis on optimized Hessian
    $end
    
    ```

???+ example "Example 9.7: Libopt3 can read in a user defined topology, rather than using the
generated topology."
    ```qchem
    $comment
    Read in user defined topology
    $end
    
    $molecule
    0 1
      H   -1.6466561   -2.6863748   -0.0117346
      O   -1.7341224   -2.4422496    0.9441588
      O   -1.0688554   -1.3124664    1.0588359
      H   -1.1563217   -1.0683412    2.0147293
    $end
    
    $rem
       BASIS  =  STO-3G
       JOB_TYPE  =  OPT
       METHOD  =  HF
    $end
    
    $geom_opt
    user_topology = read
    $end
    
    $geom_opt_topology
    6
    1 1 2
    1 2 3
    1 3 4
    2 1 3 2
    2 2 4 3
    4 1 2 3 4
    $end
    ```

???+ example "Example 9.8: Libopt3 by default uses an exact Hessian for transition-state
optimization, then allows for vibrational analysis which simplifies input."
    ```qchem
    $comment
    RXN001879
    Spiekermann, K., Pattanaik, L. & Green, W.H. High accuracy barrier heights,
    enthalpies, and rate coefficients for chemical reactions. Sci Data 9, 417
    (2022). https://doi.org/10.1038/s41597-022-01529-6
    $end
    
    $molecule
    0 1
    O   2.5305032887   0.8317743791  -0.5960924757
    C   0.9706549170  -1.0475202256   0.4849601433
    C   0.0736956346   0.0205588278   0.3578537226
    O   0.3380901377   1.1738635448  -0.0548187766
    C  -1.4333878481  -0.2639406922   0.6385105409
    O  -2.2647624299   0.6342430978  -0.0273189303
    H   2.1688119536   1.6729530969  -0.9456643506
    H   0.7400531937  -1.9417236242   1.0627253520
    H   1.7833628213  -1.0379315398  -0.2430184134
    H  -1.4983286779  -0.1807678096   1.7458032489
    H  -1.7266188309  -1.2860204892   0.3661250678
    H  -1.7121171597   1.4306544342  -0.1944071290
    $end
    
    $rem
    JOBTYPE                   TS
    METHOD                    B3LYP
    BASIS                     6-31g*
    INTERNAL_STABILITY        TRUE
    UNRESTRICTED              TRUE
    $end
    
    $geom_opt
    ¯hessian_verify recomputed
    ¯final_vibrational_analysis true
    $end
    ```
