---
title: "10.15.3 Fragment-Based Methods for Electronic Coupling"
---

## 10.15.3 Fragment-Based Methods for Electronic Coupling

(July 4, 2026)

## 10.15.3.1 Approach based on absolutely localized molecular orbitals

One can use absolutely localized molecular orbitals (ALMOs, see Chapter [12](../ch12_frag/chap_frag.md))
to construct charge-localized diabatic states directly from DFT calculations. The ALMOs
on each fragment are expanded by the AO basis functions belonging to the same fragment
alone, whose corresponding MO coefficient matrix is
fragment block-diagonal.[[683]](../bib_references/bib.md#bib705)

In energy decomposition analysis methods,[[682]](../bib_references/bib.md#bib706)

ALMOs are utilized to separate the effects of polarization and charge transfer in
intermolecular binding, because they have the useful property that they do not allow for
charge transfer between fragments under the Mulliken definition of charge population.
Making use of this property, one can construct charge-localized diabats for hole
and electron transfer. For example, considering the initial and final states of a hole
transfer process, $|D^{+}A\rangle$ and $|DA^{+}\rangle$, the two diabats
can be represented in the following form:

<a id="Ch10.E202"></a>

$$
\displaystyle|{\psi_{a}}\rangle \tag{10.202a}
$$

For systems where the donor and acceptor moieties are well-separated, one can
construct the ALMO-based diabats by simply concatenating orbitals obtained from
isolated fragment calculations: $D^{+}$ and $A$ for one diabat, and $D$ and $A^{+}$
for the other. The energy of each ALMO diabat can then be variationally optimized
with respect to orbital rotations on fragment, using the SCFMI technique (see
Section [12.5.1](../ch12_frag/sect_lp_scf.md)).[[1314]](../bib_references/bib.md#bib1371)
 These
ALMO-based diabatic states are variationally optimized such that the associated
nuclear forces can be easily computed.[[894]](../bib_references/bib.md#bib928)
 The mutual polarization of
donor and acceptor moieties in the presence of each other is also taken into account.

To calculate the electronic coupling between two ALMO diabats, one
should first construct the diabatic Hamiltonian in the ALMO state basis

<a id="Ch10.E203"></a>

$$
\mathbf{H}^{\prime}=\begin{pmatrix}H^{\prime}_{aa}&H^{\prime}_{ab}\\
H^{\prime}_{ba}&H^{\prime}_{bb}\end{pmatrix} \tag{10.203}
$$

and then transform that into the Löwdin-orthogonalized basis

<a id="eq:sym_ortho_H"></a>

$$
\mathbf{H}=\mathbf{S}^{-1/2}\mathbf{H}^{\prime}\mathbf{S}^{-1/2} \tag{10.204}
$$

whose off-diagonal element, $H_{ab}$, corresponds to the diabatic coupling to be evaluated. In the 2-state case, we have

<a id="eq:almo_coupling"></a>

$$
H_{ab}=\frac{1}{1-S_{ab}^{2}}\left|H^{\prime}_{ab}-\frac{H^{\prime}_{aa}+H^{\prime}_{bb}}{2}S_{ab}\right| \tag{10.205}
$$

which requires the overlap between two ALMO diabats and the diagonal and off-diagonal
elements of $\mathbf{H}^{\prime}$. The interstate overlap is given by

<a id="eq:state_overlap"></a>

$$
S_{ab}=\langle\psi_{a}|\psi_{b}\rangle=\mathrm{det}\big{[}(\mathbf{C}^{(a)}_{\mathrm{o}})^{\dagger}\mathbf{S}\mathbf{C}^{(b)}_{\mathrm{o}}\big{]}\;. \tag{10.206}
$$

where $\mathbf{C}^{(a)}_{\mathrm{o}}$ and $\mathbf{C}^{(b)}_{\mathrm{o}}$ are
MO coefficients for the occupied orbitals in diabats $|\psi_{a}\rangle$ and
$|\psi_{b}\rangle$, respectively, and $\mathbf{S}$ is the AO overlap matrix.

The elements of the diabatic Hamiltonian matrix can be evaluated using the multi-state
DFT (MSDFT) approach.[[220]](../bib_references/bib.md#bib216)

For the diagonal elements, it is straightforward to employ the KS energies of the two diabats:

<a id="Ch10.E207"></a>

$$
H^{\prime}_{aa}=E_{a}^{\mathrm{KS}}[\mathbf{P}^{(a)}],\quad H^{\prime}_{bb}=E_{b}^{\mathrm{KS}}[\mathbf{P}^{(b)}] \tag{10.207}
$$

where $\mathbf{P}^{(a)}$ and $\mathbf{P}^{(b)}$ are the one-electron density matrices
associated with two ALMO states $|\psi_{a}\rangle$ and $|\psi_{b}\rangle$, respectively.
The approximation for the off-diagonal element is theoretically more challenging. In the original
MSDFT scheme,[[220]](../bib_references/bib.md#bib216)

<a id="eq:msdft1"></a>

$$
H^{\prime}_{ab}=S_{ab}\left[V_{\mathrm{nn}}+\mathbf{P}_{ab}\cdot\mathbf{h}+\frac{1}{2}\mathbf{P}_{ab}\cdot\mathbf{II}\cdot\mathbf{P}_{ab}+\frac{1}{2}(\Delta E_{a}^{\mathrm{c}}+\Delta E_{b}^{\mathrm{c}})\right] \tag{10.208}
$$

where $\mathbf{P}_{ab}$ is the one-particle transition density matrix between two ALMO states

<a id="eq:trans_den"></a>

$$
\mathbf{P}_{ab}=\mathbf{C}_{\mathrm{o}}^{(a)}\left[(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger}\mathbf{S}\mathbf{C}_{\mathrm{o}}^{(a)}\right]^{-1}(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger} \tag{10.209}
$$

The first three terms on the right-hand side of Eq. ([10.208](#eq:msdft1)) correspond to the contributions
from nuclear repulsion, one-electron Hamiltonian (kinetic energy and nuclei-electron attraction),
and full two-electron integrals (Coulomb and full HF exchange),
which can be derived as in non-orthogonal CI.[[1356]](../bib_references/bib.md#bib1417)

The last term accounts for the contribution from exchange-correlation (XC) functional
as a correction to the HF coupling, which is given by the average of the difference between the
KS and HF energies calculated from the same one-electron density matrix for each diabat:

<a id="Ch10.E210"></a>

$$
\displaystyle\Delta E_{a}^{\mathrm{c}} \tag{10.210a}
$$

This approach was denoted as ALMO(MSDFT) in Ref. [[898]](../bib_references/bib.md#bib929)
 and it was found to
overestimate the electronic couplings for the tested hole and electron transfer systems.
A modified approach, denoted as ALMO(MSDFT2), was proposed in Ref. [[898]](../bib_references/bib.md#bib929)
,
which evaluates the XC contribution using the XC energy of the symmetrized transition density matrix

<a id="eq:msdft2"></a>

$$
H_{ab}^{\prime}=S_{ab}\left(V_{\mathrm{nn}}+\mathbf{P}_{ab}\cdot\mathbf{h}+\tfrac{1}{2}\mathbf{P}_{ab}\cdot\mathbf{II}\cdot\mathbf{P}_{ab}+E_{\mathrm{xc}}[\tilde{\mathbf{P}}_{ab}]\right) \tag{10.211}
$$

where

<a id="Ch10.E212"></a>

$$
\tilde{\mathbf{P}}_{ab}=\frac{1}{2}(\mathbf{P}_{ab}+\mathbf{P}_{ba})\;. \tag{10.212}
$$

Note that in Eq. ([10.211](#eq:msdft2)), $\mathbf{II}$
includes only Coulomb integrals and a fraction of exact exchange if hybrid functionals are employed.

According to the benchmark results in Ref. [[898]](../bib_references/bib.md#bib929)
, ALMO(MSDFT2) shows better accuracy
than the original MSDFT method for hole and electron transfer, and thus it is implemented as the default
approach to compute electronic couplings between ALMO diabats in **Q-Chem**. We note that the results
given by Eq. ([10.211](#eq:msdft2)) may become inaccurate when the overlap between two states
becomes near-singular, as

<a id="Ch10.E213"></a>

$$
\boldsymbol{\sigma}_{ba}=(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger}\mathbf{S}\mathbf{C}_{\mathrm{o}}^{(a)} \tag{10.213}
$$

is inverted when constructing the transition density [Eq. ([10.209](#eq:trans_den))].
To circumvent this numerical issue, one can replace the inverse in
Eq. ([10.209](#eq:trans_den)) with the Penrose pseudo-inverse, which was suggested for a similar objective in
Ref. [[1049]](../bib_references/bib.md#bib1094)
.

The evaluation of electronic coupling between ALMO-based states using the original MSDFT or MSDFT2
scheme has been extended to non-aufbau electronic states prepared using ALMO-based $\Delta$SCF
calculations.[[899]](../bib_references/bib.md#bib931)
 This method, which can be referred to as $\Delta$-ALMO(MSDFT) or
$\Delta$-ALMO(MSDFT2), is capable of calculating the coupling between locally excited (LE) and
charge-transfer (CT) states. More details regarding the job control can be found in
Sec. [10.15.3.4](#subsubsec:frag_diab_job_control).

## 10.15.3.2 Projection operator Diabatization (POD)

Besides ALMO-based diabatization method, other fragment-based diabatization methods are
available in **Q-Chem**. The projection operator diabatization (POD) method [[705]](../bib_references/bib.md#bib737)

starts from a standard KS-DFT calculation of the system and post-processes the converged
Fock matrix. It first transforms the Fock matrix into the Löwdin-orthogonalized AO basis and
then partitions that into the donor and acceptor blocks, assuming that these orthogonalized AO
basis functions still retain their original fragment tags:

<a id="eq:pod_fock"></a>

$$
\tilde{\mathbf{F}}=\mathbf{S}^{-1/2}\mathbf{F}\mathbf{S}^{-1/2}=\begin{pmatrix}\tilde{\mathbf{F}}_{dd}&\tilde{\mathbf{F}}_{da}\\
\tilde{\mathbf{F}}_{ad}&\tilde{\mathbf{F}}_{aa}\end{pmatrix} \tag{10.214}
$$

One then diagonalizes $\tilde{\mathbf{F}}_{dd}$ and $\tilde{\mathbf{F}}_{aa}$ separately

<a id="Ch10.E215"></a>

$$
\boldsymbol{\epsilon}_{d}=\mathbf{D}_{d}^{\dagger}\tilde{\mathbf{F}}_{dd}\mathbf{D}_{d},\ \boldsymbol{\epsilon}_{a}=\mathbf{D}_{a}^{\dagger}\tilde{\mathbf{F}}_{aa}\mathbf{D}_{a}, \tag{10.215}
$$

where the eigenvectors $\mathbf{D}_{d}$ and $\mathbf{D}_{a}$ define the single-particle “diabatic states”:

<a id="A3.S8.EGx101"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{|}\bar{\varphi}^{(d)}_{p}\big{\rangle}&\displaystyle=\sum_{\mu}\big{|}\tilde{\chi}^{(d)}_{\mu}\big{\rangle}(D_{d})^{\mu}_{\ p}\\
\displaystyle\big{|}\bar{\varphi}^{(a)}_{p}\big{\rangle}&\displaystyle=\sum_{\mu}\big{|}\tilde{\chi}^{(a)}_{\mu}\big{\rangle}(D_{a})^{\mu}_{\ p},\\
\end{aligned} \tag{10.216}
$$

and transforms the off-diagonal block of the Fock matrix into this diabatic basis

<a id="Ch10.E217"></a>

$$
\bar{\mathbf{F}}_{da}=\mathbf{D}_{d}^{\dagger}\tilde{\mathbf{F}}_{da}\mathbf{D}_{a} \tag{10.217}
$$

yielding

<a id="Ch10.E218"></a>

$$
\bar{\mathbf{F}}=\begin{pmatrix}\boldsymbol{\epsilon}_{d}&\bar{\mathbf{F}}_{da}\\
\bar{\mathbf{F}}_{ad}&\boldsymbol{\epsilon}_{a}\end{pmatrix} \tag{10.218}
$$

The couplings between these single-particle diabatic orbitals can then be directly read
off from the elements of $\bar{\mathbf{F}}_{da}$.

The **Q-Chem** implementation of the POD method follows the description in
Refs. [[705]](../bib_references/bib.md#bib737)
 and [[1513]](../bib_references/bib.md#bib1582)
, where a closed-shell
reference system is used to generate the Fock matrix to be processed, *i.e.*, $\mathbf{F}$
in Eq. ([10.214](#eq:pod_fock)). By default, only the $D$(HOMO)–$A$(HOMO) coupling is calculated
for the hole transfer cases, and the $D$(LUMO)–$A$(LUMO) coupling for the electron transfer
cases. To calculate the couplings between multiple pairs of donor and acceptor orbitals,
the user can set *$rem* variable POD_MULTI_PAIRS = TRUE and
control the number of orbitals pairs through POD_WINDOW. See the
instruction in Section [10.15.3.4](#subsubsec:frag_diab_job_control).

Because of the use of globally Löwdin orthogonalized orbitals in Eq. ([10.214](#eq:pod_fock)), the
diabatic orbitals created by POD cannot be strictly localized on fragments. This renders the
POD results unstable with the change of employed AO basis sets: when larger basis sets
are used, the mixing between AO basis functions on different fragments becomes stronger,
and the resulting $H_{ab}$ decreases. To alleviate this problem, a revised POD method,
which was named as “POD2”, was proposed by Ghan *et al.*.[[437]](../bib_references/bib.md#bib449)

It avoids the global Löwdin orthogonalization of the AO basis; instead, it separately
diagonalizes the the donor and acceptor blocks of the Fock matrix
(in the original AO basis):

<a id="Ch10.E219"></a>

$$
\mathbf{F}_{dd}\mathbf{C}_{d}=\mathbf{S}_{dd}\mathbf{C}_{d}\boldsymbol{\epsilon}_{d},\quad\mathbf{F}_{aa}\mathbf{C}_{a}=\mathbf{S}_{aa}\mathbf{C}_{a}\boldsymbol{\epsilon}_{a} \tag{10.219}
$$

The obtained diabatic MO coefficient matrix is fragment-block-diagonal in the AO basis:

<a id="Ch10.E220"></a>

$$
\mathbf{C}_{\text{diab}}=\begin{pmatrix}\mathbf{C}_{d}&\mathbf{0}\\
\mathbf{0}&\mathbf{C}_{a}\\
\end{pmatrix} \tag{10.220}
$$

Transforming the AO Fock matrix into this diabatic MO basis, the D–D and A–A blocks of
the resulting matrix are diagonal matrices:

<a id="Ch10.E221"></a>

$$
\bar{\mathbf{F}}_{\text{diab}}=\mathbf{C}_{\text{diab}}^{T}\mathbf{F}\mathbf{C}_{\text{diab}}=\begin{pmatrix}\boldsymbol{\epsilon}_{d}&\bar{\mathbf{F}}_{da}\\
\bar{\mathbf{F}}_{ad}&\boldsymbol{\epsilon}_{a}\\
\end{pmatrix} \tag{10.221}
$$

Using the matrix elements in the off-diagonal block ($\bar{\mathbf{F}}_{da}$) directly would yield
overestimated couplings since the diabatic MOs $\mathbf{C}_{d}$ and $\mathbf{C}_{a}$ are not
orthogonal to each other. Therefore, a final orthogonalization step is required to obtain the diabatic
coupling between a pair of orbitals that are located on the donor and acceptor, respectively.
Denoting this pair of orbital as $\phi_{d}$ and $\phi_{a}$, one can construct the $2\times 2$ Hamiltonian
and overlap matrices:

<a id="Ch10.E222"></a>

$$
\mathbf{H}=\begin{pmatrix}\epsilon_{d}&\bar{F}_{da}\\
\bar{F}_{ad}&\epsilon_{a}\\
\end{pmatrix},\quad\mathbf{S}=\begin{pmatrix}1&S_{da}\\
S_{ad}&1\\
\end{pmatrix} \tag{10.222}
$$

Two orthogonalization schemes have been investigated by Ghan *et al.*. [[437]](../bib_references/bib.md#bib449)

The first approach performs a Löwdin orthgonalization on $\phi_{d}$ and $\phi_{a}$, which
is denoted as POD2L. The resulting coupling between the orthogonalized diabatic orbitals
are

<a id="Ch10.E223"></a>

$$
H_{da}^{\text{eff}}=\frac{1}{1-S_{da}^{2}}\left|\bar{F}_{da}-\frac{1}{2}(\epsilon_{d}+\epsilon_{a})S_{da}\right| \tag{10.223}
$$

The second approach employs the Gram-Schmidt orthogonalization, which keeps one of
the two orbitals ($\phi_{d}$ or $\phi_{a}$) intact while ensures that the other is strictly
orthogonal to it. This approach is denoted as POD2GS, and it might be better choice for
asymmetric cases (*e.g.* surface and adsorbates) where one can choose to retain the
orbital on the less sizable fragment. These two POD2 variants afford significantly improved
accuracy over the original POD method, especially in terms of the robustness with regard to
the use of extensive basis sets.

## 10.15.3.3 Fragment Orbital DFT (FODFT)

Fragment orbital DFT (FODFT) [[1006]](../bib_references/bib.md#bib1047)

is an approach to compute the diabatic couplings for hole and electron transfer between
fragments. There have been several different flavors of FODFT approaches developed
in literature, and here we introduce the most recent variant by Schober *et al.*.[[1217]](../bib_references/bib.md#bib1271)

Considering a hole-transfer process, $\text{D}^{+}+\text{A}\to\text{D}+\text{A}^{+}$, or alternatively an electron transfer
process $\text{D}^{-}+\text{A}\to\text{D}+\text{A}^{-}$, where the donor (D) and acceptor (A) fragments
have $n_{\text{D}}$ and $n_{\text{A}}$ electrons, respectively, the procedure is the following.

- •

Perform KS-DFT calculations for isolated donor and acceptor fragments;
collect the converged fragment orbitals: 

$\{\phi_{\text{D1}},\phi_{\text{D2}},\dots,\phi_{\text{D}n_{\text{D}}\pm 1}\}$ and
$\{\phi_{\text{A1}},\phi_{\text{A2}},\dots,\phi_{\text{A}n_{\text{A}}}\}$
- •

Löwdin orthogonalize the occupied orbitals on two fragments.
The reactant diabat ($\text{D}^{+}\text{A}$ or $\text{D}^{-}\text{A}$) can be represented as

<a id="Ch10.E224"></a>

$$
|\bar{\psi}_{a}\rangle=\frac{1}{\sqrt{(N-1)!}}\;\mathrm{det}\left\{\bar{\phi}_{\text{D1}},\bar{\phi}_{\text{D2}},\dots,\bar{\phi}_{\text{D}n_{\text{D}}\pm 1}\bar{\phi}_{\text{A1}},\bar{\phi}_{\text{A2}},\dots,\bar{\phi}_{\text{A}n_{\text{A}}}\right\} \tag{10.224}
$$

where “$\bar{\phi}$” denotes Löwdin-orthogonalized orbitals,
and $N=n_{\text{D}}+n_{\text{A}}$. Note that the lowest unoccupied orbital where the electron
is transferring to, $\phi_{\text{D}n_{\text{D}}}$ in the case of HT or $\phi_{\text{A}n_{\text{A}}+1}$ in the case of ET,
also needs to be made orthogonal to the space spanned by all occupied orbitals.
- •

Construct the product diabat ($\text{DA}^{+}$ or $\text{DA}^{-}$), simply by moving the hole from
$\bar{\phi}_{\text{D}n_{\text{D}}}$ to $\bar{\phi}_{\text{A}n_{\text{A}}}$ (HT), or the excess electron from
$\bar{\phi}_{\text{D}n_{\text{D}}+1}$ to $\bar{\phi}_{\text{A}n_{\text{A}}+1}$ (ET)

<a id="Ch10.E225"></a>

$$
|\bar{\psi}_{b}\rangle=\frac{1}{\sqrt{(N-1)!}}\;\mathrm{det}\left\{\bar{\phi}_{\text{D1}},\bar{\phi}_{\text{D2}},\dots,\bar{\phi}_{\text{D}n_{\text{D}}}\bar{\phi}_{\text{A1}},\bar{\phi}_{\text{A2}},\dots,\bar{\phi}_{\text{A}n_{\text{A}}\pm 1}\right\} \tag{10.225}
$$

- •

Compute the electronic coupling between $|\bar{\psi}_{a}\rangle$ and
$|\bar{\psi}_{b}\rangle$, which is approximated by the coupling of the
orthogonalized fragment orbitals through the Kohn-Sham Fock operator, built from the reactant diabat:

<a id="A3.S8.EGx102"></a>

$$
\displaystyle\langle\bar{\psi}_{a}|\hat{H}|\bar{\psi}_{b}\rangle\approx\begin{cases}\langle\phi_{\text{D}n_{\text{D}}}|\hat{f}_{\text{KS}}|\phi_{\text{A}n_{\text{A}}}\rangle&\text{HT}\\
\langle\phi_{\text{D}n_{\text{D}}+1}|\hat{f}_{\text{KS}}|\phi_{\text{A}n_{\text{A}}+1}\rangle&\text{ET}\end{cases} \tag{10.226}
$$

The approach described above is denoted as
FODFT($2n-1$)@$\text{D}^{+}\text{A}$ (HT)/FODFT($2n+1$)@$\text{D}^{-}\text{A}$ (ET),[[1217]](../bib_references/bib.md#bib1271)

as the charged fragment is explicitly taken into account when preparing the fragment orbitals and the KS Fock
matrix is built from $2n\mp 1$ occupied orbitals. Besides this, there are two other variants of FODFT:

1. 1.

FODFT($2n$)@DA:[[1232]](../bib_references/bib.md#bib1287)
 fragment orbitals prepared with
D and A both closed-shell; KS Fock operator constructed from $2n$ occupied orbitals.
2. 2.

FODFT($\mathrm{2n-1}$)@DA (HT) /
FODFT($2n+1$)@$\text{D}^{-}\text{A}^{-}$ (ET):[[1006]](../bib_references/bib.md#bib1047)
 fragment orbitals
prepared with the system having one excess electron (DA for HT and $\text{D}^{-}\text{A}^{-}$ for ET),
while one occupied orbital is removed when building the KS Fock operator.

According to the benchmark results,[[1217]](../bib_references/bib.md#bib1271)

FODFT($2n-1$)@$\text{D}^{+}\text{A}$ (HT)/FODFT($2n+1$)@$\text{D}^{-}\text{A}$ (ET)
is the best-performing method, possibly because
of its explicit account for charged fragments and consistent electron count in
the preparation of fragment orbitals and in the construction of Fock matrix.

One issue associated with the FODFT methods is that for asymmetric systems, the
results would depend on how one chooses the initial and final states for an electron or
hole transfer process (*e.g.*, $\text{D}^{+}\text{A}$ vs. $\text{DA}^{+}$), especially for the two variants that
build the Fock matrix with $2n\pm 1$ occupied orbitals.[[898]](../bib_references/bib.md#bib929)

The **Q-Chem** implementation of
FODFT($\mathrm{2n-1}$)@DA/FODFT($2n+1$)@$\text{D}^{-}\text{A}^{-}$
automatically computes $H_{ab}$ in both ways
and then reports the average, as it only requires an extra Fock matrix build. This, however,
is not automatically done for
FODFT($2n-1$)@$\text{D}^{+}\text{A}$/FODFT($2n+1$)@$\text{D}^{-}\text{A}$.

## 10.15.3.4 Job control for fragment-based diabatization methods

POD, FODFT, and ALMO(MSDFT) calculations in **Q-Chem** require specification of fragments in the
*$molecule* section (see Section [12.2](../ch12_frag/sect_FRAGinput.md)). For ALMO(MSDFT) calculations, one also needs
to specify the charge and multiplicity of each fragment in each diabatic state in the *$almo_coupling* section, where two hyphens indicate the separation of different diabats:

> ```qchem
> $almo_coupling
>    charge_frag_1     mult_frag_1        !diabat 1
>    charge_frag_2     mult_frag_2
>    --
>    charge_frag_1     mult_frag_1        !diabat 2
>    charge_frag_2     mult_frag_2
> $end
> ```

The method employed to calculate the diabatic coupling is specified through
FRAG_DIABAT_METHOD. Note that the current implementation of FODFT is
limited to (i) hole transfer between the HOMOs of two fragments or (ii) electron transfer
between the LUMOs of two fragments.

The ALMO(MSDFT)/ALMO(MSDFT2) method can be used to calculate the diabatic couplings
involved in ground-state electron or hole transfer processes. With the incorporation of
ALMO-based $\Delta$SCF (supported by **Q-Chem** 6.2.1 and after), this method can further
be used to calculate the coupling between LE and CT states in photoinduced electron or
hole transfer processes. One will need set EX_ALMO_MSDFT = TRUE for
these calculations. Additionally, a simple approach based on the off-diagonal elements of
Löwdin orthogonalized Hamiltonian (Eq. [10.204](#eq:sym_ortho_H) generalized to multi-state
cases) has also been implemented to calculate the diabatic couplings with multiple ($>2$)
states taken into account at the same time.

The ALMO-based $\Delta$SCF states will be specified through the *$scfmi_mom* section, for which
the syntax is documented in detail in Sec. [12.6.7](../ch12_frag/sect_eda2_non_aufbau.md). The specifications for
different diabatic states are separated by “–”. For diabatic states that do not involve
on-fragment excitations, simply write “–” with no additional specification.

### `FRAG_DIABAT_METHOD`

> **Specify fragment based diabatization method**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * `ALMO_MSDFT`: Perform ALMO(MSDFT) diabatization
>     * `POD`: Perform projection operator diabatization (the original method)
>     * `POD2_L`: Perform POD2 with Löwdin orthogonalization
>     * `POD2_GS`: Perform POD2 with Grad-Schmidt orthogonalization
>     * `ESID`: The energy-split-in-dimer method,
>     * `1384`: Valeev E. F. et al. J. Am. Chem. Soc. (2006) ,
>     * `128`: , pp. 9882 . Link which is equivalent to the FMO approach introduced in Section 10.15.2.5
>     * `FODFT`: Calculate electronic coupling using fragment orbital DFT
> * **Recommendation**: NONE

### `FRAG_DIABAT_DOHT`

> **Specify whether hole or electron transfer is considered**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Do hole transfer
>     * `FALSE`: Do electron transfer
> * **Recommendation**: Need to be specified for POD and FODFT calculations

### `FRAG_DIABAT_PRINT`

> **Specify the print level for fragment based diabatization calculations**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No additional prints $\geq 1$ Print additional details
> * **Recommendation**: Use the default unless debug information is needed

### `MSDFT_METHOD`

> **Specify the scheme for ALMO(MSDFT)**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `1`: The original MSDFT scheme [Eq. ( 10.208 )]
>     * `2`: The ALMO(MSDFT2) approach [Eq. ( 10.211 )]
> * **Recommendation**: Use the default method. Note that the method will be automatically reset to 1 if a meta-GGA functional is requested.

### `MSDFT_PINV_THRESH`

> **Set the threshold for pseudo-inverse of the interstate overlap**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$: Set the threshold to 10 ${}^{-n}$
> * **Recommendation**: Use the default value

### `EX_ALMO_MSDFT`

> **Enable MSDFT/MSDFT2 calculations using ALMO-based $\Delta$ SCF states**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Will calculate ALMO- $\Delta$ SCF states as specified in $scfmi_mom
>     * `FALSE`: Performing ground-state ALMO(MSDFT) calculations.
> * **Recommendation**: None

### `POD_MULTI_PAIRS`

> **Calculate the couplings between multiple pairs of donor and acceptor orbitals in POD**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Calculate the couplings between multiple pairs of orbitals
>     * `FALSE`: Only calculate the $D$ (HOMO)– $A$ (HOMO) coupling (for hole transfer) or the $D$ (LUMO)– $A$ (LUMO) coupling (for electron transfer)
> * **Recommendation**: None

### `POD_WINDOW`

> **Specify the number of donor and acceptor orbitals when couplings between multiple pairs are requested**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Including
>     * $n$: frontier occupied orbitals (from $\text{HOMO}-n+1$ to HOMO) and
>     * $n$: frontier virtual orbitals (from LUMO to $\text{LUMO}+n-1$ ) for both donor and acceptor
> * **Recommendation**: None

### `FODFT_METHOD`

> **Specify the flavor of FODFT method**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: FODFT( $\mathrm{2n-1}$ )@ $D^{+}A$ (HT) / FODFT( $\mathrm{2n+1}$ )@ $D^{-}A$ (ET)
>     * `2`: FODFT( $\mathrm{2n}$ )@ $DA$
>     * `3`: FODFT( $\mathrm{2n-1}$ )@ $DA$ (HT) / FODFT( $\mathrm{2n+1}$ )@ $D^{-}A^{-}$ (ET)
> * **Recommendation**: The default approach shows the best overall performance

### `FODFT_DONOR`

> **Specify the donor fragment in FODFT calculation**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: First fragment as donor
>     * `2`: Second fragment as donor
> * **Recommendation**: With FODFT_METHOD = 1, the charged fragment needs to be the donor fragment

???+ example "Example 10.77: ALMO(MSDFT2) calculation for hole transfer in ethylene dimer"
    ```qchem
    $molecule
    1 2
    --
    1 2
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               PBE0
       BASIS                6-31+G(D)
       UNRESTRICTED         TRUE
       THRESH               14
       SCF_CONVERGENCE      8
       SCFMI_MODE           1
       FRGM_METHOD          STOLL
       FRAG_DIABAT_METHOD   ALMO_MSDFT
       INTEGRAL_SYMMETRY    FALSE
       POINT_GROUP_SYMMETRY FALSE
    $end
    
    $almo_coupling
      1  2
      0  1
      --
      0  1
      1  2
    $end
    ```

???+ example "Example 10.78: ALMO(MSDFT2) for the hole transfer between Indole ${}^{+\ast}$ and
guanine. The indole radical cation is in a non-aufbau state,
with one $\beta$ electron promoted from HOMO to HOMO $-$ 1."
    ```qchem
    $molecule
    1 2
    --
    1 2
    C        2.36540       -2.78410        3.38000
    C        3.73980       -2.83830        3.38000
    C        2.00000       -1.40150        3.38000
    C        3.20860       -0.65020        3.38000
    C        0.77390       -0.70880        3.38000
    C        3.22680        0.75070        3.38000
    C        0.78630        0.67870        3.38000
    C        2.00000        1.40150        3.38000
    N        4.24650       -1.55510        3.38000
    H        4.40550       -3.69200        3.38000
    H        5.22930       -1.31740        3.38300
    H       -0.16770       -1.25470        3.38000
    H        4.16090        1.30910        3.38000
    H       -0.15420        1.22450        3.38000
    H        1.97300        2.48860        3.38000
    H        1.69890       -3.63700        3.38000
    --
    0 1
    C        1.63430       -2.77360        0.00200
    C        1.25300       -0.68190        0.01800
    C        1.32680        0.75830        0.00900
    C       -1.17560        0.58330        0.00600
    C        0.00000       -1.29190        0.00000
    O        2.29090        1.51390       -0.00300
    N        0.26680       -2.63600       -0.00400
    N        2.26910       -1.61180        0.01600
    N        0.00000        1.29190        0.00000
    N       -2.33770        1.33540       -0.07400
    N       -1.24290       -0.72560        0.01500
    H        2.11200       -3.74490       -0.00100
    H       -0.02860        2.30410       -0.09800
    H       -2.35450        2.16800        0.50600
    H       -3.15580        0.75300        0.07300
    H       -0.42990       -3.37190       -0.01800
    $end
    
    $rem
    JOBTYPE  SP
    METHOD   B3LYP
    BASIS    6-31G
    SCF_CONVERGENCE  8
    POINT_GROUP_SYMMETRY  FALSE
    SCFMI_MODE   1
    FRGM_METHOD  STOLL
    FRAG_DIABAT_METHOD ALMO_MSDFT
    MSDFT_METHOD    2
    EX_ALMO_MSDFT   TRUE
    $end
    
    $almo_coupling
    1  2
    0  1
    --
    0  1
    1  2
    $end
    
    $scfmi_mom
    1 0 0 b
    --
    $end
    ```

???+ example "Example 10.79: POD diabatization method for hole transfer in ethylene dimer. FRAG_DIABAT_METHOD can be set to POD2_L or POD2_GS for POD2 diabatization methods."
    ```qchem
    $molecule
    0 1
    --
    0 1
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               lrc-wpbeh
       BASIS                6-31+g(d)
       FRAG_DIABAT_METHOD   pod
       SCF_CONVERGENCE      8
       THRESH               14
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 10.80: FODFT( $\mathrm{2n-1}$ )@ $D^{+}A$ calculation for hole transfer
in ethylene dimer"
    ```qchem
    $molecule
    1 2
    --
    1 2
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               wb97x-d
       BASIS                6-31+g(d)
       UNRESTRICTED         true
       SCF_CONVERGENCE      8
       THRESH               14
       FRAG_DIABAT_METHOD   fodft
       FODFT_METHOD         1
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
