---
title: "7.9.25 Active-Space EOM-CC(2,3): Tricks of the Trade (CCMAN only)"
---

## 7.9.25 Active-Space EOM-CC(2,3): Tricks of the Trade (CCMAN only)

(July 4, 2026)

Active space calculations are less demanding with respect to the size of a hard
drive. The main bottlenecks here are the memory usage and the CPU time. Both
arise due to the increased number of orbital blocks in the active space
calculations. In the current implementation, each block can contain from 0 up
to 16 orbitals of the same symmetry irrep, occupancy, and spin-symmetry. For
example, for a typical molecule of C${}_{\mathrm{2v}}$ symmetry, in a small/moderate
basis set (*e.g.*, TMM in 6-31G*), the number of blocks for each index is:

> occupied: $(\alpha+\beta)\times(a_{1}+a_{2}+b_{1}+b_{2})=2\times 4=8$
> 
> 
> virtuals: $(\alpha+\beta)\times(2a_{1}+a_{2}+b_{1}+2b_{2})=2\times 6=12$
> 
> 
> (usually there are more than 16 $a_{1}$ and $b_{2}$ virtual orbitals).

In EOM-CCSD, the total number of blocks is $O^{2}V^{2}=8^{2}\times 12^{2}=9216$.
In EOM-CC(2,3) the number of blocks in the EOM part is $O^{3}V^{3}=8^{3}\times 12^{3}=884736$. In active space EOM-CC(2,3), additional fragmentation of blocks
occurs to distinguish between the restricted and active orbitals. For example,
if the active space includes occupied and virtual orbitals of all symmetry
irreps (this will be a very large active space), the number of occupied and
virtual blocks for each index is 16 and 20, respectively, and the total number
of blocks increases to $3.3\times 10^{7}$. Not all of the blocks contain real
information, some blocks are zero because of the spatial or spin-symmetry
requirements. For the C${}_{\mathrm{2v}}$ symmetry group, the number of non-zero
blocks is about 10–12 times less than the total number of blocks, *i.e.*,
$3\times 10^{6}$. This is the number of non-zero blocks in *one* vector.
Davidson diagonalization procedure requires (2*MAX_VECTORS + 2*NROOTS)
vectors, where MAX_VECTORS is the maximum number of vectors in the subspace,
and NROOTS is the number of the roots to solve for. Taking NROOTS = 2 and
MAX_VECTORS = 20, we obtain 44 vectors with the total number of non-zero blocks
being $1.3\times 10^{8}$.

In CCMAN implementation, each block is a logical unit of information. Along with
real data, which are kept on a hard drive at all the times except of their
direct usage, each non-zero block contains an auxiliary information about its
size, structure, relative position with respect to other blocks, location on a
hard drive, and so on. The auxiliary information about blocks is *always*
kept in memory. Currently, the approximate size of this auxiliary information
is about 400 bytes per block. It means, that in order to keep information about
one vector ($3\times 10^{6}$ blocks), 1.2 GB of memory is required! The information
about 44 vectors amounts 53 GB. Moreover, the huge number of blocks
significantly slows down the code.

To make the calculations of active space EOM-CC(2,3) feasible, we need to
reduce the total number of blocks. One way to do this is to reduce the symmetry
of the molecule to lower or C${}_{1}$ symmetry group (of course, this will result
in more expensive calculation). For example, lowering the symmetry group from
C${}_{\mathrm{2v}}$ to C${}_{\mathrm{s}}$ would results in reducing the total number of
blocks in active space EOM-CC(2,3) calculations in about $2^{6}=64$ times, and
the number of non-zero blocks in about 30 times (the relative portion of
non-zero blocks in C${}_{\mathrm{s}}$ symmetry group is smaller compared to that in
C${}_{\mathrm{2v}}$).

Alternatively, one may keep the MAX_VECTORS and NROOTS parameters of
Davidson’s diagonalization procedure as small as possible (this mainly concerns
the MAX_VECTORS parameter). For example, specifying MAX_VECTORS = 12 instead
of 20 would require 30% less memory.

One more trick concerns specifying the active space. In a desperate situation
of a severe lack of memory, should the two previous options fail, one can try
to modify (increase) the active space in such a way that the fragmentation of
active and restricted orbitals would be less. For example, if there is one
restricted occupied $b_{1}$ orbital and one active occupied $B_{1}$ orbital, adding
the restricted $b_{1}$ to the active space will reduce the number of blocks, by
the price of increasing the number of FLOPS. In principle, adding extra orbital
to the active space should increase the accuracy of calculations, however, a
special care should be taken about the (near) degenerate pairs of orbitals,
which should be handled in the same way, *i.e.*, both active or both restricted.
