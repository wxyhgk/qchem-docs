---
title: "10.11.2 NMR Chemical Shifts and J-Couplings"
---

## 10.11.2 NMR Chemical Shifts and *J*-Couplings

(July 4, 2026)

NMR calculations are available at both the Hartree-Fock and DFT levels of theory.[[551]](../bib_references/bib.md#bib566)
**Q-Chem** computes NMR chemical shielding tensors using gauge-including atomic
orbitals (GIAOs),[[334]](../bib_references/bib.md#bib338)

an approach that has proven to reliable and accurate for many applications.[[550]](../bib_references/bib.md#bib564)

The shielding tensor $\bm{\sigma}$
is a second-order property that depends upon the external magnetic field,
$\mathbf{B}$, and the spin angular momentum $\bm{m}$ for a given nucleus:

<a id="Ch10.E116"></a>

$$
\Delta E=-\bm{m}\bm{\cdot}(\mathbf{1}-\bm{\sigma})\bm{\cdot}\mathbf{B}\;. \tag{10.116}
$$

Using analytical derivative techniques to evaluate $\bm{\sigma}$, the components
of this $3\times 3$ tensor are computed as

<a id="Ch10.E117"></a>

$$
\sigma_{ij}=\sum_{\mu\nu}P_{\mu\nu}\left(\frac{\partial^{2}h_{\mu\nu}}{\partial B_{i}\partial m_{j}}\right)+\sum_{\mu\nu}\frac{\partial P_{\mu\nu}}{\partial B_{i}}\frac{\partial h_{\mu\nu}}{\partial m_{j}} \tag{10.117}
$$

where $i,j\in\{x,y,z\}$ indicate Cartesian components. Note that there is a
separate chemical shielding tensor for each $\bm{m}$, that is, for each
nucleus. To compute $\sigma_{ij}$ it is necessary to solve coupled-perturbed
SCF (CPSCF) equations to obtain the perturbed densities $\partial P/\partial B_{i}$, which can be accomplished using the MO-based “MOProp” module whose use
is described below. (Use of the MOProp module to compute optical properties of
molecules was discussed in Section [10.10](sec_ElectricProps.md).) Alternatively, a
linear-scaling, density matrix-based CPSCF (D-CPSCF) formulation is
available,[[1010]](../bib_references/bib.md#bib1054)
 which is described in
Section [10.11.3](sec_D-CPSCF-NMR.md).

In addition to chemical shifts, indirect nuclear spin-spin coupling constants,
also known as scalar couplings or $J$-couplings, can be computed at the SCF
level. The coupling tensor $\mathbf{J}^{AB}$ between atoms $A$ and $B$ is
evaluated as the second derivative of the electronic energy with respect to the
nuclear magnetic moments $\bm{m}$:

<a id="issc"></a>

$$
\mathbf{J}^{AB}=\frac{\partial^{2}E}{\partial\bm{m}_{A}\partial\bm{m}_{B}}\;. \tag{10.118}
$$

The indirect coupling tensor has five distinct contributions. The diamagnetic
spin-orbit (DSO) contribution is calculated as an expectation value with the
ground state wave function. The other contributions are the paramagnetic
spin-orbit (PSO), spin-dipole (SD), Fermi contact (FC), and mixed SD/FC
contributions. These terms require the electronic response of the systems to
the perturbation due to the magnetic nuclei. Ten distinct CPSCF equations must
be solved for each perturbing nucleus, which makes the calculation of
$J$-coupling constants more time-consuming than that of chemical shifts.

Some authors have recommended calculating only the Fermi contact
contribution,[[71]](../bib_references/bib.md#bib56)
 and skipping the other contributions, for
${}^{1}$H–${}^{1}$H coupling constants. For that purpose, **Q-Chem** allows the user
to skip calculation of any of the four contributions: (FC, SD, PSO, or DSO.
(The mixed SD/FC contributions is automatically calculated at no
additional cost whenever both the SD and FC contributions are computed.) See
Section [10.10.3](moprop_jobcontrol.md) for details. Note that omitting any of the
contributions cannot be rationalized from a theoretical point of view. Results
from such calculations should be interpreted extremely cautiously.

!!! note "Note"
    1.

    Specialized basis sets are highly recommended in any $J$-coupling
    calculation, such as the pcJ-$n$ basis set family.[[634]](../bib_references/bib.md#bib660)

    2.

    The Hartree-Fock level of theory is *not* suitable to obtain
    $J$-coupling constants of *any* degree of reliability. Use GGA or
    hybrid density functionals instead.


## 10.11.2.1 FD-NMR Job Control and Examples

**Q-Chem**’s new FD-NMR feature calculates the NMR shielding tensor by applying finite differentiation on an analytic property,
such as the total energy (when IDERIV = 0), or the atom-wise induced magnetic field (when IDERIV = 1) the first
derivative of the energy with respect to the nuclear magentic moments. FD1 based shielding calculation is much more efficient than
that of FD2, and is avaliable at restricted SCF level (i.e. up to rung 4 hybrid / range-separated hybrid functionals). FD2 also has
limited support for $O(N^{5})$ correlated methods such as (regularized) RI-MP2.

???+ example "Example 10.55: FD2-based NMR calculation for water at RI-MP2/pcSseg-2 level."
    ```qchem
    $molecule
    0 1
    O          0.00000        0.00000        0.11779
    H          0.00000        0.75545       -0.47116
    H          0.00000       -0.75545       -0.47116
    $end
    
    $rem
    JOBTYPE             SP ! Required: zero-field job to prepare the initial guess for field-on job
    METHOD              HF
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-2
    AUX_BASIS_J         RIJK-def2-TZVP
    AUX_BASIS_K         RIJK-def2-TZVP
    RI_J                TRUE
    RI_K                TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    MAX_SCF_CYCLES      100
    NMR_SAVE            1 ! Required: zero-field job to prepare the initial guess for field-on job
    MEM_TOTAL           4000
    $end
    
    @@@
    
    $molecule
    READ
    $end
    
    $rem
    JOBTYPE             NMRSHIELD
    METHOD              RIMP2
    IDERIV              0 ! Required for FD2 logic
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-2
    AUX_BASIS_J         RIJK-def2-TZVP
    AUX_BASIS_K         RIJK-def2-TZVP
    AUX_BASIS_CORR      RIMP2-def2-TZVP
    RI_J                TRUE
    RI_K                TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    DO_FINITE_B_OR_M    1
    FDIFF_STEPSIZE_B    100 ! B field finite Difference step size in 1E-5 A.U.
    TENSOR_DIAG_ONLY    TRUE ! Calculates diagonal elements only
    COMPLEX             TRUE ! Required
    USE_LIBQINTS        TRUE ! Required
    MEM_TOTAL           4000
    $end
    
    $shielding ! select atom for shielding computation, index starts from 0
    0 1 2
    $end
    
    ```

???+ example "Example 10.56: FD1-based NMR calculation for benzene at HF/pcSseg-3 level."
    ```qchem
    $molecule
    0 1
    H         -8.15907        2.62281        1.60092
    C         -8.66658        2.57679        0.63197
    C        -10.05547        2.62953        0.57123
    H        -10.64089        2.71700        1.49206
    C        -10.70043        2.57096       -0.65988
    H        -11.79336        2.61234       -0.70769
    C         -9.95678        2.45974       -1.83037
    H        -10.46440        2.41365       -2.79910
    C         -8.56799        2.40692       -1.76952
    H         -7.98287        2.31923       -2.69053
    C         -7.92294        2.46549       -0.53841
    H         -6.83011        2.42401       -0.49049
    $end
    
    $rem
    JOBTYPE             SP ! Required: zero-field job to prepare the initial guess for field-on job
    METHOD              HF
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-3
    AUX_BASIS_J         RIJK-def2-QZVP
    AUX_BASIS_K         RIJK-def2-QZVP
    RI_J                TRUE
    OCC_RI_K            TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    NMR_SAVE            1 ! Required: zero-field job to prepare the initial guess for field-on job
    MEM_TOTAL           8000
    $end
    
    @@@
    
    $molecule
    READ
    $end
    
    $rem
    JOBTYPE             NMRSHIELD
    METHOD              HF
    IDERIV              1 ! Required for FD1 logic
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-3
    AUX_BASIS_J         RIJK-def2-QZVP
    AUX_BASIS_K         RIJK-def2-QZVP
    RI_J                TRUE
    OCC_RI_K            TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    DO_FINITE_B_OR_M    1
    FDIFF_STEPSIZE_B    100 ! B field finite Difference step size in 1E-5 A.U.
    COMPLEX             TRUE
    USE_LIBQINTS        TRUE ! Required
    NMR_FORWARD_DIFF    TRUE ! Calculates NMR properties with forward difference instead of central difference
    MEM_TOTAL           8000
    $end
    
    ```

## 10.11.2.2 NMR Job Control and Examples

This section describes the use of **Q-Chem**’s MO-based CPSCF code, which is
contained in the “MOProp” module that is also responsible for computing
electric properties. NMR chemical shifts are requested by setting
MOPROP = 1, and $J$-couplings by setting JOBTYPE =
ISSC. The reader is referred to to Section [10.10.3](moprop_jobcontrol.md)
for additional job control variables associated with the MOProp module, as well
as explanations of the ones that are invoked in the samples below. An
alternative, ${\cal{O}}({N})$ density matrix-based implementation of NMR chemical
shifts is also available and is described in Section [10.11.3](sec_D-CPSCF-NMR.md).
Setting JOBTYPE = NMR invokes the density-based code, not the
MO-based code.

???+ example "Example 10.57: MO-based NMR calculation."
    ```qchem
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
      METHOD             B3LYP
      BASIS              6-31G*
      MOPROP               1
      MOPROP_PERTNUM       0  ! do all perturbations at once
      MOPROP_CONV_1ST      7  ! sets the CPSCF convergence threshold
      MOPROP_DIIS_DIM_SS   4  ! no. of DIIS subspace vectors
      MOPROP_MAXITER_1ST 100  ! max iterations
      MOPROP_DIIS          5  ! turns on DIIS (=0 to turn off)
      MOPROP_DIIS_THRESH   1
      MOPROP_DIIS_SAVE     0
    $end
    ```

In the following compound job, we show how to restart an NMR calculation
should it exceed the maximum number of CPSCF iterations (specified with
MOPROP_MAXITER_1ST, or should the calculation run out of time on
a shared computer resource. Note that the first job is *intentionally*
set up to exceed the maximum number of iterations, so will crash. However,
the calculation is restarted and completed in the second job.

???+ example "Example 10.58: Illustrates how to restart an NMR calculation. In this first job, we intentionally set the max number of iterations too small, to force
premature end so that we can demonstrate restart capability in the 2nd job."
    ```qchem
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
       METHOD               B3LYP
       BASIS                6-31G*
       SCF_ALGORITHM        DIIS
       MOPROP               1
       MOPROP_MAXITER_1ST   10   ! too small, for demonstration only
       GUESS_PX             1
       MOPROP_DIIS_SAVE     0   ! don’t hang onto the subspace vectors
    $end
    
    @@@
    
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
       METHOD               B3LYP
       BASIS                6-31G*
       SCF_GUESS            READ
       SKIP_SCFMAN          TRUE   ! no need to redo the SCF
       MOPROP               1
       MOPROP_RESTART       1
       MOPROP_MAXITER_1ST   100  ! more reasonable choice
       GUESS_PX             1
       MOPROP_DIIS_SAVE     0
    $end
    ```

???+ example "Example 10.59: $J$ -coupling calculation: water molecule with B3LYP/cc-pVDZ"
    ```qchem
    $molecule
       0 1
       O
       H1 O OH
       H2 O OH H1 HOH
    
       OH  = 0.947
       HOH = 105.5
    $end
    
    $rem
       JOBTYPE           ISSC
       EXCHANGE          B3LYP
       BASIS             cc-pVDZ
       LIN_K             FALSE
       MOPROP_CONV_1ST   6
       INTEGRAL_SYMMETRY TRUE
    $end
    ```

In the event that spin-spin couplings of only certain atom pairs are of
interest, it is possible to limit the atom pairs for which the couplings are
computed. Selection is done via the *$spin-spin* input section, which is
zero-indexed. For example, the section

> ```qchem
> $spin-spin
> 0 1 5
> $end
> ```

would compute couplings between all possible pairings of the first, second,
and sixth atoms in the respective *$molecule* section: (1, 2), (1, 6), and (2,6).
If the *$spin-spin* section is not specified, couplings between all
possible pairs of atoms in *$molecule* will be computed.

## 10.11.2.3 Nucleus-Independent Chemical Shifts: Probes of Aromaticity

Unambiguous theoretical estimates of degree of aromaticity are still on high
demand. The NMR chemical shift methodology offers one unique probe of
aromaticity based on one defining characteristics of an aromatic system: its
ability to sustain a diatropic ring current. This leads to a response to an
imposed external magnetic field with a strong (negative) shielding at the
center of the ring. Von Schleyer *et al.* have employed this phenomenon to justify
a new unique probe of aromaticity.[[1383]](../bib_references/bib.md#bib1468)
 They proposed the
computed absolute magnetic shielding at ring centers (unweighted mean of the
heavy-atoms ring coordinates) as a new aromaticity criterion, called
nucleus-independent chemical shift (NICS). Aromatic rings show strong negative
shielding at the ring center (negative NICS), while anti-aromatic systems
reveal positive NICS at the ring center. As an example, a typical NICS value
for benzene is about $-11.5$ ppm as estimated with **Q-Chem** at the
Hartree-Fock/6-31G* level. The same NICS value for benzene was also
reported in Ref. [[1383]](../bib_references/bib.md#bib1468)
. The calculated NICS value for
furan of $-13.9$ ppm with **Q-Chem** is about the same as the value reported for
furan in Ref. [[1383]](../bib_references/bib.md#bib1468)
. Below is one input example of how
to the NICS of furan with **Q-Chem**, using the ghost atom option. The ghost
atom is placed at the center of the furan ring, and the basis set assigned to
it within the basis mix option must be the basis used for hydrogen atom.

???+ example "Example 10.60: Calculation of the NMR NICS probe of furan, HF/6-31G* level. Note the ghost
atom at the center of the ring."
    ```qchem
    $molecule
       0 1
       C    -0.69480       -0.62270       -0.00550
       C     0.72110       -0.63490        0.00300
       C     1.11490        0.68300        0.00750
       O     0.03140        1.50200        0.00230
       C    -1.06600        0.70180       -0.00560
       H     2.07530        1.17930        0.01410
       H     1.37470       -1.49560        0.00550
       H    -1.36310       -1.47200       -0.01090
       H    -2.01770        1.21450       -0.01040
       @H    0.02132        0.32584        0.00034
    $end
    
    $rem
       JOBTYPE               NMR
       METHOD                HF
       BASIS                 6-31G*
       PURCAR                111
       SCF_CONVERGENCE       7
       NO_REORIENT           1
       POINT_GROUP_SYMMETRY  FALSE
    $end
    ```
