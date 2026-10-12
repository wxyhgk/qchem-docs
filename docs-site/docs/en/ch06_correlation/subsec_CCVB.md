---
title: "6.19.3 Coupled Cluster Valence Bond (CCVB)"
---

## 6.19.3 Coupled Cluster Valence Bond (CCVB)

(July 4, 2026)

Cases where PP needs improvement include molecules with several strongly
correlated electron pairs that are all localized in the same region of space,
and therefore involve significant inter-pair, as well as intra-pair
correlations. For some systems of this type, Coupled Cluster Valence Bond
(CCVB) is an appropriate method.[[1274]](../bib_references/bib.md#bib1328)
 CCVB is designed
to qualitatively treat the breaking of covalent bonds. At the most basic
theoretical level, as a molecular system dissociates into a collection of
open-shell fragments, the energy should approach the sum of the ROHF energies
of the fragments. CCVB is able to reproduce this for a wide class of problems,
while maintaining proper spin symmetry. Along with this, CCVB’s main strength,
come many of the spatial symmetry breaking issues common to the GVB-CC methods.

Like the other methods discussed in this section, the leading contribution to
the CCVB wave function is the perfect pairing wave function, which is shown in
Eq. ([6.84](subsec_PP.md#eqn:PP)). One important difference is that CCVB uses the PP wave
function as a reference in the same way that other GVBMAN methods use a reference determinant.

The PP wave function is a product of simple, strongly orthogonal singlet
geminals. Ignoring normalization, two equivalent ways of displaying these
geminals are

<a id="A3.S8.EGx26"></a>

$$
\displaystyle(\phi_{i}\phi_{i}+t_{i}\phi_{i}^{*}\phi_{i}^{*})(\alpha\beta-\beta\alpha)\ \ \ (\text{Natural-orbital form}) \tag{6.85}
$$

where on the left and right we have the spatial part (involving $\phi$ and
$\chi$ orbitals) and the spin coupling, respectively. The VB-form orbitals are
non-orthogonal within a pair and are generally AO-like. The VB form is used in
CCVB and the NO form is used in the other GVBMAN methods. It turns out that
occupied UHF orbitals can also be rotated (without affecting the energy) into
the VB form (here the spin part would be just $\alpha\beta$), and as such we
store the CCVB orbital coefficients in the same way as is done in UHF (even
though no one spin is assigned to an orbital in CCVB).

These geminals are uncorrelated in the same way that molecular orbitals are
uncorrelated in a HF calculation. Hence, they are able to describe uncoupled,
or independent, single-bond-breaking processes, like that found in C${}_{2}$H${}_{6}$
$\rightarrow$ 2 CH${}_{3}$, but not coupled multiple-bond-breaking processes, such
as the dissociation of N${}_{2}$. In the latter system the three bonds may be
described by three singlet geminals, but this picture must somehow translate
into the coupling of two spin-quartet N atoms into an overall singlet, as found
at dissociation. To achieve this sort of thing in a GVB context, it is
necessary to correlate the geminals. The part of this correlation that is
essential to bond breaking is obtained by replacing clusters of singlet
geminals with triplet geminals, and re-coupling the triplets to an overall
singlet. A triplet geminal is obtained from a singlet by simply modifying the
spin component accordingly. We thus obtain the CCVB wave function:

<a id="A3.S8.EGx27"></a>

$$
\displaystyle|\Psi\rangle \tag{6.86}
$$

In this expansion, the summations go over the active singlet pairs, and the
indices shown in the labellings of the kets correspond to pairs that are being
coupled as described just above. We see that this wave function couples
clusters composed of even numbers of geminals. In addition, we see that the
amplitudes for clusters containing more than 2 geminals are parameterized by
the amplitudes for the 2-pair clusters. This approximation is important for
computational tractability, but actually is just one in a family of CCVB
methods: it is possible to include coupled clusters of odd numbers of pairs,
and also to introduce independent parameters for the higher-order amplitudes.
At present, only the simplest level is included in **Q-Chem**.

Older methods which attempt to describe substantially the same electron
correlation effects as CCVB are the IP[[1387]](../bib_references/bib.md#bib1449)
 and
RCC[[1390]](../bib_references/bib.md#bib1452)
 wave functions. In general CCVB should be used
preferentially. It turns out that CCVB relates to the GVB-IP model. In fact, if
we were to expand the CCVB wave function relative to a set of determinants, we
would see that for each pair of singlet pairs, CCVB contains only one of the
two pertinent GVB-IP doubles amplitudes. Hence, for CCVB the various
computational requirements and timings are very similar to those for GVB-IP.
The main difference between the two models lies in how the doubles amplitudes
are used to parameterize the quadruples, sextuples, etc., and this is what
allows CCVB to give correct energies at full bond dissociation.

A CCVB calculation is invoked by setting CORRELATION = CCVB. The
number of active singlet geminals must be specified by GVB_N_PAIRS.
After this, an initial guess is chosen. There are three main options for this,
specified by the following keyword

### `CCVB_GUESS`

> **Specifies the initial guess for CCVB calculations**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * `1`: Standard GVBMAN guess (orbital localization via GVB_LOCAL + Sano procedure).
>     * `2`: Use orbitals from previous GVBMAN calculation, along with SCF_GUESS = READ .
>     * `3`: Convert UHF orbitals into pairing VB form.
> * **Recommendation**: Option 1 is the most useful overall. The success of GVBMAN methods is often dependent on localized orbitals, and this guess shoots for these. Option 2 is useful for comparing results to other GVBMAN methods, or if other GVBMAN methods are able to obtain a desired result more efficiently. Option 3 can be useful for bond-breaking situations when a pertinent UHF solution has been found. It works best for small systems, or if the unrestriction is a local phenomenon within a larger molecule. If the unrestriction is non-local and the system is large, this guess will often produce a solution that is not the global minimum. Any UHF solution has a certain number of pairs that are unrestricted, and this will be output by the program. If GVB_N_PAIRS exceeds this number, the standard GVBMAN initial-guess procedure will be used to obtain a guess for the excess pairs

For potential energy surfaces, restarting from a previously computed CCVB
solution is recommended. This is invoked by GVB_RESTART = TRUE.
Whenever this is used, or any time orbitals are being read directly into CCVB
from another calculation, it is important to also set:

- SCF_GUESS = READ
- MP2_RESTART_NO_SCF = TRUE
- SCF_ALGORITHM = DIIS

This bypasses orthogonalization schemes used elsewhere within **Q-Chem** that are
likely to jumble the CCVB guess.

In addition to the parent CCVB method as discussed up until now, we have
included two related schemes for energy optimization, whose operation is
controlled by the following keyword:

### `CCVB_METHOD`

> **Optionally modifies the basic CCVB method**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Standard CCVB model
>     * `3`: Independent electron pair approximation (IEPA) to CCVB
>     * `4`: Variational PP (the CCVB reference energy)
> * **Recommendation**: Option 1 is generally recommended. Option 4 is useful for preconditioning, and for obtaining localized-orbital solutions, which may be used in subsequent calculations. It is also useful for cases in which the regular GVBMAN PP code becomes variationally unstable. Option 3 is a simple independent-amplitude approximation to CCVB. It avoids the cubic-scaling amplitude equations of CCVB, and also is able to reach the correct dissociation energy for any molecular system (unlike regular CCVB which does so only for cases in which UHF can reach a correct dissociate limit). However the IEPA approximation to CCVB is sometimes variationally unstable, which we have yet to observe in regular CCVB.

???+ example "Example 6.52: N ${}_{2}$ molecule in the intermediately dissociated region. In this case, SCF_ALGORITHM DIIS is necessary to obtain the symmetry unbroken RHF
solution, which itself is necessary to obtain the proper CCVB solution. Note
that many keywords general to GVBMAN are also used in CCVB."
    ```qchem
    $molecule
       0 1
       N  0  0  0
       N  0  0  2.0
    $end
    
    $rem
       UNRESTRICTED       = false
       BASIS              = 6-31g*
       EXCHANGE           = hf
       CORRELATION        = ccvb
       GVB_N_PAIRS        = 3
       CCVB_METHOD        = 1
       CCVB_GUESS         = 1
       GVB_LOCAL          = 2
       GVB_ORB_MAX_ITER   = 100000
       GVB_ORB_CONV       = 7
       GVB_RESTART        = false
       SCF_CONVERGENCE    = 10
       THRESH             = 14
       SCF_GUESS          = sad
       MP2_RESTART_NO_SCF = false
       SCF_ALGORITHM      = diis
       MAX_SCF_CYCLES     = 2000
       PRINT_ORBITALS     = true
       INTEGRAL_SYMMETRY    = false
       POINT_GROUP_SYMMETRY = false
    $end
    ```
