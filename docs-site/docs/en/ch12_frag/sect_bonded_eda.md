---
title: "12.7.2 ALMO-EDA for Bonded Interactions"
---

## 12.7.2 ALMO-EDA for Bonded Interactions

(July 4, 2026)

EDA schemes have been very successful at elucidating the nature of noncovalent
interactions. On the other hand, these methods are often inadequate for the analysis
of covalent bonds. In fragment-based approaches, the key difficulty arises from
the need to correctly spin-couple two open-shell radical fragments into a closed-shell
bond in a spin-pure way. The ALMO-EDA methodology was extended by Levine to
accomplish this within HF and KS DFT[[810]](../bib_references/bib.md#bib841)
.
If HF is used, the final wave function whose interaction energy is being decomposed is
the CAS(2,2)/1-pair perfect-pairing/TCSCF wave function. At present, only a single bond
may be analyzed by these schemes.

The method begins with two doublet radical fragments, each of which is described by a
restricted open-shell (RO) Hartree-Fock (HF) or Kohn-Sham DFT single determinant. In
the bonded EDA scheme, because orbital re-hybridization can play such a large role in
the energy, $\Delta E_{\text{PREP}}$ includes the energy required to distort each
radical fragment to the geometry that it adopts in the bonded state $\Delta E_{\text{GEOM}}$,
as well as an electronic preparation due to orbital re-hybridization $\Delta E_{\text{HYBRID}}$.
For example, an F atom has an unpaired electron in a $p$ orbital, while an F atom in
a bond will be $sp$-hybridized. The amine radical, NH${}_{2}$, is $sp^{2}$-hybridized with
an unpaired electron in a $p$ orbital, while an amine group is often $sp^{3}$- or
$sp^{2}$-hybridized with a lone pair in the $p$ orbital in a molecule. Then,

<a id="Ch12.E25"></a>
$$
\Delta E_{\text{PREP}}=\Delta E_{\text{GEOM}}+\Delta E_{\text{HYBRID}} \tag{12.25}
$$

This re-hybridized state is obtained by relaxing the ALMO supersystem obtained from the
fragments, permitting only on-fragment doubly-occupied–singly-occupied orbital rotations
(which are well-defined due to the RO nature of the fragments). The so-optimized fragments
are then re-separated and the energy difference between the electronically distorted
fragments and the ground state fragments is $\Delta E_{\text{HYBRID}}$. This corresponds
to fixing the $\alpha$-density and allowing the $\beta$-hole to re-optimize in the span
of that $\alpha$-density. This is a kind of polarization, although we draw a distinction
from the electronic polarization step which appears later in both the bonded
and non-bonded ALMO schemes. Another reason why it makes sense to place the
re-hybridization energy here is that it is already partially accounted for by
the fact that the geometry of the radical fragment is fixed to be that of the
interacting fragment. For instance, free methyl radical is an $sp^{2}$-hybridized
planar molecule, while a methyl group in a bond is a pyramidalized $sp^{3}$ fragment;
the re-hybridzation cost was already paid by the geometric distortion.

The FRZ energy in the bonded scheme corresponds to the ALMO supersystem formed by
combining the RO fragments to form a spin-pure triplet single-determinant wave function
without allowing the orbitals to relax further. This term is entirely a non-bonded interaction
and will typically be repulsive for a chemical bond because of Pauli repulsion.
It includes contributions from inter-fragment electrostatics, Pauli repulsion,
exchange-correlation, and dispersion. The EDA2 frozen decomposition scheme may be
applied to this term in the spin-projected formalism (*i.e.*, BONDED_EDA = 2).

A new term is introduced for the bonded EDA scheme: $\Delta E_{\text{SC}}$ of the
spin-coupling energy. This energy difference is caused by electron pairing and
loosely corresponds to the idea of covalency. Like FRZ, SC will be evaluated
with frozen orbitals, but while FRZ is typically strongly repulsive (dominated by
Pauli repulsion), SC is typically strongly attractive in the overlapping regime
associated with covalent bond formation. For this reason and because we are primarily
interested in the singlet surface (as opposed to the triplet surface of the initial
supersystem), FRZ and SC may be grouped together into a total frozen orbital term (FRZ + SC).

In the KS DFT scheme,[[809]](../bib_references/bib.md#bib843)
 this spin-coupled wave function is formed by forming
the broken-symmetry DFT determinant and spin-projecting out the triplet contaminant. Since the
wave function is constructed from RO fragment, spin-contamination can only occur within the
half-occupied space and hence the triplet contaminant is the only possible contaminant.
We therefore obtain and exact singlet wave function. For HF, this is exactly equivalent
to the scheme based on nonorthogonal CI,[[810]](../bib_references/bib.md#bib841)
 so long as there are only two
unpaired spins among the fragments (*i.e.*, the supersystem is closed shell). This is usually
the case and so, as the schemes are equivalent, we advocate only using the spin-projected
formalism as it is much more efficient.

The POL and CT terms are similarly defined as in the non-bonded ALMO scheme. FERFs may be used
to define polarization but monopole FERFs, which describe the expansion or contraction
of orbitals (which occurs in some cases on bond formation should be included).[[808]](../bib_references/bib.md#bib842)

The CT term gives an indication of the level of ionic character in the bond. Taken
together the various terms describe a fingerprint for the bond being studied. Further
details for how to analyze the results may be found in the referenced literature.

Considerations for using the bonded ALMO-EDA:

- •

SCFMI_MODE = 1 is required.
- •

ROSCF = TRUE must be set.
- •

There are no presets of the bonded ALMO-EDA. Therefore, set EDA2 = 10.
- •

DIIS may not be used for SCF_ALGORITHM. Use GDM_LS
for BONDED_EDA = 2 and L_BFGS for BONDED_EDA = 1.

BONDED_EDA

### `BONDED_EDA`

> **Use the bonded ALMO-EDA.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not perform bonded ALMO-EDA.
>     * 1
>     * Perform ALMO-EDA with non-orthogonal CI.
>     * 2
>     * Perform ALMO-EDA with spin-projected formalism.
> * **Recommendation**: Set to 2 for all cases where the supersystem is closed shell, only use 1 for cases where the fragments have more than one unpaired spin each.

EDA_CONTRACTION_ANAL

### `EDA_CONTRACTION_ANAL`

> **Perform analysis separating orbital contraction from the rest of POL.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `0`
> * **Options**:
>     * FALSE
>     * Do not perform contraction analysis.
>     * TRUE
>     * Perform contraction analysis.
> * **Recommendation**: No recommendation

???+ example "Example 12.28: Bonded EDA of F ${}_{2}$ with MDQ FERFs, frozen analysis in the spin-projected formalism"
    ```qchem
    $molecule
       0 3
       --
       0 2
       F 0.0 0.0 0.0
       --
       0 2
       F 0.0 0.0 1.382
    $end
    
    $rem
       JOBTYPE              eda
       EXCHANGE             wb97x-d
       BASIS                aug-cc-pvdz
       EDA2                 10
       BONDED_EDA           2
       SCF_CONVERGENCE      6
       MAX_SCF_CYCLES       200
       ROSCF                true
       SCF_GUESS            fragmo
       SCF_ALGORITHM        gdm_ls
       SCFMI_MODE           1
       SCF_PRINT_FRGM       true
       CHILD_MP             true
       CHILD_MP_ORDERS      1233
       FRZ_RELAX            true
       FRZ_RELAX_METHOD     2
       FRZ_ORTHO_DECOMP     false
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
       EDA_CLS_ELEC         true
    $end
    
    $rem_frgm
       scf_convergence   7
       scf_algorithm     gdm_ls
       scf_guess         sad
    $end
    ```

???+ example "Example 12.29: Bonded EDA of CH with MDQ FERFS, contraction analysis in the non-orthogonal CI formalism."
    ```qchem
    $molecule
       0 4
       --
       0 3
       C         0.0000000000    0.0000000000   -0.0525358999
       --
       0 2
       H         0.0000000000    0.0000000000    1.0525358999
    $end
    
    $rem
       JOBTYPE                eda
       EXCHANGE               hf
       BASIS                  aug-cc-pvdz
       EDA2                   10
       BONDED_EDA             1
       SCF_CONVERGENCE        6
       MAX_SCF_CYCLES         2000
       ROSCF                  true
       SCF_GUESS              fragmo
       SCF_ALGORITHM          l_bfgs
       SCFMI_MODE             1
       SCF_PRINT_FRGM         true
       CHILD_MP               true
       CHILD_MP_ORDERS        1233
       FRZ_RELAX              true
       FRZ_RELAX_METHOD       2
       EDA_CONTRACTION_ANAL   true
       INTEGRAL_SYMMETRY      false
       POINT_GROUP_SYMMETRY   false
    $end
    
    $rem_frgm
       scf_convergence   7
       scf_algorithm     gdm_ls
       scf_guess         sad
    $end
    ```
