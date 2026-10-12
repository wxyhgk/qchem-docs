---
title: "11.5.7 Running EFP Jobs"
---

## 11.5.7 Running EFP Jobs

(July 4, 2026)

The current version supports single point calculations in systems consisting of
($i$) *ab initio* and EFP regions (QM/MM); or ($ii$) EFP region
only.
Constrained QM region geometry optimziation is enabled for electrostatic embedding
QM/MM model, as described in [11.5.6](sec_EFP-QMMM.md).

The *ab initio* region can be described by conventional quantum
methods like HF, DFT, or correlated methods including methods for the excited
states [CIS, CIS(D), TDDFT, ADC, EOM-CCSD methods]. Theoretical details on the
interface of EFP with EOM-CCSD and CIS(D) can be found in
Refs. [[1272]](../bib_references/bib.md#bib1325)
 and [[711]](../bib_references/bib.md#bib743)
. ADC/EFP models
are described in Ref. [[1230]](../bib_references/bib.md#bib1285)
.

!!! note "Note"
    EFP provides both implicit (through orbital response) and explicit (as
    instantaneous response of the polarizable EFP fragments) corrections to the
    electronic excited states. EFP-modified excitation energies are printed in the
    property section of the output.


Electrostatic, polarization, exchange-repulsion, and dispersion contributions
are calculated between EFs; only electrostatic and polarization terms are
evaluated between *ab initio* and EF regions.

The *ab initio* region is specified by regular **Q-Chem** input using
*$molecule* and *$rem* sections. In calculations with no QM part, the
*$molecule* section should contain a dummy atom (for example, helium).

Positions of EFs are specified in the *$efp_fragments* section. Two geometry
formats, controlled by EFP_COORD_XYZ keyword, are available for fragments,
the Euler angle format and the XYZ format. In the
Euler angle format, each line in this section contains the information on an
individual fragment: fragment’s name and position, specified by center-of-mass
coordinates ($x$, $y$, $z$) and the Euler rotation angles ($\alpha$, $\beta$,
$\gamma$) relative to the fragment frame, *i.e.*, the coordinates of the
standard fragment provided in the fragment library. In the XYZ format,
the name of the fragment is provided on the first line followed by three lines
specifying names and ($x$, $y$, $z$) coordinates of the first three atoms of the fragment.
