---
title: "12.6.6 ALMO-EDA with Implicit Solvent Models"
---

## 12.6.6 ALMO-EDA with Implicit Solvent Models

(July 4, 2026)

Since the majority of chemical processes occur in the condensed phase, it
is often desirable to investigate intermolecular interactions in the presence
of solvents. The solvation environment can affect intermolecular interactions
in a variety of ways such that the gas-phase ALMO-EDA may not be capable of
revealing the physical picture of these interactions correctly. To address this
gap, Mao *et al.* have proposed the ALMO-EDA(solv) approach,[[897]](../bib_references/bib.md#bib932)

which, unlike many other EDA schemes, incorporates the
solvation effect in the evaluation of all the energy components. Currently,
ALMO-EDA(solv) supports two widely used implicit solvent models:
PCM and SMD (see Sec. [11.2](../ch11_env/topic_solvation.md)). More solvation models will
be made compatible in future releases of **Q-Chem**.

Within the ALMO-EDA(solv) scheme, the interaction energy to be decomposed is
given by the energy difference between the solvated, fully relaxed complex and the
sum of the energies of individually solvated, non-interacting fragments. [[897]](../bib_references/bib.md#bib932)

As in gas-phase ALMO-EDA, the total interaction energy (INT) can be partitioned into
frozen (FRZ), polarization (POL), and charge transfer (CT) contributions:

<a id="A3.S8.EGx119"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{INT}}^{(\mathrm{s})}&\displaystyle=E_{\mathrm{Full}}^{(\mathrm{s})}-\sum_{A}E_{A}^{(\mathrm{s})}\\
&\displaystyle=\Delta E^{(\mathrm{s})}_{\mathrm{FRZ}}+\Delta E^{(\mathrm{s})}_{\mathrm{POL}}+\Delta E^{(\mathrm{s})}_{\mathrm{CT}}\end{aligned} \tag{12.18}
$$

Here the superscript “(s)” indicates that the energetic terms are evaluated with the
solvent taken into account.

The frozen interaction energy ($\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}$) is defined as
the energy change upon the formation of a solvated complex from several individually
solvated non-interacting fragments *without* relaxing their orbitals, which can be
further decomposed into permanent electrostatics (ELEC), Pauli repulsion (PAULI), and
dispersion (DISP) contributions:

<a id="A3.S8.EGx120"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}&\displaystyle=E_{\mathrm{FRZ}}^{(\mathrm{s})}-\sum_{A}E_{A}^{(\mathrm{s})}\\
&\displaystyle=(E_{\mathrm{FRZ}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{0})})-\sum_{A}(E_{A}^{(\mathrm{s})}-E_{A}^{(0)})+E_{\mathrm{FRZ}}^{(0)}-\sum_{A}E_{A}^{(0)}\\
&\displaystyle=\Delta E_{\mathrm{SOL}}+\Delta E^{(0)}_{\mathrm{ELEC}}+\Delta E^{(0)}_{\mathrm{PAULI}}+\Delta E^{(0)}_{\mathrm{DISP}}\end{aligned} \tag{12.19}
$$

Here we have introduced a new term,

<a id="Ch12.E20"></a>
$$
\Delta E_{\mathrm{SOL}}=(E_{\mathrm{FRZ}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{0})})-\sum_{A}(E_{A}^{(\mathrm{s})}-E_{A}^{(0)}) \tag{12.20}
$$

to quantify the loss/gain of solvation energy upon the formation of the frozen complex.
The other three terms in Eq. [12.19](#eq:frz_decomp_sol), $\Delta E^{(0)}_{\mathrm{ELEC}})$,
$\Delta E^{(0)}_{\mathrm{PAULI}}$, and $\Delta E^{(0)}_{\mathrm{DISP}}$, are
evaluated in the same way as in vacuum [[595]](../bib_references/bib.md#bib619)
 (as indicated by the superscripts
“(0)”) but using MOs of solvated fragments.

In the most general cases, the solvent contribution to the frozen interaction
($\Delta E_{\mathrm{SOL}}$) includes both electrostatic ($\Delta E_{\mathrm{SOL}}^{\mathrm{el}}$)
and non-electrostatic ($\Delta E_{\mathrm{SOL}}^{\text{non-el}}$) components, which can be
combined with the “gas-phase” ELEC and PAULI terms, respectively. In addition, we ignore
the solvent contribution to dispersion, an effect that cannot be captured by dispersion-corrected
DFT that ALMO-EDA(solv) is based upon, which leads to $\Delta E^{(0)}_{\mathrm{DISP}}\approx\Delta E^{(\mathrm{s})}_{\mathrm{DISP}}$. The decomposition of the frozen energy in the
solvation environment (Eq. [12.19](#eq:frz_decomp_sol)) can thus be rewritten as

<a id="A3.S8.EGx121"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}&\displaystyle=(\Delta E^{(0)}_{\mathrm{ELEC}}+\Delta E_{\mathrm{SOL}}^{\mathrm{el}})+(\Delta E^{(0)}_{\mathrm{PAULI}}+\Delta E_{\mathrm{SOL}}^{\text{non-el}})+\Delta E^{(0)}_{\mathrm{DISP}}\\
&\displaystyle=\Delta E^{(\mathrm{s})}_{\mathrm{ELEC}}+\Delta E^{(\mathrm{s})}_{\mathrm{PAULI}}+\Delta E^{(\mathrm{s})}_{\mathrm{DISP}}\end{aligned} \tag{12.21}
$$

Starting from the solvated frozen complex, one can relax the fragment orbitals using the SCF-MI
technique in presence of solvent. The associated energy lowering is defined as the
polarization energy in ALMO-EDA(solv) ($\Delta E_{\mathrm{POL}}^{(\mathrm{s})}$):

<a id="Ch12.E22"></a>
$$
\Delta E_{\mathrm{POL}}^{(\mathrm{s})}=E_{\mathrm{POL}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{s})} \tag{12.22}
$$

where $E_{\mathrm{POL}}^{(\mathrm{s})}$ is the converged SCF-MI energy with solvent. Similarly,
the charge-transfer term is given by

<a id="Ch12.E23"></a>
$$
\Delta E_{\mathrm{CT}}^{(\mathrm{s})}=E_{\mathrm{Full}}^{(\mathrm{s})}-E_{\mathrm{POL}}^{(\mathrm{s})} \tag{12.23}
$$

where $E_{\mathrm{Full}}^{(\mathrm{s})}$ is the full SCF energy evaluated with the presence of solvent.
With that, the solvation effects are implicitly incorporated in the POL and CT terms produced by
the ALMO-EDA(solv) scheme.

???+ example "Example 12.17: EDA calculation for the water-Mg ${}^{2+}$ complex in PCM water."
    ```qchem
    $molecule
    2 1
    --
    0 1
    H1
    H2 H1 1.55618
    O1 H2 0.97619  H1 37.14891
    --
    2 1
    Mg1 O1 scan    H2 127.14892  H1 180.0
    
    scan = 1.91035
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              2
       METHOD            wb97m-v
       BASIS             6-31+g(d)
       UNRESTRICTED      false
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       MAX_SCF_CYCLES    200
       THRESH            14
       SOLVENT_METHOD    pcm
       EDA_CLS_DISP      true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $PCM
       THEORY                     CPCM
       METHOD                     SWIG
       SOLVER                     INVERSION
       HPOINTS                    302
       HEAVYPOINTS                302
    $END
    
    $SOLVENT
       DIELECTRIC                 78.39
    $END
    ```

???+ example "Example 12.18: EDA calculation for the water-Mg ${}^{2+}$ complex in SMD water."
    ```qchem
    $molecule
    2 1
    --
    0 1
    H1
    H2 H1 1.55618
    O1 H2 0.97619  H1 37.14891
    --
    2 1
    Mg1 O1 scan    H2 127.14892  H1 180.0
    
    scan = 1.91035
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              2
       METHOD            wb97m-v
       BASIS             6-31+g(d)
       UNRESTRICTED      false
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       MAX_SCF_CYCLES    200
       THRESH            14
       SOLVENT_METHOD    smd
       EDA_CLS_DISP      true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $smx
       solvent water
    $end
    ```
