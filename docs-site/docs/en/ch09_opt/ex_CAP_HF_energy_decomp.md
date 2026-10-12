---
title: "9.11.3 CAP-AIMD Job Control and Examples"
---

## 9.11.3 CAP-AIMD Job Control and Examples

(July 4, 2026)

The following three assignments are necessary in order to run a CAP-AIMD simulation:

- JOBTYPE = AIMD in *$rem*,
- COMPLEX_CCMAN = TRUE in *$rem* (see Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)), and
- CS_HF = 1 in *$complex_ccman* (see Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)).

For now, CAP-AIMD simulations are possible only with the cuboid CAP type, so setting CAP_TYPE = 1 is also necessary in the *$complex_ccman* section (see Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)).

With CAP-AIMD simulations, one gets two additional files in the AIMD directory (§[9.9.2](sub_aimd_jobcontrol.md)):

- `CAP_EComponents`: Records for each step the total complex energy, the CAP-corrected total complex energy, and the real and imaginary parts of the CAP contribution to the total complex energy – all in atomic units (a.u.).
- `CAP_PositionAndWidth`: Records for each step the total complex energy (in a.u.) and the resonance width (in electron-Volt).

### `CAP_AIMD_SWITCH`

> **Sets CAP_ETA to zero during a CAP-AIMD simulation when the real part of the last alpha occupied orbital’s energy is negative**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Set CAP_ETA to zero when the real part of the last alpha occupied orbital’s becomes negative.
>     * `FALSE`: Keep user’s CAP_ETA constant throughout simulation.
> * **Recommendation**: Use default.

### `CS_STRICT`

> **Determines Mulliken charges, multipole moments and complex orbital energies for CAP-HF calculations by reading, when applicable, complex density matrix or complex molecular orbital coefficient file**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: determine Mulliken charges, multipole moments and complex orbital energies for CAP-HF calculations by reading – when applicable – the complex density matrix or complex molecular orbital coefficient file.
>     * `FALSE`: Don’t read the complex density matrix or complex molecular orbital coefficient file when determining Mulliken charges, multipole moments and orbital energies for CAP-HF calculations.
> * **Recommendation**: Set to ‘TRUE’ for CAP-HF calculations.

### `SKIP_OLD_SCFMAN`

> **Skips only old SCF drivers**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Skip only old SCF drivers
>     * `FALSE`: Do not skip old SCF drivers
> * **Recommendation**: When performing CAP calculations on temporary anions, it may help setting this variable to FALSE.

### `CS_SCF_FINAL_PRINT`

> **Controls level of output from CAP-SCF procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: Print direct breakdown of CAP-SCF energy.
>     * `2`: Print breakdown of CAP-SCF energy based on the complex coefficient matrix. Also required if the options below are requested.
>     * `3`: Level 2 plus diagonal elements of complex orbital energy matrix, F . Triggered by Level 2.
>     * `4`: Level 2 plus diagonal elements of complex kinetic energy matrix, T . Triggered by Level 2
>     * `5`: Level 2 plus diagonal elements of complex electron-nuclear Coulomb potential energy matrix, V . Triggered by Level 2.
>     * `6`: Level 2 plus diagonal elements of CAP matrix, W . Triggered by Level 2.
>     * `7`: Level 2 plus diagonal elements of total complex one-electron energy matrix, $\textbf{T}+\textbf{V}+\textbf{W}$ . Triggered by Level 2.
>     * `8`: Level 2 plus diagonal elements of total complex electronic energy matrix, $\textbf{T}+\textbf{V}+\textbf{W}+\textbf{F}$ . Triggered by Level 2.
>     * `9`: Level 2 to 8. Triggered by Level 2.
> * **Recommendation**: Level 1 is usually enough. Values for this $rem variable are transformed first into a set of distinct values; thus, for example, “1111” is equivalent to “1” and “28224” is equivalent to “248”. To request Levels 3–9, please remember to request Level 2 as well.

???+ example "Example 9.9.49: CAP-HF single point job for N ${}_{2}^{-}$ , with energy decomposition of the complex energy. Basis set is cc-PVTZ+3p."
    ```qchem
    $molecule
    -1 2
    N
    N   1  1.098
    $end
    
    $rem
    ¯JOBTYPE¯¯SP
    ¯METHOD¯¯¯hf
    ¯BASIS¯¯¯general
    ¯GEN_SCFMAN¯¯TRUE
    ¯SKIP_OLD_SCFMAN¯true¯! skip old scfman drivers
    ¯SCF_CONVERGENCE¯8
    ¯SCF_GUESS¯¯CORE
    ¯COMPLEX_CCMAN¯¯TRUE
    ¯UNRESTRICTED¯¯TRUE
    ¯CS_STRICT¯¯TRUE¯! Determine orbital energies and props. using the complex density matrix/complex MO coefficients
    ¯CS_SCF_FINAL_PRINT¯1111¯! Print summary of energy decomposition
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1
    ¯CAP_TYPE ¯¯1
    ¯CAP_ETA ¯¯420
    ¯CAP_X ¯¯¯3535
    ¯CAP_Y ¯¯¯3535
    ¯CAP_Z ¯¯¯8102
    $end
    
    $basis
    N     0
    S    7   1.00
      11420.                     0.00052898
       1712.                     0.00409115
        389.3                    0.02101161
        110.0                    0.08163835
         35.57                   0.23564992
         12.54                   0.43792615
          4.644                  0.35006007
    S    7   1.00
      11420.                     0.00000185
       1712.                     0.00000699
        110.0                   -0.00073647
         35.57                  -0.00718168
         12.54                  -0.04679022
          4.644                 -0.12512392
          0.5118                 0.78627029
    S    1   1.00
          1.293                  1.000000
    S    1   1.00
          0.1787                 1.000000
    P    3   1.00
         26.63                   0.014670
          5.948                  0.091764
          1.742                  0.298683
    P    1   1.00
          0.5550                 1.000000
    P    1   1.00
          0.1725                 1.000000
    D    1   1.00
          1.654                  1.000000
    D    1   1.00
          0.469                  1.000000
    F    1   1.00
          1.093                  1.000000
    ¯P    1   1.00
    ¯¯0.08625       1.000000
          ¯P    1   1.00
          ¯¯0.043125      1.000000
          ¯P    1   1.00
          ¯¯0.0215625     1.000000
    ****
    $end
    ```

???+ example "Example 9.9.50: CAP-AIMD simulation for N ${}_{2}^{-}$ . Basis set is cc-PVTZ+3p."
    ```qchem
    $molecule
    -1 2
    N
    N   1  1.098
    $end
    
    
    $rem
     JOBTYPE¯¯AIMD
     METHOD¯¯¯HF
     BASIS¯¯¯GENERAL
     GEN_SCFMAN¯¯TRUE
     SKIP_OLD_SCFMAN¯TRUE¯¯! Skip old scfman drivers
     SCF_CONVERGENCE¯8
     MAX_SCF_CYCLES¯¯200
     SCF_GUESS¯¯CORE
     COMPLEX_CCMAN¯¯TRUE¯¯! Activate Complex CCMAN. Necessary for CAP calculations.
     UNRESTRICTED¯¯TRUE
     TIME_STEP¯¯10
     AIMD_STEPS¯¯200
     FOCK_EXTRAP_ORDER      0
     FOCK_EXTRAP_POINTS     0
     AIMD_MOMENTS¯¯1
     AIMD_TEMP¯¯300
     AIMD_INIT_VELOC¯THERMAL
     CAP_AIMD_SWITCH¯TRUE¯¯! Set CAP_ETA=0 when extra electron is bound
     CS_STRICT¯¯TRUE¯¯! Determine orbital energies and props. using the complex density. matrix/complex MO coefficients
     INTEGRAL_SYMMETRY      FALSE
     POINT_GROUP_SYMMETRY   FALSE
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1¯¯! Do complex HF
    ¯CAP_TYPE ¯¯1¯¯! CAP type is cuboid.
    ¯CAP_ETA ¯¯420
    ¯CAP_X ¯¯¯3535
    ¯CAP_Y ¯¯¯3535
    ¯CAP_Z ¯¯¯8102
    $end
    
    $basis
    N     0
    S    7   1.00
      11420.                     0.00052898
       1712.                     0.00409115
        389.3                    0.02101161
        110.0                    0.08163835
         35.57                   0.23564992
         12.54                   0.43792615
          4.644                  0.35006007
    S    7   1.00
      11420.                     0.00000185
       1712.                     0.00000699
        110.0                   -0.00073647
         35.57                  -0.00718168
         12.54                  -0.04679022
          4.644                 -0.12512392
          0.5118                 0.78627029
    S    1   1.00
          1.293                  1.000000
    S    1   1.00
          0.1787                 1.000000
    P    3   1.00
         26.63                   0.014670
          5.948                  0.091764
          1.742                  0.298683
    P    1   1.00
          0.5550                 1.000000
    P    1   1.00
          0.1725                 1.000000
    D    1   1.00
          1.654                  1.000000
    D    1   1.00
          0.469                  1.000000
    F    1   1.00
          1.093                  1.000000
    ¯P    1   1.00
    ¯¯0.08625       1.000000
          ¯P    1   1.00
          ¯¯0.043125      1.000000
          ¯P    1   1.00
          ¯¯0.0215625     1.000000
    ****
    $end
    ```

???+ example "Example 9.9.51: CAP-AIMD simulation for C ${}_{2}$ H ${}_{4}^{-}$ . Basis set is cc-PVTZ+3p(C). A CAP single point calculation is first done. The CAP-SCF solution is then read as the initial guess for the CAP-AIMD part. This procedure is useful, for example, when one wants to use the MOM_START option (§ 4.5.14 ) to preserve orbital occupation in the course of the simulation."
    ```qchem
    $molecule
    -1 2
    C    0.0000   0.0000   0.0000
    H    0.0000   0.0000   1.0742
    H    0.9596   0.0000  -0.4829
    C   -1.1191   0.0000  -0.6897
    H   -2.0787   0.0000  -0.2068
    H   -1.1191   0.0000  -1.7639
    $end
    
    
    $rem
     METHOD¯¯¯HF
     BASIS¯¯¯GENERAL
     GEN_SCFMAN¯¯TRUE
     SKIP_OLD_SCFMAN¯TRUE¯! skip old scfman drivers
     SCF_CONVERGENCE¯8
     SCF_GUESS¯¯CORE
     COMPLEX_CCMAN¯¯TRUE
     UNRESTRICTED¯¯TRUE
     CS_STRICT¯¯TRUE¯! Determine orbital energies and props. using the complex density matrix/complex MO coefficients
     CS_SCF_FINAL_PRINT¯1111¯! Print summary of energy decomposition
     INTEGRAL_SYMMETRY ¯FALSE
     POINT_GROUP_SYMMETRY¯FALSE
    $end
    
    $complex_ccman
     CS_HF ¯¯¯1
     CAP_TYPE ¯¯1
     CAP_ETA ¯¯230
     CAP_X ¯¯¯4360
     CAP_Y ¯¯¯2680
     CAP_Z ¯¯¯4360
    $end
    
    $basis
    H¯0
    cc-pvtz
    ****
    C     0
    S    8   1.00
       8236.0000000              0.0005310
       1235.0000000              0.0041080
        280.8000000              0.0210870
         79.2700000              0.0818530
         25.5900000              0.2348170
          8.9970000              0.4344010
          3.3190000              0.3461290
          0.3643000             -0.0089830
    S    8   1.00
       8236.0000000             -0.0001130
       1235.0000000             -0.0008780
        280.8000000             -0.0045400
         79.2700000             -0.0181330
         25.5900000             -0.0557600
          8.9970000             -0.1268950
          3.3190000             -0.1703520
          0.3643000              0.5986840
    S    1   1.00
         11.8760000              1.0000000
    S    1   1.00
          4.2920000              1.0000000
    S    1   1.00
          0.9059000              1.0000000
    S    1   1.00
          0.1285000              1.0000000
    P    3   1.00
         18.7100000              0.0140310
          4.1330000              0.0868660
          1.2000000              0.2902160
    P    1   1.00
         33.1900000              1.0000000
    P    1   1.00
          8.7780000              1.0000000
    P    1   1.00
          0.3827000              1.0000000
    P    1   1.00
          0.1209000              1.0000000
    D    1   1.00
         14.8390000              1.0000000
    D    1   1.00
          1.0970000              1.0000000
    D    1   1.00
          0.3180000              1.0000000
    F    1   1.00
          0.7610000              1.0000000
          P¯1¯¯1.00
          ¯¯0.06045¯1.00
          P¯1¯¯1.00
          ¯¯0.030225¯1.00
          P¯1¯¯1.00
          ¯¯0.0151125¯1.00
    ****
    $end
    
    
    @@@
    
    
    $molecule
     READ
    $end
    
    $velocity
    3.6095e-05   4.1623e-06   2.3754e-05
    -9.7386e-04  -1.4552e-05  -1.2310e-03
    -2.8737e-04   1.2165e-04   2.9068e-04
    3.3619e-05  -1.3939e-04   1.0849e-04
    6.4312e-04   2.0187e-04  -4.2066e-04
    -2.1196e-04   1.3012e-03  -2.1364e-04
    $end
    
    $rem
    ¯JOBTYPE¯¯AIMD
    ¯METHOD¯¯¯HF
    ¯BASIS¯¯¯GENERAL
    ¯GEN_SCFMAN¯¯TRUE
    ¯SKIP_OLD_SCFMAN¯TRUE
    ¯SCF_CONVERGENCE¯8
    ¯MAX_SCF_CYCLES¯¯3000
    integral_symmetry FALSE
    point_group_symmetry False
    ¯SCF_GUESS¯¯READ
    ¯COMPLEX_CCMAN¯¯TRUE
    ¯UNRESTRICTED¯¯TRUE
    ¯MOM_START¯¯1
    ¯MOM_METHOD¯¯MOM
    ¯TIME_STEP¯¯2
    ¯AIMD_STEPS¯¯200
       ¯FOCK_EXTRAP_ORDER      0
       ¯FOCK_EXTRAP_POINTS     0
      ¯AIMD_MOMENTS¯¯1
      ¯AIMD_PRINT¯¯2¯! Print Mulliken charges and dipole moments at each step
    ¯CS_STRICT¯¯TRUE
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1
    ¯CAP_TYPE ¯¯1
    ¯CAP_ETA ¯¯230
    ¯CAP_X ¯¯¯4360
    ¯CAP_Y ¯¯¯2680
    ¯CAP_Z ¯¯¯4360
    $end
    
    $basis
    H¯0
    cc-pvtz
    ****
    C     0
    S    8   1.00
       8236.0000000              0.0005310
       1235.0000000              0.0041080
        280.8000000              0.0210870
         79.2700000              0.0818530
         25.5900000              0.2348170
          8.9970000              0.4344010
          3.3190000              0.3461290
          0.3643000             -0.0089830
    S    8   1.00
       8236.0000000             -0.0001130
       1235.0000000             -0.0008780
        280.8000000             -0.0045400
         79.2700000             -0.0181330
         25.5900000             -0.0557600
          8.9970000             -0.1268950
          3.3190000             -0.1703520
          0.3643000              0.5986840
    S    1   1.00
         11.8760000              1.0000000
    S    1   1.00
          4.2920000              1.0000000
    S    1   1.00
          0.9059000              1.0000000
    S    1   1.00
          0.1285000              1.0000000
    P    3   1.00
         18.7100000              0.0140310
          4.1330000              0.0868660
          1.2000000              0.2902160
    P    1   1.00
         33.1900000              1.0000000
    P    1   1.00
          8.7780000              1.0000000
    P    1   1.00
          0.3827000              1.0000000
    P    1   1.00
          0.1209000              1.0000000
    D    1   1.00
         14.8390000              1.0000000
    D    1   1.00
          1.0970000              1.0000000
    D    1   1.00
          0.3180000              1.0000000
    F    1   1.00
          0.7610000              1.0000000
          P¯1¯¯1.00
          ¯¯0.06045¯1.00
          P¯1¯¯1.00
          ¯¯0.030225¯1.00
          P¯1¯¯1.00
          ¯¯0.0151125¯1.00
    ****
    $end
    ```
