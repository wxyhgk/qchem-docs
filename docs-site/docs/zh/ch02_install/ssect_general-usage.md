---
title: "2.2.1 General Usage"
---

## 2.2.1 General Usage

(July 4, 2026)

Once installation is complete, and any necessary adjustments are made to the
user account, the user is now able to run **Q-Chem**. There are several ways to invoke **Q-Chem**:

1. 1.

**IQmol** offers a fully integrated graphical interface for the **Q-Chem**
package and includes a sophisticated input generator with contextual help
which is able to guide you through the many **Q-Chem** options available. It
also provides a molecular builder, job submission and monitoring tools, and
is able to visualize molecular orbitals, densities and vibrational frequencies.
For the latest version and download/installation instructions, please
see the **IQmol** homepage (`http://www.iqmol.org`).
2. 2.

*qchem* command line shell script. The simple format for command line execution
is given below. The remainder of this manual covers the creation of input files in detail.
3. 3.

Via a third-party graphical user interface (GUI). The two most popular ones are:

- •

A general web-based interface for electronic structure software, **WebMO**

(`www.webmo.net`).
- •

Wavefunction’s **Spartan** user interface on some platforms. Contact Wavefunction, Inc. 

(`www.wavefun.com`) or **Q-Chem** for full details of current availability.

Using the **Q-Chem** command line shell script (*qchem*) is straightforward
provided **Q-Chem** has been correctly installed on your machine and the
necessary environment variables have been set in your `.cshrc`,
`.profile`, or equivalent login file. If done correctly, the necessary
changes will have been made to the `$PATH` variable automatically on
login so that **Q-Chem** can be invoked from your working directory.

The *qchem* shell script can be used in either of the following ways:

> ```qchem
> qchem infile outfile
> qchem infile outfile savename
> qchem -save infile outfile savename
> qchem -archive infile outfile
> ```

where `infile` is the name of a suitably formatted **Q-Chem** input file
(detailed in Chapter [3](../ch03_inputs/chap_inputs.md), and the remainder of this manual), and
the `outfile` is the name of the file to which **Q-Chem** will place the job output information.

**Note: 

If the `outfile` already exists in the working directory, it will be overwritten.
**

The use of the `savename` command line variable allows the saving of a few
key scratch files between runs, and is necessary when instructing **Q-Chem** to
read information from previous jobs. If the `savename` argument is not
given, **Q-Chem** deletes all temporary scratch files at the end of a run. The
saved files are in `$QCSCRATCH/savename/`, and include files with the
current molecular geometry, the current molecular orbitals and density matrix
and the current force constants (if available). The *–save* option in
conjunction with `savename` means that all temporary files are saved,
rather than just the few essential files described above. Normally this is not
required. When `$QCLOCALSCR` has been specified, the temporary files
will be stored there and copied to `$QCSCRATCH/savename/` at the end of normal termination.

The name of the input parameters `infile`, `outfile` and *save*
can be chosen at the discretion of the user (usual UNIX file and directory name
restrictions apply). It maybe helpful to use the same job name for
`infile` and `outfile`, but with varying suffixes. For example:

> ```qchem
> localhost-1> qchem water.in water.out &
> ```

invokes **Q-Chem** where the input is taken from `water.in` and the output
is placed into `water.out`. The `&` places the job into the
background so that you may continue to work in the current shell.

> ```qchem
> localhost-2> qchem water.com water.log water &
> ```

invokes **Q-Chem** where the input is assumed to reside in `water.com`, the
output is placed into `water.log` and the key scratch files are saved in a
directory `$QCSCRATCH/water/`.

## 2.2.1.1 OpenMP Parallelization

Parallel execution of **Q-Chem** can be threaded across multiple processors on a
single node using the OpenMP protocol. To run a **Q-Chem** calculation with
OpenMP threads, specify the number of threads (*nthreads*) using the
*qchem* command option *-nt*. Since each thread uses one CPU core,
you should not specify more threads than the total number of available CPU
cores for performance reason. When unspecified, the number of threads defaults
to 1 (serial calculation).

> ```qchem
> qchem -nt nthreads infile outfile
> qchem -nt nthreads infile outfile save
> qchem -save -nt nthreads infile outfile save
> ```

To run parallel **Q-Chem** via the Slurm job scheduling system, add the
*-slurm* command line argument when starting **Q-Chem**. For example:

> ```qchem
> qchem -slurm -nt nthreads infile outfile
> ```

## 2.2.1.2 Hybrid MPI+OpenMP Parallelization

Starting v6.3.0, parallel execution of **Q-Chem** using the message-passing
interface (MPI) protocol across multiple processor cores and/or multiple
compute nodes is possible on top of the OpenMP parallelization across multiple
threads for certain job types; the older MPI-parallelized features predating
v5.4.0 have been deprecated. This hybrid scheme involves multiple
MPI processes, each spawning several OpenMP threads.
In this hybrid scheme, cross-node communication is handled by the
MPI protocol and intra-node communication is done implicitly using OpenMP
threading for efficient utilization of shared-memory parallel (SMP) systems.
This parallelization strategy reflects current trends towards multi-core
architectures in cluster computing. In v6.3.x and v6.4.0, the new hyrbid MPI+OpenMP
scheme is *only* available for calculations involving
finite-difference derivatives or the many-body interaction method that don’t
depend on a prior calculation for which similar parallelization is not available.
For example, these calculations cannot be started
using the SCF_GUESS = READ in these older versions.
Further, geometry optimization using the **Libopt3** library is possible
with MPI+OpenMP-enabled finite-difference gradients.
In v7.0, the new hybrid MPI+OpenMP scheme is extended to include non-RI
Hartree–Fock and DFT SCF energy calculations done with DIIS and GDM SCF algorithms
and the robust SCF pipelines for RHF, UHF, and ROHF ansätze. For this MPI+OMP-parallel
SCF scheme, Q-Chem v7.0 uses the replicated-Fock approach, which requires the user to
keep the per-rank memory requirement in consideration while spawning multiple MPI ranks
on the same physical node.

To run parallel calculations with MPI, use the option *-np* to specify
the number of MPI processes to be spawned as follows:

> ```qchem
> qchem -mpi -np nprocs infile outfile
> qchem -mpi -np nprocs infile outfile savename
> qchem -save -mpi -np nprocs infile outfile savename
> ```

where *nprocs* is the number of processors to use. If the *-np*
switch is not given, **Q-Chem** will default to running locally
on a single node.

To run hybrid MPI+OpenMP calculations, use options
*-mpi* *-np* and *-nt* together, where *-np* followed
by the number of MPI processes to be spawned and *-nt* followed by the
number of OpenMP threads used in each MPI process as follows:

> ```qchem
> qchem -mpi -np nprocs -nt nthreads infile outfile
> qchem -mpi -np nprocs -nt nthreads infile outfile savename
> qchem -save -mpi -np nprocs -nt nthreads infile outfile savename
> ```

When the additional argument *savename* is specified,
the temporary files on MPI rank `n` are stored in a folder named
`$QCSCRATCH/savename.n`.
Upon successful completion of the job,
the relevant scratch information is copied back to
the `$QCSCRATCH/savename` folder on the head node.
If the job terminates abnormally, the files will not be copied to the head node.

On computer systems with batch schedulers such as PBS and SLURM,
users may need to set `$QCMPIRUN` environment variable to point to
the *mpirun* or *srun* command used in
the system. In addition, `$QCMPI` may need to be set to “srun”
for SLURM scheduler. For further details users should read the
`$QC/README.Parallel` file. Please contact **Q-Chem** if any problems are
encountered (`support@q-chem.com`).

## 2.2.1.3 GPU-accelerated **Q-Chem** with **BrianQC**

Starting with version 5.0, the core parts of **Q-Chem** calculations can be
accelerated using the **BrianQC** GPU module. It does so by providing routines
for computing all components of the Fock matrix (Eq. ([4.18](../ch04_scf/Ch4.S2.SS2.md#eq416))): the core
Hamiltonian, Coulomb, exchange, and exchange-correlation (Eq. ([5.9](../ch05_dft/sec_Kohn-Sham.md#eq437)))
integrals, along with their first derivatives and the most time-consuming
parts of their second derivatives. This can lead to significant speedups when
computing Hartree-Fock and density functional theory energies, gradients,
vibrational frequencies, and other calculations requiring these quantities.
Range-separated hybrid density functionals, where the exchange contribution is
split into two terms (Eq. ([5.12](../ch05_dft/Ch5.S3.SS1.md#eq:erf_partition))), are also supported.

In order to invoke **BrianQC**, pass the *-gpu* flag when starting
**Q-Chem**. Because **BrianQC** does not accelerate all parts of **Q-Chem**
calculations, and GPU acceleration works transparently with OpenMP threading,
it is still important to parallelize the remaining parts of a calculation
using OpenMP threading.

> ```qchem
> qchem -gpu -nt nthreads infile outfile
> ```

Requirements for using **BrianQC** are:

- •

A separate **BrianQC** license
- •

A 64-bit Linux or Windows-based operating system
- •

An Nvidia GPU based on the Pascal, Volta, Turing, or Ampere
architecture
- •

A basis set with $g$ angular momentum or lower functions
- •

Only one **Q-Chem** calculation running per GPU

To learn more, visit `https://www.brianqc.com/`.
