---
title: "3.5.1 Overview"
---

## 3.5.1 Overview

(July 4, 2026)

It is sometimes useful to place a sequence of jobs into a single **Q-Chem** input
file, where the individual inputs should be separated from one another by a
line consisting of the string `@@@`. The output from these jobs is
then appended sequentially to a single output file. This is useful to (a) use
information obtained in a prior job (*i.e.*, an optimized geometry) in a
subsequent job; or (b) keep related calculations together in a single output
file.

Some limitations should be kept in mind:

- •

The first job will overwrite any existing output file of the same name in
the working directory. Restarting the job will also overwrite any
existing file.
- •

**Q-Chem** reads all the jobs from the input file immediately and stores
them. Therefore no changes can be made to the details of subsequent jobs
following command-line initiation of **Q-Chem**, even if these subsequent jobs have not yet run.
- •

If any single job fails, **Q-Chem** proceeds to the next job in the batch
file, for good or ill.
- •

No check is made to ensure that dependencies are satisfied, or that
information is consistent. For example, in a geometry optimization
followed by a frequency calculation, no attempt is made by the latter to
check that the optimization was successful. When reading MO coefficients
from a previous job, it is the user’s responsibility to ensure that the
basis set is the same in both calculations, as this is assumed by the
program.
- •

Scratch files are saved from one job to the next in a batch job, so that
information from previous jobs can be shared with subsequent ones, but
are deleted upon completion of the entire batch job unless the
*–save* command-line argument is supplied, as discussed in
Chapter [2](../ch02_install/chap_install.md).

The following example requests a batch job consisting of ($i$) a HF/6-31G*
geometry optimization; followed by ($ii$) a frequency calculation at the same
level of theory that uses the previously-optimized geometry (and also reads in
the final MOs from the optimization job); and finally ($iii$) a single-point
calculation at the same geometry but at a higher level of theory,
MP2/6-311G(d,p).

???+ example "Example 3.11: Example of using information from previous jobs in a single input file."
    ```qchem
    $comment
       Optimize H-H at HF/6-31G*
    $end
    
    $molecule
       0 1
       H
       H  1  r
    
       r = 1.1
    $end
    
    $rem
       JOBTYPE       opt    Optimize the bond length
       METHOD        hf
       BASIS         6-31G*
    $end
    
    @@@
    
    $comment
       Now calculate the frequency of H-H at the same level of theory.
    $end
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE       freq    Calculate vibrational frequency
       METHOD        hf
       BASIS         6-31G*
       SCF_GUESS     read    Read the MOs from disk
    $end
    
    @@@
    
    $comment
      Now a single point calculation at at MP2/6-311G(d,p)//HF/6-31G*
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD        mp2
       BASIS         6-311G(d,p)
    $end
    ```
