---
title: "7.9.27 Non-Iterative Triples Corrections to EOM-CCSD and CCSD"
---

## 7.9.27 Non-Iterative Triples Corrections to EOM-CCSD and CCSD

(July 4, 2026)

The effect of triple excitations to EOM-CCSD energies can be included via
perturbation theory in an economical ${\cal{O}}({N^{7}})$ computational scheme. Using
EOM-CCSD wave functions as zero-order wave functions, the second order triples
correction to the $\mu$th EOM-EE or SF state is:

<a id="Ch7.E123"></a>

$$
\Delta E^{(2)}_{\mu}=-\frac{1}{36}\sum_{i,j,k}\sum_{a,b,c}\frac{{\tilde{\sigma}_{ijk}^{abc}}(\mu){\sigma_{ijk}^{abc}}(\mu)}{D_{ijk}^{abc}-\omega_{\mu}} \tag{7.123}
$$

where $i,j$ and $k$ denote occupied orbitals, and
$a,b$ and $c$ are virtual orbital indices. $\omega_{\mu}$ is the
EOM-CCSD excitation energy of the $\mu$th state.
The quantities $\tilde{\sigma}$ and $\sigma$ are:

<a id="A3.S8.EGx59"></a>

$$
\displaystyle\tilde{\sigma}_{ijk}^{abc}(\mu) \tag{7.124}
$$

where, the $L$ and $R$ are left and right eigen-vectors for $\mu$th state.
Two different choices of the denominator,
$D_{ijk}^{abc}$, define the (dT) and (fT) variants of the correction.
In (fT), $D_{ijk}^{abc}$ is just Hartree–Fock orbital energy differences.
A more accurate (but not fully orbital invariant) (dT) correction employs
the complete three body diagonal of $\bar{H}$,
$\langle\Phi_{ijk}^{abc}|(He^{(T_{1}+T_{2})})_{C}|\Phi_{ijk}^{abc}\rangle$,
$D_{ijk}^{abc}$as a denominator.
For the reference (*e.g.*, a ground-state CCSD wave function),
the (fT) and (dT) corrections are identical to the
CCSD(2)${}_{T}$ and CR-CCSD(T)${}_{L}$ corrections of Piecuch and coworkers.[[1091]](../bib_references/bib.md#bib1136)

The EOM-SF-CCSD(dT) and EOM-SF-CCSD(fT) methods
yield a systematic improvement over EOM-SF-CCSD bringing the errors
below 1 kcal/mol. For theoretical background and detailed benchmarks,
see Ref. [[887]](../bib_references/bib.md#bib921)
.

Similar corrections are available for EOM-IP-CCSD,[[888]](../bib_references/bib.md#bib922)
 where
triples correspond to $3h2p$ excitations and EOM-EA-CCSD, where triples
correspond to $2h3p$ excitations.

**Note: 

Due to the orbital non-invariance problem, using (dT) correction is discouraged.
**

**Note: 

EOM-IP-CCSD(fT) correction is now available both in CCMAN and CCMAN2.
**.

**Note: 

In CCMAN2, triples corrections can be computed using two different backends,
**libtensor** and **libpt**. The former is more effective and recommended for larger jobs (see Section [6.13.3](../ch06_correlation/sec_dT.md)).
**

## 7.9.27.1 Job Control for Non-Iterative Triples Corrections

Triples corrections are requested by using METHOD or
EOM_CORR:

### `METHOD`

> **Specifies the calculation method.**
>
> * **Type**: `STRING`
> * **Default**: `No default value`
> * **Options**:
>     * `EOM-CCSD(DT)`: EOM-CCSD(dT), available for EE, SF, and IP
>     * `EOM-CCSD(FT)`: EOM-CCSD(fT), available for EE, SF, IP, and EA
>     * `EOM-CCSD(ST)`: EOM-CCSD(sT), available for IP
> * **Recommendation**: None

### `EOM_CORR`

> **Specifies the correlation level.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `SD(DT)`: EOM-CCSD(dT), available for EE, SF, and IP
>     * `SD(FT)`: EOM-CCSD(fT), available for EE, SF, IP, and EA
>     * `SD(ST)`: EOM-CCSD(sT), available for IP
> * **Recommendation**: None

**Note: 

In CCMAN2, EOM-IP-CCSD(fT) can be computed with or without
USE_LIBPT = TRUE.
**

## 7.9.27.2 Examples

???+ example "Example 7.161: EOM-EE-CCSD(fT) calculation of CH ${}^{+}$ ."
    ```qchem
    $molecule
       1 1
       C
       H  C  1.13092
    $end
    
    $rem
       METHOD                 eom-ccsd(ft)
       BASIS                  general
       EE_STATES              [1,0,1,1]
       EOM_DAVIDSON_MAX_ITER  60  increase number of Davidson iterations
    $end
    
    $basis
     H   0
     S   3  1.00
           19.24060000         0.3282800000E-01
           2.899200000         0.2312080000
          0.6534000000         0.8172380000
     S   1  1.00
          0.1776000000          1.000000000
     S   1  1.00
          0.0250000000          1.000000000
     P   1  1.00
           1.00000000          1.00000000
     ****
     C   0
     S   6  1.00
           4232.610000         0.2029000000E-02
           634.8820000         0.1553500000E-01
           146.0970000         0.7541100000E-01
           42.49740000         0.2571210000
           14.18920000         0.5965550000
           1.966600000         0.2425170000
     S   1  1.00
           5.147700000          1.000000000
     S   1  1.00
          0.4962000000          1.000000000
     S   1  1.00
          0.1533000000          1.000000000
     S   1  1.00
          0.0150000000          1.000000000
     P   4  1.00
           18.15570000         0.1853400000E-01
           3.986400000         0.1154420000
           1.142900000         0.3862060000
          0.3594000000         0.6400890000
     P   1  1.00
          0.1146000000          1.000000000
     P   1  1.00
          0.0110000000          1.000000000
     D   1  1.00
          0.750000000          1.00000000
     ****
    $end
    ```

???+ example "Example 7.162: EOM-SF-CCSD(dT) calculations of methylene."
    ```qchem
    $molecule
       0 3
       C
       H 1 CH
       H 1 CH 2 HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       METHOD            eom-ccsd(dt)
       BASIS             6-31G
       SF_STATES         [2,0,0,2]
       N_FROZEN_CORE     1
       N_FROZEN_VIRTUAL  1
       CCMAN2            false   !only works in ccman1
    $end
    ```

???+ example "Example 7.163: EOM-IP-CCSD(dT) calculations of Mg."
    ```qchem
    $molecule
       0 1
       Mg    0.000000     0.000000    0.000000
    $end
    
    $rem
       N_FROZEN_CORE  1
       CORRELATION    ccsd
       EOM_CORR       sd(dt)
       BASIS          6-31g
       IP_STATES      [1,0,0,0,0,1,1,1]
       CCMAN2         false               NYI in ccman2
    $end
    ```
