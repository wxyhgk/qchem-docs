---
title: "6.6.5 Spin-Biased MP2 Methods (SCS-MP2, SOS-MP2, and MOS-MP2)"
---

## 6.6.5 Spin-Biased MP2 Methods (SCS-MP2, SOS-MP2, and MOS-MP2)

(July 4, 2026)

The accuracy of MP2 calculations can be significantly improved by
semi-empirically scaling the opposite-spin (OS) and same-spin (SS) correlation
components with separate scaling factors, as shown by
Grimme.[[491]](../bib_references/bib.md#bib499)
 Scaling with 1.2 and 0.33 (or OS and SS components)
defines the SCS-MP2 method, but other parameterizations are desirable for
systems involving intermolecular interactions, as in the SCS-MI-MP2 method,
which uses 0.40 and 1.29 (for OS and SS components).[[330]](../bib_references/bib.md#bib337)

Results of similar quality for thermochemistry can be obtained by only
retaining and scaling the opposite spin correlation (by 1.3), as was recently
demonstrated.[[656]](../bib_references/bib.md#bib680)
 Furthermore, the SOS-MP2 energy can be
evaluated using the RI approximation together with a Laplace transform
technique, in effort that scales only with the 4th power of molecular size.
Efficient algorithms for the energy[[656]](../bib_references/bib.md#bib680)
 and the analytical
gradient[[855]](../bib_references/bib.md#bib887)
 of this method are available since **Q-Chem** v. 3.0, and
offer advantages in speed over MP2 for larger molecules, as well as
statistically significant improvements in accuracy.

However, we note that the SOS-MP2 method does systematically underestimate
long-range dispersion (for which the appropriate scaling factor is 2 rather
than 1.3) but this can be accounted for by making the scaling factor
distance-dependent, which is done in the modified opposite spin variant
(MOS-MP2) that has recently been proposed and tested.[[853]](../bib_references/bib.md#bib886)
 The
MOS-MP2 energy and analytical gradient are also available in **Q-Chem** 3.0 at a
cost that is essentially identical with SOS-MP2. Timings show that the
4th-order implementation of SOS-MP2 and MOS-MP2 yields substantial
speedups over RI-MP2 for molecules in the 40 heavy atom regime and larger. It is
also possible to customize the scale factors for particular applications, such
as weak interactions, if required.

A fourth order scaling SOS-MP2/MOS-MP2 energy calculation can be invoked
by setting the CORRELATION keyword to either SOSMP2 or
MOSMP2. MOS-MP2 further requires the specification of the *$rem*
variable OMEGA, which tunes the level of attenuation of the MOS
operator:[[853]](../bib_references/bib.md#bib886)

<a id="Ch6.E28"></a>
$$
g_{\omega}(r_{12})=\frac{1}{r_{12}}+c_{\mathrm{MOS}}\frac{\mathrm{erf}\left({\omega r_{12}}\right)}{r_{12}} \tag{6.28}
$$

The recommended OMEGA value is $\omega=0.6$ bohr${}^{-1}$.[[853]](../bib_references/bib.md#bib886)

The fast algorithm makes use of auxiliary basis expansions and therefore, the
keyword AUX_BASIS should be set consistently with the user’s choice
of BASIS. Fourth-order scaling analytical gradient for both SOS-MP2
and MOS-MP2 are also available and is automatically invoked when
JOBTYPE is set to OPT or FORCE. The minimum memory
requirement is 3$X^{2}$, where $X$ = the number of auxiliary basis functions,
for both energy and analytical gradient evaluations. Disk space requirement for
closed shell calculations is $\sim 2OVX$ for energy evaluation and $\sim 4OVX$
for analytical gradient evaluation.

Summary of key *$rem* variables to be specified:

| CORRELATION | RIMP2 |
| --- | --- |
|  | SOSMP2 |
|  | MOSMP2 |
| JOBTYPE | sp (default) single point energy evaluation |
|  | opt geometry optimization with analytical gradient |
|  | force evaluation with analytical gradient |
| BASIS | user’s choice (standard or user-defined: GENERAL or MIXED ) |
| AUX_BASIS | corresponding auxiliary basis (standard or user-defined: |
|  | AUX_GENERAL or AUX_MIXED |
| OMEGA | no default $n$ ; use $\omega=n/1000$ . The recommended value is |
|  | $n=600$ ( $\omega=0.6$ bohr ${}^{-1}$ ) |
| N_FROZEN_CORE | Optional |
| N_FROZEN_VIRTUAL | Optional |
| SCS | Turns on spin-component scaling with SCS-MP2(1), |
|  | SOS-MP2(2), and arbitrary SCS-MP2(3) |

???+ example "Example 6.8: Example of SCS-MP2 geometry optimization"
    ```qchem
    $molecule
       0 1
       C
       H  1  1.0986
       H  1  1.0986  2  109.5
       H  1  1.0986  2  109.5  3   120.0 0
       H  1  1.0986  2  109.5  3  -120.0 0
    $end
    
    $rem
       JOBTYPE             opt
       CORRELATION         rimp2
       BASIS               aug-cc-pvdz
       AUX_BASIS           rimp2-aug-cc-pvdz
       BASIS2              racc-pvdz   ! Optional Secondary basis
       SCS                 1           ! Turn on spin-component scaling
       DUAL_BASIS_ENERGY   true        ! Optional dual-basis approximation
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 6.9: Example of SCS-MI-MP2 energy calculation"
    ```qchem
    $molecule
       0 1
       C       0.000000     -0.000140      1.859161
       H      -0.888551      0.513060      1.494685
       H       0.888551      0.513060      1.494685
       H       0.000000     -1.026339      1.494868
       H       0.000000      0.000089      2.948284
       C       0.000000      0.000140     -1.859161
       H       0.000000     -0.000089     -2.948284
       H      -0.888551     -0.513060     -1.494685
       H       0.888551     -0.513060     -1.494685
       H       0.000000      1.026339     -1.494868
    $end
    
    $rem
       CORRELATION         rimp2
       BASIS               aug-cc-pvtz
       AUX_BASIS           rimp2-aug-cc-pvtz
       BASIS2              racc-pvtz    Optional Secondary basis
       THRESH              12
       SCF_CONVERGENCE     8
       SCS                 3            Spin-component scale arbitrarily
       SOS_FACTOR          0400000      Specify OS parameter
       SSS_FACTOR          1290000      Specify SS parameter
       DUAL_BASIS_ENERGY   true         Optional dual-basis approximation
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 6.10: Example of SOS-MP2 geometry optimization"
    ```qchem
    $molecule
       0 3
       C1
       H1   C1   1.07726
       H2   C1   1.07726   H1  131.60824
    $end
    
    $rem
       JOBTYPE        opt
       METHOD         sosmp2
       BASIS          cc-pvdz
       AUX_BASIS      rimp2-cc-pvdz
       UNRESTRICTED   true
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "Example 6.11: Example of MOS-MP2 energy evaluation with frozen core approximation"
    ```qchem
    $molecule
       0 1
       Cl
       Cl 1 2.05
    $end
    
    $rem
       METHOD            mosmp2
       BASIS             cc-pVTZ
       AUX_BASIS         rimp2-cc-pVTZ
       N_FROZEN_CORE     fc
       OMEGA             600
       THRESH            12
       SCF_CONVERGENCE   8
    $end
    ```
