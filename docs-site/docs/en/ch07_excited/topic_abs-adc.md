---
title: "7.10.11 Excited States in Solution with ADC/SS-PCM"
---

## 7.10.11 Excited States in Solution with ADC/SS-PCM

(July 4, 2026)

**ADCman** is interfaced to the versatile polarizable-continuum model (PCM)
implemented in **Q-Chem** (Section [11.2.3](../ch11_env/topic_pcm-em.md)) and may thus be employed for
the calculation and analysis of excited-state wave functions and transitions in
solution, or more general in dielectric environments. The interface follows the
state-specific approach, and supports a self-consistent equilibration of the
solvent field for long-lived excited states commonly referred to as
*equilibrium solvation*, as well as the calculation of perturbative
corrections for vertical transitions, known as *nonequilibrium solvation*;
see also section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM). Combining both
approaches, virtually all photochemically relevant processes can be modeled,
including ground- and excited-state absorption, fluorescence, phosphorescence,
as well as photochemical reactivity. Requiring only the electron-densities of
ground- and excited states of the solute as well as and the dielectric constant
and refractive index of the solvent, ADC/SS-PCM is straightforward to set
up and supports all orders and variants of ADC for which densities are
available via the ISR. This includes all levels of canonical ADC, SOS-ADC,
SF-ADC for electronically complicated situations, as well as CVS-ADC for the
description of core-excited states with and without the resolution of the
identity and frozen-core approximation, restricted closed-shell references as
well unrestricted open-shell. The computed solvent-relaxed wave functions can
be visualized and analyzed using the interface to **libwfa**.

Although we give a short introduction to the theory in this section, it is
limited to a brief, qualitative overview with only the most important
equations, leaving out major aspects such as the polarization work.
For an overview of the theory see Ref. [[569]](../bib_references/bib.md#bib580)
.
A more detailed treatment of the theory can be found in
Refs. [[940]](../bib_references/bib.md#bib979)
 and [[939]](../bib_references/bib.md#bib982)
. See also
Sections [11.2.3](../ch11_env/topic_pcm-em.md) and [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) of this manual.

## 7.10.11.1 Modeling the Absorption Spectrum in Solution

**(A) Theory

**Let us begin with a brief review of the theoretical and technical aspects of
the calculation of absorption spectra in solution. For this purpose, one would
typically employ the perturbative, state-specific approach in combination with
an ADC of second or third order. The first step is a self-consistent reaction
field calculation [SCRF, Hartree-Fock with a PCM, Eq. ([7.152](#eq:ADC_SCRF))].

<a id="eq:ADC_SCRF"></a>
$$
E_{0}=\langle 0|\hat{H}^{\text{vac}}+\hat{R}(0)|0\rangle \tag{7.152}
$$

The PCM is formally represented by the reaction- or solvent-field operator
$\hat{R}$. In practice, $\hat{R}$ is a set of point charges placed on the
molecular surface, which are optimized together with the orbitals during the
SCF procedure. Note that since $\hat{R}$ accounts for the self-induced
polarization of the solute, it depends on solute’s wave function (here the
ground state), which will in the following be indicated in the subscript $\hat{R}_{0}$.

After the SCRF is converged, the final surface charges and the respective
operator can, according to the Franck-Condon principle, be separated into a
“slow” solvent-nuclei related ($\epsilon-n^{2}$) and “fast”,
solvent-electron related ($n^{2}$) component (using Marcus partitioning, eq.
([7.153](#eq:ADC_R_sep))), and are stored on disk.

<a id="eq:ADC_R_sep"></a>
$$
\hat{R}(0)\equiv\hat{R}^{\text{tot}}_{0}=\hat{R}^{\text{f}}_{0}+\hat{R}^{\text{s}}_{0} \tag{7.153}
$$

<a id="eq:ADC_separation"></a>
$$
\displaystyle q^{f}= \tag{7.154}
$$

The “polarized” MOs resulting from the SCRF step are subjected to ordinary
MP/ADC calculations, which yield the correlation energy for the ground and
excitation energies for the excited states, which are both added to the HF
energy to obtain the total MP ground and ADC excited-state energies. However,
since the MOs contain the interaction with the complete “frozen”
solvent-polarization of the SCF ground-state density ($\hat{R}^{\text{tot}}$,
*i.e.*, *both* components), the resulting excitation energies violate the
Franck-Condon principle, which requires the solvents electronic degrees of
freedom (fast component of the polarization) to be relaxed. Furthermore, the
solvent field has been obtained for the SCF density, which more often than not
provides a poor description of the electrostatic nature of the solute and may
in turn lead to systematic errors in the excitation energies.

To account for the relaxation of the solvent electrons and bring the
excitation/excited-state energies in accordance with Franck-Condon, we employ
the perturbative ansatz shown in eq. ([7.155](#eq:ADC_ptSS)), in which the fast
component of the ground-state solvent field $\hat{R}^{\text{f}}_{0}$ is replaced
by the respective quantity computed for the excited-state density
$\hat{R}^{\text{f}}_{\text{i}}$. In this framework, the energy of an excited
state $i$ computed with the polarized MOs can be identified as the zeroth-order
energy [Eq. ([7.157](#eq:ADC_PT_zeroth))], while the first-order term becomes the
difference between the interaction of the zeroth-order excited-state density
with the fast component of the ground- and excited-state solvent fields given
in eq. ([7.158](#eq:ADC_PT_first)).

<a id="eq:ADC_ptSS"></a>
$$
E_{\text{i}}^{\text{NEq}}=\langle i|\hat{H}^{\text{vac}}+\hat{R}^{\text{tot}}_{0}+\lambda(\hat{R}^{\text{f}}_{\text{i}}-\hat{R}^{\text{f}}_{\text{0}})|i\rangle\\ \tag{7.155}
$$

<a id="A3.S8.EGx67"></a>
$$
\displaystyle E^{\rm NEq(0)}_{i}= \tag{7.156}
$$

After the ADC iterations have converged, $\hat{R}^{\text{f}}_{\text{i}}$ is
computed from the respective excited-state density and $\hat{R}^{\text{f}}_{0}$
read from disk to form the first-order correction. Adding this so-called
ptSS-term to the zeroth order energy, one arrives at the vertical
energy in the nonequilibrium limit $E_{\text{i}}^{\text{NEq}}$. Since the
ptSS-term accounts for the response of the electron density of the implicit
solvent molecules to excitation of the solute, its always negative and thus lowers
the energy of the excited state with respect to the ground state.

To eliminate problems resulting from the poor description of the ground-state
solvent field at the SCF level of theory, we use an additive correction that
is based on the MP2 ground-state density. In a nutshell, it replaces the
interaction between the potential of the difference density of the excited
state $\hat{V}_{i^{(0)}}-\hat{V}_{0^{\textit{MP}}}$ with the SCF solvent field
$\hat{Q}_{0^{\textit{HF}}}$ by the respective interaction with the MP solvent
field $\hat{Q}_{0^{\textit{MP}}}$:

<a id="A3.S8.EGx68"></a>
$$
\displaystyle E_{\textit{PTD}}= \tag{7.159}
$$

We will in the following refer to this as “perturbative, density-based” (PTD)
correction and denote the respective approach as ptSS(PTD). Accordingly, the
non-PTD corrected results will be denoted ptSS(PTE).

In addition to the ptSS-PCM discussed above, a perturbative variant of the
so-called linear response corrections (termed ptLR presented in
Ref. [[940]](../bib_references/bib.md#bib979)
) is also available. In contrast to the ptSS
approach, the ptLR corrections depend on the transition rather than the state
(difference) densities. Although the ptLR corrections are always computed and
printed, we discourage their use with the correlated ADC variants (2 and
higher), for which the ptSS approach is better suited. The ptSS and ptLR
approaches are also available for TDDFT as described in
Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM).

A detailed, comprehensive introduction to the theory and implementation, as
well as extensive benchmark data for the nonequilibrium formalism in
combination with all orders of ADC can be found in Ref.
[[940]](../bib_references/bib.md#bib979)
.

**(B) Usage

**The calculation of vertical transition energies with the ptSS-PCM approach is
fairly straightforward. One just needs to activate the PCM (set
SOLVENT_METHOD in the *$rem* block to PCM), enable the
nonequilibrium functionality (set NONEQUILIBRIUM in the *$pcm* block
to TRUE), and specify the solvent parameters, *i.e.*, dielectric
constant $\epsilon$ (DIELECTRIC) and squared refractive index $n^{2}$
(DIELECTRIC_INFI) in the *$solvent* block.

**Note: 

Symmetry will be disabled for all calculations with a PCM.
**

In the output of a ptSS-PCM calculation with any correlated ADC variant,
multiple values are given for the total and transition energies depending in
the level of theory. For the correlated ADC variants these include:

- •

*Zeroth-order results*, direct outcome of the ADC calculation with
solvated orbitals, excited states are ordered according to this value.
- •

*First-order results*, incl. only ptSS nonequilibrium
corrections, termed ptSS(PTE).
- •

*Corrected first-order results*, incl. also the correlation
correction, termed ptSS(PTD).
- •

*Scaled and corrected first-order results*, incl. an empirical
scaling of the correlation correction, termed ptSS(PTD*).

We recommend to use the corrected first-order results since the PTD correction
generally yields the most accurate results. The ptSS(PTD) approach is typically a
very good approximation to the fully consistent, but more expensive PTED
scheme, in which the solvent field is made self-consistent with the MP2 density
(see next section for the PTED scheme and sample-jobs for a comparison of the
two). Oscillator strengths are computed using the ptSS(PTD) energies.
The PTD* approach includes an empirical scaling of the PTD correction
that was developed to improve the solvatochromic-shifts of a series of
nitro-aromatics with a cc-pVDZ basis.[[940]](../bib_references/bib.md#bib979)
 However, we later
found that for most other systems, the scaling slightly worsens the
agreement with the fully consistent PTED scheme.
In addition to the compiled total and transition energies, all contributing
terms (ptSS, PTD etc.) are given separately. An even more verbose output
detailing all the integrals contributing to the 1st order corrections can
be obtained by increasing PCM_PRINT to 1.

**Note: 

The zeroth-order results are by no means identical to the gas-phase
excitation energies, and in turn the ptSS-term is not the solvatochromic
shift.
**

**(C) Tips and Tricks

**To model the absorption spectrum in polar solvents, it is advisable to use a
structure optimized in the presence of a PCM since the influence can be quite
significant.

It should also be taken into account that a PCM, being a purely electrostatic
model, lacks at the description of explicit interactions such as hydrogen
bonds. If fairly strong H-bond donor or acceptor moieties are present, or a
protic or Lewis-basic solvent is to be modeled, consider adding one or two
explicit solvent molecules per donor/acceptor site, and optimize
them together with the molecule in the presence of a PCM. A systematic
investigation of this aspect for two representative examples can be found in
Ref. [[940]](../bib_references/bib.md#bib979)
.

If large differences between the HF and MP description of the molecule exist
(PTD terms $>0.2$ eV), it is advisable to employ the iterative ptSS(PTED)
scheme described in the next section. Due to the inverse nature of the
systematic errors of ADC(2) and ADC(3), the best guess for the excitation
energy in solution is usually the average of both values.

For the PCM, we recommend the formally exact and slightly more expensive
integral-equation formalism (IEF)-PCM variant (**Theory** to
**IEFPCM** in the *$pcm* block) in place of the approximate C-PCM, and
otherwise default parameters.

## 7.10.11.2 Modeling Emission, Excited-State Absorption and Photochemical
Reactivity

**(A) Theory

**To model emission/absorption of solvent-equilibrated excited states and/or to
investigate their photochemical reactivity, both components of the polarization
have to be relaxed with respect to the desired state. This becomes evident
considering that a full solvent-field equilibration (including the
nuclear component) is essentially a geometry optimization for the implicit
solvent, and should thus be employed whenever the geometry of the solute is
optimized for the desired excited state. The Hamiltonian for a
solvent-equilibrated state $|k\rangle$ simply reads

<a id="Ch7.E161"></a>
$$
E^{\rm EqS}_{\rm k}=\bigl{\langle}k\bigl{|}\hat{H}^{\rm vac}+\hat{R}_{\rm k}\bigl{|}k\bigr{\rangle}\;. \tag{7.161}
$$

Since the interaction with solvent field of any state has to be introduced to
the MOs in the SCF step of a calculation, a solvent-field equilibration for
excited states (and correlated ground states) is an iterative procedure
requiring multiple SCF+ADC calculations until convergence is achieved. This
also means that a guess (typically from a ptSS calculation) for the solvent
field has to generated and used in the first SCF step. The MOs resulting from
this first SCF are subjected to an ADC calculation, providing a first
excited-state density, for which a new solvent field is computed and employed
in the SCF step of the second iteration. This procedure is repeated until the
solvent field (charges) and energies are converged and ultimately provides the
total energy and wave function of the solvent-equilibrated excited state $|k\rangle$,
as well as the out-of-equilibrium wave functions of other states.
However, as the name already suggest, this state-specific approach yields a
meaningful energy only for the solvent-equilibrated reference state $|k\rangle$.
All other states have to be treated in the nonequilibrium limit and
subjected to the formalism presented in the previous section to be consistent
with the Franck-Condon principle. The respective generalization of the
perturbative ansatz for the Hamiltonian for the $i$th out-of-equilibrium
state in the field of the equilibrated state $|k\rangle$ reads as

<a id="Ch7.E162"></a>
$$
E^{\rm NEq(k)}_{\rm i}=\bigl{\langle}i|\hat{H}^{\rm vac}+\hat{R}^{\rm tot}_{\rm k}+\lambda(\hat{R}^{\rm f}_{\rm i}-\hat{R}^{\rm f}_{\rm k})|i\bigr{\rangle}\;, \tag{7.162}
$$

which can be solved using the procedure introduced in the previous section.

While most of the technical aspects concerning the application of the model
will be covered in the following, we highly recommend to read at least the
formalism and implementation section of Ref. [[939]](../bib_references/bib.md#bib982)
 before using the model.

**(B) Usage

**The main switch for the state-specific equilibrium solvation (SS-PCM) is the
variable EQSOLV in the *$pcm* block. Setting it to TRUE will
cause the SCF+ADC calculation to be carried out using the solvent field of the
first excited state (if that is found on disk), while any integer $>1$ triggers
the automatic solvent-field optimization and is interpreted as the maximum
number of steps. We recommend to use EQSOLV = 15. Note that to use the
SS-PCM, the PCM (SOLVENT_METHOD = PCM in *$rem*) and its
nonequilibrium functionalities (NONEQUILIBRIUM = TRUE in
*$pcm*) have to be activated as well. Since the solvent-field iterations
require an initial guess, a SS-PCM calculation is always the second (or
third, $\ldots$) step of a multi-step job.

**Note: 

Any SS-PCM calculation requires a preceding converged ptSS-PCM
calculation (*i.e.*, EQSOLV = FALSE) for the desired state to provide a
guess for the initial solvent field, or it will crash during the SCF.
**

To create the input-file for a multi step job, add "@@@" at the end of the
input for the first job and append the input for the second job. See also
section [3.5](../ch03_inputs/sec_multiple_jobs.md). Note that the solvent field used in the
subsequent step is stored in the basis of the molecular-surface elements and
thus, the geometry of the molecule as well as parameters that affect
construction and discretization of the molecular cavity must not be changed
between the jobs/steps. This, however, is not enforced.

The state for which the solvent field is to be optimized is specified using the
variable EQSTATE in the *$pcm* block. A value of 0 refers to the MP
ground-state (for PTED calculations), 1 selects the energetically lowest
excited state (default), 2 the second lowest, and so on. The solvent field can
be optimized for any singlet, triplet or spin-flip excited state. However,
*only the desired class of states should be requested*, *i.e.*, either
EE_SINGLETS or EE_TRIPLETS for singlet references, and
either EE_STATES or SF_STATES for triplet references. To
compute, *e.g.*, the phosphorescence energy, only triplet states should be
requested and EQSTATE would typically be set to 1.

**Note: 

Computing multiple classes of excited states during the solvent-field
iterations will confuse the state-ordering logic of the program and yield the
wrong results.
**

Convergence is controlled by EQS_CONV. Criteria are the SCF energy as
well as the RMSD, MAD and largest single difference of the surface-charges. The
convergence should not need to be modified. It is per default derived from the
SCF convergence parameter (SCF_CONVERGENCE$-4$). The default value
of 4 (since SCF_CONVERGENCE is 8 for ADC calculations) corresponds to
an maximum energy change of $2.72$ meV and will yield converged total energies
for all states. Excitation energies and in particular the total energy of the
reference state converge somewhat faster than the SCF energy, and a value of 3
may save some time for the computation, *e.g.*, for the emission energy of large solutes.

A typical ADC/SS-PCM calculation consists of three steps/subsequent jobs:

1. 1.

Generation of an initial guess for the solvent field using a
nonequilibrium calculation (EQSTATE = FALSE). To save time,
this would typically be done with a smaller basis set and lower convergence
criteria (*e.g.*,

ADC_DAVIDSON_CONV = 4).
2. 2.

Converging the solvent field for the desired state. In this step it is
advisable to compute as few states as possible (maybe one more than
EQSTATE to be aware of looming state crossings), and more importantly,
only the desired class of excited states.
3. 3.

Computing all excited states of interest and their properties in the
previously converged solvent field. If the reference state of the solvent-field
equilibration is a singlet state, this is straightforward and any number of
singlet/triplet states can be computed in this final step without further
input. *If singlet states are to be computed in the solvent field of a
triplet state*, the additional variable EQS_REF in *$pcm* has to be
set to tell the program which state is to be treated as the reference state in
this last step.
For this purpose, EQS_REF is set to the desired triplet state plus
the number of *converged* singlet states. Hence, assuming 2 singlet
states are to be calculated along with the triplets in previously converged
solvent field of $T_{1}$, and furthermore that both singlets converge,
EQS_REF needs to be set to 3 (this can not be realized using the
variable EQSTATE, because we still want to use the solvent field of
the lowest triplet state stored in the previous step).

The self-consistent SS-PCM can also be used to compute a fully consistent
solvent field for the MP2 ground state by setting EQSTATE to 0. This
is known as ptSS(PTED) approach and can improve vertical excitation energies if
there are large differences between the electrostatic properties of the SCF and
MP ground states (large PTD corrections). In most cases, however, the
non-iterative PTD approach is a very good approximation to the PTED approach
(see the sample jobs below). The output of a PTED calculation is essentially
identical to that of a ptSS calculation.

The program possesses limited intelligence in detecting the type of the
calculation (PTED or EQS/SS-PCM) as well as the target state of the
solvent-field equilibration and will assemble and designate the ptSS
corrections, total energies and transition energies accordingly. This logic
will be confused if multiple classes of states (*e.g.* singlet and triplets) are
computed simultaneously during the iterations, and/or if the ordering of the
states changes. Nevertheless, in a final job for a previously converged solvent
field *of a singlet reference* singlet and triplet states can be
computed together yielding the correct output. However, if singlet states are
computed in the converged solvent field of *a triplet reference* the
additional variable EQS_REF has to be set (and only then, see above).

In the “HF/MP2/MP3 Summary” section, zeroth (without ptSS) and first (with
ptSS) order total energies of the respective ground state in the solvent field
of the target state are given along with the ptSS term for a vertical
transition from the equilibrated state (emission). Note that to obtain the MP3
ground state energy during an ADC(3)/EQS calculation, the ptSS term has to be
added manually (it is printed in the MP2 Summary since we use the MP2 density
for this purpose).

In the “Excited-State Summary” section the reference state is distinguished
from the out-of-equilibrium states. Respective total and transition energies
are given along with the nonequilibrium corrections, transition moments and
some remarks. Note that for emission, in contrast to absorption, the ptSS term
increases the transition energy as it lowers the energy of the
out-of-equilibrium ground state. The so-called “self-ptSS term” is a
perturbative estimate of how much the solvent field of this state is off from
its equilibrium. Although the line in the output changes depending on the value
(from “not converged” to “reasonably converged” to “converged”) it is not used
in the actual convergence check. Note that the self-ptSS term is computed with
$n^{2}$ (**dielectric_infi**) and not $\epsilon$, as it probably should be.
The self-ptSS term may be used to judge how well a solvent field computed with
a different methodology (basis, ADC order/variant) fits. In such a case, values
$<0.01$ eV signal a reasonable agreement.

To calculate inter-state transition moments for excited-state absorption, the
variable ADC_PROP_ES2ES has to be set to TRUE.
Unfortunately, transition energies have to be computed manually from the
(first-order) total energies given in the excited-state summary, since the
transition energies given along with the state-to-state transition moments
following the excite-state summary are incorrect (missing nonequilibrium terms).

The progress of the solvent-field iteration and their convergence is reported
following the “Excited-State Summary”.

**(C) Tips and Tricks

**To compute fluorescence and phosphorescence energies, solute geometry AND
solvent field should both be optimized for the suspected emitting state. Since
hardly any programs can perform excited-state optimizations with the SS-PCM
solvent models, you will probably have to use gas-phase geometries. In our
experience, the errors introduced by this approximation are small to negligible
(typically $<0.1$ eV) in non-polar solvents, but can become significant in
polar solvents, in particular for polar charge-transfer states.

Concerning the predicted emission energies, we found that ADC(2)/SS-PCM
typically over-stabilizes CT states, yielding emission energies that are too
low. SOS-ADC(2) can improve this error, but does not eliminate it. In general,
while emission energies are more accurate with (SOS-)ADC(2)/SS-PCM than with
ADC(3)/SS-PCM, the latter affords better relative state energies (see Ref.
[[939]](../bib_references/bib.md#bib982)
).

Keep in mind that the solute-solvent interaction of polar solvents with polar
(*e.g.*, charge-transfer) states can become quite large (multiple eV), and may
thus affect the ordering and nature of the excited states. This is quite
typical for charge-transfer states even in remotely polar solvents. If they are
not the lowest state in the nonequilibrium calculation, but say $S_{2}$, it is
typically necessary to do one solvent-field iteration for the CT state
(EQSOLV = 1 and EQSTATE = 2), which brings the CT down to
become $S_{1}$, and then continue the iterations with EQSOLV = 15 and
EQSTATE = 1. It is in general advisable to carefully check if the
character and/or energetic ordering of the states changes during the procedure,
in particular for any equilibration of the solvent field for all but the lowest
excited state (*e.g.* $S_{2}$ or $S_{3}$). But even the solvent-field equilibration
for a weakly polar $S_{1}$ in a polar solvent can cause a more polar state with
the same dipole-vector to become the lowest state.

If the excited-states swap during the procedure, find out in which step the
swap occurred and do only so many iterations (*i.e.*, set EQSOLV
accordingly). In a following job, adjust the variable EQSTATE and
continue the iterations. If states start to mix when they get close, it might
help to first set an artificially large dielectric constant to induce the
change in ordering, and then continue with the desired dielectric constant in a
following job.

If performance is critical, the calculations may be accelerated by lowering the
ADC convergence during the solvent-field iterations (set
ADC_DAVIDSON_CONV = 5). The number of iterations may be
reduced by first converging the solvent field with a smaller basis/at a lower
level of ADC followed by another job with the full basis/level of ADC. However,
in our experience ADC(2) and ADC(3) solvent fields for the same state differ
quite significantly and the approach probably does not help much. In contrast,
the solvent field computed with a smaller basis (*e.g.* 3-21G, SVP) is often a
good approximation for that computed with a larger basis (*e.g.* def2-TZVP, see
examples), such this may actually help. It is in general advisable to compute
just as many states as is necessary during the solvent-field iterations and
include higher lying excited states and triplets in the final job. In ADC(2)
calculations for large systems, one should always employ the
resolution-of-the-identity approximation.

To save time in PTED jobs, it is suggested to disable the computation of
excited states during the solvent-field iterations of a PTED job by setting
EE_SINGLETS (and/or EE_TRIPLETS/ EE_STATES) to 0
and compute the excited-states in a final job once the reaction field is
converged.
