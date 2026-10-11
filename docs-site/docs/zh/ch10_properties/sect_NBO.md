---
title: "10.3.1 Interface to the NBO Package"
---

## 10.3.1 Interface to the NBO Package

(July 4, 2026)

**Q-Chem** incorporates v. 5 of the Natural Bond Orbital (NBO) package for molecular
properties and wave function analysis,[[459]](../bib_references/bib.md#bib471)

and can interface to v. 6[[459]](../bib_references/bib.md#bib471)
 and v. 7[[460]](../bib_references/bib.md#bib473)
 of the NBO program as well.
The NBO5 package is invoked simply by setting NBO = TRUE in the *$rem* section
and is initiated after the SCF wave function is obtained.
If switched on for a geometry optimization, the NBO5 program will only be
invoked at the end of the last optimization step.

To use either NBO6 or NBO7, the desired version of the NBO program must be purchased, downloaded, and installed separately
from [nbo.chem.wisc.edu](https://nbo.chem.wisc.edu).
**Q-Chem** can then interface to an external version of the NBO program by:
(a) setting the `NBOEXE` environment variable appropriately, and
(b) setting both NBO = TRUE and NBO_EXTERNAL = TRUE in the *$rem*
section of the **Q-Chem** input file. Note that support for (and new downloads of) the NBO6 program were
discontinued in 2020. Existing copies should still interface to **Q-Chem**,
and the newer NBO7 program should interface in the same way. The older NBO5 program continues to be
a part of **Q-Chem** and the latter is what runs if NBO = TRUE is set without specifying NBO_EXTERNAL.

Users should consult the NBO User’s Manual for options and details relating to NBO calculations.
NBO analysis is also available for excited states calculated using CIS or
TDDFT. Excited-state NBO analysis is less well-developed, and users should be
aware that the convergence of the NBO search procedure may be less well-behaved
for excited states than it is for ground states. Excited state may require specification
of additional NBO parameters in the *$nbo* section that is described below.
Consult Ref. 

 for details and suggestions.

NBO

### `NBO`

> **Controls the use of the NBO package.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not invoke the NBO package.
>     * 1
>     * Do invoke the NBO package, for the ground state.
>     * 2
>     * Invoke the NBO package for the ground state, and also each
>     * CIS, RPA, or TDDFT excited state.
> * **Recommendation**: None

NBOMEMORY

### `NBOMEMORY`

> **Controls how much memory is allocated to Q-Chem ’s internal NBO (v. 5) package.**
>
> * **Type**: `INTEGER`
> * **Default**: `500000`
> * **Options**:
>     * $N$
>     * Allocate
>     * $N$
>     * double-precision words (=
>     * $8N$
>     * bytes).
> * **Recommendation**: This memory comes out of MEM_TOTAL .

The general format for passing options from **Q-Chem** to the NBO program is shown below:

> ```qchem
> $nbo
>    {NBO program keywords, parameters and options}
> $end
> ```

A few usage notes:

1. 1.

*$rem* variable NBO must be set to TRUE before the *$nbo* keyword is recognized.
2. 2.

**Q-Chem** does not support facets of the NBO package which require multiple job runs
3. 3.

Output of the NBOs can be triggered by the PRINT_ORBITALS
and MOLDEN_FORMAT keywords. In this case two MOLDEN sections are written to *outfile*.
The first one corresponds to the regular MOs, the second one to the NBOs.
4. 4.

Print-out of the full set of NAOs, NHOs, NBOs, and NLMOs can be triggered via
the PLOT keyword in the $nbo section.
The files of interest are `FILE.31` – `FILE.39` in `$QCSCRATCH/savename`.
These files can be opened by, *e.g.*, the **ChemCraft** and **JMol** programs.
5. 5.

**Q-Chem**’s internal implementation of NBO v. 5 has an upper limit of 300 atoms and 3,000 basis functions.

???+ example "Example 10.12: Basic input for NBO computation on formaldehyde.
The NBOs are printed to outfile in MolDen format and the full set of
files in native NBO format are written to $QCSCRATCH/savename ."
    ```qchem
    $molecule
       0 1
       C    0.000000    0.000000    0.523383
       O    0.000000    0.000000   -0.671856
       H    0.931138    0.000000    1.117280
       H   -0.931138    0.000000    1.117280
    $end
    
    $rem
       METHOD           pbe0
       BASIS            def2-sv(p)
       NBO              1
       PRINT_ORBITALS   true
       MOLDEN_FORMAT    true
    $end
    
    $nbo
       PLOT
    $end
    ```

???+ example "Example 10.13: NBO calculation that provides the canonical MOs in the natural atomic orbital (NAO) basis.
This is an easy way to establish the percentage AO character in each canonical MO."
    ```qchem
    $molecule
       0 1
       C    0.000000    0.000000    0.523383
       O    0.000000    0.000000   -0.671856
       H    0.931138    0.000000    1.117280
       H   -0.931138    0.000000    1.117280
    $end
    
    $rem
       METHOD           pbe0
       BASIS            def2-sv(p)
       NBO              true
    $end
    
    $nbo
       naomo
    $end
    ```
