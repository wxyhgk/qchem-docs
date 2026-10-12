---
title: "10.13.3 Romberg Finite-Field Procedure"
---

## 10.13.3 Romberg Finite-Field Procedure

(July 4, 2026)

Whereas the FF procedure described in Section [10.13.2](sec_finite-field.md) is a
straightforward, finite-difference implementation of the derivatives suggested
in Eq. ([10.152](Ch10.S13.SS1.md#eqn:E_F)), in the Romberg procedure[[311]](../bib_references/bib.md#bib328)
 one
combines energy values obtained for a succession of $k$ external electric
fields with amplitudes that form a geometric progression:

<a id="Ch10.E153"></a>

$$
F(k)=a^{k}F_{0}\;. \tag{10.153}
$$

The FF expressions are obtained by combining truncated Taylor expansions of the
energy with different amplitudes and/or external field directions. For
example, in the case of the diagonal $\bm{\beta}$-tensor components the Romberg
FF expression is

<a id="Ch10.E154"></a>

$$
\beta_{iii}(k,0)=3\left(\frac{\bigl{[}E(F_{-i}(k+1)-E(F_{i}(k+1))\bigr{]}-a\bigl{[}E(F_{-i}(k)-E(F_{i}(k))\bigr{]}}{a(a^{2}-1)(a^{k}F_{0})^{3}}\right)\;. \tag{10.154}
$$

The field index $\pm i$ refers to the possible field directions, *i.e.*, $\pm x$, $\pm y$ or $\pm z$. Truncation of the Taylor expansions means that the
results are contaminated by higher-order hyperpolarizabilities, and to remove
this contamination, successive “Romberg iterations” are performed using a
recursive expression. For a component of a (hyper)polarizability tensor
$\bm{\zeta}$, the recursive expression is

<a id="Ch10.E155"></a>

$$
\zeta(k,n)=\frac{a^{2n}\zeta(k,n-1)-\zeta(k+1,n-1)}{a^{2n}-1}\;. \tag{10.155}
$$

This expression leads to a triangular Romberg table enabling monitoring of the
convergence of the numerical derivative.[[311]](../bib_references/bib.md#bib328)

As with any finite-difference procedure, the FF method for computing
(hyper)polarizabilities is sensitive to the details of numerical
differentiation. The Romberg procedure allows one to find a field window,
defined by its upper and lower bounds, where the finite-difference procedure is
stable. Energy values for field amplitudes below that window suffer from
too-large round-off errors, which are proportional to the energy convergence
threshold. The upper bound is imposed by the critical field amplitude
corresponding to the intersection between the ground and excited-state
energies. In the Romberg procedure, this stability window defines a
sub-triangle, determination of which is the primary goal in analyzing Romberg
tables.

The automatic procedure based on the analysis of field amplitude errors is
implemented in scripts provided with **Q-Chem**’s distribution. The field
amplitude error is defined as the difference between $\zeta$-values obtained
for consecutive field amplitudes at the same Romberg iteration:

<a id="Ch10.E156"></a>

$$
\epsilon_{k}(n)=\zeta(k+1,n)-\zeta(k,n)\;. \tag{10.156}
$$

By virtue of Romberg’s recursive expression, the field error is expected to
decrease with each iteration. Convergence of the Romberg procedure can be
probed using the iteration (order) error, defined as

<a id="Ch10.E157"></a>

$$
\epsilon_{n}(k)=\zeta(k,n+1)-\zeta(k,n)\;. \tag{10.157}
$$

Automatic analysis of these quantities is described in detail in
Ref. [[311]](../bib_references/bib.md#bib328)
.

!!! note "Note"
    - The automatic procedure can fail if the field window is not chosen wisely.

    - The Romberg procedure can be performed either for one specific diagonal
    direction or for all Cartesian components. In the case of the second
    hyperpolarizability, only the $iiii$, $iijj$ components are available.


## 10.13.3.1 How to execute Romberg’s differentiation procedure

To perform Romberg calculations of (hyper)polarizabilities, the following
utilities are in the `$QC/bin/tools/Romberg` directory:

> `input-Q-Chem-t-rex.sh`
> 
> 
> `parse-t-rex.sh`
> 
> 
> `input-Q-Chem-t-rex-3.0`
> 
> 
> `romberg_tddft_read`
> 
> 
> `romberg_eom_read`
> 
> 
> `T-REX-3.0.3`

and this directory must be manually added to the `$PATH` environment
variable depending on the shell being used:

> ```qchem
> # bash syntax for ~/.bashrc:
> export PATH="$QC/bin/tools/Romberg:$PATH"
> # csh/tcsh syntax for ~/.cshrc:
> set path=($QC/bin/tools/Romberg $path)
> ```

To run the calculation, create an input called `input` that specifies
your molecule, an electronic structure method, and several additional *$rem*
variables that

- turn off symmetry (INTEGRAL_SYMMETRY and CC_SYMMETRY for
CC/EOM calculations),
- request higher-precision printing (CC_PRINT_PREC), and
- set up very tight convergence (SCF_CONVERGENCE,
CC_CONVERGENCE, EOM_DAVIDSON_CONVERGENCE, *etc.*).

An example of an input file is given below.

???+ example "Example 10.66: Input for Romberg calculations of the ethylene molecule using B3LYP."
    ```qchem
    $molecule
    0 1
     C        0.00000000   0.00000000 -0.66880000
     H        0.94859916   0.00000000 -1.19917145
     H       -0.94859916   0.00000000 -1.19917145
     C       -0.00000000   0.00000000  0.66880000
     H       -0.54409413   0.77704694  1.19917145
     H        0.54409413  -0.77704694  1.19917145
    $end
    
    $rem
       BASIS            =  sto-3g
       EXCHANGE         =  B3lyp
       SCF_CONVERGENCE  =  13  ! tight convergence for finite field calculations
       SCF_MAX_CYCLES   =  200
       CC_PRINT_PREC    =  16  ! decimal points of total energies
       INTEGRAL_SYMMETRY = false ! all symmetries need to be turned off
    $end
    ```

Run the script `input-Q-Chem-t-rex.sh` and answer the questions
regarding the parameters of the geometrical progression of field amplitudes
(see example below). The script will create multiple input files for the FF
calculations based on the input file template that you provided. The file
name that is requested serves as a prefix to each automatically-generated FF
input file. For example, if you specify the filename as `water`, input
files named `water001.inp`, `water002.inp`, … will be
generated. These must be run independently of the Romberg procedure, such as
on a computing cluster, or locally with GNU parallel or xargs. For example,
with GNU parallel, to run 6 **Q-Chem** jobs at a time, each with 4 threads,

> ```qchem
> ls hello*.inp | parallel -j6 ’qchem -nt 4 {.}.inp {.}.out’
> ```

After running the calculations, parse the output files using the script
`parse-t-rex.sh`. Then run the `T-REX` program. Answer the the
questions to compute the dipole moment and (hyper)polarizabilities (see
example below).

Romberg differentiation is only available for methods where printing the total
energy to high precision has been enabled. In the current version of **Q-Chem**,
CC_PRINT_PREC is implemented for the following methods: HF, DFT,
MP2, RI-MP2, MP3, CCD, CCSD, CCSD(T), QCISD, QCISD(T), TDDFT, and EOM-CCSD.

!!! note "Note"
    When using excited-state methods such as TDDFT, CIS, and EOM-CC, state
    ordering may switch when the external field is large.


With the T-REX program, you can compute the static dipole moment,
polarizability, and first and second hyperpolarizabilities for one specific
diagonal direction or for all Cartesian components, except that second
hyperpolarizabilities are limited to $iiii$ and $iijj$ components. When
computing all the components, you can obtain the norm of the dipole moment and
polarizability, the Hyper-Rayleigh scattering first hyperpolarizability, the
mean of the second hyperpolarizability, and other information

## 10.13.3.2 Step-by-step Example of a Finite-Field Calculation

Put the sample `input` file (given above) for a DFT calculation in the
new directory; the name of the input file should be `input`. Run the
`input-Q-Chem-t-rex.sh` script. The following questions are asked:

> ```qchem
> Components: x=1 y=2 z=3 all_beta=4 all_alpha=5
> 4
> File name
> eth-
> Number of field amplitudes
> 5
> Smallest field amplitude F_0
> 0.0004
> a   (F_k=a^k F_0)
> 2.0
> Number of files created         101
> ```

In this example, the answers correspond to FF calculations for
$F(k)=2.0^{k}\times 0.0004$ and for a geometric progression ($k=0,1,2,3,4,5$)
of external field amplitudes. The calculation is set up for all the
components, with the input files `eth-001.inp`, `eth-002.inp`,
`eth-003.inp`, …, generated, where the exact number of inputs
generated depends on the chosen geometric progression.

After the individual FF calculations (*i.e.*, after executing **Q-Chem** jobs for all
generated inputs), parse the outputs using the `parse-t-rex.sh` script.
The energies are written in a file called `prelogfile`.

Run the `T-REX` program and answer the questions:

> ```qchem
> Components: x=1 y=2 z=3 all_beta=4
> 4
> Number of methods
> 1
> Number of field amplitudes k_max+1
> 5
> Smallest field amplitude   F_0
> 0.0004
> Step-size a
> 2.0
> ```

The energies are ordered in a file called `logfile` and the results are
printed in the `results` file.
