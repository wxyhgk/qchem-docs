---
title: "7.6.3 One-Center NOCIS (1C-NOCIS)"
---

## 7.6.3 One-Center NOCIS (1C-NOCIS)

(July 4, 2026)

## 7.6.3.1 One-electron M${}_{S}$ = 1/2 doublet and two-electron M${}_{S}$ = 1 triplet references

There is also another approximate method, one-center NOCIS (1C-NOCIS),[[1023]](../bib_references/bib.md#bib1068)

which is an intermediate between NOCIS and STEX. The open-shell determinants are separately optimized as in NOCIS, but the coupling between non-orthogonal determinants with core holes on different centers is ignored, and NOCI is used to compute the remaining matrix elements between non-orthogonal determinants. 1C-NOCIS constructs the orthogonal Slater-Condon components of the matrices, and then performs NOCI to obtain the relevant non-orthogonal components. The diagonal blocks are then projected against the ground state. For closed-shell singlet NOCIS, 1C-NOCIS is the same as STEX, since there are no open-shell ground-state orbitals.

There are two main advantages of 1C-NOCIS. First, it is substantially cheaper to evaluate than NOCIS and so enables the treatment of larger molecules. Second, and in contrast to STEX, it allows the open-shell states to relax separately, which may have a substantial impact on accuracy.

## 7.6.3.2 Two-electron M${}_{S}$ = 0 singlet and triplet references

Inspired by the 1C-NOCIS model, a theory for core excited states out of an M${}_{S}$ = 0, two-electron open-shell (2eOS)
reference state (either singlet or triplet) was developed.[[51]](../bib_references/bib.md#bib34)
 This theory is appropriate for
experiments involving an ultrafast UV pump followed by a XUV or x-ray probe, for example. For a 2eOS
state describable by a single NTO pair, where an electron in occupied orbital $o$ is promoted into a target virtual orbital $t$, the excited-state wave function takes the form

<a id="Ch7.E74"></a>

$$
\big{|}^{1,\;3}\Psi_{i}\big{\rangle}=(2)^{1/2}\left(\big{|}\Phi_{o}^{t}\big{\rangle}\pm\big{|}\Phi_{\bar{o}}^{\bar{t}}\big{\rangle}\right) \tag{7.74}
$$

where the plus corresponds to the singlet and the minus to the triplet. Subsequently promoting a core electron $c$ into an arbitrary particle level $y$, while remaining within the M${}_{s}$ = 0 manifold, results in eight possible configurations

<a id="Ch7.E75"></a>

$$
\big{|}\Phi_{oc}^{to}\big{\rangle},\;\big{|}\Phi_{\bar{o}\bar{c}}^{\bar{t}\bar{o}}\big{\rangle},\;\big{|}\Phi_{oc}^{ty}\big{\rangle},\;\big{|}\Phi_{\bar{o}\bar{c}}^{\bar{t}\bar{y}}\big{\rangle},\;\big{|}\Phi_{\bar{o}c}^{\bar{t}y}\big{\rangle},\;\big{|}\Phi_{o\bar{c}}^{t\bar{y}}\big{\rangle},\;\big{|}\Phi_{\bar{o}c}^{\bar{y}t}\big{\rangle},\;\big{|}\Phi_{o\bar{c}}^{y\bar{t}}\big{\rangle} \tag{7.75}
$$

Diagonalizing the S${}^{2}$ operator within the span of these configurations results in several possible configuration state fuctions (CSFs). A special one is the 2eOS singlet or triplet CSFs associated with the re-pairing of the core electron $c$ with the electron in the singly-occupied molecular orbital (SOMO) that was formerly fully-occupied in the closed-shell state, $o$.

<a id="Ch7.E76"></a>

$$
\big{|}^{1,\;3}\Phi_{o}^{t}\big{\rangle}=(2)^{-1/2}\left(\big{|}\Phi_{c}^{t}\big{\rangle}\pm\big{|}\Phi_{\bar{c}}^{\bar{t}}\big{\rangle}\right) \tag{7.76}
$$

When the core electron is promoted to an arbitrary virtual orbital (with respect to the closed-shell configuration), the states can be described by the remaining 4eOS singlet, triplet, and quintet CSFs.

<a id="Ch7.E77"></a>

$$
\displaystyle\big{|}^{1_{A}}\Phi_{oc}^{ty}\big{\rangle} \tag{7.77a}
$$

Note that the special 2eOS CSF associated with repairing of the core electron with the particle SOMO $t$ are included in the 4eOS CSFs presented above as the cases when $y=t$. As per the original 1C-NOCIS and STEX methods, the variant for M${}_{S}$ = 0 2eOS references diagonalizes the Hamiltonian in the subspan of all the aforementioned CSFs. In deviation with the original doublet and triplet 1C-NOCIS implementation, however, the 2eOS variant offers three possible sets of reference orbitals:

- •

The 1eOS, M${}_{S}$ = 1/2 doublet core ion orbitals, with the virtual space rotated into the NTO basis of a standard closed-shell STEX calculation
- •

The 2eOS, M${}_{S}$ = 0 ROKS-optimized orbitals for the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ configuration
- •

The 3eOS, M${}_{S}$ = 3/2 quartet core ion ROHF-optimized orbitals for the $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ configuration

Crucially, all of these references incorporate relaxation due to the presence of the core hole and hope to provide a well-defined particle state $t$. Since the STEX and 1C-NOCIS models are, in essence, a truncated CI formalism for open-shell systems, the final excited states constructed are sensitive to the underlying choice of orbitals.[[712]](../bib_references/bib.md#bib744)
 By virtue of being occupied in all the CSFs employed to describe the pump-probe states, the quality of the normally-empty $t$ orbital is essential. For the moment, we recommend using the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ orbitals when targeting singlet states and $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ orbitals when targeting triplet states.

The valence-excited state orbitals are used as a guess for the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS or $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ ROHF optimization. Alternatively, the code can use the 1eOS, M${}_{S}$ = 1/2 doublet core ion orbitals as a guess. Since HF provides virtual orbitals of poor quality, the doublet core ion calculation can be performed with DFT to provide a better guess for the subsequent calculation. The DFT method is specified with the ENV_METHOD rem variable.

The 1C-NOCIS 2eOS implementation is more flexible than the original 1C-NOCIS implementation for doublets and triplets. It allows to target arbitrary M${}_{S}$ = 0 singlet or triplet states obtained via CIS or ROKS and allows for control of the underlying calculations of the initial state and the SCF optimizations for the reference orbitals. Correspondingly, there is a larger number of $ rem variables available exclusively for 1C-NOCIS calculations for 2eOS references.
