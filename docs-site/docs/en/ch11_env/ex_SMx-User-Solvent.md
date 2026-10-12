---
title: "11.2.9 SM x Models"
---

## 11.2.9 SM$x$ Models

(July 4, 2026)

The SM$x$ models were developed by Cramer, Truhlar, and coworkers at the University
of Minnesota. Versions SM8,[[912]](../bib_references/bib.md#bib942)
 SM12,[[910]](../bib_references/bib.md#bib946)
 and SMD[[909]](../bib_references/bib.md#bib943)

are available in **Q-Chem**. Of these, SMD is recommended because it is designed to work with arbitrary basis sets
(unlike SM8) and it is implemented with both analytic gradients and Hessians (unlike SM8 or SM12).

Each of these SM$x$ methods is designed as a “universal” solvation model,[[281]](../bib_references/bib.md#bib286)

in the sense that it can be applied to any solvent for which a small of descriptors is known.
The solvent descriptors are:

- dielectric constant
- refractive index
- bulk surface tension
- acidity on the Abraham scale
- basicity on the Abraham scale
- carbon aromaticity, which equals the fraction of non-hydrogenic
solvent atoms that are aromatic carbon atoms
- electronegative halogenicity, which equals the fraction of
non-hydrogenic solvent atoms that are F, Cl, or Br).

These models consist of a generalized Born treatment of continuum electrostatic
interactions, along with nonelectrostatic interactions that are parameterized
in terms of atomic surface tensions. The nonelectrostatic interactions
include cavitation, dispersion, and changes in solvent structure, and the
treatment of these nonelectrostatic effects is crucial to obtaining accurate (free) energies of solvation.

An SM$x$ calculation is requested by setting SOLVENT_METHOD = SM8, SM12, or SMD.
Some method-specific keywords are required (in a *$smx* input section) for some of these models, and these are discussed
in the sections that follow. At a minimum, each of these models that the solvent be specified in the *$smx* section unless that solvent
is water. Available solvents are listed in Table [11.7](#table:SMx-solvents). These names should be given in the *$smx* section without
spaces or hyphens, so that propanoic acid from Table [11.7](#table:SMx-solvents) becomes `propanoicacid` and 1-hexanol becomes `1hexanol`.

Table 11.7: Solvents available for SM$x$ calculations.${}^{a}$

<table class="ltx_tabular">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt">1,1,1-trichloroethane</td>
<td class="ltx_td ltx_align_left ltx_border_tt">bromoethane</td>
<td class="ltx_td ltx_align_left ltx_border_tt">
$m$-ethylbenzoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,1,2-trichloroethane</td>
<td class="ltx_td ltx_align_left">bromooctane</td>
<td class="ltx_td ltx_align_left">
$m$-ethylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,1-dichloroethane</td>
<td class="ltx_td ltx_align_left">butanal</td>
<td class="ltx_td ltx_align_left">
$m$-ethylmethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,2,4-trimethylbenzene</td>
<td class="ltx_td ltx_align_left">butanoicacid</td>
<td class="ltx_td ltx_align_left">
$m$-ethylphenylketone</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,4-dioxane</td>
<td class="ltx_td ltx_align_left">butanone</td>
<td class="ltx_td ltx_align_left">
$m$-ethylpropanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromo-2-methylpropane</td>
<td class="ltx_td ltx_align_left">butanonitrile</td>
<td class="ltx_td ltx_align_left">
$m$-ethylbutanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromopentane</td>
<td class="ltx_td ltx_align_left">butylethanoate</td>
<td class="ltx_td ltx_align_left">
$m$-ethylcyclohexane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromopropane</td>
<td class="ltx_td ltx_align_left">butylamine</td>
<td class="ltx_td ltx_align_left">
$m$-ethylformamide</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-butanol</td>
<td class="ltx_td ltx_align_left">butylbenzene</td>
<td class="ltx_td ltx_align_left">
$m$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-chloropentane</td>
<td class="ltx_td ltx_align_left">carbon disulfide</td>
<td class="ltx_td ltx_align_left">heptane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-chloropropane</td>
<td class="ltx_td ltx_align_left">carbon tetrachloride</td>
<td class="ltx_td ltx_align_left">hexadecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-decanol</td>
<td class="ltx_td ltx_align_left">chlorobenzene</td>
<td class="ltx_td ltx_align_left">hexane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-fluorooctane</td>
<td class="ltx_td ltx_align_left">chlorotoluene</td>
<td class="ltx_td ltx_align_left">nitrobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-heptanol</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">cis</span>-1,2-dimethylcyclohexane</td>
<td class="ltx_td ltx_align_left">nitroethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexanol</td>
<td class="ltx_td ltx_align_left">decalin</td>
<td class="ltx_td ltx_align_left">nitromethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexene</td>
<td class="ltx_td ltx_align_left">cyclohexane</td>
<td class="ltx_td ltx_align_left">methylaniline</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexyne</td>
<td class="ltx_td ltx_align_left">cyclohexanone</td>
<td class="ltx_td ltx_align_left">nonane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodobutane</td>
<td class="ltx_td ltx_align_left">cyclopentane</td>
<td class="ltx_td ltx_align_left">octane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodopentene</td>
<td class="ltx_td ltx_align_left">cyclopentanol</td>
<td class="ltx_td ltx_align_left">pentane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodopropane</td>
<td class="ltx_td ltx_align_left">cyclopentanone</td>
<td class="ltx_td ltx_align_left">
$o$-chlorotoluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-nitropropane</td>
<td class="ltx_td ltx_align_left">decane</td>
<td class="ltx_td ltx_align_left">
$o$-cresol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-nonanol</td>
<td class="ltx_td ltx_align_left">dibromomethane</td>
<td class="ltx_td ltx_align_left">
$o$-dichlorobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-octanol</td>
<td class="ltx_td ltx_align_left">dibutyl ether</td>
<td class="ltx_td ltx_align_left">
$o$-nitrotoluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentanol</td>
<td class="ltx_td ltx_align_left">dichloromethane</td>
<td class="ltx_td ltx_align_left">
$o$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentene</td>
<td class="ltx_td ltx_align_left">diethyl ether</td>
<td class="ltx_td ltx_align_left">pentadecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentyne</td>
<td class="ltx_td ltx_align_left">diethylsulfide</td>
<td class="ltx_td ltx_align_left">pentanal</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-propanol</td>
<td class="ltx_td ltx_align_left">diethylamine</td>
<td class="ltx_td ltx_align_left">pentanoic acid</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,2,2-trifluoroethanol</td>
<td class="ltx_td ltx_align_left">diiodomethane</td>
<td class="ltx_td ltx_align_left">pentylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,2,4-trimethylpentane</td>
<td class="ltx_td ltx_align_left">dimethyldisulfide</td>
<td class="ltx_td ltx_align_left">pentylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,4-dimethylpentane</td>
<td class="ltx_td ltx_align_left">dimethylacetamide</td>
<td class="ltx_td ltx_align_left">perfluorobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,4-dimethylpyridine</td>
<td class="ltx_td ltx_align_left">dimethylformamide</td>
<td class="ltx_td ltx_align_left">phenyl ether</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,6-dimethylpyridine</td>
<td class="ltx_td ltx_align_left">dimethylpyridine</td>
<td class="ltx_td ltx_align_left">propanal</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-bromopropane</td>
<td class="ltx_td ltx_align_left">DMSO</td>
<td class="ltx_td ltx_align_left">propanoic acid</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-chlorobutane</td>
<td class="ltx_td ltx_align_left">dipropylamine</td>
<td class="ltx_td ltx_align_left">propanonitrile</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-heptanone</td>
<td class="ltx_td ltx_align_left">dodecane</td>
<td class="ltx_td ltx_align_left">propylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-hexanone</td>
<td class="ltx_td ltx_align_left">
$E$-1,2-dichloroethene</td>
<td class="ltx_td ltx_align_left">propylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-methylpentane</td>
<td class="ltx_td ltx_align_left">
$E$-2-pentene</td>
<td class="ltx_td ltx_align_left">
$p$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-methylpyridine</td>
<td class="ltx_td ltx_align_left">ethanethiol</td>
<td class="ltx_td ltx_align_left">pyridine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-nitropropane</td>
<td class="ltx_td ltx_align_left">ethanol</td>
<td class="ltx_td ltx_align_left">pyrrolidine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-octanone</td>
<td class="ltx_td ltx_align_left">ethylethanoate</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">sec</span>-butanol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-pentanone</td>
<td class="ltx_td ltx_align_left">ethylmethanoate</td>
<td class="ltx_td ltx_align_left">
$t$-butanol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-propanol</td>
<td class="ltx_td ltx_align_left">ethylphenyl ether</td>
<td class="ltx_td ltx_align_left">
$t$-butylbenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-propen-1-ol</td>
<td class="ltx_td ltx_align_left">ethylbenzene</td>
<td class="ltx_td ltx_align_left">tetrachloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">3-methylpyridine</td>
<td class="ltx_td ltx_align_left">ethylene glycol</td>
<td class="ltx_td ltx_align_left">tetrahydrofuran</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">3-pentanone</td>
<td class="ltx_td ltx_align_left">fluorobenzene</td>
<td class="ltx_td ltx_align_left">tetrahyrothiophenedioxide</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-heptanone</td>
<td class="ltx_td ltx_align_left">formamide</td>
<td class="ltx_td ltx_align_left">tetralin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-methyl-2-pentanone</td>
<td class="ltx_td ltx_align_left">formic acid</td>
<td class="ltx_td ltx_align_left">thiophene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-methylpyridine</td>
<td class="ltx_td ltx_align_left">hexadecyliodide</td>
<td class="ltx_td ltx_align_left">thiophenol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">5-nonanone</td>
<td class="ltx_td ltx_align_left">hexanoic acid</td>
<td class="ltx_td ltx_align_left">toluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetic acid</td>
<td class="ltx_td ltx_align_left">iodobenzene</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">trans</span>-decalin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetone</td>
<td class="ltx_td ltx_align_left">iodoethane</td>
<td class="ltx_td ltx_align_left">tribromomethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetonitrile</td>
<td class="ltx_td ltx_align_left">iodomethane</td>
<td class="ltx_td ltx_align_left">tributylphosphate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">aniline</td>
<td class="ltx_td ltx_align_left">isobutanol</td>
<td class="ltx_td ltx_align_left">trichloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">anisole</td>
<td class="ltx_td ltx_align_left">isopropyl ether</td>
<td class="ltx_td ltx_align_left">trichloromethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzaldehyde</td>
<td class="ltx_td ltx_align_left">isopropylbenzene</td>
<td class="ltx_td ltx_align_left">triethylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzene</td>
<td class="ltx_td ltx_align_left">isopropyltoluene</td>
<td class="ltx_td ltx_align_left">undecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzonitrile</td>
<td class="ltx_td ltx_align_left">
$m$-cresol</td>
<td class="ltx_td ltx_align_left">water</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzyl alcohol</td>
<td class="ltx_td ltx_align_left">mesitylene</td>
<td class="ltx_td ltx_align_left">
$Z$-1,2-dichloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">bromobenzene</td>
<td class="ltx_td ltx_align_left">methanol</td>
<td class="ltx_td ltx_align_left">other</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt" colspan="3">
${}^{a}$<span class="ltx_text" style="font-size:80%;">Solvent names should be specified without hyphens or spaces.</span>
</td>
</tr>
</table>

By setting **solvent** = **other**, the user may specify their own solvent. This requires
specification of the following solvent descriptors:

- **Dielec**, the dielectric constant, $\varepsilon$, of the solvent
- **SolN** , the index of refraction at optical frequencies at 293 K, $n_{20}^{D}$
- **SolA** , Abraham’s hydrogen bond acidity, $\sum{\alpha}_{2}^{\text{H}}$
- **SolB** , Abraham’s hydrogen bond basicity, $\sum{\beta}_{2}^{\text{H}}$
- **SolG** , $\gamma=\gamma_{m}/\gamma^{0}$
where $\gamma_{m}$ is the macroscopic surface tension at air/solvent
interface at 298 K and $\gamma^{0}$ is 1 cal mol${}^{-1}$ Å${}^{-2}$
(1 dyne/cm = 1.43932 cal mol${}^{-1}$ Å${}^{-2}$)
- **SolC**, aromaticity ($\phi$), equal to the fraction of non-hydrogen solvent atoms that are aromatic carbon atoms
- **SolH**, electronegative “halogenicity” ($\psi$), equal to the fraction of non-hydrogen solvent atoms that are F, Cl or Br

These parameters are specified in the *$smx* input section as suggested in Example 11.2.9.
(Any solvent descriptors that are omitted from the *$smx* section default to zero.)
Values can be derived from experiment or from
interpolation or extrapolation of data available for other solvents. Solvent
parameters for common organic solvents are tabulated in the Minnesota Solvent
Descriptor Database. The latest version of this database is available at:

`http://comp.chem.umn.edu/solvation/mnsddb.pdf`

Job controls variables for the *$smx* section that are common to SM8, SM12, and SMD are given below.

### `Solvent`

> **Sets the SM $x$ solvent INPUT SECTION: $smx**
>
> * **Type**: `STRING`
> * **Default**: `water`
> * **Options**:
>     * Any name from the list of solvents given in Table: 11.7 .
> * **Recommendation**: NONE

### `Print`

> **Controls extra printing for SM $x$ calculations INPUT SECTION: $smx**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Minimal printing
>     * `1`: Detailed breakdown of energy components (at SCF convergence)
>     * `2`: Additional information, dependent on the specific SM $x$ model
> * **Recommendation**: The energy components obtained with print = 1 may be useful, although a summary is printed by default. The value print = 2 is probably only useful for diagnosing problems.

???+ example "Example 11.16: SMD model with a user-defined solvent."
    ```qchem
    $comment
    User-defined specification of pentane.
    (Result should be equivalent to SOLVENT = PENTANE)
    $end
    
    $molecule
       0 1
       C    -0.361658    -0.986967     0.222366
       C    -1.331098     0.144597    -0.108363
       O    -0.592574     1.354183     0.036738
       C     0.798089     1.070899     0.136509
       C     0.964682    -0.396154    -0.256319
       H    -0.625676    -1.925862    -0.267011
       H    -0.333229    -1.158101     1.302753
       H    -1.697529     0.068518    -1.140448
       H    -2.193412     0.181620     0.562129
       H     1.130199     1.238399     1.169839
       H     1.348524     1.754318    -0.514697
       H     1.050613    -0.489646    -1.343151
       H     1.843065    -0.855802     0.199659
    $end
    
    $rem
       METHOD           b3lyp
       BASIS            6-31G*
       SOLVENT_METHOD   smd
    $end
    
    $smx
    solvent other
    epsilon 1.840
    SolN    1.357
    SolA    0.000  ! could be omitted
    SolB    0.000  ! could be omitted
    SolG   22.300
    SolC    0.000  ! could be omitted
    SolH    0.000  ! could be omitted
    $end
    
    ```

## 11.2.9.1 The SM8 Model

The SM8 model is described in detail in Ref. [[912]](../bib_references/bib.md#bib942)
. It
may be employed in conjunction with density functional theory (with any density
functional available in **Q-Chem**) or with Hartree-Fock theory, but is intended
for use only with the 6-31G*, 6-31+G*, and 6-31+G** basis sets, for reasons
discussed below.

Bulk (continuum) electrostatic interactions in SM8 are described in terms of a
generalized Born (GB) SCRF,[[569]](../bib_references/bib.md#bib580)

using a solute cavity constructed from atom-centered spheres. For the atoms H,
C, N, O, F, Si, P, S, Cl, and Br, atomic radii have been specifically optimized
for use with SM8, whereas for other atoms the Bondi radius is
used,[[146]](../bib_references/bib.md#bib136)
 or else a value of 2.0 Å for atoms not included in
Bondi’s paper. Geometry-dependent radii are computed from these “intrinsic”
Coulomb radii via a de-screening approximation.[[912]](../bib_references/bib.md#bib942)

In addition to GB electrostatics, there are several other contributions to the
SM8 standard-state free energy of solvation. One is the
electronic-nuclear-polarization (ENP) energy, which is a more descriptive (and precise)
name for what is often called the electrostatic solvation energy.[[569]](../bib_references/bib.md#bib580)

Another contribution to the free energy of
solvation comes from short-range interactions with solvent molecules in the
first solvation shell, and is sometimes called the cavitation–dispersion–solvent-structure
(CDS) term. Collectively, the various CDS interactions represent the nonelectrostatic
contributions to the solvation energy.

In the SM$x$ models, this nonelectrostatic
contribution is modeled as a sum of terms proportional to
the solvent-accessible surface area (SASA) of each individual solute atoms.
The proportionality constants, which are parameters of the model, have units of
energy/(area)${}^{2}$ so are sometimes called atomic surface tension parameters.
The SASA of the solute molecule is the area of a surface generated by the
center of a spherical effective solvent molecule rolling on the van der Waals
surface of the solute molecule, as in the solvent-accessible surface that was
mentioned in Section [11.2.3](topic_pcm-em.md). The SASA is computed using the algorith
described in Ref. [[835]](../bib_references/bib.md#bib868)
 along with Bondi’s
values for the van der Waals radii,[[146]](../bib_references/bib.md#bib136)
 or else a value of
2.0 Å if no Bondi radius is available. (As in the case of
nonelectrostatic interactions in PCMs, this means that a different molecular
surface is used for the bulk electrostatics as compared to the
nonelectrostatic interactions.) The solvent probe radius used to generate the
SASAs is set to 0.40 Å for all solvents. Note that the solvent-structure
part of the CDS term includes many aspects of solvent structure that are not
described by bulk electrostatics, for example, hydrogen bonding, exchange
repulsion, and the variation of the effective dielectric constant in the first
solvation shell, relative to its bulk value. The empirical nature of the
CDS term also makes up for errors due to ($i$) assuming fixed and
model-dependent values of the intrinsic Coulomb radii, and ($ii$) any
systematic errors in the description of the solute–solvent electrostatic
interactions using the GB approximation.

The final component of the SM8 solvation free energy is the concentration
component. This is zero if the standard-state concentration of the solute is
the same in the gas and solution phases (*e.g.*, if it is 1 mol/L in the gas
phase as well as in the solution). Otherwise, this correction can be computed
using ideal gas formulas, as discussed below.

SM8 does not require the user to assign molecular mechanics atom types to atoms
or groups; all atomic surface tensions in the theory are unique and continuous
functions of the solute geometry, defined by the model and calculated
internally within **Q-Chem**. In principle, SM8 can be used with any level of
electronic structure theory so long as accurate partial charges can be
computed, but **Q-Chem**’s implementation of SM8 specifically uses
self-consistently polarized Charge Model 4 (CM4) class IV charges.[[678]](../bib_references/bib.md#bib702)

CM4 charges are obtained from Löwdin population analysis charges, via a
mapping whose parameters depend on the basis set (and only on the basis set,
not on the density functional or anything else).
The supported basis sets in **Q-Chem** are 6-31G*, 6-31+G*, and 6-31+G**;
other basis sets should not be used in SM8 calculations.
The charge mapping parameters are given in Ref. [[678]](../bib_references/bib.md#bib702)
.

The SM8 solvation free energy is output at $T=298$ K for a standard-state
concentration of 1 M in both the gas and solution phase. However, solvation
free energies in the literature are often tabulated using a standard state of
$P=1$ atm for the gas. To convert 1 M-to1 M solvation free energies at 298 K
to a standard state consisting of $P=1$ atm for the gas and a 1 M concentration
in solution, add $+1.89$ kcal/mol to the computed solvation free energy.

Solution-phase geometry optimizations can be carried out, but basis sets that
use spherical harmonic $d$ functions, or angular momentum higher than $d$ ($f$,
$g$, *etc.*) are not supported. Since, by definition, the 6-31G*, 6-31+G*,
and 6-31+G** basis sets have Cartesian $d$ shells, they are examples of basis
sets that may be used for geometry optimization with SM8. Solution-phase
Hessian calculations can be carried out by numerical differentiation of
analytical energy gradients or by double differentiation of energies, although
the former procedure is both more stable and more economical. The analytic
gradients of SM8 are based on the analytical derivatives of the polarization
free energy and the analytical derivatives of the CDS terms derived in Ref. [[1577]](../bib_references/bib.md#bib1640)
.

The SM8 test suite contains the following representative examples:

- single-point solvation energy and analytical gradient calculation for
2,2-dichloroethenyl dimethyl phosphate in water at the
M06-2X/6-31G* level;
- single-point solvation energy calculation for 2,2-dichloroethenyl
dimethyl phosphate in benzene at the M06-2X/6-31G*
level;
- single-point solvation energy calculation for 2,2-dichloroethenyl
dimethyl phosphate in ethanol at the M06-2X/6-31G* level;
- single-point solvation energy calculation for 5-fluorouracil in water at
the M06/6-31+G* level;
- single-point solvation energy calculation for 5-fluorouracil in octanol
at the M06-L/6-31+G* level;
- single-point solvation energy and analytical gradient calculation for
5-fluorouracil in fluorobenzene at the M06-HF/6-31+G** level;
- geometry optimization for protonated methanol $\rm CH_{3}OH_{2}^{+}$ in water
at the B3LYP/6-31G* level;
- finite-difference frequency (with analytical gradient) calculation for
protonated methanol $\rm CH_{3}OH_{2}^{+}$ in water at the B3LYP/6-31G* level.

Users who wish to calculate solubilities can calculate them from the free
energies of solvation by the method described in
Ref. [[1358]](../bib_references/bib.md#bib1418)
. The present model can also be used with
confidence to calculate partition coefficients (*e.g.*, Henry’s Law constants,
octanol/water partition coefficients, *etc.*) by the method described in
Ref. 

.

The user should note that the free energies of solvation calculated by the SM8
model in the current version of **Q-Chem** are all what may be called equilibrium
free energies of solvation. The nonequilibrium algorithm required for
vertical excitation energies[[813]](../bib_references/bib.md#bib846)
 is not yet available in **Q-Chem**.
(Nonequilibrium versions of PCMs are available instead; see Section [11.2.3.3](topic_pcm-em.md#subsubsec:noneq-PCM).)

## 11.2.9.2 The SM12 Model

The SM12 model[[910]](../bib_references/bib.md#bib946)
 is also available in **Q-Chem**. Similar to
SM8, it employs (a) the generalized Born approximation for the bulk
electrostatic contribution to the free energy of solvation, and (b) the same
formulas (with re-optimized parameters) for CDS contributions. SM12 holds
several advantages over SM8, and perhaps foremost among these is that it uses
CM5 charges,[[911]](../bib_references/bib.md#bib945)
 which are based on Hirshfeld population
analysis, or else charges derived from the electrostatic
potential,[[1258]](../bib_references/bib.md#bib1310)
 for the bulk electrostatics term.
These charges are stable with respect to extension of the basis set, and thus
SM12 can be used with larger basis sets whereas SM8 is limited to 6-31G*,
6-31+G*, and 6-31+G**, due to instabilities in the Löwdin charges in larger
basis sets. In addition, SM12 is parameterized using a more diverse training
set as compared to SM8, and is defined for the entire periodic table. However,
the SM12 analytic gradient is not available in **Q-Chem** at present.

An SM12 calculation is requested by setting SOLVENT_METHOD =
SM12 in the *$rem* section. The manner in which the electrostatic
term is computed is controlled by the **Charges** keyword in the *$smx*
input section.

### `Charges`

> **Sets the type of atomic charges for the SM12 electrostatic term. INPUT SECTION: $smx**
>
> * **Type**: `STRING`
> * **Default**: `CM5`
> * **Options**:
>     * `CM5`: Charge Model 5 charges
>     * `911`: Marenich A. V. et al. J. Chem. Theory Comput. (2012) ,
>     * `8`: , pp. 527 . Link
>     * `MK`: Merz-Singh-Kollman charges
>     * `1258`: Singh U. C., Kollman P. A. J. Comput. Chem. (1984) ,
>     * `5`: , pp. 129 . Link
>     * `CHELPG`: ChElPG charges
>     * `159`: Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) ,
>     * `11`: , pp. 361 . Link
> * **Recommendation**: None. Merz-Singh-Kollman and ChElPG charges are fit to reproduce the molecular electrostatic potential on the van der Waals surface or on a cubic grid, respectively, whereas CM5 is an empirical model based on Hirshfeld population analysis.

???+ example "Example 11.17: SM12CM5 calculation of the solvation free energy of water in the 1-octanol
solvent."
    ```qchem
    $molecule
       0 1
       O    0.000000    0.125787   0.000000
       H    0.758502   -0.503148   0.000000
       H   -0.758502   -0.503148   0.000000
    $end
    
    $rem
       METHOD               b3lyp
       BASIS                6-31G*
       SCF_GUESS            core
       SOLVENT_METHOD       sm12
       POINT_GROUP_SYMMETRY false
    $end
    
    $smx
       solvent 1octanol
       charges chelpg
    $end
    ```

## 11.2.9.3 The SMD Model

The SMD model[[909]](../bib_references/bib.md#bib943)
 is also available in **Q-Chem**. Within the
original verion of this model,
the electrostatic contribution to the free energy solvation is described
via the IEF-PCM model, where the CDS contributions follow the formulas as SM8
and SM12 with the parameters re-optimized to be compatible with the IEF-PCM
electrostatics. Relative to SM8 or SM12, where the electrostatic interactions
are defined in terms of atomic point charges that are sensitive to the choice
of basis set (and therefore only certain basis sets are supported for use with
these models), SMD can be used with any basis set.

The **Q-Chem** implementation of the SMD model uses the simpler C-PCM model by
default as for SOLVENT_METHOD = PCM. Based on the benchmark
results shown in Table 4 of Ref. [[569]](../bib_references/bib.md#bib580)
, the C-PCM results
essentially have no difference from the IEF-PCM ones in terms of accuracy.
An SMD energy, gradient, or Hessian calculation is requested by setting
SOLVENT_METHOD = SMD in the *$rem* section. While **Q-Chem**
users can vary the parameters for the C-PCM or IEF-PCM part of the SMD calculation, this
is not recommended because such modifications may be less
compatible with the CDS parameters and thus lead to less accurate results.
C-PCM is the preferred electrostatics model for SMD calculations.
Starting with **Q-Chem** v. 6.3, seminumerical SMD
Hessians are available, using the C-PCM analytic Hessian[[844]](../bib_references/bib.md#bib876)
 combined
with a finite-difference evaluation of the CDS contribution.

In **Q-Chem** v. 5.2 and later, the default surface discretization method is changed
from VTN to SwiG in order to ensure the smoothness of potential energy surface.
In addition, the gas-phase SCF calculation that takes place before the SM$x$
calculation is turned off by default. If one wants to obtain the solvation free
energy, then the gas phase calculation is still required and it can be turned
on by setting SMX_GAS_PHASE = TRUE. Setting this *$rem*
variable to TRUE might also be helpful if directly converging SCF with
the SM$x$ models is difficult.

### `SMX_GAS_PHASE`

> **Converge the gas-phase SCF first before doing calculations with SM $x$ models**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Run SMx calculations directly
>     * `TRUE`: Run gas-phase calculation first
> * **Recommendation**: Use the default unless solvation free energy is needed. Set it to TRUE if the SCF calculation fails to converge otherwise.

???+ example "Example 11.18: SMD force calculation for tetrahydrofuran (THF) in the pentane solvent."
    ```qchem
    $molecule
       0 1
       C    -0.361658    -0.986967     0.222366
       C    -1.331098     0.144597    -0.108363
       O    -0.592574     1.354183     0.036738
       C     0.798089     1.070899     0.136509
       C     0.964682    -0.396154    -0.256319
       H    -0.625676    -1.925862    -0.267011
       H    -0.333229    -1.158101     1.302753
       H    -1.697529     0.068518    -1.140448
       H    -2.193412     0.181620     0.562129
       H     1.130199     1.238399     1.169839
       H     1.348524     1.754318    -0.514697
       H     1.050613    -0.489646    -1.343151
       H     1.843065    -0.855802     0.199659
    $end
    
    $rem
       JOBTYPE          force
       METHOD           b3lyp
       BASIS            6-31G*
       SOLVENT_METHOD   smd
    $end
    
    $smx
       solvent pentane
    $end
    ```
