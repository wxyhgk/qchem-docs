---
title: "4.5.7 Geometric Direct Minimization (GDM)"
---

## 4.5.7 Geometric Direct Minimization (GDM)

(July 4, 2026)

gdm

Geometric Direct Minimization (GDM) is an extremely robust SCF convergence
algorithm that is only slightly less efficient than DIIS. The GDM algorithm
takes steps in an orbital rotation space that properly respects the
hyperspherical geometry of the manifold of allowed SCF solutions. In other
words, orbital rotations are variables that describe a space that is curved
like a many-dimensional sphere. Just like the optimum flight paths for
airplanes are not straight lines but great circles, so too are the optimum
steps in orbital rotation space. GDM takes this correctly into account, which
is the origin of its efficiency and its robustness. For full details see
Ref. [[1391]](../bib_references/bib.md#bib1453)
. GDM is a good alternative to DIIS for SCF jobs
that exhibit convergence difficulties with DIIS. The GDM algorithm has been
extended to restricted open-shell SCF calculations, and results indicate that
it is much more efficient as compared to older direct-minimization methods.

Section [4.5.3](sect_diis.md) discussed the fact that DIIS can efficiently head
towards the global SCF minimum in the early iterations. This can be true even
if DIIS fails to converge in later iterations. For this reason, a hybrid scheme
has been implemented which uses the DIIS minimization procedure to achieve
convergence to an intermediate cutoff threshold. Thereafter, the geometric
direct minimization algorithm is used. This scheme combines the strengths of
the two methods quite nicely: the ability of DIIS to recover from initial
guesses that may not be close to the global minimum, and the ability of GDM to
robustly converge to a local minimum, even when the local surface topology is
challenging for DIIS. This is the recommended procedure with which to invoke
GDM (*i.e.*, setting SCF_ALGORITHM = DIIS_GDM). This hybrid
procedure is also compatible with the SAD guess, while GDM itself is not,
because it requires an initial guess set of orbitals. If one wishes to disturb
the initial guess as little as possible before switching on GDM, one should
additionally specify MAX_DIIS_CYCLES = 1 to obtain only a single
Roothaan step (which also serves up a properly orthogonalized set of orbitals).

*$rem* options relevant to GDM are SCF_ALGORITHM which should be set
to either GDM or DIIS_GDM and the following:

### `MAX_DIIS_CYCLES`

> **The maximum number of DIIS iterations before switching to (geometric) direct minimization when SCF_ALGORITHM is DIIS_GDM or DIIS_DM . See also THRESH_DIIS_SWITCH .**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * `1`: Only a single Roothaan step before switching to (G)DM
>     * $n$
>     * $n$: DIIS iterations before switching to (G)DM.
> * **Recommendation**: None

### `THRESH_DIIS_SWITCH`

> **The threshold for switching between DIIS extrapolation and direct minimization of the SCF energy is $10^{-\mbox{{\small THRESH\_DIIS\_SWITCH}}}$ when SCF_ALGORITHM is DIIS_GDM or DIIS_DM . See also MAX_DIIS_CYCLES .**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `User-defined.`
> * **Recommendation**: None

???+ example "Example 4.12: Input for a UHF calculation using geometric direct minimization (GDM) on the
phenyl radical, after initial iterations with DIIS."
    ```qchem
    $molecule
       0   2
       c1
       x1  c1  1.0
       c2  c1  rc2  x1  90.0
       x2  c2  1.0  c1  90.0  x1    0.0
       c3  c1  rc3  x1  90.0  c2    tc3
       c4  c1  rc3  x1  90.0  c2   -tc3
       c5  c3  rc5  c1   ac5  x1  -90.0
       c6  c4  rc5  c1   ac5  x1   90.0
       h1  c2  rh1  x2  90.0  c1  180.0
       h2  c3  rh2  c1   ah2  x1   90.0
       h3  c4  rh2  c1   ah2  x1  -90.0
       h4  c5  rh4  c3   ah4  c1  180.0
       h5  c6  rh4  c4   ah4  c1  180.0
    
       rc2 =   2.672986
       rc3 =   1.354498
       tc3 =  62.851505
       rc5 =   1.372904
       ac5 = 116.454370
       rh1 =   1.085735
       rh2 =   1.085342
       ah2 = 122.157328
       rh4 =   1.087216
       ah4 = 119.523496
    $end
    
    $rem
       BASIS           = 6-31G*
       METHOD          = hf
       SCF_ALGORITHM   = diis_gdm
       SCF_CONVERGENCE = 7
       THRESH          = 10
    $end
    ```
