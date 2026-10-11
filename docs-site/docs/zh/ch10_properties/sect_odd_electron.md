---
title: "10.2.4 Population of Effectively Unpaired Electrons"
---

## 10.2.4 Population of Effectively Unpaired Electrons

(July 4, 2026)

In a stretched hydrogen molecule the two electrons that are paired at
equilibrium forming a bond become un-paired and localized on the individual H
atoms. In singlet diradicals or doublet triradicals such a weak paring exists
even at equilibrium. At a single-determinant SCF level of the theory the
valence electrons of a singlet system like H${}_{2}$ remain perfectly paired, and
one needs to include non-dynamical correlation to decouple the bond electron
pair, giving rise to a population of effectively-unpaired (“odd”,
radicalized) electrons.[[1339]](../bib_references/bib.md#bib1573)

When the static correlation is strong, these electrons remain mostly unpaired
and can be described as being localized on individual atoms.

These phenomena can be properly described within wave-function formalism.
Within DFT, these effects can be described by broken-symmetry approach or by
using SF-TDDFT (see Section [7.3.1](../ch07_excited/sect_tddftintro.md)). Below we describe how to
derive this sort of information from pure DFT description of such low-spin
open-shell systems without relying on spin-contaminated solutions.

The first-order reduced density matrix (1-RDM) corresponding to a
single-determinant wave function (*e.g.*, SCF or Kohn-Sham DFT) is idempotent:

<a id="A3.S8.EGx73"></a>
$$
\displaystyle\begin{aligned} \displaystyle\rho_{\sigma}({\mathbf{r}_{1}})&\displaystyle=\int\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)\,d{\mathbf{r}_{2}}\\
\displaystyle\gamma_{\sigma}^{\text{SCF}}(1;2)&\displaystyle=\sum_{i}^{\text{occ}}\psi_{i\sigma}^{\mathrm{KS}}(1)\psi_{i\sigma}^{\mathrm{KS}}(2)\;,\end{aligned} \tag{10.9}
$$

where $\rho_{\sigma}(1)$ is the electron density of spin $\sigma$ at position
$\mathbf{r}_{1}$, and $\gamma_{\sigma}^{\text{SCF}}$ is the spin-resolved
1-RDM of a single Slater determinant. The cross product
$\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)$
reflects the Hartree-Fock exchange (or Kohn-Sham exact-exchange) governed by
the HF exchange hole:

<a id="A3.S8.EGx74"></a>
$$
\displaystyle\begin{aligned} \displaystyle\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)&\displaystyle=\rho_{\alpha}(1)h_{\mathrm{X}\sigma\sigma}(1,2)\\
\displaystyle\int{h}_{{\text{X}}\sigma\sigma}(1,2)\>d{\bf r}_{2}&\displaystyle=1\;.\end{aligned} \tag{10.10}
$$

When 1-RDM includes electron correlation, it becomes non-idempotent:

<a id="eq:non-idempotent1"></a>
$$
D_{\sigma}(1)\equiv{\rho}_{\sigma}(1)-\int\gamma_{\sigma}(1;2)\gamma_{\sigma}(2;1)\>d{\mathbf{r}_{2}}\geq 0\,. \tag{10.11}
$$

The function $D_{\sigma}(1)$ measures the deviation from idempotency of the
correlated 1-RDM and yields the density of effectively-unpaired (odd) electrons
of spin $\sigma$ at point ${\mathbf{r}_{1}}$.[[1339]](../bib_references/bib.md#bib1573)

The formation of effectively-unpaired electrons in singlet systems is therefore
exclusively a correlation based phenomenon. Summing $D_{\sigma}(1)$ over the
spin components gives the total density of odd electrons, and integrating the
latter over space gives the mean total number of odd electrons $\bar{N}_{u}$:

<a id="eq:total-odds"></a>
$$
D_{u}(1)=2\sum_{\sigma}D_{\sigma}(1)d{\mathbf{r}_{1}},\,\,{\bar{N}}_{u}=\int D_{u}(1)d{\mathbf{r}_{1}}\,. \tag{10.12}
$$

The appearance of a factor of 2 in Eq. ([10.12](#eq:total-odds)) above is required
for reasons discussed in Ref. [[1132]](../bib_references/bib.md#bib1172)
. In Kohn-Sham DFT, the
SCF 1-RDM is always idempotent which impedes the analysis of odd electron
formation at that level of the theory. Ref. [[1129]](../bib_references/bib.md#bib1180)
 has
proposed a remedy to this situation. It was noted that the correlated 1-RDM
cross product entering Eq. ([10.11](#eq:non-idempotent1)) reflects an effective
exchange, also known as cumulant exchange.[[135]](../bib_references/bib.md#bib125)
 The KS
exact-exchange hole is itself artificially too delocalized. However, the total
exchange-correlation interaction in a finite system with strong left-right
(*i.e.*, static) correlation is normally fairly localized, largely confined
within a region of roughly atomic size.[[100]](../bib_references/bib.md#bib82)
 The effective exchange
described with the correlated 1-RDM cross product should be fairly localized as
well. With this in mind, the following form of the correlated 1-RDM cross
product was proposed:[[1129]](../bib_references/bib.md#bib1180)

<a id="eq:b05-3"></a>
$$
\gamma_{\sigma}(1;2)\;\gamma_{\sigma}(2;1)=\rho_{\sigma}(1)\;\bar{h}_{\text{X}\sigma\sigma}^{\text{eff}}(1,2)\;. \tag{10.13}
$$

The function $\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}(1;2)$ is a model
DFT exchange hole of Becke-Roussel (BR) form used in Becke’s B05
method.[[101]](../bib_references/bib.md#bib85)
 The latter describes left-right static correlation
effects in terms of certain effective exchange-correlation
hole.[[101]](../bib_references/bib.md#bib85)
 The extra delocalization of the HF exchange hole alone
is compensated by certain physically motivated real-space corrections to
it:[[101]](../bib_references/bib.md#bib85)

<a id="eq:B05-ND-XChole"></a>
$$
\bar{h}_{{\text{XC}}\alpha\alpha}(1,2)=\bar{h}_{{\text{X}}\alpha\alpha}^{\text{eff}}(1,2)+f_{{\mathrm{c}}}(1)\;\bar{h}_{{\text{X}}\beta\beta}^{\text{eff}}(1,2)\;. \tag{10.14}
$$

The BR exchange hole $\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}$
is used in B05 as an auxiliary function,
such that the potential from the relaxed BR hole equals
that of the exact-exchange hole. This results in relaxed
normalization of the auxiliary BR hole less than or equal to unity:

<a id="eq:BR-auxiliary"></a>
$$
\int\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}(1;2)\;d\mathbf{r}_{2}=N_{X\sigma}^{\text{eff}}(1)\;\leq 1\,. \tag{10.15}
$$

The expression of the relaxed normalization $N_{\text{X}\sigma}^{\text{eff}}(\mathbf{r})$ is
quite complicated, but it is possible to represent it in closed analytic
form.[[1131]](../bib_references/bib.md#bib1177)
 The smaller the relaxed normalization
$N_{X\alpha}^{\mathrm{eff}}(1)$, the more delocalized
the corresponding exact-exchange hole.[[101]](../bib_references/bib.md#bib85)
 The $\alpha\!-\!\alpha$
exchange hole is further deepened by a fraction of the $\beta\!-\!\beta$
exchange hole,
$f_{{\mathrm{c}}}(1)\,{\bar{h}}_{{\mathrm{X}}\beta\beta}^{\mathrm{eff}}(1,2)$,
which gives rise to left-right static correlation. The local correlation factor
$f_{\mathrm{c}}$ in Eq.([10.14](#eq:B05-ND-XChole)) governs this deepening and
hence the strength of the static correlation at each point:[[101]](../bib_references/bib.md#bib85)

<a id="eq:f-factor1"></a>
$$
f_{\text{c}}(\mathbf{r})=\min\bigl{(}f_{\alpha}(\mathbf{r}),~{}f_{\beta}(\mathbf{r}),~{}1\bigr{)} \tag{10.16a}
$$

Using Eqs. ([10.16](#eq:f-factor1)), ([10.12](#eq:total-odds)), and ([10.13](#eq:b05-3)),
the density of odd electrons becomes:

<a id="A3.S8.EGx75"></a>
$$
\displaystyle\begin{aligned} \displaystyle D_{\alpha}(1)&\displaystyle=\rho_{\alpha}(1)(1-N_{X\alpha}^{\text{eff}}(1))\\
&\displaystyle=\rho_{\alpha}(1)f_{\mathrm{c}}(1)\,N_{X\beta}^{\text{eff}}(1)\;.\end{aligned} \tag{10.17}
$$

The final formulas for the spin-summed odd electron density and the
total mean number of odd electrons read:

<a id="A3.S8.EGx76"></a>
$$
\displaystyle\begin{aligned} \displaystyle D_{u}(1)&\displaystyle=4a_{\text{nd}}^{\text{op}}\;f_{\text{c}}(1)\left[{\rho}_{\alpha}(1)\,N_{X\beta}^{\mathrm{eff}}(1)+{\rho}_{\beta}(1)\,N_{X\alpha}^{\mathrm{eff}}(1)\right]\\
\displaystyle\bar{N}_{u}&\displaystyle=\int D_{u}(\mathbf{r_{1}})\;d\mathbf{r_{1}}\;.\end{aligned} \tag{10.18}
$$

Here $a_{\text{c}}^{\text{nd-opp}}=0.526$ is the SCF-optimized linear
coefficient of the opposite-spin static correlation energy term of the B05
functional.[[101]](../bib_references/bib.md#bib85)

It is informative to decompose the total mean number of odd electrons into
atomic contributions. Partitioning in real space the mean total number of odd
electrons $\bar{N}_{u}$ as a sum of atomic contributions, we obtain the
atomic population of odd electrons ($F_{A}^{\text{r}}$) as:

<a id="eq:b05-12"></a>
$$
F_{A}^{\mathrm{r}}=\int_{\Omega_{A}}D_{u}(\mathbf{r_{1}})\,d{\mathbf{r}_{1}}\,. \tag{10.19}
$$

Here $\Omega_{A}$ is a subregion assigned to atom
$A$ in the system. To define these atomic regions in a simple way, we use
the partitioning of the grid space into atomic subgroups within Becke’s
grid-integration scheme.[[94]](../bib_references/bib.md#bib73)
 Since the present
method does not require symmetry breaking, singlet states are calculated in
restricted Kohn-Sham (RKS) manner even at strongly stretched bonds. This
way one avoids the destructive effects that the spin contamination has on
$F_{A}^{\text{r}}$ and on the Kohn-Sham orbitals. The calculation of
$F_{A}^{\text{r}}$ can be done fully self-consistently only with the RI-B05
and RI-mB05 functionals. In these cases no special keywords are needed, just
the corresponding choice of EXCHANGE in the *$rem* section. Atomic
population of odd electron can be estimated also with any other functional in
two steps: first obtaining a converged SCF calculation with the chosen
functional, then performing one single post-SCF iteration with RI-B05 or
RI-mB05 functionals reading the guess from a preceding calculation, as shown on
the input example below:

???+ example "Example 10.10.2: To calculate the odd-electron atomic population and the correlated bond order
in stretched H ${}_{2}$ , with B3LYP/RI-mB05, and with fully SCF RI-mB05"
    ```qchem
    $comment
       Stretched H2: example of B3LYP calculation of the atomic population of odd electrons
       with post-SCF RI-BM05 extra iteration.
    $end
    
    $molecule
       0 1
       H   0.  0.   0.0
       H   0.  0.   1.5000
    $end
    
    $rem
       SCF_GUESS         CORE
       METHOD            B3LYP
       BASIS             G3LARGE
       PURECART          222
       THRESH            14
       MAX_SCF_CYCLES    80
       PRINT_INPUT       TRUE
       SCF_FINAL_PRINT   1
       INCDFT            FALSE
       XC_GRID           000128000302
       SCF_CONVERGENCE   9
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $comment
       Now one RI-B05 extra-iteration after B3LYP to generate the odd-electron atomic
       population and the correlated bond order.
    $end
    
    $molecule
       read
    $end
    
    $rem
       SCF_GUESS         READ
       EXCHANGE          BM05
       PURECART          22222
       BASIS             G3LARGE
       AUX_BASIS         riB05-cc-pvtz
       THRESH            14
       PRINT_INPUT       TRUE
       INCDFT            FALSE
       XC_GRID           000128000302
       MAX_SCF_CYCLES    0
       SCF_CONVERGENCE   9
       DFT_CUTOFFS       0
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $comment
       Finally, a fully SCF run RI-B05 using the previous output as a guess.
       The following input lines are obligatory here:
       PURECART     22222
       AUX_BASIS    riB05-cc-pvtz
       DFT_CUTOFFS  0
    $end
    
    $molecule
       read
    $end
    
    $rem
       SCF_GUESS        READ
       EXCHANGE         BM05
       PURECART         22222
       BASIS            G3LARGE
       AUX_BASIS        riB05-cc-pvtz
       THRESH           14
       PRINT_INPUT      TRUE
       INCDFT           FALSE
       IPRINT           3
       XC_GRID          000128000302
       SCF_FINAL_PRINT  1
       MAX_SCF_CYCLES   80
       SCF_CONVERGENCE  8
       DFT_CUTOFFS      0
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    ```

Once the atomic population of odd electrons is obtained, a calculation of the
corresponding correlated bond order of Mayer’s type follows in the code, using
certain exact relationships between $F_{A}^{\mathrm{r}}$, $F_{B}^{\mathrm{r}}$,
and the correlated bond order of Mayer type $B_{AB}$. Both new properties are
printed at the end of the output, right after the multipoles section. It is
useful to compare the correlated bond order with Mayer’s SCF bond order. To
print the latter, use SCF_FINAL_PRINT = 1.
