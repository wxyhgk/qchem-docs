---
title: "12.7.5 ALMO-EDA for Excited States"
---

## 12.7.5 ALMO-EDA for Excited States

(July 4, 2026)

## 12.7.5.1 Theory

So far we have only covered EDA methods for intermolecular interactions between
molecules in their ground states. Since electronic excited states are
associated with less strongly bound electrons, modified electrostatic multipole
moments (due to electron transition), and often larger polarizabilities,
effects imposed by other molecules can be even larger as well as less
chemically intuitive than those on ground states. Furthermore, there exist
systems that are weakly bound in the ground state but much more strongly bound
in the electronic excited state (*e.g.* He${}_{2}$ versus He${}_{2}^{\ast}$). Therefore, it
is very desirable to develop an interpretation tool that can be utilized to
study these important phenomena that are related to intermolecular interactions
involving excited-state molecules.

Ge *et al.* recently extended the ALMO-EDA to treat *exciplexes* (where the
excitation can be assigned to a single molecule within a complex)[[435]](../bib_references/bib.md#bib446)

and *excimers* (where multiple fragments contribute to the
excitation)[[434]](../bib_references/bib.md#bib447)
 computed at the CIS or TDDFT/TDA level of theory.
Here we briefly overview the decomposition schemes. In the EDA for exciplexes,
one first defines the interaction energy in the excited state ($\Delta E_{\mathrm{INT}}^{\ast}$) as

<a id="Ch12.E34"></a>
$$
\Delta E_{\mathrm{INT}}^{\ast}=E^{\ast}-E_{\mathrm{frag}}^{\ast} \tag{12.34}
$$

where $E^{\ast}=E+\omega$ is the energy of the excited supersystem, and
$E_{\mathrm{frag}}^{\ast}$ can be expressed as the sum of ground-state fragment
energies and the excitation energy of one of the fragments (without losing
generality, this excited fragment is denoted as fragment “1”):

<a id="eq:ex_e_frag"></a>
$$
E_{\mathrm{frag}}^{\ast}=\sum_{F}E_{F}+\omega_{1} \tag{12.35}
$$

Therefore, we can rewrite the excited-state interaction as

<a id="eq:ex_int"></a>
$$
\Delta E_{\mathrm{INT}}^{\ast}=\Delta E_{\mathrm{INT}}+\Delta\omega_{\mathrm{INT}} \tag{12.36}
$$

which contains contributions from the ground-state interaction energy ($\Delta E=E-\sum_{F}E_{F}$) and the excitation energy ($\Delta\omega_{\mathrm{INT}}=\omega-\omega_{1}$). Then, as in the first-generation
ALMO-EDA for ground states[[682]](../bib_references/bib.md#bib706)
, the excited-state
interaction energy can be separated into contributions from frozen interaction
(FRZ), polarization (POL), and charge transfer (CT):

<a id="eq:ex_eda"></a>
$$
\Delta E_{\mathrm{INT}}^{\ast}=\Delta E_{\mathrm{FRZ}}^{\ast}+\Delta E_{\mathrm{POL}}^{\ast}+\Delta E_{\mathrm{CT}}^{\ast} \tag{12.37}
$$

Each term on the RHS of Eq. ([12.37](#eq:ex_eda)) can be written in a similar form as Eq. ([12.36](#eq:ex_int)):

<a id="A3.S8.EGx124"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{\ast}&\displaystyle=\Delta E_{\mathrm{FRZ}}+\omega_{\mathrm{FRZ}}-\omega_{1}\\
&\displaystyle=\Delta E_{\mathrm{FRZ}}+\Delta\omega_{\mathrm{FRZ}}\\
\displaystyle\Delta E_{\mathrm{POL}}^{\ast}&\displaystyle=\Delta E_{\mathrm{POL}}+\omega_{\mathrm{POL}}-\omega_{\mathrm{FRZ}}\\
&\displaystyle=\Delta E_{\mathrm{POL}}+\Delta\omega_{\mathrm{POL}}\\
\displaystyle\Delta E_{\mathrm{CT}}^{\ast}&\displaystyle=\Delta E_{\mathrm{CT}}+\omega-\omega_{\mathrm{POL}}\\
&\displaystyle=\Delta E_{\mathrm{CT}}+\Delta\omega_{\mathrm{CT}}\end{aligned} \tag{12.38}
$$

The terms $\Delta E_{\mathrm{FRZ}}$, $\Delta E_{\mathrm{POL}}$, and $\Delta E_{\mathrm{CT}}$ can be obtained by performing a ground-state ALMO-EDA for the
supersystem. To compute $\Delta\omega_{\mathrm{FRZ}}$, $\Delta\omega_{\mathrm{POL}}$, and $\Delta\omega_{\mathrm{CT}}$, one needs to define
$\omega_{\mathrm{FRZ}}$ and $\omega_{\mathrm{POL}}$, *i.e.*, excitation energies
associated with the frozen and polarized supersystem, respectively. The frozen
intermediate state can be viewed as one excited fragment embedded in the
environment formed by other ground-state fragments, whose effects on the
excited fragment are only through the supersystem Fock matrix. The definition
of the polarized intermediate state utilizes the ALMO-CIS model (see
Section [12.16](sect_ALMO-CIS.md)), where both MOs and excitation amplitudes are
fragment-localized. We also note that the frozen contribution to the
excited-state interaction energy, $\Delta E_{\mathrm{FRZ}}^{\ast}$, can be
further partitioned into a classical electrostatics term (Coulomb interactions
between isolated fragment charge distributions) and a non-electrostatic term
(mostly Pauli repulsion if a non-dispersion-corrected model such as CIS is used):

<a id="eq:ex_eda_frz_decomp"></a>
$$
\Delta E_{\mathrm{FRZ}}^{\ast}=\Delta E_{\textrm{CLS-ELEC}}^{\ast}+\Delta E_{\textrm{NON-ELEC}}^{\ast} \tag{12.39}
$$

Modifications are needed in order to extend this method to excimers, where
different fragments are of degenerate or near-degenerate excited states. In
such cases, we choose $M$ reference fragment states as the initial basis.
Denote the $s$th excited state on fragment $I$ as the
$\kappa$th reference state ($\kappa=1,2,\dots,M$).
Similar to Eq. ([12.35](#eq:ex_e_frag)), we have

<a id="eq:ex_e_frag_mult"></a>
$$
E_{\mathrm{frag}}^{\kappa}=\sum_{F}E_{F}+\omega_{I}^{s} \tag{12.40}
$$

The corresponding frozen excited-state wave function is then constructed by
embedding this excited fragment into the environment formed by other fragments in their ground states:

<a id="Ch12.E41"></a>
$$
\left|\Phi_{\mathrm{FRZ}}^{\kappa}\right\rangle=\left|\Psi_{1}\Psi_{2}\cdots\Psi_{I}^{s}\cdots\Psi_{N}\right\rangle \tag{12.41}
$$

and the excited-state frozen interaction energy

<a id="Ch12.E42"></a>
$$
\Delta E_{\mathrm{FRZ}}^{\kappa}=\Delta E_{\mathrm{FRZ}}+\Delta\omega_{\mathrm{FRZ}}^{\kappa}=\Delta E_{\mathrm{FRZ}}+(\omega_{\mathrm{FRZ}}^{\kappa}-\omega_{I}^{s}) \tag{12.42}
$$

With $M$ degenerate or near-degenerate frozen excited states, a new
intermediate state is then introduced to capture the pure excitonic-splitting
(EXSP) effect in the formation of excimers, which can be expressed as a linear
combination of the frozen states:

<a id="eq:ex_eda_exsp"></a>
$$
\left|\Phi^{\kappa}_{\mathrm{EXSP}}\right\rangle=\sum_{\kappa^{\prime}}^{M}c^{\kappa\kappa^{\prime}}\left|\Psi_{1}\Psi_{2}\cdots\Psi_{I}^{s}\cdots\Psi_{N}\right\rangle \tag{12.43}
$$

The associated excitation energy $\omega^{\kappa}_{\mathrm{EXSP}}$ and the
corresponding linear combination coefficients can be obtained by solving a
secular equation in the basis of frozen states. As excitonic splitting is
purely an excited-state phenomenon, we have

<a id="Ch12.E44"></a>
$$
\Delta E^{\kappa}_{\mathrm{EXSP}}=\Delta\omega^{\kappa}_{\mathrm{EXSP}}=\omega^{\kappa}_{\mathrm{EXSP}}-\omega^{\kappa}_{\mathrm{FRZ}} \tag{12.44}
$$

Subsequently, polarization and charge transfer are handled in a similar way as in the excimer case:

<a id="A3.S8.EGx125"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E^{\kappa}_{\mathrm{POL}}&\displaystyle=\Delta E_{\mathrm{POL}}+\Delta\omega^{\kappa}_{\mathrm{POL}}=\Delta E_{\mathrm{POL}}+(\omega^{\kappa}_{\mathrm{POL}}-\omega^{\kappa}_{\mathrm{EXSP}})\\
\displaystyle\Delta E^{\kappa}_{\mathrm{CT}}&\displaystyle=\Delta E_{\mathrm{CT}}+\Delta\omega^{\kappa}_{\mathrm{CT}}=\Delta E_{\mathrm{CT}}+(\omega^{\kappa}-\omega^{\kappa}_{\mathrm{POL}})\end{aligned} \tag{12.45}
$$

One more complication compared to the EDA scheme for exciplexes is that since
multiple ($M$) states are considered, extra caution needs be paid to the
state-ordering at different stages (EXSP, POL and CT). In order to locate the
states of interest (which can be most unambiguously identified at the EXSP
stage) correctly during the entire EDA procedure, a state-tracking algorithm
based on a maximum-overlap criterion is employed. The reader is referred to
Ref. [[434]](../bib_references/bib.md#bib447)
 for more details.

## 12.7.5.2 Job Control

The ALMO-EDA for intermolecular interactions involving excited-state molecules
implemented in **Q-Chem** 5.1 supports CIS and TDDFT within the Tamm-Dancoff
approximation (TDA) for closed-shell systems, *i.e.*, excited states calculated
by TDDFT and unrestricted systems are currently *not* supported. The EDA
procedure is triggered by setting EX_EDA = TRUE. The code
first performs a customized ground-state calculation (using AO-based ALMOs)
through the “EDA2” driver. During the isolated fragment calculations in this
EDA, the fragment excited states are also computed after its ground-state SCF
is converged, which is controlled by a new input section *$frgm_cis_n_roots*.
The format of this input section is as follows:

> ```qchem
> $frgm_cis_n_roots
> ¯frgm_idx1¯¯nstates_to_calc¯¯nstates_as_exciton_basis
> ¯frgm_idx2¯¯nstates_to_calc¯¯nstates_as_exciton_basis
> ¯.  .  .
> $end
> ```

Here “nstates_to_calc” specifies the number of states to calculate for each
fragment (the value of CIS_N_ROOTS for each fragment calculation),
and “nstates_as_exciton_basis” refers to the number of calculated fragment
states that are used to construct the EXSP state (whose sum gives $M$ in
Eq. ([12.43](#eq:ex_eda_exsp))). When the supersystem is considered as an exciplex
where the excitation is assigned to a specific fragment, only one row is needed
in this section, and there is no need to specify the number of states used as
the basis for the EXSP state.

The other relevant rem variables includes CIS_N_ROOTS, which
specifies the number of roots to calculate in the ALMO-CIS/TDA and full CIS/TDA
calculations, and EIGSLV_METH (see Section [12.16](sect_ALMO-CIS.md)) that is
set to 1 (using the Davidson iterative solver) by default. Note that the number
of states that the EDA is concerned with is controlled by the number of
isolated fragment states (the exciplex case) or the total number of states that
are excitonically coupled (the excimer case). In the latter case,
CIS_N_ROOTS is usually set to a value that is larger than $M$ to
ensure that all states of interest are captured in the ALMO-CIS/TDA and full
CIS/TDA calculations, as changes in state-ordering might occur.

EX_EDA

### `EX_EDA`

> **Perform an ALMO-EDA calculation with one or more fragments excited.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform EDA with excited-state molecule(s) taken into account.
>     * FALSE
> * **Recommendation**: None

???+ example "Example 12.35: EDA for the lowest two excited states of the formamide-water complex at the
CIS/6-31+G(d) level of theory. Both excited states are assigned to the
formamide molecule and the system is regarded as an exciplex."
    ```qchem
    $molecule
    0 1
    --
    0 1
    C         1.1508059365    0.2982718924    0.0240277739
    O         0.3545181649    1.2334803420   -0.0015882208
    N         0.8104369587   -1.0072797234    0.0043506838
    H         2.2327270535    0.4686363261    0.0666232655
    H        -0.1675092286   -1.2596328526   -0.0352400180
    H         1.5210524537   -1.7122494331    0.0139809901
    --
    0 1
    O        -1.9693273428   -0.2999882700   -0.2293071572
    H        -1.3827632725    0.4697313642   -0.1375254289
    H        -2.7470364523   -0.0962178118    0.2907490329
    $end
    
    $rem
       JOBTYPE           eda
       METHOD            hf
       BASIS             6-31+g(d)
       EX_EDA            true
       SCF_CONVERGENCE   8
       CIS_N_ROOTS       2
       CIS_TRIPLETS      false
       THRESH            12
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frgm_cis_n_roots
    1  2
    $end
    
    ```

???+ example "Example 12.36: EDA for the lowest two states (1s->2s) of the He ${}_{2}^{\ast}$ excimer
computed at the CIS/6-311(2+,2+)G (customized) level of theory.
For each He, eight excited states are calculated and only the lowest
one is used to construct the EXSP state, giving rise to two supersystem
states."
    ```qchem
    $molecule
    0 1
    --
    0 1
    He    0.0   0.0  0.0
    --
    0 1
    He    3.0   0.0  0.0
    $end
    
    $rem
       JOBTYPE        eda
       EX_EDA         true
       METHOD         hf
       BASIS          gen   !6-311(2+,2+)G
       CIS_N_ROOTS    8
       CIS_TRIPLETS   false
       THRESH         12
       EIGSLV_METH    0   !direct
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frgm_cis_n_roots
    1  8  1
    2  8  1
    $end
    
    $basis
    He   0
    S    3    1.000000
    9.81243000E+01    2.87452000E-02
    1.47689000E+01    2.08061000E-01
    3.31883000E+00    8.37635000E-01
    S    1    1.000000
    8.74047000E-01    1.00000000E+00
    S    1    1.000000
    2.44564000E-01    1.00000000E+00
    SP   1    1.000000
    4.80000000E-02    1.00000000E+00   1.00000000E+00
    SP   1    1.000000
    1.44578313E-02    1.00000000E+00   1.00000000E+00
    ****
    $end
    ```
