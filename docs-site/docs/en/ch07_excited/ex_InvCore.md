---
title: "7.12.1 Many-Body Methods for Core-Excited States"
---

## 7.12.1 Many-Body Methods for Core-Excited States

(July 4, 2026)

A highly robust and accurate strategy is to invoke many-body methods, such as
EOM or ADC, together with the core-valence separation (CVS) scheme.[[218]](../bib_references/bib.md#bib215)

In this approach, the excitations involving core
electrons are decoupled from the rest of the configurational space. This allows
one to reduce computational costs and decouple the highly excited core states
from the continuum. These methods are described in Sections [7.9.9](sub_cvs_eom.md)
and [7.10.7](sect_CVS-ADC.md); CVS can also be deployed within TDDFT as described in Section [7.12.2](subsec_TDDFT-Xray.md).
Error introduced by the CVS approximation is negligible for K-edge (1s $\rightarrow$ virtual) excitations,[[573]](../bib_references/bib.md#bib589)

though its accuracy for other types of x-ray excitations is less certain.

An alternative highly accurate approach for finding core-excitation energies of
closed-shell molecules is to use the restricted open-shell Kohn-Sham (ROKS) approach
that is described in Section [7.7.4](ex_ESROKS.md). ROKS is not systematically improvable
like EOM or ADC methods, but is nonetheless quite accurate and modern density
functionals are capable of predicting excitation energies to $<0.5$ eV
error.[[510]](../bib_references/bib.md#bib525)
 The great strength of the ROKS approach is its
computational efficiency: highly accurate results can be obtained for the same
${\cal{O}}({N^{3}})$ scaling as ground-state meta-GGAs, versus the ${\cal{O}}({N^{6}})$ scaling of EOM-CCSD
or ${\cal{O}}({N^{5}})$ scaling of ADC(2). The basis set requirements of ROKS are also much
more modest than wave function theories, with a mixed basis strategy being
highly effective in practice. Details about using ROKS for core-level excitations can be found
in Section [7.12.4](ex_COCOREIP.md).

Within EOM-CC formalism, one can also use an approximate EOM-EE/IP methods in
which the target states are described by single excitations and double
excitations are treated perturbatively; these methods are described in
Section [7.9.5.2](Ch7.S9.SS5.md#sec:EOM-S-D). While being moderately useful, these methods are
less accurate than the CVS-EOM variants.[[1193]](../bib_references/bib.md#bib1248)

In addition, one can use the $\Delta E$ approach, which amounts to a simple
energy difference calculation in which core ionization is computed from energy
differences computed for the neutral and core-ionized state. This procedure is illustrated
by Example 7.12.1 below.

???+ example "Example 7.204: Q-Chem input for calculating chemical shift for 1s-level of methane
(CH ${}_{\text{4}}$ ). The first job is just an SCF calculation to obtain the orbitals and
CCSD energy of the neutral. The second job solves the HF and CCSD equations for
the core-ionized state."
    ```qchem
    $molecule
       0,1
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       EXCHANGE        = HF
       CORRELATION     = CCSD
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
    $end
    
    @@@
    
    $molecule
       +1,2
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       UNRESTRICTED    = TRUE
       EXCHANGE        = HF
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
       SCF_GUESS       = read  Read MOs from previous job and use occupied as specified below
       CORRELATION     = CCSD
       MOM_START       = 1 Do not reorder orbitals in SCF procedure!
    $end
    
    $occupied
       1 2 3 4 5
       2 3 4 5
    $end
    ```

In this job, we first compute the HF and CCSD energies of neutral CH${}_{\text{4}}$:
$E_{\text{SCF}}=-40.1949062375~{}E_{h}$ and $E_{\text{CCSD}}=-40.35748087~{}E_{h}$ (HF orbital energy
of the neutral gives the Koopmans IE, which is 11.210 hartree = 305.03 eV). In the
second job, we do the same for core-ionized CH${}_{\text{4}}$. To obtain the desired SCF
solution, MOM_START option and *$occupied* keyword are used. The
resulting energies are $E_{\text{SCF}}=-29.4656758483~{}E_{h}$ ($\langle\hat{S}^{2}\rangle$ =
0.7730) and $E_{\text{CCSD}}=-29.64793957~{}E_{h}$. Thus,
$\Delta E_{\text{CCSD}}=10.709~{}E_{h}=291.42$ eV.

This approach can be further extended to obtain multiple excited states
involving core electrons by performing CIS, TDDFT, or EOM-EE calculations.

!!! note "Note"
    This approach often leads to convergence problems in correlated calculations.


One can also use the following trick illustrated by Example 7.12.1.

???+ example "Example 7.205: Q-Chem input for calculating chemical shift for 1s-level of methane
using EOM-IP. Here we solve SCF as usual, then reorder the MOs such
that the core orbital becomes the “HOMO”, then solve the CCSD and EOM-IP
equations with all valence orbitals frozen and the core orbital being active."
    ```qchem
    $molecule
       0,1
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       EXCHANGE        = HF
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
       CORRELATION     = CCSD
       CCMAN2          = false
       N_FROZEN_CORE   = 4 Freeze all valence orbitals
       IP_STATES       = [1,0,0,0] Find one EOM_IP state
    $end
    
    $reorder_mo
       5 2 3 4 1
       5 2 3 4 1
    $end
    ```

Here we use EOM-IP to compute core-ionized states. Since core states are very
high in energy, we use “frozen core” trick to eliminate valence ionized
states from the calculation. That is, we reorder MOs such that our core is the
last occupied orbital and then freeze all the rest. The so computed EOM-IP
energy is 245.57 eV. From the EOM-IP amplitude, we note that this state of a
Koopmans character (dominated by single core ionization); thus, canonical HF
MOs provide good representation of the correlated Dyson orbital. The same
strategy can be used to compute core-excited states.

!!! note "Note"
    The accuracy of this approach is rather poor and is similar to Koopmans’ approximation.

