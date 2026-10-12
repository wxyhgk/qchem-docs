---
title: "4.4.3 Reading MOs from Disk"
---

## 4.4.3 Reading MOs from Disk

(July 4, 2026)

There are two methods by which MO coefficients can be used from a previous job by reading them from disk:

1. Running two independent jobs sequentially invoking **Q-Chem** with
three command line variables:.

> ```qchem
> localhost-1> qchem job1.in job1.out save
>    localhost-2> qchem job2.in job2.out save
> ```

!!! note "Note"
    (1) The *$rem* variable SCF_GUESS must be set to READ in `job2.in`.
    (2) Scratch files remain in `$QCSCRATCH/save` on exit.

2. Running a batch job where two jobs are placed into a single input file
separated by the string `@@@` on a single line.

!!! note "Note"
    (1) SCF_GUESS must be set to READ in the second job of the batch file.
    (2) A third **Q-Chem** command line variable is not necessary.
    (3) As for the SAD guess, **Q-Chem** requires at least two SCF cycles to
    ensure proper
    SCF convergence (idempotency of the density).


!!! note "Note"
    It is up to the user to make sure that the basis sets match between the
    two jobs. There is no internal checking for this, although the occupied
    orbitals are re-orthogonalized in the current basis after being read in. If you
    want to project from a smaller basis into a larger basis, consult
    Section [4.4.5](sect_projection.md).


???+ example "Example 4.5: Input for an ROHF calculation on the OH radical. One SCF cycle is initially
performed on the cation, to get reasonably good initial guess orbitals, which
are then read in as the guess for the radical. This avoids the use of Q-Chem ’s default GWH guess for ROHF, which is often poor."
    ```qchem
    $comment
       OH radical, part 1. Do initial iterations of cation orbitals.
    $end
    
    $molecule
       1  1
       O  0.000   0.000   0.000
       H  0.000   0.000   1.000
    $end
    
    $rem
       BASIS           =  6-311++G(2df)
       METHOD          =  hf
       THRESH          =  10
       MAX_SCF_CYCLES  =  2
       SCF_CONVERGENCE =  1
    $end
    
    @@@
    
    $comment
       OH radical, part 2. Read cation orbitals, do the radical
    $end
    
    $molecule
       0  2
       O  0.000   0.000   0.000
       H  0.000   0.000   1.000
    $end
    
    $rem
       BASIS            =  6-311++G(2df)
       METHOD           =  hf
       UNRESTRICTED     =  false
       SCF_ALGORITHM    =  dm
       SCF_CONVERGENCE  =  7
       SCF_GUESS        =  read
       THRESH           =  10
    $end
    ```
