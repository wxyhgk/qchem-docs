---
title: "7.9.13 Charge Stabilization for EOM-DIP with Unstable References and Other Methods"
---

## 7.9.13 Charge Stabilization for EOM-DIP with Unstable References and Other Methods

(July 4, 2026)

The performance of EOM-DIP deteriorates when the reference state is unstable
with respect to electron detachment,[[740]](../bib_references/bib.md#bib773)
 which is usually
the case for dianion reference states that are employed to describe neutral diradicals by EOM-DIP.
These states are often characterized by occupied Hartree–Fock energy levels having positive (unbound) eigenvalues,
corresponding to a wave function that is not normalizable.
(These are essentially discretized continuum solutions,
represented crudely in a Gaussian basis set.

)
Similar problems are encountered by all excited-state methods when
dealing with excited states lying above ionization or electron-detachment thresholds.

To remedy this problem, one can employ charge stabilization methods.[[740]](../bib_references/bib.md#bib773)

This approach, which can be used with any electronic structure method, introduces an
additional Coulomb potential to stabilize the wave function. There are three ways to do this:

- Scaling the nuclear charges, which is accomplished using the *$rem* variable SCALE_NUCLEAR_CHARGE.
- User-defined nuclear charges, activated by setting CHARGE_STABILIZE = TRUE and specifying
the new charges in a *$nuclear_charges* input section. The format for the *$nuclear_charges* input section is the
same as that of the *$van_der_waals* section, which is described in Section [11.2.10](../ch11_env/subsec_LD.md).
- Adding a “charged cage”, *i.e.*, an array of point charges around the molecule, which is activated by setting
ADD_CHARGED_CAGE = TRUE.
Two types of cages (spherical and dodecahedral) are available; the
shape, radius, number of points, and total charge of the cage are set by the user.

In the case of EOM methods, a perturbative estimate of the effect of the external Coulomb potential on the EOM energy
will be computed when target state densities are calculated, *e.g.*, when CC_EOM_PROP = TRUE.
Charge stabilization techniques can be used with other methods including ground state DFT (in order to describe
meta-stable ground states) and TDDFT (to improve the description of auto-ionizing resonances). For methods other
than EOM, no special correction is applied and one simply obtains the “ordinary” electronic structure but with
modified nuclear charges or in the presence of additional point charges. In such cases, it may be advisable to perform
several calculations with differing values of the nuclear charges in order to extrapolate the results to the true atomic
numbers.

 In so doing, only calculations for which
stabilization is sufficient to obtain a bound-state wave function should be used in the extrapolation.
Calculations that result in unbound occupied levels (SCF eigenvalues $\epsilon_{i}>0$)
should not be taken seriously, as they represent orthogonalized discretized continuum states and not true bound-state
solutions. Results from such solutions will vary strongly with respect to the choice of basis set but in ways that are
essentially meaningless.

The following descriptions and examples illustrate all three mechanisms of charge stabilization.

### `SCALE_NUCLEAR_CHARGE`

> **Scale the nuclear charges.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$: scale the nuclear charges in a way that adds a charge of $N$ /100 (in a.u.)
> * **Recommendation**: For EOM methods a perturbative correction can be added in conjunction with this option (as noted above), but for other electronic structure methods once simply gets a traditional calculation but with modified nuclear charges.

???+ example "Example 7.89: EOM-DIP excitation energies and properties using a charged cage for stabilization."
    ```qchem
    $molecule
      -2 1
       C   0.000000     0.000000     0.106788
       H  -0.989216     0.000000    -0.320363
       H   0.989216     0.000000    -0.320363
    $end
    
    $rem
       METHOD                     eom-ccsd
       BASIS                      6-311g(d,p)
       SCF_ALGORITHM              diis_gdm
       SCF_CONVERGENCE            8
       CC_T_CONV                  8
       EOM_DAVIDSON_CONVERGENCE   5
       CC_SYMMETRY                false
       DIP_SINGLETS               [1]    ! Compute one EOM-DIP singlet state
       DIP_TRIPLETS               [1]    ! Compute one EOM-DIP triplet state
       CC_EOM_PROP                true   ! Compute excited state properties
       ADD_CHARGED_CAGE           2      ! 1 for dodecahedral, 2 for spherical
       CAGE_RADIUS                225    ! Radius = 2.25 A
       CAGE_CHARGE                500    ! Total Charge = 5 a.u.
       CAGE_POINTS                100    ! Place 100 point charges
       INTEGRAL_SYMMETRY          false ! charged cage may violate point-group symmetry
    $end
    ```

???+ example "Example 7.90: Stabilization of SO ${}_{4}^{2-}$ by modified nuclear charges."
    ```qchem
    $comment
       Charge stabilization of an unbound anion (sulfate) by changing nuclear charge
       for S.  Format for nuclear charges section is same as van_der_waals section.
    $end
    
    $molecule
       -2 1
       S     0.0000000000    0.0000000000    0.0000000000
       O     0.8960432838    0.8960432838    0.8960432838
       O    -0.8960432838   -0.8960432838    0.8960432838
       O    -0.8960432838    0.8960432838   -0.8960432838
       O     0.8960432838   -0.8960432838   -0.8960432838
    $end
    
    $rem
       METHOD             mp2
       BASIS              aug-cc-pvdz
       CHARGE_STABILIZE   1
    $end
    
    $nuclear_charges
       1
       16 16.5
    $end
    ```
