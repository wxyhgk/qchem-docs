---
title: "7.9.3 EOM-XX-CCSD and CI Suite of Methods"
---

## 7.9.3 EOM-XX-CCSD and CI Suite of Methods

(July 4, 2026)

**Q-Chem** features the most complete set of EOM-CCSD models,[[729]](../bib_references/bib.md#bib760)

enabling accurate, robust, and efficient calculations of electronically excited
states (EOM-EE-CCSD or EOM-EE-OD);
[[1228]](../bib_references/bib.md#bib1283)
;
ground and excited states of diradicals and triradicals (EOM-SF-CCSD and
EOM-SF-OD);[[726]](../bib_references/bib.md#bib757)
 ionization potentials and
electron attachment energies, as well as problematic doublet radicals and
cation or anion radicals
(EOM-IP/EA-CCSD).[[1260]](../bib_references/bib.md#bib1313)
 The EOM-DIP-CCSD, EOM-2SF-CCSD, and EOM-DEA-CCSD
methods are available as well. Conceptually, EOM is very
similar to configuration interaction (CI): target EOM states are found by
diagonalizing the similarity transformed Hamiltonian $\bar{H}=e^{-T}He^{T}$,

<a id="eq747"></a>
$$
\bar{H}R=ER, \tag{7.97}
$$

where $T$ and $R$ are general excitation operators with respect to the
reference determinant $|\Phi_{0}\rangle$. In the EOM-CCSD models, $T$ and $R$ are
truncated at single and double excitations, and the amplitudes $T$ satisfy the
CC equations for the reference state $|\Phi_{0}\rangle$:

<a id="A3.S8.EGx55"></a>
$$
\displaystyle\langle\Phi_{i}^{a}|\bar{H}|\Phi_{0}\rangle \tag{7.98}
$$

The computational scaling of EOM-CCSD and CISD methods is identical, *i.e.*,
${\cal{O}}({N^{6}})$, however EOM-CCSD is numerically superior to CISD because
correlation effects are “folded in” in the transformed Hamiltonian, and
because EOM-CCSD is rigorously size-intensive.

By combining different types of excitation operators and references
$|\Phi_{0}\rangle$, different groups of target states can be accessed as explained
in Fig. [7.2](Ch7.S9.SS2.md#fig:EOM). For example, electronically excited states can be
described when the reference $|\Phi_{0}\rangle$ corresponds to the ground state wave
function, and operators $\hat{R}$ conserve the number of electrons and a total
spin.[[1289]](../bib_references/bib.md#bib1345)
 In the ionized/electron attached EOM
models,[[1291]](../bib_references/bib.md#bib1346)
 operators $R$ are not electron
conserving (*i.e.*, include different number of creation and annihilation
operators)—these models can accurately treat ground and excited states of
doublet radicals and some other open-shell systems. For example, singly ionized
EOM methods, *i.e.*, EOM-IP-CCSD and EOM-EA-CCSD, have proven very useful for
doublet radicals whose theoretical treatment is often plagued by symmetry
breaking. The EOM-SF method[[726]](../bib_references/bib.md#bib757)
 in
which the excitation operators include spin-flip allows one to access
diradicals, triradicals, and bond-breaking.

Finally, EOM-DIP and EOM-DEA methods also provide access to similar classes of
strongly correlated systems.

**Q-Chem** features EOM-EE/SF/IP/EA/DIP/DEA /DSF-CCSD
methods for both closed and open-shell references (RHF/UHF/ROHF),
including frozen core/virtual options. For EE, SF, IP, and EA, a more
economical flavor of EOM-CCSD is available (EOM-MP2 family of methods). All
EOM models take full advantage of molecular point group symmetry. Analytic
gradients are available for RHF and UHF references, for the full orbital space,
and with frozen core/virtual orbitals.[[804]](../bib_references/bib.md#bib838)
 Properties
calculations (permanent and transition dipole moments and angular momentum projections,
SOCs and NACs, $\langle\hat{S}^{2}\rangle$, $\langle\hat{R}^{2}\rangle$, *etc.*)
are also available. The current implementation of the
EOM-XX-CCSD methods enables calculations of medium-size molecules, *e.g.*, up to
15–25 heavy atoms. Using RI approximation (Section [6.12.10](../ch06_correlation/topic_ricc.md)) or Cholesky
decomposition (Section [6.12.11](../ch06_correlation/topic_cdcc.md)) helps to reduce integral transformation time and
disk usage enabling calculations on much larger systems. EOM-MP2 and EOM-MP2t
variants are also less computationally demanding. Even more robust yet computationally
effective option is afforded by RI-CC2 (Section [7.9.4](sec_eomcc2.md)).
The computational cost of
EOM-IP/SF calculations can be considerably reduced (with negligible decline in
accuracy) by truncating virtual orbital space using FNO scheme (see Section [7.9.14](sec_FNO.md)).

## 7.9.3.1 EOM-CC and Projection-Based Embedding

Due to the high computational cost of this method, the application of EOM-CCSD to large systems is difficult in terms of both computational time and resources. One strategy to overcome this issue is to combine EOM-CC with projection-based embedding[[878]](../bib_references/bib.md#bib913)
. This method performs remarkably well for the calculation of ionized, core-ionized and valence excitation energies. Rydberg states are also described with sufficient accuracy, while it is not advised to employ projection-based embedding combined with EOM-EA-CCSD.
Theory and job commands for projection-based embedding are reported in Section [11.6](../ch11_env/sect_den_emb.md).

## 7.9.3.2 Legacy Features Available in CCMAN

The CCMAN module of **Q-Chem** includes two implementations of EOM-IP-CCSD. The
proper implementation[[1092]](../bib_references/bib.md#bib1137)
 is used by default is more
efficient and robust. The EOM_FAKE_IPEA keyword invokes is a pilot
implementation in which EOM-IP-CCSD calculation is set up by adding a very
diffuse orbital to a requested basis set, and by solving EOM-EE-CCSD equations
for the target states that include excitations of an electron to this diffuse
orbital. The implementation of EOM-EA-CCSD in CCMAN also uses this trick. Fake
IP/EA calculations are only recommended for Dyson orbital calculations and
debug purposes. CCMAN2 features proper implementations of EOM-IP and EOM-EA
(including Dyson orbitals).

A more economical CI variant of EOM-IP-CCSD, IP-CISD is also available in
CCMAN. This is an ${\cal{O}}({N^{5}})$ approximation of IP-CCSD, and can be used for geometry
optimizations of problematic doublet states.[[470]](../bib_references/bib.md#bib483)
