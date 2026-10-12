---
title: "3.3.3 Reading Molecular Coordinates from a Previous Job or File"
---

## 3.3.3 Reading Molecular Coordinates from a Previous Job or File

(July 4, 2026)

Often users wish to perform several calculations in sequence, where the later
calculations rely on results obtained from the previous ones. For example, a
geometry optimization at a low level of theory, followed by a vibrational
analysis and then, perhaps, single-point energy at a higher level. Rather than
having the user manually transfer the coordinates from the output of the
optimization to the input file of a vibrational analysis or single point energy
calculation, **Q-Chem** can transfer them directly from job to job.

To achieve this requires that:

- The READ variable is entered into the molecular coordinate input
- Scratch files from a previous calculation have been saved. These may be
obtained *explicitly* by using the save option across multiple job
runs as described below and in Chapter [2](../ch02_install/chap_install.md), or
*implicitly* when running multiple calculations in one input file,
as described in Section [3.5](sec_multiple_jobs.md).

```qchem
$molecule
   READ
$end
```

In this example, the *job1* scratch files are saved in a directory
*$QCSCRATCH/job1* and are then made available to the *job2*
calculation. This is achieved with the following commands:

> ```qchem
> localhost-1> qchem job1.in job1.out job1
> localhost-2> qchem job2.in job2.out job1
> ```

In this example, the `job1` scratch files are saved in a directory
`$QCSCRATCH/job1` and are then made available to the `job2`
calculation.

!!! note "Note"
    The program must be instructed to read specific scratch files by the
    input of `job2`.


The READ function can also be used to read molecular coordinates
from a second input file. The format for the coordinates in the second file
follows that for standard **Q-Chem** input, and must be delimited with the
*$molecule* and *$end* keywords.

```qchem
$molecule
   READ filename
$end
```
