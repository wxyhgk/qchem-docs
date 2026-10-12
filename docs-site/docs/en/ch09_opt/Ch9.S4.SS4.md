---
title: "9.4.4 Dummy Atoms"
---

## 9.4.4 Dummy Atoms

(July 4, 2026)

DUMMY defines the beginning of the dummy atom section and
ENDDUMMY its conclusion. Dummy atoms are used to help define constraints
during constrained optimizations in Cartesian coordinates. They cannot be used
with delocalized internals.

All dummy atoms are defined with reference to a list of real atoms, that is,
dummy atom coordinates are generated from the coordinates of the real atoms
from the dummy atoms defining list (see below). There are three types of dummy
atom:

1. Positioned at the arithmetic mean of up to seven real atoms in the defining
list.
2. Positioned a unit distance along the normal to a plane defined by three
atoms, centered on the middle atom of the three.
3. Positioned a unit distance along the bisector of a given angle.

The format for declaring dummy atoms is:

> ```qchem
> DUMMY
> idum    type   list_length    defining_list
> ENDDUMMY
> ```

| idum | Center number of defining atom (must be one greater than the total number of real atoms for the first dummy atom, two greater for second etc. ). |
| --- | --- |
| type | Type of dummy atom (either 1, 2 or 3; see above). |
| list_length | Number of atoms in the defining list. |
| defining_list | List of up to seven atoms defining the position of the dummy atom. |

Once defined, dummy atoms can be used to define standard internal (distance,
angle) constraints as per the constraints section, above.

!!! note "Note"
    The use of dummy atoms of type 1 has never progressed beyond the experimental stage.

