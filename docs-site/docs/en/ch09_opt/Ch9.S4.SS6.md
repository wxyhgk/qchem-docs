---
title: "9.4.6 Additional Atom Connectivity"
---

## 9.4.6 Additional Atom Connectivity

(July 4, 2026)

Normally delocalized internal coordinates are generated automatically from the
input Cartesian coordinates. This is accomplished by first determining the
atomic connectivity list (*i.e.*, which atoms are formally bonded) and then
constructing a set of individual primitive internal coordinates comprising all
bond stretches, all planar bends and all proper torsions that can be generated
based on the atomic connectivity. The delocalized internal are in turn
constructed from this set of primitives.

The atomic connectivity depends simply on distance and there are default bond
lengths between all pairs of atoms in the code. In order for delocalized
internals to be generated successfully, all atoms in the molecule must be
formally bonded so as to form a closed system. In molecular complexes with
long, weak bonds or in certain transition states where parts of the molecule
are rearranging or dissociating, distances between atoms may be too great for
the atoms to be regarded as formally bonded, and the standard atomic
connectivity will separate the system into two or more distinct parts. In this
event, the generation of delocalized internal coordinates will fail. Additional
atomic connectivity can be included for the system to overcome this difficulty.

CONNECT defines the beginning of the additional connectivity section
and ENDCONNECT the end. The format of the CONNECT section is:

> ```qchem
> CONNECT
> atom   list_length   list
> ENDCONNECT
> ```

| atom | Atom for which additional connectivity is being defined. |
| --- | --- |
| list_length | Number of atoms in the list of bonded atoms. |
| list | List of up to 8 atoms considered as being bonded to the given atom. |
