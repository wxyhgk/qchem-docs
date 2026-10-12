---
title: "12.6.3 Polarization Energy with a Well-Defined Basis Set Limit"
---

## 12.6.3 Polarization Energy with a Well-Defined Basis Set Limit

(July 4, 2026)

The definition of polarization energy lowering in the original ALMO-EDA
used the full AO space of each fragment as the variational degrees of
freedom. This is based on the assumption that the AO basis functions are
fragment-ascribable based on their atomic centers. However, this assumption
becomes inappropriate when very large basis sets are used, especially those
with diffuse functions (*e.g.* def2-QZVPPD). In such scenarios, basis functions
on a given fragment tend to describe other fragments so that the “absolute
localization” constraint becomes weaker and finally gets effectively removed.
This is why the original ALMO-EDA scheme does not have a well-defined basis set
limit for its polarization energy.

To overcome this problem, Horn and Head-Gordon[[593]](../bib_references/bib.md#bib617)
 proposed a new definition for
the POL term in the ALMO-EDA method based on fragment electrical response
functions (FERFs). FERFs on a given fragment are prepared by
solving CPSCF equations after its SCF solution is found:

<a id="Ch12.E1"></a>

$$
H_{ai,bj}(\Delta_{\mu})_{bj}=2(M_{\mu})_{ai}, \tag{12.1}
$$

where $\mathbf{H}$ is SCF orbital Hessian and $\mathbf{M}_{\mu}$ is a component
($\mu$) of a multipole matrix with a certain order. The resulting fragment
response matrices ($\{\Delta_{\mu}\}$) are a set of $n_{\mathrm{v}}\times n_{\mathrm{o}}$ matrices. Then, a singular value decomposition (SVD) is
performed on $\Delta_{\mu}$:

<a id="eq:ferf_cpscf"></a>

$$
(\Delta_{\mu})_{ai}=(L_{\mu})_{ab}(d_{\mu})_{bj}(R_{\mu}^{T})_{ji}, \tag{12.2}
$$

and the left vectors (not including the null vectors) will be used to construct
a truncated virtual space, which is used to define the variational degrees of
freedom for the SCF-MI problem:

<a id="Ch12.E3"></a>

$$
\mathbf{V}_{\mu}=\mathbf{C}_{\mathrm{vir}}\mathbf{L}_{\mu}, \tag{12.3}
$$

where $\mathbf{C}_{\mathrm{vir}}$ denotes the original virtual orbitals of the
given fragment.

The basic spirit of using FERFs is to obtain a subset of virtuals that is most
pertinent to the electrical polarization of a given fragment, while the
redundant variational degrees of freedom (which might be CT-like) are excluded.
This scheme is shown to give a well-defined basis set limit for the
polarization energy that relies on the SCF-MI calculation. The multipole orders
dipole (D), quadrupole (Q), and octopole (O)m included on the RHS of
Eq. ([12.2](#eq:ferf_cpscf)), decide the span of FERFs on each fragment. Numerical
experiments suggest that the inclusion of dipole- and quadrupole-type responses
is able to long-range induced electrostatics correctly and also gives a
well-defined basis set limit, which is thus recommended as the working basis of
the SCF-MI problem. The full span of the polarization subspace of fragment $A$
is thus:

<a id="eq:pol_ss"></a>

$$
\mathbf{O}_{A}\oplus\mathrm{span}\{\mathbf{V}_{\mu x},\mathbf{V}_{\mu y},\mathbf{V}_{\mu z}\}\oplus\mathrm{span}\{\mathbf{V}_{Q2,-2},\mathbf{V}_{Q2,-1},\mathbf{V}_{Q2,0},\mathbf{V}_{Q2,1},\mathbf{V}_{Q2,2}\}. \tag{12.4}
$$

Therefore, each occupied orbital will be paired with eight virtual orbitals (if
the employed AO basis is large enough).

The polarization subspaces constructed as in Eq. ([12.4](#eq:pol_ss)) are
non-orthogonal between fragments. Therefore, it is named as the “nDQ” model
for polarization. There is another version of this method which enforces
interfragment orthogonality between the polarization subspaces and it is
correspondingly termed as “oDQ” (or with other multipole orders). The
preparation of orthogonal FERFs is more complicated (see
Ref. [[593]](../bib_references/bib.md#bib617)
 for the details) and usually gives less favorable
polarization energies. For most general cases, we recommend the use of the
“nDQ” model. Calculations using FERFs are performed using the generalized
SCF-MI procedure introduced in Section [12.6.2](sect_gen_scfmi.md).

However, solving the CPSCF equation requires inverting the large orbital Hessian matrix $\mathbf{H}$ of dimension $ov\times ov$, which is the time demanding step in solving for FERFs. For example, in Hartree-Fock theory, in the canonical representation, it has matrix elements

<a id="Ch12.E5"></a>

$$
H_{ai,bj}=2\left[(\epsilon_{a}-\epsilon_{i})\delta_{ij}\delta_{ab}+\langle aj||ib\rangle+\langle ab||ij\rangle\right]. \tag{12.5}
$$

Recently, Aldossary and coauthors

 proposed an uncoupled-FERFs (uFERFs) to improve the conventional FERFs. The idea of uFERFs is simply to adopt the solution for uncoupled CPSCF equation, where the orbital Hessian is approximated with

<a id="Ch12.E6"></a>

$$
H_{ai,bj}=2(\epsilon_{a}-\epsilon_{i})\delta_{ij}\delta_{ab}. \tag{12.6}
$$

With this approximation, the orbital Hessian is easily inverted, and the fragment response matrices are simply

<a id="Ch12.E7"></a>

$$
\left(\Delta_{\mu}^{\text{uFERF}}\right)_{ai}=\frac{(M_{\mu})_{ai}}{\epsilon_{a}-\epsilon_{i}}. \tag{12.7}
$$

Benchmark calculations on the S22, S66 and Ionic43 datasets shows that the POL energy is hardly changed using uFERFs, while a general 5-10 times speedup for FERF creation and 20% average speedup for the whole EDA calculation is achieved. In addition, the importance of monopole uFERFs (response to scaled nuclear charges) for intermolecular interactions is recognized for strong ion-neutral interactions. Therefore, it is recommended to use MDQ-uFERFs for the calculation of POL energy in ALMO-EDA calculations.

### `CHILD_MP`

> **Compute FERFs for fragments and use them as the basis for SCF-MI calculations.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not compute FERFs (use the full AO span of each fragment).
>     * `TRUE`: Compute fragment FERFs.
> * **Recommendation**: Use FERFs to compute polarization energy when large basis sets are used. In an “EDA2” calculation, this $rem variable is set based on the given option automatically.

### `CHILD_MP_ORDERS`

> **The multipole orders included in the prepared FERFs. The last digit specifies how many multipoles to compute, and the digits in the front specify the multipole orders: 2: dipole (D); 3: quadrupole (Q); 4: octopole (O). Multipole order 1 is reserved for monopole FERFs which can be used to separate the effect of orbital contraction. 808 Levine D. S., Head-Gordon M. J. Phys. Chem. Lett. (2017) , 8 , pp. 1967 . Link**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `21`: D
>     * `232`: DQ
>     * `2343`: DQO
> * **Recommendation**: Use 232 (DQ) when FERF is needed.

### `FRAG_CPSCF_MAXITER`

> **The maximum number of iterations executed by the conjugate-gradient solver before switching to the MINRES algorithm. The maximum number of MINRES iterations is set to twice of the value of . Note that this rem variable is also used for the CPSCF equations involved in the adiabatic EDA (Sec. 12.7.3 ) and force decomposition analysis (Sec. 12.7.4 ) calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: Use the default

### `FRAG_CPSCF_CONV`

> **The convergence threshold for the CPSCF equation (using the RMS error of the residual vector)**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$: Convergence is reached when the RMS error is below $10^{-n}$
> * **Recommendation**: Use the default

### `EDA_UFERF`

> **Using uncoupled-FERFs (uFERFs) instead of FERFs**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Use uFERFs
>     * `FALSE`: Use FERFs
> * **Recommendation**: Use the default uFERFs, use FALSE when FERFs are desired.

???+ example "Example 12.13: Generalized SCF-MI calculation for the water dimer using nDQ FERFs."
    ```qchem
    $molecule
    0 1
    --
    0 1
    O  -1.551007  -0.114520   0.000000
    H  -1.934259   0.762503   0.000000
    H  -0.599677   0.040712   0.000000
    --
    0 1
    O   1.350625   0.111469   0.000000
    H   1.680398  -0.373741  -0.758561
    H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       METHOD            wb97x-v
       GEN_SCFMAN        true
       BASIS             6-31+G(d)
       GEN_SCFMAN        true
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       THRESH            14
       SCF_FINAL_PRINT   1
       EDA_UFERF         false
       FRGM_METHOD       stoll
       SCFMI_MODE        1 !nonortho gen scfmi
       CHILD_MP          true
       CHILD_MP_ORDERS   232 !DQ
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    ```
