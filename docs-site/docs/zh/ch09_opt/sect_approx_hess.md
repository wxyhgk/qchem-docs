---
title: "9.3.3 Hessian-Free Transition-State Search"
---

## 9.3.3 Hessian-Free Transition-State Search

(July 4, 2026)

Once a guess structure to the transition state is obtained, standard
eigenvector-following methods such as Baker’s partitioned rational-function
optimization (P-RFO) algorithm[[64]](../bib_references/bib.md#bib46)
 can be employed to refine the
guess to the exact transition state. The reliability of P-RFO depends on the
quality of the Hessian input, which enables the method to distinguish between
the reaction coordinate (characterized by a negative eigenvalue) and the
remaining degrees of freedom. In routine calculations therefore, an exact
Hessian is determined via frequency calculation prior to the P-RFO search.
Since the cost of evaluating an exact Hessian typically scales one power of
system size higher than the energy or the gradient, this step becomes
impractical for systems containing large number of atoms.

The exact Hessian calculation can be avoided by constructing an approximate
Hessian based on the output of FSM.[[1243]](../bib_references/bib.md#bib1297)
 The tangent direction at
the transition state guess on the FSM string is a good approximation to the
Hessian eigenvector corresponding to the reaction coordinate. The tangent is
therefore used to calculate the correct eigenvalue and corresponding
eigenvector by variationally minimizing the Rayleigh-Ritz
ratio.[[739]](../bib_references/bib.md#bib1482)
 The reaction coordinate information is then
incorporated into a guess matrix which, in turn, is obtained by transforming a
diagonal matrix in delocalized internal
coordinates[[63]](../bib_references/bib.md#bib50)
 to Cartesian coordinates.
The resulting approximate Hessian, by design, has a single negative eigenvalue
corresponding to the reaction coordinate. This matrix is then used in place of
the exact Hessian as input to the P-RFO method.

???+ example "Example 9.10: An example one-shot, Hessian-free approach that combines the FSM and P-RFO
methods in order to determine the exact transition state from reactant and
product structures."
    ```qchem
    $molecule
       0  1
       Si   1.028032  -0.131573  -0.779689
       H    0.923921  -1.301934   0.201724
       H    1.294874   0.900609   0.318888
       H   -1.713989   0.300876  -0.226231
       H   -1.532839   0.232021   0.485307
    ****
       Si   0.000228  -0.000484  -0.000023
       H    0.644754  -1.336958  -0.064865
       H    1.047648   1.052717   0.062991
       H   -0.837028   0.205648  -1.211126
       H   -0.855603   0.079077   1.213023
    $end
    
    $rem
       JOBTYPE               fsm
       METHOD                b3lyp
       BASIS                 6-31g
       FSM_NGRAD             3
       FSM_NNODE             18
       FSM_MODE              2
       FSM_OPT_MODE          2
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE               ts
       METHOD                b3lyp
       BASIS                 6-31g
       SCF_GUESS             read
       GEOM_OPT_HESSIAN      read
       MAX_SCF_CYCLES        250
       GEOM_OPT_DMAX         50
       GEOM_OPT_MAX_CYCLES   100
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    ```
