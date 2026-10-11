---
title: "6.14.3 VQCCD"
---

## 6.14.3 VQCCD

(July 4, 2026)

The VQCCD method is the active space version of the QCCD method described
earlier in Section [6.12.8](topic_odcc.md). Both energies and gradients are available for
VQCCD, so that structure optimization is possible. VQCCD is applicable to a
substantially wider range of problems than the VOD method, because the modified
energy functional is not vulnerable to non variational collapse. Testing to
date suggests that it is capable of describing double bond breaking to similar
accuracy as full valence CASSCF, and that potential curves for triple
bond-breaking are qualitatively correct, although quantitatively in error by a
few tens of kcal/mol. The computational cost scales in the same manner with
system size as the VOD method, albeit with a significantly larger prefactor.
