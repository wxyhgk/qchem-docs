---
title: "9.6.1 Overview"
---

## 9.6.1 Overview

(July 4, 2026)

It is often useful to scan the potential energy surface (PES), optimizing all
other degrees of freedom for each particular value of the scanned variable(s).
Such a “relaxed” scan may provide a rough estimate of a pathway between
reactant and product—assuming the coordinate(s) for the scan has been chosen
wisely—and is often used in development of classical force fields to optimize
dihedral angle parameters. Ramachandran plots, for example, are key tools for
studying conformational changes of peptides and proteins, and are essentially
two-dimensional torsional scans.

In certain cases, relaxed scans might encounter some difficulties on
optimizations. A “frozen” scan can be easier to perform because of no
geometry optimizations although it provides less information of real dynamics.

**Q-Chem** supports one- and two-dimensional PES scans, by setting
JOBTYPE = PES_SCAN in the *$rem* section. In
addition, a *$scan* input section with the following format should be
specified, in the format below but with no more than two bond-length,
bond-angle, or torsional variables specified.

> ```qchem
> $scan
>    stre  atom1  atom2  value1 value2 incr
>    ...
>    bend  atom1  atom2  atom3  value1 value2 incr
>    ...
>    tors  atom1  atom2  atom3  atom4  value1 value2 incr
>    ...
> $end
> ```

!!! note "Note"
    Potential scans with JOBTYPE = PES_SCAN are available for ground-state potential
    energy surfaces only, although one may compute excitation energies along the scanned coordinate(s) by including
    appropriate keywords for vertical excitation in the *$rem* section, *e.g.*, CIS_N_ROOTS for CIS/TDDFT excited states.


The first example below demonstrates how to scan the torsional potential of butane,
which is a sequence of constrained optimizations with
the C1–C2–C3–C4 dihedral angle fixed at $-$180${}^{\circ}$, $-$165${}^{\circ}$, $-$150${}^{\circ}$,
$\ldots$, 165${}^{\circ}$, 180${}^{\circ}$.

???+ example "Example 9.19: One-dimensional torsional scan of butane"
    ```qchem
    $molecule
       0 1
       C       1.934574    -0.128781    -0.000151
       C       0.556601     0.526657     0.000200
       C      -0.556627    -0.526735     0.000173
       C      -1.934557     0.128837    -0.000138
       H       2.720125     0.655980    -0.000236
       H       2.061880    -0.759501    -0.905731
       H       2.062283    -0.759765     0.905211
       H       0.464285     1.168064    -0.903444
       H       0.464481     1.167909     0.903924
       H      -0.464539    -1.167976     0.903964
       H      -0.464346    -1.168166    -0.903402
       H      -2.062154     0.759848     0.905185
       H      -2.720189    -0.655832    -0.000229
       H      -2.061778     0.759577    -0.905748
    $end
    
    $rem
       JOBTYPE  pes_scan
       METHOD   hf
       BASIS    sto-3g
    $end
    
    $scan
       tors 1 2 3 4 -180 180 15
    $end
    ```

The next example is a two-dimension potential scan. The first dimension is a
scan of the C1–C2–C3–C4 dihedral angle from $-$180${}^{\circ}$ to 180${}^{\circ}$
degree in 30${}^{\circ}$ intervals; the second dimension is a scan of the
C2–C3 bond length from 1.5 Å to 1.6 Å in 0.05 Å increments.

???+ example "Example 9.20: Two-dimensional torsional scan of butane"
    ```qchem
    $molecule
       0 1
       C       1.934574    -0.128781    -0.000151
       C       0.556601     0.526657     0.000200
       C      -0.556627    -0.526735     0.000173
       C      -1.934557     0.128837    -0.000138
       H       2.720125     0.655980    -0.000236
       H       2.061880    -0.759501    -0.905731
       H       2.062283    -0.759765     0.905211
       H       0.464285     1.168064    -0.903444
       H       0.464481     1.167909     0.903924
       H      -0.464539    -1.167976     0.903964
       H      -0.464346    -1.168166    -0.903402
       H      -2.062154     0.759848     0.905185
       H      -2.720189    -0.655832    -0.000229
       H      -2.061778     0.759577    -0.905748
    $end
    
    $rem
       JOBTYPE  pes_scan
       METHOD   hf
       BASIS    sto-3g
    $end
    
    $scan
       tors 1 2 3 4 -180 180 30
       stre 2 3 1.5 1.6 0.05
    $end
    ```

To perform a frozen PES scan, set FROZEN_SCAN to be TRUE and
use input geometry in *Z*-matrix format. The example demonstrates a frozen PES
of the C1–C2 bond stretching from 1.0 Å to 2.0 Å for methanol.

???+ example "Example 9.21: One-dimensional frozen PES scan of methanol"
    ```qchem
    $molecule
      0 1
       C
       O   C  RCO
       H1  C  RCH1  O  H1CO
       X   C  1.00  O  XCO   H1  180.0
       H2  C  RCH2  X  H2CX  H1   90.0
       H3  C  RCH2  X  H2CX  H1  -90.0
       H4  O  ROH   C  HOC   H1  180.0
    
       RCO  = 1.421
       RCH1 = 1.094
       RCH2 = 1.094
       ROH  = 0.963
       H1CO = 107.2
       XCO  = 129.9
       H2CX = 54.25
       HOC  = 108.0
    $end
    
    $rem
       JOBTYPE        pes_scan
       EXCHANGE       s
       CORRELATION    vwn
       BASIS          3-21g
       FROZEN_SCAN    true
    $end
    
    $scan
       stre 1 2 1.0 2.0 0.5
    $end
    ```

**Q-Chem** supports one-dimensional restrained PES scans including bond-length,
bond-angle, torsional, atom to center of mass of two atoms, and atom to a set
of atoms. Note that the set of atoms is defined as the atoms with indices from
`atom2` to `atom3`, where the atoms indexed at `atom2` and
`atom3` are included in the set. These restrained scans apply a harmonic
potential to bias geometry optimization.
**Q-Chem** also supports restrained PES scans for transition state
search of typical S${}_{\rm N}$2 reactions where the geometry restraints have the form

<a id="Ch9.E47"></a>

$$
f(R)=k\left(R_{12}\pm R_{34}-R\right)^{2}\;. \tag{9.47}
$$

Here, $R_{12}$ and $R_{34}$ are two bond lengths in the reaction coordinate and
$k$ is a force constant for restraining $R$ in the range of $R_{12}\pm R_{34}$.
To perform a restrained PES scan, the following format should be specified.

> ```qchem
> $scan
>  r12      atom1  atom2  Rmax   Rmin   incr  force_constant
>  ...
>  rbend    atom1  atom2  atom3  Rmax   Rmin  incr  force_constant
>  ...
>  rtors    atom1  atom2  atom3  atom4  Rmax  Rmin  incr  force_constant
>  ...
>  r1to23   atom1  atom2  atom3  Rmax   Rmin  incr  force_constant
>  ...
>  r1toset  atom1  atom2  atom3  Rmax   Rmin  incr  force_constant
>  ...
>  r12mr34  atom1  atom2  atom3  atom4  Rmin  Rmax  incr  force_constant
>  ...
>  r12pr34  atom1  atom2  atom3  atom4  Rmin  Rmax  incr  force_constant
>  ...
> $end
> ```

???+ example "Example 9.22: One-dimensional restrained PES scan of chloromethane S ${}_{\text{N}}$ 2 reaction"
    ```qchem
    $molecule
      -1 1
       C     0.418808   -1.240869    0.249048
       Cl   -0.775224   -1.495584    1.586668
       H     1.408172   -1.490565    0.631227
       H     0.147593   -1.907736   -0.568952
       H     0.413296   -0.199000   -0.092071
       Cl    1.947359    1.619163   -1.747832
    $end
    
    $rem
       JOBTYPE   pes_scan
       METHOD    b3lyp
       BASIS     6-31G*
    $end
    
    $scan
       r12mr34 1 2 1 6 -2.0 2.0 0.2 1000.0
    $end
    ```

???+ example "Example 9.23: One-dimensional restrained torsional PES scan of butane"
    ```qchem
    $molecule
     0 1
      C       1.934574    -0.128781    -0.000151
      C       0.556601     0.526657     0.000200
      C      -0.556627    -0.526735     0.000173
      C      -1.934557     0.128837    -0.000138
      H       2.720125     0.655980    -0.000236
      H       2.061880    -0.759501    -0.905731
      H       2.062283    -0.759765     0.905211
      H       0.464285     1.168064    -0.903444
      H       0.464481     1.167909     0.903924
      H      -0.464539    -1.167976     0.903964
      H      -0.464346    -1.168166    -0.903402
      H      -2.062154     0.759848     0.905185
      H      -2.720189    -0.655832    -0.000229
      H      -2.061778     0.759577    -0.905748
    $end
    
    $rem
       JOBTYPE PES_SCAN
       METHOD HF
       BASIS STO-3G
    $end
    
    $scan
       rtors 1 2 3 4 -180 180 15 1000.0
    $end
    ```

???+ example "Example 9.24: One-dimensional restrained PES scan pulling Na+ to benzene"
    ```qchem
    $molecule
     1 1
      Na        0.0000000000    0.0000000000   -1.8358304117
      C         1.4040705495    0.0000000000    0.5608720717
      C         0.7020352748   -1.2159607646    0.5608720717
      C        -0.7020352748   -1.2159607646    0.5608720717
      C        -1.4040705495    0.0000000000    0.5608720717
      C        -0.7020352748    1.2159607646    0.5608720717
      C         0.7020352748    1.2159607646    0.5608720717
      H         2.4900504384    0.0000000000    0.5941562674
      H         1.2450252192   -2.1564469363    0.5941562674
      H        -1.2450252192   -2.1564469363    0.5941562674
      H        -2.4900504384    0.0000000000    0.5941562674
      H        -1.2450252192    2.1564469363    0.5941562674
      H         1.2450252192    2.1564469363    0.5941562674
    $end
    
    $rem
       JOBTYPE PES_SCAN
       BASIS STO-3G
       METHOD B3LYP
       DFT_D D3_BJ
    $end
    
    $scan
    R1toSet 1 2 13 2.3 1.8 -0.1 1000.0
    $end
    
    ```
