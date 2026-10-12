---
title: "8.3.1 Symbolic Representation Overview"
---

## 8.3.1 Symbolic Representation Overview

(July 4, 2026)

Examples are given in the tables below and follow the standard format generally
adopted for specifying basis sets. The single exception applies to additional
diffuse functions. These are best inserted in a similar manner to the
polarization functions; in parentheses with the light atom designation
following heavy atom designation: (*heavy*, *light*), using a period as
a placeholder in the unusual case that diffuse functions are to be added to hydrogen
atoms but not to heavy atoms. See Table [8.1](#table:BS:Pople) for the general form.
This convention can be applied, for example, to the named Pople-style basis sets
listed in Table [8.2](#table:Atoms:Pople), resulting in specific examples given in
Table [8.3](#table:BS:Pople-ext).

| Basis Name ${}^{a}$ | $j$ | $m$ ${}^{b}$ | $n$ ${}^{c}$ |
| --- | --- | --- | --- |
| STO- $j$ ( $k$ +, $l$ +)G( $m$ , $n$ ) | 2,3,6 | d | p |
| $j$ -21( $k$ +, $l$ +)G( $m$ , $n$ ) | 3 | 2d | 2p |
| $j$ -31( $k$ +, $l$ +)G( $m$ , $n$ ) | 4,6 | 3d | 3p |
| $j$ -311( $k$ +, $l$ +)G( $m$ , $n$ ) | 6 | df, 2df, 3df | pd, 2pd, 3pd |

- ${}^{a}$$k$ and $l$ denote the number of sets of diffuse functions on heavy atoms and on hydrogen atoms, respectively.
- ${}^{b}$$m$ denotes the number of sets of polarization functions on the heavy atoms.
- ${}^{c}$$n$ denotes the number of sets of polarization functions on the hydrogen atoms.

Table 8.1: 
Summary of Pople-type basis sets available in **Q-Chem**.

| Symbolic Name | Atoms Supported |
| --- | --- |
| STO-2G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K, Ca, Sr |
| STO-3G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ I |
| STO-6G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| 3-21G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ Xe, Cs |
| 4-31G | H, He, Li $\rightarrow$ Ne, P $\rightarrow$ Cl |
| 6-31G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| 6-311G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| G3LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| G3MP2LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

Table 8.2: 
Atoms supported for Pople basis sets available in **Q-Chem**.

| Symbolic Name | Atoms Supported |
| --- | --- |
| 3-21G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ Xe, Cs |
| 3-21+G | H, He, Na $\rightarrow$ Cl, Na $\rightarrow$ Ar, K, Ca, Ga $\rightarrow$ Kr |
| 3-21G* | Na $\rightarrow$ Ar |
| 6-31G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31+G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-31G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31G(d,p) | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31G(.,+)G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-31+G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-311G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| 6-311+G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar |
| 6-311G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| 6-311G(d,p) | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| G3LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| G3MP2LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

Table 8.3: 
Examples of extended Pople basis sets.

Although not widely used in modern quantum chemistry, Dunning[[354]](../bib_references/bib.md#bib359)
 introduced an early set of basis
sets denoted SV, DZ, and TZ; see Table [8.4](#table:BS:Dunning-orig-ext). (These are not to be confused with the widely-used
“correlation-consistent” basis sets, which are also associated with Dunning’s name.) The original Dunning basis sets
can be extended with diffuse and polarization functions using a nomenclature similar
to that used for Pople basis sets: *name*($k$+,$l$+)($m$d,$n$p),
where $k$ is the number of additional heavy atom diffuse
functions, $l$ is the number of additional light atom diffuse functions,
$m$ is the number of additional $d$ polarization functions on heavy atoms,
and $n$ is the number of additional $p$ polarization functions on light atoms.

| Symbolic Name | Atoms Supported |
| --- | --- |
| SV | H, Li $\rightarrow$ Ne |
| SV* | H, B $\rightarrow$ Ne |
| SV(d,p) | H, B $\rightarrow$ Ne |
| SV(2+,+)(2d,p) | H, B $\rightarrow$ Ne |
| DZ | H, Li $\rightarrow$ Ne, Al $\rightarrow$ Cl |
| DZ+ | H, B $\rightarrow$ Ne |
| DZ++ | H, B $\rightarrow$ Ne |
| DZ* | H, Li $\rightarrow$ Ne |
| DZ** | H, Li $\rightarrow$ Ne |
| DZ(d,p) | H, Li $\rightarrow$ Ne |
| DZ(2+,+)(2d,p) | H, B $\rightarrow$ Ne |
| TZ | H, Li $\rightarrow$ Ne |
| TZ+ | H, Li $\rightarrow$ Ne |
| TZ++ | H, Li $\rightarrow$ Ne |
| TZ* | H, Li $\rightarrow$ Ne |
| TZ** | H, Li $\rightarrow$ Ne |
| TZ(d,p) | H, Li $\rightarrow$ Ne |

Table 8.4: 
Examples of extended Dunning basis sets.

The much more widely-used basis sets that are associated with Dunning are the correlation-consistent (“cc”) ones.[[355]](../bib_references/bib.md#bib360)

The basic ones and their augmented counterparts are listed in Table [8.5](#table:Atoms:Dunning-cc). Those appended with “-PP”
are pseudopotential basis sets, defined for heavy elements only and intended to be used in conjunction with effective core potentials (ECPs),
which are discussed in Section [8.10](sec_ECPs.md). Each correlation-consistent basis set (cc-*name*
has an “augmented” counterpart (aug-cc-*name*) that includes diffuse functions.

| Symbolic Name | Atoms Supported |
| --- | --- |
| cc-pVDZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVDZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVDZ-PP | Cu $\rightarrow$ Rn |
| cc-pVTZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVTZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVTZ-PP | Cu $\rightarrow$ Rn |
| cc-pVQZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVQZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVQZ-PP | Cu $\rightarrow$ Rn |
| cc-pV5Z | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pV6Z | H $\rightarrow$ Ar except Li, Na, Mg |
| cc-pCVDZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVDZ) |
| cc-pCVTZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVTZ) |
| cc-pCVQZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVQZ) |
| cc-pCV5Z | H, He, B $\rightarrow$ Ar, Ca (H and He use cc-pV5Z) |
| cc-pwCVDZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar |
| cc-pwCVTZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn |
| cc-pwCVQZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn, Br |
| cc-pwCVDZ-PP | Cu $\rightarrow$ Rn |
| cc-pwCVTZ-PP | Cu $\rightarrow$ Rn |
| cc-pwCVQZ-PP | Cu $\rightarrow$ Rn |
| aug-cc-pVDZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVDZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pVTZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVTZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pVQZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVQZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pV5Z | H $\rightarrow$ Ar, Sc $\rightarrow$ Kr |
| aug-cc-pV6Z | H $\rightarrow$ Ar except Li, Be, Na, Mg |
| aug-cc-pCVDZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVDZ) |
| aug-cc-pCVTZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVTZ) |
| aug-cc-pCVQZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVQZ) |
| aug-cc-pCV5Z | H, He, B $\rightarrow$ Ar (H and He use aug-cc-pV5Z) |
| aug-cc-pwCVDZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar |
| aug-cc-pwCVTZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn |
| aug-cc-pwCVQZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn, Br |
| aug-cc-pwCVDZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |
| aug-cc-pwCVTZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |
| aug-cc-pwCVQZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |

- ${}^{a}$may-, jun-, and jul-cc-p(C)VXZ variants are also available
- ${}^{b}$jun-cc-pVXZ-PP variant is also available
- ${}^{c}$jun-cc-p(w)VXZ(-PP) variant is also available

Table 8.5: 
Atoms supported in **Q-Chem** for correlation-consistent basis sets.
For cc-pVXZ (X = D, T, Q), those names which
do not end in “-full” correspond to the definitions with a segmented
contraction scheme,[[308]](../bib_references/bib.md#bib313)
 and those that do end in “-full”
correspond to the original optimized generally-contracted definitions.
For all other basis sets, where there is no distinction, the only definition is from optimized general contraction.
For the augmented basis sets, footnotes indicate the availability of “calendar” variants.[[1039]](../bib_references/bib.md#bib1083)

The correlation-consistent paradigm adds additional diffuse functions for each angular momentum class, meaning that for a
second-row atom such as carbon, the aug-cc-pVDZ basis set contains diffuse $s$, $p$, and $d$ functions (10 diffuse functions per atom),
while hydrogen contains diffuse $s$ and $p$ functions. The aug-cc-pVTZ basis set also includes diffuse $f$ functions for carbon
(for a total of 20 diffuse functions per atom) and diffuse $d$ functions for hydrogen. As compared to functions with tighter exponents,
inclusion of diffuse functions is relatively expensive and prone to incur linear dependencies that hamper SCF convergence,
as discussed in Section [8.3.2](sec_Basis_Customization.md). At the same time, diffuse functions are often crucial to the description of anions,
excited states, and noncovalent interactions but the high angular momentum diffuse functions included in aug-cc-pVXZ are not always
necessary. In recognition of this fact. “calendar” versions of the correlation-consistent basis sets have been introduced
(jul-, jun-, and may-*name*),[[1039]](../bib_references/bib.md#bib1083)

which systemically remove diffuse basis functions starting from aug-cc-*name*. The jul-cc-pVXZ basis set removes all diffuse
functions from hydrogen, and is equivalent to using cc-pVXZ for hydrogen and aug-cc-pVXZ for heavy atoms. The jun-cc-pVXZ basis
set additionally removes the highest angular momentum diffuse functions from each heavy atom, *e.g.*, for a carbon atom
the diffuse $d$ functions are removed to make jun-cc-pVDZ and the diffuse $f$ functions are removed to make jun-cc-pVTZ.
The may-cc-pVXZ basis sets then remove the highest angular momentum diffuse functions that remain in jun-cc-pVXZ, so that for a
carbon atom, may-cc-pVDZ is minimally augmented with only a single diffuse $s$ function. **Q-Chem** includes may-, jun-,
and jul-cc-pVXZ and similarly may-, jun-, and jul-cc-pCVXZ (for X = D, T, and Q in both cases). Also available are the
jun-cc-pVXZ-PP parings of aug-cc-pVXZ-PP and the jun-cc-pwCVXZ(-PP) parings of aug-cc-pwCVXZ(-PP), again for X = D, T, or Q.
If the user has questions as to what functions are included in any of these basis sets, simply set PRINT_GENERAL_BASIS =
TRUE in the *$rem* section (as described in Section [8.3.2](sec_Basis_Customization.md)) to get a printout of the basis function information.

| Symbolic Name | Atoms Supported |
| --- | --- |
| TZV | H $\rightarrow$ Kr |
| VDZ | H $\rightarrow$ Kr |
| VTZ | H $\rightarrow$ Kr |

Table 8.6: 
Atoms supported in **Q-Chem** for the original Ahlrichs basis sets.[[1202]](../bib_references/bib.md#bib1256)

(Note that these are different from the more modern Karlsruhe “def2” basis sets, which are described in
Table [8.7](#table:Atoms:Karlsruhe-def2).)

The name Ahlrichs is also associated with two different collections of basis sets.
The older set (TZV, VDZ, and VTZ) is listed in Table [8.6](#table:Atoms:Ahlrichs-orig);[[1202]](../bib_references/bib.md#bib1256)

these basis sets are available but are no longer in common use. Much more widely used are the second-generation “def2”
basis sets that are listed in Table [8.7](#table:Atoms:Karlsruhe-def2),[[1438]](../bib_references/bib.md#bib1504)

which are sometimes called “Karlsruhe” basis sets to distinguish them from the older basis sets developed by Ahlrichs
and co-workers at the University of Karlsruhe. These basis sets were originally designed for SCF calculations although
more recently they have seen some use in correlated wave function calculations. Diffuse functions were added later,[[1147]](../bib_references/bib.md#bib1199)

and are stipulated with a name ending in “D”, *e.g.*, def2-SVP does not contain diffuse functions but def2-SVPD does.
The def2-ha and def2-ma variants (*e.g.*, def2-ha-SVP) include partial augmentation.[[481]](../bib_references/bib.md#bib492)

The def2-ha basis sets are “heavy-augmented”, eliminating all diffuse functions on the hydrogen atoms, so that
def2-ha-SVP consists of def2-SVP for hydrogen and def2-SVPD for other atoms. The def2-ma basis sets are “minimally-augmented”,
and are constructed from def2-ha-SVP by removing the highest angular moment diffuse function on each heavy atom, similar
to the jun-cc-pVXZ prescription.

| Symbolic Name | Atoms Supported |
| --- | --- |
| def2-mSVP | H–Kr, ${}^{a}$ Rb–Rn (with def2-ECP) |
| def2-SV(P), def2-SVP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-SVP, def2-ha-SVP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-SVPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-TZVP, def2-TZVPP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-TZVP, def2-ma-TZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-ha-TZVP, def2-ha-TZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-TZVPD, def2-TZVPPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-QZVP, def2-QZVPP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-QZVP, def2-ma-QZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-ha-QZVP, def2-ha-QZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-QZVPD, def2-QZVPPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |

- ${}^{a}$Na–Kr are identical to def2-SV(P)

Table 8.7: 
Atoms supported in **Q-Chem** for the Karlsruhe “def2” basis sets.[[1438]](../bib_references/bib.md#bib1504)

Finally, there is a set of basis sets associated with the name of Jensen[[635]](../bib_references/bib.md#bib661)

(see Table [8.8](#table:Atoms:Jensen-pc)), which were developed primarily for NMR calculations.
There is also a “universal” Gaussian basis set,[[310]](../bib_references/bib.md#bib315)
 which is supported for elements
H–Lr except for Pa–Np and Cm–Bk.

| Symbolic Name ${}^{a}$ | Atoms Supported |
| --- | --- |
| pcseg- $n$ | H $\rightarrow$ Kr |
| pc- $n$ | H $\rightarrow$ Kr |
| pcJ- $n$ | H $\rightarrow$ Ar |
| psS- $n$ | H $\rightarrow$ Ar |
| aug-pcseg- $n$ | H $\rightarrow$ Kr |
| aug-pc- $n$ | H $\rightarrow$ Kr |
| aug-pcJ- $n$ | H $\rightarrow$ Ar |
| aug-psS- $n$ | H $\rightarrow$ Ar |

- ${}^{a}$For $n=0,1,2,3,4$ in each case

Table 8.8: 
Atoms supported for Jensen polarization consistent basis sets
available in **Q-Chem**. The pcseg-$n$ sets should be preferred instead of
pc-$n$, as they are more efficient in **Q-Chem**. The pcJ-$n$[[636]](../bib_references/bib.md#bib662)
 and pcS-$n$[[635]](../bib_references/bib.md#bib661)

basis sets are optimized for NMR spin-spin couplings and chemical shieldings, respectively.
