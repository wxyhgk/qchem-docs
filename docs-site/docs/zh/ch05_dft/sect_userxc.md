---
title: "5.3.7 User-Defined Density Functionals"
---

## 5.3.7 User-Defined Density Functionals

(July 4, 2026)

Users can also request a customized density functional consisting of any linear
combination of exchange and/or correlation functionals available in
**Q-Chem**. A “general” density functional of this sort is requested by
setting EXCHANGE = GEN and then specifying the functional by
means of an *$xc_functional* input section consisting of one line for each
desired exchange (X) or correlation (C) component of the functional, and having
the format shown below.

> ```qchem
> $xc_functional
>    X   exchange_symbol   coefficient
>    X   exchange_symbol   coefficient
>    ...
>    C   correlation_symbol   coefficient
>    C   correlation_symbol   coefficient
>    ...
>    K   coefficient
> $end
> ```

Each line requires three variables: X or C to designate whether this is an
exchange or correlation component; the symbolic representation of the
functional, as would be used for the EXCHANGE or CORRELATION
keywords variables as described above; and a real number coefficient for each
component. Note that Hartree-Fock exchange can be designated either as “X"
or as “K". Examples are shown below.

???+ example "Example 5.2: Q-Chem input for H ${}_{2}$ O with the B3tLap functional."
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   0.97
       hoh = 120.0
    $end
    
    $rem
       EXCHANGE     gen
       CORRELATION  none
       BASIS        g3large   ! recommended for high accuracy
       THRESH       14        ! and better convergence
    $end
    
    $xc_functional
       X    Becke     0.726
       X    S         0.0966
       C    PK06      1.0
       K    0.1713
    $end
    ```

???+ example "Example 5.3: Q-Chem input for H ${}_{2}$ O with the BR89B94hyb functional."
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   0.97
       hoh = 120.0
    $end
    
    $rem
       EXCHANGE     gen
       CORRELATION  none
       BASIS        g3large   ! recommended for high accuracy
       THRESH       14        ! and better convergence
    $end
    
    $xc_functional
       X    BR89      0.846
       C    B94hyb    1.0
       K              0.154
    $end
    ```
