---
title: "7.2.3 CIS Methods with Extended Excitation Manifolds"
---

## 7.2.3 CIS Methods with Extended Excitation Manifolds

(July 4, 2026)

A variety of CIS-like methods have been proposed that add a limited number of double excitations to the
CIS excitation space,

 in order to overcome certain deficiencies of CIS without incurring the prohibitive
${\cal{O}}({N^{6}})$ cost of a method such as CISD or CCSD that includes the full complement of double excitations.
These “extended” CIS methods are discussed in this section, starting with the original excited CIS (XCIS) procedure of
Maurice and Head-Gordon.[[920]](../bib_references/bib.md#bib956)

## 7.2.3.1 Extended CIS (XCIS)

The motivation for XCIS stems
from the fact that ROCIS and UCIS are less effective for radicals than CIS is
for closed shell molecules. Using the attachment/detachment density
analysis procedure,[[538]](../bib_references/bib.md#bib555)

the failing of ROCIS and UCIS
methodologies for the nitromethyl radical was traced to the neglect of a
particular class of double substitution which involves the simultaneous
promotion of an $\alpha$ spin electron from the singly occupied orbital and the
promotion of a $\beta$ spin electron into the singly occupied orbital. The
spin-adapted configurations

<a id="eq611"></a>

$$
\left|{\tilde{\Psi}_{i}^{a}(1)}\right\rangle=\frac{1}{\sqrt{6}}\left(|\Psi_{\bar{i}}^{\bar{a}}\rangle-|\Psi_{i}^{a}\rangle\right)+\frac{2}{\sqrt{6}}|\Psi_{p\bar{i}}^{a\bar{p}}\rangle \tag{7.12}
$$

are of crucial importance. (Here, $a,b,c,\ldots$ are virtual orbitals;
$i,j,k,\ldots$ are occupied orbitals; and $p,q,r,\ldots$ are singly-occupied orbitals.)
It is quite likely that similar excitations are
also very significant in other radicals of interest.

The XCIS proposal, a more satisfactory generalization of CIS to open shell
molecules, is to simultaneously include a restricted class of double
substitutions similar to those in Eq. ([7.12](#eq611)). To illustrate this, consider
the resulting orbital spaces of an ROHF calculation: doubly occupied ($d$),
singly occupied ($s$) and virtual ($v$). From this starting point we can
distinguish three types of single excitations of the same multiplicity as the
ground state: $d\rightarrow s$, $s\rightarrow v$ and $d\rightarrow v$. Thus, the spin-adapted
ROCIS wave function is

<a id="eq612"></a>

$$
\left|{\Psi_{\mathrm{ROCIS}}}\right\rangle=\frac{1}{\sqrt{2}}\sum_{ia}^{dv}a_{i}^{a}\left(|\Psi_{i}^{a}\rangle+|\Psi_{\bar{i}}^{\bar{a}}\rangle\right)+\sum_{pa}^{sv}a_{p}^{a}|\Psi_{p}^{a}\rangle+\sum_{ip}^{ds}a_{\bar{i}}^{\bar{p}}|\Psi_{\bar{i}}^{\bar{p}}\rangle \tag{7.13}
$$

The extension of CIS theory to incorporate higher excitations maintains the
ROHF as the ground state reference and adds terms to the ROCIS wave function
similar to that of Eq. ([7.13](#eq612)), as well as those where the double
excitation occurs through different orbitals in the $\alpha$ and $\beta$ space:

<a id="eq613"></a>

$$
\begin{array}[]{r}\left|{\Psi_{\mathrm{XCIS}}}\right\rangle=\frac{1}{\sqrt{2}}{\displaystyle\sum_{ia}^{dv}}a_{i}^{a}\left(|\Psi_{i}^{a}\rangle+|\Psi_{\bar{i}}^{\bar{a}}\rangle\right)+{\displaystyle\sum_{pa}^{sv}}a_{p}^{a}|\Psi_{p}^{a}\rangle+{\displaystyle\sum_{ip}^{ds}}a_{\bar{i}}^{\bar{p}}|\Psi_{\bar{i}}^{\bar{p}}\rangle\\
+{\displaystyle\sum_{iap}^{dvs}}\tilde{a}_{i}^{a}(p)|\tilde{\Psi}_{i}^{a}(p)\rangle+{\displaystyle\sum_{ia,p\neq q}^{dv,ss}}a_{p\bar{i}}^{a\bar{q}}|\Psi_{p\bar{i}}^{a\bar{q}}\rangle\\
\end{array} \tag{7.14}
$$

XCIS is defined only from a restricted open shell Hartree-Fock ground state
reference, as it would be difficult to uniquely define singly occupied orbitals
in a UHF wave function. In addition, $\beta$ unoccupied orbitals, through which
the spin-flip double excitation proceeds, may not match the half-occupied
$\alpha$ orbitals in either character or even symmetry.

For molecules with closed shell ground states, both the HF ground and CIS
excited states emerge from diagonalization of the Hamiltonian in the space of
the HF reference and singly excited substituted configuration state functions.
The XCIS case is different because the restricted class of double excitations
included could mix with the ground state and lower its energy. This mixing is
avoided to maintain the size consistency of the ground state energy.

With the inclusion of the restricted set of doubles excitations in the excited
states, but not in the ground state, it could be expected that some fraction of
the correlation energy be recovered, resulting in anomalously low excited state
energies. However, the fraction of the total number of doubles excitations
included in the XCIS wave function is very small and those introduced cannot
account for the pair correlation of any pair of electrons. Thus, the XCIS
procedure can be considered one that neglects electron correlation.

The computational cost of XCIS is approximately four times greater than CIS and
ROCIS, and its accuracy for open shell molecules is generally comparable to
that of the CIS method for closed shell molecules. In general, it achieves
qualitative agreement with experiment. XCIS is available for doublet and
quartet excited states beginning from a doublet ROHF treatment of the ground
state, for excitation energies only.

???+ example "Example 7.5: An XCIS calculation of excited states of an unsaturated radical,
the phenyl radical, for which double substitutions make considerable
contributions to low-lying excited states."
    ```qchem
    $comment
       C6H5 phenyl radical C2v symmetry MP2(full)/6-31G* = -230.7777459
    $end
    
    $molecule
       0  2
       c1
       x1  c1  1.0
       c2  c1  rc2  x1  90.0
       x2  c2  1.0  c1  90.0  x1    0.0
       c3  c1  rc3  x1  90.0  c2    tc3
       c4  c1  rc3  x1  90.0  c2   -tc3
       c5  c3  rc5  c1   ac5  x1  -90.0
       c6  c4  rc5  c1   ac5  x1   90.0
       h1  c2  rh1  x2  90.0  c1  180.0
       h2  c3  rh2  c1   ah2  x1   90.0
       h3  c4  rh2  c1   ah2  x1  -90.0
       h4  c5  rh4  c3   ah4  c1  180.0
       h5  c6  rh4  c4   ah4  c1  180.0
    
       rh1  =    1.08574
       rh2  =    1.08534
       rc2  =    2.67299
       rc3  =    1.35450
       rh4  =    1.08722
       rc5  =    1.37290
       tc3  =   62.85
       ah2  =  122.16
       ah4  =  119.52
       ac5  =  116.45
    $end
    
    $rem
       BASIS            =  6-31+G*
       EXCHANGE         =  hf
       MEM_STATIC       =  80
       INTSBUFFERSIZE   =  15000000
       SCF_CONVERGENCE  =  8
       CIS_N_ROOTS      =  5
       XCIS             =  true
    $end
    ```

## 7.2.3.2 Spin-Flip Extended CIS (SF-XCIS)

Spin-flip extended CIS (SF-XCIS)[[202]](../bib_references/bib.md#bib199)
 is a
spin-complete extension of the spin-flip single excitation configuration
interaction (SF-CIS) method.[[727]](../bib_references/bib.md#bib758)

The method includes all configurations in which no more
than one virtual level of the high spin triplet reference
becomes occupied and no more than one doubly occupied level becomes vacant.

SF-XCIS is defined only from a restricted open shell Hartree-Fock triplet
ground state reference. The final SF-XCIS wave functions correspond to
spin-pure $M_{S}=0$ (singlet or triplet) states. The fully balanced treatment of
the half-occupied reference orbitals makes it very suitable for applications
with two strongly correlated electrons, such as single bond dissociation,
systems with important diradical character or the study of excited states with
significant double excitation character.

The computational cost of SF-XCIS scales in the same way with molecule size as
CIS itself, with a pre-factor 13 times larger.

???+ example "Example 7.6: A SF-XCIS calculation of ground and excited states of trimethylenemethane
(TMM) diradical, for which double substitutions make considerable
contributions to low-lying excited states."
    ```qchem
    $molecule
       0 3
       C
       C 1 CC1
       C 1 CC2   2 A2
       C 1 CC2   2 A2    3 180.0
       H 2 C2H   1 C2CH  3 0.0
       H 2 C2H   1 C2CH  4 0.0
       H 3 C3Hu  1 C3CHu 2 0.0
       H 3 C3Hd  1 C3CHd 4 0.0
       H 4 C3Hu  1 C3CHu 2 0.0
       H 4 C3Hd  1 C3CHd 3 0.0
    
       CC1    = 1.35
       CC2    = 1.47
       C2H    = 1.083
       C3Hu   = 1.08
       C3Hd   = 1.08
       C2CH   = 121.2
       C3CHu  = 120.3
       C3CHd  = 121.3
       A2     = 121.0
    $end
    
    $rem
      UNRESTRICTED    = false   SF-XCIS runs from ROHF triplet reference
      EXCHANGE        = HF
      BASIS           = 6-31G*
      SCF_CONVERGENCE = 10
      SCF_ALGORITHM   = DM
      MAX_SCF_CYCLES  = 100
      SPIN_FLIP_XCIS  = true    Do SF-XCIS
      CIS_N_ROOTS     = 3
      CIS_SINGLETS    = true    Do singlets
      CIS_TRIPLETS    = true    Do triplets
    $end
    ```

## 7.2.3.3 Spin-Adapted Spin-Flip CIS

Spin-adapted spin-flip CIS (SA-SF-CIS)[[1549]](../bib_references/bib.md#bib1615)
 is a spin-complete
extension of the spin-flip single excitation configuration interaction (SF-CIS)
method.[[727]](../bib_references/bib.md#bib758)
 Unlike SF-XCIS, SA-SF-CIS only includes the minimal
set of electronic configurations needed to remove the spin contamination in
the conventional SF-CIS method. The target SA-SF-CIS states have spin
eigenvalues one less than the reference ROHF state, *i.e.*, if singlet states ($S=0$) are targeted then the reference
state should be a triplet ($S=1$), or if doublet states ($S=1/2$) are targeted then the reference state should be a
quartet ($S=3/2$). The SA-SF-CIS approach uses a tensor equation-of-motion formalism,[[1185]](../bib_references/bib.md#bib1239)

such that the dimension of the CI vectors in SA-SF-CIS remains exactly the same as that in conventional
SF-CIS.[[1549]](../bib_references/bib.md#bib1615)

A DFT correction to SA-SF-CIS (*i.e.*, SA-SF-TDDFT) can be added; see Section [7.3.4](sect_sftddft.md).
As with other SF-TDDFT methods,
the BH&HLYP functional has become something of a *de facto* standard
choice.[[1550]](../bib_references/bib.md#bib1617)

This functional is an adequate choice for many ground-state problems also.[[484]](../bib_references/bib.md#bib496)

???+ example "Example 7.7: An SA-SF-DFT calculation of singlet ground and excited states of ethylene."
    ```qchem
    $molecule
    0 3
     C
     C    1    B1
     H    1    B2    2    A1
     H    1    B3    2    A2    3    D1
     H    2    B4    1    A3    3    D2
     H    2    B5    1    A4    3    D3
    
       B1       1.32808942
       B2       1.08687297
       B3       1.08687297
       B4       1.08687297
       B5       1.08687297
       A1     121.62604150
       A2     121.62604150
       A3     121.62604150
       A4     121.62604150
       D1     180.00000000
       D2       0.00000000
       D3     180.00000000
    $end
    
    $rem
       EXCHANGE       bhhlyp
       BASIS          cc-pvtz
       BASIS2         sto-3g
       UNRESTRICTED   false
       CIS_N_ROOTS    5
       SASF_CIS       1
       CIS_TRIPLETS   false
    $end
    ```
