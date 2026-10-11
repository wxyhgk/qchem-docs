---
title: "7.9.30 Interpretation of EOM/CI Wave Functions and Orbital Numbering"
---

## 7.9.30 Interpretation of EOM/CI Wave Functions and Orbital Numbering

(July 4, 2026)

Analysis of the leading wave function amplitudes is always necessary for
determining the character of the state (*e.g.*, $\rm HOMO\rightarrow LUMO$
excitation, open-shell diradical, *etc.*). The CCMAN module print out leading
EOM/CI amplitudes using its internal orbital numbering scheme, which is
printed in the beginning. The typical CCMAN EOM-CCSD output looks like:

> ```qchem
> Root 1 Conv-d yes Tot Ene= -113.722767530 Hartree (Ex Ene 7.9548 eV),
> U1^2=0.858795, U2^2=0.141205 ||Res||=4.4E-07
> Right U1:
>        Value                   i            ->    a
>        0.5358                  7( B2  ) B   ->   17( B2  ) B
>        0.5358                  7( B2  ) A   ->   17( B2  ) A
>       -0.2278                  7( B2  ) B   ->   18( B2  ) B
>       -0.2278                  7( B2  ) A   ->   18( B2  ) A
> ```

This means that this state is derived by excitation from occupied orbital #7
(which has $b_{2}$ symmetry) to virtual orbital #17 (which is also of $b_{2}$
symmetry). The two leading amplitudes correspond to $\beta\rightarrow\beta$
and $\alpha\rightarrow\alpha$ excitation (the spin part is denoted by $A$ or
$B$). The orbital numbering for this job is defined by the following map:

> ```qchem
> The orbitals are ordered and numbered as follows:
> Alpha orbitals:
> Number  Energy    Type    Symmetry  ANLMAN number  Total number:
>   0    -20.613     AOCC      A1      1A1     1
>   1    -11.367     AOCC      A1      2A1     2
>   2     -1.324     AOCC      A1      3A1     3
>   3     -0.944     AOCC      A1      4A1     4
>   4     -0.600     AOCC      A1      5A1     5
>   5     -0.720     AOCC      B1      1B1     6
>   6     -0.473     AOCC      B1      2B1     7
>   7     -0.473     AOCC      B2      1B2     8
> 
>   0      0.071     AVIRT     A1      6A1     9
>   1      0.100     AVIRT     A1      7A1     10
>   2      0.290     AVIRT     A1      8A1     11
>   3      0.327     AVIRT     A1      9A1     12
>   4      0.367     AVIRT     A1     10A1     13
>   5      0.454     AVIRT     A1     11A1     14
>   6      0.808     AVIRT     A1     12A1     15
>   7      1.196     AVIRT     A1     13A1     16
>   8      1.295     AVIRT     A1     14A1     17
>   9      1.562     AVIRT     A1     15A1     18
>  10      2.003     AVIRT     A1     16A1     19
>  11      0.100     AVIRT     B1      3B1     20
>  12      0.319     AVIRT     B1      4B1     21
>  13      0.395     AVIRT     B1      5B1     22
>  14      0.881     AVIRT     B1      6B1     23
>  15      1.291     AVIRT     B1      7B1     24
>  16      1.550     AVIRT     B1      8B1     25
>  17      0.040     AVIRT     B2      2B2     26
>  18      0.137     AVIRT     B2      3B2     27
>  19      0.330     AVIRT     B2      4B2     28
>  20      0.853     AVIRT     B2      5B2     29
>  21      1.491     AVIRT     B2      6B2     30
> ```

The first column is CCMAN’s internal numbering (*e.g.*, 7 and 17 from the
example above). This is followed by the orbital energy, orbital type (frozen,
restricted, active, occupied, virtual), and orbital symmetry. Note that the
orbitals are blocked by symmetries and then ordered by energy within each
symmetry block, (*i.e.*, first all occupied $a_{1}$, then all $a_{2}$, *etc.*), and
numbered starting from 0. The occupied and virtual orbitals are numbered
separately, and frozen orbitals are excluded from CCMAN numbering. The two
last columns give numbering in terms of the final ANLMAN printout (starting
from 1), *e.g.*, our occupied orbital #7 will be numbered as 1$B_{2}$ in the
final printout. The last column gives the absolute orbital number (all
occupied and all virtuals together, starting from 1), which is often used by
external visualization routines.

CCMAN2 numbers orbitals by their energy within each irrep keeping the same
numbering for occupied and virtual orbitals. This numbering is exactly the same
as in the final printout of the SCF wave function analysis. Orbital energies
are printed next to the respective amplitudes. For example, a typical CCMAN2
EOM-CCSD output will look like that:

> ```qchem
> EOMEE-CCSD transition 2/A1
>  Total energy = -75.87450159 a.u.  Excitation energy = 11.2971 eV.
>  R1^2 = 0.9396  R2^2 = 0.0604  Res^2 = 9.51e-08
> 
>  Amplitude    Orbitals with energies
>   0.6486       1 (B2) A                  ->    2 (B2) A
>               -0.5101                          0.1729
>   0.6486       1 (B2) B                  ->    2 (B2) B
>               -0.5101                          0.1729
>  -0.1268       3 (A1) A                  ->    4 (A1) A
>               -0.5863                          0.0404
>  -0.1268       3 (A1) B                  ->    4 (A1) B
>               -0.5863                          0.0404
> ```

which means that for this state, the leading EOM amplitude corresponds to the
transition from the first b${}_{2}$ orbital (orbital energy $-0.5101$) to the
second b${}_{2}$ orbital (orbital energy 0.1729).

The most complete analysis of EOM-CC calculations is afforded by deploying a
general wave-function analysis tool contained in the **libwfa** module and
described in Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md). The EOM-CC state analysis is
activated by setting STATE_ANALYSIS = TRUE. In addition,
keywords controlling calculations of state and interstate properties should be
set up accordingly.

**Note: 

Wave function analysis is only available for CCMAN2.
**

???+ example "Example 7.179: Wave function analysis of the EOM-IP states (He ${}_{3}^{+}$ )."
    ```qchem
    $molecule
       0 1
       He
       He   1       R1
       He   2       R1      1       A
    
       R1 = 1.236447
       A  = 180.00
    $end
    
    $rem
       METHOD            = EOM-CCSD
       BASIS             = 6-31G
       IP_STATES         = [1,0,0,0,0,1,0,0]
       CC_EOM_PROP       = true   Analyze state properties (state OPDM)
       CC_REF_PROP       = true   Analyze reference state and difference OPDM
       CC_STATE_TO_OPT   = [1,1]  Compute transition properties wrt 1st EOM state of 1st irrep
       CC_TRANS_PROP     = true   Analyze transitions (transition OPDM)
       STATE_ANALYSIS    = true
       MOLDEN_FORMAT     = true
       NTO_PAIRS         = 2
    $end
    ```
