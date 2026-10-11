---
title: "11.2.3 Polarizable Continuum Models"
---

## 11.2.3 Polarizable Continuum Models

(July 4, 2026)

The multipolar expansion model is based on exact formulas for the solvation energy of a point multipole
in a spherical cavity,[[948]](../bib_references/bib.md#bib988)
 which is a crude approximation except (or perhaps even)
for small molecules, and the Kirkwood-Onsager model has been largely superseded by the
more general class of “apparent surface charge” SCRF solvation models, typically known as
PCMs.[[1363]](../bib_references/bib.md#bib1425)
 These models improve upon the multipolar expansion method in two ways.
Most importantly, they provide a much more
realistic description of molecular shape, typically by constructing the
“solute cavity” (*i.e.*, the interface between the atomistic region and the
dielectric continuum) from a union of atom-centered spheres, an aspect of the
model that is discussed in Section [11.2.3.2](#subsubsec:pcm_cavity). In addition,
the exact electron density of the solute (rather than a multipole expansion) is
used to polarize the continuum. Electrostatic interactions between the solute
and the continuum manifest as an induced charge density on the cavity surface,
which is discretized into point charges for practical calculations. The
surface charges are determined based upon the solute’s electrostatic potential
at the cavity surface, hence the surface charges and the solute wave function
must be determined self-consistently.

## 11.2.3.1 Formal Theory and Discussion of Different Models

The PCM literature has a long history[[1363]](../bib_references/bib.md#bib1425)
 and there are several
different models in widespread use; connections between these models have not always been
appreciated.[[245]](../bib_references/bib.md#bib245)

Chipman[[245]](../bib_references/bib.md#bib245)
 has shown how various PCMs can be
formulated within a common theoretical framework; see
Ref. [[569]](../bib_references/bib.md#bib580)
 for a review. The PCM takes the form of a set of linear equations,

<a id="eq:Kq=Rv"></a>
$$
\mathbf{Kq}=\mathbf{Rv}\;, \tag{11.2}
$$

in which the induced charges $q_{i}$ at the cavity surface discretization points
[organized into a vector $\mathbf{q}$ in Eq. ([11.2](#eq:Kq=Rv))] are computed
from the values $v_{i}$ of the solute’s electrostatic potential at those same
discretization points. The form of the matrices $\mathbf{K}$ and $\mathbf{R}$
depends upon the particular PCM in question. These matrices are given in
Table [11.3](#table:K-matrix) for the PCMs that are available in **Q-Chem**.

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">Model</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">Literature</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">Matrix</span> $\mathbf{K}$
</td>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">Matrix</span> $\mathbf{R}$
</td>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">Scalar</span> $f_{\varepsilon}$
</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row"><span class="ltx_text ltx_font_bold">Refs.</span></th>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">COSMO${}^{a}$
</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_t"><cite class="ltx_cite ltx_citemacro">
</cite>
</th>
<td class="ltx_td ltx_align_center ltx_border_t">$\mathbf{S}$</td>
<td class="ltx_td ltx_align_center ltx_border_t">$-f_{\varepsilon}\mathbf{1}$</td>
<td class="ltx_td ltx_align_center ltx_border_t">$(\varepsilon-1)/(\varepsilon+1/2)$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">C-PCM</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[1375]](../bib_references/bib.md#bib1436)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\mathbf{1}$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/\varepsilon$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">IEF-PCM</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[245]](../bib_references/bib.md#bib245)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}-(f_{\varepsilon}/2\pi)\mathbf{DAS}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\left(\mathbf{1}-\frac{1}{2\pi}\mathbf{DA}\right)$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/(\varepsilon+1)$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">SS(V)PE</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[245]](../bib_references/bib.md#bib245)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}-(f_{\varepsilon}/4\pi)\bigl{(}\mathbf{DAS}+\mathbf{SAD}^{\dagger}\bigr{)}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\left(\mathbf{1}-\frac{1}{2\pi}\mathbf{DA}\right)$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/(\varepsilon+1)$</td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="5">
${}^{a}$<span class="ltx_text" style="font-size:80%;">Also includes a charge renormalization correction; see Section <a class="ltx_ref" href="subsec_COSMO-Klamt.html" title="11.2.8 COSMO ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.8</span></a>.</span>
</th>
</tr>
</tfoot>
</table>

Table 11.3: 
Definition of the matrices in Eq. ([11.2](#eq:Kq=Rv)) for the
various PCMs that are available in **Q-Chem**. The matrix $\mathbf{S}$ consists
of Coulomb interactions between the cavity charges and $\mathbf{D}$ is the
discretized version of the matrix that generates the outward-pointing normal electric field vector. (See
Refs. [[246]](../bib_references/bib.md#bib246) for
detailed definitions.) The matrix $\mathbf{A}$ is diagonal and contains the
surface areas of the cavity discretization elements, and $\mathbf{1}$ is a unit
matrix.

The oldest PCM is the so-called D-PCM model of Tomasi and
coworkers,[[946]](../bib_references/bib.md#bib986)
 but unlike the models listed in
Table [11.3](#table:K-matrix), D-PCM requires explicit evaluation of the electric
field normal to the cavity surface. This is undesirable, as evaluation of the
electric field is both more expensive and more prone to numerical problems as
compared to evaluation of the electrostatic potential. Moreover, the
dependence on the electric field can be formally eliminated at the level of the
integral equation whose discretized form is given in
Eq. ([11.2](#eq:Kq=Rv)).[[245]](../bib_references/bib.md#bib245)
 As such, D-PCM is essentially
obsolete, and the PCMs available in **Q-Chem** require only the evaluation of the
electrostatic potential, not the electric field.

The simplest PCM that continues to enjoy widespread use is the conductor-like model,
C-PCM.[[79]](../bib_references/bib.md#bib61)
 Originally derived by Klamt and Schüürmann

based on arguments invoking the conductor limit ($\varepsilon\rightarrow\infty$), this model can also be
derived as an approximation to more formally correct
models.[[244]](../bib_references/bib.md#bib244)

Over the years, the dielectric-dependent factor

<a id="eq:f_epsilon"></a>
$$
f_{\varepsilon}=\frac{\varepsilon-1}{\varepsilon+x} \tag{11.3}
$$

that appears in this model (see Table [11.3](#table:K-matrix)) has been used with different values of $x$.
The value $x=0$ is typically used in C-PCM calculations and $x=1/2$ in COSMO calculations, although
Klamt and co-workers later suggested using $x=1/2$ for neutral solutes and $x=0$ for ions.[[694]](../bib_references/bib.md#bib726)

The specific choice of $f_{\varepsilon}$ is controllable via the *$pcm* input section that is described in
Section [11.2.4](subsec_PCM_job_control.md).

Whereas from Table [11.3](#table:K-matrix) the C-PCM and COSMO methods would appear to be the same up
to a minor rescaling of the surface charge (*i.e.*, up to the precise choice of $f_{\varepsilon}$), historically the
term “COSMO" has been used by Klamt to mean a particular “dual-cavity” implementation of this model that
makes it different from other PCMs.[[569]](../bib_references/bib.md#bib580)
 This construction is equivalent to the
“outlying charge correction” that is discussed in Section [11.2.8](subsec_COSMO-Klamt.md), and was intended
to account for the effects of the tail of the solute’s charge density that penetrates beyond the
cavity surface.[[692]](../bib_references/bib.md#bib721)

Subsequent work cast considerable doubt on the theoretical justification for this
correction, since the C-PCM/COSMO *ansatz* was shown to include already an *implicit*
correction for outlying charge.[[244]](../bib_references/bib.md#bib244)

Further discussion of this construction, and of COSMO, is deferred to Section [11.2.8](subsec_COSMO-Klamt.md),

As compared to C-PCM, a more sophisticated treatment of continuum electrostatic
interactions is afforded by the “surface and simulation of volume polarization
for electrostatics” [SS(V)PE] approach.[[245]](../bib_references/bib.md#bib245)
 Formally speaking,
this model provides an exact treatment of the *surface polarization*
(*i.e.*, the surface charge induced by the solute charge that is contained within
the solute cavity, which induces a surface polarization owing to the
discontinuous change in dielectric constant across the cavity boundary) but
also an approximate treatment of the *volume polarization* (arising from
the aforementioned outlying charge). The “SS(V)PE” terminology is Chipman’s
notation,[[245]](../bib_references/bib.md#bib245)
 but this model is formally equivalent, at the
level of integral equations, to the “integral equation formalism” (IEF-PCM)
that was developed originally by Cancès *et al.*.[[187]](../bib_references/bib.md#bib181)

Some difference do arise when the integral equations are discretized to form
finite-dimensional matrix equations,[[756]](../bib_references/bib.md#bib789)
 and it should be noted
from Table [11.3](#table:K-matrix) that SS(V)PE uses a symmetrized form of the
$\mathbf{K}$ matrix as compared to IEF-PCM. The *asymmetric* IEF-PCM is
the recommended approach,[[756]](../bib_references/bib.md#bib789)
 although only the symmetrized
version is available in the isodensity implementation of SS(V)PE that is
discussed in Section [11.2.6](subsec_SS_V_PE.md). That said, differences between symmetry and asymmetric
versions are only important in the case of van der Waals cavity surfaces; they are insignificant for the
isodensity cavity construction.[[569]](../bib_references/bib.md#bib580)

As with the obsolete D-PCM
approach, the original version of IEF-PCM explicitly required evaluation of the
normal electric field at the cavity surface, but it was later shown that this
dependence could be eliminated to afford the version described in
Table [11.3](#table:K-matrix).[[245]](../bib_references/bib.md#bib245)
 This version
requires only the electrostatic potential, and is thus preferred, and it is
this version that we designate as IEF-PCM. The C-PCM model becomes equivalent
to SS(V)PE in the limit
$\varepsilon\rightarrow\infty$,[[245]](../bib_references/bib.md#bib245)
 which means that
C-PCM must somehow include an *implicit* correction for volume
polarization, even if this was not by design.[[692]](../bib_references/bib.md#bib721)
 For
$\varepsilon\gtrsim 50$, numerical calculations reveal that there is
essentially no difference between SS(V)PE and C-PCM results.[[756]](../bib_references/bib.md#bib789)

Since C-PCM is less computationally involved as compared to SS(V)PE, it is the
PCM of choice in high-dielectric solvents. The computational savings relative
to SS(V)PE may be particularly significant for large QM/MM/PCM jobs.

For a more detailed discussion of the history of these models, see the lengthy
and comprehensive review by Tomasi *et al.*.[[1363]](../bib_references/bib.md#bib1425)
 For a
briefer discussion of the connections between these models, see
Refs. [[246]](../bib_references/bib.md#bib246).

## 11.2.3.2 Cavity Construction and Discretization

![Figure 11.1: Illustration of various solute cavity surface definitions for
PCMs. 751 Lange A. W. et al. Mol. Phys. (2020) , 118 , pp. e1644384 . Link The union of atomic van der Waals spheres
(shown in gray) defines the van der Waals (vdW) surface, in black. Note that
actual vdW radii from the literature are sometimes scaled in constructing the
vdW surface. If a probe sphere (representing the assumed size of a solvent
molecule) is rolled over the van der Waals surface, then its center point
traces out the solvent accessible surface (SAS), shown in green; the SAS is
equivalent to a vdW surface where the atomic radii are increases by the radius
of the probe sphere. Finally, one can use the probe sphere to smooth out the
sharp crevasses in the vdW surface using the re-entrant surface elements shown
in red, resulting in the solvent-excluded surface (SES).](../assets/x2.png)

*Figure 11.1: Illustration of various solute cavity surface definitions for
PCMs. 751 Lange A. W. et al. Mol. Phys. (2020) , 118 , pp. e1644384 . Link The union of atomic van der Waals spheres
(shown in gray) defines the van der Waals (vdW) surface, in black. Note that
actual vdW radii from the literature are sometimes scaled in constructing the
vdW surface. If a probe sphere (representing the assumed size of a solvent
molecule) is rolled over the van der Waals surface, then its center point
traces out the solvent accessible surface (SAS), shown in green; the SAS is
equivalent to a vdW surface where the atomic radii are increases by the radius
of the probe sphere. Finally, one can use the probe sphere to smooth out the
sharp crevasses in the vdW surface using the re-entrant surface elements shown
in red, resulting in the solvent-excluded surface (SES).*

Construction of the cavity surface is a crucial aspect of PCMs, as computed
properties are quite sensitive to the details of the cavity construction. Most
cavity constructions are based on a union of atom-centered spheres (see
Fig. [11.1](#fig:PCM_surfs)), but there are yet several different constructions
whose nomenclature is occasionally confused in the literature. Simplest and
most common is the van der Waals (vdW) surface consisting of a union of
atom-centered spheres. The radius for the sphere centered on atom $A$ can be written in the form

<a id="eq:PCM_atomic_radii"></a>
$$
R_{A}=\alpha_{\text{vdW}}R_{\text{vdW},A}+R_{\text{probe}} \tag{11.4}
$$

where $R_{\text{vdW},A}$ is the vdW radius for atom $A$, taken for example from the set of vdW
radii published by Bondi.[[146]](../bib_references/bib.md#bib136)
 Traditionally, the vdW radii
$R_{\text{vdW},A}$ that are extracted from crystallographic data are scaled by a factor
$\alpha_{\text{vdW}}=1.1$–1.2.[[145]](../bib_references/bib.md#bib135)

This 20% augmentation is intended to mimic the fact that solvent molecules cannot
approach all the way to the vdW radius of the solute atoms, though it’s not
altogether clear that the same value ought to be optimal in all cases. (The scaling factor defaults to
$\alpha_{\text{vdW}}=1.2$ but can be modified by the user.)

An alternative to scaling
the atomic radii is to add a certain fixed increment $R_{\text{probe}}$ to each, representing the
approximate size of a solvent molecule, and leading
to what is known as the *solvent accessible surface* (SAS).
The choice $R_{\text{probe}}=1.4$ Å is common for water and represents the approximate
physical size of a water molecule, although values in the range $R_{\text{probe}}=0.2$–0.5 Å often
afford better solvation energies.[[569]](../bib_references/bib.md#bib580)

In any case, if a nonzero value of $R_{\text{probe}}$ is used, then the scaling factor in
Eq. ([11.4](#eq:PCM_atomic_radii)) should be set to $\alpha_{\text{vdW}}=1.0$, since these two parameters
are intended to model the same effect, namely, that a solvent molecule’s finite size prevents it from approaching
all the way to the vdW radii of the solute.

Note from Fig. [11.1](#fig:PCM_surfs) that both the vdW surface and the SAS possess cusps
where the atomic spheres intersect, although these become less pronounced as
the atomic radii are scaled or augmented. These cusps are eliminated in what
is known as the *solvent-accessible surface* (SES), sometimes called the
Connolly surface or the “molecular surface". The SES uses the surface of the
probe sphere at points where it is simultaneously tangent to two or more atomic
spheres to define elements of a “re-entrant surface” that smoothly connects
the atomic (or “contact”) surface.[[751]](../bib_references/bib.md#bib790)

Having chosen a model for the cavity surface, this surface is discretized using
atom-centered Lebedev grids[[777]](../bib_references/bib.md#bib809)
 of
the same sort that are used to perform the numerical integrations in DFT.
(Discretization of the re-entrant facets of the SES is somewhat more
complicated but similar in spirit.[[751]](../bib_references/bib.md#bib790)
) Surface charges $q_{i}$
are located at these grid points and the Lebedev quadrature weights can be used
to define the surface area associated with each discretization point.[[753]](../bib_references/bib.md#bib786)

A long-standing (though not well-publicized) problem with the aforementioned
discretization procedure is that it fails to afford continuous potential
energy surfaces as the solute atoms are displaced, because certain surface grid
points may emerge from, or disappear within, the solute cavity, as the atomic
spheres that define the cavity are moved. This undesirable behavior can
inhibit convergence of geometry optimizations and, in certain cases, lead to
very large errors in vibrational frequency calculations.[[753]](../bib_references/bib.md#bib786)
 It
is also a fundamental hindrance to molecular dynamics
calculations.[[754]](../bib_references/bib.md#bib787)
 Building upon earlier work by York and
Karplus,[[1525]](../bib_references/bib.md#bib1589)
 Lange and
Herbert[[753]](../bib_references/bib.md#bib786)
 developed a general scheme
for implementing apparent surface charge PCMs in a manner that affords smooth
potential energy surfaces, even for *ab initio* molecular dynamics
simulations involving bond breaking.[[754]](../bib_references/bib.md#bib787)
Notably, this approach is faithful to the properties of the underlying integral
equation theory on which the PCMs are based, in the sense that the smoothing
procedure does not significantly perturb solvation energies or cavity surface
areas.[[753]](../bib_references/bib.md#bib786)
 The smooth discretization procedure
combines a switching function with Gaussian blurring of the cavity surface
charge density, and is thus known as the “Switching/Gaussian” (SwiG)
implementation of the PCM.

Both single-point energies and analytic energy gradients are available for SwiG-PCMs,
when the solute is described using molecular mechanics or an SCF
(Hartree-Fock or DFT) electronic structure model, except that for the SES
cavity model only single-point energies are available. Analytic Hessians are
available for the C-PCM model only. (As usual, vibrational frequencies for
other models will be computed, if requested, by finite difference of analytic
energy gradients.) Single-point energy calculations using correlated wave
functions can be performed in conjunction with these solvent models, in which
case the correlated wave function calculation will use Hartree-Fock molecular
orbitals that are polarized in the presence of the continuum dielectric solvent
(*i.e.*, there is no post-Hartree–Fock PCM correction). This represents a “zeroth-order”
inclusion of solvent effects that captures the leading-order effect of continuum solvation on
molecular properties.[[569]](../bib_references/bib.md#bib580)

Given the crudeness of the model itself, more consistent inclusion of
post-Hartree–Fock solvation effects is not expected to be important.[[569]](../bib_references/bib.md#bib580)

Researchers who use these PCMs are asked to cite
Refs. [[754]](../bib_references/bib.md#bib787)
 and [[756]](../bib_references/bib.md#bib789)
, which provide the details of
**Q-Chem**’s implementation; Ref. [[751]](../bib_references/bib.md#bib790)
 if the SES is used, and
Ref. [[561]](../bib_references/bib.md#bib576) if the conjugate-gradient solver or other linear-scaling options are used.
We point the reader in particular to Refs. [[754]](../bib_references/bib.md#bib787)
 and [[1530]](../bib_references/bib.md#bib1593)
, which
provides an assessment of the discretization errors that can be anticipated
using various PCMs and Lebedev grids; default grid values in **Q-Chem** were
established based on these tests. When publishing results based on PCM
calculations, it is essential to specify both the precise model that is used
(see Table [11.3](#table:K-matrix)) as well as how the cavity was constructed, and this should be done
without resorting to software-specific keywords, the use of which has significantly muddled the
literature on continuum electrostatics.[[282]](../bib_references/bib.md#bib287)

As an example of good practice,
the default cavity construction in **Q-Chem** is a vdW cavity using Bondi atomic radii,[[146]](../bib_references/bib.md#bib136)

except that for hydrogen we use the modified radius of 1.1 Å,
following a reassessment that judged Bondi’s original value of 1.2 Å for hydrogen to be too
large.[[1186]](../bib_references/bib.md#bib1240)
 Each of these radii $R_{\text{vdW},A}$ in Eq. ([11.4](#eq:PCM_atomic_radii)) is then
scaled by a factor $\alpha_{\text{vdW}}=1.2$ for use in cavity construction.
Radii for main-group elements that were not provided by Bondi are
taken from Ref. [[889]](../bib_references/bib.md#bib923)
. Absent details such as these,
PCM calculations will be difficult to reproduce in other electronic structure programs.

## 11.2.3.3 Nonequilibrium Solvation for Vertical Excitation, Ionization and Emission

In vertical excitation or ionization, the solute undergoes a sudden change in
its charge distribution. Various microscopic motions of the solvent have
characteristic times to reach certain polarization response, and fast part of
the solvent response (electrons) can follow such a dynamic process while the
remaining degrees of freedom (nuclei) remain unchanged as in the initial state.
Such splitting of the solvent response gives rise to nonequilibrium solvation.
In the literature, two different approaches have been developed for describing
nonequilibrium solvent effects: the linear response (LR)
approach[[183]](../bib_references/bib.md#bib178)
 and the state-specific (SS)
approach.[[1365]](../bib_references/bib.md#bib1423)
 Both are
implemented in **Q-Chem**,[[1530]](../bib_references/bib.md#bib1593)
, at the SCF level for vertical
ionization and at the corresponding level (CIS and TDDFT, see Section [7.3.7](../ch07_excited/subsec_tddft-cPCM.md), or ADC, see
Section [7.10.11](../ch07_excited/topic_abs-adc.md)) for vertical excitation. A brief introduction to
these methods is given below, and users of the nonequilibrium PCM features are
asked to cite Refs. [[1530]](../bib_references/bib.md#bib1593)
 and [[940]](../bib_references/bib.md#bib979)
.
State-specific solvent-field equilibration for long-lived excited states to
compute *e.g.* emission energies is implemented for the ADC-suite of methods as
described in Section [7.10.11](../ch07_excited/topic_abs-adc.md) and for TDDFT as described in
Section [7.3.7.2](../ch07_excited/subsec_tddft-cPCM.md#subsubsec:tddft-PCM-iterSS). Users of this equilibrium-solvation
PCM please cite and be referred to Ref. [[939]](../bib_references/bib.md#bib982)
.

The LR approach considers the solvation effects as a coupling between a pair of
transitions, one for solute and the other for solvent. The transition
frequencies when the interaction between the solute and solvent is turned on
may be determined by considering such an interaction as a perturbation. In the
framework of TDDFT, the interaction between solute and solvent is given by[[599]](../bib_references/bib.md#bib622)

<a id="eq:LR-term"></a>
$$
\begin{split}\displaystyle\omega^{\prime}=&\displaystyle\int d\mathbf{r}\int d\mathbf{r}^{\prime}\int d\mathbf{r}^{\prime\prime}\int d\mathbf{r}^{\prime\prime\prime}\rho^{\ast}_{\text{tr}}(\mathbf{r})\left(\frac{1}{|\mathbf{r}-\mathbf{r}^{\prime}|}+g_{\mathrm{XC}}(\mathbf{r},\mathbf{r}^{\prime})\right)\\
&\displaystyle\times\chi^{*}(\mathbf{r}^{\prime},\mathbf{r}^{\prime\prime},\omega)\left(\frac{1}{|\mathbf{r}^{\prime\prime}-\mathbf{r}^{\prime\prime\prime}|}+g_{\mathrm{XC}}(\mathbf{r}^{\prime\prime},\mathbf{r}^{\prime\prime\prime})\right)\rho_{\text{tr}}(\mathbf{r}^{\prime\prime\prime})\;,\end{split} \tag{11.5}
$$

where $\chi$ is the charge density response function of the solvent and
$\rho_{\text{tr}}(\mathbf{r})$ is the solute’s transition density. This term accounts
for a dynamical correction to the transition energy so that it is related to
the response of the solvent to the charge density of the solute oscillating at
the solute transition frequency ($\omega$).
Within a PCM, only classical Coulomb interactions are taken into account, and
Eq. ([11.5](#eq:LR-term)) becomes

<a id="Ch11.E6"></a>
$$
\begin{split}\displaystyle\omega^{\prime}_{\mathrm{PCM}}=&\displaystyle\int d\mathbf{r}\int d\mathbf{s}\ \frac{\rho^{\ast}_{\text{tr}}(\mathbf{r})}{|\mathbf{r}-\mathbf{s}|}\int d\mathbf{s}^{\prime}\int d\mathbf{r}^{\prime}\,\mathcal{Q}(\mathbf{s},\mathbf{s}^{\prime},\varepsilon)\frac{\rho_{\text{tr}}(\mathbf{r}^{\prime})}{|\mathbf{s}^{\prime}-\mathbf{r}^{\prime}|}\;,\end{split} \tag{11.6}
$$

where $\mathcal{Q}$ is PCM solvent response operator for a generic dielectric
constant, $\varepsilon$. The integral of $\mathcal{Q}$ and the potential of the
density $\rho_{\text{tr}}(\mathbf{r})$ gives the surface charge density for the solvent polarization.

The state-specific approach takes into account the capability of a part of
the solvent degrees of freedom to respond instantaneously to changes in the
solute wave function upon excitation. Such an effect is not accounted for in
the LR approach. In SS, a generic solvated-solute excited state $\Psi_{i}$ is
obtained as a solution of a nonlinear Schrödinger equation

<a id="eq:SS-sdeq"></a>
$$
\left(\hat{H}^{\mathrm{vac}}+\hat{V}^{\mathrm{slow}}_{0}+\hat{V}^{\mathrm{fast}}_{i}\right)|\Psi_{i}\rangle=E^{\mathrm{SS}}_{i}|\Psi_{i}\rangle \tag{11.7}
$$

that depends upon the solute’s charge distribution. Here $\hat{H}^{\mathrm{vac}}$ is
the usual Hamiltonian for the solute in vacuum and the reaction field operator
$\hat{V}_{i}$ generates the electrostatic potential of the apparent surface
charge density (Section [11.2.3.1](#subsubsec:PCM-theory)), corresponding to
slow and fast polarization response.
The solute is polarized self-consistently with respect to the solvent’s
reaction field. In case of vertical ionization rather than excitation, both the
ionized and non-ionized states can be treated within a ground-state formalism.
For vertical excitations, self-consistent SS models have been developed for
various excited-state methods,[[611]](../bib_references/bib.md#bib634)
 and are
implemented for both CIS and TDDFT.

In a linear dielectric medium, the solvent polarization is governed by the
electric susceptibility, $\chi=[\varepsilon(\omega)-1]/4\pi$, where
$\varepsilon(\omega)$ is the frequency-dependent permittivity.
In case of very fast vertical transitions, the dielectric response is ruled by
the optical dielectric constant, $\varepsilon_{\text{opt}}=n^{2}$, where $n$ is
the solvent’s index of refraction. In both LR and SS, the fast part of the
solvent’s degrees of freedom is in equilibrium with the solute density change.
Within PCM, the fast solvent polarization charges for the SS excited state $i$
can be obtained by solving the following equation:[[271]](../bib_references/bib.md#bib273)

<a id="eq:Kq=Rv-fast"></a>
$$
\mathbf{K}_{\varepsilon_{\mathrm{opt}}}\mathbf{q}^{\mathrm{fast,SS}}_{i}=\mathbf{R}_{\varepsilon_{\mathrm{opt}}}\left[\mathbf{v}_{i}+\mathbf{v}(\mathbf{q}^{\mathrm{slow}}_{0})\right]\;. \tag{11.8}
$$

Here $\mathbf{q}^{\mathrm{fast,SS}}$ is the discretized fast surface charge. The
dielectric constants in the matrices $\mathbf{K}$ and $\mathbf{R}$
(Section [11.2.3.1](#subsubsec:PCM-theory)) are replaced with the optical dielectric
constant, and $\mathbf{v}_{i}$ is the potential of the solute’s excited state density,
$\rho_{i}$. The quantity $\mathbf{v}(\mathbf{q}^{\mathrm{slow}}_{0})$ is the potential of the
slow part of the apparent surface charges in the ground state, which
are given by

<a id="slow_q"></a>
$$
\mathbf{q}^{\mathrm{slow}}_{0}=\left(\frac{\varepsilon-\varepsilon_{\mathrm{opt}}}{\varepsilon-1}\right)\mathbf{q}_{0}\;. \tag{11.9}
$$

For LR-PCM, the solvent polarization is subjected to the first-order changes to
the electron density (TDDFT linear density response), and thus
Eq. ([11.8](#eq:Kq=Rv-fast)) becomes

<a id="Ch11.E10"></a>
$$
\mathbf{K}_{\varepsilon_{\mathrm{opt}}}\mathbf{q}^{\mathrm{fast,LR}}_{i}=\mathbf{R}_{\varepsilon_{\mathrm{opt}}}\mathbf{v}(\rho^{\mathrm{tr}}_{i})\;. \tag{11.10}
$$

The LR approach for CIS/TDDFT excitations and the self-consistent SS
method (using the ground-state SCF) for vertical ionizations are available in
**Q-Chem**. The self-consistent SS method is also available for vertical excitations,
but can be problematic for (near-) degeneracies between excited states,
such as in the vicinity of a conical intersection.
The fundamental problem in the SS approach is that each wave
function $\Psi_{i}$ is an eigenfunction of a *different* Hamiltonian, since
Eq. ([11.7](#eq:SS-sdeq)) depend upon the specific state of interest. To avoid the
ordering and the non-orthogonality problems, we compute the vertical
excitation energy using a first-order, perturbative approximation to the SS
approach,[[182]](../bib_references/bib.md#bib179)
 in what we have termed the “ptSS”
method.[[940]](../bib_references/bib.md#bib979)
 The zeroth-order excited-state wave function can be
calculated using various excited-state methods (currently available for CIS and
TDDFT in **Q-Chem**) with solvent-relaxed molecular orbitals obtained from a
ground-state PCM calculation. As mentioned previously, LR and SS describe
different solvent relaxation features in nonequilibrium solvation. In the
perturbation scheme, we can calculate the LR contribution using the
zeroth-order transition density, in what we have called the “ptLR” approach.
The combination of ptSS and ptLR yields quantitatively good solvatochromatic
shifts in combination with TDDFT but not with the correlated variants of ADC,
for which the pure ptSS approach was shown to be superior.[[1530]](../bib_references/bib.md#bib1593)

The LR and SS approaches can also be used in the study of photon emission
processes.[[612]](../bib_references/bib.md#bib635)
 An emission process can be treated as a vertical
excitation at a stationary point on the excited-state potential surface. The
basic requirement therefore is to prepare the solvent-relaxed geometry for the
excited-state of interest. TDDFT/LR-C-PCM analytic gradients and Hessian are available.

Section [7.3.8](../ch07_excited/subsec_tddft-hessian.md) for computational details regarding
excited-state geometry optimization with PCM. An emission process is slightly
more complicated than the absorption case. Two scenarios are discussed in
literature, depending on the lifetime of an excited state in question. In the limiting case
of ultra-fast excited state decay, when only fast solvent degrees of freedom are
expected to be equilibrated with the excited-state density. In this limit, the
emission energy can be computed exactly in the same way as the vertical
excitation energy. In this case, excited state geometry optimization should be
performed in the nonequilibrium limit.
The other limit is that of long-lived excited state, *e.g.*, strongly
fluorescent species and phosphorescence. In the long-lived case, excited state
geometry optimization should be performed with the solvent equilibrium limit.
Thus, the excited state should be computed using an equilibrium LR or SS
approach, and the ground state is calculated using nonequilibrium
self-consistent SS approach. The latter approach is implemented for the
ADC-based methods as described in Section [7.10.11](../ch07_excited/topic_abs-adc.md) and
TDDFT as described in Section [7.3.7.2](../ch07_excited/subsec_tddft-cPCM.md#subsubsec:tddft-PCM-iterSS).

## 11.2.3.4 Absorption and Emission Spectra Based on the Constrained Equilibrium Principle

For ultrafast processes in solution, such as electron transfer, photo-absorption/emission and photo-ionization,
a continuum model should combine a proper nonequilibrium solvation theory to account for nonequilibrium solute–solvent interactions.
In the traditional treatments, the nonequilibrium electrostatic solvation free energy was derived from the so-called reversible electric
work integration along the path linking the initial equilibrium state (eq) and the intermediate nonequilibrium state (neq),
*i.e.*,[[901]](../bib_references/bib.md#bib935)

<a id="Ch11.E11"></a>
$$
[\rho=0,\Phi=0]\xrightarrow[]{\varepsilon}[\rho_{1},\Phi^{\mathrm{eq}}_{1}]\xrightarrow[]{\varepsilon_{\mathrm{opt}}}[\rho_{2},\Phi^{\mathrm{neq}}_{2}] \tag{11.11}
$$

where $\Phi$ denotes the total electric potential including both the potential $\psi$ due to the solute charge $\rho$ in vacuum and polarization potential $\varphi$ due to the medium.
In order to deal with electron absorption and emission spectra in solution, the numerical expression of nonequilibrium solvation free energy which was established by intuitively collecting a series of energy terms from the interactions of solute charges and polarized charges, has been implemented using TDDFT with PCM model.[[271]](../bib_references/bib.md#bib273)

It is easy to verify this numerical form can be achieved through the discretization of analytical expression of nonequilibrium solvation energy by traditional treatments.[[821]](../bib_references/bib.md#bib852)

However, there exist a number of doubts on the overestimation of the solvent reorganization energy in ultrafast processes by this reversible electric work method.[[132]](../bib_references/bib.md#bib122)

It becomes clear now that there is no possibility to find a reversible pathway between the initial equilibrium state and the intermediate nonequilibrium state. Thus, the integrated electric work can not equal to the change of electrostatic free energy.[[821]](../bib_references/bib.md#bib852)

Xiangyuan Li *et al.*[[1495]](../bib_references/bib.md#bib1563)
 established the new theory for nonequilibrium solvation by employing
the constrained equilibrium principle,

 using the following pathway:

<a id="Ch11.E12"></a>
$$
[\rho_{1},\varphi^{\mathrm{eq}}_{1}]\xrightarrow[]{\mathrm{fast}}[\rho_{2},\varphi^{\mathrm{neq}}_{2}]\xrightarrow[]{-\lambda_{\mathrm{s}}}[\rho_{2},\varphi^{\mathrm{eq}}_{2}]\xrightarrow[]{+\rho_{\mathrm{ex}},\mathrm{quasistatic}}C[\rho_{2}+\rho_{\mathrm{ex}},\varphi^{\mathrm{neq}}_{2}] \tag{11.12}
$$

where C stands for the constrained equilibrium state which is constructed and mapped to the true nonequilibrium state by introducing the proper external charge $\rho_{\mathrm{ex}}$ which is used to equilibrate the “residual” polarization potential, $\varphi^{{}^{\prime}}=\varphi^{\mathrm{neq}}_{2}-\varphi^{\mathrm{eq}}_{2}$. In this way the solvent reorganization energy can be derived as

<a id="eq:lamuda_re"></a>
$$
\lambda_{\mathrm{s}}=-\frac{1}{2}\int_{V}\rho_{\text{ex}}\;\varphi^{\prime}\;dV \tag{11.13}
$$

Then the nonequilibrium solvation free energy is simply given by

<a id="eq:neq_sol"></a>
$$
F^{\mathrm{neq}}_{2}=\frac{1}{2}\int_{V}\rho_{2}\;\varphi^{\mathrm{eq}}_{2}\;dV+\lambda_{\mathrm{s}} \tag{11.14}
$$

For more detailed descriptions of the gain of the external (constraining) charge $\rho_{\mathrm{ex}}$, or the equivalent constraining external electric field $\mathbf{E}_{\mathrm{ex}}$, please refer to the review.[[821]](../bib_references/bib.md#bib852)

Within the framework of continuum model, the discretization and numerical solution of Eq. ([11.14](#eq:neq_sol)) is expressed as[[130]](../bib_references/bib.md#bib118)

<a id="Ch11.E15"></a>
$$
F^{\mathrm{neq}}_{i}=\sum_{m}V_{i,m}Q^{\mathrm{neq}}_{i,m}-\frac{1}{2}\sum_{m}Q^{\mathrm{neq}}_{i,m}D(\varepsilon)Q^{\mathrm{neq}}_{i,m} \tag{11.15}
$$

where the subscript $i$ denotes the ground ($i$ = 1) or excited ($i$ = 2) electronic state.
The value $V_{i,m}$ refers to the solute electrostatic potential at the *m*th tesserae.
$Q^{\mathrm{neq}}_{i,m}$ is the apparent charge for the nonequilibrium state. The quantity
$D(\varepsilon)$ is the square matrix arising in PCMs such as C-PCM and IEF-PCM (see Section [11.2.3.1](#subsubsec:PCM-theory)).

The vertical excitation energy for absorption is defined as

<a id="eq:hv_ab"></a>
$$
hv_{\mathrm{ab}}=G^{\mathrm{neq}}_{2}-G^{\mathrm{eq}}_{1} \tag{11.16}
$$

where $G$ stands for total free energy of the solute in solution,

<a id="Ch11.E17"></a>
$$
G^{\mathrm{eq}}_{1}=E_{1}+F^{\mathrm{eq}}_{1}=E_{1}+\frac{1}{2}\sum_{m}V_{1,m}Q^{\mathrm{eq}}_{1,m}\; \tag{11.17}
$$

The quantity $G^{\mathrm{eq}}_{1}$ is calculated by the SCRF method based on equilibrium ground-state reaction field and $E_{1}$
means the ground-state electronic energy of the solute.
Based on the equilibrium ground-state reaction field, with a self-consistent state-specific method in the framework of TDDFT,
$G^{\mathrm{neq}}_{2}$ is given by[[130]](../bib_references/bib.md#bib118)

<a id="eq:G2_neq"></a>
$$
G^{\mathrm{neq}}_{2}=E_{1}+\omega_{\mathrm{ab}}+\sum_{m}V_{1,m}Q^{\mathrm{eq}}_{1,m}+\sum_{m}V_{2,m}(Q^{\mathrm{neq}}_{2,m}-Q^{\mathrm{eq}}_{1,m})-\frac{1}{2}\sum_{m}Q^{\mathrm{neq}}_{2,m}D(\varepsilon)Q^{\mathrm{neq}}_{2,m} \tag{11.18}
$$

where $\omega_{\mathrm{ab}}$ is the TDDFT excitation energy.
Alternatively, based on the nonequilibrium excited-state reaction field, $G^{\mathrm{neq}}_{2}$ is given by[[129]](../bib_references/bib.md#bib119)

<a id="eq:G2_neq_k"></a>
$$
G^{\mathrm{neq}}_{2,k}=E^{k}_{1}+\omega^{k}_{\mathrm{ab}}-\sum_{m}V^{k}_{1,m}Q^{\mathrm{neq},k}_{2,m}-\frac{1}{2}\sum_{m}Q^{\mathrm{neq},k}_{2,m}D(\varepsilon)Q^{\mathrm{neq},k}_{2,m}\;, \tag{11.19}
$$

where $k$ represents the $k$th iteration of the nonequilibrium excited-state reaction field at the ground-state geometry of solute.
$\omega^{k}_{\mathrm{ab}}$ is the excitation energy from TDDFT calculation in the presence of the nonequilibrium excited-state reaction field.
The quantity $E^{k}_{1}$ is the ground-state electronic energy of solute at the $k$th iteration.
Clearly, Eq. ([11.19](#eq:G2_neq_k)) is more physically-meaningful than Eq. ([11.18](#eq:G2_neq)).

Similarly, the vertical excitation energy for emission is given by[[129]](../bib_references/bib.md#bib119)

<a id="Ch11.E20"></a>
$$
hv_{\mathrm{em}}=G^{\mathrm{eq}}_{2}-G^{\mathrm{neq}}_{1} \tag{11.20}
$$

where $G^{\mathrm{eq}}_{2}$ and $G^{\mathrm{neq}}_{1}$ represent the free energies of the equilibrium excited state and the nonequilibrium
ground state at the excited-state equilibrium geometry, respectively. These can be expressed as[[129]](../bib_references/bib.md#bib119)

<a id="Ch11.E21"></a>
$$
\displaystyle G^{\mathrm{neq}}_{1} \tag{11.21a}
$$

The quantity $\omega^{k}_{\text{em}}$ can be directly obtained by TDDFT calculation in the equilibrium excited-state reaction field
at the $k$th iteration. The energies ${E^{k}_{1}}^{\prime}$ and $E_{1}^{\prime\prime}$ are, respectively,
the corresponding ground-state electronic energy of the solute and the ground-state electronic energy of the solute at the
excited-state equilibrium geometry in the presence of the nonequilibrium ground-state reaction field.

To engage the constrained equilibrium principle for vertical absorption and emission, use the
**Td_CEq_NonEq** keyword in the *$pcm* section. Users are asked to cite Ref. [[821]](../bib_references/bib.md#bib852)
.

**Note: 

This method is incompatible with spin-flip calculations.
**

## 11.2.3.5 Heterogeneous PCM

For modeling proteins and other anisotropic environments, a “heterogeneous PCM” (HetPCM) approach
has been suggested, which amounts to using a different dielectric constant for each atomic
sphere.[[613]](../bib_references/bib.md#bib636)

Unlike the isotropic PCM, which is derivable from
Maxwell’s equations based on well-defined assumptions,[[569]](../bib_references/bib.md#bib580)
 HetPCM is entirely *ad hoc*.
However, it has recently been tested (for the first time)
against exact Poisson boundary conditions, implemented using the PEqS
approach that is discussed in Section [11.2.11](sect_PEQS.md).[[150]](../bib_references/bib.md#bib143)

Considering HetPCM methods that use a pair of distinct dielectric constants (namely, $\varepsilon=78$ to represent
an aqueous environment and a smaller value, $\varepsilon_{\text{nonp}}$, to represent a nonpolar or hydrophobic region),
it was determined that the heterogenous model is in reasonable agreement with solution of Poisson’s equation for an
analogous heterogeneous dielectric environment, provided that $\varepsilon_{\text{nonp}}\gtrsim 4$.[[150]](../bib_references/bib.md#bib143)

Fortunately, this is consistent with values that are often used to model the hydrophobic interiors of proteins.[[569]](../bib_references/bib.md#bib580)

See Example [11.2.4.2](subsec_PCM_job_control.md#ex:HetPCM) for instructions on setting up HetPCM calculations.
The analytic gradient is available for HetPCM.
