---
title: "7.9.31 Interface with OpenFermion Package for Quantum Computing"
---

## 7.9.31 Interface with OpenFermion Package for Quantum Computing

(July 4, 2026)

**Q-Chem** provides a capability to dump all quantities required for interfacing with the OpenFermion package[[617]](../bib_references/bib.md#bib969)

(and similar softwares) for quantum computation. This feature is controlled by the PRINT_QIS keyword.
Setting it to TRUE activates the dump: Fock operator, two-electron integrals, and energies of molecular orbitals
are saved in separate files in the home directory. OpenFermion
(development version, soon to be checked into official github repository) contains an import module, which understands how to read these files, and several unit tests.
Example 7.9.31 illustrates this capability for water molecule.

!!! note "Note"
    Core should not be frozen.


### `PRINT_QIS`

> **Requests to dump stuff needed for OpenFermion.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Print stuff for QIS in user directory.
> * **Recommendation**: Beware of size of the files.

???+ example "Example 7.180: CCSD/STO-3G calculation of water molecule with print-out for OpenFermion."
    ```qchem
    $comment
    Water molecule in STO-3G basis
    $end
    
    $molecule
    0 1
      H    0.5355326   -0.0489506    0.7341984
      O    0.0563012    0.0114119   -0.1303093
      H   -0.9024750   -0.0253772    0.1144725
    $end
    
    $rem
    method = ccsd
    basis = sto-3g
    print_qis = true
    gui = 2
    n_frozen_core = 0
    $end
    ```
