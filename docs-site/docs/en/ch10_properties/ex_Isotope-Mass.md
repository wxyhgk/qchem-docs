---
title: "10.8.2 Isotopic Substitutions and Changes in T and P"
---

## 10.8.2 Isotopic Substitutions and Changes in $T$ and $P$

(July 4, 2026)

By default **Q-Chem** calculates vibrational frequencies using the atomic masses
of the most abundant isotopes.

Masses of other isotopes can be specified
using the *$isotopes* section and by setting the ISOTOPES *$rem*
variable to TRUE. The format of the *$isotopes* section is as follows:

> ```qchem
> $isotopes
>    number_of_isotope_loops  tp_flag
>    number_of_atoms  [temp pressure] (loop 1)
>    atom_number1   mass1
>    atom_number2   mass2
>    ...
>    number_of_atoms  [temp pressure] (loop 2)
>    atom_number1   mass1
>    atom_number2   mass2
>    ...
> $end
> ```

!!! note "Note"
    Only the atoms whose masses are to be changed from the default
    values need to be specified. After each loop all masses are reset to the
    default values. Atoms are numbered according to the order in the *$molecule* section.


An initial loop using the default masses is always performed first. Subsequent
loops use the user-specified atomic masses. Only those atoms whose masses are
to be changed need to be included in the list, all other atoms will adopt the
default masses. The output gives a full frequency analysis for each loop. Note
that the calculation of vibrational frequencies in the additional loops only
involves a rescaling of the computed Hessian, and therefore takes little
additional computational time.

The first line of the *$isotopes* section specifies the number of substitution loops
and also whether the temperature and pressure should be modified. The *tp_flag*
setting should be set to 0 if the default temperature and pressure are to be used (298.15 K
and 1 atm respectively), or else to 1 if they are to be altered. Note that the
temperatures should be specified in Kelvin and pressures in atmospheres.
See Example 10.8.2.

### `ISOTOPES`

> **Specifies if non-default masses are to be used in the frequency calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Use default masses only.
>     * `TRUE`: Read isotope masses from $isotopes section.
> * **Recommendation**: None

???+ example "Example 10.39: An EDF1/6-31G* optimization, followed by a vibrational analysis including isotopic substitution. Doing the
vibrational analysis at a stationary point is necessary for the results to be valid."
    ```qchem
    $molecule
       0  1
       C   1.08900   0.00000   0.00000
       C  -1.08900   0.00000   0.00000
       H   2.08900   0.00000   0.00000
       H  -2.08900   0.00000   0.00000
    $end
    
    $rem
       BASIS    6-31G*
       JOBTYPE  opt
       METHOD   edf1
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       BASIS       6-31G*
       JOBTYPE     freq
       METHOD      edf1
       SCF_GUESS   read
       ISOTOPES    1
    $end
    
    $isotopes
       2   0           ! two loops, both at std temp and pressure
       4
         1   13.00336  ! All atoms are given non-default masses
         2   13.00336
         3   2.01410
         4   2.01410
       2
         3   2.01410   ! Hs replaced with Ds
         4   2.01410
    $end
    ```

???+ example "Example 10.40: EDF1/6-31G* optimization followed by vibrational analysis in which the vibrational enthalpy and entropy
and computed at different temperatures and pressures."
    ```qchem
    $molecule
       0 1
       O   0.000000   0.000000   0.106731
       H  -0.758095   0.000000  -0.528927
       H   0.758095   0.000000  -0.528927
    $end
    
    $rem
       JOBTYPE   opt
       METHOD    edf1
       BASIS     6-31G*
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE   freq
       METHOD    edf1
       BASIS     6-31G*
       ISOTOPES  true
    $end
    
    $isotopes
       3   1             ! "1" here means we will set T & P
       0   500.0   1.0   ! 500 K, 1 atm, standard masses
       0   298.0   10.0  ! 298 K, 10 atm, standard masses
       2   500.0   1.0   ! 500 K, 1 atm, subst. D for H
         2   2.0141018
         3   2.0141018
    $end
    ```
