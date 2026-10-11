---
title: "10.5.7 Electron Localization Function"
---

## 10.5.7 Electron Localization Function

(July 4, 2026)

Formulated by Becke and Edgecombe,[[86]](../bib_references/bib.md#bib76)
 the electron localization function (ELF),

<a id="Ch10.E63"></a>

$$
\text{ELF}=\Bigg{[}1+\Bigg{(}\frac{\tau_{\sigma}-\|\hat{\nabla}\rho_{\sigma}\|^{2}/(4\rho_{\sigma})}{\frac{3}{5}(6\pi^{2})^{2/3}(\rho_{\sigma}^{5/3})}\Bigg{)}^{\!2}\Bigg{]}^{-1} \tag{10.63}
$$

is a measure of electron localization.
It is derived from the Hartree-Fock conditional pair probability and can reveal information about bonding and shell structure.

The function $\text{ELF}(\mathbf{r})$ has values that lie between 0 and 1, with $\text{ELF}=1$
representing perfect localization and $\text{ELF}=1/2$
representing electron-gas-like pair probability. To generate ELF plots with **Q-Chem**, set the
PLOT_ELF *$rem* variable to TRUE.
For closed-shell systems, only the $\alpha$-spin ELF is calculated whereas for open-shell systems
(spin-unrestricted calculations), both $\alpha$- and $\beta$-spin ELFs are computed.[[702]](../bib_references/bib.md#bib734)

The following example illustrates the calculation of the ELF for a water molecule.

???+ example "Example 10.31: A job that evaluates the ELF for H ${}_{2}$ O on a $50\times 50\times 50$ grid. The output is in a cube file called elf_alpha.0.cube ."
    ```qchem
    $molecule
       0 1
       O    -4.5320698567   0.2524215916      0.0130780103
       H    -3.5641829319   0.2173288989     -0.0173259969
       H    -4.8109190521  -0.4489616171     -0.5945943692
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            b3lyp
       BASIS             6-31g*
       PLOT_ELF          true
       MAKE_CUBE_FILES   true
       geom_opt_driver optimize
    $end
    
    $plots
    water
    50 -7 7
    50 -4 4
    50 -4 4
    0 1 0 0
    0
    $end
    ```

Please refer also to `elf_methane.in` the `$QC/samples` directory, which uses the newer *$plots* format.
