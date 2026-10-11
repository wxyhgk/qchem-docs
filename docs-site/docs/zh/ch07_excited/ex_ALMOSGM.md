---
title: "7.7.7 ALMO-SGM Method"
---

## 7.7.7 ALMO-SGM Method

(July 4, 2026)

Studying the numerical stability of the initial guess density in OO-DFT
methods[[144]](../bib_references/bib.md#bib134)
, we concluded that, in the case of CT excitations,
a suitable guess density can be obtained for a fragmented system by using
the absolutely localized molecular orbitals (ALMO)
method[[1314]](../bib_references/bib.md#bib1371)
.
The ALMO method is presented in Section [12.5](../ch12_frag/sect_old_scfmi_eda.md).
In this method, the atom-centered Gaussian basis is localized, and ionized
fragments can be computed.
The resulting density is properly polarized for the calculation of intermolecular
CT excitations, and can be further relaxed using the SGM method.
Convergence is robust, and the input preparation is more straightforward compared
to the FRZ-SGM method, although it is not straightforwardly transferable to
covalently bonded systems.

???+ example "Example 7.7.57: Example input for the calculation of the lowest-lying intermolecular charge
transfer excitation energy in the anthracene-tetracyanoethylene dimer using
ALMO-SGM 144 Bogo N. et al. Phys. Chem. Chem. Phys. (2025) , 27 , pp. 17533 . Link and the nonequilibrium conductor-like polarizable
continuum (C-PCM) solvation model 1530 You Z.-Q. et al. J. Chem. Phys. (2015) , 143 , pp. 204104 . Link , 940 Mewes J.-M. et al. J. Phys. Chem. A (2015) , 119 , pp. 5446 . Link for dichloromethane (DCM).
The excitation energy and transition dipole moment to the CT excitation are
calculated."
    ```qchem
    $molecule
    0 1
    ---
    0 1
    C       0.0000024972    -1.3939649880    -1.2808767121
    C       0.0000025051     1.3939644651    -1.2808767282
    C      -1.2186821591    -0.7141902026    -1.3071478062
    C       1.2186864041    -0.7141896146    -1.3071387589
    C      -1.2186821243     0.7141897115    -1.3071478120
    C       1.2186863774     0.7141891121    -1.3071387637
    C      -2.4644125118    -1.4013703998    -1.3157095813
    C       2.4644171860    -1.4013692038    -1.3157202646
    C      -2.4644123040     1.4013701670    -1.3157095358
    C       2.4644169957     1.4013689421    -1.3157202095
    C      -3.6355756821    -0.7091886883    -1.3209438667
    C       3.6355802205    -0.7091872626    -1.3209819362
    C      -3.6355756149     0.7091887273    -1.3209437866
    C       3.6355801612     0.7091872572    -1.3209818529
    H       0.0000024198    -2.4788109280    -1.2699497414
    H       0.0000024299     2.4788104048    -1.2699497864
    H      -2.4609901895    -2.4845736396    -1.3142370557
    H       2.4609967495    -2.4845724379    -1.3142287226
    H      -2.4609894842     2.4845734123    -1.3142370884
    H       2.4609960822     2.4845721821    -1.3142287476
    H      -4.5790700028    -1.2397330066    -1.3238607200
    H       4.5790785788    -1.2397242939    -1.3239159625
    H      -4.5790698620     1.2397331701    -1.3238605613
    H       4.5790784507     1.2397244044    -1.3239157964
    ---
    0 1
    C      -0.0000060964    -0.6804948447     1.8114150650
    C      -0.0000061169     0.6804936064     1.8114151444
    C       1.2158428238    -1.4225502703     1.8615716187
    C      -1.2158551579    -1.4225518647     1.8615295498
    C       1.2158426874     1.4225492361     1.8615717275
    C      -1.2158551065     1.4225507587     1.8615296588
    N       2.1947618514    -2.0185775621     1.9228707722
    N      -2.1947808705    -2.0185720940     1.9227856078
    N       2.1947616310     2.0185766696     1.9228709110
    N      -2.1947807686     2.0185710748     1.9227857419
    $end
    
    $comment
    ALMO on the ground state to set up the localized basis
    $end
    
    $rem
    jobtype             sp
    scf_guess           fragmo
    FRGM_METHOD         STOLL
    SCF_PRINT_FRGM      TRUE
    method              wB97xD
    basis               def2-TZVP
    scf_max_cycles      1000
    sym_ignore          true
    symmetry            false
    thresh              14
    unrestricted        true
    solvent_method      pcm
    $end
    
    $rem_frgm
       unrestricted    true
       SCF_CONVERGENCE 5
       SCF_ALGORITHM   DIIS_GDM
       THRESH          14
    $end
    
    $pcm
    theory             iefpcm
    $end
    
    $solvent
    Dielectric         8.9
    Dielectric_Infi    2.03
    $end
    
    @@@
    
    $rem
    unrestricted        true
    jobtype             sp
    method              wB97xD
    scf_guess           read
    basis               def2-TZVP
    scf_algorithm       diis_gdm
    max_scf_cycles      250
    sym_ignore          true
    symmetry            false
    IQMOL_FCHK          TRUE
    trans_mom_save      true
    solvent_method      pcm
    $end
    
    $pcm
    theory             iefpcm
    rf_ptss_save       true
    $end
    
    $solvent
    Dielectric         8.9
    Dielectric_Infi    2.03
    $end
    
    $molecule
    read
    $end
    
    @@@
    
    $molecule
    0 1
    ---
    1 2
    C       0.0000024972    -1.3939649880    -1.2808767121
    C       0.0000025051     1.3939644651    -1.2808767282
    C      -1.2186821591    -0.7141902026    -1.3071478062
    C       1.2186864041    -0.7141896146    -1.3071387589
    C      -1.2186821243     0.7141897115    -1.3071478120
    C       1.2186863774     0.7141891121    -1.3071387637
    C      -2.4644125118    -1.4013703998    -1.3157095813
    C       2.4644171860    -1.4013692038    -1.3157202646
    C      -2.4644123040     1.4013701670    -1.3157095358
    C       2.4644169957     1.4013689421    -1.3157202095
    C      -3.6355756821    -0.7091886883    -1.3209438667
    C       3.6355802205    -0.7091872626    -1.3209819362
    C      -3.6355756149     0.7091887273    -1.3209437866
    C       3.6355801612     0.7091872572    -1.3209818529
    H       0.0000024198    -2.4788109280    -1.2699497414
    H       0.0000024299     2.4788104048    -1.2699497864
    H      -2.4609901895    -2.4845736396    -1.3142370557
    H       2.4609967495    -2.4845724379    -1.3142287226
    H      -2.4609894842     2.4845734123    -1.3142370884
    H       2.4609960822     2.4845721821    -1.3142287476
    H      -4.5790700028    -1.2397330066    -1.3238607200
    H       4.5790785788    -1.2397242939    -1.3239159625
    H      -4.5790698620     1.2397331701    -1.3238605613
    H       4.5790784507     1.2397244044    -1.3239157964
    ---
    -1 -2
    C      -0.0000060964    -0.6804948447     1.8114150650
    C      -0.0000061169     0.6804936064     1.8114151444
    C       1.2158428238    -1.4225502703     1.8615716187
    C      -1.2158551579    -1.4225518647     1.8615295498
    C       1.2158426874     1.4225492361     1.8615717275
    C      -1.2158551065     1.4225507587     1.8615296588
    N       2.1947618514    -2.0185775621     1.9228707722
    N      -2.1947808705    -2.0185720940     1.9227856078
    N       2.1947616310     2.0185766696     1.9228709110
    N      -2.1947807686     2.0185710748     1.9227857419
    $end
    
    $comment
    ALMO should provide a good guess for SGM
    $end
    
    $rem
    jobtype             sp
    scf_guess           fragmo
    FRGM_METHOD         STOLL
    SCF_PRINT_FRGM      TRUE
    method              wB97xD
    basis               def2-TZVP
    scf_max_cycles      1000
    sym_ignore          true
    symmetry            false
    thresh              14
    unrestricted        true
    solvent_method      pcm
    $end
    
    $rem_frgm
       unrestricted    true
       SCF_CONVERGENCE 5
       SCF_ALGORITHM   DIIS_GDM
       THRESH          14
    $end
    
    $pcm
    theory             iefpcm
    $end
    
    $solvent
    Dielectric         8.9
    Dielectric_Infi    2.03
    $end
    
    @@@
    
    $rem
       unrestricted        true
       thresh              14
       scf_convergence     5
       scf_algorithm       sgm_ls
       method              wB97xD
       basis               def2-TZVP
       scf_guess           read
       scf_max_cycles      500
       sym_ignore          true
       symmetry            false
       MAKE_CUBE_FILES     TRUE
       PLOTS               TRUE
       IQMOL_FCHK          TRUE
       trans_mom_read      true
       solvent_method      pcm
    $end
    
    $pcm
    theory             iefpcm
    rf_ptss_read       true
    $end
    
    $solvent
    Dielectric         8.9
    Dielectric_Infi    2.03
    $end
    
    $plots
       total_density    0
       grid_spacing     0.05
    $end
    
    $molecule
    read
    $end
    ```
