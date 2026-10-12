---
title: "6.4.1 Algorithm"
---

## 6.4.1 Algorithm

(July 4, 2026)

Second-order Møller-Plesset theory[[957]](../bib_references/bib.md#bib998)
 (MP2) is probably the
simplest useful wave function-based electron correlation method. Revived in
the mid-1970s, it remains highly popular today, because it offers systematic
improvement in optimized geometries and other molecular properties relative to
Hartree-Fock (HF) theory.

 Indeed, in a recent comparative
study of small closed-shell molecules,[[548]](../bib_references/bib.md#bib565)
 MP2 outperformed
much more expensive singles and doubles coupled-cluster theory for such
properties! Relative to state-of-the-art Kohn-Sham density functional
theory (DFT) methods, which are the most economical methods to account for
electron correlation effects, MP2 has the advantage of properly incorporating
long-range dispersion forces. The principal weaknesses of MP2 theory are for
open shell systems, and other cases where the HF determinant is a poor starting point.

**Q-Chem** contains an efficient conventional semi-direct method to evaluate the
MP2 energy and gradient.[[545]](../bib_references/bib.md#bib558)
 These methods require $OVN$ memory
($O$, $V$, $N$ are the numbers of occupied, virtual and total orbitals,
respectively), and disk space which is bounded from above by $OVN^{2}/2$. The
latter can be reduced to $IVN^{2}/2$ by treating the occupied orbitals in batches
of size $I$, and re-evaluating the two-electron integrals $O/I$ times. This
approach is tractable on modern workstations for energy and gradient
calculations of at least 500 basis functions or so, or molecules of between 15
and 30 first row atoms, depending on the basis set size. The computational cost
increases between the 3rd and 5th power of the size of the molecule,
depending on which part of the calculation is time-dominant.

The algorithm and implementation in **Q-Chem** is improved over earlier
methods,[[542]](../bib_references/bib.md#bib552)
 particularly in the following areas:

- Uses pure functions, as opposed to Cartesians, for all fifth-order steps.
This leads to large computational savings for basis sets containing pure
functions.
- Customized loop unrolling for improved efficiency.
- The sort-less semi-direct method avoids a read and write operation
resulting in a large I/O savings.
- Reduction in disk and memory usage.
- No extra integral evaluation for gradient calculations.
- Full exploitation of frozen core approximation.

The implementation offers the user the following alternatives:

- Direct algorithm (energies only).
- Disk-based sort-less semi-direct algorithm (energies and gradients).
- Local occupied orbital method (energies only).

The semi-direct algorithm is the only choice for gradient calculations. It is
also normally the most efficient choice for energy calculations. There are two
classes of exceptions:

- If the amount of disk space available is not significantly larger than
the amount of memory available, then the direct algorithm is preferred.
- If the calculation involves a very large basis set, then the local
orbital method may be faster, because it performs the transformation in a
different order. It does not have the large memory requirement (no
$OVN$ array needed), and always evaluates the integrals four times.

There are three important options that should be wisely chosen by the user in
order to exploit the full efficiency of **Q-Chem**’s direct and semi-direct MP2
methods (as discussed above, the LOCAL_OCCUPIED method has different
requirements).

- MEM_STATIC: The value specified for this *$rem* variable must be
sufficient to permit efficient integral evaluation (10-80MB) and to hold
a large temporary array whose size is $OVN$, the product of the number of
occupied, virtual and total numbers of orbitals.
- N_FROZEN_CORE: The computational requirements for MP2 are
proportional to the number of occupied orbitals for some steps, and the
square of that number for other steps. Therefore the CPU time can be
significantly reduced if your job employs the frozen core approximation.
Additionally the memory and disk requirements are reduced when the frozen
core approximation is employed.
