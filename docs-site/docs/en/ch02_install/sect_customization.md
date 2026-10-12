---
title: "2.1.6 Further Customization"
---

## 2.1.6 Further Customization

(July 4, 2026)

**Q-Chem** has developed a simple mechanism for users to set user-defined
long-term defaults to override the built-in program defaults. Such defaults may
be most suited to machine specific features such as memory allocation, as the
total available memory will vary from machine to machine depending on specific
hardware and accounting configurations. However, users may identify other
important uses for this customization feature. **Q-Chem** obtains input
initialization variables from four sources:

1. User input file
2. `$HOME/.qchemrc` file
3. `$QC/config/preferences` file
4. “Factory installed” program defaults

Input mechanisms higher in this list override those that are lower. Mechanisms
#2 and #3 allow the user to specify alternative default settings for certain
variables that will override the **Q-Chem** “factory-installed” defaults.
This can be done by a system administrator via a `preferences` file added
to the `$QC/config` directory, or by an individual user by means of a
`.qchemrc` file in her home directory.

!!! note "Note"
    The `.qchemrc` and `preferences` files are not requisites for
    running **Q-Chem** and currently only support keywords in the *$rem* input
    section.


The format of the `.qchemrc` and `preferences` files consists of a
*$rem* keyword section, as in the **Q-Chem** input file, terminated with the
usual *$end* keyword. Any other `$whatever` section will be ignored.
To aid in reproducibility, a copy of the `.qchemrc` file (if present) is
included near the top of the job’s output file. (The `.qchemrc `and
`preferences` files must have file permissions such that they are readable
by the user invoking **Q-Chem**.) The format of both of these files is as
follows:

> ```qchem
> $rem
>    rem_variable   option   comment
>    rem_variable   option   comment
>    ...
> $end
> ```

```qchem
$rem
   DIIS_SUBSPACE_SIZE   5         Modify max DIIS subspace size
   THRESH               10        10**(-10) threshold
   MAX_SCF_CYCLES       100       More than the default of 50
$end
```

The following *$rem* variables are specifically recommended as those that a
user might want to customize:

- MEM_STATIC
- SCF_CONVERGENCE
- THRESH
- MAX_SCF_CYCLES
- GEOM_OPT_MAX_CYCLES
