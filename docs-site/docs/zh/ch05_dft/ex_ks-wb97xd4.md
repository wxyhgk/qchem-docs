---
title: "5.6.3 User-Defined RSH Functionals"
---

## 5.6.3 User-Defined RSH Functionals

(July 4, 2026)

As pointed out in Ref. [[352]](../bib_references/bib.md#bib356)
 and elsewhere, the description
of charge-transfer excited states within density functional theory (or more
precisely, time-dependent DFT, which is discussed in Section [7.3](../ch07_excited/sect_tddft.md))
requires full (100%) non-local HF exchange, at least in the limit of large
donor–acceptor distance. Hybrid functionals such as
B3LYP[[96]](../bib_references/bib.md#bib78)
 and PBE0[[20]](../bib_references/bib.md#bib4)
 that are
well-established and in widespread use, however, employ only 20% and 25% HF
exchange, respectively. While these functionals provide excellent results for
many ground-state properties, they cannot correctly describe the distance
dependence of charge-transfer excitation energies, which are enormously
underestimated by most common density functionals. This is a serious problem
in any case, but it is a *catastrophic* problem in large molecules and in
non-covalent clusters, where TDDFT often predicts a near-continuum of spurious,
low-lying charge transfer states.[[750]](../bib_references/bib.md#bib783)
 The problems with
TDDFT’s description of charge transfer are not limited to large donor–acceptor
distances, but have been observed at $\sim$2 Å separation, in systems as
small as uracil–(H${}_{2}$O)${}_{4}$.[[750]](../bib_references/bib.md#bib783)
 Rydberg excitation energies
also tend to be substantially underestimated by standard TDDFT.

One possible avenue by which to correct such problems is to parameterize
functionals that contain 100% HF exchange, though few such functionals exist
to date. An alternative option is to attempt to preserve the form of common
GGAs and hybrid functionals at short range (*i.e.*, keep the 25% HF exchange in
PBE0) while incorporating 100% HF exchange at long range, which provides a
rigorously correct description of the long-range distance dependence of
charge-transfer excitation energies, but aims to avoid contaminating
short-range exchange-correlation effects with additional HF exchange. The
separation is accomplished using the range-separation *ansatz* that was
introduced in Section [5.3](sect_XCfuncs.md). In particular, functionals that use
100% HF exchange at long range ($c_{x,\rm LR}=1$ in Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)))
are known as “long-range-corrected” (LRC) functionals. An LRC version of
PBE0 would, for example, have $c_{x,\rm SR}=0.25$.

To fully specify an LRC functional, one must choose a value for the range
separation parameter $\omega$ in Eq. ([5.12](Ch5.S3.SS1.md#eq:erf_partition)). In the limit
$\omega\rightarrow 0$, the LRC functional in Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) reduces to
a non-RSH functional where there is no “SR” or “LR”, because all exchange
and correlation energies are evaluated using the full Coulomb operator,
$r_{12}^{-1}$. Meanwhile the $\omega\rightarrow\infty$ limit corresponds to a
new functional, $E_{xc}^{\rm RSH}=E_{c}+E_{x}^{\rm HF}$. Full HF exchange
is inappropriate for use with most contemporary GGA correlation functionals, so
the latter limit is expected to perform quite poorly. Values of $\omega>1.0$ bohr${}^{-1}$ are likely not worth considering, according to benchmark
tests.[[757]](../bib_references/bib.md#bib784)

Evaluation of the short- and long-range HF exchange energies is
straightforward,[[24]](../bib_references/bib.md#bib10)
 so the crux of any RSH functional is the
form of the short-range GGA exchange functional, and several such functionals
are available in **Q-Chem**. These include short-range variants of the B88 and
PBE exchange described by Hirao and co-workers,[[609]](../bib_references/bib.md#bib632)

called $\mu$B88 and $\mu$PBE in **Q-Chem**,[[1168]](../bib_references/bib.md#bib1221)
 and an
alternative formulation of short-range PBE exchange proposed by Scuseria and
co-workers,[[554]](../bib_references/bib.md#bib569)
 which is known as $\omega$PBE. These
functionals are available in **Q-Chem** thanks to the efforts of the Herbert
group.[[1177]](../bib_references/bib.md#bib1230)
 By way of notation, the terms
“$\mu$PBE”, “$\omega$PBE”, *etc.*, refer only to the short-range exchange
functional, $E_{x,\rm SR}^{\rm DFT}$ in Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)). These
functionals could be used in “screened exchange” mode, as described in
Section [5.3](sect_XCfuncs.md), as for example in the HSE03
functional,[[576]](../bib_references/bib.md#bib595)
 therefore the designation “LRC-$\omega$PBE”, for
example, should only be used when the short-range exchange functional
$\omega$PBE is combined with 100% Hartree-Fock exchange in the long range.

In general, LRC-DFT functionals have been shown to remove the near-continuum of
spurious charge-transfer excited states that appear in large-scale TDDFT
calculations.[[757]](../bib_references/bib.md#bib784)
 However, certain results depend sensitively upon
the value of the range-separation parameter
$\omega$,[[757]](../bib_references/bib.md#bib784)

especially in TDDFT calculations (Section [7.3](../ch07_excited/sect_tddft.md)) and therefore the
results of LRC-DFT calculations must therefore be interpreted with caution, and
probably for a range of $\omega$ values. This can be accomplished by
requesting a functional that contains some short-range GGA exchange functional
($\omega$PBE or $\mu$PBE, in the examples mentioned above), in combination with
setting the *$rem* variable LRC_DFT = TRUE, which requests
the addition of 100% Hartree-Fock exchange in the long-range. Basic
job-control variables and an example can be found below. The value of the
range-separation parameter is then controlled by the variable OMEGA,
as shown in the examples below.

LRC_DFT

### `LRC_DFT`

> **Controls the application of long-range-corrected DFT**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE (or 0)
>     * Do not apply long-range correction.
>     * TRUE (or 1)
>     * Add 100% long-range Hartree-Fock exchange to the requested functional.
> * **Recommendation**: The $rem variable OMEGA must also be specified, in order to set the range-separation parameter.

OMEGA

### `OMEGA`

> **Sets the range-separation parameter, $\omega$ , also known as $\mu$ , in functionals based on Hirao’s RSH scheme.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\omega=n/1000$
>     * , in units of bohr
>     * ${}^{-1}$
> * **Recommendation**: None

COMBINE_K

### `COMBINE_K`

> **Controls separate or combined builds for short-range and long-range K**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE (or 0)
>     * Build short-range and long-range K separately (twice as expensive as a global hybrid)
>     * TRUE (or 1)
>     * Build short-range and long-range K together (
>     * $\approx$
>     * as expensive as a global hybrid)
> * **Recommendation**: Most pre-defined range-separated hybrid functionals in Q-Chem use this feature by default. However, if a user-specified RSH is desired, it is necessary to manually turn this feature on.

HFK_SR_COEF

### `HFK_SR_COEF`

> **Sets the coefficient for short-range HF exchange**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n/100000000$
> * **Recommendation**: None

HFK_LR_COEF

### `HFK_LR_COEF`

> **Sets the coefficient for long-range HF exchange**
>
> * **Type**: `INTEGER`
> * **Default**: `100000000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n/100000000$
> * **Recommendation**: None

???+ example "Example 5.6: Application of LRC- $\mu$ BOP to $\rm(H_{2}O)_{2}^{-}$ ."
    ```qchem
    $comment
       The value of omega is 0.47 by default but can
       be overwritten by specifying OMEGA.
    $end
    
    $molecule
       -1 2
       O           1.347338    -0.017773    -0.071860
       H           1.824285     0.813088     0.117645
       H           1.805176    -0.695567     0.461913
       O          -1.523051    -0.002159    -0.090765
       H          -0.544777    -0.024370    -0.165445
       H          -1.682218     0.174228     0.849364
    $end
    
    $rem
       EXCHANGE      LRC-BOP
       BASIS         6-311(1+,2+)G*
       XC_GRID       2
       LRC_DFT       TRUE
       OMEGA         300      ! = 0.300 bohr**(-1)
    $end
    ```

Rohrdanz *et al.*[[1178]](../bib_references/bib.md#bib1231)
 published a thorough benchmark study of
both ground- and excited-state properties using the LRC-$\omega$PBEh
functional, in which the “h” indicates a short-range hybrid (*i.e.*, the
presence of some short-range HF exchange). Empirically-optimized parameters of
$c_{x,\rm SR}=0.2$ (see Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA))) and $\omega=0.2$ bohr${}^{-1}$ were obtained,[[1178]](../bib_references/bib.md#bib1231)
 and these parameters are
taken as the defaults for LRC-$\omega$PBEh. Caution is warranted, however,
especially in TDDFT calculations for large systems, as excitation energies for
states that exhibit charge-transfer character can be rather sensitive to the
precise value of $\omega$.[[752]](../bib_references/bib.md#bib785)
 In such cases (and
maybe in general), the “tuning” procedure described in
Section [5.6.4](subsubsec_w-tuning.md) is recommended.

???+ example "Example 5.7: Application of LRC- $\omega$ PBEh to the $\rm C_{2}H_{4}$ – $\rm C_{2}F_{4}$ dimer at
5 Å separation."
    ```qchem
    $comment
        This example uses the "optimal" parameter set discussed above.
        It can also be run by setting METHOD = LRC-wPBEh.
    $end
    
    $molecule
       0 1
       C           0.670604    0.000000    0.000000
       C          -0.670604    0.000000    0.000000
       H           1.249222    0.929447    0.000000
       H           1.249222   -0.929447    0.000000
       H          -1.249222    0.929447    0.000000
       H          -1.249222   -0.929447    0.000000
       C           0.669726    0.000000    5.000000
       C          -0.669726    0.000000    5.000000
       F           1.401152    1.122634    5.000000
       F           1.401152   -1.122634    5.000000
       F          -1.401152   -1.122634    5.000000
       F          -1.401152    1.122634    5.000000
    $end
    
    $rem
       EXCHANGE      GEN
       BASIS         6-31+G*
       LRC_DFT       TRUE
       OMEGA         200      ! = 0.2 a.u.
       CIS_N_ROOTS   4
       CIS_TRIPLETS  FALSE
    $end
    
    $xc_functional
       C  PBE   1.00
       X  wPBE  0.80
       X  HF    0.20
    $end
    ```

Recently, Li and Chai re-optimized the B97-type range-separated functional with the latest version of the semi-empirical dispersion
correction D4.[[815]](../bib_references/bib.md#bib858)
 The resulting functional is denoted as KS-$\omega$B97X-D4, which performs comparably
to $\omega$B97M-V and consistently outperforms $\omega$B97X-D3  and $\omega$B97X-V
for the entire GMTKN55 database.[[815]](../bib_references/bib.md#bib858)

???+ example "Example 5.8: KS- $\omega$ B97X-D4 calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    SCF_GUESS            = SAD
    GEN_SCFMAN           = FALSE
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 0
    TAO_DFT_THETA_NDP    = 0
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    SYMMETRY             = false
    SYM_IGNORE           = true
    DFT_D                = D4
    DFT_D4_A1            = 35000000
    DFT_D4_A2            = 500000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 139483100
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X HF                  0.186861
    X KS_wB97X            1.000000
    C KS_wB97X            1.000000
    $end
    ```

By adding 100% Hartree-Fock exchange to the asymptotic Coulomb operator, LRC functionals
guarantee that an electron and hole experience an asymptotic interaction potential $1/r$.
This is correct for a molecule in the gas phase, but to simulate a material one might desire an asymptotic
behavior of $1/(\varepsilon r)$, where $\varepsilon$ is the (static) dielectric constant of the material.
In conjunction with “optimal tuning” of the range-separation parameter, as described in Section [5.6.4](subsubsec_w-tuning.md),
such functionals have been shown to afford accurate fundamental gaps for organic photovoltaic
materials,[[719]](../bib_references/bib.md#bib752)
 and are naturally combined with polarizable continuum models
(Section [11.2.3](../ch11_env/topic_pcm-em.md))
that employ the same dielectric constant.[[128]](../bib_references/bib.md#bib117)

These have come to be called *screened* RSH (sRSH) functionals.[[719]](../bib_references/bib.md#bib752)

An XC function of this type can be expressed generically as[[33]](../bib_references/bib.md#bib16)

<a id="eq:sRSH"></a>
$$
E_{xc}^{\textrm{sRSH}}=c_{x,{\rm SR}}E_{x,{\rm SR}}^{\textrm{HF}}+\varepsilon^{-1}E_{x,\rm LR}^{\textrm{HF}}+(\varepsilon^{-1}-c_{x,\rm SR})E_{x,\rm SR}^{\textrm{DFT}}+(1-\varepsilon^{-1})E_{x,\rm LR}^{\textrm{DFT}}+E_{c}^{\textrm{DFT}}\;, \tag{5.17}
$$

which should be compared to Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)) that provides the generic form for an RSH functional.
Although the RSH formalism allows for an arbitrary coefficient $c_{x,\rm LR}$ for the long-range Hartree-Fock
exchange term, as in Eq. ([5.13](Ch5.S3.SS1.md#eq:RSHGGA)),
this implies that the asymptotic electron–hole interaction has the form $c_{x,\rm LR}/r$ rather than $1/r$.[[352]](../bib_references/bib.md#bib356)

As such, LRC functionals are a particular class of RSH functionals where $c_{x,\rm LR}=1$, ensuring proper
asymptotic behavior in vacuum. Along the same lines, sRSH functionals set $c_{x,\rm LR}=\varepsilon^{-1}$
to ensure proper asymptotic behavior in a dielectric material. Using Eq. ([5.17](#eq:sRSH)), users may construct
sRSH functionals by means of a *$xc_functional* input section.
