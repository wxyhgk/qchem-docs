---
title: "11.5.5 Extension to Macromolecules: Fragmented EFP Scheme"
---

## 11.5.5 Extension to Macromolecules: Fragmented EFP Scheme

(July 4, 2026)

Macromolecules such as proteins or DNA present a large number of electronic
structure problems (photochemistry, redox chemistry, reactivity) that can be
described within QM/EFP framework. EFP has been extended to deal with such
complex systems via the so-called fragmented EFP scheme (fEFP). The current
**Q-Chem** implementation allows one to (i) compute interaction energy between a
ligand and a macromolecule (both represented by EFP) and (ii) to calculate the
excitation energies, ionization potentials, electronic affinities of a QM
moiety interacting with a fEFP macromolecule using QM/EFP scheme (see
Section [11.5.3](sec_EOM-EFP.md)). In the present implementation, the ligand cannot
be covalently bound to the macromolecule.

There are multiple ways to cut a large molecule into units depending on the
position of the cut between two covalently bound residues. An obvious way to
cut a protein is to cut through peptide bonds such that each fragment
represents one amino acid. Alternatively, one can cut bonds between two atoms of
the same nature (carbonyl and carbon-$\alpha$ or carbon-$\alpha$ and the first
carbon of the side chain). The user can choose the most appropriate way to cut.

Consider a protein ($P$) consisting of $N$ amino acids, $A_{1}A_{2}\ldots A_{N}$, and
is split into $N$ fragments ($A_{i}$). The fragments can be saturated by either
“hydrogen link atom” (HLA),[[1259]](../bib_references/bib.md#bib1311)
 or by mono-valent groups of atoms
from the neighboring fragment(s), called “cap link atom” (CLA) hereafter. If
fragments are capped using the HLA scheme, the hydrogen is located along the
peptide bond axis and at the distance corresponding to the equilibrium bond
length of a CH bond:

<a id="eq:hla"></a>
$$
P=A_{1}H+\sum_{i=2}^{N-1}HA_{i}H+HA_{N} \tag{11.89}
$$

In the CLA scheme, the cap has exactly the same geometry as the respective
neighboring group. If the cuts are made through peptide bonds (one fragment is
one amino acid), the caps ($C^{i}$) are either an aldehyde to saturate the -N(H)
end of the fragment, or an amine to saturate the -C(=O) extremity of the
fragment.

<a id="eq:cla"></a>
$$
P=A_{1}C^{2}+\sum_{i=2}^{N-1}C^{i-1}A_{i}C^{i+1}+C^{N-1}A_{N} \tag{11.90}
$$

**Q-Chem** provides a two-step script, `prefefp.pl`, located in
`$QC/bin` which takes a PDB file and breaks it into capped fragments in
the **gamess** format, such that the EFP parameters for these capped
fragments can be generated, as explained in Section [11.5.11](sec_fefp-param.md). As
the EFP parameters are generated for each capped fragment, the neighboring
fragments have duplicated parameter points (overlapping areas) in both the HLA
and CLA schemes due to the overlapping caps. Since multipole expansion points
and polarizability expansion points are computed on each capped residue by the
standard procedure, the multipole (and damping terms) and polarizabilities need
to be removed ($C^{\emptyset}$) from the overlapping areas.

Equations ([11.89](#eq:hla)) and ([11.90](#eq:cla)) become:

<a id="eq:hcla"></a>
$$
P=A_{1}C^{\emptyset}+\sum_{i=2}^{N-1}C^{\emptyset}A_{i}C^{\emptyset}+C^{\emptyset}A_{N} \tag{11.91}
$$

The details concerning this removing procedure are presented in
Section [11.5.11](sec_fefp-param.md).

Once these duplicate parameters are removed from the EFP parameters of the
capped fragments, the EFP-EFP and QM-EFP calculations can be conducted as
usual.

Currently, fEFP includes electrostatic and polarization contributions, which
appear in EFP(ligand)/fEFP(macromolecule) and in QM/fEFP
calculations (note that the QM part is not covalently bound to the
macromolecule). Consequently, the total interaction energy
($E^{\text{tot}}$) between a ligand ($L$) and a protein ($P$) divided into
fragments is:

<a id="eq:fefp-tot"></a>
$$
E^{\text{tot}}(P-L)=E^{\text{elec}}(P-L)+E^{\text{pol}}(P-L) \tag{11.92}
$$

The electrostatics is an additive term; its contribution to fragment-fragment
and ligand-fragment interaction is computed as follows:

<a id="eq:la-fefp-elec"></a>
$$
E^{\text{elec}}(P-L)=\sum_{i}^{N}{E^{\text{elec}}\left(C^{\emptyset}A_{i=1}C^{\emptyset}-L\right)}\;. \tag{11.93}
$$

The polarization contribution in an EFP system (no QM) is:

<a id="eq:pol-efpfefp"></a>
$$
E^{\text{pol}}(P-L)=-\frac{1}{2}\sum_{k\in P,L}\mu^{k}F^{\text{mult},k}+\frac{1}{2}\sum_{k\in P}\mu^{k}F^{\text{mult},k}\;. \tag{11.94}
$$

The first term is the polarization energy obtained upon convergence of the
induced dipoles of the ligand ($\mu^{k}_{\text{efp}}(L)$) and all fragments
($\mu^{k}_{\text{fefp}}(A_{i})$).
The system is thus fully polarized, all fragments (A${}_{i}$ or L) are polarizing
each other until self-consistency:

<a id="A3.S8.EGx110"></a>
$$
\displaystyle\mu^{k}_{\text{efp}}(L) \tag{11.95}
$$

The second term of Eq. ([11.94](#eq:pol-efpfefp)) is the polarization of the
protein by itself; this value has to be subtracted once the induced dipoles
[Eq. ([11.95](#eq:pol-mu-fefp))] converged.

The LA scheme is available to perform QM/fEFP job. In this situation the
fEFP has to include a macromolecule (covalent bond between fragments). This
scheme is not able yet to perform QM/fEFP/EFP in which a
macromolecule and solvent molecules would be described at the EFP level of theory.

In addition to the HLA and CLA schemes, **Q-Chem** also features the
*molecular fragmentation with conjugated caps* (MFCC)
approach,[[1542]](../bib_references/bib.md#bib1608)

which avoids the issue of overlapping of saturated fragments.
The MFCC procedure consists of a summation
over the interactions between a ligand and capped residues (CLA scheme) and a
subtraction over the interactions of merged caps ($C^{i+1}C^{i-1}$)
with the ligand.[[568]](../bib_references/bib.md#bib578)
 (These are the so-called
so-called conjugated caps or “concaps”.[[537]](../bib_references/bib.md#bib551)
)
$N-1$ concap fragments are actually used to subtract the overlapping effect.

<a id="eq:mfcc"></a>
$$
P=A_{1}C^{2}+\sum_{i=2}^{N-1}C^{i-1}A_{i}C^{i+1}+C^{N-1}A_{N}-\sum_{i}^{N-1}C^{i+1}C^{i-1} \tag{11.97}
$$

In this scheme the contributions due to overlapping caps simply cancel out and
the EFP parameters do not need any modifications, in contrast to the HLA or CLA
procedures. However, the number of parameters that need to be generated is
larger, namely, $N$ capped fragments and $N-1$ concaps.

The MFCC electrostatic interaction energy is given as the sum of the
interaction energy between each capped fragment ($C^{i-1}A_{i}C^{i+1}$) and
the ligand minus the interaction energy between each concap ($C^{i-1}C^{i+1}$) and the ligand:

<a id="eq:mfcc-fefp-elec"></a>
$$
E^{\text{elec}}(P-L)=\sum_{i}^{N}{E^{\text{elec}}\left(C^{i-1}A_{i}C^{i+1}-L\right)}-\sum_{i}^{N-1}{E^{\text{elec}}\left(C^{i-1}C^{i+1}-L\right)} \tag{11.98}
$$

The main advantage of MFCC is that the multipole expansion obtained on each
capped residue or concap are kept during the $E^{\text{elec}}(P-L)$ calculation.
In the present implementation, there are no polarization contributions. The
MFCC scheme is not yet available for QM/fEFP.
