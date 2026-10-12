---
title: "5.6.4 Tuned RSH Functionals"
---

## 5.6.4 Tuned RSH Functionals

(July 4, 2026)

Whereas the range-separation parameters for the functionals described in
Section [5.6.2](subsec_wb97series.md) are wholly empirical in nature and should not
be adjusted, for the functionals described in
Section [5.6.3](ex_ks-wb97xd4.md) some adjustment *was* suggested,
especially for TDDFT calculations and for any properties that require
interpretation of orbital energies, such as HOMO/LUMO gaps. This
adjustment can be performed in a non-empirical (albeit system-specific) way,[[60]](../bib_references/bib.md#bib45)

by “tuning” the value of $\omega$ in order to satisfy the Koopmans-like ionization energy criterion

<a id="eq:IP-tuning"></a>

$$
-\epsilon_{\rm HOMO}(\omega)=\mbox{IE}(\omega) \tag{5.18}
$$

where $\mbox{IE}=E(N-1)-E(N)$ is the $\Delta$SCF value of the ionization energy for the
$N$-electron system of interest. The condition $\epsilon_{\rm HOMO}=-\mbox{IE}$ is a theorem
in exact DFT,[[1065]](../bib_references/bib.md#bib1113)
 but this condition is often badly violated by approximate functionals.
When an RSH functional is used, both sides of Eq. ([5.18](#eq:IP-tuning)) are $\omega$-dependent and
this parameter is adjusted until the condition in Eq. ([5.18](#eq:IP-tuning)) is
met, which requires a sequence of SCF calculations on both the neutral and
ionized species, using different values of $\omega$. The value that is obtained has come to be called
the “optimally tuned” value of $\omega$.
Formally speaking, there is no guarantee
that an approximate density functional can be made to satisfy
Eq. ([5.18](#eq:IP-tuning)) for any given molecule, thus the optimally-tuned value need not exist.
In practice it is usually possible to find such a value, although it should be noted that the optimally-tuned
value of $\omega$ depends on system size, and as a result this tuning procedure formally violates
size-consistency.[[667]](../bib_references/bib.md#bib692)

A few variations on the simple “IE tuning” criterion in Eq. ([5.18](#eq:IP-tuning)) are possible.
For proper description
of charge-transfer states, Baer and co-workers[[60]](../bib_references/bib.md#bib45)
 suggest finding
the value of $\omega$ that (to the extent possible) satisfies
Eq. ([5.18](#eq:IP-tuning)) for both the neutral donor molecule and (separately) for the *anion*
of the acceptor species. Along similar lines, in an effort to set both the HOMO
and LUMO energy levels such that the fundamental gap ($\mbox{IE}-\mbox{EA}$) is equal to the HOMO/LUMO
gap, Kronik *et al.*[[720]](../bib_references/bib.md#bib751)
 suggest minimizing the function

<a id="eq:J(w)"></a>

$$
J(\omega)=\big{[}\epsilon_{\rm HOMO}(\omega)+\mbox{IE}(\omega)\big{]}^{2}+\big{[}\epsilon_{\rm LUMO}(\omega)+\mbox{EA}(\omega)\big{]}^{2} \tag{5.19}
$$

with respect to $\omega$, where $\mbox{EA}=E(N+1)-E(N)$. Minimization of $J(\omega)$ represents an attempt
to satisfy the IE theorem of Eq. ([5.18](#eq:IP-tuning)) for both the $N$-electron molecule and its ($N+1$)-electron anion,
assuming that the latter is bound.
Published benchmarks suggest that these system-specific approaches afford the
most accurate values of IEs and TDDFT excitation
energies.[[851]](../bib_references/bib.md#bib885)

A script that optimizes $\omega$, called `OptOmegaIPEA.pl`, is located in
the `$QC/bin/tools` directory. The script scans $\omega$ over the range
0.1–0.8 bohr${}^{-1}$, corresponding to values of the *$rem* variable
OMEGA in the range 100–800. See the script for the instructions how
to modify the script to scan over a wider range.
To execute the script, the user must create three inputs for an RSH single-point energy calculation,
using the same geometry and basis
set: one for a neutral molecule (`N.in`), one for its anion (`M.in`), and one for the molecule’s
cation (`P.in`). The user should then run the command

> ```qchem
> OptOmegaIPEA.pl >& optomega
> ```

This command both generates the input files (`N_*`, `P_*`, `M_*`) and also
runs **Q-Chem** on these input files, writing the optimization output into `optomega`.
This script applies the IE condition to both the neutral molecule and its
anion, minimizing $J(\omega)$ in Eq. ([5.19](#eq:J(w))).
A similar script, `OptOmegaIP.pl`, uses Eq. ([5.18](#eq:IP-tuning)) for the neutral molecule only.

!!! note "Note"
    1.

    If the system does not have positive EA, then the tuning should be done
    according to the IP condition only. The IP/EA script will yield an
    incorrect value of $\omega$ in such cases.

    2.

    In order for the scripts to work, one must specify
    SCF_FINAL_PRINT = 1 in the inputs. The scripts look for
    specific regular expressions and will not work correctly without this
    keyword.


Although the tuning procedure was originally developed by Baer and co-workers
using the BNL functional,[[851]](../bib_references/bib.md#bib885)
 it can equally well be applied to any RSH
functional, as for example LRC-$\omega$PBE (see,
Ref. [[1380]](../bib_references/bib.md#bib1441)
). The aforementioned scripts will work with these other RSH functionals as well.

Unfortunately, optimally-tuned values of “$\omega_{\text{IE}}$”, obtained by satisfying the criterion in Eq. ([5.18](#eq:IP-tuning))
exhibit a troubling dependence on system
size,[[710]](../bib_references/bib.md#bib742)

leading to a loss of size-extensivity.[[667]](../bib_references/bib.md#bib692)
 For example, the optimally-tuned
value for the cluster anion (H${}_{2}$O)${}^{-}_{6}$ is very different than the one tuned for (H${}_{2}$O)${}^{-}_{70}$,[[1380]](../bib_references/bib.md#bib1441)

and the optimally-tuned value also varies with conjugation length for
$\pi$-conjugated systems.[[710]](../bib_references/bib.md#bib742)
 An alternative to the IE-based criterion in Eq. ([5.18](#eq:IP-tuning))
is the global density-dependent (GDD)
tuning procedure,[[956]](../bib_references/bib.md#bib997)
 in which the optimal value

<a id="eq:wgdd"></a>

$$
\omega_{\text{GDD}}=C\langle d^{2}_{\text{x}}\rangle^{-1/2} \tag{5.20}
$$

is related to the average of the distance $d_{\text{x}}$ between an electron in
the outer regions of a molecule and the exchange hole in the region of
localized valence orbitals. The quantity $C$ is an empirical parameter for a
given LRC functional, which was determined for LRC-$\omega$PBE ($C=0.90$) and
LRC-$\omega$PBEh ($C=0.75$),[[956]](../bib_references/bib.md#bib997)
 in order to ensure that $\omega_{\text{GDD}}\approx\omega_{\text{IE}}$
in small molecules. (A slightly different value, $C=0.885$, was
determined for **Q-Chem**’s implementation of LRC-$\omega$PBE.[[764]](../bib_references/bib.md#bib798)
)
For TD-DFT calculations in small molecules, the choice of $\omega_{\text{GDD}}$ versus $\omega_{\text{IE}}$ makes
essentially no difference, while the former can be considerably cheaper (and more convenient) as compared to searching
for the value $\omega_{\text{IE}}$.[[880]](../bib_references/bib.md#bib915)

Since LRC-$\omega_{\text{GDD}}$PBE provides a better description of
polarizabilities in polyacetylene as compared to
$\omega_{\text{IE}}$,[[526]](../bib_references/bib.md#bib540)
 it is anticipated that using $\omega_{\text{GDD}}$ in
place of $\omega_{\text{IE}}$ may afford more accurate molecular properties,
especially in conjugated systems where IE tuning sometimes encounters problems related to vanishing
HOMO/LUMO gaps.[[480]](../bib_references/bib.md#bib491)

GDD tuning of an RSH functional is
involving by setting the *$rem* variable OMEGA_GDD = TRUE.
The electron density is needed to compute $\omega_{\text{GDD}}$ in
Eq. ([5.20](#eq:wgdd)) and this is accomplished using the converged SCF density
computed using the RSH functional with the value of $\omega$ given by the
*$rem* variable OMEGA. The value of $\omega_{\text{GDD}}$ therefore
depends, in principle, upon the value of OMEGA, although in practice
it is not very sensitive to this value and results obtained in this way are similar to fully self-consistent values
of $\omega_{\text{GDD}}$.[[956]](../bib_references/bib.md#bib997)

### `OMEGA_GDD`

> **Controls the application of $\omega_{\text{GDD}}$ tuning for long-range corrected DFT**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Do not apply GDD tuning.
>     * `TRUE`（或 `1`）: Use GDD tuning.
> * **Recommendation**: The $rem variable OMEGA must also be specified, in order to set the initial range-separation parameter.

### `OMEGA_GDD_SCALING`

> **Sets the empirical constant $C$ in the GDD tuning procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `885`
> * **Options**:
>     * $n$: Corresponding to $C=n/1000$ .
> * **Recommendation**: The quantity $C=0.885$ ( $n=885$ ) was determined in Ref. 764 Lao K. U., Herbert J. M. J. Chem. Theory Comput. (2018) , 14 , pp. 2955 . Link using LRC- $\omega$ PBE/hpTZVPP calculations.

???+ example "Example 5.9: Sample input illustrating a calculation to determine the $\omega$ value for
LRC- $\omega$ PBE based on the GDD tuning procedure."
    ```qchem
    $comment
       The initial omega value has to set.
    $end
    
    $molecule
       0 1
       O   -0.042500   0.091700   0.110000
       H    0.749000   0.556800   0.438700
       H   -0.825800   0.574700   0.432500
    $end
    
    
    $rem
       EXCHANGE          gen
       BASIS             aug-cc-pvdz
       LRC_DFT           true
       OMEGA             300
       OMEGA_GDD         true
    $end
    
    $xc_functional
       X   wPBE   1.0
       C    PBE   1.0
    $end
    ```

However the tuning is accomplished, these tuned functionals are generally thought to work by
reducing self-interaction error in approximate DFT.
A convenient way to quantify—or at least depict—this
error is by plotting the DFT energy as a function of the (fractional) number of
electrons, $N$, because $E(N)$ should in principle consist of a sequence of
line segments with abrupt changes in slope (the so-called derivative
discontinuity[[261]](../bib_references/bib.md#bib262)
) at integer values of $N$,
but in practice these $E(N)$ plots bow away from straight-line
segments.[[261]](../bib_references/bib.md#bib262)
 Examination of such plots has been suggested as a
means to adjust the fraction of short-range exchange in an RSH
functional,[[58]](../bib_references/bib.md#bib41)
 while the $\omega$ parameter is set by tuning.

### `FRACTIONAL_ELECTRON`

> **Add or subtract a fraction of an electron.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Use an integer number of electrons.
>     * $n$: Add $n/1000$ electrons to the system.
> * **Recommendation**: Use only if trying to generate $E(N)$ plots. If $n<0$ , a fraction of an electron is removed from the system.

???+ example "Example 5.10: Example of a DFT job with a fractional number of electrons. Here, we make the $-1.x$ anion of fluoride by subtracting a fraction of an electron from the HOMO
of F ${}^{2-}$ ."
    ```qchem
    $comment
       Subtracting a whole electron recovers the energy of F-.
       Adding electrons to the LUMO is possible as well.
    $end
    
    $molecule
       -2 2
       F
    $end
    
    $rem
       EXCHANGE              b3lyp
       BASIS                 6-31+G*
       FRACTIONAL_ELECTRON  -500   ! divide by 1000 to get the fraction, -0.5 here.
       GEN_SCFMAN            FALSE ! not yet available in new scf code
    $end
    ```

Another, alternative to IE-based tuning is the effective (EFF) tuning procedure [[1257]](../bib_references/bib.md#bib1312)
, in which the optimal value of the range-separation parameter is given by

<a id="mu-eff"></a>

$$
\omega=\frac{a_{1}}{\langle r_{s}\rangle}+\frac{a_{2}\langle r_{s}\rangle}{1+a_{3}\langle r_{s}\rangle^{2}}~{}, \tag{5.21}
$$

where $a_{1}=1.91718$, $a_{2}=-0.02817$, and $a_{3}=0.14954$. The local Seitz radius is defined as
$r_{s}=\left(\frac{3}{4\pi n}\right)^{1/3}$, with $n=n_{\uparrow}+n_{\downarrow}$. The quantity $\langle r_{s}\rangle$ denotes the volume-averaged Seitz radius.

While $\langle r_{s}\rangle$ is straightforward to compute for bulk solids, special care is required for finite systems such as atoms and molecules, where $r_{s}$ diverges in the low-density tail.
To address this issue, a weighted average of $r_{s}$ is employed:

<a id="eq:rs-average"></a>

$$
\langle r_{s}\rangle=\frac{\int w(\mathbf{r})\,r_{s}(\mathbf{r})\,d^{3}r}{\int
w(\mathbf{r})\,d^{3}r}\;. \tag{5.22}
$$

Here, the weight function $w(\mathbf{r})$ is constructed to emphasize regions where the electron density is significant (i.e., core and valence regions).
For further details on the construction of the weight function and its derivation, we refer to Ref. [[1257]](../bib_references/bib.md#bib1312)
.

The LRC-$\omega_{\text{EFF}}$PBE functional has been shown to provide an improved description of charge-transfer excitations, HOMO-LUMO gaps, and excitonic properties.

In practice, EFF tuning of an RSH functional is enabled by setting the *$rem* variable OMEGA_EFF = TRUE.
The evaluation of $\omega_{\text{EFF}}$ in Eq. ([5.21](#mu-eff)) requires the electron density, which is obtained from a converged SCF calculation.
When using an RSH functional, an initial value of $\omega$ must be specified via the *$rem* variable OMEGA. In contrast, for semilocal or global hybrid functionals (e.g., PBE or B3LYP), specifying OMEGA is not required.

### `OMEGA_EFF`

> **Controls the application of $\omega_{\text{EFF}}$ tuning for long-range corrected DFT**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Do not apply EFF tuning.
>     * `TRUE`（或 `1`）: Apply EFF tuning.
> * **Recommendation**: The $rem variable OMEGA must also be specified to provide an initial value for the range-separation parameter.

???+ example "Example 5.11: Sample input illustrating a calculation to determine the $\omega$ value using EFF tuning procedure."
    ```qchem
    $comment
    w_EFF tuning for anthracene molecule
    Effective (eff) tunning of the range-separation parameter, w
    J. Phys. Chem. Lett. 2025, 16, 32, 8198–8208
    $end
    
    
    $molecule
    0 1
      Ne  0 0 0
    $end
    
    $rem
    METHOD           PBE
    BASIS            cc-pVDZ
    OMEGA_EFF       true
    SCF_CONVERGENCE  7
    MAX_SCF_CYCLES   100
    XC_GRID          000099000590
    THRESH           14
    SYM_IGNORE       TRUE
    $end
    ```
