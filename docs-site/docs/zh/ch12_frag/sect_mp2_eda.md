---
title: "12.7.1 ALMO-EDA for the MP2 Method"
---

## 12.7.1 ALMO-EDA for the MP2 Method

(July 4, 2026)

The previously described EDA methods are limited to SCF methods such as HF and
DFT. However, for many systems, it is preferable to use a wave function based
correlation method. For this reason, the ALMO-EDA has been extended to
MP2.[[1353]](../bib_references/bib.md#bib1413)
 The MP2 ALMO-EDA is based on the
first-generation ALMO-EDA. It provides an MP2 correction to the FRZ, POL, and
CT terms defined by the ALMO-EDA and also adds in a term corresponding to the
London dispersion force. This is done by defining a constrained intermediate
MP2 wave function corresponding to each HF intermediate.

The current implementation is limited to only RI-MP2 rather than full MP2, and
only works in the closed shell, spin restricted case. Frozen core and spin
scaling are also not yet supported. Attempting to use the EDA with a
correlation method other then RI-MP2 or with unrestricted orbitals will result
in a crash. Frozen core and spin scaling settings will be ignored with a
warning by the EDA, but not by the final energy, leading to inconsistent
results.

Though the MP2 EDA is based on the first generation ALMO-EDA, the code path and
REM settings are shared with the second generation ALMO-EDA. The MP2 ALMO-EDA
does not define any new REM variables of its own. Rather, running an EDA job
with EDA2 and GEN_SCFMAN will trigger an MP2 ALMO-EDA when the correlation
method is RI-MP2. The correlation setting causes the SCF portion of the EDA to
be switched back to the original scheme and will also decompose the correlation
energy. Most settings intended for the second generation ALMO-EDA are not
supported, but EDA_NO_CT and EDA_BSSE are. An example
appears below.

???+ example "Example 12.27: MP2 energy decomposition analysis of the water dimer."
    ```qchem
    $molecule
    0 1
    --
    0 1
    O  -0.031783  -0.057754   0.000000
    H  -0.415035   0.819269   0.000000
    H   0.919546   0.097478   0.000000
    --
    0 1
    O   2.960796   0.171800   0.000000
    H   3.290569  -0.313410  -0.758561
    H   3.290569  -0.313410   0.758561
    $end
    
    $rem
       JOBTYPE         EDA
       GEN_SCFMAN      TRUE
       EDA2            TRUE
       FRGM_METHOD     STOLL
       EXCHANGE        HF
       CORRELATION     RIMP2
       BASIS           aug-cc-pVTZ
       AUX_BASIS       rimp2-aug-cc-pVTZ
       THRESH          14
       SCF_CONVERGENCE 10
       N_FROZEN_CORE   0
       EDA_BSSE        TRUE
       USE_LIBQINTS    0
       INTEGRAL_SYMMETRY FALSE
    $end
    ```
