---
title: "11.2.5 Linear-Scaling QM/MM/PCM Calculations"
---

## 11.2.5 Linear-Scaling QM/MM/PCM Calculations

(July 4, 2026)

Recall that PCM electrostatics calculations require the solution of the set of
linear equations given in Eq. ([11.2](topic_pcm-em.md#eq:Kq=Rv)), to determine the vector
$\mathbf{q}$ of apparent surface charges. The precise forms of the matrices
$\mathbf{K}$ and $\mathbf{R}$ depend upon the particular PCM
(Table [11.3](topic_pcm-em.md#table:K-matrix)), but in any case they have dimension
$N_{\text{grid}}\times N_{\text{grid}}$, where $N_{\text{grid}}$ is the number of Lebedev grid
points used to discretize the cavity surface. Construction of the matrix
$\mathbf{K}^{-1}\mathbf{R}$ affords a numerically exact solution to
Eq. ([11.2](topic_pcm-em.md#eq:Kq=Rv)), whose cost scales as ${\cal{O}}({N^{3}_{\text{grid}}})$ in CPU time
and ${\cal{O}}({N^{2}_{\text{grid}}})$ in memory. This cost is exacerbated by smooth PCMs,
which discard fewer interior grid points so that $N_{\text{grid}}$ tends to be
larger, for a given solute, as compared to traditional discretization schemes.
For QM solutes, the cost of inverting $\mathbf{K}$ is usually negligible
relative to the cost of the electronic structure calculation, but for the large
values of $N_{\text{grid}}$ that are encountered in MM/PCM or QM/MM/PCM jobs,
the ${\cal{O}}({N^{3}_{\text{grid}}})$ cost of inverting $\mathbf{K}$ is often prohibitively expensive.

To avoid this bottleneck, Lange and Herbert[[561]](../bib_references/bib.md#bib576) have developed
an iterative conjugate gradient (CG) solver for Eq. ([11.2](topic_pcm-em.md#eq:Kq=Rv)) whose cost
scales as ${\cal{O}}({N^{2}_{\text{grid}}})$ in CPU time and ${\cal{O}}({N_{\text{grid}}})$ in memory.
A number of other cost-saving options are available, including efficient
pre-conditioners and matrix factorizations that speed up convergence of the CG
iterations, and a fast multipole algorithm for computing the electrostatic
interactions.[[814]](../bib_references/bib.md#bib849)
 Together, these features lend themselves to a
solution of Eq. ([11.2](topic_pcm-em.md#eq:Kq=Rv)) whose cost scales as ${\cal{O}}({N_{\text{grid}}})$ in
both memory and CPU time, for sufficiently large systems.[[561]](../bib_references/bib.md#bib576)
Currently, these options are available only for C-PCM, not for SS(V)PE or IEF-PCM.

Set **Solver** to **CG** in the *$pcm* section in order to invoke the CG solver, as described in
Section [11.2.4.1](subsec_PCM_job_control.md#subsec:PCM_job_control:PCM-section). Additional options for the CG solver are listed below,
each of which should also be specified in the *$pcm* input section. Researchers who use this feature
are asked to cite the original SwiG-PCM references[[754]](../bib_references/bib.md#bib787)

as well as the reference for the CG solver.[[561]](../bib_references/bib.md#bib576)

### `CGThresh`

> **The threshold for convergence of the conjugate gradient solver. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$: Conjugate gradient converges when the maximum residual is less than $10^{-n}$ .
> * **Recommendation**: The default typically affords PCM energies on par with the precision of matrix inversion for small systems. For systems that have difficulty with SCF convergence, one should increase $n$ or try the matrix inversion solver. For well-behaved or very large systems, a smaller $n$ might be permissible.

### `DComp`

> **Controls decomposition of matrices to reduce the matrix norm for the CG Solver. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: Turns off matrix decomposition
>     * `1`: Turns on matrix decomposition
>     * `3`: Option 1 plus only stores upper half of matrix and enhances gradient evaluation
> * **Recommendation**: None

### `PreCond`

> **Controls the use of the pre-conditioner for the CG solver. INPUT SECTION: $pcm**
>
> * **Type**: `None`
> * **Default**: `Off`
> * **Options**:
>     * No options. Specify the keyword to enable pre-conditioning.
> * **Recommendation**: A Jacobi block-diagonal pre-conditioner is applied during the conjugate gradient algorithm to improve the rate of convergence. This reduces the number of CG iterations, at the expense of some overhead. Pre-conditioning is generally recommended for large systems.

### `NoMatrix`

> **Specifies whether PCM matrices should be explicitly constructed and stored. INPUT SECTION: $pcm**
>
> * **Type**: `None`
> * **Default**: `Off`
> * **Options**:
>     * No options. Specify the keyword to avoid explicit construction of PCM matrices.
> * **Recommendation**: Storing the PCM matrices requires ${\cal{O}}({N_{\text{grid}}^{2}})$ memory. If this is prohibitive, the option forgoes explicit construction of the PCM matrices, and instead constructs the matrix elements as needed, reducing the memory requirement to ${\cal{O}}({N_{\text{grid}}})$ at the expense of additional computation.

### `UseMultipole`

> **Controls the use of the adaptive fast multipole method in the CG solver. INPUT SECTION: $pcm**
>
> * **Type**: `None`
> * **Default**: `Off`
> * **Options**:
>     * No options. Specify the keyword in order to enable the fast multipole method.
> * **Recommendation**: The fast multipole approach formally reduces the CPU time to ${\cal{O}}({N_{\text{grid}}})$ , but is only beneficial for spatially extended systems with several thousand cavity grid points. Requires the use of NoMatrix .

### `MultipoleOrder`

> **Specifies the highest multipole order to use in the FMM. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$: The highest order multipole in the multipole expansion.
> * **Recommendation**: Increasing the multipole order improves accuracy but also adds more computational expense. The default yields satisfactory performance in common QM/MM/PCM applications.

### `Theta`

> **The multipole acceptance criterion. INPUT SECTION: $pcm**
>
> * **Type**: `FLOAT`
> * **Default**: `0.6`
> * **Options**:
>     * $n$: A number between zero and one.
> * **Recommendation**: The default is recommended for general usage. This variable determines when the use of a multipole expansion is valid. For a given grid point and box center in the FMM, a multipole expansion is accepted when $r/d\leq$ , where $d$ is the distance from the grid point to the box center and $r$ is the radius of the box. Setting to one will accept all multipole expansions, whereas setting it to zero will accept none. If not accepted, the grid point’s interaction with each point inside the box is computed explicitly. A low is more accurate but also more expensive than a higher .

### `NBox`

> **The FMM boxing threshold. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: The maximum number of grid points for a leaf box.
> * **Recommendation**: The default is recommended. This option is for advanced users only. The adaptive FMM boxing algorithm divides space into smaller and smaller boxes until each box has less than or equal to grid points. Modification of the threshold can lead to speedup or slowdown depending on the molecular system and other FMM variables.

A sample input file for the linear-scaling QM/MM/PCM methodology
can be found in the `$QC/samples` directory, under the name
`pcm_qmmm_crambin.in`. This sample involves a QM/MM description of
a protein (crambin) in which a single tyrosine side chain is taken to be the QM
region. The entire protein is immersed in a dielectric using C-PCM with SwiG
discretization.
