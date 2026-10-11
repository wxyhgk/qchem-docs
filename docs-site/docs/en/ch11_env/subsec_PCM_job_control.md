---
title: "11.2.4 PCM Job Control"
---

## 11.2.4 PCM Job Control

(July 4, 2026)

A PCM calculation is requested by setting SOLVENT_METHOD =
PCM in the *$rem* section. As mentioned above, there are a variety
of different theoretical models that fall within the PCM family, so additional
fine-tuning may be required, as described below.

## 11.2.4.1 *$pcm* section

Most PCM job control is accomplished via options specified in the *$pcm* input
section, which allows the user to specify which flavor of PCM will be used,
which algorithm will be used to solve the PCM equations, and other options.
The format of the *$pcm* section is analogous to that of the *$rem* section:

> ```qchem
> $pcm
>    <Keyword>  <parameter/option>
> $end
> ```

**Note: 

The following job control variables belong *only* in the *$pcm* section.
Do not place them in the *$rem* section.
**

### `Theory`

> **Specifies the which polarizable continuum model will be used. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `CPCM`
> * **Options**:
>     * CPCM
>     * Conductor-like PCM of Ref.
>     * 275
>     * Cossi M. et al.
>     * J. Comput. Chem.
>     * (2003)
>     * ,
>     * 24
>     * ,
>     * pp. 669
>     * .
>     * Link
>     * ,
>     * with
>     * $f_{\varepsilon}=(\varepsilon-1)/\varepsilon$
>     * .
>     * CPCM1
>     * Equivalent to CPCM.
>     * CPCM2
>     * Original conductor-like screening model of Ref.
>     * , with
>     * $f_{\varepsilon}=(\varepsilon-1)/(\varepsilon+1/2)$
>     * .
>     * IEFPCM
>     * IEF-PCM with an asymmetric
>     * $\mathbf{K}$
>     * matrix.
>     * SSVPE
>     * SS(V)PE model, equivalent to IEF-PCM with a symmetric
>     * $\mathbf{K}$
>     * matrix.
> * **Recommendation**: The IEF-PCM/SS(V)PE model is more sophisticated model than C-PCM, and formally more appropriate for low-dielectric solvents, but it is also more complicated to work with. In practice there is often little difference between these models; see Ref. 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link . Regarding the two versions of C-PCM and the choice of $f_{\varepsilon}$ in Eq. ( 11.3 ), the choice $x=0$ has been suggested for neutral solutes and $x=1/2$ for ions; again, see Ref. 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link for a discussion of these distinctions.

### `Method`

> **Specifies which surface discretization method will be used. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `SwiG`
> * **Options**:
>     * SwiG
>     * Switching/Gaussian method
>     * ISwiG
>     * “Improved” Switching/Gaussian method with an alternative switching function
>     * Spherical
>     * Use a single, fixed sphere for the cavity surface.
>     * Fixed
>     * Use discretization point charges instead of smooth Gaussians.
> * **Recommendation**: Use of SwiG is recommended only because it is slightly more efficient than the switching function of ISwiG . On the other hand, ISwiG offers some conceptually more appealing features and may be superior in certain cases. Consult Refs. 754 Lange A. W., Herbert J. M. J. Chem. Phys. (2010) , 133 , pp. 244111 . Link , 756 Lange A. W., Herbert J. M. Chem. Phys. Lett. (2011) , 509 , pp. 77 . Link for a discussion of these differences. The Fixed option uses the Variable Tesserae Number (VTN) algorithm of Li and Jensen, 812 Li H., Jensen J. H. J. Comput. Chem. (2004) , 25 , pp. 1449 . Link with Lebedev grid points. VTN uses point charges with no switching function or Gaussian blurring, and is therefore subject to discontinuities that may cause errors in analytic gradients and lead to slow convergence in geometry optimizations. 753 Lange A. W., Herbert J. M. J. Phys. Chem. Lett. (2010) , 1 , pp. 556 . Link Its use is not recommended except to make contact with other calculations in the literature.

### `Solver`

> **Specifies the algorithm used to solve the PCM equations. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `INVERSION`
> * **Options**:
>     * INVERSION
>     * Direct matrix inversion
>     * CG
>     * Iterative conjugate gradient
> * **Recommendation**: Matrix inversion is faster for small solutes because it needs to be performed only once in a single-point calculation. However, the CG solver (which must be applied at each SCF iteration) is recommended if the number of discretization points approaches or exceeds $\sim$ 10,000. Linear-scaling options for large-scale MM/PCM and QM/MM/PCM calculations are discussed in Section 11.2.5 .

### `SwitchThresh`

> **Threshold for discarding grid points on the cavity surface. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$
>     * Discard grid points when the switching function is less than
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default, which is found to avoid discontinuities within machine precision. Increasing $n$ reduces the cost of PCM calculations but can introduce discontinuities in the potential energy surface. If the PCM part of the calculation becomes too expensive it is better to reduce the number of discretization points ( HeavyPoints and HPoints , described below), or to use Solver = CG , than it is to adjust .

Construction of the solute cavity is an important part of the model and users
should consult the literature in this capacity, especially with regard to the
radii used for the atomic spheres. The default values provided in **Q-Chem**
correspond to the consensus choice that has emerged over several decades,
namely, to use vdW radii $\{R_{\text{vdW},A}\}$ scaled by a factor $\alpha_{\text{vdW}}=1.2$;
see Eq. ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii)). The most widely-used set
of vdW radii are those determined from crystallographic data by
Bondi,[[146]](../bib_references/bib.md#bib136)
 although the radius for hydrogen was later adjusted to
1.1 Å,[[1186]](../bib_references/bib.md#bib1240)
 and radii for those main-group elements not
addressed by Bondi were provided later.[[889]](../bib_references/bib.md#bib923)
 This extended set
of vdW is used by default in **Q-Chem**, and for simplicity we call these “Bondi
radii” regardless of whether they come from Bondi’s original paper or the
later work. Alternatively, atomic radii from the Universal Force Field (UFF)
are available.[[1146]](../bib_references/bib.md#bib1198)
 The main appeal of UFF radii is that they are
defined for all atoms of the periodic table, though the quality of these radii
for PCM applications is unclear.

### `Radii`

> **Specifies which set of atomic van der Waals radii will be used to define the solute cavity. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `Bondi`
> * **Options**:
>     * Bondi
>     * Use the (extended) set of Bondi radii (Ref.
>     * 1186
>     * Rowland R. S., Taylor R.
>     * J. Phys. Chem.
>     * (1996)
>     * ,
>     * 100
>     * ,
>     * pp. 7384
>     * .
>     * Link
>     * ).
>     * FF
>     * Use Lennard-Jones radii from a molecular mechanics force field.
>     * UFF
>     * Use radii from the Universal Force Field (Ref.
>     * 1146
>     * Rappé A. K. et al.
>     * J. Am. Chem. Soc.
>     * (1992)
>     * ,
>     * 114
>     * ,
>     * pp. 10024
>     * .
>     * Link
>     * ).
>     * Read
>     * Read the atomic radii from a
>     * $van_der_waals
>     * input section.
> * **Recommendation**: Bondi radii are widely used. The FF option requires the user to specify an MM force field using the FORCE_FIELD variable in the $rem section, and also to define the atom types in the $molecule section (see Section 11.3 ). This is not required for UFF radii. For user-defined radii, see Section 11.2.10 for the format of the $van_der_waals input section.

### `vdwScale`

> **Scaling factor for the atomic van der Waals radii used to define the solute cavity. INPUT SECTION: $pcm**
>
> * **Type**: `FLOAT`
> * **Default**: `1.2`
> * **Options**:
>     * $\alpha$
>     * Use a scaling factor of
>     * $\alpha>0$
>     * .
> * **Recommendation**: The default value is widely used in PCM calculations, although a value of 1.0 might be appropriate if using a solvent-accessible surface.

### `SASradius`

> **Form a “solvent accessible” surface with the given solvent probe radius. INPUT SECTION: $pcm**
>
> * **Type**: `FLOAT`
> * **Default**: `0.0`
> * **Options**:
>     * $r$
>     * Use a solvent probe radius of
>     * $r$
>     * , in Å.
> * **Recommendation**: The solvent probe radius is added to the scaled van der Waals radii of the solute atoms. A common solvent probe radius for water is 1.4 Å, but smaller values (0.2–0.5 Å) have also been used historically. 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link

### `SurfaceType`

> **Selects the solute cavity surface construction. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `VDW_SAS`
> * **Options**:
>     * VDW_SAS
>     * van der Waals or solvent-accessible surface
>     * SES
>     * solvent-excluded surface
> * **Recommendation**: The vdW surface and the SAS are each comprised simply of atomic spheres and thus share a common option; the only difference is the specification of a solvent probe radius, SASradius . For a true vdW surface, the probe radius should be zero (which is the default), whereas for the SAS the atomic radii are traditionally not scaled, hence vdwScale should be set to 1.0 (which is not the default). For the SES, only SwiG discretization is available, but this can be used with any set of (scaled or unscaled) atomic radii, or with radii that are augmented by SASradius .

Note from the description of the **Radii** keyword
that the user may specify his or her own radii for cavity construction, using a *$van_der_waals* input section.
To specify all of the radii for a given molecule, use the format of the *$van_der_waals* section that is described in Section [11.2.10](subsec_LD.md).
Alternatively, if one simply needs to specify a radius that is missing from a given set of radii (such as Bondi’s set, which is not
defined for the entire periodic table), this can be accomplished without setting **Radii** = **Read**. Instead, leave
**Radii** = **Bondi** (or some other choice) but include a *$van_der_waals* section having the format

> ```qchem
> $van_der_waals
> atomic_number   vdW_radius
> $end
> ```

No scaling factor is applied to
user-defined radii. Note that $R=0$ is allowed for a particular atomic radius,
in which case the atom in question is not used to construct the cavity surface.
This feature facilitates the construction of “united atom”
cavities,[[78]](../bib_references/bib.md#bib60)
 in which the hydrogen atoms do not get their own
spheres and the heavy-atom radii are increased to compensate.
As an alternative to scaling the vdW radii $\{R_{\text{vdW},A}\}$, the user can choose to augment
each of them with a probe radius $R_{\text{probe}}$ [see Eq. ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii))] to obtain the SAS cavity.

Historically, discretization of the cavity surface has involved
“tessellation” methods that divide the cavity surface area into finite
polygonal “tesserae”. (The GEPOL algorithm[[1044]](../bib_references/bib.md#bib1089)
 is
perhaps the most widely-used tessellation scheme.) Tessellation methods,
however, suffer not only from discontinuities in the cavity surface area and
solvation energy as a function of the nuclear coordinates, but in addition they
lead to analytic energy gradients that are complicated to derive and implement.
To avoid these problems, **Q-Chem**’s SwiG-PCM
implementation[[753]](../bib_references/bib.md#bib786)
 uses Lebedev grids to
discretize the atomic spheres. These are atom-centered grids with icosahedral
symmetry, and may consist of anywhere from 26 to 5294 grid points per atomic
sphere. The default values used by **Q-Chem** were selected based on extensive
numerical tests,[[754]](../bib_references/bib.md#bib787)
 and they are looser for MM atoms
(in MM/PCM or QM/MM/PCM jobs) than they are for QM atoms,
reflecting the more complicated electrostatic potential that is generated by a
QM density as compared to an MM point charge. For QM atoms, the default is to
use $N=110$ points for hydrogen atoms and $N=194$ points for all other atoms,
whereas for MM atoms the default is $N=50$ for hydrogen and $N=110$ for
non-hydrogen. These default values exhibit good rotational invariance
($<0.1$ kcal/mol differences in $\Delta G$ when the molecule is
rotated[[754]](../bib_references/bib.md#bib787)
) and absolute solvation energies that typically lie
within $<1$ kcal/mol of the $N\rightarrow\infty$
limit,[[754]](../bib_references/bib.md#bib787)
 at least for charge-neutral solutes.

Note that earlier versions of **Q-Chem** used denser grids by default. (In
versions up to and including **Q-Chem** v. 4.2, the default was $N=590$ for all
QM atoms, but was switched to $N=302$ beginning with v. 4.2.1. The defaults
mentioned above are the current ones starting with v. 5.2.) However, grid
errors of $\sim$0.5 kcal/mol are well within the intrinsic accuracy of $\Delta G_{\textrm{solvation}}$ for these models. Grid errors in solvatochromatic
shifts for excitation energies tend to be $\sim$0.01–0.02 eV, which is well
within the intrinsic accuracy of nearly any excited-state methodology. If
questions about grid accuracy arise, we suggest using $N=302$ as a high-quality
option and $N=590$ as an essentially converged option.[[754]](../bib_references/bib.md#bib787)

For large molecules it may be necessary to reduce the number of grid points
(*e.g.*, to $N=86$) or to use linear-scaling solvers rather than matrix inversion, as
discussed in Section [11.2.5](subsec_linear-PCM.md).

**Note: 

The acceptable values for the number of Lebedev points per sphere are
$N=6$, 26, 38, 50, 86, 110, 146, 170, 194, 302, 350, 434, 590, 770, 974, 1202,
1454, 1730, 2030, 2354, 2702, 3074, 3470, 3890, 4334, 4802, 5294.
**

### `HeavyPoints`

> **The number of Lebedev grid points to be placed non-hydrogen atoms in the QM system. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `194`
> * **Options**:
>     * Acceptable values are listed above.
> * **Recommendation**: Use the default for geometry optimizations. For absolute solvation energies, the user may want to examine convergence with respect to $N$ .

### `HPoints`

> **The number of Lebedev grid points to be placed on H atoms in the QM system. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `110`
> * **Options**:
>     * Acceptable values are listed above.
> * **Recommendation**: Use the default for geometry optimizations. For absolute solvation energies, the user may want to examine convergence with respect to $N$ .

### `MMHeavyPoints`

> **The number of Lebedev grid points to be placed on non-hydrogen atoms in the MM subsystem. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `110`
> * **Options**:
>     * Acceptable values are listed above.
> * **Recommendation**: Use the default for geometry optimizations. For absolute solvation energies, the user may want to examine convergence with respect to $N$ . This option applies only to MM/PCM or QM/MM/PCM calculations.

### `MMHPoints`

> **The number of Lebedev grid points to be placed on H atoms in the MM subsystem. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * Acceptable values are listed above.
> * **Recommendation**: Use the default for geometry optimizations. For absolute solvation energies, the user may want to examine convergence with respect to $N$ . This option applies only to MM/PCM or QM/MM/PCM calculations.

Especially for complicated molecules, the user may want to visualize the cavity
surface. This can be accomplished by setting **PrintLevel** $\geq 2$,
which will trigger the generation of several `.PQR` files that describe
the cavity surface. (These are written to the **Q-Chem** output file.) The
`.PQR` format is similar to the common `.PDB` (Protein Data Bank)
format, but also contains charge and radius information for each atom. One of
the output `.PQR` files contains the charges computed in the PCM
calculation and radii (in Å) that are half of the square root of the surface
area represented by each surface grid point. Thus, in examining this
representation of the surface, larger discretization points are associated with
larger surface areas. A second `.PQR` file contains the solute’s
electrostatic potential (in atomic units), in place of the charge information,
and uses uniform radii for the grid points. These `.PQR` files can be
visualized using various third-party software, including the freely-available
Visual Molecular Dynamics (VMD) program,[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627) which is
particularly useful for coloring the `.PQR` surface grid points according
to their charge, and sizing them according to their contribution to the
molecular surface area. (Examples of such visualizations can be found in
Ref. [[753]](../bib_references/bib.md#bib786)
.)

### `PrintLevel`

> **Controls the printing level during PCM calculations. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Prints PCM energy and basic surface grid information. Minimal additional printing.
>     * 1
>     * Level 0 plus PCM solute-solvent interaction energy components and Gauss’ Law error.
>     * 2
>     * Level 1 plus surface grid switching parameters and a
>     * .PQR
>     * file for
>     * visualization of the cavity surface apparent surface charges.
>     * 3
>     * Level 2 plus a
>     * .PQR
>     * file for visualization of the electrostatic
>     * potential at the surface grid created by the converged solute.
>     * 4
>     * Level 3 plus additional surface grid information, electrostatic potential
>     * and apparent surface charges on each SCF cycle.
>     * 5
>     * Level 4 plus extensive debugging information.
> * **Recommendation**: Use the default unless further information is desired.

Finally, note that setting **Method** to **Spherical** in the *$pcm*
input selection requests the construction of a solute cavity consisting of a
single, fixed sphere. This is generally not recommended but is occasionally
useful for making contact with the results of Born models in the literature, or
the Kirkwood-Onsager model discussed in Section [11.2.2](example_SCRF.md). In this
case, the cavity radius and its center must also be specified in the *$pcm*
section. The keyword **HeavyPoints** controls the number of Lebedev grid
points used to discretize the surface.

### `CavityRadius`

> **Specifies the solute cavity radius. INPUT SECTION: $pcm**
>
> * **Type**: `FLOAT`
> * **Default**: `None`
> * **Options**:
>     * $R$
>     * Use a radius of
>     * $R$
>     * , in Ångstroms.
> * **Recommendation**: None.

### `CavityCenter`

> **Specifies the center of the spherical solute cavity. INPUT SECTION: $pcm**
>
> * **Type**: `FLOAT`
> * **Default**: `0.0 0.0 0.0`
> * **Options**:
>     * $x$
>     * $y$
>     * $z$
>     * Coordinates of the cavity center, in Ångstroms.
> * **Recommendation**: The format is followed by three floating-point values, delineated by spaces. Uses the same coordinate system as the $molecule section.

Finally, the HetPCM method (Section [11.2.3.5](topic_pcm-em.md#sec:HetPCM)) is activated by the appearance of a keyword
**Het-PCM** in the *$pcm* section. Such calculations require an *$atomic_epsilon* input section that specifies
the value of $\varepsilon$ that is to be used for each atomic sphere. The format is simply a list of atom numbers
with a double-precision value of $\varepsilon$ for each:

> ```qchem
> $atomic_epsilon
> 1   epsilon_1
> 2   epsilon_2
> 3   epsilon_3
> ...
> $end
> ```

Atoms can be omitted from this list and will be assigned $\varepsilon=1$.

### `Het-PCM`

> **If present, activates the heterogeneous PCM. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * If the keyword is present, HetPCM is turned on
> * **Recommendation**: Requires an $atomic_epsilon section to provide a user-specified dielectric constant for each atom. Set PCM_PRINT $\geq 1$ in $rem to confirm that the atomic values of $\varepsilon$ are being used.

## 11.2.4.2 Examples

???+ example "Example 11.3: A basic example of using the PCMs: optimization of trifluoroethanol in water.
The solvent dielectric is specified in the $solvent section, which is described below."
    ```qchem
    $comment
    2023/4/5 Add geom_opt_driver optimize per #2954, [39888/qchem]
    $end
    
    $molecule
       0 1
       C    -0.245826    -0.351674    -0.019873
       C     0.244003     0.376569     1.241371
       O     0.862012    -0.527016     2.143243
       F     0.776783    -0.909300    -0.666009
       F    -0.858739     0.511576    -0.827287
       F    -1.108290    -1.303001     0.339419
       H    -0.587975     0.878499     1.736246
       H     0.963047     1.147195     0.961639
       H     0.191283    -1.098089     2.489052
    $end
    
    $rem
       JOBTYPE         OPT
       BASIS           6-31G*
       METHOD          B3LYP
       SOLVENT_METHOD  PCM
       geom_opt_driver optimize
    $end
    
    $pcm
       Theory          CPCM
       Method          SWIG
       Solver          Inversion
       HeavyPoints     194
       HPoints         194
       Radii           Bondi
       vdwScale        1.2
    $end
    
    $solvent
       Dielectric 78.39
    $end
    ```

???+ example "Example 11.4: PCM with a single spherical cavity, applied to H ${}_{2}$ O in acetonitrile.
Compared to the Kirkwood-Onsager multipole expansion method,
Example 11.2.2 on page 11.2.2 ."
    ```qchem
    $molecule
       0 1
       O       0.00000000     0.00000000     0.11722303
       H      -0.75908339     0.00000000    -0.46889211
       H       0.75908339     0.00000000    -0.46889211
    $end
    
    $rem
       METHOD            HF
       BASIS             6-31g**
       SOLVENT_METHOD    pcm
    $end
    
    $pcm
       method        spherical   ! single spherical cavity with 590 discretization points
       HeavyPoints   590
       CavityRadius  1.8         ! Solute Radius, in Angstrom
       CavityCenter  0.0 0.0 0.0 ! Will be at center of Standard Nuclear Orientation
       Theory        SSVPE
    $end
    
    $solvent
       Dielectric        35.9   !   Acetonitrile
    $end
    ```

Finally, we consider an example of a united-atom cavity. Note that a
user-defined vdW radius is supplied only for carbon, so the hydrogen
radius is taken to be zero and thus the hydrogen atoms are not used to
construct the cavity surface. (As mentioned above, the format for the *$van_der_waals*
input section is discussion in Section [11.2.10](subsec_LD.md)).

???+ example "Example 11.5: United-atom cavity construction for ethylene."
    ```qchem
    $comment
       Benzene (in benzene), with a united-atom cavity construction
       R = 2.28 A for carbon, R = 0 for hydrogen
    $end
    
    $molecule
       0 1
       C    1.38620    0.000000   0.000000
       C    0.69310    1.200484   0.000000
       C   -0.69310    1.200484   0.000000
       C   -1.38620    0.000000   0.000000
       C   -0.69310   -1.200484   0.000000
       C    0.69310   -1.200484   0.000000
       H    2.46180    0.000000   0.000000
       H    1.23090    2.131981   0.000000
       H   -1.23090    2.131981   0.000000
       H   -2.46180    0.000000   0.000000
       H   -1.23090   -2.131981   0.000000
       H    1.23090   -2.131981   0.000000
    $end
    
    $rem
       EXCHANGE        hf
       BASIS           6-31G*
       SOLVENT_METHOD  pcm
    $end
    
    $pcm
       theory          iefpcm   ! this is a synonym for ssvpe
       method          swig
       printlevel      1
       radii           read
    $end
    
    $solvent
       dielectric 2.27
    $end
    
    $van_der_waals
    1
      6     2.28
      1     0.00
    $end
    ```

???+ example "Example 11.6: Heterogeneous (HetPCM) example, triggered by the Het-PCM flag in the $pcm section.
This is a truncated model of protonated histidine, with the cationic aromatic moiety exposed to and environment
where $\varepsilon=78.4$ , whereas $\varepsilon=10.0$ for atoms in the side chain."
    ```qchem
    
    $molecule
    1 1
      H   -4.9076613   -1.9352798   -1.3335875
      C   -2.3500449   -0.5754970    0.0756697
      N   -3.3660526    0.0772627    0.6735620
      H   -3.3085727    0.8201166    1.4041665
      C   -4.4907166   -0.4318030    0.1363201
      H   -5.4902154   -0.1170220    0.4064538
      N   -4.2187491   -1.3840482   -0.7759280
      C   -2.8779889   -1.4836771   -0.8202360
      H   -2.3293638   -2.1655889   -1.4569339
      C   -0.4271237    1.0622789   -0.0051732
      C   -0.8883153   -0.3558429    0.3532960
      H   -0.6778182   -0.5663962    1.4234430
      H   -0.2980823   -1.0704793   -0.2605079
      N   -1.0842830    2.0665662    0.8255888
      H   -0.6455886    1.2632695   -1.0772303
      H   -0.7421259    3.0116763    0.5376181
      H   -0.8094259    1.9175321    1.8239106
      H    0.6740052    1.1315080    0.1435944
    $end
    
    $rem
    method            hf
    basis             sto-3g
    solvent_method    pcm
    pcm_print         1
    $end
    
    $pcm
    het-pcm
    theory     cpcm
    $end
    
    $atomic_epsilon
    1  78.4
    2  78.4
    3  78.4
    4  78.4
    5  78.4
    6  78.4
    7  78.4
    8  78.4
    9  78.4
    10 10.0
    11 10.0
    12 10.0
    13 10.0
    14 10.0
    15 10.0
    16 10.0
    17 10.0
    18 10.0
    $end
    ```

## 11.2.4.3 *$solvent* Section: Electrostatics Options

The solvent for PCM calculations is specified using the *$solvent* section, as documented in
this section and the next one. Note that the *$solvent* section is also used to specify
parameters for the Kirkwood-Onsager SCRF model (Section [11.2.2](example_SCRF.md)),
and the particular options that can be listed in the *$solvent* section
depend upon the value of SOLVENT_METHOD in the *$rem* section.
A minimum requirement for a PCM calculation is that the *$solvent* section must specify
the static dielectric constant ($\varepsilon$), and for nonequilibrium excited-state calculations the optical
dielectric constant ($\varepsilon_{\text{opt}}\equiv\varepsilon_{\infty}$) must be specified as well.
There are default values that are appropriate for water, but for any other solvent these constants must be
specified. These can either be specified individually, using the variables **Dielectric** and
**OpticalDielectric** in the *$solvent* section, or they can be set to predefined values by setting
**SolventName** equal to one of the named solvents that is given in Table [11.4](#table:PCM-solvents).

Unlike the SM$x$ models (Section [11.2.9](ex_SMx-User-Solvent.md)), which also employ named solvents (specified in the
*$smx* section), use of **SolventName** with a PCM serves only to specify
the two dielectric constants. Nonelectrostatic interactions are not included in an automatic way, although
they can be added in an *ad hoc* way as described in Section [11.2.4.4](#subsubsec:PCM-solvent-NonElst).
The dielectric constants listed in Table [11.4](#table:PCM-solvents) correspond to values at 20${}^{\circ}$C.
For water, this is slightly different than the default values of **Dielectric**
and **OpticalDielectric**, which correspond to 25${}^{\circ}$C. The latter two values are fully tunable,
whereas the named solvents are limited to the pairs of values ($\varepsilon$, $\varepsilon_{\infty}$)
listed in Table [11.4](#table:PCM-solvents).

### `Dielectric`

> **Specifies the static dielectric constant for the PCM solvent. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `78.39`
> * **Options**:
>     * $\varepsilon$
>     * Use a dielectric constant
>     * $\varepsilon>0$
>     * .
> * **Recommendation**: The static ( i.e. , zero-frequency) dielectric constant is what is usually called “the” dielectric constant. The default corresponds to water at 25 ${}^{\circ}$ C.

### `OpticalDielectric`

> **Specifies the optical dielectric constant for the PCM solvent. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `1.78`
> * **Options**:
>     * $\varepsilon_{\infty}$
>     * Use an optical dielectric constant
>     * $\varepsilon_{\infty}>0$
>     * .
> * **Recommendation**: The default corresponds to water at 25 ${}^{\circ}$ C. Note that $\varepsilon_{\infty}=n^{2}$ , where $n$ is the solvent’s index of refraction.

### `SolventName`

> **Specify both $\varepsilon$ and $\varepsilon_{\infty}$ for PCM calculations by naming the solvent. INPUT SECTION: $solvent**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * name
>     * Use values
>     * $\varepsilon$
>     * and
>     * $\varepsilon_{\infty}$
>     * corresponding to solvent
>     * name
>     * in
>     * Table
>     * 11.4
>     * .
> * **Recommendation**: The use of is incompatible with explicit specification of either Dielectric or OpticalDielectric .

| SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| acetic_acid | 6.2 | 1.88 | dimethoxyethane | 7.3 | 1.90 | iodobenzene | 4.7 | 2.63 |
| acetone | 21.1 | 1.85 | 1-2-dimethoxyethane |  |  | isobutanol | 18.1 | 1.95 |
| acetonitrile | 36.6 | 1.81 | glyme |  |  | 2-methyl-1-propanol |  |  |
| acetylacetone | 26.5 | 2.11 | dimethylacetamide | 40.2 | 2.07 | isopropanol | 20.2 | 1.90 |
| pentane-2-4-dione |  |  | dimethylaminobenzene | 5.0 | 2.43 | 2-propanol |  |  |
| 2-4-pentanedione |  |  | n-n-dimethylaniline |  |  | mesitylene | 2.3 | 2.25 |
| aniline | 7.1 | 2.52 | dimethylformamide | 38.2 | 2.05 | 1-3-5-trimethylbenzene |  |  |
| benzenamine |  |  | N-N-dimethylformamide |  |  | methanol | 33.0 | 1.77 |
| anisole | 4.4 | 2.30 | dimethylsulfoxide | 47.2 | 2.18 | methyl_acetate | 6.8 | 1.85 |
| methoxybenzene |  |  | DMSO |  |  | acetic_acid_methyl_ester |  |  |
| benzaldehyde | 17.8 | 2.39 | dioxane | 2.2 | 2.02 | methyl_ethanoate |  |  |
| benzene | 2.3 | 2.25 | 1-4-dioxane |  |  | nitrobenzene | 35.6 | 2.41 |
| benzonitrile | 25.6 | 2.34 | ethanol | 25.3 | 1.85 | nonane | 2.0 | 1.98 |
| benzyl_alcohol | 13.7 | 2.38 | ethanolamine | 31.9 | 2.12 | n-nonane |  |  |
| phenyl_methanol |  |  | ethyl_acetate | 6.1 | 1.88 | octanol | 10.1 | 2.05 |
| bromobenzene | 5.5 | 2.43 | ethyl_ethanoate |  |  | 1-octanol |  |  |
| butanol | 18.1 | 1.96 | acetic_acid_ethyl_ester |  |  | p-xylene | 2.3 | 2.24 |
| 1-butanol |  |  | ethyl_acetoacetate | 14.0 | 2.02 | para-xylene |  |  |
| butanol | 17.1 | 1.95 | ethyl-3-oxobutanoate |  |  | 1-4-dimethylbenzene |  |  |
| 2-butanol |  |  | acetoacetic_acid_ethyl_ester |  |  | pentane | 1.8 | 1.84 |
| butanone | 18.6 | 1.90 | ethyl_benzoate | 6.2 | 2.27 | n-pentane |  |  |
| 2-butanone |  |  | benzoic_acid_ethyl_ester |  |  | 1-pentanol | 15.1 | 1.99 |
| butan-2-one |  |  | decane | 2.0 | 1.99 | 2-pentanol | 13.4 | 1.98 |
| methyl_ethyl_ketone |  |  | n-decane |  |  | 3-pentanol | 14.0 | 2.00 |
| carbon_tetrachloride | 2.2 | 2.13 | ethyl_formate | 8.7 | 1.85 | 2-pentanone | 15.4 | 1.94 |
| tetrachloromethane |  |  | ethyl_methanoate |  |  | pentan-2-one |  |  |
| chlorobenzene | 5.7 | 2.33 | formic_acid_methyl_ester |  |  | methyl_propyl_ketone |  |  |
| chloroform | 4.8 | 2.08 | ethylene_glycol | 42.8 | 2.05 | phenol | 13.4 | 2.37 |
| trichloromethane |  |  | 1-2-ethanediol |  |  | 1-propanol | 20.8 | 1.92 |
| cyclohexane | 2.0 | 2.03 | fluorobenzene | 5.5 | 2.23 | propanal | 17.4 | 1.86 |
| cyclohexanol | 16.4 | 2.15 | formamide | 111.8 | 2.10 | propionaldehyde |  |  |
| cyclohexanone | 16.1 | 2.11 | formic_acid | 51.1 | 1.88 | pyridine | 13.3 | 2.28 |
| 1-1-dichloroethane | 10.1 | 2.01 | heptane | 1.9 | 1.93 | t-butanol | 12.0 | 1.92 |
| 1-2-dichloroethane | 10.4 | 2.09 | n-heptane |  |  | tert-butanol |  |  |
| dichloromethane | 8.9 | 2.02 | heptanol | 11.9 | 2.03 | 2-methyl-2-propanol |  |  |
| methylene_chloride |  |  | 1-heptanol |  |  | tetrahydrofuran | 7.5 | 1.97 |
| diethylamine | 3.7 | 1.92 | hexane | 1.9 | 1.89 | THF |  |  |
| diethyl_ether | 4.3 | 1.83 | n-hexane |  |  | toluene | 2.4 | 2.24 |
| diethyl_ketone | 17.0 | 1.95 | hexanol | 13.6 | 2.01 | triethylamine | 2.4 | 1.96 |
| 3-pentanone |  |  | 1-hexanol |  |  | n-n-diethylethanamine |  |  |
| pentan-3-one |  |  |  |  |  | water | 80.2 | 1.78 |

Table 11.4: 
Named solvents available for PCM calculations. (Indented names are synonyms.)
Values for $\varepsilon$ correspond
to the most recent measurements at 20${}^{\circ}$C (from Ref. 

)
and values of $\varepsilon_{\infty}=n^{2}$ correspond to the most recent measurement at 20${}^{\circ}$C and
$\lambda=589$ nm (from Ref. 

).
Setting **SolventName** to one of these values specifies the two dielectric constants but does
not stipulate any nonelectrostatic interactions.

## 11.2.4.4 *$solvent* Section: Nonelectrostatic Options

A PCM describes only electrostatic interactions with the solute, based on the static
dielectric constant (for the initial state) and possibly the optical dielectric constant in the
case of a nonequilibrium excitation or ionization process. Nonelectrostatic interaction
terms,[[569]](../bib_references/bib.md#bib580)
 describing cavitation (Pauli repulsion) and dispersion interactions, for example,
can be added in an *ad hoc* way but have not been specifically parameterized for PCMs.
(For solvation models with automatic incorporation of nonelectrostatic terms, which are needed to obtain
absolute solvation energies, see the SM$x$ models in Section [11.2.9](ex_SMx-User-Solvent.md) or the CMIRS approach in
Section [11.2.7](example_CMIRS-water.md).

To add nonelectrostatic interactions to a PCM calculation, use the *$solvent* section whose general form
is shown below.

> ```qchem
> $solvent
>    NonEls  <Option>
>    NSolventAtoms <Number unique of solvent atoms>
>    SolventAtom <Number1> <Number2> <Number3> <SASradius>
>    SolventAtom <Number1> <Number2> <Number3> <SASradius>
>    . . .
>    <Keyword>  <parameter/option>
>    . . .
> $end
> ```

The keyword **SolventAtom** requires multiple parameters, whereas all other
keywords require only a single parameter, including the **Dielectric**, **OpticalDielectric**,
and **SolventName** options that were discussed above.
The keyword **SolventAtom** requires multiple parameters, whereas all other
keywords require only a single parameter. Whereas the dielectric constant is required for any PCM
calculation (with a default value representing water), the nonelectrostatic parameters are optional
and have only infrequently been added to these models.[[282]](../bib_references/bib.md#bib287)

The nonelectrostatic interactions currently available in **Q-Chem** are based on
the work of Cossi *et al.*,[[274]](../bib_references/bib.md#bib272)
 and are computed outside of the
SCF procedure used to determine the electrostatic interactions. The
nonelectrostatic energy is highly dependent on the input parameters and can be
extremely sensitive to the radii chosen to define the solute cavity.
Accordingly, the inclusion of nonelectrostatic interactions is highly
empirical and probably needs to be considered on a case-by-case basis.
Following Ref. [[274]](../bib_references/bib.md#bib272)
, the cavitation energy is computed using
the same solute cavity that is used to compute the electrostatic energy,
whereas the dispersion/repulsion energy is computed using a SAS cavity definition.

The following keywords (in the *$solvent* section) are used to define
nonelectrostatic parameters for PCM calculations.

### `NonEls`

> **Specifies what type of nonelectrostatic contributions to include. INPUT SECTION: $solvent**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * Cav
>     * Cavitation energy
>     * Buck
>     * Buckingham dispersion and repulsion energy from atomic number
>     * LJ
>     * Lennard-Jones dispersion and repulsion energy from force field
>     * BuckCav
>     * Buck + Cav
>     * LJCav
>     * LJ + Cav
> * **Recommendation**: A very limited set of parameters for the Buckingham potential is available at present.

### `NSolventAtoms`

> **The number of different types of atoms. INPUT SECTION: $solvent**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $N$
>     * Specifies that there are
>     * $N$
>     * different types of atoms.
> * **Recommendation**: This keyword is necessary when NonEls = Buck , LJ , BuckCav , or LJCav . Methanol ( $\rm CH_{3}OH$ ), for example, has three types of atoms (C, H, and O).

### `SolventAtom`

> **Specifies a unique solvent atom. INPUT SECTION: $solvent**
>
> * **Type**: `Various`
> * **Default**: `None.`
> * **Options**:
>     * Input (TYPE)
>     * Description
>     * Number1 (INTEGER):
>     * The atomic number of the atom
>     * Number2 (INTEGER):
>     * How many of this atom are in a solvent molecule
>     * Number3 (INTEGER):
>     * Force field atom type
>     * SASradius (FLOAT):
>     * Probe radius (in Å) for defining the solvent accessible surface
> * **Recommendation**: If not using LJ or LJCav , then Number3 should be set to 0. The keyword is necessary when NonEls = Buck , LJ , BuckCav , or LJCav

### `Temperature`

> **Specifies the solvent temperature. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `300.0`
> * **Options**:
>     * $T$
>     * Use a temperature of
>     * $T$
>     * , in Kelvin.
> * **Recommendation**: Used only for the cavitation energy.

### `Pressure`

> **Specifies the solvent pressure. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `1.0`
> * **Options**:
>     * $P$
>     * Use a pressure of
>     * $P$
>     * , in bar.
> * **Recommendation**: Used only for the cavitation energy.

### `SolventRho`

> **Specifies the solvent number density INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `Determined for water, based on temperature.`
> * **Options**:
>     * $\rho$
>     * Use a density of
>     * $\rho$
>     * , in molecules/Å
>     * ${}^{3}$
>     * .
> * **Recommendation**: Used only for the cavitation energy.

### `SolventRadius`

> **The radius of a solvent molecule of the PCM solvent. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `None`
> * **Options**:
>     * $r$
>     * Use a radius of
>     * $r$
>     * , in Å.
> * **Recommendation**: Used only for the cavitation energy.

The following example illustrates the use of the nonelectrostatic interactions.

???+ example "Example 11.7: Optimization of trifluoroethanol in water using both electrostatic and
nonelectrostatic PCM interactions. OPLS-AA parameters are used in the Lennard-Jones
potential for dispersion and repulsion."
    ```qchem
    $molecule
       0 1
       C    -0.245826    -0.351674    -0.019873     23
       C     0.244003     0.376569     1.241371     22
       O     0.862012    -0.527016     2.143243     24
       F     0.776783    -0.909300    -0.666009     26
       F    -0.858739     0.511576    -0.827287     26
       F    -1.108290    -1.303001     0.339419     26
       H    -0.587975     0.878499     1.736246     27
       H     0.963047     1.147195     0.961639     27
       H     0.191283    -1.098089     2.489052     25
    $end
    
    $rem
       JOBTYPE        OPT
       BASIS          6-31G*
       METHOD         B3LYP
       SOLVENT_METHOD PCM
       FORCE_FIELD    OPLSAA
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       HeavyPoints 194
       HPoints     194
       Radii       Bondi
       vdwScale    1.2
    $end
    
    $solvent
       NonEls        LJCav
       NSolventAtoms 2
       SolventAtom   8 1 186 1.30
       SolventAtom   1 2 187 0.01
       SolventRadius 1.35
       Temperature   298.15
       Pressure      1.0
       SolventRho    0.03333
       Dielectric    78.39
    $end
    ```

## 11.2.4.5 Job Control and Examples for Non-Equilibrium Solvation

The **OpticalDielectric** keyword in the *$solvent* section is needed for nonequilibrium
calculations, or it can be set to a predefined value by specifying **SolventName** instead.
The LR-PCM excitation energy is automatically calculated whenever the CIS/TDDFT calculations are
performed with PCM, but it is turned off while the perturbation scheme is employed.

### `ChargeSeparation`

> **Partition fast and slow charges in solvent equilibrium state INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `No default.`
> * **Options**:
>     * Marcus
>     * Do slow-fast charge separation with the Marcus partition.
>     * Pekar
>     * Do slow-fast charge separation with the Pekar partition.
> * **Recommendation**: Charge separation is used in conjunction with the StateSpecific keyword in $pcm .

### `StateSpecific`

> **Specifies which the state-specific PCM will be used. INPUT SECTION: $pcm**
>
> * **Type**: `Various`
> * **Default**: `No default.`
> * **Options**:
>     * Perturb
>     * Perform ptSS and ptLR for vertical excitations.
>     * External
>     * Perform self-consistent EI-SS-PCM to the excited state (for emission).
>     * Internal
>     * Perform self-consistent II-SS-PCM to the excited state (for emission or excitation).
> * **Recommendation**: Use for vertical excition energies ptSS-PCM or in very polar cases the nonequilibrium II-SS-PCM, and equilibrium EI-SS-PCM for emission energies of long-lived excited states.

### `Td_CEq_NonEq`

> **Specify the self-consistent SS-PCM/TDDFT method to calculate the solvent effects on vertical absorption and emission in solution based on the constrained equilibrium principle for nonequilibrium solvation. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * 1
>     * Calculate nonequilibrium excited-state free energy in absorption based on the equilibrium ground-state reaction field via an RPA calculation at the ground-state geometry.
>     * 2
>     * Calculate nonequilibrium excited-state free energy in absorption based on the nonequilibrium excited-state reaction field via an RPA calculation at the ground-state geometry.
>     * 3
>     * Calculate equilibrium excited-state free energy in emission based on the equilibrium excited-state reaction field via an RPA calculation at the excited-state geometry.
>     * 4
>     * Calculate nonequilibrium ground-state free energy in emission based on the nonequilibrium ground-state reaction field via a pure single-point energy calculation at the excited-state geometry.
> * **Recommendation**: Option 2 and 3 need to be iterated until the excited-state reaction field converges. Option 1 is the first iteration of option 2. After the equilibrium excited state reaction field of option 3 converges, option 4 is executed.

???+ example "Example 11.8: LR-TDDFT/LR-C-PCM low-lying vertical excitation energy"
    ```qchem
    $molecule
       0 1
       C    0  0  0.0
       O    0  0  1.21
    $end
    
    $rem
       EXCHANGE            B3LYP
       CIS_N_ROOTS         10
       CIS_SINGLETS        TRUE
       CIS_TRIPLETS        TRUE
       RPA                 TRUE
       BASIS               6-31+G*
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric         78.39
       OpticalDielectric  1.777849
    $end
    ```

???+ example "Example 11.9: PCM solvation effects on the vertical excitation energies of planar DMABN
using the ptSS and ptLR methods."
    ```qchem
    $molecule
       0  1
       C     0.000046   -0.000398    1.904953
       C     1.210027    0.000379    1.186051
       C     1.214640   -0.000065   -0.194515
       C     0.000164   -0.000616   -0.933832
       C    -1.214349   -0.001557   -0.194687
       C    -1.209753   -0.001846    1.185775
       H     2.151949    0.001377    1.722018
       H     2.164371    0.000481   -0.709640
       H    -2.164082   -0.002008   -0.709781
       H    -2.151763   -0.002287    1.721615
       C    -0.000227    0.001061    3.325302
       N    -0.000475    0.002405    4.484321
       N     0.000053   -0.000156   -2.297372
       C    -1.258656    0.001284   -3.036994
       H    -1.041042    0.001615   -4.102376
       H    -1.860897   -0.885647   -2.811117
       H    -1.859247    0.889133   -2.810237
       C     1.258563   -0.000660   -3.037285
       H     1.860651    0.886208   -2.810755
       H     1.859362   -0.888604   -2.811461
       H     1.040664   -0.000097   -4.102609
    $end
    
    $rem
       EXCHANGE              LRC-wPBEPBE
       OMEGA                 260
       BASIS                 6-31G*
       CIS_N_ROOTS           10
       RPA                   2
       CIS_SINGLETS          1
       CIS_TRIPLETS          0
       CIS_RELAXED_DENSITY   TRUE
       SOLVENT_METHOD        PCM
    $end
    
    $pcm
       NonEquilibrium
       Theory                 IEFPCM
       StateSpecific          Perturb
    $end
    
    $solvent
       Dielectric             35.688000       ! Acetonitrile
       OpticalDielectric      1.806874
    $end
    ```

???+ example "Example 11.11.10: TDDFT with External Iteration SS-PCM for nitrate in acetonitrile."
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype    ¯¯         sp
       method ¯¯             PBE0
       basis  ¯¯¯           3-21g
    point_group_symmetry False
       cis_n_roots             2           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method        ¯ pcm
    $end
    
    $pcm
       StateSpecific           External    ! Keyword for External Iteration SS-PCM
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             2
       cis_singlets            true
       cis_triplets            false
       rpa                     false
       cis_moments             true
       cis_relaxed_density     true
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           External
       Eqsolv                  15          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       LinearResponse          false
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    ```

???+ example "Example 11.11.11: TDDFT with Internal Iteration SS-PCM and the additional ground state calculation for
vertical emission energies of nitrate in acetonitrile."
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             4           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           Internal    ! Keyword for Internal Iteration SS-PCM
       ChargeSeparation        MARCUS      ! Keyword for the charge separation
       InternalIteration       AEM(f)      ! Procedure (VEM(f), VEM(d), AEM(f), or AEM(d)) + state sequence (add e.g.: -state 1 3 1 0)
       Eqsolv                  10          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       theory                  iefpcm      ! PCM Theory (else CPCM)
       rf_ptss_save            true        ! Save the eq. reaction field of Ref. State
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype                 sp
       method ¯¯             PBE0
       basis                   3-21g
    point_group_symmetry False
       solvent_method          pcm
    $end
    
    $pcm
       theory                  iefpcm
       rf_ptss_read            true        ! Flag to read the reaction field and do RF-ptSS calc
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    
    ```

???+ example "Example 11.11.12: SS-PCM/TDDFT low-lying vertical excitation energy based on the constrained
equilibrium principle."
    ```qchem
    $molecule
      0 1
      C     0.00000000    0.00000000    0.00000000
      O     0.00000000    0.00000000    1.22027000
      C     1.28132052    0.00000000   -0.79367740
      H     2.14499626   -0.00083829   -0.12870724
      H     1.30455453   -0.88067608   -1.44302080
      H     1.30547296    0.88142003   -1.44198042
      C    -1.28127663    0.00458022   -0.79382239
      H    -2.14504139    0.00537545   -0.12895306
      H    -1.30703468   -0.87518579   -1.44430491
      H    -1.30295394    0.88686493   -1.44106115
    $end
    
    $rem
       METHOD              M062X
       BASIS               6-31+G*
       JOB_TYPE            sp
       RPA                 2
       DFT_D               D3
       cis_singlets        TRUE
       cis_triplets        FALSE
       cis_n_roots         5
       cis_state_deriv     1
       CIS_DYNAMIC_MEM     TRUE
       CIS_RELAXED_DENSITY TRUE
       CIS_MOMENTS         TRUE
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory              SSVPE
       ChargeSeparation    Pekar
       StateSpecific       Perturb
       Td_CEq_NonEq        1
    $end
    
    $solvent
       Dielectric          32.613
       OpticalDielectric   1.766
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       METHOD              M062X
       BASIS               6-31+G*
       JOB_TYPE            sp
       RPA                 2
       DFT_D               D3
       cis_singlets        TRUE
       cis_triplets        FALSE
       cis_n_roots         5
       cis_state_deriv     1
       CIS_DYNAMIC_MEM     TRUE
       CIS_RELAXED_DENSITY TRUE
       CIS_MOMENTS         TRUE
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory              SSVPE
       ChargeSeparation    Pekar
       StateSpecific       Perturb
       Td_CEq_NonEq       2
    $end
    
    $solvent
       Dielectric          32.613
       OpticalDielectric   1.766
    $end
    ```

???+ example "Example 11.11.13: SS-PCM/TDDFT equilibrium excited-state free energy in emission based on the constrained equilibrium principle."
    ```qchem
    $molecule
      0 1
      C    0.00000000   -0.57624800    0.00000000
      H   -0.95773500   -1.10813200    0.00000000
      H    0.95773500   -1.10813200    0.00000000
      O    0.00000000    0.70921900    0.00000000
    $end
    
    $rem
      METHOD               M062X
      BASIS                6-31+G*
      CIS_N_ROOTS          5
      RPA                  2
      CIS_SINGLETS         1
      CIS_TRIPLETS         0
      CIS_DYNAMIC_MEM      TRUE
      CIS_RELAXED_DENSITY  TRUE
      SOLVENT_METHOD       PCM
      POP_MULLIKEN         -1
      CIS_MOMENTS          TRUE
      DFT_D                D3
      CIS_CONVERGENCE      5
      MAX_CIS_CYCLES       150
    $end
    
    $pcm
      Theory               SSVPE
      Method               SWIG
      ChargeSeparation     EXCITED
      StateSpecific        1
      Td_CEq_NonEq         3
    $end
    
    $solvent
      Dielectric           78.5
      OpticalDielectric    1.778
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
      METHOD                M062X
      BASIS                 6-31+G*
      SOLVENT_METHOD        PCM
      POP_MULLIKEN          -1
      DFT_D                 D3
      SCF_CONVERGENCE       8
    $end
    
    $pcm
      Theory                SSVPE
      Method                SWIG
      ChargeSeparation      Pekar
      StateSpecific         Pekar
      Td_CEq_NonEq          4
    $end
    
    $solvent
      Dielectric            78.5
      OpticalDielectric     1.778
    $end
    ```

???+ example "Example 11.14: SS-PCM/TDDFT nonequilibrium ground-state free energy in emission based on the
constrained equilibrium principle."
    ```qchem
    $molecule
       0 1
       C    0.00000000   -0.57624800    0.00000000
       H   -0.95773500   -1.10813200    0.00000000
       H    0.95773500   -1.10813200    0.00000000
       O    0.00000000    0.70921900    0.00000000
    $end
    
    $rem
       METHOD           M062X
       BASIS            6-31+G(d)
       SOLVENT_METHOD   PCM
       POP_MULLIKEN     -1
       DFT_D            D3
    $end
    
    $pcm
       Theory            SSVPE
       Method            SWIG
       ChargeSeparation  Pekar
       StateSpecific     Pekar
       Td_CEq_NonEq      4
    $end
    
    $solvent
       Dielectric 78.5
       OpticalDielectric 1.778
    $end
    ```
