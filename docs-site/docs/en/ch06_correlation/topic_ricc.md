---
title: "6.12.10 Resolution-of-the-Identity with CC (RI-CC)"
---

## 6.12.10 Resolution-of-the-Identity with CC (RI-CC)

(July 4, 2026)

The RI approximation (see Section [6.6](topic_rimp2.md)) can be used in
coupled-cluster calculations, which substantially reduces the cost of integral
transformation and disk storage requirements. The RI approximation may be
used for integrals only such that integrals are generated in conventional MO
form and canonical CC/EOM calculations are performed, or in a more complete
version when modified CC/EOM equations are used such that the integrals are
used in their RI representation. The latter version allows for more substantial
savings in storage and in computational speed-up.

The RI for integrals is invoked when AUX_BASIS is specified. All
two-electron integrals are used in RI decomposed form in CC when
AUX_BASIS is specified.

By default, the integrals will be stored in the RI form and special CC/EOM code
will be invoked. Keyword CC_DIRECT_RI allows one to use RI generated
integrals in conventional form (by transforming RI integrals back to the
standard format) invoking conventional CC procedures. This option is mostly used for
debugging and benchmarking purposes.

!!! note "Note"
    RI for integrals is available for all CCMAN/CCMAN2 methods. CCMAN
    requires that the unrestricted reference be used, CCMAN2 does not have this
    limitation. The RI is also available for jobs that need analytic
    gradients.
    Full RI implementation (with integrals used in decomposed form) is
    only available for CCMAN2. For maximum computational efficiency, combine with
    FNO (see Sections [6.15.1](sec_FNOCC.md) and [7.9.14](../ch07_excited/sec_FNO.md)) when appropriate.


!!! note "Note"
    Efficient implementation[[532]](../bib_references/bib.md#bib546)
     of RI-CC2 that does not store double amplitudes
    is available in **libgmbpt**; it is invoked by setting CCMAN2=-1. See Section [6.12.4](topic_cc2.md).

