---
title: "7.11.7 Spin-flip CAS with Perturbative External Singles Corrections (casman)"
---

## 7.11.7 Spin-flip CAS with Perturbative External Singles Corrections (**casman**)

(July 4, 2026)

The **casman** module allows one to run spin-flip CAS-based calculations, with perturbative
corrections accounting for hole and particle excitations outside of the active space.
(For variational hole and particle excitations, please refer to the section on **librassf**.)
It also allows one to run with a limited number of spin-flips, which can be useful
for large transition metal complexes in which the maximum number of spin-flips
cannot be performed. For more details on this approach, please refer to the publication
by Mayhall and Head-Gordon.[[926]](../bib_references/bib.md#bib964)

**Q-Chem** has several built-in excitation schemes. To use these, simply set CORRELATION
to the appropriate value. The following methods are currently available:
SF-CAS, SF-CAS(h,p), SF-CAS(S), SF-CAS(2x), SF-CAS(3x), and SF-CAS(3x)+D.

Alternatively, if a custom method is desired, one can set CORRELATION = SF-CAS
and manually define the appropriate *$rem* variables as needed. Please see the section on **casman**
job control options for further details.
