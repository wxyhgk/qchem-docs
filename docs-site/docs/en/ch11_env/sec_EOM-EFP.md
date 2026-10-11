---
title: "11.5.3 Excited-State Calculations with EFP"
---

## 11.5.3 Excited-State Calculations with EFP

(July 4, 2026)

Interface of EFP with EOM-CCSD (both via CCMAN and CCMAN2), CIS, CIS(D),
TDDFT and ADC has been developed.[[1272]](../bib_references/bib.md#bib1325)

In the excited state calculations, the induced dipoles of the fragments are frozen
at their values consistent with the electronic ground state (HF or DFT). The resulting excitation energies account for a
zero-order response of the polarizable environment. Additionally, perturbative state-specific
polarization corrections [[1272]](../bib_references/bib.md#bib1325)
 are computed according to

<a id="eq:EOM-EFP-ene2"></a>

$$
\Delta E_{\text{pol}}=\frac{1}{2}\sum_{k}\sum_{a}^{x,y,z}\Bigl{[}-(\mu_{\text{ex},a}^{k}-\mu_{\text{gr},a}^{k})(F_{a}^{\text{mult},k}+F_{a}^{\text{nuc},k})\\
+(\tilde{\mu}_{\text{ex},a}^{k}F_{\text{ex},a}^{\text{ai},k}-\tilde{\mu}_{\text{gr},a}^{k}F_{\text{gr},a}^{\text{ai},k})-(\mu_{\text{ex},a}^{k}-\mu_{\text{gr},a}^{k}+\tilde{\mu}_{\text{ex},a}^{k}-\tilde{\mu}_{\text{gr},a}^{k})F_{\text{ex},a}^{\text{ai},k}\Bigr{]} \tag{11.77}
$$

where $F_{\text{gr}}^{\text{ai}}$ and $F_{\text{ex}}^{\text{ai}}$ are
the fields due to the reference state and excited-state electronic
densities, respectively. $\mu_{\text{gr}}^{k}$ and
$\tilde{\mu}_{\text{gr}}^{k}$ are the induced dipole and conjugated induced
dipole at the distributed polarizability point $k$ consistent with the
reference-state density, while $\mu_{\text{ex}}^{k}$ and
$\tilde{\mu}_{\text{ex}}^{k}$ are the induced dipoles corresponding to the excited state density.

The first two terms in Eq. ([11.77](#eq:EOM-EFP-ene2)) provide a difference of the
polarization energy of the QM/EFP system in the excited and ground
electronic states; the last term is the leading correction to the interaction
of the ground-state-optimized induced dipoles with the wave function of the
excited state. Thus, the excited states have both direct and indirect polarization
contributions. The indirect term comes from the orbital relaxation of the solute in the field due
to induced dipoles of the solvent. The direct term given by
Eq. ([11.77](#eq:EOM-EFP-ene2)) is the response of the polarizable environment to
the change in solute’s electronic density upon excitation. Note that the
direct polarization contribution can be very large (tenths of eV) in
EOM-IP/EFP since the electronic densities of the neutral and the ionized
species are very different.

An important advantage of the perturbative QM/EFP scheme is that it does
not compromise multi-state nature of single-referenced excited state calculations
and that the electronic wave functions
of the target states remain orthogonal to each other since they are obtained
with the same (reference-state) field of the polarizable environment. For
example, transition properties between these states can be calculated.

In the EOM-CCSD/EFP calculations, the reference-state CCSD equations for the $T$
cluster amplitudes are solved with the HF Hamiltonian modified by the
electrostatic and polarization contributions due to the effective fragments,
Eq. ([11.62](sec_theory.md#eq:H-EFP)). In the coupled-cluster calculation, the induced dipoles
of the fragments are frozen at their HF values.

EOM-CC/EFP scheme works with any type of the EOM excitation operator
$\hat{R}_{k}$ currently supported in **Q-Chem**, *i.e.*, spin-flipping (SF), excitation
energies (EE), ionization potential (IP), electron affinity (EA) (see
Section [7.9.18](../ch07_excited/sub_ccjobcontol.md) for details). However, direct polarization
correction requires calculation of one-electron density of the excited state,
and will be computed only for the methods with implemented one-electron properties.
