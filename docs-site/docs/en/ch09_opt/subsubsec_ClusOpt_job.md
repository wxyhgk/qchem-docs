---
title: "9.12.2 Cluster Optimization Job Control"
---

## 9.12.2 Cluster Optimization Job Control

(July 4, 2026)

NSEARCH

### `NSEARCH`

> **INTEGER**
>
> * **Type**: `Sets the number of structures that are generated and optimized.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

SEARCH_ATOMIC

### `SEARCH_ATOMIC`

> **Perform an optimization for atomic cluster.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Atomic cluster search will be performed.
>     * False
>     * Molecular clusters search will be performed.
> * **Recommendation**: Use N_SWOP to specify atomic number of atom swops in structure generation.

N_SWOP

### `N_SWOP`

> **INTEGER**
>
> * **Type**: `Sets the number atom coordinate swops for atomic cluster search.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined
> * **Recommendation**: None

N_MOL_TYPE

### `N_MOL_TYPE`

> **INTEGER**
>
> * **Type**: `Sets the number of different atom or molecule types.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined : can be 1 or 2.
> * **Recommendation**: None

NMOL1

### `NMOL1`

> **INTEGER**
>
> * **Type**: `Sets the number of molecules of type 1.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

N_ATOM_TYPE_1

### `N_ATOM_TYPE_1`

> **INTEGER**
>
> * **Type**: `Sets the number atoms in molecule type 1.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

NMOL2

### `NMOL2`

> **INTEGER**
>
> * **Type**: `Sets the number of molecules of type 2.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

N_ATOM_TYPE_2

### `N_ATOM_TYPE_2`

> **INTEGER**
>
> * **Type**: `Sets the number atoms in molecule type 2.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

MAXBOX

### `MAXBOX`

> **Sets the size of the box which the molecules are kept within.**
>
> * **Type**: `INTEGER`
> * **Default**: `20000`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * =
>     * $n/1000$
>     * bohr.
> * **Recommendation**: Need to ensure that the cluster can fit within this box.

MIN_SEPARATION

### `MIN_SEPARATION`

> **Reject initial structures where the closest approach of molecules is less than this value.**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * =
>     * $n/100$
>     * bohr.
> * **Recommendation**: of approximately 2.5 bohr.

MAX_DISPLACE

### `MAX_DISPLACE`

> **Sets the maximum distance a molecule will be moved during a translation.**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * =
>     * $n/100$
>     * bohr.
> * **Recommendation**: None.

SCF_NOCRASH

### `SCF_NOCRASH`

> **Ensure the calculations continues if the SCF fails to converge for a given structure.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Ensure calculation will continue with next structure.
>     * False
>     * Calculation will stop.
> * **Recommendation**: Use = TRUE .

TIGHTEN_CONVERG

### `TIGHTEN_CONVERG`

> **At the end of the search re-calculate the energies of the optimized structures with tighter SCF convergence criteria.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Additional calculations with tighter SCF convergence performed.
>     * False
>     * No additional calculations performed.
> * **Recommendation**: None.

USE_INITIAL

### `USE_INITIAL`

> **Include input structure as part of the search.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Input structure is included in the search.
>     * False
>     * Input structure is not included in the search.
> * **Recommendation**: None.

SEARCH_MOM

### `SEARCH_MOM`

> **Allows the search to be performed in conjunction with MOM to explore excited states.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * A search with MOM is performed.
>     * False
>     * Normal calculation without MOM.
> * **Recommendation**: None.

MC_CYCLES

### `MC_CYCLES`

> **INTEGER**
>
> * **Type**: `Sets the number of cycles in a basin hopping search.`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

MC_STEPS

### `MC_STEPS`

> **INTEGER**
>
> * **Type**: `Sets the number of Monte Carlo steps in each`
> * **Default**: `No default.`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

MC_TEMP

### `MC_TEMP`

> **INTEGER**
>
> * **Type**: `Sets the temperature (in Kelvin).`
> * **Default**: `300`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

N_MOVES

### `N_MOVES`

> **INTEGER**
>
> * **Type**: `Sets the number of structural changes/moves on each step.`
> * **Default**: `2`
> * **Options**:
>     * User defined.
> * **Recommendation**: None

MAX_JUMP

### `MAX_JUMP`

> **INTEGER**
>
> * **Type**: `Sets the number of moves accepted on jumping.`
> * **Default**: `10`
> * **Options**:
>     * User defined.
> * **Recommendation**: None
