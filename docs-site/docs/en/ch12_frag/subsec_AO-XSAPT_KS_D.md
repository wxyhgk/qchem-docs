---
title: "12.10.3 Dispersion Models"
---

## 12.10.3 Dispersion Models

(July 4, 2026)

SAPT(KS) calculations and their many-body extension, XSAPT(KS), uses a
Kohn-Sham DFT description of the monomers in order to introduce
*intra*molecular electron correlation in a low-cost way, then described
the *inter*molecular interactions using second-order SAPT. As mentioned
in The resulting interaction energies, however, are not of benchmark quality
even when tuned LRC functionals are employed,[[761]](../bib_references/bib.md#bib794)
 because although
the use of DFT for the monomers often improves the description of hydrogen
bonding (relative to Hartree-Fock-based SAPT0 calculations), the description of
dispersion often deteriorates.[[560]](../bib_references/bib.md#bib574)
 In any case, SAPT0
dispersion is not of benchmark quality anyway, as it suffers from the usual MP2
overestimation of dispersion. At the same time the dispersion and
exchange-dispersion terms are the most expensive parts of a SAPT0 or SAPT(KS)
calculation, with a formal scaling of ${\cal{O}}({N^{4}})$ and ${\cal{O}}({N^{5}})$,
respectively, with respect to system size. Other terms in SAPT0 scale no
worse than ${\cal{O}}({N^{3}})$ and can be computed efficiently for large monomers using
an atomic orbital (AO)-based implementation of the non-dispersion terms in
SAPT.[[764]](../bib_references/bib.md#bib798)

In view of this, both the efficiency and the accuracy of XSAPT(KS) calculations
is improved if second-order dispersion, *i.e.*, $E_{\mathrm{disp}}^{(2)}+E_{\mathrm{exch\mbox{-}disp}}^{(2)}$ in Eqs ([12.61](Ch12.S9.SS1.md#eq:SAPT_interaction)) and
([12.65](Ch12.S9.SS1.md#eq:E(2)_disp)), is replaced by an *ad hoc* atom–atom dispersion
potential of the $-C_{6}/R^{6}-C_{8}/R^{8}-\cdots$ variety. This is reminiscent of
dispersion-corrected DFT or DFT-D, as described in Section [5.7.3](../ch05_dft/subsec_DFT-D.md).
Unlike the situation in DFT, however, the dispersion energy is well-defined and
separable within the SAPT formalism, so it can be replaced by atom–atom
potentials without any fear of double counting of correlation effects, as there
inevitably is in DFT-D. Moreover, in the present case the dispersion
potentials can be fit directly to *ab initio* dispersion energies from
high-level SAPT calculations [SAPT(DFT) and SAPT2+(3)], since the dispersion
contribution is separable. As such, while the dispersion potentials that are
described here are classical in form and do contain fitting parameters, they
can nevertheless reasonably be described as *ab initio* dispersion
potentials. We therefore describe this method as
“+*ai*D”,[[764]](../bib_references/bib.md#bib798)
 to distinguish it from the “+D” dispersion
corrections of DFT-D, although we simply called it “+D” in earlier
work.[[759]](../bib_references/bib.md#bib792)
 The composite method is called
XSAPT(KS)+*ai*D; see Ref. [[760]](../bib_references/bib.md#bib793)
 for an overview and
Ref. [[764]](../bib_references/bib.md#bib798)
 for an efficient implementation in the AO basis.
The latter version exhibits ${\cal{O}}({N^{3}})$ scaling without significant memory
bottlenecks, and is applicable to supramolecular complexes whose monomers
contain $\gtrsim 100$ atoms.[[764]](../bib_references/bib.md#bib798)

To request an XSAPT(KS)+*ai*D calculation, set JOBTYPE =
XSAPT in the *$rem* section to perform XSAPT, with an appropriate
choice of SCF method (Hartree-Fock or DFT). The +*ai*D part of the
algorithm is invoked by two keywords in the *$sapt* input section: first, set
**Algorithm** to **AO** to select the ${\cal{O}}({N^{3}})$ AO-based version of
XSAPT; and second, set **Dispersion** in the *$sapt* section according to one of the
choices that is described below. Available models include pairwise empirical dispersion
(+*ai*D) models,[[759]](../bib_references/bib.md#bib792)

the many-body dispersion (+MBD) potential[[200]](../bib_references/bib.md#bib188)
 and a revised version of it (+MBDrev),[[1406]](../bib_references/bib.md#bib1465)

and “optimized” $C_{6}$-$C_{8}$ MBD models,

 as described below.
Results among these models are very similar for
total interaction energies in small molecules,[[762]](../bib_references/bib.md#bib795)

but different in their performance for large molecules and ions.[[200]](../bib_references/bib.md#bib188)

### `Dispersion`

> **Requests a dispersion potential for use with (X)SAPT. INPUT SECTION: $sapt**
>
> * **Type**: `STRING`
> * **Default**: `aiD3`
> * **Options**:
>     * `aiD`: First-generation empirical pairwise dispersion potential
>     * `aiD2`: Second-generation empirical pairwise dispersion potential
>     * `aiD3`: Third-generation empirical pairwise dispersion potential
>     * `MBD`: Many-body $C_{6}$ and $C_{8}$ dispersion potential
>     * `MBDrev`: Revised MBD dispersion, refit to SAPT10K data
>     * `OC8AIMMBD`: Optimized $C_{6}$ - $C_{8}$
>     * MBD with nonrelativistic free-atom reference data
>     * `OC8RAIMMBD`: Optimized $C_{6}$ - $C_{8}$ MBD, relativistic reference data
>     * `RAIMVDW`: Pairwise atoms-in-molecules dispersion only (no MBD term), relativistic references
> * **Recommendation**: The MBD-based models are generally better than the ai D models, especially for large systems where MBD effects (beyond pairwise additivity) become important. The optimized $C_{6}$ - $C_{8}$ MBD models perform even better for ions and extend MBD to heavy elements via relativistic reference data.

The +*ai*D potentials make a pairwise approximation for dispersion, in which
the interaction potential is assumed to be additive across all pairs of atoms.
The pairwise dispersion approximation employs sums over atom pairs of the form,

<a id="eq:PairwiseDispersion"></a>

$$
E_{\text{disp}}=-\sum_{i\in A}\sum_{\begin{subarray}{c}j\in B\\
A\neq B\end{subarray}}\Bigg{[}f_{6}(R_{ij})\frac{C_{6}^{ij}}{R^{6}_{ij}}+f_{8}(R_{ij})\frac{C_{8}^{ij}}{R^{8}_{ij}}\Bigg{]}\;, \tag{12.68}
$$

where $i$ and $j$ are nuclei in molecules $A$ and $B$, respectively. The original
+*ai*D1 model[[759]](../bib_references/bib.md#bib792)
 was fit to reproduce total interaction energies rather than
being fit directly to *ab initio* dispersion data, and as a consequence
does a much poorer job of reproducing individual energy components and is not recommended.[[760]](../bib_references/bib.md#bib793)

The difference between +*ai*D2[[760]](../bib_references/bib.md#bib793)
 and +*ai*D3[[762]](../bib_references/bib.md#bib795)

is a larger training set for the latter, which was designed to
afford better coverage of $\pi$-stacked systems. As such, the +*ai*D3 correction
is the superior choice out of the pairwise potentials in the +*ai*D suite of methods.
That said, the pairwise approximation for dispersion breaks down in the limit of very large systems because
the interactions between atom pairs are modulated by the local electrodynamic environment
in the molecule.[[764]](../bib_references/bib.md#bib798)

Although a correction to this pairwise approximation has been proposed,[[765]](../bib_references/bib.md#bib799)

based on the difference between XSAPT and SAPT dispersion energies, all of the +*ai*D models are
*ad hoc* and their corrections do not depend on the applied level of theory.
The +MBD potential uses a modified version of the
many-body dispersion potential of Ambrosetti *et al.*[[43]](../bib_references/bib.md#bib27)
 (see Section [5.7.6](../ch05_dft/sect_MBD.md))
in order to account for nonadditive dispersion in a natural way.[[200]](../bib_references/bib.md#bib188)

Because the +MBD method is based on the electron density, it is much more
connected to the *ab initio* method being used.[[199]](../bib_references/bib.md#bib191)

When combined with the XSAPT procedure, the XSAPT+MBD energy decomposition accounts
for nonadditive polarization and dispersion effects. Due to its excellent performance regardless of
system size, the +MBD potential is recommended in most cases.
To improve the transferability and accuracy of dispersion interactions across diverse chemical environments, the four parameters contained in the
MBD model have been re-optimized against the comprehensive SAPT10K benchmark
data set of SAPT2+(3)(CCD)/aug-cc-pVTZ dispersion energies.[[1406]](../bib_references/bib.md#bib1465)

The resulting revised model, denoted MBDrev, is used in conjunction with (X)SAPT for non-dispersion contributions and delivers systematically improved performance relative to the original (X)SAPT+MBD approach, including for chemically realistic systems comprising hundreds of atoms.[[767]](../bib_references/bib.md#bib800)

However, the Hirshfeld partition that is inherent to MBD-based dispersion models is ill-defined for ions, for which MBD sometimes gives poor
results,[[557]](../bib_references/bib.md#bib588) even relative to +*ai*D3.[[481]](../bib_references/bib.md#bib492)

For this reason, an optimized family of atoms-in-molecules dispersion models is also available, in
which the per-atom response properties $(\alpha_{0}$, $C_{6}$, and $R_{\mathrm{vdW}})$ are obtained
by Tkatchenko–Scheffler scaling of free-atom reference data,[[1361]](../bib_references/bib.md#bib1421)

using an iterative version of Hirshfeld volume partition that is better behaved for ions.

As in the original (X)SAPT+MBD approach,[[200]](../bib_references/bib.md#bib188)

these models combine both $C_{6}/R^{6}$ and $C_{8}/R^{8}$ dispersion terms, with the former computed using the
Drude oscillator Hamiltonian of Tkatchenko’s MBD model.[[43]](../bib_references/bib.md#bib27)

However, this new “optimized” approach

 uses
$C_{8}$ parameters that are obtained in an optimal way from the Drude oscillator
invariants from the $C_{6}$ MBD calculation.[[464]](../bib_references/bib.md#bib477)

This new family of models for (X)SAPT is collectively called “oC8aimMBD” (optimized atoms-in-molecules MBD),

and there are three variants that differ only in their free-atom reference data, as indicated in the description of the
**Dispersion** keyword above. The oC8aimMBD approach uses non-relativistic Hartree–Fock reference data for the free atoms,
whereas oC8(r)aimMBD uses four-component Dirac–Hartree–Fock
references in uncontracted Dyall basis sets, and is recommended whenever elements with $Z>36$ are present.

Finally, the (r)aimVDW model retains only the pairwise $C_{6}/R^{6}$ correction, dropping the many-body term.

The per-fragment Hirshfeld evaluation is enabled automatically; set
**print** to 3 in the *$xpol* section reports the per-atom Hirshfeld volume
ratios used to scale the dispersion parameters.

As with XPol, the XSAPT and XSAPT(KS)+*ai*D methods do not function with
external changes. Only single-point energies are
available, and frozen orbitals orbitals are not allowed. Both restricted and
unrestricted versions are available. Researchers who use XSAPT(KS)+*ai*D
are asked to cite Ref. [[759]](../bib_references/bib.md#bib792)
 for +*ai*D1,
Ref. [[760]](../bib_references/bib.md#bib793)
 for +*ai*D2, Ref. [[762]](../bib_references/bib.md#bib795)
 for
+*ai*D3, Ref. [[200]](../bib_references/bib.md#bib188)
 for +MBD, Ref. [[1406]](../bib_references/bib.md#bib1465)
 for +MBDrev, and
Ref. 

 for the optimized aimMBD models. All of these are based on the AO-based version of XSAPT that was
introduced in Ref. [[764]](../bib_references/bib.md#bib798)
.
