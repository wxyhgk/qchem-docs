---
title: "7.9.2 Excited States via EOM-EE-CCSD and EOM-CCSDT"
---

## 7.9.2 Excited States via EOM-EE-CCSD and EOM-CCSDT

(July 4, 2026)

One can describe electronically excited states at a level of theory similar to
that associated with coupled-cluster theory for the ground state by applying
either linear response[[699]](../bib_references/bib.md#bib730)
 or equation-of-motion[[1289]](../bib_references/bib.md#bib1345)

formalisms.
A number of groups have demonstrated that
excitation energies based on a coupled-cluster singles and doubles ground state
are generally very accurate for states that are primarily single electron
promotions from the ground state. The error observed in calculated excitation energies to such states
is typically 0.1–0.2 eV, with 0.3 eV as a conservative estimate, including
both valence and Rydberg excited states. This, of course, assumes that a basis
set large and flexible enough to describe the valence and Rydberg states is
employed. The accuracy of excited state coupled-cluster methods deteriorates
for excited states that involve a substantial double excitation character,
where errors may be 1 eV or even more. Such errors arise because the
description of electron correlation of an excited state with substantial double
excitation character requires higher truncation of the excitation operator.
The description of these states can be improved by including triple
excitations, as in EOM(2,3). Including triple excitations at CC as well as
EOM levels results in the
the EOM-CCSDT method (see Section [7.9.23](subsec_EOM-CCSDT.md)
for details) in which, the higher-level correlation treatment is
incorporated in a rigorous and balanced way.

**Q-Chem** includes coupled-cluster methods for excited states based on the
coupled cluster singles and doubles (CCSD) and the
singles, doubles and triples (CCSDT) methods described above.

CCMAN code
also includes the optimized orbital coupled-cluster doubles (OD) variant. OD
excitation energies have been shown to be essentially identical in numerical
performance to CCSD excited states.[[725]](../bib_references/bib.md#bib756)

These methods, while far more computationally expensive than TDDFT, are
nevertheless useful as proven high accuracy methods for the study of excited
states of small molecules. Moreover, they are capable of describing both
valence and Rydberg excited states, as well as states of a charge-transfer
character. Also, when studying a series of related molecules it can be very
useful to compare the performance of TDDFT and coupled-cluster theory for at
least a small example to understand its performance. Along similar lines, the
CIS(D) method described earlier as an economical correlation energy correction
to CIS excitation energies is in fact an approximation to EOM-CCSD.
RI-CC2/EOM-CC2 is another popular approximation to EOM-CCSD, which
enables calculations of much larger systems.
It is
useful to assess the performance of CIS(D) or CC2 for a class of problems by
benchmarking against the full coupled-cluster treatment. Finally, **Q-Chem**
includes extensions of EOM methods to treat ionized or electron attachment
systems, as well as di- and triradicals.

![Figure 7.2: In the EOM formalism, target states $\Psi$ are described as
excitations from a reference state $\Psi_{0}$ : $\Psi=R\Psi_{0}$ , where $R$ is a
general excitation operator. Different EOM models are defined by choosing the
reference and the form of the operator $R$ . In the EOM models for
electronically excited states (EOM-EE, upper panel), the reference is the
closed-shell ground state Hartree–Fock determinant, and the operator $R$ conserves the number of $\alpha$ and $\beta$ electrons. Note that
two-configurational open-shell singlets can be correctly described by EOM-EE
since both leading determinants appear as single electron excitations. The
second and third panels present the EOM-IP/EA models. The reference
states for EOM-IP/EA are determinants for $N+1$ / $N-1$ electron
states, and the excitation operator $R$ is ionizing or electron-attaching,
respectively. Note that both the EOM-IP and EOM-EA sets of determinants are
spin-complete and balanced with respect to the target multi-configurational
ground and excited states of doublet radicals. The EOM-SF method (the
lowest panel) employs the high-spin triplet state as a reference, and the
operator $R$ includes spin-flip, i.e. , does not conserve the number of $\alpha$ and $\beta$ electrons. All the determinants present in the target
low-spin states appear as single excitations, which ensures their balanced
treatment both in the limit of large and small HOMO/LUMO gaps. Other EOM
methods available in Q-Chem are EOM-2SF, EOM-DIP, and EOM-DEA.](../assets/eom_formalism_figure.png)

*Figure 7.2: In the EOM formalism, target states $\Psi$ are described as
excitations from a reference state $\Psi_{0}$ : $\Psi=R\Psi_{0}$ , where $R$ is a
general excitation operator. Different EOM models are defined by choosing the
reference and the form of the operator $R$ . In the EOM models for
electronically excited states (EOM-EE, upper panel), the reference is the
closed-shell ground state Hartree–Fock determinant, and the operator $R$ conserves the number of $\alpha$ and $\beta$ electrons. Note that
two-configurational open-shell singlets can be correctly described by EOM-EE
since both leading determinants appear as single electron excitations. The
second and third panels present the EOM-IP/EA models. The reference
states for EOM-IP/EA are determinants for $N+1$ / $N-1$ electron
states, and the excitation operator $R$ is ionizing or electron-attaching,
respectively. Note that both the EOM-IP and EOM-EA sets of determinants are
spin-complete and balanced with respect to the target multi-configurational
ground and excited states of doublet radicals. The EOM-SF method (the
lowest panel) employs the high-spin triplet state as a reference, and the
operator $R$ includes spin-flip, i.e. , does not conserve the number of $\alpha$ and $\beta$ electrons. All the determinants present in the target
low-spin states appear as single excitations, which ensures their balanced
treatment both in the limit of large and small HOMO/LUMO gaps. Other EOM
methods available in Q-Chem are EOM-2SF, EOM-DIP, and EOM-DEA.*
