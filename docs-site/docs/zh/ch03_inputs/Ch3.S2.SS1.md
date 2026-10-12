---
title: "3.2.1 概述"
---

## 3.2.1 概述

（2026 年 7 月 4 日）

**IQmol**（或其他图形界面）是控制 **Q-Chem** 最简单的方式。不过，底层（low level）命令行界面同样可用，以实现最大程度的定制并让用户能够充分利用 **Q-Chem** 的所有功能。命令行界面需要一份 **Q-Chem** 输入文件，它只是一个简单的 ASCII 文本文件。按照接下来几章所述的基本步骤，使用您喜爱的编辑器（*e.g.*，vi、emacs、jot，*etc.*）即可创建该输入文件。

**Q-Chem** 的输入机制使用一系列**关键字（keywords）**来标识输入文件中的用户输入区段。程序会按需在整个输入文件中搜索其支持的关键字。当 **Q-Chem** 找到一个关键字时，它就从该关键字处开始读取输入文件的相应区段，直到该区段被 *$end* 关键字结束为止。所有 **Q-Chem** 关键字的简要说明见表 [3.1](#table:input_sections) 及后续各节。用户**必须**理解 *$molecule*（第 [3.3](sect_molinput.md) 节）与 *$rem*（第 [3.4](sect_rem.md) 节）这两个关键字的功能和格式，因为分子几何信息以及作业规格说明正是放置在这两个关键字区段中的。

表 3.1： 
**Q-Chem** 输入区段的部分列表；前两个区段（*$molecule* 和 *$rem*）对所有作业都是必需的，其余区段则仅在某些作业类型下才需要，或者作为指定额外作业控制变量的可选位置。
每个输入区段（“*$section*”）都应以 *$end* 结束。
具体使用这些关键字的 **Q-Chem** 输入文件示例，请参阅随发行版一同提供的 `$QC/samples` 目录。

<table class="ltx_tabular">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">区段名称</span></th>
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">说明</span></th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t"><em class="ltx_emph ltx_font_italic">$molecule</em></td>
<td class="ltx_td ltx_align_left ltx_border_t">包含分子坐标输入（输入文件必需项）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$rem</em></td>
<td class="ltx_td ltx_align_left">作业规格与定制参数（输入文件必需项）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t"><em class="ltx_emph ltx_font_italic">$active_orbitals</em></td>
<td class="ltx_td ltx_align_left ltx_border_t">为非正交组态相互作用（nonorthogonal configuration interaction）指定活性轨道（第 <a class="ltx_ref" href="subsec_LIBNOCI.html" title="7.5.2 Job Control ‣ 7.5 Non-Orthogonal Configuration Interaction (NOCI) ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.5.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$alist</em></td>
<td class="ltx_td ltx_align_left">为采用截断子空间的含时密度泛函理论（TDDFT）指定活性轨道（第 <a class="ltx_ref" href="subsec_TDDFT-Xray.html" title="7.12.2 Calculations of X-Ray Spectroscopy with TDDFT ‣ 7.12 Core Ionization Energies and Core-Excited States ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.12.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的辅助基组（auxiliary basis set），用于分辨率恒等（resolution-of-identity）计算</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">（第 <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_j</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的辅助基组，用于分辨率恒等库仑（Coulomb）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">计算（第 <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_k</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的辅助基组，用于分辨率恒等精确交换（exact exchange）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">计算（第 <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$aux_basis_corr</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的辅助基组，用于分辨率恒等关联方法（correlation methods）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">（第 <a class="ltx_ref" href="sect_userbasis.html" title="8.4 User-Defined Basis Sets ($basis) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.4</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$basis</em></td>
<td class="ltx_td ltx_align_left">用户定义的基组（Basis Set）信息（第 <a class="ltx_ref" href="chap_basis.html" title="Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$cdft</em></td>
<td class="ltx_td ltx_align_left">受约束密度泛函理论（constrained DFT）方法的选项（第 <a class="ltx_ref" href="topic_cdft.html" title="5.11 Methods Based on “Constrained” DFT ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.11</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$chem_sol</em></td>
<td class="ltx_td ltx_align_left"><span class="ltx_text ltx_font_smallcaps">Q-Chem</span>/<span class="ltx_text ltx_font_smallcaps">ChemSol</span> 接口的作业控制（朗之万偶极子（Langevin dipoles）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">模型；第 <a class="ltx_ref" href="subsec_LD.html" title="11.2.10 Langevin Dipoles Model ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.10</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$comment</em></td>
<td class="ltx_td ltx_align_left">写入输出文件的用户注释（第 <a class="ltx_ref" href="A2.S1.SS2.html#ssec:commentsec" title="B.1.2.4 $comment ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$complex_ccman</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">包含复标度（complex-scaled）及 CAP 增强的 EOM-CC</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">计算参数（第 <a class="ltx_ref" href="topic_eomcc.html" title="7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$ecp</em></td>
<td class="ltx_td ltx_align_left">用户定义的有效核势（Effective Core Potentials, ECP）（第 <a class="ltx_ref" href="subsec_ECP-userdef.html" title="8.10.5 User-Defined ECPs ‣ 8.10 Effective Core Potentials (ECPs) ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.10.5</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efei</em></td>
<td class="ltx_td ltx_align_left">在几何优化中施加外力（第 <a class="ltx_ref" href="sec_EFEI.html" title="9.5.1 Application of External Forces ‣ 9.5 Application of Pressure and Forces ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.5.1</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efp_fragments</em></td>
<td class="ltx_td ltx_align_left">指定有效碎片势（EFP）碎片的标签与位置（第 <a class="ltx_ref" href="sect_efp.html" title="11.5 Effective Fragment Potential Method ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.5</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$efp_params</em></td>
<td class="ltx_td ltx_align_left">包含用户定义的有效碎片参数（第 <a class="ltx_ref" href="sect_efp.html" title="11.5 Effective Fragment Potential Method ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.5</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$empirical_dispersion</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的范德华参数，用于 DFT 色散校正</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">（第 <a class="ltx_ref" href="subsec_DFT-D.html" title="5.7.3 Empirical Dispersion Corrections: DFT-D ‣ 5.7 DFT Methods for van der Waals Interactions ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.7.3</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$eom_user_guess</em></td>
<td class="ltx_td ltx_align_left">EOM-CC 计算的用户自定义初始猜测（第 <a class="ltx_ref" href="topic_eomcc.html" title="7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$external_charges</em></td>
<td class="ltx_td ltx_align_left">指定外部点电荷及其位置（第 <a class="ltx_ref" href="A2.S1.SS2.html#sec:externalcharges" title="B.1.2.7 $external_charges ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.7</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$fde</em></td>
<td class="ltx_td ltx_align_left">指定冻结密度嵌入（frozen density embedding）选项（第 <a class="ltx_ref" href="sect_FDET_methods.html" title="11.7 Frozen-Density Embedding Theory ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.7</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$force_field_params</em></td>
<td class="ltx_td ltx_align_left">QM/MM 计算的力场（force-field）参数（第 <a class="ltx_ref" href="sec_QMMM.html" title="11.3 Stand-Alone QM/MM Calculations ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.3</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$geom_opt</em></td>
<td class="ltx_td ltx_align_left"><span class="ltx_text ltx_font_smallcaps">Libopt3</span> 计算的几何优化控制项（第 <a class="ltx_ref" href="sec_geom_opt_controls.html" title="9.2 Geometry Optimization Job Controls ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$harmonic_opt</em></td>
<td class="ltx_td ltx_align_left">采用软谐约束（soft harmonic constraints）进行优化的信息（第 <a class="ltx_ref" href="subsec_HarmonicConfiner.html" title="9.4.7 Atomic Confining Potentials as Alternatives to Constrained Optimization ‣ 9.4 Constrained Optimization ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.4.7</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$intracule</em></td>
<td class="ltx_td ltx_align_left">电子内对（intracule）参数（第 <a class="ltx_ref" href="sect_intracules.html" title="13.2 Intracules ‣ Chapter 13 Specialized Topics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">13.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$isotopes</em></td>
<td class="ltx_td ltx_align_left">用于振动计算的同位素替代（第 <a class="ltx_ref" href="ex_Isotope-Mass.html" title="10.8.2 Isotopic Substitutions and Changes in T and P ‣ 10.8 Harmonic Vibrational Analysis ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.8.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$localized_diabatization</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">将多个绝热（adiabatic）态混合为非绝热（diabatic）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">态所需的信息（第 <a class="ltx_ref" href="chap_properties.html" title="Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$magnet</em></td>
<td class="ltx_td ltx_align_left">与磁场相关响应性质（response properties）的作业控制（第 <a class="ltx_ref" href="sec_magnetman.html" title="10.11.4 Additional Magnetic Field-Related Properties ‣ 10.11 NMR and Other Magnetic Properties ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.11.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$mass</em></td>
<td class="ltx_td ltx_align_left">用户定义的原子质量（第 <a class="ltx_ref" href="topic_aimd.html" title="9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$multipole_field</em></td>
<td class="ltx_td ltx_align_left">外部多极场（multipole field）的细节（第 <a class="ltx_ref" href="A2.S1.SS2.html#sec:multipolefield" title="B.1.2.10 $multipole_field ‣ B.1.2 Descriptions of Some Q-Chem Input Sections ‣ B.1 Text Input Summary ‣ Appendix B Q-Chem Quick Reference ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">B.1.2.10</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$nbo</em></td>
<td class="ltx_td ltx_align_left">自然键轨道（Natural Bond Orbital, NBO）程序包的选项（第 <a class="ltx_ref" href="sect_NBO.html" title="10.3.1 Interface to the NBO Package ‣ 10.3 Orbital Analysis ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.3.1</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$occupied</em></td>
<td class="ltx_td ltx_align_left">指定应被占据的初始猜测轨道（第 <a class="ltx_ref" href="sect_occupied.html" title="4.4.4 Modifying the Occupied Molecular Orbitals ‣ 4.4 SCF Initial Guess ‣ Chapter 4 Self-Consistent Field Ground-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">4.4.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$opt</em></td>
<td class="ltx_td ltx_align_left">几何优化的约束定义（第 <a class="ltx_ref" href="sec_constrained_opt.html" title="9.4 Constrained Optimization ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$pcm</em></td>
<td class="ltx_td ltx_align_left">极化连续介质模型（polarizable continuum models, PCM）的作业控制（第 <a class="ltx_ref" href="subsec_PCM_job_control.html" title="11.2.4 PCM Job Control ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$plots</em></td>
<td class="ltx_td ltx_align_left">在网格点上生成绘图信息（第 <a class="ltx_ref" href="sect_plots.html" title="10.5 Visualizing and Plotting Volumetric Quantities ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.5</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_active_modes</em></td>
<td class="ltx_td ltx_align_left ltx_border_l" rowspan="3">准经典轨迹（quasi-classical trajectory）计算所需信息（第 <a class="ltx_ref" href="subsec_QCT.html" title="9.9.6 Quasi-Classical Molecular Dynamics ‣ 9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9.6</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_vib_distribution</em></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qct_vib_phase</em></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$qm_atoms</em></td>
<td class="ltx_td ltx_align_left">为 QM/MM 计算指定量子力学（QM）区域（第 <a class="ltx_ref" href="sec_QMMM.html" title="11.3 Stand-Alone QM/MM Calculations ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.3</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$response</em></td>
<td class="ltx_td ltx_align_left">广义响应求解器（generalized response solver）的作业控制（第 <a class="ltx_ref" href="sec_GeneralResponseTheory.html" title="10.14 General Response Theory ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.14</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$solvent</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">隐式溶剂模型的额外参数与变量</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">（第 <a class="ltx_ref" href="topic_solvation.html" title="11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$smx</em></td>
<td class="ltx_td ltx_align_left">SM$x$ 隐式溶剂模型的作业控制（第 <a class="ltx_ref" href="ex_SMx-User-Solvent.html" title="11.2.9 SM x Models ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.9</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$spin-spin</em></td>
<td class="ltx_td ltx_align_left">自旋-自旋耦合计算中要包含的原子编号（第 <a class="ltx_ref" href="sec_magnetic_NMR.html#subsec:mopropmanNMRJobControl" title="10.11.2.2 NMR Job Control and Examples ‣ 10.11.2 NMR Chemical Shifts and J-Couplings ‣ 10.11 NMR and Other Magnetic Properties ‣ Chapter 10 Molecular Properties and Analysis ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">10.11.2.2</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$swap_occupied_virtual</em></td>
<td class="ltx_td ltx_align_left">需要进行占据/虚轨道交换的初始猜测轨道（第 <a class="ltx_ref" href="sect_occupied.html" title="4.4.4 Modifying the Occupied Molecular Orbitals ‣ 4.4 SCF Initial Guess ‣ Chapter 4 Self-Consistent Field Ground-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">4.4.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$svp</em></td>
<td class="ltx_td ltx_align_left">等密度（iso-density）SS(V)PE 模块的特殊参数（第 <a class="ltx_ref" href="subsec_SS(V)PE.html" title="11.2.6 Isodensity Implementation of SS(V)PE ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.6</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$svpirf</em></td>
<td class="ltx_td ltx_align_left">等密度 SS(V)PE 模块的初始猜测（第 <a class="ltx_ref" href="subsec_SS(V)PE.html" title="11.2.6 Isodensity Implementation of SS(V)PE ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.6</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" rowspan="2"><em class="ltx_emph ltx_font_italic">$van_der_waals</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">用户定义的原子半径，用于朗之万偶极子溶剂化（第 <a class="ltx_ref" href="subsec_LD.html" title="11.2.10 Langevin Dipoles Model ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.10</span></a> 节）</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_l">以及 PCM（第 <a class="ltx_ref" href="topic_pcm-em.html" title="11.2.3 Polarizable Continuum Models ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.3</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$velocity</em></td>
<td class="ltx_td ltx_align_left">AIMD 计算中用户定义的原子核速度（第 <a class="ltx_ref" href="topic_aimd.html" title="9.9 Ab Initio Molecular Dynamics ‣ Chapter 9 Exploring Potential Energy Surfaces: Searches for Critical Points and Molecular Dynamics ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">9.9</span></a> 章）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$xc_functional</em></td>
<td class="ltx_td ltx_align_left">用户定义的密度泛函理论（DFT）交换-关联泛函（第 <a class="ltx_ref" href="sect_userxc.html" title="5.3.7 User-Defined Density Functionals ‣ 5.3 Overview of Available Functionals ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.3.7</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$xdm</em></td>
<td class="ltx_td ltx_align_left">XDM（交换-偶极子模型，Exchange-Dipole Model）色散方法的作业控制（第 <a class="ltx_ref" href="sect_XDM.html" title="5.7.4 Exchange-Dipole Model (XDM) ‣ 5.7 DFT Methods for van der Waals Interactions ‣ Chapter 5 Density Functional Theory ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">5.7.4</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left"><em class="ltx_emph ltx_font_italic">$zbasis</em></td>
<td class="ltx_td ltx_align_left">用户定义的复基组（complex basis set）信息（第 <a class="ltx_ref" href="sect_zbas.html" title="8.7 Complex Basis Sets ‣ Chapter 8 Basis Sets and Effective Core Potentials ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">8.7</span></a> 节）。</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_bb" rowspan="2"><em class="ltx_emph ltx_font_italic">$2pa</em></td>
<td class="ltx_td ltx_align_left ltx_border_l">双光子吸收（two-photon absorption）计算的额外参数</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_bb ltx_border_l">（第 <a class="ltx_ref" href="sec_EOMGRAD.html#sec:2PA" title="7.9.21.6 Transition Moments and Cross Sections for Two-Photon Absorption within EOM-EE-CCSD ‣ 7.9.21 Analytic Gradients and Properties for CCSD and EOM-XX-CCSD ‣ 7.9 Coupled-Cluster Excited-State and Open-Shell Methods ‣ Chapter 7 Open-Shell and Excited-State Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">7.9.21.6</span></a> 节）。</td>
</tr>
</tbody>
</table>

**任何 **Q-Chem** 输入文件中都必须包含 *$rem* 与 *$molecule* 这两个关键字**

由于每个关键字的功能各不相同，为适应这些差异，各特定关键字所要求的格式也略有不同（格式要求汇总于附录 [B](../app_b_quickref/app_quick_ref.md)）。不过，由于输入文件中的每个关键字都是由程序独立查找的，因此 **Q-Chem** 输入文件的整体格式要求并不十分严格。例如，*$molecule* 区段并不必出现在输入文件的最开头。

> **注：
> 
> (1) 用户可以按任意顺序输入各关键字区段。
> (2) 每个关键字区段都必须以 *$end* 关键字结束。
> (3) 必须包含 *$rem* 和 *$molecule* 区段。
> (4) 输入文件中并非需要包含所有关键字。
> (5) 每个关键字区段的说明见附录 [B](../app_b_quickref/app_quick_ref.md)。
> (6) 整个 **Q-Chem** 输入不区分大小写。
> **

**Q-Chem** 输入的另一普遍特征在于，实际上存在四种输入来源：

- 用户输入文件（必需）
- `$HOME` 中的 `.qchemrc` 文件（可选）
- `$QC/config` 中的 `preferences` 文件（可选）
- 程序内部默认值与计算结果（内置）

优先级顺序如上所示，*i.e.*，该输入机制提供了面向*所有*用户的程序默认值覆盖、面向*单个*用户的默认值覆盖，当然，用户提供的输入文件会覆盖所有默认值。有关 `.qchemrc` 和 `preferences` 的详细信息，请参阅第 [2.1.6](../ch02_install/sect_customization.md) 节。目前，**Q-Chem** 在 `.qchemrc` 和 `preferences` 文件中仅支持 *$rem* 关键字。

一般而言，用户需要在 *$molecule* 和 *$rem* 关键字区段中输入变量，并建议添加 *$comment* 以便日后查阅。其他关键字输入的必要性将在整本手册中逐渐体现。
