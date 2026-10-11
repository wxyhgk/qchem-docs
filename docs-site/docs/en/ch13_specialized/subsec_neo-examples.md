---
title: "13.5.6 Examples"
---

## 13.5.6 Examples

(July 4, 2026)

???+ example "Example 13.7: Input for the NEO-HF calculation on H ${}_{2}$ O molecule with the second proton treated quantum mechanically. The electronic basis set is cc-pVDZ and the protonic is an uncontracted 2s2p2d basis set with exponents 4.0 and 8.0."
    ```qchem
    $molecule
       0 1
       H   -3.5008791    1.2736107    0.7596000
       O   -3.9840791    1.3301107   -0.0574000
       H   -4.9109791    1.2967107    0.1521000
    $end
    
    $rem
       METHOD   hf
       BASIS    cc-pvdz
       NEO      true
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       8.0 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       8.0 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       8.0 1.0
    ****
    $end
    ```

???+ example "Example 13.8: Input for the NEO-DFT/epc17-2 calculation of CH ${}_{2}$ O molecule treating both protons quantum mechanically and using simultaneous DIIS
algorithm to perform NEO-SCF. The electronic basis set is cc-pVDZ and the protonic basis set is an uncontracted 1s1p basis set with exponents
4.0 and 4.0. A maximum of 10 previous Fock matrices is used to form the next guess in interpolation/extrapolation, and the NEO wave function
is considered converged when all three criteria are met (all in atomic units): (1) the largest element of the electronic error vector is below the
cutoff threshold of $10^{-8}$ , (2) the largest element of the protonic error vector is below the cutoff threshold of $10^{-7}$ , and (3) the energy
difference between two consecutive steps is below $10^{-8}$ ."
    ```qchem
    $molecule
    0 1
      C        0.000000    0.000000    0.000000
      O        0.000000    0.000000    1.220000
      H        0.935307    0.0000000  -0.5400000
      H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
       JOBTYPE              SP
       SYM_IGNORE           TRUE
       INPUT_BOHR           FALSE
       BASIS                cc-pvdz
       NEO                  TRUE
       METHOD               pbe0
       xc_grid = 000099000302
       NEO_EPC              epc172
       NEO_N_SCF_CONVERGENCE = 7
       SCF_CONVERGENCE = 8
       NEO_E_CONV = 8
       SCF_ALGORITHM        DIIS
       NEO_SIMULTANEOUS_SCF TRUE
       NEO_STEPWISE_SCF_STEPS = 2
       DIIS_SUBSPACE_SIZE = 10
       DIIS_ERR_RMS         FALSE
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.9: Input for the NEO-DFT/epc17-2 geometry optimization calculation of all centers on CH ${}_{2}$ O molecule with both protons treated quantum
mechanically. The electronic exchange-correlation functional is PBE0. The electronic basis set is STO-3G and the protonic is an uncontracted
1s1p basis set with exponents 4.0. This calculation utilizes DFT grid with 99 radial and 302 spherical quadrature points along with the DIIS
algorithm."
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000    0.000000
       O     0.000000    0.000000    1.220000
       H     0.935307    0.000000   -0.540000
       H    -0.935307    0.000000   -0.540000
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            pbe0
       BASIS             sto-3g
       NEO               true
       NEO_EPC           epc172
    point_group_symmetry False
       SCF_CONVERGENCE   11
       MAX_SCF_CYCLES    100
       SCF_ALGORITHM     diis
       XC_GRID           000099000302
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.10: Input for the NEO-DFT/epc19 geometry optimization calculation of the NEO center only on open-shell OH radical molecule with a proton treated
quantum mechanically. The electronic exchange-correlation functional is PBE0. The electronic basis set is 6-31G and the protonic is an uncontracted
1s1p basis set with exponents 4.0. This calculation utilizes DFT grid with 99 radial and 230 spherical quadrature points along with the DIIS algorithm."
    ```qchem
    $molecule
       0 2
       O    -4.511414   1.264878   0.000000
       H    -2.739325   1.866123   0.000000
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            pbe0
       BASIS             6-31g
       UNRESTRICTED      true
       INPUT_BOHR        true
       NEO               true
    point_group_symmetry False
       SCF_CONVERGENCE   6
       MAX_SCF_CYCLES    100
       SCF_ALGORITHM     diis
       NEO_EPC           epc19
       XC_GRID           000099000230
    $end
    
    $opt
       FIXED
       1 XYZ
       ENDFIXED
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.11: Input for a NEO-MSDFT calculation on FHF ${}^{-}$ with a fixed F–F distance of 2.70 Å.
The proton in between the two F atoms is quantized and the proton basis function centers are optimized on the NEO-MSDFT ground state.
The electronic basis set is STO-3G, and the protonic basis set is an uncontracted 1s1p basis set with exponents 4.0.
The electronic exchange-correlation functional is B3LYP, and the electron-proton correlation functional is epc17-2.
The second basis function center for the quantum proton is input as a ghost center."
    ```qchem
    $molecule
    -1  1
    F      0.00000000     0.00000000    -1.35000000
    F      0.00000000     0.00000000     1.35000000
    H      0.00000000     0.00000000    -0.25220000
    @H     0.00000000     0.00000000     0.25220000
    $end
    
    $rem
    jobtype = opt
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    max_scf_cycles 500
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE 6
    NEO_E_CONV = 6
    SCF_ALGORITHM gdm
    $end
    
    $OPT
    FIXED
    1 XYZ
    2 XYZ
    ENDFIXED
    $END
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.12: Input for a NEO-MSDFT calculation on a fixed average reactant-product structure of the formic acid dimer with a C–C distance of
3.86 Å, where both transferring protons are quantized. The electronic basis set is STO-3G, and the protonic basis set is an uncontracted
1s1p basis set with exponents 4.0. The electronic exchange-correlation functional is B3LYP, and the electron-proton correlation functional is
epc17-2. Only the two trans states are included in the adiabatic state expansion (note the spaces between the ones and zeros of the $neo_msdft_diabat_control section). The second center for each quantum proton is input as a ghost center. Proton density plotting for both the ground and
first excited state has been enabled."
    ```qchem
    $molecule
    0  1
    H        -3.0310572606    0.0000000000    0.0000000000
    H        -0.4438453003    1.0873992328    0.0000000000
    @H        0.4438452993    1.0873992291    0.0000000000
    O        -1.3616953972   -1.1310228162    0.0000000000
    O        -1.3616953971    1.1310228163    0.0000000000
    C        -1.9296657251    0.0000000000    0.0000000000
    H         3.0310572606    0.0000000000    0.0000000000
    H         0.4438452993   -1.0873992291    0.0000000000
    @H       -0.4438453003   -1.0873992328    0.0000000000
    O         1.3616953972    1.1310228162    0.0000000000
    O         1.3616953971   -1.1310228163    0.0000000000
    C         1.9296657251    0.0000000000    0.0000000000
    $end
    
    $rem
    jobtype = sp
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE = 6
    NEO_E_CONV = 6
    max_scf_cycles 500
    SCF_ALGORITHM GDM
    $end
    
    $neo_msdft
    denplt = 1
    $end
    
    $neo_msdft_diabat_control
    1 0 1 0
    0 1 0 1
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    8
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H   9
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.13: Input for a NEO-MSDFT calculation on a protonated water dimer with a fixed O–O distance of 2.80 Å,
where all protons in the system are quantized, but only the proton between the two oxygen atoms is treated as transferring.
The two centers for the transferring proton are written consecutively in the $molecule section, with the first one written as an H
atom center and the second one is written as a ghost H atom center. The other centers do not have corresponding ghost centers
and are therefore not recognized as being transferring. The electronic basis set is STO-3G, and the protonic basis set is an
uncontracted 1s1p basis set with exponents 4.0. The electronic exchange-correlation functional is B3LYP, and the electron-proton
correlation functional is epc17-2."
    ```qchem
    $molecule
    1  1
    O      -1.4000000000     0.0000000000     0.0000000000
    O       1.4000000000     0.0000000000     0.0000000000
    H      -0.3000000000     0.0000000000     0.0000000000
    @H      0.3000000000     0.0000000000     0.0000000000
    H       1.6600000000     0.7500000000    -0.5500000000
    H       1.6600000000    -0.7500000000    -0.5500000000
    H      -1.6600000000     0.7500000000     0.5500000000
    H      -1.6600000000    -0.7500000000     0.5500000000
    $end
    
    $rem
    jobtype = sp
    input_bohr = false
    method = b3lyp
    basis = sto-3g
    neo = true
    neo_epc = epc172
    neo_msdft = 1
    sym_ignore = 1
    scf_convergence 6
    NEO_N_SCF_CONVERGENCE = 6
    NEO_E_CONV = 6
    max_scf_cycles 500
    SCF_ALGORITHM GDM
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    5
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    6
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    7
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    8
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.14: Input for the NEO-DFT/epc17-2 geometry optimization calculation of a CH ${}_{2}$ O molecule in C-PCM water. A van der Waals surface
is constructed around the fixed, classical nuclear point charge positions and the nuclear basis function
center positions of the two quantum hydrogens. Here, the Bondi radii for hydrogen is used in the construction
of the spherical cavity surrounding the delocalized proton densities, but the user has the option to specify
a custom-defined atomic radii in a $van_der_waals input section. The entire cavity is scaled by a factor of $\alpha_{\text{vdW}}=1.2$ ,
and is then discretized via the SwiG approach."
    ```qchem
    $molecule
    0 1
      C        0.000000    0.000000    0.000000
      O        0.000000    0.000000    1.220000
      H        0.935307    0.0000000  -0.5400000
      H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    point_group_symmetry False
       JOBTYPE              OPT
       INPUT_BOHR           FALSE
       BASIS                sto-3g
       NEO                  TRUE
       METHOD               pbe0
       xc_grid = 000099000302
       NEO_EPC              epc172
       SCF_CONVERGENCE = 8
       NEO_E_CONV = 8
       SCF_ALGORITHM        GDM
       SOLVENT_METHOD       PCM
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $pcm
       Theory               CPCM
       Method               SWIG
       Solver               INVERSION
       HeavyPoints          194
       HPoints              194
       Radii                Bondi
       vdwScale             1.2
    $end
    
    $solvent
      Dielectric   78.39
    $end
    ```

???+ example "Example 13.15: Input for the NEO-DFT/epc17-2 geometry optimization calculation of a Au ${}_{2}$ H, C ${}_{\infty\text{v}}$ molecule utilizing
the fit-LANL2DZ effective core potential for the gold atoms."
    ```qchem
    $molecule
    1 1
      Au       0.000000    0.000000    2.222000
      Au       0.000000    0.000000    5.502000
      H        0.000000    0.000000    3.842000
    $end
    
    $rem
       JOBTYPE                 OPT
       SYM_IGNORE             TRUE
       INPUT_BOHR            FALSE
       BASIS                 mixed
       NEO                    TRUE
       METHOD                b3lyp
       xc_grid      = 000099000302
       NEO_EPC              epc172
       NEO_N_SCF_CONVERGENCE   = 8
       SCF_CONVERGENCE         = 8
       NEO_E_CONV              = 8
       SCF_ALGORITHM           GDM
       ECP             fit-LANL2DZ
    $end
    
    $basis
    Au 1
    LANL2DZ
    ****
    Au 2
    LANL2DZ
    ****
    H 3
    def2-qzvp
    ****
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       5.973 1.0
    S    1    1.000000
       10.645 1.0
    S    1    1.000000
       17.943 1.0
    S    1    1.000000
       28.950 1.0
    P    1    1.000000
       7.604 1.0
    P    1    1.000000
       14.701 1.0
    P    1    1.000000
       23.308 1.0
    D    1    1.000000
       9.011 1.0
    D    1    1.000000
       19.787 1.0
    F    1    1.000000
       10.914 1.0
    F    1    1.000000
       20.985 1.0
    ****
    $end
    ```

???+ example "Example 13.16: Input for NEO-HF analytic Hessian calculation on HCN molecule with a proton treated quantum mechanically.
The electronic basis set is STO-3G and the protonic basis is 1s1p with exponents 4.0."
    ```qchem
    $molecule
    0 1
      C         0.0000000000    0.0000000000    0.9684140792
      N         0.0000000000    0.0000000000   -1.2085828830
      H         0.0000000000    0.0000000000    2.9046475823
    $end
    
    $rem
    jobtyp = freq
    input_bohr = true
    point_group_symmetry = False
    method = hf
    basis = sto-3g
    neo = true
    SCF_ALGORITHM = gdm
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.17: Input to simulate the intramolecular proton transfer in malonaldehyde on the NEO-DFT vibronic ground-state surface with NEO-BOMD. Note the inclusion of the $neo_gs_dynamics , $neo_gs_dynamics_donor_acceptor_indices , and $neo_gs_dynamics_velocities input sections. Also note that the protonic basis function center, the first entry of the $molecule section, has zero velocity in the $neo_gs_dynamics_velocities input section."
    ```qchem
    $molecule
    0 1
    H        -0.3982276484    4.7093371192    0.0000000000
    C        -2.2965024834    1.7761906527    0.0000000000
    C        -0.0778296218    0.4606600999    0.0000000000
    C         2.2683699385    1.8502803018    0.0000000000
    O        -2.4548505732    4.2439921132    0.0000000000
    O         2.3773400124    4.1728718529    0.0000000000
    H        -4.1386563233    0.8241552831    0.0000000000
    H        -0.0809127358   -1.5993342589    0.0000000000
    H         4.0571330701    0.7432112784    0.0000000000
    $end
    
    $rem
    NEO_BOMD                    TRUE
    SYM_IGNORE                  TRUE
    INPUT_BOHR                  TRUE
    METHOD                      b3lyp
    BASIS                       sto-3g
    SCF_ALGORITHM               DIIS
    MAX_SCF_CYCLES              1000
    NEO                         TRUE
    NEO_EPC                     EPC172
    NEO_PURECART                1111
    NEO_VPP                     FALSE
    NEO_SIMULTANEOUS_SCF        TRUE
    NEO_VPP                     FALSE
    NEO_E_CONV                  5
    NEO_N_SCF_CONVERGENCE       5
    SCF_CONVERGENCE             5
    $end
    
    $neo_gs_dynamics
    nsteps 1
    dt 0.2
    $end
    
    $neo_gs_dynamics_donor_acceptor_indices
    5 6
    $end
    
    $neo_gs_dynamics_velocities
      0.0000000000e+00        0.0000000000e+00        0.0000000000e+00
      2.9512420606e-05        7.9677231137e-05        0.0000000000e+00
      4.9086468803e-05       -1.2437450767e-04        0.0000000000e+00
     -1.2941243817e-04       -1.0648277856e-04        0.0000000000e+00
      3.6818304686e-04       -5.1390359408e-05        0.0000000000e+00
     -3.2247267387e-04        2.5782796687e-05        0.0000000000e+00
     -1.9003838357e-05        1.2271678408e-04        0.0000000000e+00
      2.9746441198e-05       -1.2106793256e-04        0.0000000000e+00
     -5.6394270736e-06        1.7513876629e-04        0.0000000000e+00
    $end
    
    $neo_basis
    H    1
    S   1   1.00
         4.0                  1.0
    P   1   1.00
         4.0                  1.0
    ****
    $end
    ```

???+ example "Example 13.18: Input to simulate the intramolecular proton transfer in malonaldehyde on the NEO-DFT extended vibronic ground-state surface with NEO-ELMD(4). Note the inclusion of the $neo_gs_dynamics , $neo_gs_dynamics_donor_acceptor_indices , and $neo_gs_dynamics_velocities input sections. Also note that the protonic basis function center, the first entry of the $molecule section, has zero velocity in the $neo_gs_dynamics_velocities input section."
    ```qchem
    $molecule
    0 1
    H        -0.3982276484    4.7093371192    0.0000000000
    C        -2.2965024834    1.7761906527    0.0000000000
    C        -0.0778296218    0.4606600999    0.0000000000
    C         2.2683699385    1.8502803018    0.0000000000
    O        -2.4548505732    4.2439921132    0.0000000000
    O         2.3773400124    4.1728718529    0.0000000000
    H        -4.1386563233    0.8241552831    0.0000000000
    H        -0.0809127358   -1.5993342589    0.0000000000
    H         4.0571330701    0.7432112784    0.0000000000
    $end
    
    $rem
    NEO_ELMD                    TRUE
    SYM_IGNORE                  TRUE
    INPUT_BOHR                  TRUE
    METHOD                      b3lyp
    BASIS                       sto-3g
    SCF_ALGORITHM               DIIS
    MAX_SCF_CYCLES              1000
    NEO                         TRUE
    NEO_EPC                     EPC172
    NEO_PURECART                1111
    NEO_VPP                     FALSE
    NEO_SIMULTANEOUS_SCF        TRUE
    NEO_VPP                     FALSE
    NEO_E_CONV                  5
    NEO_N_SCF_CONVERGENCE       5
    SCF_CONVERGENCE             5
    $end
    
    $neo_gs_dynamics
    nsteps 10
    dt 1.0
    ASPC 1
    ASPC_NDENMATS 4
    $end
    
    $neo_gs_dynamics_donor_acceptor_indices
    5 6
    $end
    
    $neo_gs_dynamics_velocities
      0.0000000000e+00        0.0000000000e+00        0.0000000000e+00
      2.9512420606e-05        7.9677231137e-05        0.0000000000e+00
      4.9086468803e-05       -1.2437450767e-04        0.0000000000e+00
     -1.2941243817e-04       -1.0648277856e-04        0.0000000000e+00
      3.6818304686e-04       -5.1390359408e-05        0.0000000000e+00
     -3.2247267387e-04        2.5782796687e-05        0.0000000000e+00
     -1.9003838357e-05        1.2271678408e-04        0.0000000000e+00
      2.9746441198e-05       -1.2106793256e-04        0.0000000000e+00
     -5.6394270736e-06        1.7513876629e-04        0.0000000000e+00
    $end
    
    $neo_basis
    H    1
    S   1   1.00
         4.0                  1.0
    P   1   1.00
         4.0                  1.0
    ****
    $end
    ```

???+ example "Example 13.19: Input for NEO-HF(V) on HCN molecule with a proton treated quantum mechanically. The electronic basis set is STO-3G and the protonic
basis is 1s1p with exponents 4.0."
    ```qchem
    $molecule
    0 1
      C         0.0000000000    0.0000000000    0.9684140792
      N         0.0000000000    0.0000000000   -1.2085828830
      H         0.0000000000    0.0000000000    2.9046475823
    $end
    
    $rem
    jobtyp = freq
    input_bohr = true
    point_group_symmetry = False
    method = hf
    SCF_ALGORITHM = gdm
    basis = sto-3g
    neo = true
    neo_scfv = 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.20: Input for CNEO-DFT analytic Hessian calculation on HCN molecule with a proton treated quantum mechanically.
The electronic basis set is STO-3G, and the protonic basis set is an uncontracted 1s1p basis set with exponents 4.0.
The electronic exchange-correlation functional is BLYP, and the electron-proton correlation functional is epc17-2."
    ```qchem
    $molecule
    0 1
    H    0.000000    0.000000   -0.013880
    C    0.000000    0.000000    1.103384
    N    0.000000    0.000000    2.310496
    $end
    
    $rem
    jobtype     freq
    sym_ignore  true
    method      blyp
    basis       sto-3g
    neo         true
    neo_epc     epc172
    cneo        true
    $end
    
    $neo_basis
    H    1
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.21: Input for NEO-DFT energy calculation on CH ${}_{2}$ O molecule with the two protons treated quantum mechanically
using the nuclear Hartree product approximation.
The electronic basis set is STO-3G, and the protonic basis set is an uncontracted 1s1p basis set with exponents 4.0.
The electronic exchange-correlation functional is BLYP, and the electron-proton correlation functional is epc17-2."
    ```qchem
    $molecule
    0 1
    C        0.000000    0.000000    0.000000
    O        0.000000    0.000000    1.220000
    H        0.935307    0.000000   -0.540000
    H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    jobtype         sp
    sym_ignore      true
    scf_algorithm   gdm
    method          blyp
    basis           sto-3g
    neo             true
    neo_epc         epc172
    neo_n_hartree_prod     true
    neo_n_scf_convergence  8
    scf_convergence        8
    neo_e_conv             8
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.22: Input for the LR-NEO-TDDFT/epc19 calculation on CH ${}_{2}$ O molecule (both protons treated quantum mechanically) of the first five roots
obtained with the Davidson algorithm. The electronic exchange-correlation functional is PBE0. The electronic basis set is STO-3G and the
protonic is an uncontracted 1s1p basis set with exponents 4.0. This calculation utilizes DFT grid with 99 radial and 302 spherical quadrature points."
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000    0.000000
       O     0.000000    0.000000    1.220000
       H     0.935307    0.000000   -0.540000
       H    -0.935307    0.000000   -0.540000
    $end
    
    $rem
       METHOD            pbe0
       BASIS             sto-3g
       THRESH            14
       XC_GRID           000099000302
       S2THRESH          12
       NEO               true
       NEO_EPC           epc172
       SET_ROOTS         5
       RPA               true
       SCF_CONVERGENCE   12
       NEO_E_CONV        12
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.23: Input for the LR-NEO-TDHF calculation on the FDF ${}^{-}$ molecule treating quantum nuclei as deuterium and employing the NO_VPP option.
The electronic basis set is cc-pVDZ and the protonic is an uncontracted even-tempered 8s8p basis set."
    ```qchem
    $molecule
       -1 1
       F   0.000000   0.000000   -1.122987
       F   0.000000   0.000000    1.122987
       H   0.000000   0.000000    0.000000
    $end
    
    $rem
       METHOD            hf
       BASIS             cc-pvdz
       NEO               true
       SCF_ALGORITHM     GDM
       RPA               true
       CIS_N_ROOTS       100
       THRESH            14
       S2THRESH          12
       SCF_CONVERGENCE   11
       MAX_SCF_CYCLES    300
       NEO_VPP           0
       NEO_ISOTOPE       2
       NEO_E_CONV        11
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       2.828400 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.828400 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "Example 13.24: Input for the analytic LR-NEO-TDDFT gradient calculation on the CH ${}_{2}$ molecule with both protons treated quantum mechanically.
A total of four excited states are requested and the gradient is computed for the 3rd excited state. The electronic exchange-correlation
functional is CAM-B3LYP, and electron-proton correlation functional epc17-2 is used. The electronic basis set is STO-3G and the protonic
basis is 1s1p with exponents 4.0. This calculation utilizes DFT grid with 99 radial and 302 spherical quadrature points along with the GDM
algorithm."
    ```qchem
    $molecule
    0 3
    C  0.00000000000000e+00  0.00000000000000e+00 -5.63654429543699e-02
    H  1.81800983405161e+00  0.00000000000000e+00 -9.92269386019353e-01
    H -1.81800983405161e+00  0.00000000000000e+00 -9.92269386019353e-01
    $end
    
    $rem
    point_group_symmetry = false
    input_bohr           = true
    method               = cam-b3lyp
    basis                = sto-3g
    thresh               = 14
    s2thresh             = 12
    neo                  = true
    cis_n_roots          = 4
    rpa                  = true
    xc_grid              = 000099000302
    unrestricted         = 1
    neo_epc              = epc172
    scf_algorithm        = gdm
    cis_state_deriv      = 3
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.25: Input for LR-NEO-TDDFT geometry optimization on the C ${}_{2}$ H ${}_{2}$ molecule with both protons treated quantum mechanically.
A total of three excited states are requested and the geometry optimization is computed for the 1st excited state.
The electronic exchange-correlation functional is B3LYP, and electron-proton correlation functional epc17-2 is used.
The electronic basis set is STO-3G and the protonic basis is 1s1p with exponents 4.0. This calculation utilizes DFT grid with 99 radial
and 302 spherical quadrature points along with the GDM algorithm."
    ```qchem
    $molecule
    0 1
            C       0.4142076725     1.0563578037     0.0000000223
            C      -0.4142118956    -1.0563667882     0.0000000223
            H       1.1661939287     2.9673893099     0.0000000246
            H      -1.1661909474    -2.9673788285     0.0000000246
    $end
    
    $rem
    jobtype              = opt
    neo_set_opt          = true
    neo_epc              = epc172
    cis_state_deriv      = 1
    input_bohr           = true
    method               = b3lyp
    neo                  = true
    scf_algorithm        = gdm
    thresh               = 14
    s2thresh             = 12
    basis                = sto-3g
    rpa                  = true
    cis_n_roots          = 3
    xc_grid              = 000099000302
    point_group_symmetry = false
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    ```

???+ example "Example 13.26: Input for LR-NEO-TDDFT on the C ${}_{2}$ H ${}_{2}$ molecule with both protons treated quantum mechanically. A total of 12 excited states are requested.
Ground-state protonic and electronic densities are printed in the cube files. Protonic and electronic transition densities of the first and the second vibronic excitations with electronic dominant characters are also printed in the cube files.
The electronic exchange-correlation functional is B3LYP, and electron-proton correlation functional epc17-2 is used.
The electronic basis set is STO-3G and the protonic basis is 1s1p with exponents 4.0. This calculation utilizes DFT grid with 99 radial and
302 spherical quadrature points along with the GDM algorithm."
    ```qchem
    $molecule
    0 1
           C        -0.2315710674    1.2702261467    0.0000001295
           C         0.2315702809   -1.2702255666    0.0000001295
           H         1.2946585350    2.6676952886   -0.0000000923
           H        -1.2946589903   -2.6676943717   -0.0000000923
    $end
    
    $rem
    point_group_symmetry = False
    input_bohr = true
    method = b3lyp
    neo = true
    NEO_SET_ESTATE = 1
    SCF_ALGORITHM = gdm
    thresh = 14
    s2thresh = 12
    basis = sto-3g
    GEOM_OPT_MAX_CYCLES = 500
    rpa = true
    SET_ROOTS = 12
    xc_grid = 000099000302
    MAKE_CUBE_FILES = true
    plots = true
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $plots
    grid information to plot protonic and electronic ground state densities and transition densities for two eletronic dominant transitions
       100  -4.0 6.0
       100  -5.0 4.0
       100  -4.0 4.0
       0 1 2 0
       0
       0 1
    $end
    
    ```

???+ example "Example 13.27: Formate ion simulated with RT-NEO-TDHF and excited by a Gaussian impulse response from all three orthogonal directions, $x$ , $y$ , and $z$ ."
    ```qchem
    $molecule
    -1 1
    C   0.000000  0.000000  0.316833
    H   0.000000  0.000000  1.430087
    O   0.000000  1.135580 -0.208193
    O   0.000000 -1.135580 -0.208193
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = cc-pvtz
    METHOD                = hf
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    2
    S    1    1.000000
       5.973 1.0
    S    1    1.000000
       10.645 1.0
    S    1    1.000000
       17.943 1.0
    S    1    1.000000
       28.950 1.0
    P    1    1.000000
       7.604 1.0
    P    1    1.000000
       14.701 1.0
    P    1    1.000000
       23.308 1.0
    D    1    1.000000
       9.011 1.0
    D    1    1.000000
       19.787 1.0
    F    1    1.000000
       10.914 1.0
    F    1    1.000000
       20.985 1.0
    ****
    $end
    
    $neo_tdks
    METHOD              = realtime
    DT                  = 0.04
    MAXITER             = 20000
    FIELD_TYPE          = gaussian
    FIELD_AMP           = 0.02
    FIELD_PEAK          = 0.0
    FIELD_TAU           = 800.0
    FIELD_FREQUENCY     = 6.0
    FIELD_DIRECTION     = xyz
    FIELD_PARTICLE_TYPE = both
    $end
    ```

???+ example "Example 13.28: Excited-state intramolecular proton transfer in $o$ -hydroxylbenzaldehyde simulated with RT-NEO-TDDFT-Ehrenfest
utilzing the B3LYP electronic exchange-correlation functional and epc17-2 electron-proton correlation functional.
Two additional basis function centers are added along the proton transfer path, the total simulation time was
specified to be 19.35 fs, and an electronic HOMO to LUMO swap was performed to prepare the initial state."
    ```qchem
    $molecule
    0 1
    C  -1.310008  1.258755  0.000000
    C   0.019289  0.780580  0.000000
    C   0.322586 -0.621636  0.000000
    C  -0.761283 -1.465586  0.000000
    C  -2.125342 -0.985468  0.000000
    C  -2.398971  0.362640  0.000000
    O   1.008708  1.658363  0.000000
    C   1.725826 -1.062678  0.000000
    O   2.682115 -0.219090  0.000000
    H  -3.414260  0.733314  0.000000
    H  -0.596742 -2.537818  0.000000
    H  -2.926679 -1.713458  0.000000
    H  -1.459388  2.331114  0.000000
    H   1.924136 -2.138192  0.000000
    H   1.844187  1.135044  0.000000
    @H  2.042593  0.928022  0.000000
    @H  2.241000  0.721000  0.000000
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = cc-pvtz
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    15
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    H    16
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    H    17
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD                  = ehrenfest
    DT                      = 0.04
    MAXITER                 = 20000
    ELECTRONIC_HOMO_TO_LUMO = true
    $end
    ```

???+ example "Example 13.29: Ground-state intramolecular proton transfer in malonaldehyde simulated with BO-RT-NEO-TDDFT-Ehrenfest. Minimal
basis sets are employed as a proof of principle. Note the large time step of 4.2 atomic units is employed since the
electronic dynamics are no longer being propagated."
    ```qchem
    $molecule
    0 1
    O   0.000000 -1.300873  2.045662
    O   0.000000  1.290832  2.045662
    C   0.000000 -1.216031  0.759259
    C   0.000000  1.205990  0.759259
    C   0.000000 -0.005020  0.053344
    H   0.000000 -0.005020 -1.024823
    H   0.000000 -2.163146  0.218967
    H   0.000000  2.153105  0.218967
    H   0.000000 -0.301012  2.355420
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = sto-3g
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    $end
    
    $neo_basis
    H    9
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD  = bo-ehrenfest
    DT      = 4.2
    MAXITER = 1335
    $end
    ```

???+ example "Example 13.30: Ground-state intramolecular proton transfer in malonaldehyde simulated with BO-RT-NEO-TDDFT-Ehrenfest,
and utilizing the B3LYP-D3(0) empirical dispersion correction with custom parameters."
    ```qchem
    $molecule
    0 1
    O   0.000000 -1.300873  2.045662
    O   0.000000  1.290832  2.045662
    C   0.000000 -1.216031  0.759259
    C   0.000000  1.205990  0.759259
    C   0.000000 -0.005020  0.053344
    H   0.000000 -0.005020 -1.024823
    H   0.000000 -2.163146  0.218967
    H   0.000000  2.153105  0.218967
    H   0.000000 -0.301012  2.355420
    $end
    
    $rem
    NEO                   = true
    SYM_IGNORE            = true
    INPUT_BOHR            = false
    BASIS                 = sto-3g
    METHOD                = b3lyp
    SCF_CONVERGENCE       = 9
    NEO_N_SCF_CONVERGENCE = 9
    NEO_E_CONV            = 9
    NEO_EPC               = epc172
    NEO_VPP               = 0
    NEO_TDKS              = true
    DFT_D                 = D3_ZERO
    DFT_D3_S6             = 100000
    DFT_D3_RS6            = 126100
    DFT_D3_S8             = 170300
    DFT_D3_3BODY          = FALSE
    $end
    
    $neo_basis
    H    9
    S    1    1.000000
    4.0 1.0
    P    1    1.000000
    4.0 1.0
    ****
    $end
    
    $neo_tdks
    METHOD  = bo-ehrenfest
    DT      = 4.2
    MAXITER = 1335
    $end
    ```

???+ example "Example 13.31: Input for the NEO-RICCSD calculation on H ${}_{2}$ O molecule with the second proton treated quantum mechanically.
The electronic basis set is STO-3G and the protonic is an uncontracted 1s1p basis set with exponents 4.0.
The electronic auxiliary basis set is RIMP2-aug-cc-pVDZ and the protonic auxiliary basis set is an uncontracted even-tempered 8s8p basis set."
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    neo = true
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    NEO_RICCSD 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "Example 13.32: Input for the NEO-SCS ${}^{\prime}$ -MP2 calculation on CH ${}_{2}$ O molecule with the both protons treated quantum mechanically.
The electronic basis set is STO-3G and the protonic is an uncontracted 1s1p basis set with exponents 4.0.
The electronic auxiliary basis set is RIMP2-aug-cc-pVDZ and the protonic auxiliary basis set is an uncontracted even-tempered 8s8p basis set.
SCS scaling corresponds to $c_{\text{ss}}=0.33$ , $c_{\text{os}}=1.2$ and $c_{\text{ep}}=1.2$ ."
    ```qchem
    $molecule
    0 1
    C        0.000000    0.000000    0.000000
    O        0.000000    0.000000    1.220000
    H        0.935307    0.0000000  -0.5400000
    H       -0.935307    0.000000   -0.540000
    $end
    
    $rem
    method = hf
    basis = sto-3g
    neo = true
    sym_ignore = 1
    aux_basis = rimp2-cc-pVDZ
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_RIMP2 1
    SCS 1
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    H    4
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    H   4
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "Example 13.33: Input for the NEO-OOMP2 calculation on H ${}_{2}$ O molecule with the second proton treated quantum mechanically.
The electronic basis set is STO-3G and the protonic is an uncontracted 1s1p basis set with exponents 4.0.
The electronic auxiliary basis set is RIMP2-aug-cc-pVDZ and the protonic auxiliary basis set is an uncontracted even-tempered 8s8p basis set."
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    input_bohr = false
    method = hf
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    neo = true
    sym_ignore = 1
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_VPP 0
    NEO_RIMP2 2
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "Example 13.34: Input for the NEO-SOS ${}^{\prime}$ -OOMP2 calculation on H ${}_{2}$ O molecule with the second proton treated quantum mechanically.
The electronic basis set is STO-3G and the protonic is an uncontracted 1s1p basis set with exponents 4.0.
The electronic auxiliary basis set is RIMP2-aug-cc-pVDZ and the protonic auxiliary basis set is an uncontracted even-tempered 8s8p basis set.
SOS scaling corresponds to $c_{\text{ss}}=0.0$ and $c_{\text{os}}=1.2$ , with a custom value of $c_{\text{ep}}=1.5$ ."
    ```qchem
    $molecule
    0 1
    O          0.00000       -0.07579        0.00000
    H          0.86681        0.60144        0.00000
    H         -0.86681        0.60144        0.00000
    $end
    
    $rem
    input_bohr = false
    method = hf
    basis = sto-3g
    aux_basis = rimp2-aug-cc-pVDZ
    neo = true
    sym_ignore = 1
    scf_convergence 10
    max_scf_cycles 100
    SCF_ALGORITHM diis
    NEO_E_CONV 10
    NEO_VPP 0
    NEO_RIMP2 2
    SCS 2
    EP_FACTOR 1500000
    $end
    
    $neo_basis
    H    3
    S    1    1.000000
       4.0 1.0
    P    1    1.000000
       4.0 1.0
    ****
    $end
    
    $neo_aux_basis
    H   3
    S    1    1.000000
       2.8284 1.0
    S    1    1.000000
       4.0 1.0
    S    1    1.000000
       5.6569 1.0
    S    1    1.000000
       8.0 1.0
    S    1    1.000000
       11.3137 1.0
    S    1    1.000000
       16.0 1.0
    S    1    1.000000
       22.6274 1.0
    S    1    1.000000
       32.0 1.0
    P    1    1.000000
       2.8284 1.0
    P    1    1.000000
       4.0 1.0
    P    1    1.000000
       5.6569 1.0
    P    1    1.000000
       8.0 1.0
    P    1    1.000000
       11.3137 1.0
    P    1    1.000000
       16.0 1.0
    P    1    1.000000
       22.6274 1.0
    P    1    1.000000
       32.0 1.0
    D    1    1.000000
       2.8284 1.0
    D    1    1.000000
       4.0 1.0
    D    1    1.000000
       5.6569 1.0
    D    1    1.000000
       8.0 1.0
    D    1    1.000000
       11.3137 1.0
    D    1    1.000000
       16.0 1.0
    D    1    1.000000
       22.6274 1.0
    D    1    1.000000
       32.0 1.0
    ****
    $end
    ```

???+ example "Example 13.35: Input for the NEO-SOS ${}^{\prime}$ -CC2 excited-state calculation on the HCN molecule with the proton treated quantum mechanically.
The electronic basis set is STO-3G and the protonic is an uncontracted 1s1p basis set with exponents 4.0.
SOS scaling corresponds to $c_{\text{ss}}=0.0$ and $c_{\text{os}}=1.3$ , with ground-state electron–proton correlation scaling $c_{\text{ep}}=0.94$ and
excited-state electron–proton correlation scaling $c^{\text{ex}}_{\text{ep}}=1.0$ . Set to calculate the first six excited states, which correspond to protonic excitations."
    ```qchem
    $molecule
     0 1
     H  0.0000000000  0.0000000000  0.0000000000
     C  0.0000000000  0.0000000000  -1.058
     N  0.0000000000  0.0000000000  -2.207
    $end
    
    $rem
     neo = true
     purecart = 1111
     neo_purecart = 2222
     neo_vpp = 0
     method = hf
     basis = sto-3g
     scf_convergence = 11
     thresh = 14
     neo_n_scf_convergence = 11
     thresh = 14
     scf_algorithm = diis
     unrestricted = false
     neo_cc2 = 1
     scs = 2
     ep_factor = 940000
     ep_ex_factor = 1000000
     set_roots = 6
     direct_diag = 0
    $end
    
    $neo_basis
    H  1
    S  1  1.0
       4.0 1.0
    P  1  1.0
       4.0 1.0
    ****
    $end
    ```

???+ example "Example 13.36: Input for NEO-SA-MCSCF on HeHHe ${}^{+}$ molecule with the proton treated quantum mechanically. 3 states are averaged. The NEO-CASSCF uses AH/GDM."
    ```qchem
    $molecule
    1  1
    He    0.0000  0.0000  0.9000
    He    0.0000  0.0000 -0.9000
    H     0.0000  0.0000  0.0000
    $end
    
    $rem
    input_bohr = false
    mem_total = 32000
    method = hf
    basis = mixed
    use_libqints = 1
    print_general_basis = 0
    scf_algorithm = gdm
    neo_basis_lin_dep_thresh = 3
    neo = true
    neo_vpp = 0
    neo_purecart = 1111
    neo_mcscf = true
    neo_wf_e_docc = 0
    neo_wf_e_cas = 4
    neo_wf_n_cas = 87
    neo_mcscf_sa = true
    neo_mcscf_sa_nstates = 3
    neo_mcscf_nstates = 6
    neo_mcscf_opt_method = 2
    neo_mcscf_macro_conv_thresh = 6
    neo_mcscf_macro_max_iter = 100
    neo_mcscf_emc_conv_thresh = 8
    neo_mcscf_micro_conv_thresh = 8
    neo_mcscf_micro_max_iter = 100000
    neo_mcscf_micro_opt_max_iter = 5
    neo_mcscf_kspace_min = 8
    neo_mcscf_kspace_max = 20
    neo_mcscf_reorder_mos = false
    neo_mcscf_print_mos = false
    neo_mcscf_read_mos = false
    neo_mcscf_print_level = 0
    neo_mcscf_use_prev_ci_iter = 0
    $end
    
    $neo_basis
    H    3
    S    1    1.0
       2.8284  1.0
    S    1    1.0
       4.0000  1.0
    S    1    1.0
       5.6569  1.0
    S    1    1.0
       8.0000  1.0
    S    1    1.0
      11.3137  1.0
    S    1    1.0
      16.0000  1.0
    S    1    1.0
      22.6274  1.0
    S    1    1.0
      32.0000  1.0
    P    1    1.0
       2.8284  1.0
    P    1    1.0
       4.0000  1.0
    P    1    1.0
       5.6569  1.0
    P    1    1.0
       8.0000  1.0
    P    1    1.0
      11.3137  1.0
    P    1    1.0
      16.0000  1.0
    P    1    1.0
      22.6274  1.0
    P    1    1.0
      32.0000  1.0
    D    1    1.0
       2.8284  1.0
    D    1    1.0
       4.0000  1.0
    D    1    1.0
       5.6569  1.0
    D    1    1.0
       8.0000  1.0
    D    1    1.0
      11.3137  1.0
    D    1    1.0
      16.0000  1.0
    D    1    1.0
      22.6274  1.0
    D    1    1.0
      32.0000  1.0
    F    1    1.0
       2.8284  1.0
    F    1    1.0
       4.0000  1.0
    F    1    1.0
       5.6569  1.0
    F    1    1.0
       8.0000  1.0
    F    1    1.0
      11.3137  1.0
    F    1    1.0
      16.0000  1.0
    F    1    1.0
      22.6274  1.0
    F    1    1.0
      32.0000  1.0
    ****
    $end
    
    $basis
    He  1
    6-31g
    ****
    He  2
    6-31g
    ****
    H   3
    def2-QZVP
    ****
    $end
    ```

???+ example "Example 13.37: Input for NEO-SD ${}_{\text{en}}$ CI on HeHHe ${}^{+}$ molecule with the proton treated quantum mechanically, solving for 7 roots."
    ```qchem
    $molecule
    1  1
    He    0.0000  0.0000  0.9000
    He    0.0000  0.0000 -0.9000
    H     0.0000  0.0000  0.0000
    $end
    
    $rem
    input_bohr = false
    mem_total = 32000
    method = hf
    basis = mixed
    use_libqints = 1
    print_general_basis = 0
    scf_algorithm = gdm
    neo_basis_lin_dep_thresh = 3
    neo = true
    neo_vpp = 0
    neo_purecart = 1111
    neo_wf_e_docc = 2
    neo_wf_e_xlevel = 1
    neo_wf_n_cas = 1
    neo_wf_n_xlevel = 1
    neo_mrci = true
    neo_mrci_max_iter = 1000
    neo_mrci_num_roots = 7
    neo_mrci_kspace_min = 8
    neo_mrci_kspace_max = 15
    neo_mrci_prediag_routine = 1
    neo_mrci_prediag_dim = 1000
    neo_mrci_conv_thresh = 5
    $end
    
    $neo_basis
    H    3
    S    1    1.0
       2.8284  1.0
    S    1    1.0
       4.0000  1.0
    S    1    1.0
       5.6569  1.0
    S    1    1.0
       8.0000  1.0
    S    1    1.0
      11.3137  1.0
    S    1    1.0
      16.0000  1.0
    S    1    1.0
      22.6274  1.0
    S    1    1.0
      32.0000  1.0
    P    1    1.0
       2.8284  1.0
    P    1    1.0
       4.0000  1.0
    P    1    1.0
       5.6569  1.0
    P    1    1.0
       8.0000  1.0
    P    1    1.0
      11.3137  1.0
    P    1    1.0
      16.0000  1.0
    P    1    1.0
      22.6274  1.0
    P    1    1.0
      32.0000  1.0
    D    1    1.0
       2.8284  1.0
    D    1    1.0
       4.0000  1.0
    D    1    1.0
       5.6569  1.0
    D    1    1.0
       8.0000  1.0
    D    1    1.0
      11.3137  1.0
    D    1    1.0
      16.0000  1.0
    D    1    1.0
      22.6274  1.0
    D    1    1.0
      32.0000  1.0
    F    1    1.0
       2.8284  1.0
    F    1    1.0
       4.0000  1.0
    F    1    1.0
       5.6569  1.0
    F    1    1.0
       8.0000  1.0
    F    1    1.0
      11.3137  1.0
    F    1    1.0
      16.0000  1.0
    F    1    1.0
      22.6274  1.0
    F    1    1.0
      32.0000  1.0
    ****
    $end
    
    $basis
    He  1
    6-31g
    ****
    He  2
    6-31g
    ****
    H   3
    def2-QZVP
    ****
    $end
    ```
