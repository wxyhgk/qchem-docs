---
title: "6.9.1 Introduction"
---

## 6.9.1 Introduction

(July 4, 2026)

Maximum Physical Regularisaion can be understood both as an extension to
size-consistent Brillouin-Wigner theory (BW-s2) as well as to Møller-Plesset
perturbation theory (MP2). In either framework, it introduces additional terms
into the unperturbed Hamiltonian which allow the user to manipulate ground state
properties and energies with more parametric precision. The second order energy
in MPR-BWs(2) is given by an equation superficially reminiscient of both
MP2 and BW-s2:

<a id="Ch6.E39"></a>

$$
E_{\text{c}}^{(2)}=\frac{1}{4}\sum\limits_{ijab}\langle ab||ij\rangle{t^{ab}_{ij}}^{(1)} \tag{6.39}
$$

where the first order amplitudes ${t^{ab}_{ij}}^{(1)}$ are determined by their
linear amplitude equation. In strong analogy to BW-s2, MPR-BWs2 contains two
matrices $W_{ij}$ and $W_{ab}$ which augment and mould the phyiscal description
of the unperturbed ground state. The MPR-BWs2 amplitude equation is given by:

<a id="Ch6.E40"></a>

$$
\sum\limits_{c}\big{(}(f_{ac}+W_{ac}){t^{cb}_{ij}}^{(1)}+(f_{cb}+W_{cb}){t^{ac}_{ij}}^{(1)}\big{)}-\sum\limits_{k}\big{(}(f_{ik}+W_{ik}){t^{ab}_{kj}}^{(1)}+(f_{kj}+W_{kj}){t^{ab}_{ik}}^{(1)}\big{)}+\langle ij||ab\rangle=0 \tag{6.40}
$$

The central distinction between MPR-BWs2, BW-s2 and MP2 lies in the definition of
$W_{ab}$ and $W_{ij}$. The occupied block in MPR-BWs2 has five distinct contributions.
The first term ($A_{0}$) is identical to BW-s2 and is characterised by the fact
that it traces out to the second order energy multiplied by $A_{0}$:

<a id="Ch6.E41"></a>

$$
W_{ij}\leftarrow\frac{A_{0}}{8}\big{(}{t^{ab}_{ik}}^{(1)}\langle ab||jk\rangle+{t^{ab}_{jk}}^{(1)}\langle ab||ik\rangle\big{)} \tag{6.41}
$$

Analogously, the second term ($A_{1}$) traces out to the opposite-spin part of
the second order correlation energy and can best be written in spatial orbitals as:

<a id="Ch6.E42"></a>

$$
W_{ij}\leftarrow\frac{A_{1}}{2}\big{(}{t^{a\overline{b}}_{i\overline{k}}}^{(1)}(ia|\overline{kb})+{t^{a\overline{b}}_{j\overline{k}}}^{(1)}(ja|\overline{kb})\big{)} \tag{6.42}
$$

The remaining occupied terms contain the pseudo-density matrices $\rho_{ij}$ and
$\rho_{ab}$, which are defined in analogy to MP2, but are notably distinct from
the true second order MPR-BWs2 density matrix:

<a id="Ch6.E43"></a>

$$
\rho_{ij}=-\frac{1}{2}{t^{ab}_{ik}}^{(1)}{t^{ab}_{jk}}^{(1)} \tag{6.43}
$$

<a id="Ch6.E44"></a>

$$
\rho_{ab}=\frac{1}{2}{t^{ac}_{ij}}^{(1)}{t^{bc}_{ij}}^{(1)} \tag{6.44}
$$

The $A_{2}$ and $A_{3}$ terms are constructed as follows:

<a id="Ch6.E45"></a>

$$
W_{ij}\leftarrow A_{2}\langle ik||jl\rangle\rho_{kl}+A_{3}\langle ia||jb\rangle\rho_{ab} \tag{6.45}
$$

Finally, the $A_{4}$ term is given by a symmetric contraction with the fock matrix:

<a id="Ch6.E46"></a>

$$
W_{ij}\leftarrow\frac{A_{4}}{2}\big{(}f_{ik}\rho_{kj}+f_{jk}\rho_{ki}\big{)} \tag{6.46}
$$

The virtual parameters are labelled according to their occupied counterparts,
wherefore the $B_{0}$ and $B_{1}$ parameters are:

<a id="Ch6.E47"></a>

$$
W_{ab}\leftarrow\frac{B_{0}}{8}\big{(}{t^{ac}_{ij}}^{(1)}\langle bc||ij\rangle+{t^{bc}_{ij}}^{(1)}\langle ac||ij\rangle\big{)} \tag{6.47}
$$

<a id="Ch6.E48"></a>

$$
W_{ab}\leftarrow\frac{B_{1}}{2}\big{(}{t^{a\overline{c}}_{i\overline{j}}}^{(1)}(ib|\overline{jc})+{t^{b\overline{c}}_{i\overline{j}}}^{(1)}(ia|\overline{jc}) \tag{6.48}
$$

The $B_{2}$ parameter, which would contract $\rho_{ab}$ into $W_{ab}$ is deliberately
not implemented, since its evaluation contains a step of order $O(V^{4})$, where $V$
is the number of virtual orbitals. The $B_{3}$ and $B_{4}$ terms are given by:

<a id="Ch6.E49"></a>

$$
W_{ab}\leftarrow B_{3}\langle ai||bj\rangle\rho_{ij} \tag{6.49}
$$

<a id="Ch6.E50"></a>

$$
W_{ab}\leftarrow\frac{B_{4}}{2}\big{(}f_{ac}\rho_{cb}+f_{bc}\rho_{ca}\big{)} \tag{6.50}
$$

For an interpretation of these parameters and their respective terms,
see Ref. [[335]](../bib_references/bib.md#bib339)
.

Since terms with quadratic dependence on the amplitudes subsequently turn the
amplitude equation into a cubic tensor equation, convergence of the self-consistent
construction scheme described in section [6.8](topic_bws2.md) is sometimes difficult
or impossible to achieve. For this reason, it can be best to approximate the effect
of each parameter non-iteratively. As can be seen from the Hylleraas functional,
the second order correlation energy can be rewritten as:

<a id="Ch6.E51"></a>

$$
E^{(2)}_{\text{c}}=-\sum\limits_{pq}P^{(2)}_{pq}(f_{pq}+W_{pq}) \tag{6.51}
$$

where $P^{(2)}_{pq}$ denotes the exact second order density matrix. Replacing
$P^{(2)}_{ij}$ with $\rho_{ij}$ and $P^{(2)}_{ab}$ with $\rho_{ab}$ and subtracting
the iterative contribution defines the non-iterative approximation:

<a id="Ch6.E52"></a>

$$
E^{(2)}_{\text{c},\>\text{noniter}}=\sum\limits_{ij}\rho_{ij}W^{\text{noniter}}_{ij}-\sum\limits_{ab}\rho_{ab}W^{\text{noniter}}_{ab} \tag{6.52}
$$
