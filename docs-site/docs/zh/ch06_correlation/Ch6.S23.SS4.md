---
title: "6.23.4 Examples"
---

## 6.23.4 Examples

(July 4, 2026)

???+ example "Example 6.62: Single-point v2RDM/STO-3G energy computation."
    ```qchem
    $molecule
        0 1
        O  0.0000  0.0000  0.1173
        H  0.0000  0.7572 -0.4692
        H  0.0000 -0.7572 -0.4692
    $end
    
    $rem
        BASIS                           sto-3g
        AUX_BASIS                       rimp2-vdz
        METHOD                          rdm
        UNRESTRICTED                    false
        RDM_POSITIVITY                  dqg
        RDM_CONSTRAIN_SPIN              true
        RDM_MU_UPDATE_FREQUENCY         200
        RDM_EPS_CONVERGENCE             4
        RDM_E_CONVERGENCE               4
        RDM_MAXITER                     500000
        RDM_TAU                         10
        RDM_PRINT                       1
    $end
    ```

???+ example "Example 6.63: Single-point v2RDM/STO-3G energy computation with frozen core orbital."
    ```qchem
    $molecule
        0 1
        O  0.0000  0.0000  0.1173
        H  0.0000  0.7572 -0.4692
        H  0.0000 -0.7572 -0.4692
    $end
    
    $rem
        JOBTYPE                         sp
        BASIS                           sto-3g
        AUX_BASIS                       rimp2-vdz
        METHOD                          rdm
        UNRESTRICTED                    false
        RDM_POSITIVITY                  dqg
        RDM_CONSTRAIN_SPIN              true
        RDM_MU_UPDATE_FREQUENCY         200
        RDM_EPS_CONVERGENCE             4
        RDM_E_CONVERGENCE               4
        RDM_MAXITER                     500000
        RDM_TAU                         10
        RDM_PRINT                       1
    $end
    
    $rdm_active_space
    ¯1 0 0 0¯¯! frozen orbitals
    ¯0 0 0 0¯¯! restricted orbitals
    ¯3 0 2 1¯¯! active orbitals
    $end
    ```

???+ example "Example 6.64: Single-point v2RDM-CASSCF/cc-pVDZ energy and gradient computation."
    ```qchem
    $molecule
        0 1
        O  0.0000  0.0000  0.1173
        H  0.0000  0.7572 -0.4692
        H  0.0000 -0.7572 -0.4692
    $end
    
    $rem
        JOBTYPE                         force
        BASIS                           cc-pvdz
        AUX_BASIS                       rimp2-cc-pvdz
        METHOD                          rdm
        UNRESTRICTED                    false
        RDM_POSITIVITY                  dqg
        RDM_CONSTRAIN_SPIN              true
        RDM_MU_UPDATE_FREQUENCY         200
        RDM_EPS_CONVERGENCE             4
        RDM_E_CONVERGENCE               4
        RDM_MAXITER                     500000
        RDM_TAU                         10
        RDM_PRINT                       1
        RDM_ORBOPT_ENERGY_CONVERGENCE   7
        RDM_ORBOPT_GRADIENT_CONVERGENCE 4
        RDM_ORBOPT_FREQUENCY            500
        RDM_ORBOPT_MAXITER              5
    $end
    
    $rdm_active_space
    ¯0 0 0 0 ! frozen orbitals
    ¯1 0 0 0 ! restricted orbitals
    ¯3 0 2 1 ! active orbitals
    $end
    ```

???+ example "Example 6.65: Single-point MC-PDFT/cc-pVDZ energy computation with v2RDM-CASSCF optimized RDMs."
    ```qchem
    $molecule
    0 1
    H
    H 1 0.6
    $end
    
    $rem
    method = rdm(pdft)
    pdft_exchange = s
    pdft_correlation = vwn1rpa
    basis = cc-pvdz
    aux_basis = rimp2-cc-pvdz
    xc_grid = 000075000302
    rdm_optimize_orbitals = false
    rdm_e_convergence = 6
    rdm_print = 1
    $end
    
    ```
