---
title: "9.4.1 Introduction"
---

## 9.4.1 Introduction

(July 4, 2026)

Constrained optimization refers to the optimization of molecular structures
(transition state or minimum-energy) in which certain parameters such as bond
lengths, bond angles or dihedral angles are fixed. **Q-Chem** can handle constraints
directly in delocalized internal coordinates using the method of Lagrange
multipliers (see Section [9.1.5](sec_geom_opt_theory_constrained.md)). Features of constrained
optimization in **Q-Chem** are:

- Starting geometries need not satisfy the requested constraints.
- Constrained optimization is performed in delocalized internal coordinates, which
is typically the most efficient coordinate system for optimization of large molecules.
- **Q-Chem**’s free-format *$opt* section allows the user to apply constraints with ease.

Constraints are imposed via the *$opt* input section, whose format is shown
below, and the various parts of this input section are described below.

!!! note "Note"
    As with the rest of the **Q-Chem** input file, the *$opt* section is
    case-insensitive, but there should be no blank space at the beginning of a line.


> ```qchem
> $opt
> CONSTRAINT
> stre  atom1  atom2  value
> ...
> bend  atom1  atom2  atom3  value
> ...
> outp  atom1  atom2  atom3  atom4  value
> ...
> tors  atom1  atom2  atom3  atom4  value
> ...
> linc  atom1  atom2  atom3  atom4  value
> ...
> linp  atom1  atom2  atom3  atom4  value
> ...
> ENDCONSTRAINT
> 
> FIXED
> atom   coordinate_reference
> ...
> ENDFIXED
> 
> DUMMY
> idum   type   list_length   defining_list
> ...
> ENDDUMMY
> 
> CONNECT
> atom   list_length   list
> ...
> ENDCONNECT
> $end
> ```
