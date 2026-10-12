---
title: "7.3.1 Brief Introduction"
---

## 7.3.1 Brief Introduction

(July 4, 2026)

Excited states may be obtained from density functional theory via linear
response,[[351]](../bib_references/bib.md#bib357)

which for historical reasons is known as “time-dependent”
(TD-)DFT.

 This should not be confused with
the explicitly time-dependent methods that are discussed in Section [7.4](sec_TDKS.md),
however linear-response DFT is nearly universally
called TDDFT and we shall use that nomenclature as well. This approach calculates poles
in the response of the ground state density to a time-varying applied electric
field. These poles are Bohr frequencies, or in other words the excitation
energies. Operationally, this involves solution of an eigenvalue equation

<a id="eq:TDDFT"></a>

$$
\left(\begin{array}[]{cc}\mathbf{A}&\mathbf{B}\\
\mathbf{B}^{\dagger}&\mathbf{A}^{\dagger}\\
\end{array}\right)\left(\begin{array}[]{c}\mathbf{x}\\
\mathbf{y}\end{array}\right)=\omega\left(\begin{array}[]{cc}\mathbf{-1}&\mathbf{0}\\
\mathbf{0}&\mathbf{1}\\
\end{array}\right)\left(\begin{array}[]{c}\mathbf{x}\\
\mathbf{y}\end{array}\right) \tag{7.15}
$$

where the elements of the matrix $\mathbf{A}$ similar to those used at the CIS
level, Eq. ([7.11](subsec_CIS.md#eq:orbital-Hessian)), but with an exchange-correlation
correction.

 Elements of $\mathbf{B}$ are similar.
Equation ([7.15](#eq:TDDFT)) is solved iteratively for the lowest few excitation
energies, $\omega$. Alternatively, one can make a Tamm-Dancoff
approximation (TDA) in which the “de-excitation”
amplitudes $\mathbf{Y}$ are neglected.[[580]](../bib_references/bib.md#bib602)

In that case, the $\mathbf{B}$ matrix is not required and
Eq. ([7.15](#eq:TDDFT)) reduces to a CIS-like equation $\mathbf{Ax}=\omega\mathbf{x}$.

TDDFT is popular because its computational cost is roughly similar to that of
the simple CIS method, but a description of differential electron correlation
effects is implicit in the method. It is advisable to only employ TDDFT for
low-lying valence excited states that are below the first ionization potential
of the molecule,

 or more conservatively, below the first
Rydberg state, and in such cases the valence excitation energies are often
remarkably improved relative to CIS, with an accuracy of $\sim 0.3$ eV for many
functionals.[[770]](../bib_references/bib.md#bib803)
 The calculation of the nuclear gradients of
full TDDFT and within the TDA is implemented.[[838]](../bib_references/bib.md#bib872)

Standard TDDFT also does not yield a good description of static correlation
effects (see Section [6.14](../ch06_correlation/sect_ccactive.md)), because it is based on a single
reference configuration of Kohn-Sham orbitals. A variant called spin-flip (SF)
TDDFT has been developed to address this issue.[[1239]](../bib_references/bib.md#bib1294)

SF-TDDFT is different from standard TDDFT in two ways:

- The reference is a high-spin triplet (quartet) for a system with an even
(odd) number of electrons;
- One electron is spin-flipped from an $\alpha$ Kohn–Sham orbital to a $\beta$
orbital during the excitation.

SF-TDDFT can describe the ground state as well as a few low-lying excited states,
and has been applied to bond-breaking processes, and di- and tri-radicals with
degenerate or near-degenerate frontier orbitals.
Different flavors of SF-DFT are described in Section [7.3.4](sect_sftddft.md).
