---
title: "8.10.5 User-Defined ECPs"
---

## 8.10.5 User-Defined ECPs

(July 4, 2026)

Many users will find that the library of built-in ECPs is adequate
for their needs. However, if you need to use an ECP that is not built into
**Q-Chem**, you can enter it in much the same way as you can enter a
user-defined orbital basis set; see Chapter [8](chap_basis.md).

To apply a user-defined ECP, you must set the ECP and
BASIS keywords in *$rem* to GEN. You then add a *$ecp* block that
defines your ECP, element by element, and a *$basis* block that defines your
orbital basis set, separating elements by asterisks.

The syntax within the *$basis* block is described in Chapter [8](chap_basis.md).
The syntax for each record within the *$ecp* block is as follows:.

*$ecp*

For each atom that will bear an ECP: 

      Chemical symbol for the atom 

      ECP name; the $L$ value for the ECP; number of core electrons removed 

      For each ECP component (in the order unprojected,
$\hat{P}_{0}$, $\hat{P}_{1}$, …, $\hat{P}_{L-1}$): 

            The component name 

            The number of Gaussians in the component 

            For each Gaussian in the component 

                  The power of $r$ ; the exponent ; the contraction coefficient 

A sequence of four asterisks (*i.e.*, `****`) 

*$end*

**Note: 

1.

All of the information in the *$ecp* block is case-insensitive.

2.

The power of $r$ (which includes the Jacobian $r^{2}$ factor) must be 0, 1, or 2.

3.

If an $r^{0}$ or $r^{1}$ term is included you must include the rem keyword
“ECP_FIT = TRUE”.

**

???+ example "Example 8.10: Optimizing the HF geometry of AlH ${}_{3}$ using a user-defined ECP and basis set
on Al and the 3-21G basis on H."
    ```qchem
    $molecule
       0  1
       Al
       H1  Al  r
       H2  Al  r  H1  120.0
       H3  Al  r  H1  120.0  H2  180.0
    
       r = 1.6
    $end
    
    $rem
       JOBTYPE    opt   Geometry optimization
       METHOD     hf    Hartree-Fock theory
       ECP        gen   User-defined ECP
       BASIS      gen   User-defined basis
       ECP_FIT    true
       geom_opt_driver optimize
    $end
    
    $ecp
       Al
       Stevens_ECP  2  10
       d potential
         1
         1   1.95559  -3.03055
       s-d potential
         2
         0   7.78858   6.04650
         2   1.99025  18.87509
       p-d potential
         2
         0   2.83146   3.29465
         2   1.38479   6.87029
    ****
    $end
    
    $basis
       Al
       SP 3  1.00
          0.90110  -0.30377  -0.07929
          0.44950   0.13382   0.16540
          0.14050   0.76037   0.53015
       SP 1  1.00
          0.04874   0.32232   0.47724
    ****
       H
       3-21G
    ****
    $end
    ```
