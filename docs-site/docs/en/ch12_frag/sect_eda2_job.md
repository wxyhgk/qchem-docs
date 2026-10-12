---
title: "12.6.5 Job Control for EDA2"
---

## 12.6.5 Job Control for EDA2

(July 4, 2026)

The use of the FERF model for the evaluation of polarization energy and the
further decomposition of the frozen term define the second generation of the
ALMO-EDA method. Meanwhile, under the same code structure, the original
AO-block based ALMO model and other related methods (such as the constrained
relaxation of the frozen wave function[[594]](../bib_references/bib.md#bib618)
 which renders the
frozen energy variationally computed, and the polMO model[[59]](../bib_references/bib.md#bib42)
 that
arguably gives a lower limit to the polarization contribution) are also
available. This entire set of methods implemented in **Q-Chem** based on
GEN_SCFMAN (see Section [4.3](../ch04_scf/sec_SCF_job-control.md)) is referred to as “EDA2”.
In **Q-Chem** 5.2 and after, “EDA2” is used as the default ALMO-EDA driver
when “JOBTYPE = EDA” is requested.

The job control for EDA2 is largely simplified by a series of preset options
provided by the developers. The option number is set through the EDA2
*$rem* variable (introduced below). Besides that, for the sake of flexibility,
users are allowed to overwrite the values of part of the preset *$rem*
variables:

- •

Related to the isolated fragment calculations:

- **–**

EDA_CHILD_SUPER_BASIS: use the super-system basis for fragment calculations (default: FALSE).
- **–**

FRAGMO_GUESS_MODE: as introduced in Section [12.3](sect_FRAGMOguess.md) (default: 0).
- •

Related to the decomposition of the FRZ term:

- **–**

FRZ_ORTHO_DECOMP: it can be turned off by setting its value to $-1$ in the *$rem* section 

(default: TRUE).
- **–**

FRZ_ORTHO_DECOMP_CONV: as introduced in Section [12.6.4](sect_frz_decomp.md) (default: 6).
- **–**

EDA_CLS_DISP: as introduced in Section [12.6.4](sect_frz_decomp.md) (default: FALSE).
- **–**

DISP_FREE_X: as introduced in Section [12.6.4](sect_frz_decomp.md) (default: HF).
- **–**

DISP_FREE_C: as introduced in Section [12.6.4](sect_frz_decomp.md) (default: NONE).
- •

Related to the evaluation and analysis of POL:

- **–**

CHILD_MP_ORDERS: as introduced in Section [12.6.3](sect_ferf.md) (default: 232 (DQ)).
- **–**

SCFMI_FREEZE_SS: as introduced in Section [12.6.2](sect_gen_scfmi.md) (default: 0).
- **–**

EDA_POL_A: perform non-perturbative polarization analysis (default: FALSE; see Section [12.6.8](sect_eda2_vcta.md)).
- •

Related to the evaluation of CT and BSSE:

- **–**

EDA_NO_CT: skip the evaluation of the CT term in the EDA procedure 

(default: FALSE
(automatically turned on when SCFMI_FREEZE_SS = TRUE)).
- **–**

EDA_BSSE: use counterpoise-corrected monomer calculations to evaluate the BSSE 

(default: FALSE).
- **–**

EDA_PCT_A: turn on perturbative (Roothaan step based) charge transfer analysis (default: FALSE).
- **–**

EDA_VCT_A: turn on non-perturbative charge transfer analysis (default: FALSE; see Section [12.6.8](sect_eda2_vcta.md)).
- **–**

EDA_COVP: perform COVP analysis for charge transfer (default: FALSE; see Section [12.5.3](sect_eda1.md)).
- **–**

EDA_PRINT_COVP: dump COVPs to the MO coefficient file (default: FALSE; see Section [12.5.3](sect_eda1.md)). 

Note: EDA2 can automatically generate the cubes for the dominant complementary occupied-virtual orbitals for each pair of donor
and acceptor fragments when EDA_PRINT_COVP is greater than 1.
- •

Miscellaneous:

- **–**

EDA2_PRINT_LEVEL: print additional details for some of the EDA terms (*e.g.* solvation-corrected ELEC/PAULI)
when set to $>1$ (default: 1)

### `EDA2`

> **Switch on EDA2 and specify the option set number.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `0`: Do not run through EDA2.
>     * `1`: Frozen energy decomposition + nMDQ-uFERF polarization (the standard EDA2 option)
>     * `2`: Frozen energy decomposition + (AO-block-based) ALMO polarization (old scheme with the addition of frozen decomposition)
>     * `3`: Frozen energy decomposition + oDQ-FERF polarization (NOT commonly used)
>     * `4`: Frozen wave function relaxation + Frozen energy decomposition + nDQ-FERF polarization (NOT commonly used)
>     * `5`: Frozen energy decomposition + polMO polarization (NOT commonly used).
>     * `10`: No preset. Completely controlled by user’s $rem input (for developers only)
> * **Recommendation**: Turn on for Q-Chem ’s ALMO-EDA jobs unless CTA with the old scheme is desired. Option 1 is recommended in general, especially when substantially large basis sets are employed. The original ALMO scheme (option 2) can be used when the employed basis set is of small or medium size (arguably no larger than augmented triple- $\zeta$ ). The other options are rarely used for routine applications.

Note that starting with **Q-Chem** v. 5.2, if JOBTYPE = EDA
is requested while but the *$rem* variable EDA2 is not specified by the user,
the latter defaults to EDA2 = 2 with EDA_PCT_A = TRUE.

For calculations based on EDA2, the default SCF convergence criterion is set to 10${}^{-8}$
(rather than 10${}^{-5}$ as in **Q-Chem**’s normal SCF calculations). The fragment calculations
involved are forced to use the same SCF convergence criterion as the parent job.

In cases where the radical is a single atom (*e.g.* $\bullet$Cl) or of a highly
symmetric geometry (*e.g.* $\bullet$OH), there can be multiple degenerate
electronic configurations with the unpaired electron residing in different
orbitals, resulting in arbitrariness in the definition of the frozen state.
For such systems, it is desirable to obtain the orientation of fragment spin
that leads to the lowest-energy frozen state. This can be achieved by employing
a “polarize-then-depolarize” (PtD) approach,[[895]](../bib_references/bib.md#bib930)
 using
interfragment polarization to resolve the degeneracy of radical’s electronic
states: one first converges the polarization (SCF-MI) calculation for the full system,
and then recalculates the SCF solutions for each isolated fragment using their
corresponding blocks in the ALMO coefficient matrix as the initial guess.
To ensure that the “depolarized” fragments are of the same electronic configuration
as in the fully polarized wave function, the initial maximum overlap
method[[75]](../bib_references/bib.md#bib59)
 (IMOM) is used in these fragment calculations. The fragment orbitals
obtained therefrom then uniquely determine the frozen wave function.

In **Q-Chem** 5.2 and after, the procedure described above is performed for unrestricted
ALMO-EDA calculations by default. It can also be manually requested by setting
EDA_ALIGN_FRGM_SPIN to $>0$ values. Note that this setting further
ensures that one obtains a stable SCF-MI solution in the initial polarization step
(see below), which is crucial for the success of this approach. Occasionally, one may
find that the frozen state constructed from “spin-aligned” fragments is of a higher
energy than the initial one. This indicates that the fragment spin alignment procedure
is not functioning well, and in such cases we recommend the user to run EDA2 calculation
without this procedure by setting FRZ_RELAX = $-1$.

With **Q-Chem** 6.2.1 or later versions, the user is also allowed to specify fragments to
which the PtD scheme is not applied. These fragments can be specified through the
*$skip_frgm_spin_align* section (fragment index starts from 1). For instance,

> ```qchem
> $skip_frgm_spin_align
>  2
> $end
> ```

indicates that the 2nd fragment will skip the spin alignment procedure. Typically, for
interactions between radicals and closed-shell molecules, spin alignment only needs to
be applied to the radicals.

### `EDA_ALIGN_FRGM_SPIN`

> **Turn on the fragment spin alignment procedure**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not performed the spin alignment procedure (turned on by default in unrestricted cases)
>     * `1`: Perform fragment spin alignment; use GDM for the polarization step preceding the MOM calculations
>     * `2`: Perform fragment spin alignment; use GDM and perform stability analysis for the polarization step
> * **Recommendation**: Use 1 or 2 when the radical is of highly symmetric structure

Another feature that can be useful for systems involving open-shell species
is the capability of performing stability analysis on user-specified fragments,
since it is important to ensure the stability of each fragment’s SCF solution.
This can be done through the *$frgm_stability* input section:

> ```qchem
> $frgm_stability
>    [frgm_idx1]  [frgm_idx2]  ...
> $end
> ```

where one simply puts the indices of fragments that require stability analysis.

???+ example "Example 12.14: Energy decomposition analysis for the ammonia-borane complex. The FERF-nDQ
model is used for the POL term (as very large basis set is employed here), and
decomposition of the frozen interaction energy is performed (Hartree-Fock is
employed as the DFXC functional by default)."
    ```qchem
    $molecule
       0 1
       --
       0 1
       N       0.000000     0.000000    -0.727325
       H       0.947371     0.000000    -1.091577
       H      -0.473685    -0.820448    -1.091577
       H      -0.473685     0.820448    -1.091577
       --
       0 1
       B       0.000000     0.000000     0.930725
       H      -1.165774     0.000000     1.243063
       H       0.582887    -1.009590     1.243063
       H       0.582887     1.009590     1.243063
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              1
       METHOD            wB97M-V
       BASIS             def2-TZVPPD
       MEM_TOTAL         4000
       MEM_STATIC        1000
       THRESH            14
       SCF_CONVERGENCE   8
       XC_GRID           000099000590
       NL_GRID           1
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "Example 12.15: Energy decomposition analysis of the water dimer with a low-cost model
chemistry. The original ALMO model is used for the evaluation of polarization
energy, and revPBE is chosen as the DFXC functional. Counterpoise correction
for the BSSE is applied."
    ```qchem
    $molecule
    0 1
    --
    0 1
    H1
    O1 H1 0.95641
    H2 O1 0.96500  H1 104.77306
    --
    0 1
    O2 H2 dist     O1 171.85474 H1 180.000
    H3 O2 0.95822  H2 111.79807 O1 -58.587
    H4 O2 0.95822  H2 111.79807 O1 58.587
    
    dist = 2.0
    $end
    
    $rem
       JOBTYPE          eda
       EDA2             2
       METHOD           b97m-v
       BASIS            def2-svpd
       SCF_CONVERGENCE  8
       THRESH           14
       DISP_FREE_X      revPBE
       DISP_FREE_C      PBE
       EDA_BSSE         true
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "Example 12.16: Unrestricted EDA calculation for the H ${}_{2}$ O $\cdots$ Cl ${}^{\bullet}$ complex.
The fragment spin alignment procedure is performed to ensure the uniqueness
of the frozen wave function ( EDA_ALIGN_FRGM_SPIN = 2)."
    ```qchem
    $molecule
       0 2
       --
       0 2
       Cl         0.00127        0.00000       -0.88139
       --
       0 1
       O         -0.06700        0.00000        1.72173
       H          0.50943       -0.76061        1.83598
       H          0.50943        0.76061        1.83598
    $end
    
    $rem
       JOBTYPE               eda
       METHOD                m06-2x
       BASIS                 6-31+g(d)
       EDA2                  2
       UNRESTRICTED          true
       SCF_ALGORITHM         diis
       SCF_CONVERGENCE       8
       MAX_SCF_CYCLES        200
       THRESH                14
       EDA_BSSE              true
       EDA_ALIGN_FRGM_SPIN   2
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    ```
