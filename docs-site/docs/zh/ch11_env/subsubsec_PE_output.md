---
title: "11.8.3 Interpreting the Output"
---

## 11.8.3 Interpreting the Output

(July 4, 2026)

After SCF convergence, the PE module prints a summary of PE energy
contributions, for example:

```qchem
----------------------------------------------------------------------
Polarizable Embedding Summary:

   Electrostatics:
      Electronic:                   0.30901227399981
      Nuclear:                      -0.32134940137969
      Multipole:                    0.00000000000000
      Total:                        -0.01233712737988

   Polarization:
      Electronic:                   -0.01817189734325
      Nuclear:                      0.01717961961137
      Multipole:                    -0.02091890381649
      Total:                        -0.02191118154837

   Total Energy:                    -0.03424830892825
----------------------------------------------------------------------
```

If a PE-ADC calculation is carried out, the perturbative corrections are
printed together with the excitation energies:

```qchem
Excited state 1 (singlet, A)                                     [converged]
  ----------------------------------------------------------------------------
  Term symbol:  2 (1) A                                     R^2 =  1.84764e-13

  Total energy:                                           -483.3704138865 a.u.
  Excitation energy:                                               3.906651 eV
  -------------------------------------------
  PE ptSS energy correction:                                      -0.001804 eV
  Corrected Excitation Energy (ptSS):                              3.904847 eV
  -------------------------------------------
  PE ptLR energy correction:                                      -0.000096 eV
  Corrected Excitation Energy (ptLR):                              3.906554 eV
  -------------------------------------------
```
