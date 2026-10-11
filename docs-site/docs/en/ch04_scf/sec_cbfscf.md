---
title: "4.9.5 Non-Hermitian SCF with complex basis functions"
---

## 4.9.5 Non-Hermitian SCF with complex basis functions

(July 4, 2026)

Metastable electronic states can be characterized by a complex Siegert energy,

<a id="Ch4.E74"></a>
$$
E=E_{r}-i\Gamma/2, \tag{4.74}
$$

where the width, $\Gamma$, is proportional to the inverse lifetime of the state: $\Gamma=\hbar/\tau$. Complex coordinate methods aim to compute this complex energy as an eigenvalue of an effective non-Hermitian Hamiltonian. One such method is the method of complex basis functions (CBFs) where a basis of Gaussians with complex exponents is used in conjunction with a symmetric (not complex-conjugated) inner product to effictively produce a finite-basis representation of a non-Hermitian operators.[[931]](../bib_references/bib.md#bib970)
 In cases, such as temporary anions, where the decay channel is of 1-electron character, a mean-field theory can provide approximate Siegert energies for a many-electron system.

The simplest such approximation is the static-exchange approximation. In this approximation the Siegert energies of an ($N+1$)-electron state are computed by diagonalizing a Fock operator computed from the density of an $N$-electron state.[[1457]](../bib_references/bib.md#bib1525)
 This approximation neglects orbital relaxation effects which can be included by a non-Hermitian self-consistent-field (NH-SCF) procedure.[[931]](../bib_references/bib.md#bib970)
 In practice the NH-SCF energy functional is the same as the Holomorphic Hartree-Fock energy functional (Eq. [4.70](sec_HoloHF.md#eq:HoloHFEnergy)), though it is used for a different purpose. Both static-exchange and NH-SCF theories using complex basis functions (CBFs) are available in **Q-Chem**. Specification of the complex basis set is described in Section [8.7](../ch08_basis/sect_zbas.md).

COMPLEX_EXPONENTS

### `COMPLEX_EXPONENTS`

> **Enable a non-Hermitian calculation with CBFs.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform a non-Hermitian calculation with CBFs
> * **Recommendation**: Set to TRUE if a non-Hermitian calculation using CBFs is desired.

COMPLEX_SPIN_STATE

### `COMPLEX_SPIN_STATE`

> **Spin state for non-Hermitian calculation**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $2S+1$
>     * A state of spin
>     * $S$
> * **Recommendation**: None

COMPLEX_N_ELECTRON

### `COMPLEX_N_ELECTRON`

> **Add electrons for non-Hermitian calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Perform the non-Hermitian calculation on an
>     * $N+n$
>     * electron system
> * **Recommendation**: None

COMPLEX_STATIC_EXCHANGE

### `COMPLEX_STATIC_EXCHANGE`

> **Perform a CBF static-exchange calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform a static exchange calculation
>     * FALSE
>     * Do not perform a static exchange calculation
> * **Recommendation**: Set to TRUE if a static-exchange calculation is desired.

COMPLEX_SCF

### `COMPLEX_SCF`

> **Perform a non-Hermitian SCF calculation with CBFs**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not perform an NH-SCF calculation
>     * 1
>     * Perform a restricted NH-SCF calculation
>     * 2
>     * Perform an unrestricted NH-SCF calculation
>     * 3
>     * Perform a restricted, open-shell NH-SCF calculation
> * **Recommendation**: None

COMPLEX_METSCF

### `COMPLEX_METSCF`

> **Specify the NH-SCF solver**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * Roothaan iterations
>     * 1
>     * DIIS
>     * 3
>     * ADIIS
>     * 21
>     * Newton-MINRES
> * **Recommendation**: Use the default (DIIS).

COMPLEX_SCF_GUESS

### `COMPLEX_SCF_GUESS`

> **Specify the NH-SCF guess**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use a guess from a static-exchange calculation
>     * 1
>     * Read real-basis MO coefficients
>     * 2
>     * Read real-basis density matrix
>     * 1000
>     * Read guess from a previous calculation
> * **Recommendation**: Use a guess from a static exchange calculation. Note that for temporary anions, this requires the specification of COMPLEX_TARGET .

COMPLEX_TARGET

### `COMPLEX_TARGET`

> **Specify the orbital index to be occupied for a temporary anion**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Orbital index (starting at zero) for the additional electron
> * **Recommendation**: $n$ should always be greater than $N_{\text{occ}}-1$ .
