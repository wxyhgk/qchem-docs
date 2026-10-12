---
title: "12.6.7 ALMO-EDA with Non-Aufbau Electronic Configurations"
---

## 12.6.7 ALMO-EDA with Non-*Aufbau* Electronic Configurations

(July 4, 2026)

**Q-Chem** also supports ALMO-EDA calculations with one or multiple
fragments in non-*aufbau* electronic configurations.[[899]](../bib_references/bib.md#bib931)
 This method is
particularly useful for cases where the energetically most stable electronic
state of a given fragment changes upon the formation of intermolecular
complex, which is common for systems involving open-shell species such
as carbenes, transition metal cations, etc. For example, the lowest-energy
electronic configuration of an isolated Ba${}^{+}$ radical cation is 6s${}^{1}$;
however, when it is ligated with CO, the complex is more stable when
the unpaired electron of Ba${}^{+}$ is promoted from 6s${}^{1}$ to 5d${}^{1}$, which
is thus in a non-*aufbau* state relative to the isolated Ba${}^{+}$ cation. A
sensible strategy to study the formation of such a complex is to perform
an ALMO-EDA calculation with Ba${}^{+}$ in the 5d${}^{1}$ electronic configuration,
and then evaluate the energy difference between Ba${}^{+}$(5d${}^{1}$) and
Ba${}^{+}$(6s${}^{1}$) and interpret that as the monomer “electronic preparation”
energy. To ensure that the system stays in a given non-*aufbau* electronic
configuration throughout, the Maximum Overlap Method [[443]](../bib_references/bib.md#bib455)
 (MOM,
see Sec. [4.5.14](../ch04_scf/topic_mom.md) for details) is applied to almost all stages in ALMO-EDA,
including (i) isolated fragment calculations, (ii) calculation for the polarized wave function,
and (iii) full SCF calculation for the whole system. Among them, (i) and (iii) are
standard SCF calculations using MOM, while (ii) involves the application of MOM
to an SCF-MI calculation,[[899]](../bib_references/bib.md#bib931)
 which is compatible with the use of
DIIS algorithm to solve locally projected SCF equations (with FRGM_METHOD =
STOLL or GIA, see Section [12.5.1](sect_lp_scf.md)).

Specifically, an ALMO-EDA calculation for a complex within a non-*aufbau*
electronic configuration (assuming only one of the fragments is excited)
comprises the following steps:

- Perform ground-state SCF calculations for all fragments
- Calculate the non-*aufbau* electronic configuration for the fragment
as specified in the input using MOM: the energy consumed to excite this fragment
is reported in the output as the *preparation* energy ($E_{\mathrm{prp}}$);
construct the frozen state for the system with that one fragment in the
non-*aufbau* state and the rest in ground state
- Starting from the frozen state, perform an SCF-MI calculation with MOM
to obtain the polarized state within the non-*aufbau* electronic configuration
- Perform a full SCF calculation with MOM, starting from the polarized
wave function in the non-*aufbau* state

Such a calculation requires EDA2_MOM = TRUE in addition to
the setup of standard EDA2 jobs. The non-*aufbau* electronic state is specified
through the *$scfmi_mom* input section, which has the following format:

> ```qchem
> $scfmi_mom
> frag_idx1   X_1   Y_1   spin_1
> frag_idx2   X_2   Y_2   spin_2
> ...
> $end
> ```

In each row, the first entry specifies the index of the non-*aufbau* fragment
(starting from 1). The second and third entries specify the non-*aufbau*
electronic configuration, which is prepared by promoting an electron from
a given fragment’s HOMO$-$X to LUMO$+$Y once the ground-state
SCF calculation of that fragment is finished. The last entry specifies the spin
of the occupied and virtual orbitals that are being swapped (“a” for $\alpha$
electrons and “b” for $\beta$ electrons, and $\alpha$ orbitals will be used by
default if the fourth entry is left blank). For instance, for a
HOMO$\rightarrow$LUMO excitation on the first fragment, this section would
simply look like

> ```qchem
> $scfmi_mom
> 1  0  0  a
> $end
> ```

**Q-Chem** 5 also allows one to perform SCF-MI calculations for non-*aufbau* electronic
configurations,[[899]](../bib_references/bib.md#bib931)
 without going through the entire ALMO-EDA procedure.
To do that, one can simply add SCFMI_MOM = TRUE to the *$rem* setup of an
SCF-MI calculation (see Section [12.6.2](sect_gen_scfmi.md)). The non-*aufbau* electronic
configuration can be specified through the *$scfmi_mom* section in the same way.

### `EDA2_MOM`

> **Perform ALMO-EDA calculation with non- aufbau electronic configurations using MOM**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Standard ALMO-EDA calculation
>     * `TRUE`: ALMO-EDA for non- aufbau states
> * **Recommendation**: None

### `SCFMI_MOM`

> **Perform an SCF-MI calculation with non- aufbau electronic configurations using MOM**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Standard SCF-MI calculation
>     * `TRUE`: SCF-MI calculation with MOM
> * **Recommendation**: None

Note that EDA2_MOM and SCFMI_MOM can be used without
explicitly setting the *$scfmi_mom* section, where the electronic configuration of the
frozen state constructed from two ground-state fragments will be preserved in the SCF-MI
or ALMO-EDA calculation.

???+ example "Example 12.19: ALMO-EDA calculation for the [Ba(CO)] ${}^{+}$ complex with Ba ${}^{+}$ in the
5d ${}^{1}$ electronic configuration at the B3LYP/def2-TZVP level.
The $scfmi_mom section specifies that the unpaired $\alpha$ electron in the 6s orbital is promoted to one of the 5d orbitals."
    ```qchem
    $molecule
    1 2
    --
    1 2
    Ba   0.0  0.0  0.0
    --
    0 1
    C    0.0  0.0  2.734
    O    0.0  0.0  3.876
    $end
    
    $rem
       JOBTYPE           EDA    !by default EDA2 = 2 with CT analysis
       METHOD            B3LYP
       BASIS             DEF2-TZVP
       ECP               DEF2-ECP
       UNRESTRICTED      TRUE
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     DIIS
       EDA2_MOM          TRUE
    $end
    
    $scfmi_mom
    1 0 2
    $end
    ```
