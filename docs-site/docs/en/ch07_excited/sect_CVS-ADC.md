---
title: "7.10.7 Core-Excitation ADC Methods"
---

## 7.10.7 Core-Excitation ADC Methods

(July 4, 2026)

Core-excited electronic states are located in the high energy x-ray region of the spectrum.
Thus, to compute core-excited states using standard diagonalization
procedures, which usually
solve for the energetically lowest-lying excited states first, requires the
calculation of a multitude of excited states.
This is computationally very expensive and only feasible for calculations on
very small molecules and small basis sets.

The core-valence separation (CVS) approximation solves the problem by
neglecting the couplings between core and valence excited states
*a priori*.[[218]](../bib_references/bib.md#bib215)

Thereby, the ADC matrix acquires a certain block structure which allows to
solve only for core-excited states.
The application of the CVS approximation is justified, since core and
valence excited states are energetically well separated and the coupling
between both types of states is very small.
To achieve the separation of core and valence excited states the CVS
approximation forces the following types of two-electron integrals to zero

<a id="A3.S8.EGx66"></a>

$$
\displaystyle\langle Ip|qr\rangle=\langle pI|qr\rangle=\langle pq|Ir\rangle=\langle pq|rI\rangle=0 \tag{7.151}
$$

where capital letters $I,J,K$ refer to core orbitals while lower-case letters
$p,q,r$ denote non-core occupied or virtual orbitals.

The core-valence approximation is currently available of ADC models up to
third order (including the extended variant).[[1451]](../bib_references/bib.md#bib1512)

It can be invoked by setting METHOD to the respective ADC model prefixed
by CVS. Besides the general ADC related keywords, two additional keywords
in the *$rem* block are necessary to control CVS-ADC calculations:

- •

ADC_CVS = TRUE switches on the CVS-ADC calculation
- •

CC_REST_OCC = $n$ controls the number of core orbitals included
in the excitation space. The integer $n$ corresponds to the n energetically
lowest core orbitals.

*Example:* cytosine with the molecular formula C${}_{4}$H${}_{5}$N${}_{3}$O
includes one oxygen atom.
To calculate O 1s core-excited states, CC_REST_OCC has to be set to 1,
because the 1s orbital of oxygen is the energetically lowest.
To obtain the N 1s core excitations, the integer has to be set to 4,
because the 1s orbital of the oxygen atom is included as well,
since it is energetically below the three 1s orbitals of the nitrogen atoms.
Accordingly, to simulate the C(1s) XAS spectrum of cytosine,
CC_REST_OCC must be set to 8.

To obtain the best agreement with experimental
data, one should use the CVS-ADC(2)-x method in combination with at least a diffuse
triple-$\zeta$ basis set.[[1451]](../bib_references/bib.md#bib1512)
