---
title: "4.5.8 Direct Minimization (DM)"
---

## 4.5.8 Direct Minimization (DM)

(July 4, 2026)

Direct minimization (DM) is a less sophisticated forerunner of the
geometric direct minimization (GDM) method discussed in the previous
section. DM does not properly step along great circles in the
hyper-spherical space of orbital rotations, and therefore converges
less rapidly and less robustly than GDM, in general. DM is retained in
**Q-Chem** only for legacy purposes. In general, the input options are
the same as for GDM, with the exception of the specification of
SCF_ALGORITHM, which can be either DIIS_DM
(recommended) or DM.

### `PSEUDO_CANONICAL`

> **When SCF_ALGORITHM = DM , this controls the way the initial step, and steps after subspace resets are taken.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Use Roothaan steps when (re)initializing
>     * `TRUE`: Use a steepest descent step when (re)initializing
> * **Recommendation**: The default is usually more efficient, but choosing TRUE sometimes avoids problems with orbital reordering.
