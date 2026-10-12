---
title: "6.13.4 Job Control Options"
---

## 6.13.4 Job Control Options

(July 4, 2026)

The evaluation of a non-iterative (T) or (2) correction after a coupled-cluster
singles and doubles level calculation (either CCSD, QCISD or OD) is controlled
by the correlation keyword, and the specification of any frozen orbitals via
N_FROZEN_CORE (and possibly N_FROZEN_VIRTUAL).

For the (2) correction, it is possible to apply the frozen core approximation
in the reference coupled cluster calculation, and then correlate all orbitals
in the (2) correction. This is controlled by CC_INCL_CORE_CORR,
described below.

The default is to include core and core-valence correlation automatically in
the CCSD(2) or OD(2) correction, if the reference CCSD or OD calculation was
performed with frozen core orbitals. The reason for this choice is that core
correlation is economical to include via this method (the main cost increase is
only linear in the number of core orbitals), and such effects are important to
account for in accurate calculations. This option should be made false if a job
with explicitly frozen core orbitals is desired. One good reason for freezing
core orbitals in the correction is if the basis set is physically inappropriate
for describing core correlation (*e.g.*, standard Pople basis sets, and Dunning
cc-pV$x$Z basis sets are designed to describe valence-only correlation
effects). Another good reason is if a direct comparison is desired against
another method such as CCSD(T) which is always used in the same orbital window
as the CCSD reference.

There are several implementations of non-iterative triples available in
**Q-Chem**. In the original CCMAN suite, (T), (2), and (dT)/(fT) corrections can be computed.
The parallel scaling of this code is very modest (4 cores max).
CCMAN2 currently allows only the calculation of (T) and (fT) correction for CCSD wave
functions. By default, the CCMAN2 code is used for (T); to use the CCMAN code, set CCMAN2 to false.
There are two versions of (T) in CCMAN2: The default version (native CCMAN2)
and a new version using **libpt**.
The implementation based on **libpt** is in-core OpenMP parallel.
It is significantly faster in most realistic
calculations, but it does not use point group symmetry, so it might show slower performance for small jobs
with high symmetry. The **libpt** code is enabled by setting USE_LIBPT=TRUE.
The CCSD(T) calculation can be restarted using the *$ccsd_pt_restart* data
printed during the CCSD(T) calculation. To restart the job simply copy the last
printed *$ccsd_pt_restart* to your **Q-Chem** input file.

**Note: 

For the best performance of **libpt** (T) code, parallel execution should be requested,
see Section [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel).
**

### `USE_LIBPT`

> **Enable libpt for CCSD(T) calculations in CCMAN2.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`
>     * `FALSE`
> * **Recommendation**: libpt is now used by default in all real-valued CC/EOM-CC calculations

### `CC_INCL_CORE_CORR`

> **Whether to include the correlation contribution from frozen core orbitals in non iterative (2) corrections, such as OD(2) and CCSD(2).**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`
>     * `FALSE`
> * **Recommendation**: Use the default unless no core-valence or core correlation is desired ( e.g. , for comparison with other methods or because the basis used cannot describe core correlation).
