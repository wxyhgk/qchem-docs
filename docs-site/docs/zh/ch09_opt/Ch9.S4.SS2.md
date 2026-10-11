---
title: "9.4.2 Geometry Optimization with General Constraints"
---

## 9.4.2 Geometry Optimization with General Constraints

(July 4, 2026)

CONSTRAINT and ENDCONSTRAINT define the beginning and end,
respectively, of the constraint section of *$opt* within which users may
specify up to six different types of constraints:

**interatomic distances**

Values in Ångstroms; *value* $>0$: 

`stre   atom1   atom2   value

`

**angles**

Values in degrees, $0\leq value\leq 180$; *atom2* is the middle atom
of the bend: 

`bend   atom1   atom2   atom3   value

`

**out-of-plane-bends**

Values in degrees, $-180\leq value\leq 180$ *atom2*; angle between
*atom4* and the *atom1–atom2–atom3* plane:

`outp   atom1   atom2   atom3   atom4   value

`

**dihedral angles**

Values in degrees, $-180\leq value\leq 180$; angle the plane
*atom1–atom2–atom3* makes with the plane *atom2–atom3–atom4*:

`tors   atom1   atom2   atom3   atom4   value

`

**coplanar bends**

Values in degrees, $-180\leq value\leq 180$; bending of
*atom1–atom2–atom3* in the plane *atom2–atom3–atom4*: 

`linc   atom1   atom2   atom3   atom4   value

`

**perpendicular bends**

Values in degrees, $-180\leq value\leq 180$; bending of
*atom1–atom2–atom3* perpendicular to the plane
*atom2–atom3–atom4*: 

`linp   atom1   atom2   atom3   atom4   value

`

???+ example "Example 9.11: Methanol geometry optimization with constraints in bond length and bond angles."
    ```qchem
    $molecule
       0  1
       C   0.14192   0.33268   0.00000
       O   0.14192  -1.08832   0.00000
       H   1.18699   0.65619   0.00000
       H  -0.34843   0.74268   0.88786
       H  -0.34843   0.74268  -0.88786
       H  -0.77395  -1.38590   0.00000
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            hf
       BASIS             3-21g
       GEOM_OPT_PRINT    6
    $end
    
    $opt
       CONSTRAINT
       stre  1  6  1.8
       bend  2  1  4  110.0
       bend  2  1  5  110.0
       ENDCONSTRAINT
    $end
    ```
