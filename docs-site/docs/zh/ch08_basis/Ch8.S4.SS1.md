---
title: "8.4.1 Introduction"
---

## 8.4.1 Introduction

(July 4, 2026)

Users may, on occasion, prefer to use non-standard basis, and it is possible
to declare user-defined basis sets in **Q-Chem** input (see Chapter [3](../ch03_inputs/chap_inputs.md)
on **Q-Chem** inputs). The format for inserting a non-standard
user-defined basis set is both logical and flexible, and is described in
detail in the job control section below.

Note that the SAD guess is not currently supported with non-standard or
user-defined basis sets. The current default is to use SCF_GUESS = AUTOSAD,
unless a mixed basis is specified. When using a mixed basis, the
simplest alternative is to specify the GWH or CORE options
for SCF_GUESS, but these are relatively ineffective other than for
small basis sets. The recommended alternative is to employ basis set
projection by specifying a standard basis set for the BASIS2
keyword. See Section [4.4](../ch04_scf/sect_initialguess.md) on initial guesses for more information.
