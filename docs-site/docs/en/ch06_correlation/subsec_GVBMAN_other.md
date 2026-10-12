---
title: "6.19.5 Other GVBMAN Methods and Options"
---

## 6.19.5 Other GVBMAN Methods and Options

(July 4, 2026)

In **Q-Chem**, the unrestricted and restricted GVB methods are implemented with a
resolution of the identity (RI) algorithm that makes them computationally very
efficient.[[1392]](../bib_references/bib.md#bib1454)
 They can be applied to systems
with more than 100 active electrons, and both energies and analytical gradients
are available. These methods are requested via the standard CORRELATION
keyword. If AUX_BASIS is not specified, the calculation uses
four-center two-electron integrals by default. Much faster auxiliary basis
algorithms (see Section [6.6](topic_rimp2.md) for an introduction), which are used for the
correlation energy (not the reference SCF energy), can be enabled by specifying
a valid string for AUX_BASIS. The example below illustrates a simple IP calculation.

???+ example "Example 6.54: Imperfect pairing with auxiliary basis set for geometry optimization."
    ```qchem
    $molecule
       0 1
       H
       F   1   1.0
    $end
    
    $rem
       JOBTYPE       opt
       CORRELATION   gvb_ip
       BASIS         cc-pVDZ
       AUX_BASIS     rimp2-cc-pVDZ
    $end
    ```

If further improvement in the orbitals are needed, the GVB_SIP, GVB_DIP, OP, NP
and 2P models are also included.[[774]](../bib_references/bib.md#bib807)
 The GVB_SIP model
includes all the amplitudes of GVB_IP plus a set of quadratic
amplitudes the represent the single ionization of a pair. The GVB_DIP
model includes the GVB_SIP models amplitudes and the doubly ionized
pairing amplitudes which are analogous to the correlation of the occupied
electrons of the $i$th pair exciting into the virtual orbitals of
the $j$th pair. These two models have the implementation limit of no
analytic orbital gradient, meaning that a slow finite differences calculation
must be performed to optimize their orbitals, or they must be computed using
orbitals from a different method. The 2P model is the same as the GVB_DIP model,
except it only allows the amplitudes to couple via integrals that span only two
pairs. This allows for a fast implementation of it’s analytic orbital gradient
and enables the optimization of it’s own orbitals. The OP method is like the
2P method except it removes the “direct”-like IP amplitudes and all of the
same-spin amplitudes. The NP model is the GVB_IP model with the DIP amplitudes.
This model is the one that works best with the symmetry breaking corrections
that will be discussed later. All GVB methods except GVB_SIP and
GVB_DIP have an analytic nuclear gradient implemented for both regular
and RI four-center two-electron integrals.

There are often considerable challenges in converging the orbital optimization
associated with these GVB-type calculations. The situation is somewhat
analogous to SCF calculations but more severe because there are more orbital
degrees of freedom that affect the energy (for instance, mixing occupied active
orbitals amongst each other, mixing active virtual orbitals with each other, mixing
core and active occupied, mixing active virtual and inactive virtual).
Furthermore, the energy changes associated with many of these new orbital
degrees of freedom are rather small and delicate. As a consequence, in cases
where the correlations are strong, these GVB-type jobs often require many more
iterations than the corresponding GDM calculations at the SCF level. This is a
reflection of the correlation model itself. To deal with convergence issues, a
number of REM values are available to customize the calculations, as listed below.

### `GVB_ORB_MAX_ITER`

> **Controls the number of orbital iterations allowed in GVB-CC calculations. Some jobs, particularly unrestricted PP jobs can require 500–1000 iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `256`
> * **Options**:
>     * User-defined number of iterations.
> * **Recommendation**: Default is typically adequate, but some jobs, particularly UPP jobs, can require 500–1000 iterations if converged tightly.

### `GVB_ORB_CONV`

> **The GVB-CC wave function is considered converged when the root-mean-square orbital gradient and orbital step sizes are less than $10^{-\mathrm{GVB\_ORB\_CONV}}$ . Adjust THRESH simultaneously.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: Use 6 for PP(2) jobs or geometry optimizations. Tighter convergence ( i.e. 7 or higher) cannot always be reliably achieved.

### `GVB_ORB_SCALE`

> **Scales the default orbital step size by $n$ /1000.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$: User-defined, 0–1000
> * **Recommendation**: Default is usually fine, but for some stretched geometries it can help with convergence to use smaller values.

### `GVB_AMP_SCALE`

> **Scales the default orbital amplitude iteration step size by $n$ /1000 for IP/RCC. PP amplitude equations are solved analytically, so this parameter does not affect PP.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$: User-defined, 0–1000
> * **Recommendation**: Default is usually fine, but in some highly-correlated systems it can help with convergence to use smaller values.

### `GVB_RESTART`

> **Restart a job from previously-converged GVB-CC orbitals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: Useful when trying to converge to the same GVB solution at slightly different geometries, for example.

### `GVB_REGULARIZE`

> **Coefficient for GVB_IP exchange type amplitude regularization to improve the convergence of the amplitude equations especially for spin-unrestricted amplitudes near dissociation. This is the leading coefficient for an amplitude dampening term ${-(c/10000)(e^{t_{ij}^{p}}-1)/(e^{1}-1)}$**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $c$
>     * `User-defined`
> * **Recommendation**: Should be increased if unrestricted amplitudes do not converge or converge slowly at dissociation. Set this to zero to remove all dynamically-valued amplitude regularization.

### `GVB_POWER`

> **Coefficient for GVB_IP exchange type amplitude regularization to improve the convergence of the amplitude equations especially for spin-unrestricted amplitudes near dissociation. This is the leading coefficient for an amplitude dampening term included in the energy denominator: -( $c$ /10000) $(e^{t_{ij}^{p}}-1)/(e^{1}-1)$**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $p$
>     * `User-defined`
> * **Recommendation**: Should be decreased if unrestricted amplitudes do not converge or converge slowly at dissociation, and should be kept even valued.

### `GVB_SHIFT`

> **Value for a statically valued energy shift in the energy denominator used to solve the coupled cluster amplitude equations, $n$ /10000.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: Default is fine, can be used in lieu of the dynamically valued amplitude regularization if it does not aid convergence.

Another issue that a user of these methods should be aware of is the fact that
there is a multiple minimum challenge associated with GVB calculations. In SCF
calculations it is sometimes possible to converge to more than one set of
orbitals that satisfy the SCF equations at a given geometry. The same problem
can arise in GVB calculations, and based on our experience to date, the problem
in fact is more commonly encountered in GVB calculations than in SCF
calculations. A user may therefore want to (or have to!) tinker with the
initial guess used for the calculations. One way is to set GVB_RESTART
= TRUE (see above), to replace the default initial guess (the converged SCF
orbitals which are then localized). Another way is to change the localized
orbitals that are used in the initial guess, which is controlled by the
GVB_LOCAL variable, described below. Sometimes different localization
criteria, and thus different initial guesses, lead to different converged
solutions. Using the new amplitude regularization keywords enables some control
over the solution GVB optimizes.[[773]](../bib_references/bib.md#bib806)
 A calculation can be
performed with amplitude regularization to find a desired solution, and then
the calculation can be rerun with GVB_RESTART = TRUE and the
regularization turned off to remove the energy penalty of regularization.

### `GVB_LOCAL`

> **Sets the localization scheme used in the initial guess wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `0`: No Localization
>     * `1`: Boys localized orbitals
>     * `2`: Pipek-Mezey orbitals
> * **Recommendation**: Different initial guesses can sometimes lead to different solutions. It can be helpful to try both to ensure the global minimum has been found.

### `GVB_DO_SANO`

> **Sets the scheme used in determining the active virtual orbitals in a Unrestricted-in-Active Pairs GVB calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `0`: No localization or Sano procedure
>     * `1`: Only localizes the active virtual orbitals
>     * `2`: Uses the Sano procedure
> * **Recommendation**: Different initial guesses can sometimes lead to different solutions. Disabling sometimes can aid in finding more non-local solutions for the orbitals.

Other *$rem* variables relevant to GVB calculations are given below. It is
possible to explicitly set the number of active electron pairs using the
GVB_N_PAIRS variable. The default is to make all valence electrons
active. Other reasonable choices are certainly possible. For instance all
electron pairs could be active ($n_{\mathrm{active}}=n_{\beta})$. Or
alternatively one could make only formal bonding electron pairs active
($n_{\mathrm{active}}=N_{\mathrm{STO-3G}}-n_{\alpha})$. Or in some cases, one might
want only the most reactive electron pair to be active ($n_{\mathrm{active}}=$1).
Clearly making physically appropriate choices for this variable is essential
for obtaining physically appropriate results!

### `GVB_N_PAIRS`

> **Alternative to CC_REST_OCC and CC_REST_VIR for setting active space size in GVB and valence coupled cluster methods.**
>
> * **Type**: `INTEGER`
> * **Default**: `PP active space (1 occ and 1 virt for each valence electron pair)`
> * **Options**:
>     * $n$: user-defined
> * **Recommendation**: Use the default unless one wants to study a special active space. When using small active spaces, it is important to ensure that the proper orbitals are incorporated in the active space. If not, use the $reorder_mo feature to adjust the SCF orbitals appropriately.

### `GVB_PRINT`

> **Controls the amount of information printed during a GVB-CC job.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: Should never need to go above 0 or 1.

### `GVB_TRUNC_OCC`

> **Controls how many pairs’ occupied orbitals are truncated from the GVB active space.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: This allows for asymmetric GVB active spaces removing the $n$ lowest energy occupied orbitals from the GVB active space while leaving their paired virtual orbitals in the active space. Only the models including the SIP and DIP amplitudes ( i.e. NP and 2P) benefit from this all other models this equivalent to just reducing the total number of pairs.

### `GVB_TRUNC_VIR`

> **Controls how many pairs’ virtual orbitals are truncated from the GVB active space.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: This allows for asymmetric GVB active spaces removing the $n$ highest energy occupied orbitals from the GVB active space while leaving their paired virtual orbitals in the active space. Only the models including the SIP and DIP amplitudes ( i.e. NP and 2P) benefit from this all other models this equivalent to just reducing the total number of pairs.

### `GVB_REORDER_PAIRS`

> **Tells the code how many GVB pairs to switch around.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: $0\leq n\leq 5$
> * **Recommendation**: This allows for the user to change the order the active pairs are placed in after the orbitals are read in or are guessed using localization and the Sano procedure. Up to 5 sequential pair swaps can be made, but it is best to leave this alone.

### `GVB_REORDER_1`

> **Tells the code which two pairs to swap first.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined XXXYYY
> * **Recommendation**: This is in the format of two 3-digit pair indices that tell the code to swap pair XXX with YYY, for example swapping pair 1 and 2 would get the input 001002. Must be specified in GVB_REORDER_PAIRS $\geq$ 1 .

### `GVB_REORDER_2`

> **Tells the code which two pairs to swap second.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined XXXYYY
> * **Recommendation**: This is in the format of two 3-digit pair indices that tell the code to swap pair XXX with YYY, for example swapping pair 1 and 2 would get the input 001002. Must be specified in GVB_REORDER_PAIRS $\geq$ 2 .

### `GVB_REORDER_3`

> **Tells the code which two pairs to swap third.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined XXXYYY
> * **Recommendation**: This is in the format of two 3-digit pair indices that tell the code to swap pair XXX with YYY, for example swapping pair 1 and 2 would get the input 001002. Must be specified in GVB_REORDER_PAIRS $\geq$ 3 .

### `GVB_REORDER_4`

> **Tells the code which two pairs to swap fourth.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined XXXYYY
> * **Recommendation**: This is in the format of two 3-digit pair indices that tell the code to swap pair XXX with YYY, for example swapping pair 1 and 2 would get the input 001002. Must be specified in GVB_REORDER_PAIRS $\geq$ 4 .

### `GVB_REORDER_5`

> **Tells the code which two pairs to swap fifth.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined XXXYYY
> * **Recommendation**: This is in the format of two 3-digit pair indices that tell the code to swap pair XXX with YYY, for example swapping pair 1 and 2 would get the input 001002. Must be specified in GVB_REORDER_PAIRS $\geq$ 5 .

It is known that symmetry breaking of the orbitals to favor localized solutions
over non-local solutions is an issue with GVB methods in general. A combined
coupled-cluster perturbation theory approach to solving symmetry breaking (SB)
using perturbation theory level double amplitudes that connect up to three
pairs has been examined in the literature,[[771]](../bib_references/bib.md#bib804)
 and
it seems to alleviate the SB problem to a large extent. It works in
conjunction with the GVB_IP, NP, and 2P levels of correlation for both
restricted and unrestricted wave functions (barring that there is no restricted
implementation of the 2P model, but setting GVB_DO_ROHF to the same number as
the number of pairs in the system is equivalent).

### `GVB_SYMFIX`

> **Should GVB use a symmetry breaking fix.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: no symmetry breaking fix
>     * `1`: symmetry breaking fix with virtual orbitals spanning the active space
>     * `2`: symmetry breaking fix with virtual orbitals spanning the whole virtual space
> * **Recommendation**: It is best to stick with type 1 to get a symmetry breaking correction with the best results coming from CORRELATION = NP and = 1.

### `GVB_SYMPEN`

> **Sets the pre-factor for the amplitude regularization term for the SB amplitudes.**
>
> * **Type**: `INTEGER`
> * **Default**: `160`
> * **Options**:
>     * $\gamma$
>     * `User-defined`
> * **Recommendation**: Sets the pre-factor for the amplitude regularization term for the SB amplitudes: $-(\gamma/1000)(e^{(c*100)*t^{2}}-1)$ .

### `GVB_SYMSCA`

> **Sets the weight for the amplitude regularization term for the SB amplitudes.**
>
> * **Type**: `INTEGER`
> * **Default**: `125`
> * **Options**:
>     * $c$
>     * `User-defined`
> * **Recommendation**: Sets the weight for the amplitude regularization term for the SB amplitudes: $-(\gamma/1000)(e^{(c*100)*t^{2}}-1)$ .

We have already mentioned a few issues associated with the GVB calculations:
the neglect of dynamic correlation [which can be remedied with PP(2)], the
convergence challenges and the multiple minimum issues. Another weakness of
these GVB methods is the occasional symmetry-breaking artifacts that are a
consequence of the limited number of retained pair correlation amplitudes. For
example, benzene in the PP approximation prefers D${}_{3h}$ symmetry over
D${}_{6h}$ by 3 kcal/mol (with a 2o distortion), while in IP, this difference
is reduced to 0.5 kcal/mol and less than 1o.[[1387]](../bib_references/bib.md#bib1449)

Likewise the allyl radical breaks symmetry in the unrestricted PP
model,[[110]](../bib_references/bib.md#bib98)
 although to a lesser extent than in restricted open
shell HF. Another occasional weakness is the limitation to the perfect pairing
active space, which is not necessarily appropriate for molecules with expanded
valence shells, such as in some transition metal compounds (*e.g.* expansion
from $4s3d$ into $4s4p3d$) or possibly hyper-valent molecules (expansion from
$3s3p$ into $3s3p3d$). The singlet strongly orthogonal geminal method (see the
next section) is capable of dealing with expanded valence shells and could be
used for such cases. The perfect pairing active space is satisfactory for most
organic and first row inorganic molecules.

To summarize, while these GVB methods are powerful and can yield much insight
when used properly, they do have enough pitfalls for not to be considered true
“black box” methods.
