---
title: "2.1.3 Q-Chem Auxiliary files ($QCAUX)"
---

## 2.1.3 **Q-Chem** Auxiliary files (*$QCAUX*)

(July 4, 2026)

The `$QCAUX` environment variable determines the directory where **Q-Chem**
searches for auxiliary files and the machine license. If not set explicitly,
it defaults to `$QC/qcaux`.

The *$QCAUX* directory contains files required to run **Q-Chem**
calculations, including basis set and ECP specifications, SAD
guesses (see Chapter [4](../ch04_scf/chap_scf.md)),
library of standard effective fragments (see Section [11.5](../ch11_env/sect_efp.md)),
and instructions for the **AOInts** package for generating two-electron integrals efficiently.
