---
title: "12.7.4 ALMO Force Decomposition Analysis"
---

## 12.7.4 ALMO Force Decomposition Analysis

(July 4, 2026)

Building on the success of the adiabatic EDA (Section [12.7.3](sect_adiabatic_eda.md)), a
similar extension can be introduced which decomposes the forces at any
geometry. Instead of following the forces to generate a geometry and evaluate
the energy in that geometry as in the adiabatic EDA, the force decomposition
analysis decomposes and analyzes the forces on their own at a given geometry.
One important feature emerges from this approach which is the ability to
decompose the frozen force, uncovering the frozen component relevant to a
geometric change. This decomposition is not meaningful in the the adiabatic
EDA since following purely attractive forces, for example, would collapse the
molecules into each other.

Work by Aldossary *et al.* implements the analytical derivative of the classical
electrostatics energy [[36]](../bib_references/bib.md#bib21)
, allowing the frozen force to be
broken down into classical electrostatics and van der Waals (Pauli and
Dispersion) forces:

<a id="eq:Ffrz_decomp"></a>

$$
\Delta\mathbf{F}_{\text{frz}}=\Delta\mathbf{F}_{\text{cls-elec}}+\Delta\mathbf{F}_{\text{vdw}}. \tag{12.32}
$$

Additionally, the frozen forces are now defined to subtract the geometric
distortion forces (forces arising from geometric distortion energy). The
frozen force term is now:

<a id="eq:Ffrz"></a>

$$
\Delta\textbf{F}_{\text{frz}}=\textbf{F}_{\text{frz}}[\mathbf{P}_{\text{frz}}]-\sum_{A}\textbf{F}_{A}[\textbf{P}_{A}], \tag{12.33}
$$

where the second term on the right hand side the geometric distortion
forces. Similar to the geometric distortion energy, the geometric distortion
forces are subtracted from those of the isolated geometry which evaluate to
zero for a geometric minimum. In other words, the geometetric distortion forces
are nothing but the isolated fragments’ forces in the complex geometry. The
geometric distortion forces are printed separately for analysis.

By decomposing the intermolecular forces into geometric distortion,
electrostatics, van der Waals, polarization, and charge transfer, we have now
generated 5 times more forces than a regular force job. The $5(3N)$ forces
can be difficult to analyze manually, and we use internal coordinates to make
chemical sense of these forces. The Wilson’s B matrix is generated using the
new opt3 library and we apply the usual transformation. The user can then hone
in to the bond, angle, or dihedral of interest to analyze the which force
components are relevant to the stretch or compression. Despite the usefulness
of the redundant internal coordinates, they are not unique, and the order of
the atoms in the input file can affect the results.

FDA

### `FDA`

> **Decompose intermolecular forces**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Does a regular force job.
>     * TRUE
>     * Invokes the force decomposition analysis method
> * **Recommendation**: Set it to TRUE with jobtype=force to decompose the force.

???+ example "Example 12.34: Force Decomposition Analysis job for the H ${}_{2}$ O $\cdots$ F ${}^{-}$ job using the internal coordinates"
    ```qchem
    $molecule
    -1 1
    --
    0 1
    O       0.0144306160     0.0000000000     0.0991268524
    H      -0.0433242925     0.0000000000     1.2143531865
    H       0.9756708294     0.0000000000    -0.0327279220
    --
    -1 1
    F      -0.0237828221    -0.0000000000     2.5253092017
    $end
    
    $rem
    JOBTYPE      FORCE
    FDA          TRUE
    GEN_SCFMAN   TRUE
    METHOD       PBE
    BASIS        def2-svp
    MEM_TOTAL    2000
    MEM_STATIC   500
    SCF_GUESS    FRAGMO
    BASIS_LIN_DEP_THRESH  6
    SCFMI_MODE            0
    SCF_PRINT_FRGM        TRUE
    SCF_CONVERGENCE       10
    THRESH                14
    INTEGRAL_SYMMETRY     FALSE
    POINT_GROUP_SYMMETRY  FALSE
    $end
    
    ```
