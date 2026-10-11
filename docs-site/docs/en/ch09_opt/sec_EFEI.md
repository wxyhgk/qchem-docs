---
title: "9.5.1 Application of External Forces"
---

## 9.5.1 Application of External Forces

(July 4, 2026)

In 2009, three methods for optimizing the geometry of a molecule under a
constant external force were introduced, which were called *Force-Modified
Potential Energy Surface* (FMPES),[[1022]](../bib_references/bib.md#bib1064)
*External Force is Explicitly Included* (EFEI),[[1164]](../bib_references/bib.md#bib1217)

and *Enforced Geometry Optimization* (EGO).[[1488]](../bib_references/bib.md#bib1549)

These methods are closely related, and the interested reader is referred to Ref. [[1296]](../bib_references/bib.md#bib1351)

for a detailed discussion of the similarities and differences between them. For
simplicity, we will stick to the term EFEI here. An EFEI
calculation is a geometry optimization in which a constant that is equal to the
external force is added to the nuclear gradient of two atoms specified by the
user. The external force is applied along the vector connecting the two atoms,
thus driving them apart. The geometry optimization converges when the restoring
force of the molecule is equal to the external force. The EFEI method can also
be used in AIMD simulations (Section [9.9](topic_aimd.md)), in which case the
force is added in every time step.

**Q-Chem** 5.4 is the first version that uses a new syntax for specifying EFEI
calculations, which requires DISTORT = TRUE in the *$rem* section
(see Section [9.5](sec_Pressure.md)):

> ```qchem
> $distort
>    model efei
>    force [atom1 atom2 force1]
>    force [atom3 atom4 force2]
>    ...
> $end
> ```

Here, *atom1* and *atom2* are the indices of the atoms to which a
force is applied. *force1* is the sum of the force values that acts on
*atom1* and *atom2* in nanoNewtons (nN). If this value is
positive, a mechanical force of magnitude *force1*/2 acts on each of
these atoms, thus driving them apart. If it is negative, an attractive force
acts between the atoms. Optionally, additional pairs of atoms that are subject
to a force can be specified by adding lines in the *$distort* section.
