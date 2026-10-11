---
title: "2.1.2 Installation Requirements"
---

## 2.1.2 Installation Requirements

(July 4, 2026)

## 2.1.2.1 Execution Environment

**Q-Chem** is shipped as a single executable along with several scripts. No
compilation is required. Once the package is installed it is ready to run.
Please refer to the installation notes for your particular platform, which are
distributed with the software. The system software required to run **Q-Chem** on
your platform is minimal, and includes:

- •

A suitable operating system.
- •

Run-time libraries (usually provided with your operating system).

Please check the **Q-Chem** web site (`www.q-chem.com`) or contact **Q-Chem** support
(`support@q-chem.com`) if further details are
required.

## 2.1.2.2 Hardware Platforms and Operating Systems

**Q-Chem** runs on a wide variety of computer systems, ranging from Intel and
AMD microprocessor-based PCs and workstations, to high-performance server nodes
used in clusters and supercomputers. **Q-Chem** supports the Linux, Mac, and
Windows operating systems. To determine the availability of a specific
platform or operating system, please contact
`support@q-chem.com`.

## 2.1.2.3 Memory and Disk Requirements

**Memory**

**Q-Chem**, Inc. has endeavored to minimize memory requirements and maximize the
efficiency of memory usage. Still, the larger the structure or the higher the level
of theory, the more memory is needed. Although **Q-Chem** can be run successfully
in very small-memory environments, this is seldom an issue nowadays and we
recommend 2 GB per CPU core as a minimum.
**Q-Chem** also offers the ability for user control of important,
memory-intensive aspects of the program. In general, the more memory your
system has, the larger the calculation you will be able to perform.

**Q-Chem** uses two types of memory: a chunk of static memory that is used by
multiple data sets and managed by the code, and dynamic memory which is
allocated using system calls. The size of the static memory is specified by the
user through the *$rem* variable MEM_STATIC and has a default value
of 192 MB.

The *$rem* variable MEM_TOTAL specifies the limit of the total memory the
user’s job can use. The default value is sufficiently large that on most
machines it will allow **Q-Chem** to use all the available memory. This value
should be reduced on machines where this is undesirable (for example if the
machine is used by multiple users). The limit for the dynamic memory allocation
is given by (MEM_TOTAL $-$ MEM_STATIC). The amount of
MEM_STATIC needed depends on the size of the user’s particular job.
Please note that one should not specify an excessively large value for
MEM_STATIC, otherwise it will reduce the available memory for dynamic
allocation. Memory settings in CC, EOM, and ADC calculations are described in
Section [6.17](../ch06_correlation/CCparallel.md). The use of *$rem* variables will be discussed in the
next Chapter.

**Disk**

The **Q-Chem** executables, shell scripts, auxiliary files, samples and
documentation require about 1.4GB of disk space, depending on the
platform. The default **Q-Chem** output, which is printed to the designated
output file, is usually only a few kilobytes. This will be exceeded, of course,
in difficult geometry optimizations, QM/MM and QM/EFP jobs, as well as in cases
where users invoke non-default print options. In order to maximize the
capabilities of your copy of **Q-Chem**, additional disk space is required for
scratch files created during execution, and these are automatically deleted upon
normal termination of a job. The amount of disk space required for scratch
files depends critically on the type of job, the size of the molecule and the
basis set chosen.

**Q-Chem** uses direct methods for Hartree-Fock and density functional theory
calculations, which do not require a large amount of scratch disk space.
Wave function-based correlation methods, such as MP2 and coupled-cluster theory,
require substantial amounts of temporary (scratch) disk storage, and the faster
the access speeds, the better these jobs will perform. With the low cost of
disk drives, it is feasible to have between 100 and 1000 GB of scratch space
available as a dedicated file system for these large temporary job files. The
more you have available, the larger the jobs you will be able to run. In the
case of some jobs, like MP2, the jobs will also run faster as two-electron
integrals are computed less often.
