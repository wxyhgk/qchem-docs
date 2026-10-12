---
title: "4.9.2 SCF Metadynamics"
---

## 4.9.2 SCF Metadynamics

(July 4, 2026)

As the SCF equations are non-linear in the electron density, there are in
theory very many solutions, *i.e.*, sets of orbitals where the energy is
stationary with respect to changes in the orbital subset. Most often sought
is the solution with globally minimal energy as this is a variational upper
bound to the true eigenfunction in this basis. The SCF methods available in
**Q-Chem** allow the user to converge upon an SCF solution, and (using
STABILITY_ANALYSIS) ensure it is a minimum, but there is no known
method of ensuring that the found solution is a global minimum; indeed in
systems with many low-lying energy levels the solution converged upon may vary
considerably with initial guess.

SCF metadynamics[[1355]](../bib_references/bib.md#bib1415)
 is a technique which can be used to locate
multiple SCF solutions, and thus gain some confidence that the calculation has
converged upon the global minimum. It works by searching out a solution to the
SCF equations. Once found, the solution is stored, and a biasing potential
added so as to avoid re-converging to the same solution. More formally, the
distance between two solutions, $w$ and $x$, can be expressed as
$d_{wx}^{2}=\langle{{}^{w}\!\Psi|^{w}\!\hat{\rho}-{{}^{x}}\!\hat{\rho}}|^{w}\!\Psi\rangle$, where ${}^{w}\!\Psi$ is a Slater determinant formed from the
orthonormal orbitals, ${}^{w}\!\phi_{i}$, of solution $w$, and ${}^{w}\!\hat{\rho}$ is
the one-particle density operator for ${}^{w}\!\Psi$. This definition is
equivalent to
$d_{wx}^{2}=N-{{}^{w}}\!P^{\mu\nu}S_{\nu\sigma}\cdot{{}^{x}}\!P^{\sigma\tau}S_{\tau\mu}.$
and is easily calculated. The function $d_{wx}^{2}$ is between zero and the
number of electrons, and can be taken as the distance between two solutions.
As an example, any singly-excited determinant (which will not in general be
another SCF solution) is a distance 1 away from the reference (unexcited)
determinant.

In a manner analogous to classical metadynamics, to bias against the set of
previously located solutions, $x$, we create a new Lagrangian,

<a id="A3.S8.EGx13"></a>

$$
\displaystyle\tilde{E}=E+\sum_{x}N_{x}e^{-\lambda_{x}d_{0x}^{2}} \tag{4.68}
$$

where $0$ represents the present density.
From this we may derive a new effective Fock matrix,

<a id="A3.S8.EGx14"></a>

$$
\displaystyle\tilde{F}_{\mu\nu}=F_{\mu\nu}+\sum_{x}{{}^{x}\!P}_{\mu\nu}N_{x}\lambda_{x}e^{-\lambda_{x}d_{0x}^{2}} \tag{4.69}
$$

This may be used with very little modification within a standard DIIS procedure
to locate multiple solutions. When close to a new solution, the biasing
potential is removed so the location of that solution is not affected by it.
If the calculation ends up re-converging to the same solution, $N_{x}$ and
$\lambda_{x}$ can be modified to avert this. Once a solution is found it is
added to the list of solutions, and the orbitals mixed to provide a new guess
for locating a different solution.

This process can be customized by the REM variables below. Both DIIS and GDM
methods can be used, but it is advisable to turn on MOM when using DIIS to
maintain the orbital ordering. Post-HF correlation methods can also be
applied. By default they will operate for the last solution located, but this
can be changed with the SCF_MINFIND_RUNCORR variable.

### `SCF_SAVEMINIMA`

> **Turn on SCF metadynamics and specify how many solutions to locate.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not use SCF metadynamics
>     * $n$: Attempt to find
>     * $n$: distinct SCF solutions.
> * **Recommendation**: Perform SCF Orbital metadynamics and attempt to locate $n$ different SCF solutions. Note that these may not all be minima. Many saddle points are often located. The last one located will be the one used in any post-SCF treatments. In systems where there are infinite point groups, this procedure cannot currently distinguish between spatial rotations of different densities, so will likely converge on these multiply.

### `SCF_READMINIMA`

> **Read in solutions from a previous SCF metadynamics calculation**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Read in
>     * $n$: previous solutions and attempt to locate them all. $-n$ Read in
>     * $n$: previous solutions, but only attempt to locate solution
>     * $n$: (not available in libnoci ).
> * **Recommendation**: This may not actually locate all solutions required and will probably locate others too. The SCF will also stop when the number of solutions specified in SCF_SAVEMINIMA are found. Solutions from other geometries may also be read in and used as starting orbitals. If a solution is found and matches one that is read in within SCF_MINFIND_READDISTTHRESH , its orbitals are saved in that position for any future calculations. The algorithm works by restarting from the orbitals and density of a the minimum it is attempting to find. After 10 failed restarts (defined by SCF_MINFIND_RESTARTSTEPS ), it moves to another previous minimum and attempts to locate that instead. If there are no minima to find, the restart does random mixing (with 10 times the normal random mixing parameter). Note that in libnoci , previous minima are read using NOCI_REFGEN = 1, whilst the exact solutions are specified as described in Section 4.9.3

### `SCF_MINFIND_WELLTHRESH`

> **Specify what SCF_MINFIND believes is the basin of a solution**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$
> * **Recommendation**: When the DIIS error is less than $10^{-n}$ , penalties are switched off to see whether it has converged to a new solution.

### `SCF_MINFIND_RESTARTSTEPS`

> **Restart with new orbitals if no minima have been found within this many steps**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * $n$: Restart after
>     * $n$: steps.
> * **Recommendation**: If the SCF calculation spends many steps not finding a solution, lowering this number may speed up solution-finding. If the system converges to solutions very slowly, then this number may need to be raised.

### `SCF_MINFIND_INCREASEFACTOR`

> **Controls how the height of the penalty function changes when repeatedly trapped at the same solution**
>
> * **Type**: `INTEGER`
> * **Default**: `10100 meaning 1.01`
> * **Options**:
>     * $abcde$: corresponding to $a.bcde$
> * **Recommendation**: If the algorithm converges to a solution which corresponds to a previously located solution, increase both the normalization N and the width lambda of the penalty function there. Then do a restart.

### `SCF_MINFIND_INITLAMBDA`

> **Control the initial width of the penalty function.**
>
> * **Type**: `INTEGER`
> * **Default**: `02000 meaning 2.000`
> * **Options**:
>     * $abcde$: corresponding to $ab.cde$
> * **Recommendation**: The initial inverse-width ( i.e. , the inverse-variance) of the Gaussian to place to fill solution’s well. Measured in electrons ${}^{(}-1)$ . Increasing this will repeatedly converging on the same solution.

### `SCF_MINFIND_INITNORM`

> **Control the initial height of the penalty function.**
>
> * **Type**: `INTEGER`
> * **Default**: `01000 meaning 1.000`
> * **Options**:
>     * $abcde$: corresponding to $ab.cde$
> * **Recommendation**: The initial normalization of the Gaussian to place to fill a well. Measured in hartrees.

### `SCF_MINFIND_RANDOMMIXING`

> **Control how to choose new orbitals after locating a solution**
>
> * **Type**: `INTEGER`
> * **Default**: `00200 meaning .02 radians`
> * **Options**:
>     * $abcde$: corresponding to $a.bcde$ radians
> * **Recommendation**: After locating an SCF solution, the orbitals are mixed randomly to move to a new position in orbital space. For each occupied and virtual orbital pair picked at random and rotate between them by a random angle between 0 and this. If this is negative then use exactly this number, e.g. , $-15708$ will almost exactly swap orbitals. Any number $<-15708$ will cause the orbitals to be swapped exactly.

### `SCF_MINFIND_NRANDOMMIXES`

> **Control how many random mixes to do to generate new orbitals**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$: Perform
>     * $n$: random mixes.
> * **Recommendation**: This is the number of occupied/virtual pairs to attempt to mix, per separate density ( i.e. , for unrestricted calculations both alpha and beta space will get this many rotations). If this is negative then only mix the highest 25% occupied and lowest 25% virtuals.

### `SCF_MINFIND_READDISTTHRESH`

> **The distance threshold at which to consider two solutions the same**
>
> * **Type**: `INTEGER`
> * **Default**: `00100 meaning 0.1`
> * **Options**:
>     * $abcde$: corresponding to $ab.cde$
> * **Recommendation**: The threshold to regard a minimum as the same as a read in minimum. Measured in electrons. If two minima are closer together than this, reduce the threshold to distinguish them.

### `SCF_MINFIND_MIXMETHOD`

> **Specify how to select orbitals for random mixing**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Random mixing: select from any orbital to any orbital.
>     * `1`: Active mixing: select based on energy, decaying with distance from the Fermi level.
>     * `2`: Active Alpha space mixing: select based on energy, decaying with distance from the Fermi level only in the alpha space.
> * **Recommendation**: Random mixing will often find very high energy solutions. If lower energy solutions are desired, use 1 or 2.

### `SCF_MINFIND_MIXENERGY`

> **Specify the active energy range when doing Active mixing**
>
> * **Type**: `INTEGER`
> * **Default**: `00200 meaning 00.200`
> * **Options**:
>     * $abcde$: corresponding to $ab.cde$
> * **Recommendation**: The standard deviation of the Gaussian distribution used to select the orbitals for mixing (centered on the Fermi level). Measured in Hartree. To find less-excited solutions, decrease this value

### `SCF_MINFIND_RUNCORR`

> **Run post-SCF correlated methods on multiple SCF solutions**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `If this is set`: $>0$ , then run correlation methods for all found SCF solutions.
> * **Recommendation**: Post-HF correlation methods should function correctly with excited SCF solutions, but their convergence is often much more difficult owing to intruder states.
