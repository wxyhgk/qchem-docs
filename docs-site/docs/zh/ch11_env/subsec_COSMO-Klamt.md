---
title: "11.2.8 COSMO"
---

## 11.2.8 COSMO

(July 4, 2026)

According to Table [11.3](topic_pcm-em.md#table:K-matrix), COSMO and C-PCM appear to differ only
in the dielectric screening factor, $f_{\varepsilon}$ in
Eq. ([11.3](topic_pcm-em.md#eq:f_epsilon)). Indeed, surface charges in either model are computed according to

<a id="eq:C-PCM"></a>
$$
\mathbf{q}=-f_{\varepsilon}\mathbf{S}^{-1}\mathbf{v}\;. \tag{11.24}
$$

As discussed in Section [11.2.4](subsec_PCM_job_control.md), the user can choose between various values of
$f_{\varepsilon}$, including the original value
$f_{\varepsilon}=(\varepsilon-1)/(\varepsilon+1/2)$ that was suggested by Klamt and co-workers,[[692]](../bib_references/bib.md#bib721)

or else $f_{\varepsilon}=(\varepsilon-1)/\varepsilon$ as is typically used in C-PCM
calculations.[[1375]](../bib_references/bib.md#bib1436)
. More importantly,
however, COSMO differs from C-PCM in that the former includes an *ad hoc* correction for
outlying charge that goes beyond Eq. ([11.24](#eq:C-PCM)), whereas C-PCM consists
of nothing more than induced surface charges computed (self-consistently)
according to Eq. ([11.24](#eq:C-PCM)). This correction, which is common to many implementations of
COSMO,[[569]](../bib_references/bib.md#bib580)
 involves the use of two separate solute cavities. It is worth noting that
Eq. ([11.24](#eq:C-PCM)) was later shown to *implicitly* include an outlying charge correction,[[244]](../bib_references/bib.md#bib244)

by virtue of the fact that it is derivable from the SS(V)PE model,[[755]](../bib_references/bib.md#bib788)
 and
the latter was developed specifically with an eye towards the treatment of outlying charge. As such, there is little
theoretical justification for the additional *explicit* correction for outlying charge, despite its success in
practice.[[694]](../bib_references/bib.md#bib726)
 See Ref. [[569]](../bib_references/bib.md#bib580)
 for a discussion of these issues.

In any case, the nature of the *a posteriori* correction for the outlying charge proceeds as follows.
Upon solution of Eq. ([11.24](#eq:C-PCM)), the outlying charge correction in
COSMO[[692]](../bib_references/bib.md#bib721)
 is obtained by first defining a larger
cavity that is likely to contain essentially all of the solute’s electron
density; in practice, this typically means using atomic radii of $1.95R$,
where $R$ denotes the original atomic van der Waals radius that was used to
compute $\mathbf{q}$. (Note that unlike the PCMs described in
Sections [11.2.3](topic_pcm-em.md) and [11.2.4](subsec_PCM_job_control.md), where the atomic
radii have default values but a high degree of user-controllability is allowed,
the COSMO atomic radii are parameterized for this model and are fixed.) A new
set of charges, $\mathbf{q}^{\prime}=-f_{\varepsilon}(\mathbf{S}^{\prime})^{-1}\mathbf{v}^{\prime}$, is
then computed on this larger cavity surface, and the charges on the *original* cavity surface are adjusted to new values, $\mathbf{q}^{\prime\prime}=\mathbf{q}+\mathbf{q}^{\prime}$. Finally, a corrected electrostatic potential on the
original surface is computed according to $\mathbf{v}^{\prime\prime}=-f_{\varepsilon}\mathbf{S}\mathbf{q}^{\prime\prime}$. It is this potential that is used to
compute the solute–continuum electrostatic interaction (polarization energy),
$G_{\rm pol}=\tfrac{1}{2}\sum_{i}q_{i}^{\prime\prime}v_{i}^{\prime\prime}$. (For comparison, when the
C-PCM approach described in Section [11.2.3](topic_pcm-em.md) is used, the electrostatic
polarization energy is $G_{\rm pol}=\tfrac{1}{2}\sum_{i}q_{i}v_{i}$,
computed using the original surface charges $\mathbf{q}$ and surface
electrostatic potential $\mathbf{v}$.) With this outlying charge correction,
**Q-Chem**’s implementation of COSMO resembles the one in **Turbomole**.[[1203]](../bib_references/bib.md#bib1257)

A COSMO calculation is requested by setting SOLVENT_METHOD =
COSMO in the *$rem* section, in addition to normal job control
variables. The keyword **Dielectric** in the *$solvent* section is used
to set the solvent’s static dielectric constant, as described above for other
solvation models.
