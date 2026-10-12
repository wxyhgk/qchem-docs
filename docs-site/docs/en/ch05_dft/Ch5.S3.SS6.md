---
title: "5.3.6 Specialized Functionals"
---

## 5.3.6 Specialized Functionals

(July 4, 2026)

- SRC1-R1: TDDFT short-range corrected functional
[Eq. (1) in Ref. [[123]](../bib_references/bib.md#bib112)
, 1st row atoms]
- SRC1-R2: TDDFT short-range corrected functional
[Eq. (1) in Ref. [[123]](../bib_references/bib.md#bib112)
, 2nd row atoms]
- SRC2-R1: TDDFT short-range corrected functional
[Eq. (2) in Ref. [[123]](../bib_references/bib.md#bib112)
, 1st row atoms]
- SRC2-R2: TDDFT short-range corrected functional
[Eq. (2) in Ref. [[123]](../bib_references/bib.md#bib112)
, 2nd row atoms]
- BR89: Becke-Roussel meta-GGA exchange functional modeled after the hydrogen atom[[91]](../bib_references/bib.md#bib75)
- B94: meta-GGA correlation functional by Becke that uses the BR89
exchange functional to compute the Coulomb potential[[97]](../bib_references/bib.md#bib79)
- B94hyb: modified version of the B94 correlation functional for use with
the BR89B94hyb exchange-correlation functional[[97]](../bib_references/bib.md#bib79)
- BR89B94h: 15.4% HF exchange + 84.6% BR89 meta-GGA exchange + BR89hyb
meta-GGA correlation[[97]](../bib_references/bib.md#bib79)
- BRSC: Exchange component of the original B05 exchange-correlation functional[[101]](../bib_references/bib.md#bib85)
- MB05: Exchange component of the modified B05 (BM05) exchange-correlation functional[[1128]](../bib_references/bib.md#bib1179)
- B05: A full exact-exchange Kohn-Sham scheme of Becke that uses the exact-exchange energy density (RI) and accounts for static correlation[[101]](../bib_references/bib.md#bib85)
- BM05 (XC): Modified B05 hyper-GGA scheme that uses MB05 instead of BRSC as the exchange functional[[1128]](../bib_references/bib.md#bib1179)
- PSTS: Hyper-GGA (100% HF exchange) exchange-correlation functional of Perdew, Staroverov, Tao, and Scuseria[[1072]](../bib_references/bib.md#bib1119)
- MCY2: Mori-Sánchez-Cohen-Yang adiabatic connection-based hyper-GGA exchange-correlation functional[[960]](../bib_references/bib.md#bib1001)

This example illustrate the use of the RI-B05 and RI-PSTS functionals.
These are presently available only for single-point calculations, and
convergence is greatly facilitated by obtaining converged SCF orbitals from,
*e.g.*, an LDA or HF calculation first. (LDA is used in the example below but
HF can be substituted.) Use of the RI approximation (Section [6.6](../ch06_correlation/topic_rimp2.md))
requires specification of an auxiliary basis set.

???+ example "Example 5.1: Q-Chem input of H ${}_{2}$ using RI-B05."
    ```qchem
    $comment
       H2, example of SP RI-B05.  First do a well-converged LSD, G3LARGE is the
       basis of choice for good accuracy.
    $end
    
    $molecule
       0 1
       H   0.  0.   0.0
       H   0.  0.   0.7414
    $end
    
    $rem
       METHOD           lda
       BASIS            g3large
       SCF_GUESS        core     ! required
       PURECART         2222     ! required
       THRESH           14
       INCDFT           false
       SCF_CONVERGENCE  9
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE        b05            ! or set to psts for ri-psts
       BASIS           g3large
       AUX_BASIS       rib05-cc-pvtz  ! the aux basis for both RI-B05 and RI-PSTS
       SCF_GUESS       read
       PURECART        2222           ! required
       THRESH          4
       PRINT_INPUT     true
       INCDFT          false
       MAX_SCF_CYCLES  0              ! required
       DFT_CUTOFFS     0              ! required
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    ```
