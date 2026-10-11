---
title: "6.19.4 Second-Order Correction to Perfect Pairing: PP(2)"
---

## 6.19.4 Second-Order Correction to Perfect Pairing: PP(2)

(July 4, 2026)

The PP and CCVB models are potential replacements for HF theory as a zero order
description of electronic structure and can be used as a starting point for
perturbation theory. They neglect all correlations that involve electron
configurations with one or more orbitals that are outside the active space.
Physically this means that the so-called “dynamic correlations”, which
correspond to atomic-like correlations involving high angular momentum virtual
levels are neglected. Therefore, the GVB models may not be very accurate for
describing energy differences that are sensitive to this neglected correlation
energy, *e.g.*, atomization energies. It is desirable to correct them for this
neglected correlation in a way that is similar to how the HF reference is
corrected via MP2 perturbation theory.

For this purpose, the leading (second-order) correction to the PP model, termed
PP(2),[[112]](../bib_references/bib.md#bib99)
 has been formulated and efficiently implemented for
restricted and unrestricted orbitals (energy only). PP(2) improves upon many of
the worst failures of MP2 theory (to which it is analogous), such as for open
shell radicals. PP(2) also greatly improves relative energies relative to PP
itself. PP(2) is implemented using a resolution of the identity (RI) approach
to keep the computational cost manageable. This cost scales in the same
5th-order way with molecular size as RI-MP2, but with a pre-factor that is
about 5 times larger. It is therefore vastly cheaper than CCSD or CCSD(T)
calculations which scale with the 6th and 7th powers of system size
respectively. PP(2) calculations are requested with CORRELATION = PP(2).
Since the only available algorithm uses auxiliary basis sets, it is
essential to also provide a valid value for AUX_BASIS to have a
complete input file.

The example below shows a PP(2) input file for the challenging case of the N2
molecule with a stretched bond. For this reason a number of the non-standard
options discussed in Sections [6.19.2](subsec_PP.md) and [6.19.5](subsec_GVBMAN_other.md)
for orbital convergence are enabled here. First, this case is an unrestricted
calculation on a molecule with an even number of electrons, and so it is
essential to break the alpha/beta spin symmetry in order to find an
unrestricted solution. Second, we have chosen to leave the lone pairs
uncorrelated, which is accomplished by specifying GVB_N_PAIRS.

???+ example "Example 6.53: A non-standard PP(2) calculation. UPP(2) for stretched N2 with only 3
correlating pairs Try Boys localization scheme for initial guess."
    ```qchem
    $molecule
       0 1
       N
       N   1   1.65
    $end
    
    $rem
       UNRESTRICTED    true
       CORRELATION     pp(2)
       EXCHANGE        hf
       BASIS           cc-pvdz
       AUX_BASIS       rimp2-cc-pvdz   must use RI with PP(2)
       SCF_GUESS_MIX   10              mix SCF guess 100{\%}
       GVB_GUESS_MIX   25              mix GVB guess 25{\%} also!
       GVB_N_PAIRS     3               correlate only 3 pairs
       GVB_ORB_CONV    6               tighter convergence
       GVB_LOCAL       1               use Boys initial guess
    $end
    ```
