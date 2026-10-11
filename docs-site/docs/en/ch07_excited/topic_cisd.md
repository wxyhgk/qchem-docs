---
title: "7.8.2 CIS(D) Theory"
---

## 7.8.2 CIS(D) Theory

(July 4, 2026)

The CIS(D) excited state procedure is a second-order perturbative
approximation to the computationally expensive CCSD, based on a single
excitation configuration interaction (CIS) reference. The coupled-cluster
wave function, truncated at single and double excitations, is the exponential of
the single and double substitution operators acting on the Hartree-Fock
determinant:

<a id="eq614"></a>

$$
\left|\Psi\right\rangle=\exp\left({T_{1}+T_{2}}\right)\left|{\Psi_{0}}\right\rangle \tag{7.82}
$$

Determination of the singles and doubles amplitudes requires solving the two
equations

<a id="eq615"></a>

$$
\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({1+T_{1}+T_{2}+\frac{1}{2}T_{1}^{2}+T_{1}T_{2}+\frac{1}{3!}T_{1}^{3}}\right)\Psi_{0}}\right\rangle=0 \tag{7.83}
$$

and

<a id="eq616"></a>

$$
\left\langle{\Psi_{ij}^{ab}}\right|H-E\left|{\left({1+T_{1}+T_{2}+\frac{1}{2}T_{1}^{2}+T_{1}T_{2}+\frac{1}{3!}T_{1}^{3}+\frac{1}{2}T_{2}^{2}+\frac{1}{2}T_{1}^{2}T_{2}+\frac{1}{4!}T_{1}^{4}}\right)\Psi_{0}}\right\rangle=0 \tag{7.84}
$$

which lead to the CCSD excited state equations. These can be written

<a id="eq617"></a>

$$
\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({U_{1}+U_{2}+T_{1}U_{1}+T_{1}U_{2}+U_{1}T_{2}+\frac{1}{2}T_{1}^{2}U_{1}}\right)\Psi_{0}}\right\rangle=\omega b_{i}^{a} \tag{7.85}
$$

and

<a id="eq618"></a>

$$
\begin{array}[]{r}\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({U_{1}+U_{2}+T_{1}U_{1}+T_{1}U_{2}+U_{1}T_{2}+\frac{1}{2}T_{1}^{2}U_{1}}\right.}\right.+T_{2}U_{2}\\
\left.{+\frac{1}{2}T_{1}^{2}U_{2}+T_{1}T_{2}U_{1}+\frac{1}{3!}T_{1}^{3}U_{1}}\right|\left.{\Psi_{0}}\right\rangle=\omega b_{ij}^{ab}\\
\end{array} \tag{7.86}
$$

This is an eigenvalue equation $\mathbf{A}\mathbf{b}=\omega\mathbf{b}$ for the transition
amplitudes ($\mathbf{b}$ vectors), which are also contained in the $U$ operators.

The second-order approximation to the CCSD eigenvalue equation yields a
second-order contribution to the excitation energy which can be written in the form

<a id="eq619"></a>

$$
\omega^{(2)}=\mathbf{b}^{(0)^{\mathbf{t}}}{\rm{\bf A}}^{(1)}\mathbf{b}^{(1)}+\mathbf{b}^{(0)^{\mathbf{t}}}{\rm{\bf A}}^{(2)}\mathbf{b}^{(0)} \tag{7.87}
$$

or in the alternative form

<a id="eq620"></a>

$$
\omega^{(2)}=\omega^{\mathrm{CIS(D)}}=E^{\mathrm{CIS(D)}}-E^{\mathrm{MP2}} \tag{7.88}
$$

where

<a id="eq621"></a>

$$
E^{\mathrm{CIS(D)}}=\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{U_{2}\Psi^{\mathrm{HF}}}\right\rangle+\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{T_{2}U_{1}\Psi^{\mathrm{{HF}}}}\right\rangle \tag{7.89}
$$

and

<a id="eq622"></a>

$$
E^{\mathrm{MP2}}=\left\langle{\Psi^{\mathrm{HF}}}\right|V\left|{T_{2}\Psi^{\mathrm{HF}}}\right\rangle \tag{7.90}
$$

The output of a CIS(D) calculation contains useful information beyond the
CIS(D) corrected excitation energies themselves. The stability of the CIS(D)
energies is tested by evaluating a diagnostic, termed the “theta
diagnostic”.[[1031]](../bib_references/bib.md#bib1074)
 The theta diagnostic calculates a mixing angle
that measures the extent to which electron correlation causes each pair of
calculated CIS states to couple. Clearly the most extreme case would be a
mixing angle of $45^{\circ}$, which would indicate breakdown of the validity of
the initial CIS states and any subsequent corrections. On the other hand, small
mixing angles on the order of only a degree or so are an indication that the
calculated results are reliable. The code can report the largest mixing angle
for each state to all others that have been calculated.
