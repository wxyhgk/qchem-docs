---
title: "11.2.6 Isodensity Implementation of SS(V)PE"
---

## 11.2.6 Isodensity Implementation of SS(V)PE

(July 4, 2026)

## 11.2.6.1 Basic Job Control

As discussed above, results obtained various types of PCMs are quite sensitive
to the details of the cavity construction. **Q-Chem**’s implementation of PCMs,
using Lebedev grids, simplifies this construction somewhat, but leaves the
radii of the atomic spheres as empirical parameters (albeit ones for which
widely-used default values are provided). An alternative implementation of the
SS(V)PE solvation model is also available,[[242]](../bib_references/bib.md#bib247)
 which attempts
to further eliminate empiricism associated with cavity construction by taking
the cavity surface to be a specified iso-contour of the solute’s electron
density. [We call this the isodensity implementation of SS(V)PE in
Table [11.3](topic_pcm-em.md#table:K-matrix), and it is based on Chipman’s “symmetrized” form
of the $\mathbf{K}$ matrix,[[242]](../bib_references/bib.md#bib247)

although the difference between symmetric and asymmetric forms is essentially negligible
when an isodensity cavity construction is used.[[242]](../bib_references/bib.md#bib247)
]
In this case, the
cavity surface is discretized by projecting a single-center Lebedev grid onto
the iso-contour surface. Unlike the PCM implementation discussed in
Section [11.2.3](topic_pcm-em.md), for which point-group symmetry is disabled, this
implementation of SS(V)PE supports full symmetry for all Abelian point groups.
The larger and/or the less spherical the solute molecule is, the more points
are needed to get satisfactory precision in the results. Further experience
will be required to develop detailed recommendations for this parameter.
Values as small as 110 points are usually sufficient for diatomic or triatomic
molecules. The default value of 1202 points is adequate to converge the energy
within 0.1 kcal/mol for solutes the size of mono-substituted benzenes.

Energy gradients are also not available for this implementation of SS(V)PE,
although they are available for the implementation described in
Section [11.2.3](topic_pcm-em.md) in which the cavity is constructed from atom-centered
spheres. As with the PCMs discussed in that section, the solute may be
described using Hartree-Fock theory or DFT; post-Hartree–Fock correlated wave
functions can also take advantage of molecular orbitals that are polarized
using SS(V)PE. Researchers who use the isodensity SS(V)PE feature are asked to
cite Ref. [[245]](../bib_references/bib.md#bib245)
.

In related work, Pomogaeva and
Chipman[[1108]](../bib_references/bib.md#bib1155)

recently introduced a “composite method for implicit representation of
solvent” (CMIRS) that is based on SS(V)PE electrostatics but adds
nonelectrostatic terms. This model is available in **Q-Chem[[1527]](../bib_references/bib.md#bib1594)
** and
is discussed in Section [11.2.7](example_CMIRS-water.md). In its current
implementation, CMIRS requires an isodensity SS(V)PE calculation, However, the
current implementation computes the nonelectrostatic interactions using the
cavity and the solute’s charge density generated from the isodensity SS(V)PE.
To use the CMIRS model, an isodensity SS(V)PE calculation must be requested (as
described below), and the keywords **IDEFESR** and **IPnRF** must both be set to 1 in the *$svp* input section. The CMIRS model is further described in Section [11.2.6.2](#subsec:SVP).

An isodensity SS(V)PE calculation is requested by setting
SOLVENT_METHOD = ISOSVP in the *$rem* section, in addition
to normal job control variables for a single-point energy calculation. Whereas
the other solvation models described in this chapter use specialized input
sections (*e.g.*, *$pcm*) in lieu of a slew of *$rem* variables, the isodensity
SS(V)PE code is an interface between **Q-Chem** and a code written by
Chipman,[[242]](../bib_references/bib.md#bib247)
 so some *$rem* variables are used for
job control of isodensity SS(V)PE calculations. These are listed below.

SVP_MEMORY

### `SVP_MEMORY`

> **Specifies the amount of memory for use by the solvation module.**
>
> * **Type**: `INTEGER`
> * **Default**: `125`
> * **Options**:
>     * $n$
>     * corresponds to the amount of memory in MB.
> * **Recommendation**: The default should be fine for medium size molecules with the default Lebedev grid, only increase if needed.

SVP_PATH

### `SVP_PATH`

> **Specifies whether to run a gas phase computation prior to performing the solvation procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Run a gas-phase calculation and upon convergence run the SS(V)PE computation.
>     * 1
>     * Do not run a gas-phase calculation.
> * **Recommendation**: Running the gas-phase calculation provides a good guess to start the solvation stage and provides a more complete set of solvated properties.

SVP_CHARGE_CONV

### `SVP_CHARGE_CONV`

> **Determines the convergence value for the charges on the cavity. When the change in charges fall below this value, if the electron density is converged, then the calculation is considered converged.**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $n$
>     * Convergence threshold set to
>     * $10^{-n}$
>     * .
> * **Recommendation**: The default value unless convergence problems arise.

SVP_CAVITY_CONV

### `SVP_CAVITY_CONV`

> **Determines the convergence value of the iterative isodensity cavity procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$
>     * Convergence threshold set to
>     * $10^{-n}$
>     * .
> * **Recommendation**: The default value unless convergence problems arise.

SVP_GUESS

### `SVP_GUESS`

> **Specifies how and if the SS(V)PE model will use a given guess for the charges and cavity points.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * No guessing.
>     * 1
>     * Read a guess from a previous isodensity SS(V)PE calculation.
>     * 2
>     * Use a guess specified by the
>     * $svpirf
>     * section from the input.
> * **Recommendation**: It is helpful to also set SCF_GUESS to READ when using a guess from a previous Q-Chem run. Set IPnRF = 1 in the $svp section of the previous Q-Chem job, in order to save the reaction field for subsequent reading (see Section 11.2.6.2 ).

This last *$rem* variable requires specification of a *$svpirf* input section, the format for which is the following:

> ```qchem
> $svpirf
>    <# point> <x point>  <y point>  <z point>  <charge> <grid weight>
>    <# point> <x normal> <y normal> <z normal>
> $end
> ```

## 11.2.6.2 The *$svp* Input Section

More refined control over SS(V)PE jobs is obtained using a *$svp* input section.
These are read directly by Chipman’s SS(V)PE solvation module
and therefore must be specified in the context of a Fortran namelist.
The format is as follows:

> ```qchem
> $svp
>    <KEYWORD>=<VALUE>, <KEYWORD>=<VALUE>,...
>    <KEYWORD>=<VALUE>
> $end
> ```

For example, the section may look like this:

> ```qchem
> $svp
>    RHOISO=0.001, DIELST=78.39, NPTLEB=110
> $end
> ```

The following keywords are supported in the *$svp* section:

### `DielSt`

> **The static dielectric constant. INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `78.39`
> * **Options**:
>     * real number specifying the constant.
> * **Recommendation**: The default value 78.39 is appropriate for water solvent.

### `IDEFESR`

> **Specifies whether to request a CMIRS calculation. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not invoke a CMIRS calculation.
>     * 1
>     * Invoke a CMIRS calculation.
> * **Recommendation**: None. Need to set IPnRF = 1 in the $svp section if CMIRS is desired.

### `IPnRF`

> **Specifies whether to save the SS(V)PE reaction field. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not save the reaction field.
>     * 1
>     * Save the reaction field.
> * **Recommendation**: None. = 1 is required for CMIRS ( i.e. , if IDEFESR = 1).

### `IShape`

> **A flag to set the shape of the cavity surface. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * use the electronic isodensity surface.
>     * 1
>     * use a spherical cavity surface.
> * **Recommendation**: Use the default surface.

### `RhoIso`

> **Value of the electronic isodensity contour used to specify the cavity surface. (Only relevant for IShape = 0.) INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `0.001`
> * **Options**:
>     * Real number specifying the density in electrons/bohr
>     * ${}^{3}$
>     * .
> * **Recommendation**: The default value is optimal for most situations. Increasing the value produces a smaller cavity which ordinarily increases the magnitude of the solvation energy.

### `RadSph`

> **Sphere radius used to specify the cavity surface (Only relevant for IShape =1.) INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `Half the distance between the outermost atoms plus 1.4 Å.`
> * **Options**:
>     * Real number specifying the radius in Bohr (if positive) or in Å(if negative).
> * **Recommendation**: Make sure that the cavity radius is larger than the length of the molecule.

### `IntCav`

> **A flag to select the surface integration method. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Single center Lebedev integration.
>     * 1
>     * Single center spherical polar integration.
> * **Recommendation**: The Lebedev integration is by far the more efficient.

### `NPtLeb`

> **The number of points used in the Lebedev grid for the single-center surface integration. (Only relevant if IntCav = 0.) INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `1202`
> * **Options**:
>     * Valid choices are:
>     * 6, 18, 26, 38, 50, 86, 110, 146, 170, 194, 302, 350, 434, 590, 770,
>     * 974, 1202, 1454, 1730, 2030, 2354, 2702, 3074, 3470, 3890, 4334,
>     * 4802, or 5294.
> * **Recommendation**: The default value has been found adequate to obtain the energy to within 0.1 kcal/mol for solutes the size of mono-substituted benzenes.

### `NPtThe, NPtPhi`

> **The number of ( $\theta$ , $\phi$ ) points used for single-centered surface integration (relevant only if IntCav = 1.) INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `8,16`
> * **Options**:
>     * $\theta$
>     * ,
>     * $\phi$
>     * specifying the number of points.
> * **Recommendation**: These should be multiples of 2 and 4 respectively, to provide symmetry sufficient for all Abelian point groups. Defaults are too small for all but the tiniest and simplest solutes.

### `LinEq`

> **Flag to select the method for solving the linear equations that determine the apparent point charges on the cavity surface. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * use LU decomposition in memory if space permits, else switch to
>     * = 2
>     * 1
>     * use conjugate gradient iterations in memory if space permits, else use
>     * = 2
>     * 2
>     * use conjugate gradient iterations with the system matrix stored externally on disk.
> * **Recommendation**: The default should be sufficient in most cases.

### `CvgLin`

> **Convergence criterion for solving linear equations by the conjugate gradient iterative method (relevant if LinEq = 1 or 2.) INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `1.0E-7`
> * **Options**:
>     * Real number specifying the actual criterion.
> * **Recommendation**: The default value should be used unless convergence problems arise.

Note that the single-center surface integration approach that is used to find
the isodensity surface may fail for certain very non-spherical solute
molecules. The program will automatically check for this, aborting with a
warning message if necessary. The single-center approach succeeds only for what
is called a “star surface”, meaning that an observer sitting at the center
has an unobstructed view of the entire surface. Said another way, for a star
surface any ray emanating out from the center will pass through the surface
only once. Some cases of failure may be fixed by simply moving to a new center
with the **ITrnGr** parameter described below. But some surfaces are
inherently non-star surfaces and cannot be treated with this program until more
sophisticated surface integration approaches are developed and implemented.

### `ITrnGr`

> **Translation of the cavity surface integration grid. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 0
>     * No translation (
>     * i.e.
>     * , center of the cavity at the origin
>     * of the atomic coordinate system)
>     * 1
>     * Translate to the center of nuclear mass.
>     * 2
>     * Translate to the center of nuclear charge.
>     * 3
>     * Translate to the midpoint of the outermost atoms.
>     * 4
>     * Translate to midpoint of the outermost non-hydrogen atoms.
>     * 5
>     * Translate to user-specified coordinates in Bohr.
>     * 6
>     * Translate to user-specified coordinates in Ångstroms.
> * **Recommendation**: The default value is recommended unless the single-center integrations procedure fails. If cavity construction fails for a small, high-symmetry system, consider setting = 0.

### `TranX, TranY, TranZ`

> **$x$ , $y$ , and $z$ value of user-specified translation (only relevant if ITrnGr is set to 5 or 6). INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `0, 0, 0`
> * **Options**:
>     * $x$
>     * ,
>     * $y$
>     * , and
>     * $z$
>     * relative to the origin in the appropriate units.
> * **Recommendation**: None.

### `IRotGr`

> **Rotation of the cavity surface integration grid. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 0
>     * No rotation.
>     * 1
>     * Rotate initial
>     * $xyz$
>     * axes of the integration grid to coincide
>     * with principal moments of nuclear inertia (relevant if
>     * ITrnGr
>     * = 1)
>     * 2
>     * Rotate initial
>     * $xyz$
>     * axes of integration grid to coincide with
>     * principal moments of nuclear charge (relevant if
>     * ITrnGr
>     * = 2)
>     * 3
>     * Rotate initial
>     * $xyz$
>     * axes of the integration grid through user-specified
>     * Euler angles as defined by Wilson, Decius, and Cross.
> * **Recommendation**: The default is recommended unless the knowledgeable user has good reason otherwise. If cavity construction fails for a small, high-symmetry system, consider setting = 0.

### `RotThe  RotPhi  RotChi`

> **Euler angles ( $\theta$ , $\phi$ , $\chi$ ) in degrees for user-specified rotation of the cavity surface (relevant if IRotGr = 3). INPUT SECTION: $svp**
>
> * **Type**: `FLOAT`
> * **Default**: `0,0,0`
> * **Options**:
>     * $\theta$
>     * ,
>     * $\phi$
>     * ,
>     * $\chi$
>     * in degrees
> * **Recommendation**: None.

### `IOpPrd`

> **Specifies the choice of system operator-product form. INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Symmetric form.
>     * 1
>     * Non-symmetric form.
> * **Recommendation**: The default uses more memory but is generally more efficient, we recommend its use unless there is shortage of memory available.

By default, **Q-Chem** will check the validity of the single-center expansion by
searching for the isodensity surface in two different ways: first, working
inwards from a large distance, and next by working outwards from the origin.
If the same result is obtained (within tolerances) using both procedures, then
the cavity is accepted. If the two results do not agree, then the program
exits with an error message indicating that the inner isodensity surface is
found to be too far from the outer isodensity surface.

**Note: 

For some small molecules (such as atoms and diatomics), construction of the isodensity
cavity may fail with the default parameters. In such cases, we recommend setting ITrnGr = 0
and also IRotGr = 0, with the molecule centered at the origin of the grid (*i.e.*, in the standard
nuclear orientation).
**

Some molecules, for example C${}_{60}$, can have a hole in the middle. Such
molecules have two different “legal” isodensity surfaces, a small inner one
inside the “hole”, and a large outer one that is the desired surface for
solvation. In such cases, the cavity check described in the preceding
paragraph causes the program to exit. To avoid this, one can consider turning
off the cavity check that works out from the origin, leaving only the outer
cavity determined by working in from large distances.

### `ICvICk`

> **Specifies whether to perform cavity check INPUT SECTION: $svp**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * no cavity check, use only the outer cavity
>     * 1
>     * cavity check, generating both the inner and outer cavities and compare.
> * **Recommendation**: Consider turning off cavity check only if the molecule has a hole and if a star (outer) surface is expected.
