---
title: "4.9.3 Multiple SCF Solutions for Non-Orthogonal CI"
---

## 4.9.3 Multiple SCF Solutions for Non-Orthogonal CI

(July 4, 2026)

The solutions found through metadynamics often appear to be good approximations
to diabatic surfaces, where the electronic structure does not significantly
change with geometry. In situations where there are such multiple electronic
states close in energy, an adiabatic state may be produced by diagonalizing a
matrix of these states, *i.e.*, through a configuration interaction (CI)
procedure. As they are distinct solutions of the SCF equations, these states
are non-orthogonal (*i.e.* one cannot be constructed as a single determinant
made out of the orbitals of another), and so the CI is a little more
complicated and corresponds to a non-orthogonal CI (NOCI). More information on
NOCI can be found in Section [7.5](../ch07_excited/subsec_NOCI.md).

Version 5.2 of **Q-Chem** introduces a new NOCI package, **libnoci**, for locating
multiple SCF solutions and running NOCI calculations (see
Section [7.5.2](../ch07_excited/subsec_LIBNOCI.md)), including a new implementation of SCF
metadynamics. The **libnoci** implementation of SCF metadynamics can be accessed
using USE_LIBNOCI = TRUE in combination with NOCI_DETGEN = 3.
In addition to the original SCF metadynamics features available in **Q-Chem**, this new implementation includes:

- •

An active space approach where orbital mixing and optimization
occurs only in a user-defined subset of orbitals.
- •

Full support for restricted, unrestricted and generalized orbital types, along
with complex (Hermitian) and holomorphic (non-Hermitian) orbitals; see Section [4.9.4](sec_HoloHF.md).

Multiple Hartree-Fock states of particular relevance for NOCI are often
related to varying orbital occupations in a dominant subset of molecular
orbitals. For example, important multiple solutions may correspond to excited
determinants whose orbitals have been individually relaxed at the SCF level, or
symmetry-broken states formed from strong mixing in a dominant active space.
**libnoci** allows multiple solutions to be identified by allowing orbital mixing
and relaxation only in a subset of orbitals defined using the *$active_orbitals* input section
By default, the multiple solutions located are then
subsequently optimized in the full orbital space, although this can be skipped
using SKIP_SCFMAN = TRUE.

Finally, **libnoci** introduces easier control over reading initial guesses from
previous calculations. Using the input NOCI_REFGEN = 1, all previous
solutions are read from file (if available), while a particular subset can be chosen
using SCF_READMINIMA.

???+ example "Example 4.29: Example of using the libnoci implementation of SCF metadynamics."
    ```qchem
    $molecule
       0 1
       H    0.0000000   0.0000000   0.0000000
       H    0.0000000   0.0000000   4.0000000
    $end
    
    $rem
       METHOD                     hf
       UNRESTRICTED               true
       BASIS                      sto-3g
       SCF_CONVERGENCE            10
       MAX_SCF_CYCLES             1000
       MOM_START                  1
       USE_LIBNOCI                true
       NOCI_DETGEN                3
       SCF_SAVEMINIMA             4
       SCF_MINFIND_RANDOMMIXING   30000
       SCF_MINFIND_MIXMETHOD      1
    $end
    ```

Active orbitals can be specified for SCF metadynamics in **libnoci**.
Indices for $\beta$ orbitals are offset by the number of $\alpha$ MOs, *i.e.*
the case selects $\alpha$ orbitals 1 and 2, and $\beta$ orbitals 1 and 2, with
a total of 10 $\alpha$ molecular orbitals (including occupied and virtual).

> > ```qchem
> > $active_orbitals
> >     1 2 11 12
> > $end
> > ```

The initial guess coefficients can also be read in as follows:

> > ```qchem
> > $scf_read
> >     1 2 4 ...
> > $end
> > ```
