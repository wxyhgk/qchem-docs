---
title: "7.9.11 Auger Spectra and Lifetimes of Core-Level States"
---

## 7.9.11 Auger Spectra and Lifetimes of Core-Level States

(July 4, 2026)

Certain types of resonances can be described by using real-valued EOM-CC
wave functions via Feshbach–Fano approach.[[384]](../bib_references/bib.md#bib392)
 In this section we describe
the application of Feshbach–Fano approach to core-excited and
core-ionized states.[[1262]](../bib_references/bib.md#bib1316)

Core-hole states, which are Feshbach resonances, are subject to autoionization—commonly known
as Auger decay. Auger Electron Spectroscopy (AES) measures kinetic energy and intensity of
ejected electrons. The energy of the Auger electrons are computed as differences between the initial
core-hole state and final decay states. For example, for regular Auger decay:

<a id="eq:Echannel_a"></a>

$$
E_{\text{Auger}}^{\mu n}=E_{n}^{\text{CoreIP}}-E_{\mu}^{\text{DIP}}, \tag{7.104}
$$

where $E_{n}^{\text{CoreIP}}$ and $E_{\mu}^{\text{DIP}}$ are energies of the
initial (core-hole) and final (doubly ionized valence) states, respectively.
The intensities of each decay channel are given by partial decay widths, $\Gamma_{\mu n}$.
In the crudest approximation, one can assign each decay channel unit intensity—so-computed Auger spectra reflect density of doubly ionized states of the system.
For more rigorous treatments, the decay widths can be computed
by either the Feshbach–Fano or complex-variable approaches[[1262]](../bib_references/bib.md#bib1316)

for electronic resonances (the latter approach is described in sections
7.9.11 and [7.9.12](sec_AugerComplexVariable.md)).

The Feshbach–Fano theory[[384]](../bib_references/bib.md#bib392)
 invokes
two projection operators, $\hat{Q}$ and $\hat{P}$, which
decompose the total wave function into bound-like and continuum-like
components. In the case of core-level states this separation
is enabled by invoking the CVS scheme and frozen-core approximation in the calculations of initial and final
states in the Auger process (more details about CVS can be found in Section [7.9.9](sub_cvs_eom.md)).

The initial (bound-like) state $\Psi_{0}$ is a core-hole ionized or
core-hole excited state, which can be described by CVS-EOM-CC.
The final (continuum-like) state $\chi_{\mu,E_{k}}$ is represented by
an antisymmetrized product of a stable channel state $\Psi_{\mu}$ (described by an appropriate EOM-CC model)
and a continuum orbital
$\phi_{k}$, $\chi_{\mu,E_{k}}\sim{\cal{A}}\{\phi_{k}\Psi_{\mu}\}$.
Note that $\Psi_{\mu}$ is a state with one electron less than $\Psi_{0}$.
Two essential parameters defining AES are the rate of the
decay into a channel $\mu$, given as

<a id="eqn:gamma"></a>

$$
\Gamma_{\mu}=2\pi\langle\Psi_{0}^{L}|\hat{H}-E_{0}|\chi_{\mu,E_{k}}^{R}\rangle\langle\chi_{\mu,E_{k}}^{L}|\hat{H}-E_{0}|\Psi_{0}^{R}\rangle, \tag{7.105}
$$

and partial energy correction $\Delta_{\mu}$ to the zero-order resonance position $E_{0}$, defined as

<a id="eqn:delta"></a>

$$
\Delta_{\mu}=P.V.\int_{0}^{\infty}\frac{\langle\Psi_{0}^{L}|\hat{H}-E_{0}|\chi_{\mu,E}^{R}\rangle\langle\chi_{\mu,E}^{L}|\hat{H}-E_{0}|\Psi_{0}^{R}\rangle}{E_{0}-E_{\mu}-E}dE. \tag{7.106}
$$

In the expressions above $\hat{H}$ is the electronic Hamiltonian,
$E_{\mu}$ is the energy of the channel state $\Psi_{\mu}$,
$E_{k}$ is the energy of the ejected electron ($E_{k}=E_{0}-E_{\mu}$),
$L/R$ superscripts denote left and right
EOM-CCSD wave functions, and $P.V.$ stands for the Cauchy principle value.
Calculations of $\Gamma_{\mu}$ are activated with the CC_DO_FESHBACH keyword.
By default, the continuum orbital $\phi_{k}$ is approximated with a plane
wave.[[1262]](../bib_references/bib.md#bib1316)

It is also possible to model $\phi_{k}$ with a Coulomb wave by setting CC_FESHBACH_CW = 1.
This option requires an additional input section *$coulomb_wave*, which provides
the Coulomb wave parameters for the expansion of the Coulomb wave in terms of product of a plane wave
and Gaussian-type functions (PW-CGTOs), as detailed in Ref. [[1262]](../bib_references/bib.md#bib1316)
. The parameters
are listed below.

> ```qchem
> $coulomb_wave
>    lmax   =   4      ! Maximum angular momentum in the pseudo partial wave expansion
>    ncoeff =   6      ! Number of contraction coefficient for each \emph{l}
>    Rmin   =   0.05   ! PW-CGTO grid in atomic unit
>    Rmax   =   10
>    Rmid   =   2
>    Charge =   6.2    ! Effective charge of the Coulomb wave
>    cwave_center = 1  ! Atom index for the position of Coulomb wave. Starts from 1.
>    print_cw = false  ! For printing the partial wave and the PW-CGTO basis
> $end
> ```

The Coulomb wave is approximated by the linear combination of PW-CGTOs. Typically,
*lmax* = 4-6 and *ncoeff* = 6-8 provide a good approximation;
increasing these values significantly increases computational cost.
The grid is set up by the
*Rmin*, *Rmax*, and *Rmid* parameters.
If *Rmid* is specified, the grid spacing is set to 0.05 bohr from *Rmin* to
*Rmid* and 0.1 bohr from *Rmid* to *Rmax*. If *Rmid* is not provided,
a uniform grid spacing of 0.1 bohr is used. The grid should be large enough
to accurately represent the continuum function in the space where bound-domain orbitals
involved in the decay have considerable amplitudes.
The *cwave_center* sets the position of the Coulomb wave.
By default, it is at the origin (*cwave_center = 0*). One can place it at a specific
atom or any other location, such as the midpoint of a bond, by
defining a ghost atom (Gh) in the input and setting its index as the *cwave_center*.
The *print_cw* option enables printing the Coulomb wave, its fitted
representation (for each *l*), and the corresponding Coulomb
basis. The user can check the *Fit square error:* in the
**Q-Chem** output file and adjust these parameters
accordingly by varying *ncoeff*.

It is also possible to provide the direct expansion of the Coulomb wave in terms of PW-CGTOs from external
optimization (for the given effective charge and kinetic energy) in the input section *$coulomb_wave*. This
is enabled by setting CC_FESHBACH_CW = 3.

The implementation of Feshbach widths includes numerical integration over all possible
directions of the emitted electron (**k**-vector). This integration over the sphere is
carried out using Lebedev’s quadrature, with the default order of 5. For molecules with
delocalized core-hole states (e.g., benzene), higher-order quadrature may be needed.
The order of the quadrature is controlled by CC_FESHBACH_INT_ORDER.
Examples [7.9.11.2](#ex:auger1) and [7.9.11.2](#ex:auger1) below illustrate calculations of auger decay rates using plane-wave and Coulomb wave treatments.

For non-resonant Auger decay, the initial state can be conveniently computed by
CVS-EOM-IP-CCSD and its stable decay channels can be computed by EOM-DIP-CCSD.
A section of the input invoking Auger decay rates
calculation for an atom can be given as:

> ```qchem
> $rem
>    JOBTYPE         sp
>    METHOD          eom-ccsd
>    basis           6-31G*
>    CVS_EOM_IP_BETA [1,0,0,0,0,0,0,0] !This is the initial core-hole state
>    DIP_TRIPLETS    [0,0,0,0,0,1,1,1] !These are the final triplet decay channels
>    DIP_SINGLETS    [3,1,1,1,0,1,1,1] !These are the final singlet decay channels
>    CC_DO_DYSON     1                 !Needed for Feshbach-type calculations
>    CC_DO_FESHBACH  1
> $end
> ```

In resonant Auger decay, the initial state can be computed by
CVS-EOM-EE-CCSD and the corresponding decay channels can be computed by EOM-IP-CCSD.
By default, Feshbach calculations are performed for all possible state pairs that
include an energetically allowed decay channel. This is not practical
if, for example, the core-hole state of interest is not the lowest state in the
given symmetry, or when the Coulomb wave is used to model the continuum orbital.
In such a case, the user can specify pairs of states for Feshbach calculations
using the *$trans_prop* section with $dyson$ as the requested property:

> ```qchem
> $trans_prop
>    state_list
>    cvs_ip_beta  1 1 !state 1: CVS_IP with irrep = 1 and istate = 1
>    dip_singlets 1 3 !state 2: DIP_SINGLET state with irrep = 1 and istate = 3
>    dip_triplets 6 1 !state 3: DIP_TRIPLET state with irrep = 6 and istate = 1
>    end_list
>    state_pair_list
>    1 2   ! transition 1 <-> 2
>    1 3   ! transition 1 <-> 3
>    end_pairs
>    calc dyson
> $end
> ```

Calculations of energy correction $\Delta_{\mu}$
are invoked by setting CC_DO_FESHBACH = 2,
and are currently available only within the plane-wave approximation.

The integrals in Eq. ([7.105](#eqn:gamma)) are evaluated analytically. Integration in
Eq. ([7.106](#eqn:delta)) is done numerically, and
is split into two or three intervals to bypass the singularity at $E=E_{0}-E_{\mu}$. The upper limits of those intervals
are set to default values related to $E_{0}$. They can also be customized
(except for the first interval) by setting CC_FESHBACH_DELTA_INTB = XX and/or
CC_FESHBACH_DELTA_INTC = YY where XX and/or YY are desired upper integration limits in units of eV.

A molecular-orbital description of the Auger process (or other two-electron decay processes such as intermolecular Coulomb and electron-transfer-mediated decay) can be obtained from
the singular-value decomposition of the two-particle Dyson amplitudes ($\Gamma_{\mu}$)[[631]](../bib_references/bib.md#bib655)
. The procedure yields several
three-orbital sets, which represent the core-vacancy state and the valence decay states. These sets, called Natural Auger Orbitals, provide the most compact
description of the two-electron decay process[[631]](../bib_references/bib.md#bib655)
. The calculations of NAOs can be invoked within Feshbach calculations by the
CC_DO_NAO keyword. The NAOs are printed in the **MolDen** format in a subdirectory created in the working directory. The “energies”
are the squares of singular values (not normalized), core-hole NAOs are assigned populations of 1, and valence decay NAOs are assigned populations of 0.
The default threshold for
the NAOs to be printed is 0.20. It can be controlled by the user using the WFA_ORB_THRESH keyword (see Section [10.2](../ch10_properties/sec_wfa.md)). This feature is illustrated in examples
[7.9.11.2](#ex:auger1), [7.9.11.2](#ex:auger1), and [7.9.11.2](#ex:auger1) below.

**Note: 

NAOs are computed using $\Gamma_{r\beta}^{p\alpha,q\beta}$ block of the two-body Dyson amplitude. This means that in the non-resonant Auger decay calculations, the core hole
should correspond to removing $\beta$-electron.
**

### `CC_DO_FESHBACH`

> **Activates calculation of resonance widths using Feshbach-Fano approach.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: do not invoke Feshbach-Fano calculation
>     * `1`: invoke Feshbach-Fano calculation of the resonance width
>     * `2`: invoke Feshbach-Fano calculation of the resonance width and resonance shift
> * **Recommendation**: Initial and final states should be correctly specified.

### `CC_FESHBACH_CW`

> **Activates Coulomb wave description of the ejected electron.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Use plane wave
>     * `1`: Use Coulomb wave generated internally
>     * `3`: Use Coulomb basis provided by the user in the $coulomb_wave section
> * **Recommendation**: Additional details need to be specified in $coulomb_wave section.

### `CC_FESHBACH_INT_ORDER`

> **Controls k-vector integration grid in calculations of resonance widths using Feshbach-Fano approach.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: corresponds to the Lebedev quadrature order
> * **Recommendation**: Use default, unless tighter convergence is desired (16 gives fully converged widths).

### `CC_FESHBACH_DELTA_INTB`

> **Specifies integration limits in calculation of energy shift in Feshbach-Fano calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `Preset`
> * **Options**:
>     * $n$: corresponds to energy limit in eV
> * **Recommendation**: Use default.

### `CC_FESHBACH_DELTA_INTC`

> **Specifies integration limits in calculation of energy shift in Feshbach-Fano calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `Preset`
> * **Options**:
>     * $n$: corresponds to energy limit in eV
> * **Recommendation**: Use default.

### `CC_DO_NAO`

> **Activates calculation of NAOs within Feshbach–Fano calculation of the decay widths.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: do not compute NAOs
>     * `1`: compute NAOs
> * **Recommendation**: Initial and final states should be correctly specified.

## 7.9.11.1 One-Center Approximation

The Feshbach–Fano calculations of Auger decay that treat the continuum orbital $\phi_{k}$ explicitly[[1262]](../bib_references/bib.md#bib1316)

entail the evaluation of the mixed bound–continuum two-electron integrals, which
is a computationally demanding step. Moreover, the currently available $\phi_{k}$ models only
allow a plane wave or a Coulomb wave treatments, which do not always yield fully satisfactory results.

A widely used and computationally efficient alternative to the explicit treatment of the continuum state is
the one-center approximation (OCA).[[1264]](../bib_references/bib.md#bib1318)
 In this approach, the bound–continuum integrals are replaced by pretabulated
atomic integrals:

<a id="Ch7.E107"></a>

$$
\langle\phi_{p}\phi_{q}||\phi_{k}\phi_{r}\rangle\approx\sum_{\mu\nu\rho}\langle\chi_{\mu}^{A}\chi_{\nu}^{A}||\chi_{E,lm}^{A}\chi_{\rho}^{A}\rangle D_{\mu p}D_{\nu q}D_{\rho r}. \tag{7.107}
$$

Here $\langle\chi_{\mu}^{A}\chi_{\nu}^{A}||\chi_{E,lm}^{A}\chi_{\rho}^{A}\rangle$ denote the precomputed atomic integrals and
$D_{\mu p}$ are transformation matrices constructed by the projection of the molecular basis onto the chosen Minimal
Basis Set (MBS).

Similarly to the standard Feshbach–Fano setup described above, the OCA calculation requires specification of the initial core-ionized state (CVS-EOM-IP or CVS-EOM-EE) and the final decay channels (EOM-DIP or EOM-IP).
The method is controlled by two keywords: CC_FESHBACH_OCA and OCA_ATOM_INDEX.
The keyword CC_FESHBACH_OCA activates the OCA calculation and currently supports two options: 1 for $1s$
core holes (K-LL, K-LM, and K-MM decays) and 2 for $2s$ core holes (only L1-MM decay).
The keyword OCA_ATOM_INDEX = $n$
specifies the atom on which the core hole is localized. The indexing starts from 1 and follows the order given
in the *$molecule* section. For larger systems, it is recommended to use
PRINT_ORBITALS option to verify proper identification of the core orbital.
For cases where the core hole is delocalized over symmetry-equivalent atoms (e.g., benzene or the O-edge in CO${}_{2}$,
OCA_ATOM_INDEX may correspond to any equivalent atom. The final decay width $\Gamma$ for a given channel
$\mu$ is then obtained by summing over the corresponding symmetry-equivalent core-hole states $\Psi_{0}$.

In addition, an OCA calculation requires specification of a Minimal Basis Set (MBS) through the *$mbasis*
section. The ordering of basis functions is important and must follow the shell structure:
$(1s,2s,2p,\ldots)$. Two MBS choices for OCA-EOM-CCSD calculations were tested[[1264]](../bib_references/bib.md#bib1318)
: a
subset of the cc-pVTZ basis set and STO-3G.

Examples [7.9.11.2](#ex:auger1) and [7.9.11.2](#ex:auger1) illustrate OCA calculations.

### `CC_FESHBACH_OCA`

> **Activates Auger width calculation through OCA method.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: 1s core-hole
>     * `2`: 2s core-hole.
> * **Recommendation**: None

### `OCA_ATOM_INDEX`

> **Defines atom with core-hole.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$: follows order from molecule section.
> * **Recommendation**: None

## 7.9.11.2 Examples

Examples [7.9.11.2](#ex:auger1) and [7.9.11.2](#ex:auger1) illustrate calculation of resonant
Auger decay of core-ionized water molecule. The initial state is described by
CVS-EOM-IP-CCSD and the decay channels are described by EOM-DIP-CCSD.
Example [7.9.11.2](#ex:auger1) uses a plane-wave representation of the ejected electron.
In example [7.9.11.2](#ex:auger1), the autoionizing electron is described by the Coulomb
wave, represented by a pseudo-partial wave expansion over PW-CGTO functions.
Examples [7.9.11.2](#ex:auger1), [7.9.11.2](#ex:auger1), and [7.9.11.2](#ex:auger1) illustrate calculations of NAOs for regular and resonant Auger decay.

???+ example "Example 7.79: Calculation of Auger decay rates of core-ionized water molecule
to selected singlet and triplet final states.
Continuum orbital is a plane wave."
    ```qchem
    $molecule
    0 1
       O         0.0000    0.000    0.0000
       H        -0.7528    0.000   -0.5917
       H         0.7528    0.000   -0.5917
    $end
    
    $rem
       METHOD            ccsd
       BASIS             6-311+G(3df)
       CVS_EOM_IP_BETA   [1,0,0,0]
       DIP_SINGLETS      [4,1,2,2]
       DIP_TRIPLETS      [1,1,2,2]
       CC_DO_DYSON       1
       CC_DO_FESHBACH    1
    $end
    ```

???+ example "Example 7.80: Calculation of Auger decay rates of core-ionized water molecule
to selected singlet and triplet final states.
Continuum orbital is approximated by a Coulomb wave."
    ```qchem
    $molecule
    0 1
       O         0.0000    0.000    0.0000
       H        -0.7528    0.000   -0.5917
       H         0.7528    0.000   -0.5917
    $end
    
    $rem
       METHOD            ccsd
       BASIS             6-311+G(3df)
       CVS_EOM_IP_BETA   [1,0,0,0]
       DIP_TRIPLETS      [1,1,2,2]
       CC_DO_DYSON       1
       CC_DO_FESHBACH    1
       CC_FESHBACH_CW    1
    $end
    
    $trans_prop
    state_list
      cvs_ip_beta  1 1
      dip_triplets 3 2
    end_list
    state_pair_list
      1 2   ! transition 1 <-> 2
    end_pairs
    calc dyson
    $end
    
    $coulomb_wave
    lmax = 4
    ncoeff = 6
    Rmin = 0.05
    Rmax = 10
    Rmid = 2
    Charge = 4.9
    cwave_center = 1  !CW is centered on oxygen (atom #1)
    print_cw = false
    $end
    ```

???+ example "Example 7.81: Calculation of Natural Auger Orbitals for regular (non-resonant) Auger decay in water for both singlet and triplet decay channels."
    ```qchem
    $comment
    NAO calculation - regular Auger decay in water
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    
    $rem
    jobtype              sp
    method               eom-ccsd
    basis                6-31g
    cvs_eom_ip_beta      [1,0,0,0]  !Initial core-hole state
    dip_singlets         [1,1,0,0]  !Final singlet decay channels
    dip_triplets         [0,1,0,0]  !Final triplet decay channels
    cc_do_dyson          1          !Needed for Feshbach-type calculations
    cc_do_feshbach       1          !Needed for Feshbach-type calculations
    cc_do_nao            1          !Needed for natural Auger orbitals
    wfa_orb_thresh       1          !Setting the threshold for singular value dceomposition
    mem_total            4000
    $end
    
    
    ```

???+ example "Example 7.82: Calculation of Natural Auger Orbitals for regular (non-resonant) Auger decay in benzene for both singlet and triplet decay channels, and for
several core-hole states."
    ```qchem
    $comment
    NAO calculation - regular Auger decay in benzene
    $end
    
    $molecule                                                                                                                         0 1
      H   2.4750347531   0.0000000000   0.0000000000
      C   1.3935929418   0.0000000000   0.0000000000
      C   0.6967964709   1.2068868901   0.0000000000
      H   1.2375173766   2.1434429715   0.0000000000
      C  -0.6967964709   1.2068868901   0.0000000000
      H  -1.2375173766   2.1434429715   0.0000000000
      C  -1.3935929418   0.0000000000   0.0000000000
      H  -2.4750347531   0.0000000000   0.0000000000
      C  -0.6967964709  -1.2068868901   0.0000000000
      H  -1.2375173766  -2.1434429715   0.0000000000
      C  0.6967964709   -1.2068868901   0.0000000000
      H  1.2375173766   -2.1434429715   0.0000000000
    $end
    
    $rem
    jobtype             sp
    method              ccsd
    basis               6-31g
    cvs_eom_ip_beta     [1,0,0,0,0,0,1,1] !Initial core-hole state
    dip_singlets        [2,0,0,1,0,0,0,0] !Final singlet decay channel
    dip_triplets        [1,0,0,1,0,0,0,0] !Final triplet decay channel
    cc_do_dyson         1                 !Needed for Feshbach-type calculation
    cc_do_feshbach      1                 !Needed for Feshbach-type calculation
    cc_do_nao           1                 !Needed for natural Auger orbital calculation
    mem_total           8000
    $end
    ```

???+ example "Example 7.83: Calculation of Natural Auger Orbitals for resonant Auger decay in water."
    ```qchem
    $comment
    NAO calculation - resonant Auger decay in water
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    
    $rem
    jobtype              sp
    method               eom-ccsd
    basis                6-31g
    cvs_ee_states        [1,0,0,0]  !Initial core-hole state
    ip_states            [1,0,1,0]  !Final  decay channels
    cc_do_dyson          1          !Needed for Feshbach-type calculations
    cc_do_feshbach       1          !Needed for Feshbach-type calculations
    cc_do_nao            1          !Needed for natural Auger orbitals
    mem_total            4000
    $end
    
    
    ```

???+ example "Example 7.84: Calculation of Auger decay rates of core-ionized water molecule
using OCA"
    ```qchem
    $comment
    OCA-EOM-CCSD Auger width calculation for core-ionized H2O(1s^-1)
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    $rem
    jobtype = sp
    basis = cc-pVTZ
    method = ccsd
    dip_singlets [1,0,0,0]
    cvs_eom_ip_beta [1,0,0,0]
    cc_do_dyson 1
    cc_feshbach_oca = 1 ! 1s core
    oca_atom_index = 1  ! Core localized on oxygen atom
    $end
    
    $mbasis
    !Subset of cc-pVTZ  used as Minimal Basis Set
    H     0
    S   5   1.00
          3.387000D+01           6.068000D-03
          5.095000D+00           4.530800D-02
          1.159000D+00           2.028220D-01
          3.258000D-01           5.039030D-01
          1.027000D-01           3.834210D-01
    ****
    O     0
    S   10   1.00
          1.533000D+04           5.080000D-04
          2.299000D+03           3.929000D-03
          5.224000D+02           2.024300D-02
          1.473000D+02           7.918100D-02
          4.755000D+01           2.306870D-01
          1.676000D+01           4.331180D-01
          6.207000D+00           3.502600D-01
          1.752000D+00           4.272800D-02
          6.882000D-01          -8.154000D-03
          2.384000D-01           2.381000D-03
    S   10   1.00
          1.533000D+04          -1.150000D-04
          2.299000D+03          -8.950000D-04
          5.224000D+02          -4.636000D-03
          1.473000D+02          -1.872400D-02
          4.755000D+01          -5.846300D-02
          1.676000D+01          -1.364630D-01
          6.207000D+00          -1.757400D-01
          1.752000D+00           1.609340D-01
          6.882000D-01           6.034180D-01
          2.384000D-01           3.787650D-01
    P   5   1.00
          3.446000D+01           1.592800D-02
          7.749000D+00           9.974000D-02
          2.280000D+00           3.104920D-01
          7.156000D-01           4.910260D-01
          2.140000D-01           3.363370D-01
    ****
    $end
    
    ```

???+ example "Example 7.85: Calculation of Auger decay rates of core-ionized CO ${}_{2}$ molecule
using OCA"
    ```qchem
    $comment
    OCA-EOM-CCSD Auger width calculation for core-ionized CO2 (O-edge 1s^-1)
    The core orbital is delocalized over two oxygen atoms
    For equivalent core atoms (O1 and O2) the final result is the sum
    over the two initial cvs_ip states in irreps A1g and B1u
    oca_atom_index can be chosen as 2 or 3
    $end
    
    $molecule
    0 1
    C         0.0000000000    0.0000000000    0.0000000000
    O         0.0000000000    0.0000000000    1.1702258366
    O         0.0000000000    0.0000000000   -1.1702258366
    $end
    
    $rem
    jobtype = sp
    basis = cc-pVTZ
    method = ccsd
    dip_singlets [1,0,0,0,0,0,0,0]
    cvs_eom_ip_beta [1,0,0,0,0,1,0,0]
    cc_do_dyson 1
    cc_feshbach_oca = 1   ! 1s decay
    oca_atom_index = 2    ! Second atom (O1) is chosen as OCA core
    n_frozen_core = 2     ! O-edge
    $end
    
    $mbasis
    !STO-3G is used as Minimal Basis Set
    C     0
    S   3   1.00
          0.7161683735D+02       0.1543289673D+00
          0.1304509632D+02       0.5353281423D+00
          0.3530512160D+01       0.4446345422D+00
    SP   3   1.00
          0.2941249355D+01      -0.9996722919D-01       0.1559162750D+00
          0.6834830964D+00       0.3995128261D+00       0.6076837186D+00
          0.2222899159D+00       0.7001154689D+00       0.3919573931D+00
    ****
    O     0
    S   3   1.00
          0.1307093214D+03       0.1543289673D+00
          0.2380886605D+02       0.5353281423D+00
          0.6443608313D+01       0.4446345422D+00
    SP   3   1.00
          0.5033151319D+01      -0.9996722919D-01       0.1559162750D+00
          0.1169596125D+01       0.3995128261D+00       0.6076837186D+00
          0.3803889600D+00       0.7001154689D+00       0.3919573931D+00
    ****
    $end
    
    ```
