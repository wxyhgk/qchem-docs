---
title: "9.2.1 Job Control Overview"
---

## 9.2.1 Job Control Overview

(July 4, 2026)

Obviously a level of theory, basis set, and starting molecular geometry must be
specified to begin a geometry optimization or transition-structure search.
These aspects are described elsewhere in this manual, and this section
describes job-control variables specific to optimizations.

The job controls for geometry optimization have the general rem variable
pattern, GEOM_OPT. These are the original rem variables used within
the **Optimize** driver, Section [9.2.2](topic_ts_Job-Control-Optimize.md). The job
controls for **Libopt3** are contained within *$geom_opt* section,
which provide even greater job control to the users than the original rem
variables, Section  [9.2.5](topic_ts_Job-Control-Libopt3.md).
To allow our users with existing workflows to not experience any disruptions,
the GEOM_OPT variables can be read within the **Libopt3** driver if
they have similar matching variables/controls. The decreasing order of
precedence for setting of rem variables are as follows:
1) *$geom_opt* variables, 2) GEOM_OPT variables, 3) Default.

### `JOBTYPE`

> **Specifies the calculation.**
>
> * **Type**: `STRING`
> * **Default**: `Default is single-point, which should be changed to one of the following options.`
> * **Options**:
>     * `OPT`: Equilibrium structure optimization.
>     * `TS`: Transition structure optimization.
>     * `RPATH`: Intrinsic reaction path following.
> * **Recommendation**: Application-dependent.

### `GEOM_OPT_DRIVER`

> **Controls the geometry optimization driver.**
>
> * **Type**: `STRING`
> * **Default**: `LIBOPT3`
> * **Options**:
>     * `OPTIMIZE`: Use the original optimization original driver.
>     * `LIBOPT3`: Use the new driver.
> * **Recommendation**: Note that the new driver is still under active development.
