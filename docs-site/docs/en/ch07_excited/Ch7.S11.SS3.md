---
title: "7.11.3 Second-Order Perturbative Corrections to RAS-CI"
---

## 7.11.3 Second-Order Perturbative Corrections to RAS-CI

(July 4, 2026)

In general, the RAS-CI family of methods within the $hole$ and $particle$
approximation is unable to capture the necessary amounts of dynamic correlation
for the computation of relative energies with chemical accuracy. The missed
correlation can be added on top of the RAS-CI wave function using
multi-reference perturbation theory (MRPT).[[210]](../bib_references/bib.md#bib204)
 The second
order energy correction, *i.e.* RASCI(2), can be expressed as:

<a id="eqRASCI2"></a>

$$
E^{(2)}=-\sum_{k}\frac{|\langle k|\hat{H}|0\rangle|^{2}}{E_{k}-E_{0}+\epsilon} \tag{7.165}
$$

where $0$ indicates the zero-order space and $\{|k\rangle\}$ is the
complementary set of determinants. There is no natural choice for the
$\{E_{k}\}$ excited energies in MRPT, and two different models are available
within the RASCI(2) approach, namely, either Davidson-Kapuy or Epstein-Nesbet
partitioning. As it is common practice in many second-order MRPT corrections,
the denominator energy differences in Eq. ([7.165](#eqRASCI2)) can be level shifted
with a parameter $\epsilon$.
