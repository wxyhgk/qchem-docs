---
title: "7.10.8 Spin-Flip ADC Methods"
---

## 7.10.8 Spin-Flip ADC Methods

(July 4, 2026)

The spin-flip (SF) method[[726]](../bib_references/bib.md#bib757)

is used for molecular systems with few-reference wave functions like diradicals,
bond-breaking, rotations around single bonds, and conical intersections.
Starting from a triplet ($m_{s}=1$) ground state reference a spin-flip excitation
operator $\{\hat{C}_{J}\}=\{c_{a\beta}^{\dagger}c_{i\alpha};$
$\hskip 2.845276ptc_{a\beta}^{\dagger}c_{b\sigma}^{\dagger}c_{i\alpha}c_{j\sigma},$
$\hskip 7.113189pt\text{a \textless~{} b, i \textless~{} j}\}$ is introduced,
which flipped the spin of one electron while singlet and
($m_{s}=0$) triplet excited target states are yielded. The spin-flip method
is implemented for the ADC(2) (strict and extended) and the ADC(3)
methods.[[796]](../bib_references/bib.md#bib830)
 Note that high-spin ($m_{s}=1$) triplet states
can be calculated with the SF-ADC method as well using a closed-shell singlet
reference state. The number of spin-flip states that shall be calculated
is controlled with the *$rem* variable SF_STATES.
