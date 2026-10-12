---
title: "3.4.1 Overview"
---

## 3.4.1 Overview

(July 4, 2026)

The *$rem* section in the input file is the means by which users specify the
type of calculation that they wish to perform (*i.e.*, level of theory, basis
set, convergence criteria, additional special features, *etc.*). The keyword
*$rem* signals the beginning of the overall job specification. Within the
*$rem* section the user inserts **$rem**** variables** (one per line) which
define the essential details of the calculation. The allowed format is either

> ```qchem
> REM_VARIABLE     VALUE    [ comment ]
> ```

or alternatively

> ```qchem
> REM_VARIABLE   =  VALUE   [ comment ]
> ```

The “=” sign is automatically discarded and only the first two remaining
arguments are read, so that all remaining text is ignored and can be used to
place comments in the input file. Thus the *$rem* section that provides
**Q-Chem** job control takes the form shown in the following example.

The general format of the *$rem* section of the text input file is

> ```qchem
> $rem
>   REM_VARIABLE  value  [ comment ]
>   REM_VARIABLE  value  [ comment ]
>   ...
> $end
> ```

**Note: 

1.

Tab stops can be used to format input.

2.

A line prefixed with an exclamation mark ‘!’ is treated as a comment
and will be ignored by the program.

3.

*$rem* variables are case-insensitive (as is the whole **Q-Chem** input file).

4.

Depending on the particular *$rem* variable, “`value`” may be a
keyword (string), an integer, or a logical value (true or false).

5.

A complete list of *$rem* variables can be found in Appendix [B](../app_b_quickref/app_quick_ref.md).

**

In this manual, *$rem* variables will be described using the following format:

### `REM_VARIABLE_NAME`

> **A short description of what the variable controls.**
>
> * **Type**: `The type of variable (INTEGER, LOGICAL or STRING)`
> * **Default**: `The default value, if any.`
> * **Options**:
>     * A list of the options available to the user.
> * **Recommendation**: A brief recommendation, where appropriate.

For example:

### `IQMOL_FCHK`

> **Controls printing of a formatted checkpoint file that can be read by the IQmol program.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Generate a checkpoint file named inputfilename.fchk .
> * **Recommendation**: For many Q-Chem jobs there is no reason not to generate the checkpoint file. Note that GUI = 2 (used by IQmol ) is synonymous with = TRUE .

If a default setting is indicated for a particular *$rem* variable, then it is
not necessary to declare that variable in order for the default setting to be
used. For example, the default value for the variable JOBTYPE is
SP, indicating a single-point energy calculation, so to perform such a
calculation the user does **not** need to set the JOBTYPE
variable. To perform a geometry optimization, however, it is necessary to
override this default by setting JOBTYPE = OPT. System
administrator preferences for default *$rem* settings can be specified in the
`$QC/config/preferences` file, and user preferences in a
`$HOME/.qchemrc` file, both of which are described in
Section [2.1.6](../ch02_install/sect_customization.md).

**Q-Chem** provides defaults for most *$rem* variables, but the user will always
have to stipulate a few others. In a single point energy calculation, for
example, the minimum requirements will be BASIS (defining the basis
set) and METHOD (defining the level of theory for correlation and
exchange). For example, METHOD = HF invokes a Hartree-Fock
calculation, whereas METHOD = CIS specifies a CIS
excited-state calculation.

```qchem
$rem
  BASIS         6-31G*   Just a small basis set
  METHOD        mp2      MP2
$end
```

The level of theory can alternatively be specified by setting values for two
other *$rem* variables, EXCHANGE (defining the level of theory to
treat exchange) and CORRELATION (defining the level of theory to treat
electron correlation, if required). For excited states computed using
equation-of-motion (EOM) methods (Chapter [7](../ch07_excited/chap_excited.md)), there is a third
*$rem* variable, EOM_CORR, which specifies the level of correlation
for the target states.

For DFT calculations, METHOD specifies an exchange-correlation
functional; see Section [5.4](../ch05_dft/sect_DFT_METHOD.md) for a list of supported
functionals. For wave function approaches, supported values of METHOD
can be found in Section [6.1](../ch06_correlation/sect_c5Intro.md) for ground-state methods and in
Section [7.1](../ch07_excited/sect_ExStatesSummary.md) for excited-state methods. If a wave
function-based correlation treatment such as MP2 or CC is requested using the
CORRELATION keyword, then HF is taken as the default for
EXCHANGE.
