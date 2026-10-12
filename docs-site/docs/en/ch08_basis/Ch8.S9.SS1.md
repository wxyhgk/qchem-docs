---
title: "8.9.1 Overview"
---

## 8.9.1 Overview

(July 4, 2026)

When calculating intermolecular interaction energies, a naïve calculation
of the energy difference

<a id="eq:DeltaE_AB"></a>

$$
\Delta E_{AB}=E_{AB}-E_{A}-E_{B} \tag{8.5}
$$

usually results in severe overestimation of the interaction energy, even if all
three energies in Eq. ([8.5](#eq:DeltaE_AB)) are computed at a good level of
theory. This phenomenon, known as *basis set superposition error* (BSSE),
is an artifact of an unbalanced approximation, namely, that the dimer energy
$E_{AB}$ is computed in a more flexible basis set as compared to the two
monomer energies. Although BSSE disappears in the complete basis-set limit, it
does so extremely slowly: in $\rm(H_{2}O)_{6}$, for example, an MP2/aug-cc-pVQZ calculation of the interaction energy is still a bit more than
1 kcal/mol away from the MP2 complete-basis limit.[[1171]](../bib_references/bib.md#bib1223)
 Short
of computing all energies in very large basis sets and extrapolating to the
complete-basis limit, the conventional solution to the BSSE problem is the
*counterpoise correction*, originally proposed by Boys and
Bernardi.[[151]](../bib_references/bib.md#bib148)
 Here, one corrects for BSSE by computing the monomer
energies $E_{A}$ and $E_{B}$ in the dimer basis set, with the idea being that this
results in a more balanced treatment of $\Delta E_{AB}$.

In truth the average of the counterpoise-corrected and uncorrected results is
often a better approximation than either of them individually, but in any case
one needs the counterpoise-corrected result. This requires basis functions to
be placed at arbitrary points in space, not just those defined by the nuclear
centers; these are usually termed “floating centers” or “ghost atoms”.
Ghost atoms have zero nuclear charge but can support a user-defined basis set.
Their positions are specified in the *$molecule* section alongside all the
other atoms (atomic symbol: Gh), and their intended basis functions are
specified in one of two ways:

1. Via a user-defined *$basis* section, using BASIS = MIXED.
2. Placing “$@$” next to an atomic symbol in the *$molecule* section
designates it as a ghost atom supporting the same basis functions as the
corresponding atom, so that a *$basis* section is not required.

Examples of either procedure appear below.

The calculation of $\Delta E_{AB}$ in Eq. ([8.5](#eq:DeltaE_AB)) requires three
separate electronic structure calculations but this process can be performed
automatically using **Q-Chem**’s BSSE job type based on calculations
using fragment jobs. This machinery is much more versatile and is
described in detail later so we will not discuss the automatic procedure here;
see Section [12.4](../ch12_frag/sect_autoBSSE.md) for that.

???+ example "Example 8.4: A calculation on a water monomer in the presence of the full
dimer basis set. The energy will be slightly lower than that without the ghost
atom functions due to the greater flexibility of the basis set."
    ```qchem
    $molecule
       0  1
       O    1.68668  -0.00318   0.000000
       H    1.09686   0.01288  -0.741096
       H    1.09686   0.01288   0.741096
       Gh  -1.45451   0.01190   0.000000
       Gh  -2.02544  -0.04298  -0.754494
       Gh  -2.02544  -0.04298   0.754494
    $end
    
    $rem
       METHOD        mp2
       BASIS         mixed
    $end
    
    $basis
       O 1
       6-31G*
       ****
       H 2
       6-31G*
       ****
       H 3
       6-31G*
       ****
       O 4
       6-31G*
       ****
       H 5
       6-31G*
       ****
       H 6
       6-31G*
       ****
    $end
    ```

???+ example "Example 8.5: A calculation on ammonia in the presence of the basis set of ammonia borane."
    ```qchem
    $molecule
       0 1
        N     0.0000   0.0000   0.7288
        H     0.9507   0.0001   1.0947
        H    -0.4752  -0.8234   1.0947
        H    -0.4755   0.8233   1.0947
       @B     0.0000   0.0000  -0.9379
       @H     0.5859   1.0146  -1.2474
       @H     0.5857  -1.0147  -1.2474
       @H    -1.1716   0.0001  -1.2474
    $end
    
    $rem
       METHOD          B3LYP
       BASIS           6-31G(d,p)
       PURECART        1112
    $end
    ```
