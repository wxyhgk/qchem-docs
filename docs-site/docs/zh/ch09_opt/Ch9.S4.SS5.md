---
title: "9.4.5 Dummy Atom Placement in Dihedral Constraints"
---

## 9.4.5 Dummy Atom Placement in Dihedral Constraints

(July 4, 2026)

Bond and dihedral angles cannot be constrained in Cartesian optimizations to
exactly $0^{\circ}$ or $\pm 180^{\circ}$. This is because the corresponding
constraint normals are zero vectors. Also, dihedral constraints near these two
limiting values (within, say $20^{\circ}$) tend to oscillate and are difficult
to converge.

These difficulties can be overcome by defining dummy atoms and redefining the
constraints with respect to the dummy atoms. For example, a dihedral constraint
of $180^{\circ}$ can be redefined to two constraints of $90^{\circ}$ with
respect to a suitably positioned dummy atom. The same thing can be done with a
$180^{\circ}$ bond angle (long a familiar use in *Z*-matrix construction).

Typical usage is as shown in Table [9.3](#tab9.2). Note that the
order of atoms is important to obtain the correct signature on the dihedral
angles. For a $0^{\circ}$ dihedral constraint, atoms J and K should be switched in
the definition of the second torsion constraint in Cartesian coordinates.

| Internal Coordinates | Cartesian Coordinates |
| --- | --- |
| $opt | $opt |
| CONSTRAINT | DUMMY |
| tors I J K L 180.0 | M 2 I J K |
| ENDCONSTRAINT | ENDDUMMY |
| $end | CONSTRAINT |
|  | tors I J K M 90 |
|  | tors M J K L 90 |
|  | ENDCONSTRAINT |
|  | $end |

Table 9.3: 
Comparison of dihedral angle constraint method for adopted coordinates.

**Note: 

In almost all cases the above discussion is somewhat academic, as
internal coordinates are now best imposed using delocalized internal
coordinates and there is no restriction on the constraint values.
**
