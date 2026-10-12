---
title: "10.5.5 Direct Generation of “Cube” Files"
---

## 10.5.5 Direct Generation of “Cube” Files

(July 4, 2026)

As an alternative to the output format discussed above, all of the *$plots*
data may be output directly to a sub-directory named `plots` in the job’s
scratch directory, which must therefore be saved using the *–save* option
described in Section [2.2](../ch02_install/sect_running.md). The plotting data in this
sub-directory are not written in the `plot.*` format described above, but
rather in the form of so-called “cube” file, one for each orbital or density
that is requested. The cube file format is a standard one for volumetric data
and consists of a small header followed by the orbital or density values at
each grid point, in ASCII format. (Consult Ref. 

 for
the complete format specification.) Because the grid coordinates themselves are
not printed (their locations are implicit from information contained in the
header), each individual cube file is much smaller than the corresponding
`plot.*` file would be. Cube files can be read by many standard (and
freely-available) graphics programs, including
**MacMolPlt[[136]](../bib_references/bib.md#bib126)
[[12]](../bib_references/bib.md#bib16)
** and **VMD**.[[604]](../bib_references/bib.md#bib627)
[[15]](../bib_references/bib.md#bib19)

VMD, in particular, is recommended for generation of high-quality images for
publication. Cube files for the MOs and densities requested in the *$plots*
section are requested by setting MAKE_CUBE_FILES to TRUE,
with the *$plots* section specified as described in Section [10.5.4](sect_plot.mo.md).

### `MAKE_CUBE_FILES`

> **Requests generation of cube files for MOs, NTOs, or NBOs.**
>
> * **Type**: `LOGICAL/STRING`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not generate cube files.
>     * `TRUE`: Generate cube files for MOs and densities.
>     * `NTOS`: Generate cube files for NTOs.
>     * `NBOS`: Generate cube files for NBOs.
> * **Recommendation**: None

### `PLOT_SPIN_DENSITY`

> **Requests the generation of spin densities, $\rho_{\alpha}$ and $\rho_{\beta}$ .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not generate spin density cube files.
>     * `TRUE`: Generate spin density cube files.
> * **Recommendation**: Set to TRUE if spin densities are desired in addition to total densities. Requires that MAKE_CUBE_FILES be set to TRUE as well, and that one or more total densities is requested in the $plots input section. The corresponding spin densities will then be generated also.

The following example illustrates the generation of cube files for a ground and
an excited-state density, including the corresponding spin densities. In this
example, the `plots` sub-directory of the job’s scratch directory should
contain files named `dens.N.cube` (total density for state $N$, where $N=0$
or 1 represents the ground and first excited state, respectively), `dens_alpha.N.cube` and `dens_beta.N.cube` ($\rho_{\alpha}$ and $\rho_{\beta}$
for each state), and `dens_spin.N.cube` ($\rho_{\alpha}-\rho_{\beta}$ for
each state.)

???+ example "Example 10.27: Generating density and spin-density cube files for the ground and first
excited state of the HOO radical."
    ```qchem
    $molecule
       0 2
       H     1.004123   -0.180454    0.000000
       O    -0.246002    0.596152    0.000000
       O    -1.312366   -0.230256    0.000000
    $end
    
    $rem
       PLOT_SPIN_DENSITY  true
       MAKE_CUBE_FILES    true
       SCF_CONVERGENCE    8
       METHOD             b3lyp
       BASIS              6-31+G*
       CIS_N_ROOTS        1
    $end
    
    $plots
    grid information and request to plot 2 densities
       20  -5.0  5.0
       20  -5.0  5.0
       20  -5.0  5.0
       0  2  0  0
       0  1
    $end
    ```

Cube files are also available for natural transition orbitals
(Sections [7.13.3](../ch07_excited/sect_NTOs.md) and [10.5.3](sect_visualize_NTOs.md)) by setting
MAKE_CUBE_FILES to NTOS, although in this case the
procedure is somewhat more complicated, due to the state-specific nature of
these quantities. Cube files for the NTOs are generated only for a single
excited state, whose identity is specified using CUBEFILE_STATE.
Cube files for additional states are readily obtained using a sequence of
**Q-Chem** jobs, in which the second (and subsequent) jobs read in the converged
ground- and excited-state information using SCF_GUESS and
SKIP_CIS_RPA.

### `CUBEFILE_STATE`

> **Determines which excited state is used to generate cube files**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: Generate cube files for the
>     * $n$: th excited state
> * **Recommendation**: None

An additional complication is the manner in which to specify which NTOs will be
output as cube files. When MAKE_CUBE_FILES is set to TRUE,
this is specified in the *$plots* section, in the same way that MOs would be
specified for plotting. However, one must understand the order in which the
NTOs are stored. For a system with $N_{\alpha}$ $\alpha$-spin MOs, the occupied
NTOs $1,2,\ldots,N_{\alpha}$ are stored in order of increasing amplitudes, so
that the $N_{\alpha}$’th occupied NTO is the most important. The virtual NTOs
are stored next, in order of *decreasing* importance. According to this
convention, the principle NTO pair consists of the final occupied orbital and
the first virtual orbital, for any particular excited state. Thus, orbitals
$N_{\alpha}$ and $N_{\alpha}+1$ represent the most important NTO pair, while
orbitals $N_{\alpha}-1$ and $N_{\alpha}+2$ represent the second most important NTO
pair, *etc.*.

???+ example "Example 10.28: Generating cube files for the excitation between the principle occupied and
virtual NTOs of the second singlet excited state of uracil. Note that $N_{\alpha}=29$ for uracil."
    ```qchem
    $molecule
       0 1
       N    -2.181263     0.068208     0.000000
       C    -2.927088    -1.059037     0.000000
       N    -4.320029    -0.911094     0.000000
       C    -4.926706     0.301204     0.000000
       C    -4.185901     1.435062     0.000000
       C    -2.754591     1.274555     0.000000
       N    -1.954845     2.338369     0.000000
       H    -0.923072     2.224557     0.000000
       H    -2.343008     3.268581     0.000000
       H    -4.649401     2.414197     0.000000
       H    -6.012020     0.301371     0.000000
       H    -4.855603    -1.768832     0.000000
       O    -2.458932    -2.200499     0.000000
    $end
    
    $plots
    Plot the dominant NTO pair, N --&gt; N+1
       25  -5.0  5.0
       25  -5.0  5.0
       25  -5.0  5.0
       2  0  0  0
       29  30
    $end
    
    $rem
       METHOD           B3LYP
       BASIS            6-31+G*
       CIS_N_ROOTS      2
       CIS_TRIPLETS     FALSE
       NTO_PAIRS        TRUE    ! calculate the NTOs
       MAKE_CUBE_FILES  NTOS    ! generate NTO cube files...
       CUBEFILE_STATE   2       ! ...for the 2nd excited state
    $end
    ```

Cube files for Natural Bond Orbitals (for either the ground state
or any CIS, RPA, of TDDFT excited states) can be generated in much the
same way, by setting MAKE_CUBE_FILES equal to NBOS,
and using CUBEFILE_STATE to select the desired electronic state.
CUBEFILE_STATE = 0 selects ground-state NBOs. The particular
NBOs to be plotted are selected using the *$plots* section, recognizing
that **Q-Chem** stores the NBOs in order of decreasing occupancies, with
all $\alpha$-spin NBOs preceding any $\beta$-spin NBOs, in the case of an
unrestricted SCF calculation. (For ground states, there is typically one
strongly-occupied
NBO for each electron.) NBO cube files are saved to the
`plots` sub-directory of the job’s scratch directory. One final
caveat: to get NBO cube files, the user must specify the AONBO
option in the *$nbo* section, as shown in the following example.

???+ example "Example 10.29: Generating cube files for the NBOs of the first excited state of $\rm H_{2}O$ ."
    ```qchem
    $rem
       METHOD           CIS
       BASIS            CC-PVTZ
       CIS_N_ROOTS      1
       CIS_TRIPLETS     FALSE
       NBO              2      ! ground- and excited-state NBO
       MAKE_CUBE_FILES  NBOS   ! generate NBO cube files...
       CUBEFILE_STATE   1      ! ...for the first excited state
    $end
    
    $nbo
      AONBO
    $end
    
    $molecule
       0 1
       O
       H  1  0.95
       H  1  0.95  2  104.5
    $end
    
    $plots
    Plot the 5 high-occupancy NBOs, one for each alpha electron
       40  -8.0  8.0
       40  -8.0  8.0
       40  -8.0  8.0
       5  0  0  0
       1  2  3  4  5
    $end
    ```

???+ example "Example 10.30: NTO and NBO plots with the new format for the $plots section:
NTOs for the first excited state (two pairs) and five NBOs for
both the ground and first excited state are plotted.
The aonbo keyword in the nbo section below is required."
    ```qchem
    $molecule
      0 1
       O
       H 1 0.95
       H 1 0.95 2 104.5
    $end
    
    $rem
       METHOD¯¯     cis
       BASIS¯¯     cc-pvtz
       CIS_N_ROOTS       1
       CIS_TRIPLETS      false
       nbo               2  ! ground- and excited-state NBO
       NTO_PAIRS         2  ! triggers NTO analysis
       MAKE_CUBE_FILES   true
       PLOTS             true
    $end
    
    $nbo
       aonbo
    $end
    
    $plots
       grid_points 50 50 50
       nbo_state   0-1
       natural_bond_orbital 1-5
       natural_transition_orbital 1
    $end
    ```

It is also possible to obtain Molecular Orbital (MO) or ground-state electron
density cube files from Complex-Absorbing-Potential Hartree-Fock (CAP-HF) or
Density Functional Theory (CAP-DFT) calculations. No adjustment in the plot
ection is required, however the user should pay attention in order to identify
which cube file contains which spatial function. For each requested MO with
index $N$, three files will be printed:

- •

mo.$N$.cube contains the real-valued MO prior to addition of the
CAP.
- •

mo.$\left(1000+N\right)$.cube contains the real part of the
complex MO after convergence of the CAP-SCF calculation.
- •

mo.$\left(1000+N+o\right)$.cube contains the imaginary part
of the complex MO after convergence of the CAP-SCF calculation. $o$ is
equal to the total number of spin orbitals calculated for the molecule.

For the ground-state density, the three files will have indices 0, 1000 and 1001.
They contain the density prior to CAP addition, and the real and imaginary density
after CAP-SCF convergence respectively.
