---
title: "7.9.7 EOM-DIP-CCSD"
---

## 7.9.7 EOM-DIP-CCSD

(July 4, 2026)

Double-ionization potential (DIP) is another non-electron-conserving variant of
EOM-CCSD.[[740]](../bib_references/bib.md#bib773)

In DIP, target states are reached by detaching two electrons from the reference state:

<a id="DIP:WF"></a>

$$
\Psi_{k}=\hat{R}_{N-2}\Psi_{0}(N+2), \tag{7.100}
$$

and the excitation operator $R$ has the following form:

<a id="eq:R-IP"></a>

$$
\hat{R}=\frac{1}{2}\sum_{ij}r_{ij}ji+\frac{1}{6}\sum_{ijka}r_{ijk}^{a}a^{\dagger}kji. \tag{7.101}
$$

As a reference state in the EOM-DIP calculations one usually takes a
well-behaved closed-shell state. EOM-DIP is a useful tool for describing
molecules with electronic degeneracies of the type “$2n$-2 electrons in $n$
orbitals”. The simplest examples of such systems are diradicals
with two-electrons-in-two-orbitals pattern. Moreover, DIP is a preferred method
for four-electrons-in-three-orbitals wave functions or valence $2h$ states in Auger decay.

Accuracy of the EOM-DIP-CCSD method is similar to accuracy of other EOM-CCSD
models, *i.e.*, 0.1–0.3 eV. The scaling of EOM-DIP-CCSD is ${\cal{O}}({N^{6}})$,
analogous to that of other EOM-CCSD methods. However, its computational cost is
less compared to, *e.g.*, EOM-EE-CCSD, and it increases more slowly with the
basis set size. An EOM-DIP calculation is invoked by using
DIP_STATES, or DIP_SINGLETS and DIP_TRIPLETS.
In certain circumstances, the DIP_AA_STATES, DIP_BB_STATES,
DIP_BA_STATES keywords can be used.

!!! note "Note"
    The performance of EOM-DIP may be poor if the reference state is unstable
    with respect to electron detachment. See Section [7.9.13](sec_CAGE.md) for details.


!!! note "Note"
    In some applications of EOM-DIP-CCSD, only
    2$h$ operators were included in the EOM part. These calculations
    correspond to energies obtained from EOM_PRECONV_DOUBLES = TRUE
    calculation.

