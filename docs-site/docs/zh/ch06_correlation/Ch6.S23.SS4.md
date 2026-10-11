---
title: "6.23.4 示例"
---

## 6.23.4 示例

（2026 年 7 月 4 日）

???+ example "示例 6.62: 单点 v2RDM/STO-3G 能量计算。"
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

???+ example "示例 6.63: 含冻结核轨道的单点 v2RDM/STO-3G 能量计算。"
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

???+ example "示例 6.64: 单点 v2RDM-CASSCF/cc-pVDZ 能量与梯度计算。"
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

???+ example "示例 6.65: 使用 v2RDM-CASSCF 优化后的约化密度矩阵（RDM）进行单点 MC-PDFT/cc-pVDZ 能量计算。"
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
