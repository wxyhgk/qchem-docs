---
title: "7.12.4 Calculations of Core Excitations with ROKS"
---

## 7.12.4 Calculations of Core Excitations with ROKS

(July 4, 2026)

The restricted open-shell Kohn-Sham (ROKS) approach is a
highly accurate method for estimating core-excitation energies of closed-shell
molecules,[[510]](../bib_references/bib.md#bib525)

as described in Section [7.7.4](ex_ESROKS.md). Here, we briefly recapitulate
the key aspects and refer the reader to Ref. [[510]](../bib_references/bib.md#bib525)
 for details
ROKS with the SCAN functional is found to reproduce
40 experimental core excitation energies (from the 1s orbital, *i.e.*, K-edge) of
second-period elements (C, N, O, and F) to an RMS error of 0.2 eV and a maximum
absolute error of 0.5 eV. The $\omega$B97X-V functional provides
similar (if a little worse) accuracy as well. Similar behavior is observed for
the L${}_{2,3}$ edges of third-period elements Si, P, S and Cl. Other widely used
functionals like PBE fare somewhat worse, but still predict much lower error
as compared to TDDFT using the same functionals. Recently, we extended the applicability for
ROKS for core excited states of heavier elements by including scalar
relativistic effects as described in Section [4.9.6](../ch04_scf/sec_x2c.md). Accurate modeling of K-edge of elements
up to $Z=24$ can be achieved with the SCAN functional.[[292]](../bib_references/bib.md#bib296)

That said, the ROKS approach is state-specific in
that it can only predict a single state at a time and needs to be told which
state to target (via the *$reorder_mo* section, as shown in
Example [7.7.5](ex_BEDSCF.md)). This makes it less black-box than TDDFT as the final
orbital needs to be identified *a priori*, perhaps via a pilot TDDFT job if
no other information is available. (For core-level excitations, the initial
orbital is usually intuitively obvious.) ROKS can also
be used for two-site doubly core-ionized states, or other systems with one
broken electron pair in total.

The accuracy of ROKS stems from three factors: choice of density functional
(SCAN or $\omega$B97X-V), excited state orbital optimization (only available
via SGM for core excitations, as described in Section [4.5.15](../ch04_scf/sect_SGM-SCF.md)) and a
sufficiently flexible basis set. The last is key, as the split-core functions
(as provided by basis sets like cc-pCV$n$Z) are needed instead of standard basis
sets like cc-pV$n$Z that only have split valence functions. Indeed, a basis of
triple-$\zeta$ quality like cc-pCVTZ is necessary to fully account for the
core-hole relaxation and smaller basis sets lead to systematic overestimation
of excitation energies. However, the highly local nature of the core-hole
ensures that a large basis is only needed for the target atom of the ROKS
calculation, and a smaller basis (of double-$\zeta$ quality, like cc-pVDZ) is
adequate for all other atoms. An example of this mixed basis strategy is given
below in Example 7.12.4. Details about using mixed basis sets in
general can be found in Section [8.5](../ch08_basis/sect_mixedbas.md).

The number of cycles needed for ROKS calculations can also be considerably
reduced by decoupling the core hole relaxation from the rest of the orbital
optimization. This entails a restricted open-shell $\Delta$SCF calculation of
the core-ionized state first, and use of those orbitals as guess for ROKS.
Example [7.7.5](ex_BEDSCF.md) is a representative case for how such calculations
should proceed.

The conjunction of high accuracy and low computational cost (due to the affordability of the SCAN
meta-GGA and the mixed basis strategy) makes ROKS a very attractive
approach for computing core spectra of large, closed-shell systems where more
expensive wave function theories are unaffordable. Users are requested to cite
Ref. [[510]](../bib_references/bib.md#bib525)
 when using ROKS for core excitations and Ref. [[292]](../bib_references/bib.md#bib296)

when performing calculations that include scalar relativistic effects.

???+ example "Example 7.215: RO- $\Delta$ SCF core-ionization at C for CO, using SGM. The mixed basis strategy is used as the core-hole is local to C."
    ```qchem
    $molecule
       0 1
       C 0.0000   0.0000   0.0000
       O 0.0000   0.0000   1.1282
    $end
    
    $rem
       METHOD     scan
       BASIS      gen
       BASIS2     aug-cc-pVDZ
       INTEGRAL_SYMMETRY false
    $end
    
    $basis
    C
    aug-cc-pCVTZ
    ****
    O
    aug-cc-pVDZ
    ****
    $end
    
    @@@@
    
    $molecule
       1 2
       C 0.0000   0.0000   0.0000
       O 0.0000   0.0000   1.1282
    $end
    
    $rem
       METHOD          scan
       BASIS           gen
       UNRESTRICTED    false
       SCF_GUESS       read
       INTEGRAL_SYMMETRY false
       SCF_ALGORITHM   sgm
    $end
    
    $reorder_mo
       1 3 4 5 6 7 2
       1 3 4 5 6 7 2
    $end
    
    $basis
    C
    aug-cc-pCVTZ
    ****
    O
    aug-cc-pVDZ
    ****
    $end
    ```

???+ example "Example 7.7.216: Combined RO- $\Delta$ SCF core-ionization and $1s\rightarrow\text{LUMO}$ ROKS core-excited state for HCl including scalar relativistic effects.
The uncontracted aug-pcX-2 basis has to be supplied by the user"
    ```qchem
    $molecule
    0 1
    Cl  0.0000  0.0000  0.0000
    H   0.0000  0.0000  1.2746
    $end
    
    $rem
    method scan
    basis  gen ! Decontracted aug-pcX-2 basis for X2C
    rel_x2c 1  ! Do X2C relativistic one-electron Hamiltonian
    rel_x2c_fd_displacement 100 ! Controls the finite difference step for W (default = 100 * 1e-6 = 1e-4)
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $basis
    Cl     0
    S   1   1.00
          0.216264D+06           1.00000000D+00
    S   1   1.00
          0.324104D+05           1.00000000D+00
    S   1   1.00
          0.737630D+04           1.00000000D+00
    S   1   1.00
          0.208877D+04           1.00000000D+00
    S   1   1.00
          0.681028D+03           1.00000000D+00
    S   1   1.00
          0.245288D+03           1.00000000D+00
    S   1   1.00
          0.949871D+02           1.00000000D+00
    S   1   1.00
          0.385297D+02           1.00000000D+00
    S   1   1.00
          0.158316D+02           1.00000000D+00
    S   1   1.00
          0.610936D+01           1.00000000D+00
    S   1   1.00
          0.244372D+01           1.00000000D+00
    S   1   1.00
          0.603084D+00           1.00000000D+00
    S   1   1.00
          0.209285D+00           1.00000000D+00
    S   1   1.00
          0.679167D-01           1.00000000D+00
    P   1   1.00
          0.121088D+04           1.00000000D+00
    P   1   1.00
          0.287276D+03           1.00000000D+00
    P   1   1.00
          0.924350D+02           1.00000000D+00
    P   1   1.00
          0.343221D+02           1.00000000D+00
    P   1   1.00
          0.139811D+02           1.00000000D+00
    P   1   1.00
          0.590468D+01           1.00000000D+00
    P   1   1.00
          0.250190D+01           1.00000000D+00
    P   1   1.00
          0.928135D+00           1.00000000D+00
    P   1   1.00
          0.348099D+00           1.00000000D+00
    P   1   1.00
          0.117780D+00           1.00000000D+00
    P   1   1.00
          0.373244D-01           1.00000000D+00
    D   1   1.00
          0.241272D+01           1.00000000D+00
    D   1   1.00
          0.544426D+00           1.00000000D+00
    D   1   1.00
          0.111960D+00           1.00000000D+00
    F   1   1.00
          0.749400D+00           1.00000000D+00
    F   1   1.00
          0.149279D+00           1.00000000D+00
    ****
    H     0
    S   1   1.00
          0.754732D+02           1.00000000D+00
    S   1   1.00
          0.113575D+02           1.00000000D+00
    S   1   1.00
          0.260081D+01           1.00000000D+00
    S   1   1.00
          0.735503D+00           1.00000000D+00
    S   1   1.00
          0.231761D+00           1.00000000D+00
    S   1   1.00
          0.741675D-01           1.00000000D+00
    S   1   1.00
          0.223070D-01           1.00000000D+00
    P   1   1.00
          0.160000D+01           1.00000000D+00
    P   1   1.00
          0.450000D+00           1.00000000D+00
    P   1   1.00
          0.669210D-01           1.00000000D+00
    D   1   1.00
          0.125000D+01           1.00000000D+00
    D   1   1.00
          0.892290D-01           1.00000000D+00
    ****
    $end
    
    @@@@@@@@@@@
    $comment
    RO core ionized state. Note that the $molecule section thus set up will read geometry from before, but not charge/spin, which is supplied
    $end
    
    $molecule
    1 2
    read
    $end
    
    $rem
    method        scan
    basis         gen
    scf_algorithm sgm
    scf_guess     read
    roscf         true
    rel_x2c 1 ! Do X2C relativistic one-electron Hamiltonian
    rel_x2c_fd_displacement 100 ! Controls the finite difference step for W (default = 100 * 1e-6 = 1e-4)
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $reorder_mo ! push the 1s orbital to the frontier. For HCl we have 18 electrons, so 9 orbitals. Pushing 1 (1s) to the frontier (9) is done thus.
    2 3 4 5 6 7 8 9 1
    2 3 4 5 6 7 8 9 1
    $end
    
    $basis
    Cl     0
    S   1   1.00
          0.216264D+06           1.00000000D+00
    S   1   1.00
          0.324104D+05           1.00000000D+00
    S   1   1.00
          0.737630D+04           1.00000000D+00
    S   1   1.00
          0.208877D+04           1.00000000D+00
    S   1   1.00
          0.681028D+03           1.00000000D+00
    S   1   1.00
          0.245288D+03           1.00000000D+00
    S   1   1.00
          0.949871D+02           1.00000000D+00
    S   1   1.00
          0.385297D+02           1.00000000D+00
    S   1   1.00
          0.158316D+02           1.00000000D+00
    S   1   1.00
          0.610936D+01           1.00000000D+00
    S   1   1.00
          0.244372D+01           1.00000000D+00
    S   1   1.00
          0.603084D+00           1.00000000D+00
    S   1   1.00
          0.209285D+00           1.00000000D+00
    S   1   1.00
          0.679167D-01           1.00000000D+00
    P   1   1.00
          0.121088D+04           1.00000000D+00
    P   1   1.00
          0.287276D+03           1.00000000D+00
    P   1   1.00
          0.924350D+02           1.00000000D+00
    P   1   1.00
          0.343221D+02           1.00000000D+00
    P   1   1.00
          0.139811D+02           1.00000000D+00
    P   1   1.00
          0.590468D+01           1.00000000D+00
    P   1   1.00
          0.250190D+01           1.00000000D+00
    P   1   1.00
          0.928135D+00           1.00000000D+00
    P   1   1.00
          0.348099D+00           1.00000000D+00
    P   1   1.00
          0.117780D+00           1.00000000D+00
    P   1   1.00
          0.373244D-01           1.00000000D+00
    D   1   1.00
          0.241272D+01           1.00000000D+00
    D   1   1.00
          0.544426D+00           1.00000000D+00
    D   1   1.00
          0.111960D+00           1.00000000D+00
    F   1   1.00
          0.749400D+00           1.00000000D+00
    F   1   1.00
          0.149279D+00           1.00000000D+00
    ****
    H     0
    S   1   1.00
          0.754732D+02           1.00000000D+00
    S   1   1.00
          0.113575D+02           1.00000000D+00
    S   1   1.00
          0.260081D+01           1.00000000D+00
    S   1   1.00
          0.735503D+00           1.00000000D+00
    S   1   1.00
          0.231761D+00           1.00000000D+00
    S   1   1.00
          0.741675D-01           1.00000000D+00
    S   1   1.00
          0.223070D-01           1.00000000D+00
    P   1   1.00
          0.160000D+01           1.00000000D+00
    P   1   1.00
          0.450000D+00           1.00000000D+00
    P   1   1.00
          0.669210D-01           1.00000000D+00
    D   1   1.00
          0.125000D+01           1.00000000D+00
    D   1   1.00
          0.892290D-01           1.00000000D+00
    ****
    $end
    
    @@@@@@@
    $comment
    ROKS for core excitation
    $end
    
    $molecule
    0 1
    read
    $end
    
    $rem
    method        scan
    basis         gen
    scf_algorithm sgm
    scf_guess     read
    os_roscf      true ! Turns ROKS on
    scf_convergence 5
    max_scf_cycles  5000
    rel_x2c 1 ! Do X2C relativistic one-electron Hamiltonian
    rel_x2c_fd_displacement 100 ! Controls the finite difference step for W (default = 100 * 1e-6 = 1e-4)
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $basis
    Cl     0
    S   1   1.00
          0.216264D+06           1.00000000D+00
    S   1   1.00
          0.324104D+05           1.00000000D+00
    S   1   1.00
          0.737630D+04           1.00000000D+00
    S   1   1.00
          0.208877D+04           1.00000000D+00
    S   1   1.00
          0.681028D+03           1.00000000D+00
    S   1   1.00
          0.245288D+03           1.00000000D+00
    S   1   1.00
          0.949871D+02           1.00000000D+00
    S   1   1.00
          0.385297D+02           1.00000000D+00
    S   1   1.00
          0.158316D+02           1.00000000D+00
    S   1   1.00
          0.610936D+01           1.00000000D+00
    S   1   1.00
          0.244372D+01           1.00000000D+00
    S   1   1.00
          0.603084D+00           1.00000000D+00
    S   1   1.00
          0.209285D+00           1.00000000D+00
    S   1   1.00
          0.679167D-01           1.00000000D+00
    P   1   1.00
          0.121088D+04           1.00000000D+00
    P   1   1.00
          0.287276D+03           1.00000000D+00
    P   1   1.00
          0.924350D+02           1.00000000D+00
    P   1   1.00
          0.343221D+02           1.00000000D+00
    P   1   1.00
          0.139811D+02           1.00000000D+00
    P   1   1.00
          0.590468D+01           1.00000000D+00
    P   1   1.00
          0.250190D+01           1.00000000D+00
    P   1   1.00
          0.928135D+00           1.00000000D+00
    P   1   1.00
          0.348099D+00           1.00000000D+00
    P   1   1.00
          0.117780D+00           1.00000000D+00
    P   1   1.00
          0.373244D-01           1.00000000D+00
    D   1   1.00
          0.241272D+01           1.00000000D+00
    D   1   1.00
          0.544426D+00           1.00000000D+00
    D   1   1.00
          0.111960D+00           1.00000000D+00
    F   1   1.00
          0.749400D+00           1.00000000D+00
    F   1   1.00
          0.149279D+00           1.00000000D+00
    ****
    H     0
    S   1   1.00
          0.754732D+02           1.00000000D+00
    S   1   1.00
          0.113575D+02           1.00000000D+00
    S   1   1.00
          0.260081D+01           1.00000000D+00
    S   1   1.00
          0.735503D+00           1.00000000D+00
    S   1   1.00
          0.231761D+00           1.00000000D+00
    S   1   1.00
          0.741675D-01           1.00000000D+00
    S   1   1.00
          0.223070D-01           1.00000000D+00
    P   1   1.00
          0.160000D+01           1.00000000D+00
    P   1   1.00
          0.450000D+00           1.00000000D+00
    P   1   1.00
          0.669210D-01           1.00000000D+00
    D   1   1.00
          0.125000D+01           1.00000000D+00
    D   1   1.00
          0.892290D-01           1.00000000D+00
    ****
    $end
    
    ```
