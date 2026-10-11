---
title: "7.10.5 Spin Opposite Scaling ADC(2) Models"
---

## 7.10.5 Spin Opposite Scaling ADC(2) Models

(July 4, 2026)

The spin-opposite scaling (SOS) approach originates from MP2 where it was
realized that the same spin contributions can be completely neglected,
if the opposite spin components are scaled appropriately.
In a similar way it is possible to simplify the second order ADC
equations by neglecting the same spin contributions in the ADC matrix,
while the opposite-spin contributions are scaled with appropriate
semi-empirical parameters.[[553]](../bib_references/bib.md#bib568)

Starting from the SOS-MP2 ground state the same scaling parameter
$c_{T}=1.3$ is introduced into the ADC equations to scale the $t_{2}$
amplitudes.
This alone, however, does not result in any computational savings or
substantial improvements of the ADC(2) results.
In addition, the opposite spin components in the $ph$/$2p2h$ and $2p2h$/$ph$
coupling blocks have to be scaled using a second parameter $c_{c}$ to
obtain a useful SOS-ADC(2)-s model.
With this model the optimal value of the parameter $c_{c}$ has been found
to be 1.17 for the calculation of singlet excited states.[[1479]](../bib_references/bib.md#bib1540)

To extend the SOS approximation to the ADC(2)-x method yet
another scaling parameter $c_{x}$ for the opposite spin components of the
off-diagonal elements in the $2p2h$/$2p2h$ block has to be introduced.
Here, the optimal values of the scaling parameters have been
determined as $c_{c}=1.0$ and $c_{x}=0.9$ keeping $c_{T}$ unchanged.[[717]](../bib_references/bib.md#bib749)

The spin-opposite scaling models can be invoked by setting METHOD to either
SOSADC(2) or SOSADC(2)-x.
By default, the scaling parameters are chosen as the optimal values reported
above, *i.e.*, $c_{T}=1.3$ and $c_{c}=1.17$ for ADC(2)-s and $c_{T}=1.3$,
$c_{c}=1.0$, and $c_{x}=0.9$ for ADC(2)-x.
However, it is possible to adjust any of the three parameters by setting
ADC_C_T, ADC_C_C, or ADC_C_X, respectively.
