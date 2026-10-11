---
title: "7.4.5 Real-Time Extension of TAO-DFT (RT-TAO)"
---

## 7.4.5 Real-Time Extension of TAO-DFT (RT-TAO)

(July 4, 2026)

In order to investigate the time-dependent dynamics of large, strongly correlated systems starting from the ground state,
and with a focus on minimizing computational complexity,
Hung-Yi Tsai and Prof. Jeng-Da Chai have extended thermally-assisted-occupation density functional theory (TAO-DFT)[[227]](../bib_references/bib.md#bib222)
 to real-time TAO-DFT (RT-TAO).[[1376]](../bib_references/bib.md#bib1437)

The RT-TAO method is initiated with a TAO-DFT calculation (refer to Section [5.12.3](../ch05_dft/ex_ptao.md)) and is followed by time propagation (refer to Section [7.4](sec_TDKS.md)).
The computational cost associated with RT-TAO is comparable to that of time-dependent Kohn-Sham,
and it becomes equivalent to the cost of time-dependent Kohn-Sham in the absence of significant static correlation effects.

To perform an RT-TAO calculation, users are instructed to set TAO_DFT = TRUE and TDKS = TRUE in the *$rem* input section.
Additional job control options are detailed in Section [5.12.3](../ch05_dft/ex_ptao.md) and Section [7.4.2](sec_TDKS_JobControl.md).

RT-TAO, serving as a real-time extension of TAO-DFT, is governed by a fictitious temperature parameter denoted as $\theta$.
Setting TAO_DFT_THETA = 0 brings the method back to the ordinary time-dependent Kohn-Sham.[[1376]](../bib_references/bib.md#bib1437)

In the adiabatic approximation, alongside the exchange-correlation (XC) functional, an additional functional $E_{\theta}[\rho]$ is required for RT-TAO.

Two illustrative examples of RT-TAO calculations are provided:

???+ example "Example 7.37: RT-TAO-ALDA, spin-restricted calculation on stretched H ${}_{2}$"
    ```qchem
    $molecule
       0 1
       H 0.000000 0.000000 1.000000
       H 0.000000 0.000000 -1.000000
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TDKS                true
       SCF_CONVERGENCE     7
       TAO_DFT             true
       TAO_DFT_THETA       40   ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3    ! default
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```

???+ example "Example 7.38: RT-TAO-ALDA, spin-unrestricted calculation on stretched H ${}_{2}$"
    ```qchem
    $molecule
       0 1
       H 0.000000 0.000000 1.000000
       H 0.000000 0.000000 -1.000000
    $end
    
    $rem
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TDKS                true
       SCF_CONVERGENCE     7
       TAO_DFT             true
       TAO_DFT_THETA       40   ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3    ! default
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3    ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```
