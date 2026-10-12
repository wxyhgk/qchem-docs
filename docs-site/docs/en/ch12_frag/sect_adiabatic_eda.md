---
title: "12.7.3 Adiabatic ALMO-EDA and VFB Analysis"
---

## 12.7.3 Adiabatic ALMO-EDA and VFB Analysis

(July 4, 2026)

Despite the huge success and usefulness of today’s most popular EDA methods,
they still face some limitations in their capabilities. For instance, EDAs are
usually performed at complex geometries that are obtained from unconstrained
electronic structure calculations (*e.g.*, optimized equilibrium geometries). For
strongly interacting systems, close intermolecular contacts driven by POL and
particularly CT often result in largely unfavorable FRZ interaction, which
offers little physical insights besides indicating obviously substantial
intermolecular overlap. Another limitation is that the conventional EDA methods
often partitions a “single-point" interaction energy evaluated at a given
geometry. Therefore, the influence of FRZ, POL and CT on the structural and
vibrational properties of an intermolecular complex cannot be directly
characterized.

Recently Mao *et al.* reformulated the original ALMO-EDA method in an
adiabatic picture,[[894]](../bib_references/bib.md#bib928)
 where the term “adiabatic" is borrowed from
spectroscopy and indicates that energy differences are evaluated at
relaxed geometry on each potential energy surface. In this scheme, the
total binding energy (including monomer geometry distortions) is repartitioned
into adiabatic FRZ, POL and CT terms:

<a id="eq:ad_EDA"></a>

$$
\Delta E_{\mathrm{bind}}=\Delta E^{(\mathrm{ad})}_{\mathrm{frz}}+\Delta E^{(\mathrm{ad})}_{\mathrm{pol}}+\Delta E^{(\mathrm{ad})}_{\mathrm{ct}}. \tag{12.26}
$$

The adiabatic frozen interaction energy is given by the difference between the
energy minimum of the frozen potential surface (on which the energy of each point is computed
using the corresponding frozen wave function) and the sum of fully relaxed,
non-interacting fragment energies:

<a id="eq:ad_FRZ"></a>

$$
\Delta E^{(\mathrm{ad})}_{\mathrm{frz}}=E[\mathbf{P}_{\mathrm{frz}}^{(\mathrm{frz})}]-\sum_{A}E_{A}^{(0)}. \tag{12.27}
$$

Similarly, the adiabatic POL and CT terms can be obtained by performing
geometry optimizations on the polarized (SCF-MI) and fully relaxed
(unconstrained SCF) potential surfaces:

<a id="A3.S8.EGx122"></a>

$$
\displaystyle\Delta E^{(\mathrm{ad})}_{\mathrm{pol}} \tag{12.28}
$$

With this method, the changes in monomer structures and intermolecular
coordinates due to FRZ, POL and CT and the accompanied energetics are provided.
Moreover, at the energy minimum (or other stationary points) on each potential surface, the
other properties such as multipole points, vibrational frequencies and
intensities can also be computed, therefore the effect of different
intermolecular interaction components on them can also be characterized.

The geometry optimization on the frozen potential surface is facilitated by the analytical
gradient of the frozen wave function energy implemented in **Q-Chem**. As for the
geometry optimization on the polarized potential surface, the nuclear gradient of the SCF-MI
energy has the same form as that of the full SCF energy if the original ALMO
model is used. These analytical gradients can also be used for finite
difference calculations of harmonic frequencies by setting IDERIV = 1.
We note that the analytical gradients of SCF-MI calculations that use FERFs are
not available yet, and SCFMI_MODE = 0 is required for computing the
forces on the frozen and polarized potential surfaces. Also, the current implementation of
this method requires users to perform geometry optimization separately on the three potential surfaces
(see the example below) and then evaluate the energy components by taking
several **Q-Chem** outputs (including geometry optimizations for the monomers)
together, which is probably not so convenient. We look forward to extending the
functionality of this method and improving its implementation in the future.

As mentioned in Section [12.6.5](sect_eda2_job.md), for systems containing radicals of highly
symmetric geometries, the frozen wave function obtained from concatenating the
fragment MOs might be non-unique. In those cases, we recommend the user to set
EDA_ALIGN_FRGM_SPIN = 1 or 2 when performing geometry optimization
on the frozen potential surface. The job will then go through the fragment spin alignment procedure
in each optimization cycle.

### `FRZ_GEOM`

> **Compute forces on the frozen potential surface.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not compute forces on the frozen potential surface.
>     * `TRUE`: Compute forces on the frozen potential surface.
> * **Recommendation**: Set it to TRUE when optimized geometry or vibrational frequencies on the frozen potential surface are desired.

### `POL_GEOM`

> **Compute forces on the polarized (converged SCF-MI) potential surface.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not compute forces on the polarized potential surface.
>     * `TRUE`: Compute forces on the polarized potential surface.
> * **Recommendation**: Set it to TRUE when optimized geometry or vibrational frequencies on the polarized potential surface are desired.

???+ example "Example 12.12.30: Geometry optimization of the ammonia-borane complex on the fully relaxed,
polarized, and frozen potential energy surfaces successively."
    ```qchem
    $molecule
    0 1
    --
    0 1
    H       0.000000     0.000000     0.000000
    H       0.000000     0.000000     1.629090
    H       1.417687     0.000000     0.814543
    N       0.473683    -0.370067     0.814542
    --
    0 1
    N       3.494032    -1.531250     0.814538
    H       3.967715    -1.901317    -0.000008
    H       2.550028    -1.901319     0.814537
    H       3.967715    -1.901317     1.629083
    $end
    
    $rem
       JOBTYPE          opt  !optimization on the fully relaxed PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCF_GUESS        fragmo
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE          opt
       POL_GEOM         true !optimization on the polarized PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCFMI_MODE       0
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE          opt
       FRZ_GEOM         true !optimization on the frozen PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCFMI_MODE       0
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 12.31: Geometry optimization of the [Cu(CO)] ${}^{+}$ complex on the frozen potential surface, followed by
a frequency calculation which is computed via finite differences."
    ```qchem
    $molecule
    1 1
    --
    0 1
    C         0.0000000000    0.0000000000    1.3792049588
    O         0.0000000000    0.0000000000    2.4988670685
    --
    1 1
    Cu        0.0000000000    0.0000000000   -0.9778656750
    $end
    
    $rem
       JOBTYPE            opt
       FRZ_GEOM           true
       METHOD             b3lyp
       BASIS              def2-svp
       UNRESTRICTED       false
       IDERIV             1
       FD_MAT_VEC_PROD    false
       INTEGRAL_SYMMETRY  false
       POINT_GROUP_SYMMETRY true
    $end
    
    
    @@@
    
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           freq
       FRZ_GEOM          true
       METHOD            b3lyp
       BASIS             def2-svp
       UNRESTRICTED      false
       IDERIV            1
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY true
    $end
    ```

To further understand the charge-transfer effects in dative complexes, in **Q-Chem**
5.2.2 and after, one is allowed to separate the overall CT into contributions from
forward and backward donations using the variational forward-backward (VFB)
approach.[[857]](../bib_references/bib.md#bib891)
 Such a decomposition is achieved by introducing
two additional constrained intermediate states in which only one direction of CT is
permitted. These two “one-way” CT states are variationally relaxed such that the
associated nuclear forces can be readily obtained. This allows for a facile integration
into the adiabatic ALMO-EDA scheme introduced above:

<a id="A3.S8.EGx123"></a>

$$
\displaystyle\Delta E^{(\mathrm{ad})}_{\mathrm{ctf}} \tag{12.30}
$$

and thus the molecular property changes arising from forward and backward donations
can be separately assigned. Note that in its **Q-Chem** implementation, the evaluation of
a VFB state always follows a polarization (standard SCF-MI) calculation. Also, since the
definition of VFB states is based on the generalized SCF-MI technique (Section [12.6.2](sect_gen_scfmi.md)),
SCFMI_MODE = 1 is required.

### `VFB_CTA`

> **Use the Variational Forward-Backward (VFB) approach to obtain “one-way” CT potential surfaces.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * `FORWARD`: Allow 1 $\rightarrow$ 2 CT only (1 and 2 are two fragments).
>     * `BACKWARD`: Allow 2 $\rightarrow$ 1 CT only.
> * **Recommendation**: None

???+ example "Example 12.32: Geometry optimization on one-side CT surface (2 $\to$ 1)
using the variational forward-backward (VFB) approach"
    ```qchem
    $molecule
       0 1
       --
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
       --
       0 1
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            wb97x-d
       BASIS             6-31g
       VFB_CTA           backward
       THRESH            14
       SCF_CONVERGENCE   9
       SCF_ALGORITHM     DIIS
       IDERIV            1
       SCFMI_MODE        1
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

In **Q-Chem** v. 5.4 or later, analytical gradients for the polarized and two VFB “one-way” CT
states with implicit solvent models PCM and SMD are supported so that one can perform
part of the adiabatic ALMO-EDA steps (POL $\rightarrow$ CTf/CTb $\rightarrow$ Full)
in solvation environments. To do this, one only needs to set the *$rem* variable
SOLVENT_METHOD to PCM or SMD, which is similar to the usage of ALMO-EDA(solv)
(see Section [12.6.6](sect_eda2_sol.md)). The calculation of analytical forces on the frozen surface with
implicit solvents is currently unavailable, and we look forward to enabling that in future
releases of **Q-Chem**.

???+ example "Example 12.33: Geometry optimization on the polarized surface with
SMD solvent model"
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
       JOBTYPE           OPT
       METHOD            wB97X-D
       BASIS             cc-pVDZ
       POL_GEOM          TRUE
       THRESH            14
       SCF_CONVERGENCE   9
       MEM_TOTAL         2000
       MEM_STATIC        500
       SCF_GUESS         FRAGMO
       IDERIV            1
       SCFMI_MODE        0
       SOLVENT_METHOD    SMD
       INTEGRAL_SYMMETRY FALSE
       POINT_GROUP_SYMMETRY FALSE
    $end
    
    $smx
       solvent water
    $end
    ```
