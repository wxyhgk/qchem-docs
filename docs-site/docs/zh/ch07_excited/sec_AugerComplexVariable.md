---
title: "7.9.12 Partial Auger Decay Widths from Complex-Variable Calculations"
---

## 7.9.12 Partial Auger Decay Widths from Complex-Variable Calculations

(July 4, 2026)

Auger decay in core-ionized atoms and molecules can be described by Feshbach–Fano approach
(see Section [7.9.11](sec_Auger.md)) as well as by complex-variable extensions of
the CCSD or EOM-CCSD methods.[[917]](../bib_references/bib.md#bib953)

In this latter approach, energies and widths $\Gamma$ (which are proportional to the decay rates)
of core-hole states are computed as
the difference of complex energies of ground and core-vacant states.

Both in Feshbach–Fano and complex-variable calculations of the AES, the
Auger intensities are proportional to the rate of decay into a particular channel.
Hence, one need to compute partial decay widths $\Gamma_{ij}$, which add up to the total width $\Gamma$.
Therein, $i$ and $j$
refer to the valence orbitals from which the electrons involved in the decay process are removed.
Below we describe two different ways of computing partial decay width using complex-variable CC/EOM-CC
approaches.

## 7.9.12.1 Decomposition of the Coupled-Cluster energy

The energy of a complex-variable coupled-cluster singles and doubles wave function can be written as

<a id="eq:ccenergy"></a>
$$
E-\mathrm{i}\frac{\Gamma}{2}=E_{\mathrm{CCSD}}=E_{\mathrm{HF}}+\sum_{ijab}\left(\frac{1}{4}t_{ij}^{ab}+\frac{1}{2}t_{i}^{a}t_{j}^{b}\right)\langle ij||ab\rangle. \tag{7.108}
$$

If the reference state has a core-hole, Auger decay-like transitions leading to doubly ionized states are double
excitations from two valence orbitals $i$ and $j$ to the core-hole $a$ and a virtual orbital $b$, which represents
emission into the continuum when using a complex-variable method.[[917]](../bib_references/bib.md#bib953)
 From Eq. ([7.108](#eq:ccenergy))
it is evident that we can obtain the contribution from one of these valence orbital combinations, *i.e.*, the
partial width, from the amplitude and two-electron integral tensors as

<a id="Ch7.E109"></a>
$$
\frac{\Gamma_{ij}}{2}=-\mathrm{Im}\left(\sum_{b}\left(t_{ij}^{ab}+2t_{i}^{a}t_{j}^{b}\right)\langle ij||ab\rangle\right). \tag{7.109}
$$

Since these quantities are determined in every CCSD calculation, the computational cost for such a partial width
calculation is negligible. This procedure is implemented in the CCMAN2 module of **Q-Chem** and can be invoked by setting
the CC_PW variable to 1. Open decay channels are determined by comparing the orbital energies. The output
contains a list of all combinations of two valence orbitals and their partial widths.

If the core-vacancy is produced through core-ionization in the closed-shell ground state of a molecule or atom, the
combination of $i_{\alpha}$ and $j_{\beta}$ describes the same target state as $i_{\beta}$ and $j_{\alpha}$. In the current
implementation, these two channels are automatically combined to a single decay width: in the output, one of the
orbitals characterizing the decay channel is always an alpha orbital and the inverted spin case is implicitly contained.

**Note: 

Core electrons must not be frozen in such calculations—N_FROZEN_CORE should be set to 0. The core hole must be in a $\beta$ orbital.

**

CC_PW

### `CC_PW`

> **Activates calculation of partial Auger decay widths via decomposition of the imaginary part of the coupled-cluster energy of a complex-variable CCSD calculation on a core-ionized state. Currently, this is implemented for states resulting from ionization of a $\beta$ core electron of a closed-shell system.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * do not invoke energy decomposition into partial Auger decay widths
>     * 1
>     * invoke energy decomposition into partial Auger decay widths
> * **Recommendation**: Use to compute partial widths for a complex-variable calculation on a core-vacant state. An appropriate complex-scaled basis set has to be chosen in order to capture Auger decay and the optimal scaling angle needs to be determined. 917 Matz F., Jagau T.-C. J. Chem. Phys. (2022) , 156 , pp. 114117 . Link , 918 Matz F., Jagau T.-C. Mol. Phys. (2023) , 121 , pp. e2105270 . Link

???+ example "Example 7.7.86: Calculation of Auger partial decay widths of the core-ionized neon atom."
    ```qchem
    $molecule
    0 1
    Ne 0 0 0
    $end
    
    $rem
    BASIS cc-pCVDZ
    COMPLEX_THETA = 200
    method = hf
    n_frozen_core = 0
    complex_basis gen
    complex_exponents 1
    complex_scf 1
    complex_scf_guess 1
    $end
    
    $complex_ccman
    cs_alpha 1000
    CS_THETA 0
    $end
    
    $zbasis
    Ne     0
    S   1   1.00
          4.3306000              1.0000000
    S   1   1.00
          1.4028562              1.0000000
    P   1   1.00
         17.4312839              1.0000000
    P   1   1.00
          5.6513946              1.0000000
    D   1   1.00
         23.7130337              1.0000000
    D   1   1.00
          4.1919117              1.0000000
    S    8   1.00
      17880.0000000              0.0007380
       2683.0000000              0.0056770
        611.5000000              0.0288830
        173.5000000              0.1085400
         56.6400000              0.2909070
         20.4200000              0.4483240
          7.8100000              0.2580260
          1.6530000              0.0150630
    S    8   1.00
      17880.0000000             -0.0001720
       2683.0000000             -0.0013570
        611.5000000             -0.0067370
        173.5000000             -0.0276630
         56.6400000             -0.0762080
         20.4200000             -0.1752270
          7.8100000             -0.1070380
          1.6530000              0.5670500
    S    1   1.00
         12.8540000              1.0000000
    S    1   1.00
          0.4869000              1.0000000
    P    3   1.00
         28.3900000              0.0460870
          6.2700000              0.2401810
          1.6950000              0.5087440
    P    1   1.00
         40.1840000              1.0000000
    P    1   1.00
          0.4317000              1.0000000
    D    1   1.00
          2.2020000              1.0000000
    ****
    $end
    
    @@@
    
    $molecule
    +1 2
    Ne 0 0 0
    $end
    
    $rem
    BASIS cc-pCVDZ
    COMPLEX_THETA = 200
    SCF_GUESS = READ
    method = ccsd
    n_frozen_core = 0
    MOM_START = 1
    cs_ccsd 1
    complex_ccman 1
    complex_basis gen
    complex_exponents 1
    complex_scf 2
    complex_scf_guess 1
    cc_pw 1
    $end
    
    $complex_ccman
    cs_alpha 1000
    CS_THETA 0
    $end
    
    $occupied
     1 2 3 4 5
     2 3 4 5
    $end
    
    $zbasis
    Ne     0
    S   1   1.00
          4.3306000              1.0000000
    S   1   1.00
          1.4028562              1.0000000
    P   1   1.00
         17.4312839              1.0000000
    P   1   1.00
          5.6513946              1.0000000
    D   1   1.00
         23.7130337              1.0000000
    D   1   1.00
          4.1919117              1.0000000
    S    8   1.00
      17880.0000000              0.0007380
       2683.0000000              0.0056770
        611.5000000              0.0288830
        173.5000000              0.1085400
         56.6400000              0.2909070
         20.4200000              0.4483240
          7.8100000              0.2580260
          1.6530000              0.0150630
    S    8   1.00
      17880.0000000             -0.0001720
       2683.0000000             -0.0013570
        611.5000000             -0.0067370
        173.5000000             -0.0276630
         56.6400000             -0.0762080
         20.4200000             -0.1752270
          7.8100000             -0.1070380
          1.6530000              0.5670500
    S    1   1.00
         12.8540000              1.0000000
    S    1   1.00
          0.4869000              1.0000000
    P    3   1.00
         28.3900000              0.0460870
          6.2700000              0.2401810
          1.6950000              0.5087440
    P    1   1.00
         40.1840000              1.0000000
    P    1   1.00
          0.4317000              1.0000000
    D    1   1.00
          2.2020000              1.0000000
    ****
    $end
    ```

## 7.9.12.2 Auger Channel Projectors

An alternative recipe to compute partial decay widths via complex-variable methods is to restrict the excitation manifold
so that excitations describing decay via a certain channel are no longer included. The projectors accomplishing this
are dubbed Auger Channel Projectors (ACP).[[918]](../bib_references/bib.md#bib954)
 A calculation with a decay channel projected out yields a
different energy and decay width than one with the channel present, and the difference in the decay width represents the
partial decay width of that channel.

ACP-EOM-IP-CCSD calculations are accelerated by using the EOM-IP-CCSD solution with the full excitation manifold as a guess.
For this purpose, the Maximum Overlap Method is used to ensure convergence to the same roots as in the initial EOM-IP-CCSD
calculation. This is invoked in the ccman2 module of **Q-Chem** by setting the EOM_ACP variable to 1. The output
contains a list of all open decay channels and their partial widths for each core-ionized state.

If the core-vacancy is produced through core-ionization in the closed-shell ground state of a molecule or atom, the
combination of $i_{\alpha}$ and $j_{\beta}$ describes the same target state as $i_{\beta}$ and $j_{\alpha}$. In the current
implementation, these two channels are automatically combined to a single decay width: in the output, one of the
orbitals characterizing the decay channel is always an alpha orbital and the inverted spin case is implicitly contained.

**Note: 

Core electrons must not be frozen in such calculations—N_FROZEN_CORE should be set to 0. The
core-valence separation must not be invoked.

**

EOM_ACP

### `EOM_ACP`

> **Activates calculation of partial Auger decay widths by recomputation of the EOM-CCSD state with an Auger Channel Projector applied. Currently, this is implemented for EOMIP-CCSD calculations with a closed-shell reference.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * do not run ACP-EOM-CCSD calculations
>     * 1
>     * determine partial Auger decay widths by running ACP-EOM-CCSD calculations
> * **Recommendation**: Use to compute partial widths for a complex-variable calculation which produces a core-vacant state. An appropriate complex-scaled basis set has to be chosen in order to capture Auger decay and the optimal scaling angle needs to be determined. 917 Matz F., Jagau T.-C. J. Chem. Phys. (2022) , 156 , pp. 114117 . Link , 918 Matz F., Jagau T.-C. Mol. Phys. (2023) , 121 , pp. e2105270 . Link

???+ example "Example 7.7.87: Calculation of Auger partial decay widths of the core-ionized neon atom."
    ```qchem
    $molecule
    0 1
    Ne 0 0 0
    $end
    
    $rem
    MEM_TOTAL = 172421
    BASIS cc-pCVDZ
    COMPLEX_THETA = 200
    method = ccsd
    n_frozen_core = 0
    complex_ccman 1
    complex_basis gen
    complex_exponents 1
    complex_scf 1
    complex_scf_guess 1
    ip_states = [1,0,0,0,0,0,0,0]
    eom_shift = 32000
    eom_acp 1
    $end
    
    $complex_ccman
    cs_alpha 1000
    CS_THETA 0
    $end
    
    $zbasis
    Ne     0
    S   1   1.00
          4.3306000              1.0000000
    S   1   1.00
          1.4028562              1.0000000
    P   1   1.00
         17.4312839              1.0000000
    P   1   1.00
          5.6513946              1.0000000
    D   1   1.00
         23.7130337              1.0000000
    D   1   1.00
          4.1919117              1.0000000
    S    8   1.00
      17880.0000000              0.0007380
       2683.0000000              0.0056770
        611.5000000              0.0288830
        173.5000000              0.1085400
         56.6400000              0.2909070
         20.4200000              0.4483240
          7.8100000              0.2580260
          1.6530000              0.0150630
    S    8   1.00
      17880.0000000             -0.0001720
       2683.0000000             -0.0013570
        611.5000000             -0.0067370
        173.5000000             -0.0276630
         56.6400000             -0.0762080
         20.4200000             -0.1752270
          7.8100000             -0.1070380
          1.6530000              0.5670500
    S    1   1.00
         12.8540000              1.0000000
    S    1   1.00
          0.4869000              1.0000000
    P    3   1.00
         28.3900000              0.0460870
          6.2700000              0.2401810
          1.6950000              0.5087440
    P    1   1.00
         40.1840000              1.0000000
    P    1   1.00
          0.4317000              1.0000000
    D    1   1.00
          2.2020000              1.0000000
    ****
    $end
    ```

???+ example "Example 7.7.88: Calculation of Auger partial decay widths using an open-shell reference and frozen core."
    ```qchem
    $molecule
    0 3
    O         0.0000000000    0.0000000000   -0.5800000000
    O         0.0000000000    0.0000000000    0.5800000000
    $end
    
    $rem
    BASIS gen
    COMPLEX_THETA = 110
    method = ccsd
    scf_convergence = 9
    cc_convergence = 9
    eom_davidson_convergence = 9
    eom_davidson_max_iter = 200
    ip_states = [0,0,0,0,0,1,0,0]
    scf_max_cycles = 400
    n_frozen_core = 1
    cs_ccsd 1
    complex_ccman 1
    complex_spin_state 3
    complex_basis gen
    complex_spin_state 3
    complex_scf_guess 1
    complex_exponents 1
    complex_scf 2
    complex_metscf 1
    thresh = 14
    eom_acp 1
    eom_user_guess 1
    $end
    
    $eom_user_guess
    2
    $end
    
    $complex_ccman
    cs_alpha 1000
    CS_THETA 0
    $end
    
    $zbasis
    O 0
    S   1   1.00
    8.00 1.00
    P   1   1.00
    8.00 1.00
    S   6   1.00
          0.5484671660D+04       0.1831074430D-02
          0.8252349460D+03       0.1395017220D-01
          0.1880469580D+03       0.6844507810D-01
          0.5296450000D+02       0.2327143360D+00
          0.1689757040D+02       0.4701928980D+00
          0.5799635340D+01       0.3585208530D+00
    SP   3   1.00
          0.1553961625D+02      -0.1107775495D+00       0.7087426823D-01
          0.3599933586D+01      -0.1480262627D+00       0.3397528391D+00
          0.1013761750D+01       0.1130767015D+01       0.7271585773D+00
    SP   1   1.00
          0.2700058226D+00       0.1000000000D+01       0.1000000000D+01
    ****
    $end
    
    $basis
    O     0
    S   6   1.00
          0.5484671660D+04       0.1831074430D-02
          0.8252349460D+03       0.1395017220D-01
          0.1880469580D+03       0.6844507810D-01
          0.5296450000D+02       0.2327143360D+00
          0.1689757040D+02       0.4701928980D+00
          0.5799635340D+01       0.3585208530D+00
    SP   3   1.00
          0.1553961625D+02      -0.1107775495D+00       0.7087426823D-01
          0.3599933586D+01      -0.1480262627D+00       0.3397528391D+00
          0.1013761750D+01       0.1130767015D+01       0.7271585773D+00
    SP   1   1.00
          0.2700058226D+00       0.1000000000D+01       0.1000000000D+01
    ****
    $end
    ```
