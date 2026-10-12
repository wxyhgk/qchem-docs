---
title: "6.12.1 Introduction"
---

## 6.12.1 Introduction

(July 4, 2026)

The following sections give short summaries of the various coupled-cluster
based methods available in **Q-Chem**, most of which are variants of
coupled-cluster theory. The basic object-oriented tools necessary to permit the
implementation of these methods in **Q-Chem** was accomplished by Anna
Krylov and David Sherrill, working at Berkeley with Martin Head-Gordon, and
then continuing independently at the University of Southern California and
Georgia Tech, respectively. While at Berkeley, Krylov and Sherrill also
developed the optimized orbital coupled-cluster method, with additional
assistance from Ed Byrd. The extension of this code to MP3, MP4, CCSD and QCISD
is the work of Steve Gwaltney at Berkeley, while the extensions to QCCD
were implemented by Ed Byrd at Berkeley. The original tensor library and
CC/EOM suite of methods are handled by the CCMAN module of **Q-Chem**.
Later, a new code (termed CCMAN2) was developed in Krylov group by
Evgeny Epifanovsky and others, and a gradual transition from CCMAN to CCMAN2
has begun. During the transition time, both codes will be available for users
via the CCMAN2 keyword. Finally, there is a new module called **libgmbpt** developed to facilitate correlated calculations of very large systems. This module
now includes efficient implementations of RI-CC2 and stochastic RI-CC2 methods.

### `CORRELATION`

> **Specifies the correlation level of theory handled by CCMAN/CCMAN2.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `CCMP2`: Regular MP2 handled by CCMAN/CCMAN2
>     * `MP3`: CCMAN and CCMAN2
>     * `MP4SDQ`: CCMAN
>     * `MP4`: CCMAN
>     * `CCD`: CCMAN and CCMAN2
>     * `CCD(2)`: CCMAN
>     * `CCSD`: CCMAN and CCMAN2
>     * `CCSDT`: CCMAN2
>     * `CC2`: CCMAN2 and LIBGMBPT
>     * `CCSD(T)`: CCMAN and CCMAN2
>     * `CCSD(2)`: CCMAN
>     * `CCSD(fT)`: CCMAN and CCMAN2
>     * `CCSD(dT)`: CCMAN
>     * `CCSDT`: CCMAN2
>     * `CCVB-SD`: CCMAN2
>     * `QCISD`: CCMAN and CCMAN2
>     * `QCISD(T)`: CCMAN and CCMAN2
>     * `OD`: CCMAN
>     * `OD(T)`: CCMAN
>     * `OD(2)`: CCMAN
>     * `VOD`: CCMAN
>     * `VOD(2)`: CCMAN
>     * `QCCD`: CCMAN
>     * `QCCD(T)`: CCMAN
>     * `QCCD(2)`: CCMAN
>     * `VQCCD`: CCMAN
>     * `VQCCD(T)`: CCMAN
>     * `VQCCD(2)`: CCMAN
> * **Recommendation**: Consult the literature for guidance.

!!! note "Note"
    All methods implemented in CCMAN2 can be executed in combination
    with PCM implicit solvation models (at a “zeroth-order” level, as described in
    Section [11.2.1](../ch11_env/topic_solvation_Intro.md)) and with the EFP method (Section [11.5](../ch11_env/sect_efp.md)).
    Only energies and unrelaxed properties are available, not gradients.

