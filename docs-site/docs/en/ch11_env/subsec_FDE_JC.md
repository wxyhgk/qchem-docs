---
title: "11.7.3 FDE-Man Job Control"
---

## 11.7.3 FDE-Man Job Control

(July 4, 2026)

The FDE-Man job control with respect to embedding parameters is accomplished
via options in the *$fde* input section. The format of the *$fde* section
requires key and value pairs separated by a space character:

> ```qchem
> $fde
>    <Keyword>  <parameter>
> $end
> ```

!!! note "Note"
    The following job control variables belong *only* in the *$fde*
    section. Do not place them in the *$rem* section.


The supermolecular expansion (SE) uses the full basis set of the supersystem
for calculations on each fragment. Because of the computational cost this
option should only be used for small to medium sized supersystems.
Note that for visualization of orbitals or densities SE only
supports the generation of volumetric data via MAKE_CUBE_FILES
(**MolDen** files are not supported, *i.e.* MOLDEN_FORMAT should be
avoided). On the other hand, the monomer expansion (ME) only uses the basis set of
each individual fragment.
This choice of basis expansion is recommended for daily basis embedding calculations.

Analogous to a regular DFT calculation in **Q-Chem** (by using METHOD)
the exchange-correlation functional combination can either be selected with one
keyword **XC_Func**,or by defining **X_Func** and **C_Func**
(similar to EXCHANGE and CORRELATION). To include only the
electrostatic terms in the embedding potential one can set all the functional
keywords to **None**.

It is recommended to employ the same level of approximation for the non-additive kinetic and
exchange-correlation functional, for instance TF/SVWN or PW91k/PW91.

The *minimal specifications required* to successfully run a FDET calculation are:

- Functionals for embedding potential: **T_Func**, **XC_Func** (or **X_Func** and **C_Func**),
- Basis expansion: **Expansion**,
- Method for environment density: **rhoB_method**

### `T_Func`

> **Kinetic energy functional used for the construction of the embedding potential. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `TF`: Use Thomas-Fermi kinetic energy functional.
>     * `PW91k / LC94`: Use kinetic energy functional based on PW91.
>     * `None`: Do not include any kinetic energy functional.
> * **Recommendation**: Use the same level of approximation as for the non-additive exchange-correlation energy functional.

### `XC_Func`

> **Exchange-Correlation functional used for the construction of the embedding potential. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA or GGA exchange-correlation functionals available in Q-Chem .
>     * `None`: Do not include any exchange-correlation energy functional.
> * **Recommendation**: Only use LDA or GGA-type functionals.

### `X_Func`

> **Exchange functional used for the construction of the embedding potential. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA or GGA exchange functionals available in Q-Chem .
>     * `None`: Do not include any exchange energy functional.
> * **Recommendation**: Only use LDA or GGA-type functionals. XC_Func and are mutually exclusive.

### `C_Func`

> **Exchange-Correlation functional used for the construction of the embedding potential. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA or GGA correlation functionals available in Q-Chem .
>     * `None`: Do not include any exchange energy functional.
> * **Recommendation**: Only use LDA or GGA-type functionals. XC_Func and are mutually exclusive.

### `Expansion`

> **Specifies which basis set expansion should be used. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `SE/super/supermolecular`: Supermolecular basis is used for both System A and B.
>     * `ME/mono/monomer`: Monomer expansion basis is used on each System A and B.
> * **Recommendation**: SE should be used for testing purposes only, since it is more expensive. Use the ME as standard choice, particularly for large systems.

### `rhoA_method`

> **Method to calculate reference density $\rho_{A}^{\text{ref}}(\mathbf{r})$ of the core fragment (A). If DFT is requested, the respective exchange-correlation functional is the same as defined for the embedding calculation, i.e. with the keywords XC_FUNC or X_FUNC and C_FUNC . INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `HF`
> * **Options**:
>     * `HF`: Use Hartree-Fock method.
>     * `DFT`: Use Density Functional Theory.
>     * `MP`: Use Second-Order Møller-Plesset perturbation theory.
> * **Recommendation**: Use either HF or DFT.

### `rhoB_method`

> **Method to calculate the environment density (B). If DFT is requested, the respective exchange-correlation functional has to be defined using the keyword XC_FUNC_B or X_FUNC_B and C_FUNC_B . INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `HF`: Use Hartree-Fock method.
>     * `DFT`: Use Density Functional Theory.
>     * `MP`: Use Second-Order Moller-Pleset method.
> * **Recommendation**: Use either HF or DFT.

### `XC_Func_B`

> **Exchange-Correlation functional used for the environment DFT calculation. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA, GGA, or global hybrid-GGA exchange-correlation functionals available in Q-Chem .
> * **Recommendation**: None

### `X_Func_B`

> **Exchange functional used for the environment DFT calculation. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA or GGA exchange functionals available in Q-Chem .
> * **Recommendation**: XC_Func_B and are mutually exclusive.

### `C_Func_B`

> **Correlation functional used for the environment DFT calculation. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `NAME`
>     * `NAME`: can be any of the LDA or GGA correlation functionals available in Q-Chem .
> * **Recommendation**: XC_Func_B and are mutually exclusive.

### `PrintLevel`

> **Print level for FDE-Man output. INPUT SECTION: $fde**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: minimum print level
>     * `1`: extended print level
>     * `2`: maximum print level
>     * `3`: maximum print level and additional text files (densities, etc.)
> * **Recommendation**: Use minimal print level.

## 11.7.3.1 Superposition of Molecular Densities

When the selected environment comprises many atoms and molecules, a sensible
approximation is to construct the total environment density as the sum of
the densities of the individual molecules. This can be done with the keywords **Superposition_B**
or **Import_Superposition_B**. In the first case, the molecular densities are computed
in the same calculation, and assembled into one single density matrix.
The molecular densities and the superposed density matrices are saved into text files.

### `Superposition_B`

> **Compute the density of fragment B as a superposition of molecular densities. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Do a superposition of molecular densities to build the density of fragment B.
>     * `FALSE`: Don’t do a superposition, use the whole fragment B.
> * **Recommendation**: The molecular densities are calculated with the method specified with the keyword: rhoB_method .

In the second case, the individual density matrices are expected to be already calculated independently
and are required to be present in the same folder of the calculation.

### `Import_Superposition_B`

> **Assemble the density of fragment B from molecular densities. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Read and superpose the molecular densities to build the density of fragment B.
>     * `FALSE`: Don’t do a superposition, use the whole fragment B.
> * **Recommendation**: The files with the molecular density matrices should be .txt files, numerated from 0, with the prefix SCF_Dens_B_Subfrag_ .

!!! note "Note"
    No embedding calculation is performed if these functions are selected. In both cases,
    only the geometry of fragment B has to be given, and each molecule needs to be specified as independent
    fragment in the MOLECULE section.


When using the *superposition* options, the file of the superposed density matrix of the environment (B)
is saved with the name `Densmat_B.txt`, and can be used with the **import_rhoB** option
to subsequently perform an embedding calculation (see Sec. [11.7.3.2](#subsubsec:FDE-import) below).

## 11.7.3.2 Import Densities

In FDE-Man the user has the option to import the density matrices used to generate the embedding potential.
This alternative is particularly useful if the desired method to generate the densities for the embedding potential
is not available in the current version, for instance, or when the superposition of densities is used to generate $\rho_{B}(\mathbf{r})$.
The density matrices must be given *in AO basis* in a text file with the following format:

> ```qchem
> <nspin> <nbas> <nbas>
> <value>
> <value>
> ...
> ```

where `<nspin>` has two possible values (1 or 2) depending on the number of spin densities contained in the file.
The first line should also contain the dimensions of the density matrix (`<nbas>`).

### `import_rhoA`

> **Import density of subsystem A used for the embedding potential. The file must be named Densmat_A.txt and located in the calculation folder. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Read the density for subsystem A from file.
>     * `FALSE`: Do not use density from file.
> * **Recommendation**: None

### `import_rhoB`

> **Import density of subsystem B used for the embedding potential. The file must be named Densmat_B.txt and located in the calculation folder. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Read the environment density from file.
>     * `FALSE`: Do not use density from file.
> * **Recommendation**: None

## 11.7.3.3 Pre-Polarization of the Environment Density

Formally the exactness of FDET equations requires the condition
$\forall\mathbf{r}\left(\rho_{0}(\mathbf{r})\leq\rho_{B}(\mathbf{r})\right)$ to be satisfied,
whereby $\rho_{0}(\mathbf{r})$ denotes the exact density of the supersystem.[[1453]](../bib_references/bib.md#bib1515)

This condition can, however, not be assured *a priori*.
In practice, deficiencies with the initial choice of $\rho_{B}(\mathbf{r})$ can be cured to some extent by
pre-polarizing the environment density.[[1166]](../bib_references/bib.md#bib1219)

Pre-polarization schemes available in FDE-Man can be turn on
with the **prepol** keyword. The different pre-polarization options are described below.

### `prepol`

> **Pre-polarize $\rho_{B}(\mathbf{r})$ in the field of the embedded species represented by point charges or a charge density. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Turn on pre-polarization of $\rho_{B}(\mathbf{r})$ .
>     * `FALSE`: Do not pre-polarize the environment density.
> * **Recommendation**: See Ref. 1166 Ricardi N. et al. Phys. Chem. Chem. Phys. (2018) , 20 , pp. 26053 . Link for a review of FDET polarization schemes.

### `prepol_type`

> **Type of pre-polarization scheme. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `Mulliken`
> * **Options**:
>     * `Mulliken`: Use Mulliken charges of system A to pre-polarize $\rho_{B}(\mathbf{r})$ .
>     * `CHELPG`: Use ChElPG charges of system A to pre-polarize $\rho_{B}(\mathbf{r})$ .
>     * `elstat / Coulomb`: Use electrostatic embedding potential (using density and nuclear charges of A) to pre-polarize $\rho_{B}(\mathbf{r})$ .
> * **Recommendation**: None

### `root_Aref`

> **Defines which electronic state is considered for $\rho_{A}^{\text{ref}}(\mathbf{r})$ in the pre-polarization scheme. INPUT SECTION: $fde**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `n`: Use
>     * `n`: th state of A for pre-polarization scheme (ground state = 0).
> * **Recommendation**: None

## 11.7.3.4 Miscellaneous Options

### `Debug`

> **Request additional printings as well as saving the separate components of the embedding potential (in AO basis) to disk. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Print extra options and save components to disk.
>     * `FALSE`: Do not print extra info.
> * **Recommendation**: This option creates multiple files and additional details in the output. Use only for debugging purposes.

### `rhoB_basis`

> **Use a different basis set for fragment B than the one for the embedded system A, specified in the $rem section. Basis sets can be requested in the same way as in the BASIS section. However, contrary to the standard definition inside the input file, the user-defined basis and mixed basis must be defined without $basis and $end , in a text file called fde_genbasB and located in the calculation folder. INPUT SECTION: $fde**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `General, Gen`: User-defined. See Section 8.4 .
>     * `Symbol`: Use standard basis sets as in the tables in Section 8.3 .
>     * `Mixed`: Use a combination of different built-in basis sets (see Section 8.5 ).
> * **Recommendation**: Smaller basis for fragment B can be used to improve the performance of embedding calculations.

!!! note "Note"
    All basis used within the FDE-Man module use PURECART = 2111.


### `print_props`

> **Print molecular properties (multipole moments, Mulliken charges) associated with the reference fragment densities used to construct the embedding potential. INPUT SECTION: $fde**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: Do not print molecular properties.
>     * `1`: Print molecular properties only for fragment A.
>     * `2`: Print molecular properties for both fragments A and B.
> * **Recommendation**: None

If the user desires to *only* save the embedding potential without performing an embedding calculation, it can be done
by setting to *TRUE* simultaneously the variables **debug** and **Vemb_only**. In this case, the individual components
of the embedding potential are saved to disk into text files as mentioned above in the **debug**.

### `Vemb_only`

> **Only generate the embedding potential and save its components to disk. INPUT SECTION: $fde**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Generate embedding potential and exit FDE-Man.
>     * `FALSE`: Perform regular embedding calculation.
> * **Recommendation**: None
