---
title: "9.11.1 Introduction"
---

## 9.11.1 Introduction

(July 4, 2026)

The study of metastable electronic states like temporary anions presents a major challenge for computational chemists. For example, finding a Hartree-Fock (HF) SCF solution that describes the electronic state of a given temporary anion is usually an arduous and tricky task.

That makes the prospect of performing a simple HF-based AIMD simulation of temporary anions even more daunting. On top of the inherent difficulties of the electronic structure problem, one also has to take into account the fact that upon its formation, the temporary anion is, in general, subject to two competing processes: electron autodetachment (AB${}^{-}\ \rightarrow\$AB $+$ e${}^{-}$)
and dissociative electron attachment (DEA) (AB${}^{-}\ \rightarrow\$A $+$ B${}^{-}$).
However, the need to be able to perform such an AIMD simulation cannot be overstated given that such an effort has the potential to offer very important insights into the mechanisms connecting the formation of temporary anions to their DEA products, for example.

Taking advantage of the analytic gradients for complex absorbing potential (CAPs) in **Q-Chem**,[[108]](../bib_references/bib.md#bib95)
,
one may combine the general principles of AIMD simulations with the CAP method (Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)),
facilitating AIMD simulations for temporary anions. Based on the Born-Oppenheimer approximation, this
“CAP-AIMD” method makes it possible to propagate the nuclei on a complex potential energy surface (CPES)
computed on the fly.[[509]](../bib_references/bib.md#bib522)

Starting a CAP-AIMD simulation on the right CPES is paramount to a successful simulation. Failure to do so will lead to wrong results. For this reason, before moving on to discuss how one can run CAP-AIMDs with **Q-Chem**, it is useful
to provide brief guidelines on how to find correct CAP-HF SCF solutions for temporary anions.
