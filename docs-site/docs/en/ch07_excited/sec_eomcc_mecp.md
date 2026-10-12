---
title: "7.9.28 Potential Energy Surface Crossing Minimization"
---

## 7.9.28 Potential Energy Surface Crossing Minimization

(July 4, 2026)

EOM-CCSD can also be used as the excited-state method to find minimum energy
crossing points (MECPs). See Section [9.8.3](../ch09_opt/sect_MECP.md) for more general
information about MECP calculations.

The potential energy surface crossing optimization procedure finds energy minima
of crossing seams. On the seam, the potential surfaces are degenerate in the
subspace perpendicular to the plane defined by two vectors: the gradient
difference

<a id="Ch7.E125"></a>

$$
{\rm\bf g}=\frac{\partial}{\partial{\rm\bf q}}(E_{1}-E_{2}) \tag{7.125}
$$

and the derivative coupling

<a id="Ch7.E126"></a>

$$
{\rm\bf h}=\left\langle\Psi_{1}\left|\frac{\partial{\rm\bf H}}{\partial{\rm\bf
q}}\right|\Psi_{2}\right\rangle \tag{7.126}
$$

At this time **Q-Chem** is unable to locate crossing minima for states which have
non-zero derivative coupling. Fortunately, this does not occur often. Minima
on the seams of conical intersections of states of different multiplicity can
be found as their derivative coupling is zero. Minima on the seams of
intersections of states of different point group symmetry can be located as
well.

To run a PES crossing minimization, CCSD and EOM-CCSD methods must be employed
for the ground and excited state calculations respectively.

!!! note "Note"
    MECP optimization is only available for methods with analytic gradients.
    Finite-difference evaluation of two gradients is not possible.


## 7.9.28.1 Job Control Options

!!! note "Note"
    When performing coupled-cluster-based MECP calculations, one must use
    the XOPT_STATE_1 and XOPT_STATE_2 keywords and not
    MECP_STATE1 and MECP_STATE2.


XOPT_STATE_1, XOPT_STATE_2

### `XOPT_STATE_1, XOPT_STATE_2`

> **Specify two electronic states the intersection of which will be searched.**
>
> * **Type**: `[INTEGER, INTEGER, INTEGER]`
> * **Default**: `No default value (the option must be specified to run this calculation)`
> * **Options**:
>     * `[spin, irrep, state]`: spin = 0 Addresses states with low spin, see also EE_SINGLETS or IP_STATES,EA_STATES. spin = 1 Addresses states with high spin, see also EE_TRIPLETS. irrep Specifies the irreducible representation to which the state belongs; for example, in the $C_{2v}$ point group, irreps are ordered 1, 2, 3, 4 for $A_{1}$ , $A_{2}$ , $B_{1}$ , and $B_{2}$ , respectively. state Specifies the state number within the irreducible representation, state = 1 means the lowest excited state, state = 2 is the second excited state, etc. . 0, 0, -1 Ground state.
> * **Recommendation**: Only intersections of states with different spin or symmetry can be calculated at this time.

!!! note "Note"
    The spin can only be specified when using closed-shell RHF references. In
    the case of open-shell references all states are treated together, see also
    EE_STATES. For example, in spin-flip calculations use spin = 0 regardless of what is
    the actual multiplicity of the target state.


### `XOPT_SEAM_ONLY`

> **Orders an intersection seam search only, no minimization is to be performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Find a point on the intersection seam and stop.
>     * `FALSE`: Perform a minimization of the intersection seam.
> * **Recommendation**: In systems with a large number of degrees of freedom it might be useful to locate the seam first by setting this option to TRUE and using that geometry as a starting point for the minimization.

## 7.9.28.2 Examples

???+ example "Example 7.164: Optimization of the intersection of Ã ${}^{1}$ B ${}_{2}$ and B̃ ${}^{1}$ A ${}_{2}$ states
of the N ${}_{3}^{+}$ ion at the EOM-EE-CCSD level."
    ```qchem
    $molecule
       1 1
       N1
       N2 N1 rnn
       N3 N2 rnn N1 annn
    
       rnn=1.46
       annn=70.0
    $end
    
    $rem
       JOBTYPE                opt
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]   C2v point group symmetry
       XOPT_STATE_1           [0,4,1]     1B2 low spin state
       XOPT_STATE_2           [0,2,2]     2A2 low spin state
       XOPT_SEAM_ONLY         true        Find the seam only
       GEOM_OPT_TOL_GRADIENT  100
    $end
    
    $opt
    CONSTRAINT                Set constraints on the N-N bond lengths
       stre  1  2  1.46
       stre  2  3  1.46
    ENDCONSTRAINT
    $end
    
    @@@
    
    $molecule
       READ
    $end
    
    $rem
       JOBTYPE                opt         Optimize the intersection seam
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]
       XOPT_STATE_1           [0,4,1]
       XOPT_STATE_2           [0,2,2]
       GEOM_OPT_TOL_GRADIENT  30
       GEOM_OPT_DRIVER        optimize
    $end
    ```

???+ example "Example 7.165: Optimization of the intersection of Ã ${}^{2}$ A ${}_{1}$ and B̃ ${}^{2}$ B ${}_{1}$ states
of the NO ${}_{2}$ molecule at the EOM-IP-CCSD level."
    ```qchem
    $molecule
       -1  1
       N1
       O2  N1  rno
       O3  N1  rno  O2  aono
    
       rno  = 1.3040
       aono = 106.7
    $end
    
    $rem
       JOBTYPE                opt         Optimize the intersection seam
       UNRESTRICTED           true
       METHOD                 eom-ccsd
       N_FROZEN_CORE          0
       BASIS                  6-31g
       IP_STATES              [1,0,1,0]   C2v point group symmetry
       EOM_FAKE_IPEA          1
       XOPT_STATE_1           [0,1,1]     1A1 low spin state
       XOPT_STATE_2           [0,3,1]     1B1 low spin state
       GEOM_OPT_TOL_GRADIENT  30          Tighten gradient tolerance
       CCMAN2                 false
    $END
    ```
