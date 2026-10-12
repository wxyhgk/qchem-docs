---
title: "10.5.8 Electrostatic Potentials"
---

## 10.5.8 Electrostatic Potentials

(July 4, 2026)

**Q-Chem** can evaluate electrostatic potentials on a grid of points.
Electrostatic potential (ESP) evaluation is controlled by the *$rem* variable ESP_GRID.

**Note: 

For backwards compatibility with the **Q-Chem**/**Charmm** interface, the name IGDESP is equivalent to ESP_GRID.
**

### `ESP_GRID`

> **Controls evaluation of the electrostatic potential on a grid of points. If enabled, the output is in an ASCII file, plot.esp , in the format $x,y,z,\phi(x,y,z)$ for each point, where $\phi$ is the ESP.**
>
> * **Type**: `INTEGER`
> * **Default**: `-4`
> * **Options**:
>     * $-1$: read grid input via the $plots section of the input deck $-2$ same as the option $-1$ , plus evaluate the ESP of the $external_charges $-3$ same as the option $-1$ but in connection with STATE_ANALYSIS =
>     * `TRUE`: . This computes the ESP for all excited-state densities, transition densities, and electron/hole densities. $-4$ No ESP evaluation $0$ Generate the ESP values at all nuclear positions +
>     * $n$: read
>     * $n$: grid points in bohr from the ASCII file ESPGrid
> * **Recommendation**: For the $+n$ option, the user should also specify NO_REORIENT = TRUE . This forces Q-Chem to use the user’s coordinate frame (as established in the $molecule section), which should be the same coordinate frame used in the ESPGrid file.

The following example illustrates the evaluation of electrostatic potentials on
a grid. Note that IANLTY must also be set to 200.

???+ example "Example 10.32: A job that evaluates the electrostatic potential for H ${}_{2}$ on a 1 by 1 by 15
grid, along the bond axis. The output is in an ASCII file called plot.esp , which lists for each grid point, $x$ , $y$ , $z$ , and the
electrostatic potential."
    ```qchem
    $molecule
       0  1
       H   0.0   0.0   0.35
       H   0.0   0.0  -0.35
    $end
    
    $rem
       METHOD     hf
       BASIS      6-31g**
       IANLTY     200
       ESP_GRID     -1
    $end
    
    $plots
       plot the electrostatic potential on a line
       1   0.0   0.0
       1   0.0   0.0
      15  -3.0   3.0
       0  0  0  0
       0
    $end
    ```

The example below evaluates ESP on a plotting grid and generates a cube file,
which can be loaded by IQmol to visualize ESP on a molecular surface (*e.g.* vdW
surface or electron density isosurface).

???+ example "Example 10.33: Calculating the ESP of acetyl chloride on a user-specified grid and generate a
cube file as the result; the new format for the $plots section is used"
    ```qchem
    $molecule
     0 1
     C       0.00000     1.18959     1.29360
     H       0.00000     1.01580     2.37206
     H       0.88291     1.76694     1.00084
     H      -0.88291     1.76694     1.00084
     C       0.00000    -0.13357     0.57945
     O       0.00000    -1.22212     1.05977
     Cl      0.00000     0.06441    -1.23718
    $end
    
    $rem
     jobtype  sp
     method   b3lyp
     basis    6-31g(d)
     point_group_symmetry False
     scf_convergence  8
     esp_grid  -1
     make_cube_files  true
     plots    true
     gui      2
    $end
    
    $plots
     grid_points 50 50 50
     grid_range (-4,4) (-5,5) (-5,5)
    $end
    ```

We can also compute the electrostatic potential for the transition density,
which can be used, for example, to compute the Coulomb coupling in excitation energy transfer.

### `ESP_TRANS`

> **Controls the calculation of the electrostatic potential of the transition density**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: compute the electrostatic potential of the excited state transition density
>     * `FALSE`: compute the electrostatic potential of the excited state electronic density
> * **Recommendation**: NONE

The electrostatic potential is a complicated object and it is not uncommon to
model it using a simplified representation based on atomic charges. For this
purpose it is well known that Mulliken charges perform very poorly. Several
definitions of ESP-derived atomic charges have been given in the literature,
however, most of them rely on a least-squares fitting of the ESP evaluated on a
selection of grid points. Although these grid points are usually chosen so
that the ESP is well modeled in the “chemically important” region, it still
remains that the calculated charges will change if the molecule is rotated.
Recently an efficient rotationally invariant algorithm was proposed that sought
to model the ESP not by direct fitting, but by fitting to the multipole
moments.[[1255]](../bib_references/bib.md#bib1308)
 By doing so it was found that the fit to the ESP
was superior to methods that relied on direct fitting of the ESP. The
calculation requires the traceless form of the multipole moments and these are
also printed out during the course of the calculations. To request these
multipole-derived charges, set MM_CHARGES = TRUE in the *$rem* section.

### `MM_CHARGES`

> **Requests the calculation of multipole-derived charges (MDCs).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Calculates the MDCs and also the traceless form of the multipole moments
> * **Recommendation**: Set to TRUE if MDCs or the traceless form of the multipole moments are desired. The calculation does not take long.
