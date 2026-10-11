---
title: "8.4.3 Format for User-Defined Basis Sets"
---

## 8.4.3 Format for User-Defined Basis Sets

(July 4, 2026)

The format for the user-defined basis section is as follows:

> | $basis |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- |
> |  | $X$ | 0 |  |  |  |
> |  | $L$ | $K$ | $scale$ |  |  |
> |  | $\alpha_{1}$ | $C_{1}^{L_{\text{min}}}$ | $C_{1}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{1}^{L_{\text{max}}}$ |
> |  | $\alpha_{2}$ | $C_{2}^{L_{\text{min}}}$ | $C_{2}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{2}^{L_{\text{max}}}$ |
> |  | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
> |  | $\alpha_{K}$ | $C_{K}^{L_{\text{min}}}$ | $C_{K}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{K}^{L_{\text{max}}}$ |
> | **** |  |  |  |  |  |
> | $end |  |  |  |  |  |

where

| $X$ | Atomic symbol of the atom (atomic number not accepted) |
| --- | --- |
| $L$ | Angular momentum symbol (S, P, SP, D, F, G) |
| $K$ | Degree of contraction of the shell (integer) |
| $scale$ | Scaling to be applied to exponents (default is 1.00) |
| $\alpha_{i}$ | Gaussian primitive exponent (positive real number) |
| $C_{i}^{L}$ | Contraction coefficient for each angular momentum (non-zero real numbers). |

Atoms are terminated with `****` and the complete basis set is
terminated with the *$end* keyword terminator. No blank lines can be
incorporated within the general basis set input. Note that more than one
contraction coefficient per line is required for compound shells like SP.
As with all **Q-Chem** input deck information, all input is case-insensitive.

???+ example "Example 8.1: Example of adding a user-defined non-standard basis set. Note that since $d$ , $f$ and $g$ functions are incorporated, the $rem variable PURECART must be set. Note the use of BASIS2 for the initial guess."
    ```qchem
    $molecule
       0  1
       O
       H  O  oh
       H  O  oh  2  hoh
    
       oh  =   1.2
       hoh = 110.0
    $end
    
    $rem
       EXCHANGE   hf
       BASIS      gen      user-defined general basis
       BASIS2     sto-3g   sto-3g orbitals as initial guess
       PURECART   112      Cartesian d functions, pure f and g
    $end
    
    $basis
       H  0
       S  2  1.00
          1.30976    0.430129
          0.233136   0.678914
    ****
       O  0
       S  2  1.00
          49.9810    0.430129
          8.89659    0.678914
       SP 2  1.00
          1.94524    0.049472    0.511541
          0.49336    0.963782    0.612820
       D  1  1.00
          0.39000    1.000000
       F  1  1.00
          4.10000    1.000000
       G  1  1.00
          3.35000    1.000000
    ****
    $end
    ```
