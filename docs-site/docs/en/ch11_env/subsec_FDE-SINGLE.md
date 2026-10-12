---
title: "11.7.4 Single-Fragment Calculations"
---

## 11.7.4 Single-Fragment Calculations

(July 4, 2026)

FDE-Man allows the user to perform the embedding calculation by importing the embedding potential
in its atomic-orbital matrix representation. Consequently, all the specifications needed to construct
the embedding potential are no longer required. Additionally, the single-fragment mode is turned on
when only *one molecule* is given in the MOLECULE section.

### `import_vmat`

> **Import the embedding potential in AO matrix representation. The expected file name is FDE_vembmat.txt and does not have a header. All the keywords related to fragment B and the embedding potential will cause an error. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Read and add the embedding potential to the Fock matrix.
>     * `FALSE`: Don’t read the embedding potential, use other options.
> * **Recommendation**: None

!!! note "Note"
    This functionality is constructed as a separate module, only the import_rhoA and print_props=1
    options can be used with the single-fragment mode.


One can also use the single-fragment mode to obtain Mulliken and ChElPG charges from a density matrix.
In order to do that, one needs to import the density of fragment A, and set **charges** to one of the options below.
Importing the density matrix of fragment A is done as described previously.

### `charges`

> **Compute Mulliken or ChElPG charges from a density matrix in AO matrix representation. The import_rhoA option must be set to TRUE . INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `Mulliken`: Compute Mulliken charges from system A density matrix.
>     * `CHELPG`: Compute ChElPG charges from system A density matrix.
> * **Recommendation**: None
