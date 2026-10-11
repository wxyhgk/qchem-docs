---
title: "3.3.1 Introduction"
---

## 3.3.1 Introduction

(July 4, 2026)

The *$molecule* section communicates to the program the charge, spin
multiplicity, and geometry of the molecule being considered. The molecular
coordinates input begins with two integers: the net charge and the spin
multiplicity of the molecule. The net charge can be any integer, including 0 for neutral molecules, positive for cations, negative for anions.
The multiplicity can be any integer as well (1 for a singlet, 2 for
a doublet, 3 for a triplet, *etc.*). Each subsequent line of the molecular
coordinate input corresponds to a single atom in the molecule (or dummy atom),
regardless of whether using *Z*-matrix internal coordinates or Cartesian coordinates.

**Note: 

The coordinate system used for declaring an initial molecular geometry by
default does not affect that used in a geometry optimization procedure. See
Chapter [9.1](../ch09_opt/sec_geom_opt.md) which discusses the geometry optimization packages in further detail.
**

**Q-Chem** begins all calculations by rotating and translating the user-defined
molecular geometry into a Standard Nuclear Orientation whereby the center of
nuclear charge is placed at the origin. This is a standard feature of most
quantum chemistry programs. This action can be turned off by
using POINT_GROUP_SYMMETRY FALSE.

**Note: 

POINT_GROUP_SYMMETRY = FALSE will also turn off
determining and using of the point group symmetry.
**

**Note: 

**Q-Chem** ignores commas and equal signs, and requires all distances,
positions and angles to be entered as Ångstroms and degrees unless the
INPUT_BOHR *$rem* variable is set to TRUE, in which case all
lengths are assumed to be in bohr.
**
