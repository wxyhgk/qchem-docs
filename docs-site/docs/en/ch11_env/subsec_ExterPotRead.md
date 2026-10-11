---
title: "11.7.5 Read an External Potential From a File"
---

## 11.7.5 Read an External Potential From a File

(July 4, 2026)

Users can introduce an external potential affecting the active molecule in a DFT calculation,
representing an embedding environment. Any functional can be used. To invoke the reading of
an external potential, users must set the key-word **PROJ_CAP = -10** in the $rem section,
and the file named **external_potential.grid** must be present at the same directory.
The external potential must be expressed at the same exact grid points. The potential file includes only the potential
values in *atomic coordinates*. As a preparation step the grid points can be printed using libqints by setting the flag
**use_libqints = true**. A related published work[[232]](../bib_references/bib.md#bib232)
 can also be read
in order to see its usage in different DFT functional.
