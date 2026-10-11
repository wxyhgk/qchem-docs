---
title: "9.5.2 Application of Pressure"
---

## 9.5.2 Application of Pressure

(July 4, 2026)

**Q-Chem** features a number of methods to apply pressure to a chemical system
during a geometry optimization or an AIMD simulation.[[1298]](../bib_references/bib.md#bib1354)
 The
following methods are implemented:

| Hydrostatic Compression Force Field (HCFF) [[1295]](../bib_references/bib.md#bib1352) | Section 9.5.2.1 |
| --- | --- |
| eXtended Hydrostatic Compression Force Field (X-HCFF) [[1297]](../bib_references/bib.md#bib1353) | Section 9.5.2.2 |
| Pressure times Volume term (PV) [[1540]](../bib_references/bib.md#bib1604) | Section 9.5.2.3 |
| Gaussians on Surface Tesserae Simulate HYdrostatic Pressure (GOSTSHYP) [[1206]](../bib_references/bib.md#bib1261) | Section 9.5.2.4 |

To invoke one of these methods, set DISTORT = TRUE in the *$rem* section.
By setting the *$rem* variable SCF_FINAL_PRINT = 1,
the energy contribution due to pressure is printed in the output.

DISTORT

### `DISTORT`

> **Specifies whether to apply pressure or external force to a chemical system**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * False
>     * Do not use pressure or force
>     * True
>     * Use pressure or force
> * **Recommendation**: Set to true to apply pressure or force.

The parameters of the jobs are set *via* options specified in the
*$distort* input section. The format of the *$distort* section is analogous to the *$rem* section:

> ```qchem
> $distort
>   <Keyword>  <parameter/option>
> $end
> ```

**Note: 

The following job control variables belong *only* in the *$distort* 
section. Do not place them in the *$rem* section.
**

### `Model`

> **Specifies which model is used to distort the molecule. INPUT SECTION: $distort**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * HCFF
>     * Hydrostatic Compression Force Field
>     * 1295
>     * Stauch T., Chakraborty R., Head-Gordon M.
>     * ChemPhysChem
>     * (2019)
>     * ,
>     * 20
>     * ,
>     * pp. 2742
>     * .
>     * Link
>     * XHCFF
>     * eXtended Hydrostatic Compression Force Field
>     * 1297
>     * Stauch T.
>     * J. Chem. Phys.
>     * (2020)
>     * ,
>     * 153
>     * ,
>     * pp. 134503
>     * .
>     * Link
>     * PV
>     * Add PV term by computing vDW volume
>     * 1540
>     * Zeller F., Pracht P., Neudecker T.
>     * J. Phys. Chem. A
>     * (2025)
>     * ,
>     * 129
>     * ,
>     * pp. 2108
>     * .
>     * Link
>     * GOSTSHYP
>     * Gaussians On Surface Tesserae Simulate HYdrostatic Pressure
>     * 1206
>     * Scheurer M. et al.
>     * J. Chem. Theory Comput.
>     * (2021)
>     * ,
>     * 17
>     * ,
>     * pp. 583
>     * .
>     * Link
>     * EFEI
>     * External Force is Explicitly Included (Section
>     * 9.5.1
>     * )
> * **Recommendation**: Please refer to the following subsections for recommendations on which model to use.

### `Pressure`

> **Specifies the pressure (in MPa) used to compress the molecule. INPUT SECTION: $distort**
>
> * **Type**: `DOUBLE`
> * **Default**: `None`
> * **Options**:
>     * User defined
> * **Recommendation**: None

### `NPoints_Heavy`

> **Specifies the number of tessellation points per non-hydrogen atom. INPUT SECTION: $distort**
>
> * **Type**: `INTEGER`
> * **Default**: `110`
> * **Options**:
>     * User defined
> * **Recommendation**: Use the default.

### `NPoints_Hydrogen`

> **Specifies the number of tessellation points per hydrogen atom. INPUT SECTION: $distort**
>
> * **Type**: `INTEGER`
> * **Default**: `110`
> * **Options**:
>     * User defined
> * **Recommendation**: Use the default.

### `Scaling`

> **Specifies the scaling factor of the atomic van der Waals radii used in the tessellation of the molecular surface, which is used in the pressure models. INPUT SECTION: $distort**
>
> * **Type**: `DOUBLE`
> * **Default**: `1.2`
> * **Options**:
>     * User defined
> * **Recommendation**: Increase when modeling a chemical complex to make sure that the complex is placed inside a single cavity. 1206 Scheurer M. et al. J. Chem. Theory Comput. (2021) , 17 , pp. 583 . Link A value of 1.0 was suggested to be used in the X-HCFF model. 1297 Stauch T. J. Chem. Phys. (2020) , 153 , pp. 134503 . Link

### `tess_method`

> **Choose method for tessellation INPUT SECTION: $distort**
>
> * **Type**: `STRING`
> * **Default**: `scrf`
> * **Options**:
>     * scrf
>     * use the same tessellation code as implicit solvation models
>     * distort
>     * use libdistort tessellation routine
>     * occ
>     * use outer cavity correction
> * **Recommendation**: Use distort option for compatibility with implicit solvation models in the same calculation. Scrf option allows for more cavity options. OCC allows to reduce the amount of negative amplitudes - use for GOSTSHYP calculations with bad SCF convergence.

### `proberad`

> **Add proberad to vDW radii to resemble the solvent accessible surface (SAS). INPUT SECTION: $distort**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.0`
> * **Options**:
>     * User defined

### `occrad`

> **Distance to outer cavity for OCC GOSTSHYP calculations. INPUT SECTION: $distort**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.25`
> * **Options**:
>     * User defined
> * **Recommendation**: Smaller values will lead to higher probability of negative amplitudes, larger values lead to discarding many tessellation points.

## 9.5.2.1 Hydrostatic Compression Force Field (HCFF)

The Hydrostatic Compression Force Field (HCFF) model was introduced by Stauch,
Chakraborty and Head-Gordon.[[1295]](../bib_references/bib.md#bib1352)
 In HCFF, mechanical forces that
point towards the non-mass-weighted molecular centroid are used to compress a
molecule. Care must be exercised when modeling extended molecules due to the
tendency of HCFF to generate spherical geometries under very high
pressure.[[1298]](../bib_references/bib.md#bib1354)
 Also, the pressure input by the user is only a
guess for the pressure that is applied to the molecule. The latter is
calculated *a posteriori* based on the generated geometry and the
molecular surface and is output as *HCFF Macroscopic Pressure*. Typically,
the applied pressure is lower than the input pressure. It should be noted that
the dependence on the nuclear gradient precludes the application of pressure to
single atoms in HCFF. Moreover, the increase in electronic energy when
compressing a molecule is typically underestimated by HCFF, since the pressure
acts only on the nuclei, whereas the compression of electron density is not
modeled directly. HCFF works with any electronic structure method for which a
nuclear gradient is available.

???+ example "Example 9.16: Geometry optimization of diborane under pressure using the
HCFF model with an input pressure of 3808 MPa"
    ```qchem
    $molecule
       0 1
       B     0.0000000000    0.0000000000    0.8917854534
       B     0.0000000000    0.0000000000   -0.8917854534
       H    -0.5244343500    0.9105724300    1.4720415209
       H     0.5244343500   -0.9105724300    1.4720415209
       H    -0.5244343500    0.9105724300   -1.4720415209
       H     0.5244343500   -0.9105724300   -1.4720415209
       H     0.8561835151    0.4929549655    0.0000000000
       H    -0.8561835151   -0.4929549655    0.0000000000
    $end
    
    $rem
       JOBTYPE            opt
       METHOD             m06-2x
       BASIS              6-311++G(d,p)
       DISTORT            true
    $end
    
    $distort
       model              hcff
       pressure           3808
       scaling            1.0
       npoints_heavy      590
       npoints_hydrogen   590
    $end
    ```

## 9.5.2.2 eXtended Hydrostatic Compression Force Field (X-HCFF)

The eXtended Hydrostatic Compression Force Field (X-HCFF) approach was introduced
by Stauch to solve the problems associated with HCFF.[[1297]](../bib_references/bib.md#bib1353)
 In X-HCFF,
mechanical forces are used to compress the molecule as well, but, in contrast to
HCFF, these forces are strictly perpendicular to the tessellated molecular surface,
thus simulating truly hydrostatic conditions. As a result, chemically feasible
geometries are retained even at high pressures. In addition, the user is able to
input the precise pressure that is applied to the molecule during the simulation.
It was suggested to use the unscaled atomic van der Waals radii in the tessellation
routine.[[1297]](../bib_references/bib.md#bib1353)
 X-HCFF works with any electronic structure method for
which a nuclear gradient is available.
It is also possible to perform an analytic Hessian
calculation with X-HCFF using JOBTYPE = FREQ, to obtain related
structural properties such as IR and Raman frequencies.[[1447]](../bib_references/bib.md#bib1509)

It should be noted that the forces formulated for the X-HCFF model are not
derived as the derivative of an energy term, but direcctly formulated and added to
gradient. Thus no corresponding energy term is added to the electronic energy
and consequently pressure induced increases in electronic energy are typically low.
The X-HCFF forces can be understood as a approximation to the gradient of the
vDW volume.[[1540]](../bib_references/bib.md#bib1604)

???+ example "Example 9.17: Geometry optimization of the CO ${}_{2}$ dimer under a pressure of
100 GPa using the X-HCFF model"
    ```qchem
    $molecule
       0 1
       O    2.6192991230   -0.0571311942    0.0000000000
       C    1.6782610262    0.6502025480    0.0000000000
       O    0.7413912820    1.3674070371    0.0000000000
       C   -1.6782610262   -0.6502025480    0.0000000000
       O   -2.6192991230    0.0571311942    0.0000000000
       O   -0.7413912820   -1.3674070371    0.0000000000
    $end
    
    $rem
       JOBTYPE            opt
       METHOD             pbe
       BASIS              cc-pvdz
       DISTORT            true
    $end
    
    $distort
       model              xhcff
       pressure           100000
       scaling            1.0
       npoints_heavy      302
       npoints_hydrogen   302
    $end
    ```

## 9.5.2.3 PV term

The enthalpy $H$ of a molecular system in an arbitrary pressure exerting medium may
be expressed as the sum of the electronic energy $E_{el}$ and the pressure $P$ times
the volume $V$ occupied by the molecule.

<a id="Ch9.E44"></a>
$$
H=E_{el}+PV \tag{9.44}
$$

The probably most simple approximation for the molecular Volume is the vDW Volume,
which is used here. It can be calculated by numerical integration of the molecular
vDW surface (see [11.2.3.2](../ch11_env/topic_pcm-em.md#subsubsec:pcm_cavity)) and leads to a well defined contribution
to the molecular gradient.[[1540]](../bib_references/bib.md#bib1604)
 This approach leads to pressure induced deformations similar
to the X-HCFF model, however it provides a far more realistic correction to the energy.

A Hessian is available, to obtain IR and Raman frequencies using frequency calculations.

## 9.5.2.4 Gaussians On Surface Tesserae Simulate HYdrostatic Pressure (GOSTSHYP)

The Gaussians On Surface Tesserae Simulate HYdrostatic Pressure (GOSTSHYP)
method, which was introduced by Scheurer and co-workers,[[1206]](../bib_references/bib.md#bib1261)

overcomes the problems associated with the mechanochemical models of pressure,
*i.e.* HCFF and X-HCFF. GOSTSHYP uses a uniform field of Gaussian potentials
that is placed on the tessellated molecular surface and that compresses the
electron density. Each Gaussian potential G${}_{j}$ has the form

<a id="Ch9.E45"></a>
$$
G_{j}=p_{j}\cdot\exp\left(-w_{j}(\textbf{r}-\textbf{r}_{0})^{2}\right) \tag{9.45}
$$

During the GOSTSHYP routine, the parameters of the Gaussian potentials, $p_{j}$ and
$w_{j}$, are adjusted such that a user-defined pressure is applied. Atoms and molecules
can be treated, and the pressure-induced increase in the electronic energy is
physically sound. During the SCF, the energy expression takes the form

<a id="A3.S8.EGx72"></a>
$$
\displaystyle E_{\text{GOSTSHYP}} \tag{9.46}
$$

Due to the availability of nuclear gradients, geometry optimizations under pressure
using the GOSTSHYP model are possible. At present, GOSTSHYP is implemented at the SCF
level, allowing calculations with Hartree-Fock and Density Functional Theory.

For good performance GOSTSHYP needs relatively large amounts of available RAM. If not
enough available RAM is detected, GOSTSHYP will switch to a memory efficient algorithm
at the cost of performance, a warning containing the required amount of memory for better
performance will be printed in the output.

We found, that at the edges between the tessellation spheres of two atoms "negative amplitudes"
$p_{j}$ may appear. Since those would lead to nonphysical attractive pressure potentials
they are generally blacklisted in GOSTSHYP calculations. This however leads to instabilities
within SCF calculations. We found that negative amplitudes appear very rarely for VDW-scaling
factors larger than $1.5$ but become more likely to appear for smaller scaling factors.
Alternaively the solvent accessible surface (SAS) (see [11.2.3.2](../ch11_env/topic_pcm-em.md#subsubsec:pcm_cavity)) may be
used with a similar effect by defining a proberadius. We recently proposed the outer cavity
corrextion (OCC),[[1048]](../bib_references/bib.md#bib1093)
 which should lead to a far better convergence.
To use this correction set tess_method to occ.

???+ example "Example 9.18: Geometry optimization of cyclopentadiene and ethylene under a pressure
of 40 GPa using the GOSTSHYP model"
    ```qchem
    $molecule
       0 1
       C    1.1148422354   -0.6418674001    0.7279292386
       C    1.1148422354   -0.6418674001   -0.7279292386
       C    0.5936432126    0.5363396649    1.1772168767
       C   -2.0464511598   -0.6129291257    0.6711240568
       C   -2.0464511598   -0.6129291257   -0.6711240568
       C    0.5936432126    0.5363396649   -1.1772168767
       C    0.2915208637    1.4128825196    0.0000000000
       H    0.9756522868    2.2894492537    0.0000000000
       H   -0.7374232239    1.8214336422    0.0000000000
       H    1.4681344173   -1.4690333337   -1.3527755131
       H    1.4681344173   -1.4690333337    1.3527755131
       H   -2.3879086093    0.2541525765    1.2531118994
       H   -1.7231567891   -1.4887031107    1.2461940178
       H   -1.7231567891   -1.4887031107   -1.2461940178
       H   -2.3879086093    0.2541525765   -1.2531118994
       H    0.4773764265    0.8454441265    2.2200767812
       H    0.4773764265    0.8454441265   -2.2200767812
    $end
    
    $rem
       JOBTYPE               opt
       METHOD                pbe
       BASIS                 cc-pvdz
       GEOM_OPT_MAX_CYCLES   150
       SCF_ALGORITHM         diis_gdm
       MAX_SCF_CYCLES        150
       USE_LIBQINTS          1
       GEN_SCFMAN            1
       DISTORT               1
    $end
    
    $distort
       model                 gostshyp
       pressure              40000
       npoints_heavy         302
       npoints_hydrogen      302
       scaling               1.8
    $end
    ```
