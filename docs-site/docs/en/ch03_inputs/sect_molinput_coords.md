---
title: "3.3.2 Specifying the Molecular Coordinates Manually"
---

## 3.3.2 Specifying the Molecular Coordinates Manually

(July 4, 2026)

Coordinates in the *$molecule* section can be given either in Cartesian form or in *Z*-matrix form, as discussed below.
In either case, **Q-Chem** rotates the user-specified coordinates into the so-called *standard nuclear orientation*,[[448]](../bib_references/bib.md#bib460)

defined as the principle axes of nuclear charge. This helps to make outputs more reproducible, because different
structure-building tools might provide coordinates in different orientations, and quadrature grids used in DFT and some other
types of calculations are not strictly rotationally invariant.[[301]](../bib_references/bib.md#bib305)

Thus, two structures with identical internal coordinates but differing by a rigid rotation can give slightly different energies.
By rotating the user’s input into a standard orientation, identical structures prepared with different graphical user interfaces
should afford the same energy. Occassionally, however, one might want to use the absolute (laboratory-fixed) coordinate frame
that is defined by the coordinates provided in the *$molecule* section. This can be obtained by setting NO_REORIENT = TRUE
in the *$rem* section, which disables rotation into the standard orientation. The coordinate system that **Q-Chem** uses, whether it is
the standard one or the user’s, is printed in the **Q-Chem** output file immediately below where the input file is reproduced.

### `NO_REORIENT`

> **Disable rotation into the standard nuclear orientation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Use the standard nuclear orientation.
>     * `TRUE`: Use the coordinate system defined by the $molecule section.
> * **Recommendation**: Use the default unless you have a reason to want a different coordinate system.

## 3.3.2.1 Cartesian Coordinates

**Q-Chem** can accept a list of $N$ atoms and their $3N$ Cartesian coordinates.
The atoms can be entered either as atomic numbers or atomic symbols where each
line corresponds to a single atom. The **Q-Chem** format for declaring a
molecular geometry using Cartesian coordinates (in Ångstroms) is:

> ```qchem
> atom  x-coordinate  y-coordinate  z-coordinate
> ```

!!! note "Note"
    The geometry can by specified in bohr by setting the *$rem* variable
    INPUT_BOHR equal to TRUE.


```qchem
$molecule
   0 1
   8   0.000000   0.000000  -0.212195
   1   1.370265   0.000000   0.848778
   1  -1.370265   0.000000   0.848778
$end
```

```qchem
$molecule
   0 1
   O   0.000000   0.000000  -0.212195
   H   1.370265   0.000000   0.848778
   H  -1.370265   0.000000   0.848778
$end
```

!!! note "Note"
    1.

    Atoms can be declared by either atomic number or symbol.

    2.

    Coordinates can be entered either as variables/parameters or real numbers.

    3.

    Variables/parameters can be declared in any order.

    4.

    A single blank line separates parameters from the atom declaration.


Once all the molecular Cartesian coordinates have been entered, terminate
the molecular coordinate input with the *$end* keyword.

## 3.3.2.2 *Z*-matrix Coordinates

For small molecules, *Z*-matrix notation is a common input format. The
*Z*-matrix defines the positions of atoms relative to previously defined atoms
using a length, an angle and a dihedral angle. Again, note that all bond
lengths and angles must be in Ångstroms and degrees, unless
INPUT_BOHR is set to TRUE, in which case bond lengths are
specified in bohr.

The first three atom entries of a *Z*-matrix are different from the subsequent
entries. The first *Z*-matrix line declares a single atom. The second line of
the *Z*-matrix input declares a second atom, refers to the first atom and gives
the distance between them. The third line declares the third atom, refers to
either the first or second atom, gives the distance between them, refers to the
remaining atom and gives the angle between them. All subsequent entries begin
with an atom declaration, a reference atom and a distance, a second reference
atom and an angle, a third reference atom and a dihedral angle. This can be
summarized as:

1. First atom.
2. Second atom, reference atom, distance.
3. Third atom, reference atom A, distance between A and the third atom,
reference atom B, angle defined by atoms A, B and the third atom.
4. Fourth atom, reference atom A, distance, reference atom B, angle,
reference atom C, dihedral angle (A, B, C and the fourth atom).
5. All subsequent atoms follow the same basic form as (4)

```qchem
O1
  O2   O1   oo
  H1   O1   ho   O2   hoo
  H2   O2   ho   O1   hoo   H1   hooh
```

Line 1 declares an oxygen atom (O1). Line 2 declares the second oxygen atom
(O2), followed by a reference to the first atom (O1) and a distance between
them denoted `oo`. Line 3 declares the first hydrogen atom (H1), indicates
it is separated from the first oxygen atom (O1) by a distance HO and makes an
angle with the second oxygen atom (O2) of `hoo`. Line 4 declares the
fourth atom and the second hydrogen atom (H2), indicates it is separated from
the second oxygen atom (O2) by a distance HO and makes an angle with the first
oxygen atom (O1) of `hoo` and makes a dihedral angle with the first
hydrogen atom (H1) of `hooh`.

Some further points to note are:

- Atoms can be declared by either atomic number or symbol.

- If declared by atomic number, connectivity needs to be indicated
by *Z*-matrix line number.
- If declared by atomic symbol either number similar atoms (*e.g.*,
H1, H2, O1, O2 *etc.*) and refer connectivity using this symbol, or
indicate connectivity by the line number of the referred atom.
- Bond lengths and angles can be entered either as variables/parameters or
real numbers.

- Variables/parameters can be declared in any order.
- A single blank line separates parameters from the *Z*-matrix.

All the following examples are equivalent in the information forwarded to the
**Q-Chem** program.

```qchem
$molecule
   0 1
   O1
   O2  O1  oo
   H1  O1  ho  O2  hoo
   H2  O2  ho  O1  hoo  H1  hooh

   oo   =   1.5
   oh   =   1.0
   hoo  = 120.0
   hooh = 180.0
$end
```

```qchem
$molecule
   0 1
   O1
   O2  O1  1.5
   H1  O1  1.0  O2  120.0
   H2  O2  1.0  O1  120.0  H1  180.0
$end
```

```qchem
$molecule
   0 1
   8
   8  1  oo
   1  1  ho  2  hoo
   1  2  ho  1  hoo  3  hooh

   oo   =   1.5
   oh   =   1.0
   hoo  = 120.0
   hooh = 180.0
$end
```

```qchem
$molecule
  0 1
  8
  8  1  1.5
  1  1  1.0  2  120.0
  1  2  1.0  1  120.0  3  180.0
$end
```

Obviously, a number of the formats outlined above are less appealing to the
eye and more difficult for us to interpret than the others, but each
communicates *exactly* the same *Z*-matrix to the **Q-Chem** program.

## 3.3.2.3 Dummy Atoms

Dummy atoms are indicated by the identifier $X$ and followed, if necessary, by
an integer. (*e.g.*, $X1$, $X2$. Dummy atoms are often useful for molecules
where symmetry axes and planes are not centered on a real atom, and have also
been useful in the past for choosing variables for structure optimization and
introducing symmetry constraints.

!!! note "Note"
    Dummy atoms play no role in the quantum mechanical calculation, and are
    used merely for convenience in specifying other atomic positions or geometric
    variables.

