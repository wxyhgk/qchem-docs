---
title: "7.10.10 Properties and Visualization"
---

## 7.10.10 Properties and Visualization

(July 4, 2026)

The calculation of excited, ionized and electron-attached states using the **ADCman** module yields by default
the usual excitation energies, ionization potentials and electron-attachment energies
together with the respective excitation amplitudes, as well as the
transition dipole moments, oscillator strengths (or pole strengths in case of IP- and
EA-ADC calulations), and the norm of the doubles
part of the amplitudes (if applicable). In addition, the calculation of
excited, ionized and electron-attached state properties, like dipole moments, and transition properties
between these states can be requested by setting the *$rem* variables
ADC_PROP_ES and ADC_PROP_ES2ES, respectively.

Resonant
two-photon absorption cross-sections of excited states can be computed as
well, using either sum-over-states expressions or the matrix inversion
technique. The calculation via sum-over-state expressions is automatically
activated, if ADC_PROP_ES2ES is set. The accuracy of the results,
however, strongly depends on the number of states which are included in the
summation, *i.e.* the number of states computed. At least, 20-30 excited states
(per irreducible representation) are required to yield useful results for the
two-photon absorption cross-sections. Alternatively, the resonant two-photon
absorption cross-sections can be calculated by setting ADC_PROP_TPA
to TRUE. In this case, the computation of a large number of excited
states is avoided and there is no dependence on the number of excited states.
Instead, an additional linear matrix equation has to be solved for every
excited state for which the two-photon absorption cross-section is computed.
Thus, the obtained resonant two-photon absorption cross-sections are usually
more reliable. The quantity printed out is the microscopic cross-section (also
known as rotationally averaged 2PA strength). Specifically, the value
$30\times\delta^{m}_{TP}$ is printed out where $\delta^{m}_{TP}$ is defined in
Eq. (13) of Ref. [[1494]](../bib_references/bib.md#bib1555)
.
The quantity printed out is the microscopic cross-section (also known as rotationally averaged 2PA strength).
Specifically, the value $30\times\delta^{m}_{TP}$ is printed out where $\delta^{m}_{TP}$ is defined in Eq. (13) of Ref. [[1494]](../bib_references/bib.md#bib1555)
.

Furthermore, the **ADCman** module allows for the detailed analysis of the
excited states and export of various types of excited state related orbitals
and densities. This can be activated by setting the keyword
STATE_ANALYSIS. Details on the available analyses and export options
can be found in section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md).
