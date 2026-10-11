---
title: "7.9.8 EOM-DEA-CCSD"
---

## 7.9.8 EOM-DEA-CCSD

(July 4, 2026)

In the EOM-DEA method, the target states are described by
$2p$ and $1h3p$ operators acting on $N-2$ electron reference[[1077]](../bib_references/bib.md#bib1122)
:

<a id="DEA:WF"></a>

$$
\Psi_{k}=\hat{R}_{N+2}\Psi_{0}(N-2), \tag{7.102}
$$

and the excitation operator $R$ has the following form:

<a id="eq:R-DEA"></a>

$$
\hat{R}=\frac{1}{2}\sum_{ab}r_{ab}a^{\dagger}b^{\dagger}+\frac{1}{6}\sum_{iabc}r_{i}^{abc}a^{\dagger}b^{\dagger}c^{\dagger}i. \tag{7.103}
$$

EOM-DEA is useful for calculating diradical states including excited states beyond the SF manifold.
In calculations of neutral diradicals, EOM-DEA should use +2 charged reference state. EOM-DEA
is also suitable for describing certain types of doubly excited states, such as $\ldots(\pi)^{0}(\pi^{*})^{2}$ in ethylene.
An EOM-DEA calculation is invoked by using DEA_STATES, or DEA_SINGLETS and DEA_TRIPLETS.
In more exotic calculations, such as EOM-DEA for open-shell references, DEA_AA_STATES, DEA_BB_STATES,
and DEA_AB_STATES keywords might be useful. Both EOM-CCSD and EOM-MP2 variants are available.

**Note: 

In some applications of EOM-DEA-CCSD, only
2$p$ operators were included in the EOM part. These calculations
correspond to energies obtained from EOM_PRECONV_DOUBLES = TRUE calculation.
**
