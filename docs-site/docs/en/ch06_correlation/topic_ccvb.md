---
title: "6.14.4 CCVB-SD"
---

## 6.14.4 CCVB-SD

(July 4, 2026)

Working with Prof. Head-Gordon at Berkeley, Dr. D. W. Small and Joonho Lee
have developed and implemented a novel single-reference coupled-cluster method
with singles and doubles, called CCVB-SD.[[1276]](../bib_references/bib.md#bib1330)
 CCVB-SD
improves upon a more crude model CCVB (Section [6.19.3](subsec_CCVB.md)) and can be
considered a simple modification to restricted CCSD (RCCSD). CCVB-SD inherits
good properties from CCVB and RCCSD; it is spin-pure, size-extensive, and
capable of breaking multiple bonds as long as only the valence space is
correlated. It is a full doubles model and thus scales $\mathcal{O}(N^{6})$.
However, its energy is invariant under rotations in occupied space and virtual
space, which makes it much more black-box than CCVB. Its energy function
follows

<a id="eq:ccvbsd"></a>

$$
E_{\mathrm{CCVB-SD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}}\right)\left|{\hat{H}}\right|\left(\exp\left({\hat{T}}\right)-\hat{\text{I}}_{\text{S}}\frac{\hat{Q}^{2}}{2}\right)\Phi_{0}}\right\rangle_{C} \tag{6.82}
$$

where $\hat{\text{I}}_{\text{S}}$ is a singlet projection operator and $\hat{Q}$
is a quintet doubles operator. Unlike QCCD, CCVB-SD improves the right
eigenfunction while leaving the left eigenfunction unchanged. The quintet term
in Eq. ([6.82](#eq:ccvbsd)) represents approximate connected quadruples which are
responsible for describing strong correlation. The cost of CCVB-SD is only
twice as expensive as RCCSD, and it is better suited for strong correlation
than QCCD/VQCCD in the sense that the method becomes exact at the dissociation
limits of most multiple bond breaking whereas QCCD does not except special
cases.

Although CCVB-SD can be used without the active space constraints, we recommend
that users use it with the valence active space in general. For benchmarking
purposes, using a minimal basis will automatically provide the valence space
correctly with frozen cores. Both the energy and nuclear gradients of CCVB-SD
are available through CCMAN2.

It should be noted that there is no orbital optimization implemented for
CCVB-SD at the moment. This means that using basis sets larger than minimal
basis requires choosing right valence orbitals to use. Therefore, we recommend
that users run GVB-PP (or CCVB) to obtain orbitals to begin with. Orbital
optimization (*i.e.* CCVB-OD) will soon be implemented and running CCVB-OD will
be much more black-box than CCVB-SD as it does not require selecting proper
valence space orbitals.

Furthermore, CCVB-SD can be applied to only closed-shell molecules at the
moment. The extension to open-shell molecules is under development.

???+ example "Example 6.47: A CCVB-SD force calculation of benzene in a minimal basis."
    ```qchem
    $comment
    CCVB-SD job for benzene computing energy+gradients.
    It will also print out natural orbital occupation numbers (NOONs)
    $end
    
    $molecule
       0 1
       C    0.000000    0.698200    0.000000
       C    0.000000   -0.698200    0.000000
       C    1.209318    1.396400    0.000000
       C    1.209318   -1.396400    0.000000
       C    2.418636    0.698200    0.000000
       C    2.418636   -0.698200    0.000000
       H   -0.931410    1.235950    0.000000
       H   -0.931410   -1.235950    0.000000
       H    1.209318    2.471900    0.000000
       H    1.209318   -2.471900    0.000000
       H    3.350046    1.235950    0.000000
       H    3.350046   -1.235950    0.000000
    $end
    
    $rem
       JOBTYPE           force
       BASIS             sto-3g
       METHOD            ccvbsd
       THRESH            14
       SCF_ALGORITHM     gdm
       SCF_CONVERGENCE   10
       CC_REF_PROP       true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    ```
