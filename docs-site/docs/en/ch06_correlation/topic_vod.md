---
title: "6.14.2 VOD and VOD(2) Methods"
---

## 6.14.2 VOD and VOD(2) Methods

(July 4, 2026)

The VOD method is the active space version of the OD method described earlier
in Section [6.12.8](topic_odcc.md). Both energies and gradients are available for VOD, so
structure optimization is possible. There are a few important comments to make
about the usefulness of VOD. First, it is a method that is capable of
accurately treating problems that fundamentally involve 2 active electrons in a
given local region of the molecule. It is therefore a good alternative for
describing single bond-breaking, or torsion around a double bond, or some
classes of diradicals. However it often performs poorly for problems where
there is more than one bond being broken in a local region, with the non
variational solutions being quite possible. For such problems the newer VQCCD
method is substantially more reliable.

Assuming that VOD is a valid zero order description for the electronic
structure, then a second-order correction, VOD(2), is available for energies
only. VOD(2) is a version of OD(2) generalized to valence active spaces. It
permits more accurate calculations of relative energies by accounting for
dynamical correlation.

???+ example "Example 6.45: Calculate the correlation energy of the water molecule with partially
stretched bonds, the VOD coupled-cluster active space method. This is a
relatively “easy” job to converge, and may be contrasted with the next
example, which is not easy to converge. The orbitals are restricted."
    ```qchem
    $molecule
      0  1
      O
      H  1  r
      H  1  r  2  a
    
      r =   1.5
      a = 104.5
    $end
    
    $rem
       METHOD        vod
       BASIS         6-31G
    $end
    ```

???+ example "Example 6.46: The water molecule with highly stretched bonds, calculated via the VOD
coupled-cluster active space method. This is a “difficult”
job to converge. The convergence options shown permitted the job to converge
after some experimentation (thanks due to Ed Byrd for this!). The difficulty of
converging this job should be contrasted with the previous example where the
bonds were less stretched."
    ```qchem
    $molecule
       0  1
       O
       H  1  r
       H  1  r  2  a
    
       r =   3.0
       a = 104.5
    $end
    
    $rem
       METHOD                vod
       BASIS                 6-31G
       SCF_CONVERGENCE       9
       THRESH                12
       CC_PRECONV_T2Z        50
       CC_PRECONV_T2Z_EACH   50
       CC_DOV_THRESH         7500
       CC_THETA_STEPSIZE     3200
       CC_DIIS_START         75
    $end
    ```
