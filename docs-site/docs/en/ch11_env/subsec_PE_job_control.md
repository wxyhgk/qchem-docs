---
title: "11.8.2 Job Control"
---

## 11.8.2 Job Control

(July 4, 2026)

The PE job control is accomplished in two sections, *$rem* and *$pe*.
To enabling PE-ADC, specification of the ADC method and other ADC job control
parameters (thresholds, max. iterations *etc.*) should be set in the *$rem*
section. PE-ADC supports the excited state analysis
(STATE_ANALYSIS) carried out by the **libwfa** module.

PE

### `PE`

> **Turns PE on.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Perform a PE calculation.
>     * False
>     * Don’t perform a PE calculation.
> * **Recommendation**: Set the $rem variable to TRUE to start a PE calculation.

**Note: 

Turning PE on disables symmetry by setting POINT_GROUP_SYMMETRY to FALSE.

**

**Note: 

Setting the REM variables USE_LIBQINTS and GEN_SCFMAN
to TRUE is required to run PE.
**

The PE-specific options can be set in the *$pe* input section. The format of the *$pe* section
requires key and value pairs separated by a space character:

> ```qchem
> $pe
>    <keyword>  <parameter>
> $end
> ```

**Note: 

The following job control variables belong *only* in the *$pe*
section. Do not place them in the *$rem* section.
**

### `POTFILE`

> **Path of the potential file. INPUT SECTION: $pe**
>
> * **Type**: `STRING`
> * **Default**: `potfile.pot`
> * **Options**:
>     * Provide the path/name of the potential file.
> * **Recommendation**: None

### `DIIS`

> **Use DIIS acceleration to obtain induced moments. INPUT SECTION: $pe**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Turns DIIS acceleration on.
>     * FALSE
>     * Turns DIIS acceleration off (normal Jacobi solver is used).
> * **Recommendation**: TRUE

### `CONVERGENCE_INDUCED`

> **Threshold for induced moments convergence. Converge induced moments to a residual norm of $10^{-\text{CONVERGENCE\_INDUCED}}$ . INPUT SECTION: $pe**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n\leq 12$
>     * Corresponding to
>     * $10^{-n}$
> * **Recommendation**: Use the default unless higher accuracy is desired.

### `MAXITER`

> **Maximum number of iterations for induced moments. INPUT SECTION: $pe**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n\geq 1$
> * **Recommendation**: Use the default. If more iterations are required to converge the induced moments, there might be an error in the system setup.

### `BORDER`

> **Activate border redistribution/removal options for sites in proximity to the QM/MM border. INPUT SECTION: $pe**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Enable border options.
>     * FALSE
>     * Disable border options.
> * **Recommendation**: None

### `BORDER_TYPE`

> **Remove or redistribute multipole moments/polarizabilities. INPUT SECTION: $pe**
>
> * **Type**: `STRING`
> * **Default**: `REMOVE`
> * **Options**:
>     * REMOVE
>     * remove multipole moments/polarizabilities.
>     * REDIST
>     * redistribute multipole moments/polarizabilities.
> * **Recommendation**: None

### `BORDER_RMIN`

> **Minimum distance from QM atoms to MM sites to be taken into account for removal/redistribution INPUT SECTION: $pe**
>
> * **Type**: `FLOAT`
> * **Default**: `2.2`
> * **Options**:
>     * $r>0$
>     * (Unit depends on BORDER_RMIN_UNIT)
> * **Recommendation**: None

### `BORDER_RMIN_UNIT`

> **Unit of BORDER_RMIN, default is atomic units (AU) INPUT SECTION: $pe**
>
> * **Type**: `STRING`
> * **Default**: `AU`
> * **Options**:
>     * AU
>     * Use atomic units.
>     * AA
>     * Use Angstrom.
> * **Recommendation**: None

### `BORDER_REDIST_ORDER`

> **Order from which on moments are removed. For example, if set to 1 (default), only charges are redistributed and all higher order moments are removed. INPUT SECTION: $pe**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n=0,1,2,3,...$
> * **Recommendation**: None

### `BORDER_N_REDIST`

> **Number of neighbor sites to redistribute multipole moments/polarizabilities to. The default (-1) redistributes to all sites which are not in the border region. INPUT SECTION: $pe**
>
> * **Type**: `INTEGER`
> * **Default**: `-1`
> * **Options**:
>     * $n=-1,1,2,3,...,\text{number of MM sites}$
> * **Recommendation**: Use the default value.

### `BORDER_REDIST_POL`

> **Redistribute polarizabilities? If set to FALSE, polarizabilities are removed. INPUT SECTION: $pe**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Redistribute polarizabilities.
>     * FALSE
>     * Remove polarizabilities.
> * **Recommendation**: None

???+ example "Example 11.52: Input for a PE-HF calculation of 4-Nitroaniline in presence of six water
molecules"
    ```qchem
    $comment
    The potential file \texttt{gen\_scfman\_pe\_potfile.pot} can be
    found in the samples folder.
    $end
    
    $molecule
       0 1
       C      8.64800        1.07500       -1.71100
       C      9.48200        0.43000       -0.80800
       C      9.39600        0.75000        0.53800
       C      8.48200        1.71200        0.99500
       C      7.65300        2.34500        0.05500
       C      7.73200        2.03100       -1.29200
       H     10.18300       -0.30900       -1.16400
       H     10.04400        0.25200        1.24700
       H      6.94200        3.08900        0.38900
       H      7.09700        2.51500       -2.01800
       N      8.40100        2.02500        2.32500
       N      8.73400        0.74100       -3.12900
       O      7.98000        1.33100       -3.90100
       O      9.55600       -0.11000       -3.46600
       H      7.74900        2.71100        2.65200
       H      8.99100        1.57500        2.99500
    $end
    
    $rem
       METHOD               HF
       BASIS                STO-3G
       PE                   TRUE
    point_group_symmetry False
       USE_LIBQINTS         TRUE
    $end
    
    $pe
       potfile  gen_scfman_pe_potfile.pot
    $end
    ```
