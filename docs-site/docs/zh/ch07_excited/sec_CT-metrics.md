---
title: "7.3.2 Charge-Transfer Metrics"
---

## 7.3.2 Charge-Transfer Metrics

(July 4, 2026)

Standard density functionals do not yield a potential with
the correct long-range Coulomb tail, owing to the self-interaction problem.
Therefore, excitation energies corresponding to states that sample
this tail (*e.g.*, diffuse Rydberg states and some charge transfer excited
states) are not given accurately.[[213]](../bib_references/bib.md#bib210)

The extent to which a particular excited state is characterized by charge transfer
can be assessed using an a spatial overlap metric, $\Lambda$,
defined as[[1057]](../bib_references/bib.md#bib1102)

<a id="eq:Tozer-metric"></a>
$$
\Lambda=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}O_{ia}}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.16}
$$

where $O_{ia}$ is the spatial overlap of occupied MO $\psi_{i}$ with virtual MO $\psi_{a}$:

<a id="eq:Tozer-overlaps"></a>
$$
O_{ia}=\int|\psi_{i}(\mathbf{r})|\cdot|\psi_{a}(\mathbf{r})|\;d\mathbf{r}\;. \tag{7.17}
$$

The absolute value signs are necessary since the occupied and virtual MOs are
orthogonal, $\langle\psi_{i}|\psi_{a}\rangle$, although **Q-Chem** includes the option to use squares of the MOs instead:

<a id="eq:Tozer-overlaps2"></a>
$$
\tilde{O}_{ia}=\int|\psi_{i}(\mathbf{r})|^{2}|\psi_{a}(\mathbf{r})|^{2}\;d\mathbf{r}\;. \tag{7.18}
$$

In that case, $\tilde{O}_{ia}$ is used in place of $O_{ia}$ in Eq. ([7.16](#eq:Tozer-metric)).
For the original version of the metric (using $O_{ia}$, and where $\psi_{i}$ and $\psi_{a}$ are canonical MOs),
Tozer and coworkers find that $0.45\leq\Lambda\leq 0.89$ for localized valence
excitations whereas Rydberg excitations lie in the range
$0.08\leq\Lambda\leq 0.27$.[[1057]](../bib_references/bib.md#bib1102)

Furthermore, they suggest functional-specific cutoffs for when a particular excitation may have
too much charge-transfer character for TDDFT results to be trusted.
Note that while **Q-Chem** implements the definition
in Eq. ([7.16](#eq:Tozer-metric)) that was proposed in Ref. [[1057]](../bib_references/bib.md#bib1102)
, the normalizing
denominator in this expression is inconsistent for full TDDFT calculations
(*i.e.*, those not invoking the TDA),[[563]](../bib_references/bib.md#bib587)
 for which the normalization condition
on $\mathbf{x}$ and $\mathbf{y}$ is $\sum_{ia}(x_{ia}^{2}-y_{ia}^{2})=1$ rather than
$\sum_{ia}(x_{ia}^{2}+y_{ia}^{2})=1$.

Empirically, the $\Lambda$ metric provides very good correlations with TDDFT errors,[[1057]](../bib_references/bib.md#bib1102)

yet its numerical value is difficult to interpret in terms of a physical charge separation. For that reason, a similar metric

<a id="eq:Delta-r"></a>
$$
\Delta r=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}\|\mathbf{R}_{ia}\|}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.19}
$$

was proposed,[[503]](../bib_references/bib.md#bib515)
 where

<a id="Ch7.E20"></a>
$$
\mathbf{R}_{ia}=\langle\psi_{i}|\hat{\mathbf{r}}|\psi_{i}\rangle-\langle\psi_{a}|\hat{\mathbf{r}}|\psi_{i}\rangle \tag{7.20}
$$

is the vector displacement between the centroids of orbitals $\psi_{i}$ and $\psi_{a}$, and $\|\mathbf{R}_{ia}\|$ in
Eq. ([7.19](#eq:Delta-r)) is the distance between their centroids. This makes $\Delta r$ an incoherent average of
electron displacements ($\psi_{i}\to\psi_{a}$), which has consequences for states where a coherent superposition of
displacements is qualitatively important.[[563]](../bib_references/bib.md#bib587)
 Because $\Delta r$ vanishes for any centrosymmetric
molecule, it was later augmented by a quantity

<a id="eq:Delta-sigma"></a>
$$
\Delta\sigma=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}\sigma_{ia}}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.21}
$$

where

<a id="Ch7.E22"></a>
$$
\sigma_{ia}=\bigl{|}\langle\psi_{i}|\hat{r}^{2}|\psi_{i}\rangle-\langle\psi_{a}|\hat{r}^{2}|\psi_{a}\rangle\big{|}^{1/2}\;, \tag{7.22}
$$

where $\langle\psi_{r}|\hat{r}^{2}|\psi_{r}\rangle$ is the second moment of orbital $\psi_{r}$.
The quantity $\sigma_{ia}$ provides a measure of the change in orbital size between donor ($\psi_{i}$) and acceptor ($\psi_{a}$) MOs,
and a metric

<a id="Ch7.E23"></a>
$$
\Gamma=\Delta r+\Delta\sigma \tag{7.23}
$$

was proposed to measure charge-transfer character for TDDFT excitations.[[502]](../bib_references/bib.md#bib516)

It was suggested that a “trust radius” based on $\Gamma$, which has dimensions of length, could be used to replace Tozer’s
critical values of $\Lambda$ as a detector of problematic charge-transfer transitions.[[502]](../bib_references/bib.md#bib516)

A major shortcoming, however, is that none of these metrics ($\Lambda$, $\Delta r$, $\Delta\sigma$, or $\Gamma$) is invariant
to unity transformation of the MOs.[[563]](../bib_references/bib.md#bib587)
 As such, their numerical values can depend quite strongly on which orbitals
$\{\psi_{i}\}$ and $\{\psi_{a}\}$ are used. In their original formulations, it was assumed that these would be canonical MOs, although it
was subsequently noticed that values of $\Gamma$ for Rydberg transitions were somewhat erratic but more stable (especially with
regard to changes in basis set) when natural transition orbitals (NTOs, Section [7.13.3](sect_NTOs.md)) were used instead.[[502]](../bib_references/bib.md#bib516)

An explanation was provided later.[[563]](../bib_references/bib.md#bib587)
 When the transition in question is dominated by a single occupied/virtual
pair of NTOs (as is often the case, although counterexamples are also easy to find),[[572]](../bib_references/bib.md#bib586)
 then $\Delta r$
and $\Gamma$ approximate expectation values with respect to an excitonic wave function, and any proper expectation value must be
invariant to unitary transformations of the occupied MOs and, separately, the virtual MOs.[[563]](../bib_references/bib.md#bib587)
 For this reason, if these
metrics are going to be used then it is recommended that they be evaluated in the NTO basis rather than the canonical MO basis; **Q-Chem**
can provide both values, for each of $\Lambda$, $\Delta r$, $\Delta\sigma$, and $\Gamma$.

Although the NTO representation affords better stability with respect to changes in basis set (especially, with regard to addition of
diffuse functions),[[563]](../bib_references/bib.md#bib587)
 it remains the case that each of these metrics is formulated as an incoherent, amplitude-weighted
average of $\psi_{i}\to\psi_{a}$ excitations. In a proper expectation value, the excitation amplitudes have a coherent phase relationship, as in
the CIS wave function in Eq. ([7.10](subsec_CIS.md#eq:CIS-wavefn)). It is possible to find examples where the $\Gamma$ metric provides a very misleading
measure of charge separation, because several individual $\psi_{i}\to\psi_{a}$ excitations are associated with large values of $\|\mathbf{R}_{ia}\|$,
yet they interfere destructively such that the net result hardly displaces any charge at all.[[563]](../bib_references/bib.md#bib587)

Thus, while the metrics $\Lambda$, $\Delta r$, and $\Gamma$ (in both the canonical and NTO representations) are included in order to help users
make contact with existing literature, it is recommended that charge-transfer analysis be based on proper expectation values with respect
to transition density matrices. These can be computed using the **libwfa** module that is described in Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md).
As documented in Table [10.1](../ch10_properties/ex_StateAnal_MolDen.md#table:TDM-analysis) of that section, **libwfa** can compute expectation values such as

<a id="Ch7.E24"></a>
$$
d_{\text{e-h}}=\|\langle\mathbf{r}_{\text{elec}}-\mathbf{r}_{\text{hole}}\rangle\|\;, \tag{7.24}
$$

or in other words the expectation value of the distance between the centroid of the excited electron and that of the hole. This constitutes a
proper measure of electron–hole separation.[[563]](../bib_references/bib.md#bib587)
 Exciton size can be measured via

<a id="Ch7.E25"></a>
$$
d_{\text{exc}}=\langle\|\mathbf{r}_{\text{elec}}-\mathbf{r}_{\text{hole}}\|^{2}\rangle^{1/2}\;, \tag{7.25}
$$

which is also available from **libwfa**. Charge-displacement metrics[[572]](../bib_references/bib.md#bib586)

can also be computed using **libwfa**. These include

<a id="Ch7.E26"></a>
$$
\displaystyle d_{\text{CD1}} \tag{7.26a}
$$

where $\sigma_{\text{elec}}$ and $\sigma_{\text{hole}}$ are
the root-mean-square size of the excited electron and the hole, respectively.
See Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) for a discussion of other metrics computed by **libwfa**.
