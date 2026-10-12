---
title: "3.6.1 Overview"
---

## 3.6.1 Overview

(July 4, 2026)

When **Q-Chem** is invoked using

> ```qchem
> # qchem infile outfile
> ```

the output file *outfile* contains a variety of information, depending on
the type of job(s), but in general consists of the following.

- **Q-Chem** citation
- User input (for record-keeping purposes)
- Molecular geometry in Cartesian coordinates
- Molecular point group, nuclear repulsion energy, number of $\alpha$- and
$\beta$-spin electrons
- Basis set information (number of functions, shells and function pairs)
- SCF details (method, guess, and convergence procedure)
- Energy and DIIS error for each SCF iteration
- Results of any post-SCF calculation that is requested
- Results of any excited-state calculation that is requested
- Molecular orbital symmetries and energies
- Wave function analysis
- Message signaling successful job completion

!!! note "Note"
    If *outfile* above already exists when the job is started, then the
    existing file is overwritten with the results of the new calculation.

