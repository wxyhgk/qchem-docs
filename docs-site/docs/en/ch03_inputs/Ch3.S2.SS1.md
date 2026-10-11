---
title: "3.2.1 Overview"
---

## 3.2.1 Overview

(July 4, 2026)

**IQmol** (or another graphical interface) is the simplest way to control
**Q-Chem**. However, the low level command line interface is available to enable
maximum customization and allow the user to exploit all **Q-Chem**’s features.
The command line interface requires a **Q-Chem** input file which is simply an
ASCII text file. This input file can be created using your favorite editor
(*e.g.*, vi, emacs, jot, *etc.*) following the basic steps outlined in the next few chapters.

**Q-Chem**’s input mechanism uses a series of **keywords** to signal user
input sections of the input file. As required, the **Q-Chem** program searches
the input file for supported keywords. When **Q-Chem** finds a keyword, it then
reads the section of the input file beginning at the keyword until that keyword
section is terminated the *$end* keyword. A short description of all **Q-Chem**
keywords is provided in Table [3.1](#table:input_sections) and the following
sections. The user **must** understand the function and format of the
*$molecule* (Section [3.3](sect_molinput.md)) and *$rem* (Section [3.4](sect_rem.md))
keywords, as these keyword sections are where the user places the molecular
geometry information and job specification details.

Table 3.1: 
Partial list of **Q-Chem** input sections; the first two (*$molecule* and *$rem*)
are required for all jobs, whereas the rest are required only for certain job
types, or else are optional places to specify additional job-control variables.
Each input section (“*$section*”) should be terminated with *$end*.
See the `$QC/samples` directory that is included with your release for
specific examples of **Q-Chem** input files using these keywords.

<table class="ltx_tabular">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Section Name</span></th>
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Description</span></th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t"><em class="ltx_emph ltx_font_italic">$molecule</em></td>
<td class="ltx_td ltx_align_left ltx_border_t">Contains the molecular coordinate input (input file requisite).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$rem</em></td>
<td class="ltx_td ltx_align_left">Job specification and customization parameters (input file requisite).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t"><em class="ltx_emph ltx_font_italic">$active_orbitals</em></td>
<td class="ltx_td ltx_align_left ltx_border_t">Specify active orbitals for nonorthogonal configuration interaction (Section <a class="ltx_ref" href="subsec_LIBNOCI.html" title="7.5.2 Job Control ‣ 7.5 Non-Orthogonal Configuration Interaction (NOCI) ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.5.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$alist</em></td>
<td class="ltx_td ltx_align_left">Specify active orbitals for TDDFT with a truncated subspace (Section <a class="ltx_ref" href="subsec_TDDFT-Xray.html" title="7.12.2 Calculations of X-Ray Spectroscopy with TDDFT ‣ 7.12 Core Ionization Energies and Core-Excited States ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.12.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined auxiliary basis set for resolution-of-identity calculations</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">(Chapter <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_j</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined auxiliary basis set for resolution-of-identity Coulomb</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">calculations (Chapter <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_k</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined auxiliary basis set for resolution-of-identity exact exchange</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">calculations (Chapter <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_corr</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined auxiliary basis set for resolution-of-identity correlation methods</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">(Chapter <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$basis</em></td>
<td class="ltx_td ltx_align_left">User-defined basis set information (Chapter <a class="ltx_ref" href="chap_basis.html" title="Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$cdft</em></td>
<td class="ltx_td ltx_align_left">Options for the constrained DFT method (Section <a class="ltx_ref" href="topic_cdft.html" title="5.11 Methods Based on “Constrained” DFT ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.11</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$chem_sol</em></td>
<td class="ltx_td ltx_align_left">Job control for the <span class="ltx_text ltx_font_smallcaps">Q-Chem</span>/<span class="ltx_text ltx_font_smallcaps">ChemSol</span> interface (Langevin dipoles</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">model; Section <a class="ltx_ref" href="subsec_LD.html" title="11.2.10 Langevin Dipoles Model ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.10</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$comment</em></td>
<td class="ltx_td ltx_align_left">User comments for inclusion into output file (Section <a class="ltx_ref" href="A2.S1.SS2.html#ssec:commentsec" title="B.1.2.4 $comment ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$complex_ccman</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">Contains parameters for complex-scaled and CAP-augmented EOM-CC</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">calculations (Chapter <a class="ltx_ref" href="topic_eomcc.html" title="7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$ecp</em></td>
<td class="ltx_td ltx_align_left">User-defined effective core potentials (Section <a class="ltx_ref" href="subsec_ECP-userdef.html" title="8.10.5 User-Defined ECPs ‣ 8.10 Effective Core Potentials (ECPs) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.10.5</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efei</em></td>
<td class="ltx_td ltx_align_left">Application of external forces in a geometry optimization (Section <a class="ltx_ref" href="sec_EFEI.html" title="9.5.1 Application of External Forces ‣ 9.5 Application of Pressure and Forces ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.5.1</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efp_fragments</em></td>
<td class="ltx_td ltx_align_left">Specifies labels and positions of EFP fragments (Section <a class="ltx_ref" href="sect_efp.html" title="11.5 Effective Fragment Potential Method ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.5</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efp_params</em></td>
<td class="ltx_td ltx_align_left">Contains user-defined parameters for effective fragments (Section <a class="ltx_ref" href="sect_efp.html" title="11.5 Effective Fragment Potential Method ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.5</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$empirical_dispersion</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined van der Waals parameters for DFT dispersion correction</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">(Section <a class="ltx_ref" href="subsec_DFT-D.html" title="5.7.3 Empirical Dispersion Corrections: DFT-D ‣ 5.7 DFT Methods for van der Waals Interactions ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.7.3</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$eom_user_guess</em></td>
<td class="ltx_td ltx_align_left">User-defined guess for EOM-CC calculations (Chapter <a class="ltx_ref" href="topic_eomcc.html" title="7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$external_charges</em></td>
<td class="ltx_td ltx_align_left">Specifies external point charges and their positions (Section <a class="ltx_ref" href="A2.S1.SS2.html#sec:externalcharges" title="B.1.2.7 $external_charges ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.7</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$fde</em></td>
<td class="ltx_td ltx_align_left">Specifies frozen density embedding options (Section <a class="ltx_ref" href="sect_FDET_methods.html" title="11.7 Frozen-Density Embedding Theory ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.7</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$force_field_params</em></td>
<td class="ltx_td ltx_align_left">Force-field parameters for QM/MM calculations (Section <a class="ltx_ref" href="sec_QMMM.html" title="11.3 Stand-Alone QM/MM Calculations ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.3</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$geom_opt</em></td>
<td class="ltx_td ltx_align_left">Geometry optimization controls for <span class="ltx_text ltx_font_smallcaps">Libopt3</span> calculations (Section <a class="ltx_ref" href="sec_geom_opt_controls.html" title="9.2 Geometry Optimization Job Controls ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$harmonic_opt</em></td>
<td class="ltx_td ltx_align_left">Information for optimization with soft harmonic constraints (Section <a class="ltx_ref" href="subsec_HarmonicConfiner.html" title="9.4.7 Atomic Confining Potentials as Alternatives to Constrained Optimization ‣ 9.4 Constrained Optimization ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.4.7</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$intracule</em></td>
<td class="ltx_td ltx_align_left">Intracule parameters (Section <a class="ltx_ref" href="sect_intracules.html" title="13.2 Intracules ‣ Chapter 13 Specialized Topics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">13.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$isotopes</em></td>
<td class="ltx_td ltx_align_left">Isotopic substitutions for vibrational calculations (Section <a class="ltx_ref" href="ex_Isotope-Mass.html" title="10.8.2 Isotopic Substitutions and Changes in T and P ‣ 10.8 Harmonic Vibrational Analysis ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.8.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$localized_diabatization</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">Information for mixing together multiple adiabatic states into diabatic</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">states (Chapter <a class="ltx_ref" href="chap_properties.html" title="Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$magnet</em></td>
<td class="ltx_td ltx_align_left">Job control for magnetic field-related response properties (Section <a class="ltx_ref" href="sec_magnetman.html" title="10.11.4 Additional Magnetic Field-Related Properties ‣ 10.11 NMR and Other Magnetic Properties ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.11.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$mass</em></td>
<td class="ltx_td ltx_align_left">User-defined atomic mass (Chapter <a class="ltx_ref" href="topic_aimd.html" title="9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$multipole_field</em></td>
<td class="ltx_td ltx_align_left">Details of an external multipole field (Section <a class="ltx_ref" href="A2.S1.SS2.html#sec:multipolefield" title="B.1.2.10 $multipole_field ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.10</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$nbo</em></td>
<td class="ltx_td ltx_align_left">Options for the Natural Bond Orbital package (Section <a class="ltx_ref" href="sect_NBO.html" title="10.3.1 Interface to the NBO Package ‣ 10.3 Orbital Analysis ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.3.1</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$occupied</em></td>
<td class="ltx_td ltx_align_left">Guess orbitals to be occupied (Section <a class="ltx_ref" href="sect_occupied.html" title="4.4.4 Modifying the Occupied Molecular Orbitals ‣ 4.4 SCF Initial Guess ‣ Chapter 4 Self-Consistent Field Ground-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">4.4.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$opt</em></td>
<td class="ltx_td ltx_align_left">Constraint definitions for geometry optimizations (Section <a class="ltx_ref" href="sec_constrained_opt.html" title="9.4 Constrained Optimization ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$pcm</em></td>
<td class="ltx_td ltx_align_left">Job control for polarizable continuum models (Section <a class="ltx_ref" href="subsec_PCM_job_control.html" title="11.2.4 PCM Job Control ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$plots</em></td>
<td class="ltx_td ltx_align_left">Generate plotting information over a grid of points (Section <a class="ltx_ref" href="sect_plots.html" title="10.5 Visualizing and Plotting Volumetric Quantities ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.5</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_active_modes</em></td>
<td class="ltx_td ltx_align_left ltx_border_l" rowspan="3">Information for quasi-classical trajectory calculations (Section <a class="ltx_ref" href="subsec_QCT.html" title="9.9.6 Quasi-Classical Molecular Dynamics ‣ 9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9.6</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_vib_distribution</em></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_vib_phase</em></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qm_atoms</em></td>
<td class="ltx_td ltx_align_left">Specify the QM region for QM/MM calculations (Section <a class="ltx_ref" href="sec_QMMM.html" title="11.3 Stand-Alone QM/MM Calculations ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.3</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$response</em></td>
<td class="ltx_td ltx_align_left">Job control for the generalized response solver (Section <a class="ltx_ref" href="sec_GeneralResponseTheory.html" title="10.14 General Response Theory ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.14</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$solvent</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">Additional parameters and variables for implicit solvent models</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">(Section <a class="ltx_ref" href="topic_solvation.html" title="11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$smx</em></td>
<td class="ltx_td ltx_align_left">Job control for SM$x$ implicit solvent models (Section <a class="ltx_ref" href="ex_SMx-User-Solvent.html" title="11.2.9 SM x Models ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.9</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$spin-spin</em></td>
<td class="ltx_td ltx_align_left">Indices for atoms to include in spin-spin coupling calculations (Section <a class="ltx_ref" href="sec_magnetic_NMR.html#subsec:mopropmanNMRJobControl" title="10.11.2.2 NMR Job Control and Examples ‣ 10.11.2 NMR Chemical Shifts and J-Couplings ‣ 10.11 NMR and Other Magnetic Properties ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.11.2.2</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$swap_occupied_virtual</em></td>
<td class="ltx_td ltx_align_left">Guess orbitals to be swapped (Section <a class="ltx_ref" href="sect_occupied.html" title="4.4.4 Modifying the Occupied Molecular Orbitals ‣ 4.4 SCF Initial Guess ‣ Chapter 4 Self-Consistent Field Ground-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">4.4.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$svp</em></td>
<td class="ltx_td ltx_align_left">Special parameters for the iso-density SS(V)PE module (Section <a class="ltx_ref" href="subsec_SS(V)PE.html" title="11.2.6 Isodensity Implementation of SS(V)PE ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.6</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$svpirf</em></td>
<td class="ltx_td ltx_align_left">Initial guess for the iso-density SS(V)PE module (Section <a class="ltx_ref" href="subsec_SS(V)PE.html" title="11.2.6 Isodensity Implementation of SS(V)PE ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.6</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$van_der_waals</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">User-defined atomic radii for Langevin dipoles solvation (Section <a class="ltx_ref" href="subsec_LD.html" title="11.2.10 Langevin Dipoles Model ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.10</span></a>)</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">and PCMs (Section <a class="ltx_ref" href="topic_pcm-em.html" title="11.2.3 Polarizable Continuum Models ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.3</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$velocity</em></td>
<td class="ltx_td ltx_align_left">User-defined nuclear velocity for AIMD calculations (Chapter <a class="ltx_ref" href="topic_aimd.html" title="9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$xc_functional</em></td>
<td class="ltx_td ltx_align_left">User-defined DFT exchange-correlation functional (Section <a class="ltx_ref" href="sect_userxc.html" title="5.3.7 User-Defined Density Functionals ‣ 5.3 Overview of Available Functionals ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.3.7</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$xdm</em></td>
<td class="ltx_td ltx_align_left">Job control for the XDM dispersion method (Section <a class="ltx_ref" href="sect_XDM.html" title="5.7.4 Exchange-Dipole Model (XDM) ‣ 5.7 DFT Methods for van der Waals Interactions ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.7.4</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$zbasis</em></td>
<td class="ltx_td ltx_align_left">User-defined complex basis set information (Section <a class="ltx_ref" href="sect_zbas.html" title="8.7 Complex Basis Sets ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.7</span></a>).</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_bb" rowspan="2"><em class="ltx_emph ltx_font_italic">$2pa</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">Additional parameters for two-photon absorption calculations</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_bb ltx_border_l">(Section <a class="ltx_ref" href="sec_EOMGRAD.html#sec:2PA" title="7.9.21.6 Transition Moments and Cross Sections for Two-Photon Absorption within EOM-EE-CCSD ‣ 7.9.21 Analytic Gradients and Properties for CCSD and EOM-XX-CCSD ‣ 7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9.21.6</span></a>).</td>
</tr>
</tbody>
</table>

**The keywords *$rem* and *$molecule* are required in any **Q-Chem** input file**

As each keyword has a different function, the format required for specific
keywords varies somewhat, to account for these differences (format requirements
are summarized in Appendix [B](../app_b_quickref/app_quick_ref.md)). However, because each keyword in
the input file is sought out independently by the program, the overall format
requirements of **Q-Chem** input files are much less stringent. For example, the
*$molecule* section does not have to occur at the very beginning of the input file.

> **Note: 
> 
> (1) Users are able to enter keyword sections in any order.
> (2) Each keyword section must be terminated with the *$end* keyword.
> (3) The *$rem* and *$molecule* sections must be included.
> (4) It is not necessary to have all keywords in an input file.
> (5) Each keyword section is described in Appendix [B](../app_b_quickref/app_quick_ref.md).
> (6) The entire **Q-Chem** input is case-insensitive.
> **

The second general aspect of **Q-Chem** input is that there are effectively four input sources:

- •

User input file (required)
- •

`.qchemrc` file in `$HOME` (optional)
- •

`preferences` file in `$QC/config` (optional)
- •

Internal program defaults and calculation results (built-in)

The order of preference is as shown, *i.e.*, the input mechanism offers a program
default override for *all* users, default override for *individual*
users and, of course, the input file provided by the user overrides all
defaults. Refer to Section [2.1.6](../ch02_install/sect_customization.md) for details of
`.qchemrc` and `preferences`. Currently, **Q-Chem** only supports the
*$rem* keyword in `.qchemrc` and `preferences` files.

In general, users will need to enter variables for the *$molecule* and *$rem*
keyword section and are encouraged to add a *$comment* for future reference.
The necessity of other keyword input will become apparent throughout the
manual.
