---
title: "11.6.5 Previous Implementation Based on “EmbedMan”"
---

## 11.6.5 Previous Implementation Based on “EmbedMan”

(July 4, 2026)

The original implementation of the projection-based embedding in **Q-Chem**
was through the “EmbedMan” module, which was based on the old SCF module that is no longer the default.
This implementation applies a level-shift projection operator to
enforce the orthogonality between orbitals belonging to fragments 1 and 2.
For the 1-in-2 case, the Fock matrix can be written as

<a id="eq:des_fock"></a>

$$
\mathbf{f}^{(1)}=\mathbf{h}+\mathbf{J}[\gamma^{(1)}+\gamma^{(2)}]+\nu_{xc}[\gamma^{(1)}+\gamma^{(2)}]+\mu\mathbf{P}^{(2)} \tag{11.120}
$$

where $\mathbf{P}^{(2)}$ is the level-shift projection operator constructed as:

<a id="eq:des_proj"></a>

$$
\mathbf{P}^{(2)}_{\alpha\beta}=[\mathbf{S}\gamma^{(2)}\mathbf{S}]_{\alpha\beta} \tag{11.121}
$$

where $\gamma^{(2)}$ is the localized density of fragment 2, and $\mathbf{S}$
is the AO overlap matrix. Upon convergence, an energy correction term is added to
the final energy to account for the level-shift projection operator contribution to
the Fock matrix energy. The correction term is calculated as the following:

<a id="eq:des_corr"></a>

$$
E_{\mathrm{correction}}=\mu*\mathrm{tr}(\gamma^{(1)}\mathbf{P}^{(2)}) \tag{11.122}
$$

Once the KS-DFT energy of fragment 1-in-2 is computed, a post-SCF method can be
applied to this converged density to obtain the high-level QM additive energy
of fragment 1. The same procedure can be repeated for fragment 2-in-1, without
continuing to a post-SCF method to yield the low-level QM additive energy of
the fragment 2. These energies are then summed to yield the total energy.

To run an embedding calculation through the “EmbedMan” module, one must
split the super-molecular system into two fragments indexed 1 and 2, and set
EMBEDMAN to 1. This is done through the standard **Q-Chem**
fragment input syntax. Two separate jobs must be run to find the total energy
of fragment 1-in-2 at a high level QM theory, and fragment 2-in-1 at a low level
QM theory. The order of the fragments in the *$molecule* section determines which
fragment will undergo the high level QM. The user must submit a separate job for
the 2-in-1 low-level QM calculation, with the order of the fragments reversed and
EMBED_THEORY set to 0, which is the default value. The user
must then add the final energies of the calculations to determine the total
QM/QM embedded energy.

For the current **Q-Chem** implementation of density embedding, it is necessary
to specify the basis as MIXED, which requires to define the basis for
each individual atom. When using CCSD(T), one should specify CCMAN2
as TRUE, for **Q-Chem**’s most updated coupled-cluster code. The
current implementation of density embedding only works in combination with the
following settings: SCF_ALGORITHM = DIIS, INCFOCK = 0,
and PURECART = 222. It is also recommended that
users disable symmetry for calculations with INTEGRAL_SYMMETRY =
FALSE, and POINT_GROUP_SYMMETRY = FALSE. Refer to the sample
input for correct job settings.

### `EMBEDMAN`

> **Turns density embedding on.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not use density embedding.
>     * `1`: Turn on density embedding.
> * **Recommendation**: Use for QM/QM density embedded calculations.

### `EMBED_THEORY`

> **Specifies post-DFT method performed on fragment one.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No post HF method, only DFT on fragment one.
>     * `1`: Perform CCSD(T) calculation on fragment one.
>     * `2`: Perform MP2 calculation on fragment one.
> * **Recommendation**: This should be 1 or 2 for the high-level QM calculation of fragment 1-in-2, and 0 for fragment 2-in-1 low-level QM calculation.

### `EMBED_MU`

> **Specifies exponent value of projection operator scaling factor, $\mu$ [Eqs. ( 11.120 ) and ( 11.122 )].**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * `n`: $\mu=10^{n}$ .
> * **Recommendation**: Values of 2 - 7 are recommended. A higher value of $\mu$ leads to better orthogonality of the fragment MOs but $\mu>10^{7}$ introduces numerical noise. $\mu<10^{2}$ results in non-additive terms becoming too large. Energy corrections are fairly insensitive to changes in $\mu$ within the range of $10^{2}-10^{7}$ .

### `EMBED_THRESH`

> **Specifies threshold cutoff for AO contribution used to determine which MOs belong to which fragments**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * `n`: Threshold $=n/1000$
> * **Recommendation**: Acceptable values range from 0 to 1000. Should only need to be tuned for non-highly localized MOs

???+ example "Example 11.11.47: Input for a MP2/PBE density embedding calculation of He-in-HF. The sum
of the final energies for these two jobs will yield the total QM/QM energy."
    ```qchem
    $comment
    2023/4/5 use core guess becuase autosad and sad do not work with basis mixed
    $end
    
    $molecule
       0 1
    --
       0 1
       He      -4.63032        2.10289       -1.62399
    --
       0 1
       F       -8.00612        1.74605       -1.25581
       H       -7.40964        1.84462       -0.47756
    $end
    
    $rem
       EXCHANGE        PBE
       CORRELATION     PBE
       BASIS           mixed  ! Must specify basis sets per atom in $basis section below
       PURECART        222
       MAX_SCF_CYCLES  100
       SCF_ALGORITHM   DIIS
       INCFOCK         0
       CC_SYMMETRY     false
       EMBEDMAN        1      ! Turning density embedding on
       EMBED_THEORY    2      ! Running MP2 on fragment 1 in 2, or He in FH
       EMBED_MU        7      ! Default value
       EMBED_THRESH    500    ! Default value for assigning MOs to fragments
       SCF_GUESS       CORE
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $basis
      he 1
      6-31G
      ****
      f 2
      6-31G
      ****
      h 3
      6-31G
      ****
    $end
    
    @@@
    
    $molecule
    0 1
    --
    0 1
       F       -8.00612        1.74605       -1.25581
       H       -7.40964        1.84462       -0.47756
    --
    0 1
       He      -4.63032        2.10289       -1.62399
    $end
    
    $rem
      EXCHANGE        PBE
      CORRELATION     PBE
      BASIS           mixed
      PURECART        222
      MAXSCF          100
      SCF_ALGORITHM   DIIS
      INCFOCK         0
      EMBEDMAN        1
      EMBED_THEORY    0      ! There will be no post-DFT calculations for HF-in-He
      SCF_GUESS       core
      INTEGRAL_SYMMETRY    false
      POINT_GROUP_SYMMETRY false
    $end
    
    $basis
      f 1
      6-31G
      ****
      h 2
      6-31G
      ****
      he 3
      6-31G
      ****
    $end
    ```
