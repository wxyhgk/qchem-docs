---
title: "4.7.4 Basis-Set Pairings"
---

## 4.7.4 Basis-Set Pairings

(July 4, 2026)

We recommend using basis pairings in which the small basis set is a proper
subset of the target basis (6-31G into 6-31G*, for example). They not only
produce more accurate results; they also lead to more efficient integral
screening in both energies and gradients. Subsets for many standard basis sets
(including Dunning-style cc-pV$X$Z basis sets and their augmented analogs) have
been developed and thoroughly tested for these purposes. A summary of the
pairings is provided in Table [4.2](#tab:DBsummary); details of these truncations
are provided in Figure [4.1](#fig:DBfig).

A new pairing for 6-31G*-type calculations is also available. The 6-4G subset
(named r64G in **Q-Chem**) is a subset by *primitive* functions and provides
a smaller, faster alternative for this basis set regime.[[1302]](../bib_references/bib.md#bib1357)
 A
case-dependent switch in the projection code (still OVPROJECTION)
properly handles 6-4G. For DB-HF, the calculations proceed as described above.
For DB-DFT, empirical scaling factors (see Ref. [[1302]](../bib_references/bib.md#bib1357)
 for
details) are applied to the dual-basis correction. This scaling is handled
automatically by the code and prints accordingly.

As of **Q-Chem** version 3.2, the basis set projection code has also been adapted
to properly account for linear dependence,[[1299]](../bib_references/bib.md#bib1358)
 which can often be
problematic for large, augmented (aug-cc-pVTZ, *etc.*) basis set calculations.
The same standard keyword (LIN_DEP_THRESH) is used to determine
linear dependence in the projection code. Because of the scheme used to
account for linear dependence, only proper-subset pairings are now allowed.

Like single-basis calculations, user-specified general or mixed basis sets may
be employed (see Chapter [8](../ch08_basis/chap_basis.md)) with dual-basis calculations. The
target basis specification occurs in the standard *$basis* section. The
smaller, secondary basis is placed in a similar *$basis*2 section; the syntax
within this section is the same as the syntax for *$basis*. General and mixed
small basis sets are activated by BASIS2 = BASIS2_GEN and
BASIS2 = BASIS2_MIXED, respectively.

| BASIS | BASIS2 |
| --- | --- |
| cc-pVTZ | rcc-pVTZ |
| cc-pVQZ | rcc-pVQZ |
| aug-cc-pVDZ | racc-pVDZ |
| aug-cc-pVTZ | racc-pVTZ |
| aug-cc-pVQZ | racc-pVQZ |
| 6-31G* | r64G, 6-31G |
| 6-31G** | r64G, 6-31G |
| 6-31++G** | 6-31G* |
| 6-311++G(3df,3pd) | 6-311G*, 6-311+G* |

Table 4.2: Summary and nomenclature of recommended dual-basis pairings

<a id="Ch4.Ex5"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&-\\
&-\\
s\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d\\
&p\\
s\\
\end{array}\\
&$cc-pVTZ$&$rcc-pVTZ$&&$cc-pVTZ$&$rcc-pVTZ$\\
\end{array}\\
$$

<a id="Ch4.Ex6"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&-\\
s&&-\\
&p&&-\\
s&&-\\
&-\\
s\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d&&g\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&d\\
&p\\
s\\
\end{array}\\
&$cc-pVQZ$&$rcc-pVQZ$&&$cc-pVQZ$&$rcc-pVQZ$\\
\end{array}\\
$$

<a id="Ch4.Ex7"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&\\
&p\\
s^{\prime}&\\
\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&\\
&-\\
s^{\prime}&\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVDZ$&$racc-pVDZ$&&$aug-cc-pVDZ$&$racc-pVDZ$\\
\end{array}\\
$$

<a id="Ch4.Ex8"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&-\\
&p\\
s&&-\\
&-\\
s^{\prime}\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d\\
&p&&-\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVTZ$&$racc-pVTZ$&&$aug-cc-pVTZ$&$racc-pVTZ$\\
\end{array}\\
$$

<a id="Ch4.Ex9"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&-\\
&p&&-\\
s&&-\\
&p&&-\\
s&&-\\
&-\\
s^{\prime}\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d&&g\\
&p&&f\\
s&&d&&g^{\prime}\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVQZ$&$racc-pVQZ$&&$aug-cc-pVQZ$&$racc-pVQZ$\\
\end{array}
$$

Figure 4.1: Structure of the truncated basis set pairings for cc-pV(T,Q)Z and
aug-cc-pV(D,T,Q)Z. The most compact functions are listed at the top. Primed
functions depict diffuse function augmentation. Dashes indicate eliminated
functions, relative to the paired standard basis set. In each case, the
truncations for hydrogen and heavy atoms are shown, along with the nomenclature
used in **Q-Chem**.
