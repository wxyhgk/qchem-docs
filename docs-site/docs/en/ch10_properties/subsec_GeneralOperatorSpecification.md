---
title: "10.14.3 $response Section and Operator Specification"
---

## 10.14.3 *$response* Section and Operator Specification

(July 4, 2026)

The specification of operators used in solving for response vectors is designed
to be very flexible. The general form of the *$response* input section is given
by

> ```qchem
> $response
>   keyword_1 setting_1
>   keyword_2 setting_2
>   ...
>   [operator_1_label, operator_1_origin]
>   [operator_2_label, operator_2_origin]
>   [operator_3_label, operator_3_origin]
>   ...
> $end
> ```

where the keywords are those found in
section [10.14.2](subsec_responsemanJobControl.md) (with the exception of
RESPONSE).

The specification of an operator is given within a line contained by
`[]`, where the first element is a label from
table [10.4](#tab:responseman_operators), and the second element is a label from
table [10.5](#tab:responseman_origins). Operator specifications may appear in any
order. Response values are calculated for all possible permutations of
operators and their components.

For the Cartesian moment operator, a third field within `[]` may be
specified for the order of the expansion, entered as $(i,j,k)$. For
example, the molecular response to the moment of order (2, 5, 4) with its
origin at (0.2, 0.3, 0.4) a.u. can be found with the operator specification

> ```qchem
> [multipole, (0.2, 0.3, 0.4), (2, 5, 4)]
> ```

Table 10.4: Available operators

| Operator Label | Description | Integral |
| --- | --- | --- |
| dipole or diplen | dipole (length gauge) | $\langle\chi_{\mu}\|\mathbf{r}_{O}\|\chi_{\nu}\rangle$ |
| quadrupole | second moment (length gauge) | $\langle\chi_{\mu}\|\mathbf{r}\mathbf{r}^{T}\|\chi_{\nu}\rangle$ |
| multipole | arbitrary-order Cartesian moment (length gauge) | $\langle\chi_{\mu}\|x^{i}y^{j}z^{k}\|\chi_{\nu}\rangle$ |
| fermi or fc | Fermi contact | $\frac{4\pi g_{e}}{3}\langle\chi_{\mu}\|\delta(\mathbf{r}_{K})\|\chi_{\nu}\rangle$ |
| spindip or sd | spin dipole | $\frac{g_{e}}{2}\langle\chi_{\mu}\|\frac{3\mathbf{r}_{K}\mathbf{r}_{K}^{T}-r_{K}^{2}}{r_{K}^{5}}\|\chi_{\nu}\rangle$ |
| angmom or dipmag | angular momentum | $\langle\chi_{\mu}\|\mathbf{L}_{O}\|\chi_{\nu}\rangle$ |
| dipvel | dipole (velocity gauge) | $\langle\chi_{\mu}\|\mathbf{\nabla}\|\chi_{\nu}\rangle$ |

Table 10.5: Available operator origins

| Origin Label | Description |
| --- | --- |
| zero | Cartesian origin, same as (0.0, 0.0, 0.0) |
| (x, y, z) | arbitrary point (double precision, units are bohrs) |
