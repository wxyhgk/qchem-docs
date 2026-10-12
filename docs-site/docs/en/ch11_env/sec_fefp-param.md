---
title: "11.5.11 fEFP Input Structure"
---

## 11.5.11 fEFP Input Structure

(July 4, 2026)

A two-step script, `prefefp.pl` located in
`$QC/bin`, allows users to break molecular structures
from a PDB file into the capped fragments in the **gamess** format, such
that parameters for fEFP calculations can be generated.

To use the `prefefp.pl` scripts you need a PDB file, a MAP file, and a
directory with all your `.efp` parameter files.
Run the following commands to: (1) obtain the $N$ input file generating the
$N$ EFP parameters for the $N$ capped fragments, and (2) create the EFP input file in XYZ format.

```qchem
perl prefp.pl 1 <PDB file> <MAP file>
perl prefp.pl 2 <PDB file> <.efp path> <MAP file> <GMS input file name>
```

At the first step the script splits the biomolecule (PDB format) into $N$
fragments generating $N$ **gamess** MAKEFP input files with the help of a MAP file.

At the second step the `.efp` file from **gamess** MAKEFP is analyzed and
is auto-edited using the same MAP file to create the final EFP
input (XYZ format).

The MAP file is required as an input for the script. It defines groups of
atoms belonging to each EFP fragment both for the MAKEFP calculation and for
the consequent EFP jobs. Here is a description of the MAP file: Each fragment
described using section $RESIDUE followed by closing $end In this example the
Lys2 is extracted cutting through the peptide bond, the cut bond is saturated
with hydrogen atom. The explanation of each variable is given below.

```qchem
$Residue
Name = lys2
PreAtoms = 14-35
NH = 14,12
CH = 34,36
PostAtoms = 14-35
Rescharge = +1
USEFP = lys2
$end
```

The four first lines are required for the first step of the script
(**gamess** MAKEFP job); the next ones are necessary for the actual EFP job:

- `Name`: Residue name
- `PreAtoms`:
Atoms which belongs to the residue for **gamess** MAKEFP calculation.
- `CH, NH, or OH`:
In the case of broken bonds a hydrogen atom is added so
that in X–Y bond (where X belongs to the Lys2 residue and Y belongs to the
previous or next residue) the Y atom is replaced by H along the X–Y axis.
The default equilibrium distance for the X-H bond is set to 1.08 Å for
a C–H bond, to 1.00 Å for a N–H bond, and to 0.94 Å for a O–H bond.
It required to specify the atom number of the X and Y atoms.
- `PostAtoms`:
Atoms which belong to the residue after removing the
overlapping fragment atoms or caps when the HLA or the CLA
scheme is used. This important step removes multipoles and polarizability
expansion points of those atoms according to the cutoff procedure (set by default to 1.3 Å and
1.2 Å for multipoles and polarizability expansion points, respectively).
Multipole expansion at duplicated points are eliminated but to
maintain the net integer charge on each amino acid the monopole expansion
of the caps is redistributed on the natural fragment. This method is called
Expand-Remove-Redistribute. Concerning the polarizability expansion
points, only one polarizability expansion point is removed when a hydrogen atom
saturates the dangling bond, whereas 6 or 5 polarizability points are
removed when the cap is an amine or an aldehyde, respectively.
- `ResCharge`: The net charge of the residue after removing the
overlapping fragment atoms (*cf.* the LA scheme).
- `USEFP`:
Name of the EFP fragment (and `.efp` file) to use with this fragment in the
actual EFP calculation.

!!! note "Note"
    - In the MFCC scheme, the two first letters of the concap fragment have to be “CC”.

    - If the *PostAtoms* keyword is not present, the second script will
    generate an EFP job file without any modification of the parameters, which is useful for the MFCC scheme.

    - **Q-Chem**’s implementation of EFP currently does not support dipole–quadrupole polarizabilities.
    These may be present in a `.efp` generated using **gamess** and should be removed if that file is to be
    read by **Q-Chem**.

