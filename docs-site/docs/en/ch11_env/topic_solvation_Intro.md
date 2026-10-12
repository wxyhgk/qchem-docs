---
title: "11.2.1 Introduction"
---

## 11.2.1 Introduction

(July 4, 2026)

*Ab initio* quantum chemistry makes possible the study of gas-phase
molecular properties from first principles. In liquid solution, however, these
properties may change significantly, especially in polar solvents. Although it
is possible to model solvation effects by including explicit solvent molecules
in the quantum-chemical calculation (*e.g.*, a supramolecular cluster
calculation, averaged over different configurations of the molecules in the
first solvation shell), such calculations are very computationally demanding.
Furthermore, cluster calculations typically do not afford accurate solvation
energies, owing to the importance of long-range electrostatic interactions.
(Hybrid discrete/continuum models, which contain *some* explicit solvent,
can be quite effective, however.[[1101]](../bib_references/bib.md#bib1147)
)
Accurate prediction of solvation free energies is crucial for
modeling of chemical reactions but also for relative conformational energies in solution.

**Q-Chem** contains several different implicit solvent models, which differ
greatly in their level of sophistication. These are generally known as
self-consistent reaction field (SCRF) models, because the continuum solvent
establishes a “reaction field” (additional terms in the solute Hamiltonian)
that depends upon the solute electron density, and must therefore be updated
self-consistently during the iterative convergence of the wave function.
The simplest and oldest of these models that is available in **Q-Chem** is the
multipole expansion method, also known as a Kirkwood-Onsager model,[[569]](../bib_references/bib.md#bib580)

in which the solute molecule is placed inside of a spherical cavity and its
electrostatic potential is represented in terms of a single-center multipole expansion.
(This should not be confused with the *Onsager model*, in which a dipole approximation is used,
and to avoid confusion the *multipolar expansion method* is better terminology.)
More sophisticated models, which use a molecule-shaped cavity and
the full molecular electrostatic potential, include the
conductor-like PCM (C-PCM),[[79]](../bib_references/bib.md#bib61)

the conductor-like screening model (COSMO),

the “surface and simulation of volume polarization for electrostatics”
[SS(V)PE] model,[[245]](../bib_references/bib.md#bib245)
 and the closely-related
“integral equation formalism” (IEF-PCM).[[187]](../bib_references/bib.md#bib181)

For an overview of all of these methods and their interconnections, see the review by Herbert.[[569]](../bib_references/bib.md#bib580)

The C-PCM, IEF-PCM, and SS(V)PE are examples of what are called “apparent
surface charge” SCRF models, and the term *polarizable continuum
models* (PCMs), as popularized by Tomasi and coworkers,[[1363]](../bib_references/bib.md#bib1425)
 is
now used almost universally to refer to this class of solvation models.
**Q-Chem** employs a Switching/Gaussian or “SwiG” implementation of these
PCMs,[[753]](../bib_references/bib.md#bib786)
which resolves a long-standing (though little-publicized) problem with
standard PCMs, namely, that the boundary-element methods used to discretize the
solute/continuum interface may lead to discontinuities in the potential
energy surface for the solute molecule. These discontinuities inhibit
convergence of geometry optimizations, introduce serious artifacts in
vibrational frequency calculations, and make *ab initio* molecular
dynamics calculations virtually impossible.[[753]](../bib_references/bib.md#bib786)

In contrast, **Q-Chem**’s SwiG-PCMs afford potential energy surfaces that are
rigorously continuous and smooth. Unlike earlier attempts to obtain smooth
PCMs, the SwiG approach largely preserves the properties of the underlying
integral-equation solvent models, so that solvation energies and molecular
surface areas are hardly affected by the smoothing procedure.

Other solvent models available in **Q-Chem** include the “Langevin dipoles”
model;[[394]](../bib_references/bib.md#bib402)
 as well as the
SM8,[[912]](../bib_references/bib.md#bib942)
 SM12,[[910]](../bib_references/bib.md#bib946)
 and SMD models.[[909]](../bib_references/bib.md#bib943)

SM8 and SM12 are based upon the generalized Born method for electrostatics, augmented with
atomic surface tensions intended to capture nonelectrostatic effects
(cavitation, dispersion, exchange repulsion, and changes in solvent structure).
These models have been carefully parameterized to reproduce experimental free energies of solvation.[[281]](../bib_references/bib.md#bib286)

The SMD model, in which the “D” is for “density”,
combines IEF-PCM with similar nonelectrostatic corrections. Statistically speaking,
SMD is not any more or less accurate than other SM$x$ models,[[569]](../bib_references/bib.md#bib580)
 but has
the advantage of being based on rigorous electrostatics derived from the solute’s exact SCF density.
The SM12 and SMD models can each be used in arbitrary basis sets. The SM8 model
uses generalized Born electrostatics based on “CM4” charges,[[678]](../bib_references/bib.md#bib702)

which are themselves based on Löwdin atomic charges, and as such this model should only be used in the basis sets
for which it was parameterized: 6-31G*, 6-31+G*, or 6-31+G**. (Other basis sets, if requested will use the 6-31G* parameters
but this is not recommended.) The SM12 model also uses generalized Born electrostatics but substitutes CM4 charges for
Hirshfeld charges; the latter are more stable with respect to changes in basis set and therefore SM12 is available in arbitrary
basis sets. The trade-off is that an analytic gradient is available for SM8 but not SM12; see Table [11.2](#table:solvent_model_derivatives).
For SMD, both analytic first and second derivatives (frequencies) are available.

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">Model</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt" colspan="2"><span class="ltx_text ltx_font_bold">Cavity</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">Non-</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">Basis</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td ltx_align_center ltx_border_t">Construction</td>
<td class="ltx_td ltx_align_center ltx_border_t">Discretization</td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">Electrostatic</span></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">Sets</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">Terms?</span></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">Supported</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Kirkwood-Onsager</th>
<td class="ltx_td ltx_align_center ltx_border_t">spherical</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges</td>
<td class="ltx_td ltx_align_center ltx_border_t">no</td>
<td class="ltx_td ltx_align_center ltx_border_t">all</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">Langevin Dipoles</th>
<td class="ltx_td ltx_align_center ltx_border_t">atomic spheres</td>
<td class="ltx_td ltx_align_center ltx_border_t">dipoles in</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">no</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">(user-definable)</td>
<td class="ltx_td ltx_align_center">3-d space</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Poisson Equation</th>
<td class="ltx_td ltx_align_center ltx_border_t">atomic spheres</td>
<td class="ltx_td ltx_align_center ltx_border_t">grid in</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">no</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">Solver</th>
<td class="ltx_td ltx_align_center">(user-definable)</td>
<td class="ltx_td ltx_align_center">3-d space</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">C-PCM</th>
<td class="ltx_td ltx_align_center ltx_border_t">atomic spheres</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges or</td>
<td class="ltx_td ltx_align_center ltx_border_t">user-</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">(user-definable)</td>
<td class="ltx_td ltx_align_center">smooth Gaussians</td>
<td class="ltx_td ltx_align_center">specified</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">SS(V)PE/</th>
<td class="ltx_td ltx_align_center ltx_border_t">atomic spheres</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges or</td>
<td class="ltx_td ltx_align_center ltx_border_t">user-</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">IEF-PCM</th>
<td class="ltx_td ltx_align_center">(user-definable)</td>
<td class="ltx_td ltx_align_center">smooth Gaussians</td>
<td class="ltx_td ltx_align_center">specified</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">COSMO</th>
<td class="ltx_td ltx_align_center ltx_border_t">predefined</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">point charges</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">none</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">atomic spheres</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Isodensity SS(V)PE</th>
<td class="ltx_td ltx_align_center ltx_border_t">isodensity contour</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges</td>
<td class="ltx_td ltx_align_center ltx_border_t">none</td>
<td class="ltx_td ltx_align_center ltx_border_t">all</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">CMIRS</th>
<td class="ltx_td ltx_align_center ltx_border_t">isodensity contour</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges</td>
<td class="ltx_td ltx_align_center ltx_border_t">automatic</td>
<td class="ltx_td ltx_align_center ltx_border_t">all</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="3">SM8</th>
<td class="ltx_td ltx_align_center ltx_border_t">predefined</td>
<td class="ltx_td ltx_border_t"></td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="3">automatic</td>
<td class="ltx_td ltx_align_center ltx_border_t">6-31G*</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">atomic spheres</td>
<td class="ltx_td ltx_align_center">N/A${}^{a}$
</td>
<td class="ltx_td ltx_align_center">6-31+G*</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center">6-31+G**</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">SM12</th>
<td class="ltx_td ltx_align_center ltx_border_t">predefined</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">N/A${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">automatic</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">atomic spheres</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">SMD</th>
<td class="ltx_td ltx_align_center ltx_border_t">predefined</td>
<td class="ltx_td ltx_align_center ltx_border_t">point charges</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">automatic</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">all</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">atomic spheres</td>
<td class="ltx_td"></td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="5">
${}^{a}$<span class="ltx_text" style="font-size:80%;">Generalized Born electrostatic model; does not require cavity construction.</span>
</th>
</tr>
</tfoot>
</table>

Table 11.1: 
Summary of implicit solvation models available in **Q-Chem**,
indicating how the solute cavity is constructed and discretized, whether
nonelectrostatic terms are (or can be) included, and which basis sets are
available for use with each model.

Table [11.1](#table:solvent_models) summarizes the implicit solvent models that
are available in **Q-Chem**. Solvent models are invoked via the
SOLVENT_METHOD keyword, as shown below. Additional details about
each particular solvent model can be found in the sections that follow. In
general, these methods are available for any SCF level of electronic structure
theory, with the aforementioned caveat about basis sets for SM8.
Post-Hartree–Fock calculations (such as MP2 or EOM-CC) can be performed by first running an SCF + PCM
job, in which case the correlated wave function will employ MOs and
Hartree-Fock energy levels that are polarized by the solvent. This represents a
“zeroth-order” inclusion of the solvent effects at the correlated level of theory, but is perfectly
adequate for many applications as higher-order corrections are usually small.[[939]](../bib_references/bib.md#bib982)

Table [11.2](#table:solvent_model_derivatives) also summarizes the availability of analytical energy
gradients for implicit solvent models. (Finite-difference gradients and Hessians are requested automatically
for calculations where the requisite analytic derivatives are not available.)

!!! note "Note"
    The format for specifying implicit solvent models changed
    significantly starting in **Q-Chem** v. 4.2.1. This change was made in an
    attempt to simply and unify the input notation for a large number of different models.


<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" rowspan="3"><span class="ltx_text ltx_font_bold">Energy Derivatives</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt" colspan="9"><span class="ltx_text ltx_font_bold">Solvent Model</span></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">C-PCM</td>
<td class="ltx_td ltx_align_center ltx_border_t">SS(V)PE/</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">CMIRS</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">COSMO</td>
<td class="ltx_td ltx_align_center ltx_border_t" colspan="3">SM$x$
</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">PEqS</td>
<td class="ltx_td ltx_align_center ltx_border_t">Langevin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">IEF-PCM</td>
<td class="ltx_td ltx_align_center ltx_border_t">SM8</td>
<td class="ltx_td ltx_align_center ltx_border_t">SM12</td>
<td class="ltx_td ltx_align_center ltx_border_t">SMD</td>
<td class="ltx_td ltx_align_center">Dipoles</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">SCF energy gradient</th>
<td class="ltx_td ltx_align_center ltx_border_t">yes${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t">yes${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t">no</td>
<td class="ltx_td ltx_align_center ltx_border_t">yes</td>
<td class="ltx_td ltx_align_center ltx_border_t">yes</td>
<td class="ltx_td ltx_align_center ltx_border_t">no</td>
<td class="ltx_td ltx_align_center ltx_border_t">yes</td>
<td class="ltx_td ltx_align_center ltx_border_t">no</td>
<td class="ltx_td ltx_align_center ltx_border_t">yes</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">SCF energy Hessian</th>
<td class="ltx_td ltx_align_center">yes${}^{a}$
</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">yes${}^{b}$
</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">yes${}^{c}$
</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">no</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">CIS/TDDFT energy gradient</th>
<td class="ltx_td ltx_align_center">yes${}^{a}$
</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— unsupported —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">CIS/TDDFT energy Hessian</th>
<td class="ltx_td ltx_align_center">yes${}^{a}$
</td>
<td class="ltx_td ltx_align_center">no</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— unsupported —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">MP2 &amp; double-hybrid${}^{d}$
</th>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— unsupported —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb">Coupled cluster methods${}^{d}$
</th>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb" colspan="3">— unsupported —</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
</tr>
</tbody>
</table>

- ${}^{a}$Gradients available for vdW cavities and SAS cavity surfaces only.
- ${}^{b}$Hessians for COSMO with the outlying charge correction are not supported.
- ${}^{c}$Seminumerical Hessian, with a step size controllable via FDIFF_STEPSIZE.
- ${}^{d}$Gradients are not supported but single-point calculations can be performed using solvent-polarized MOs.

Table 11.2: 
Summary of analytic energy gradient and Hessian capabilities with implicit solvent models.

### `SOLVENT_METHOD`

> **Sets the preferred solvent method.**
>
> * **Type**: `STRING`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not use a solvation model.
>     * `KIRKWOOD`: Use the Kirkwood-Onsager model (Section 11.2.2 ).
>     * `PCM`: Use an apparent surface charge, polarizable continuum model (Section 11.2.3 ).
>     * `ISOSVP`: Use the isodensity implementation of the SS(V)PE model (Section 11.2.6 ).
>     * `COSMO`: Use COSMO (Section 11.2.8 ).
>     * `SM8`: Use version 8 of the Cramer-Truhlar SM $x$ model (Section 11.2.9.1 ).
>     * `SM12`: Use version 12 of the SM $x$ model (Section 11.2.9.2 ).
>     * `SMD`: Use SMD (Section 11.2.9.3 ).
>     * `CHEM_SOL`: Use the Langevin Dipoles model (Section 11.2.10 ).
>     * `PEQS`: Use the Poisson Equation Solver (Section 11.2.11 ).
> * **Recommendation**: Consult the literature ( e.g. , Ref. 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link ). PCM is a collective name for a family of models and additional input options may be required in this case, in order to fully specify the model; see Section 11.2.3 . Several versions of SM12 are available as well, as discussed in Section 11.2.9.2 .

Before going into detail about each of these models, a few potential points of
confusion warrant mention, with regards to nomenclature. First, “PCM” is used frequently (and sometimes ambiguously)
to a family of models that includes COSMO, C-PCM, SS(V)PE, and IEF-PCM. The latter two models are formally
equivalent at the level of integral equations,[[188]](../bib_references/bib.md#bib183)
 but exhibit some
some differences in their numerical implementation.[[756]](../bib_references/bib.md#bib789)

One or the other of these models can be selected by additional job control variables in a *$pcm* input
section, as described in Section [11.2.3](topic_pcm-em.md). COSMO is very similar to
C-PCM but includes a correction for that part of the solute’s electron density
that penetrates beyond the cavity (the so-called “outlying charge”),[[692]](../bib_references/bib.md#bib721)

although later work cast doubt on the theoretical justification for this and other *ad hoc*
charge renormalization procedures.[[244]](../bib_references/bib.md#bib244)

[The IEF-PCM and SS(V)PE methods already contain an *implicit* correction for outlying charge, as does the
C-PCM method that is derived as an approximation to these models,[[244]](../bib_references/bib.md#bib244)

although this was not recognized at the time that COSMO was formulated.
See Ref. [[569]](../bib_references/bib.md#bib580)
 for a historical discussion of these developments.]
In any case, COSMO is described in Section [11.2.8](subsec_COSMO-Klamt.md).

Two implementations of the SS(V)PE model are also available. The PCM
implementation (which is requested by setting SOLVENT_METHOD = PCM in
conjunction with appropriate job-control variables in the *$pcm* input section)
uses a solute cavity constructed from atom-centered spheres, in keeping with other PCMs.
On the other hand, setting SOLVENT_METHOD =
ISOSVP requests an SS(V)PE calculation in which the solute cavity is
defined by an isocontour of the solute’s own electron density.[[242]](../bib_references/bib.md#bib247)

This is an appealing, one-parameter cavity construction that avoid many of the problems with cusps
in “van der Waals” cavity surfaces that are constructed from atom-centered spheres, and the isodensity
implementation of SS(V)PE forms the basis of a physics-based continuum solvation model
called CMIRS that is described in
Section [11.2.7](example_CMIRS-water.md).[[1108]](../bib_references/bib.md#bib1155)

CMIRS is competitive in accuracy (for solvation free energies)
with the best-available SM$x$ solvation models,[[569]](../bib_references/bib.md#bib580)

despite using far fewer fitting parameters.
However, analytic energy gradients are not available for the isodensity cavity construction and therefore
not available for CMIRS, whereas these gradients are available when the cavity surface is constructed from atom-centered spheres.

Regarding the accuracy of these models for solvation free energies ($\Delta G_{298}$),
the SM$x$ models generally achieve
sub-kcal/mol accuracy for neutral molecules, based on
comparison to a large database of experimental values, although average errors
for ions are more like 4 kcal/mol.[[281]](../bib_references/bib.md#bib286)

(Note that the SM12 and SMD models generally do not improve too much upon SM8 in any statistical
sense,[[909]](../bib_references/bib.md#bib943)
 but do extend these models to arbitrary basis sets whereas
SM8 is limited to a few small basis sets. Furthermore, SMD includes both gradients and frequencies.

)
To achieve accuracy comparable to the SM$x$ models within the
PCM class of solvent models, nonelectrostatic terms must be added.[[569]](../bib_references/bib.md#bib580)

Among the various PCMs described above, the only one that constitutes a “black box” model for
solvation energies is CMIRS, which slightly outperforms the SM$x$ models in a statistical
sense,[[1527]](../bib_references/bib.md#bib1594)
 although it is only available for a few solvents.

The following sections provide more details regarding theory and job control
for the various implicit solvent models that are available in **Q-Chem**.
Ref. [[569]](../bib_references/bib.md#bib580)
 contains both formal comparisons amongst these
models as well as a side-by-side comparison of the accuracy of solvation free energies.
