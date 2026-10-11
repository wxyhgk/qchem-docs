---
title: "4.10.2 Job Control"
---

## 4.10.2 Job Control

(July 4, 2026)

xTB calculations are requested through the usual *$rem* section. The only
mandatory keyword is METHOD = XTB; all other controls are optional.
Charge and multiplicity are specified in the standard way in the
*$molecule* section. In xTB mode, **Q-Chem** automatically uses valence
electrons when constructing the occupation pattern, so users should simply
provide the chemically correct molecular charge and multiplicity.

METHOD

### `METHOD`

> **XTB**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * None.
> * **Recommendation**: Set to XTB .

BASIS

### `BASIS`

> **XTB**
>
> * **Type**: `STRING`
> * **Default**: `XTB (implied)`
> * **Options**:
>     * None
> * **Recommendation**: For METHOD = XTB , BASIS = XTB is implied and may be omitted. No other basis is allowed.

XTB_FERMI_TEMP

### `XTB_FERMI_TEMP`

> **Controls the Fermi-smearing temperature used for fractional occupations in xTB calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * $n\geq 0$
>     * Temperature in Kelvin.
> * **Recommendation**: The default is usually appropriate. Setting XTB_FERMI_TEMP = 0 recovers integer occupations.

Standard SCF controls such as SCF_ALGORITHM and
SCF_CONVERGENCE are also available. SCF_ALGORITHM = DIIS is the default, while
SCF_ALGORITHM = GDM or SCF_ALGORITHM = ROBUST can be useful for difficult cases.
