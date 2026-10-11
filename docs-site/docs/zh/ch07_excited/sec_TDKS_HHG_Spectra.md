---
title: "7.4.4 Calculation of High-Harmonic Generation (HHG) Spectra"
---

## 7.4.4 Calculation of High-Harmonic Generation (HHG) Spectra

(July 4, 2026)

The high-harmonic generation (HHG) spectrum $H(\omega)$ in the dipole acceleration form is calculated
by[[258]](../bib_references/bib.md#bib259)

<a id="eq:hhg"></a>
$$
H(\omega)=\sum_{\kappa=x,y,z}\frac{1}{2\pi}\left|\int\frac{d^{2}\mu_{\kappa}(t)}{dt^{2}}w(t)e^{-i\omega t}dt\right|^{2} \tag{7.72}
$$

where $w(t)$ is some kind of window function to improve spectrum quality, and $\mu_{\kappa}(t)$ is the time-dependent dipole moment component.
For light polarized in the $\kappa$ direction ($\kappa\in\{x,y,z\}$), we have $\mu_{\lambda}(t)=0$ ($\lambda\in\{x,y,z\},\lambda\neq\kappa$), and Eq. ([7.72](#eq:hhg)) becomes

<a id="eq:hhg2"></a>
$$
H(\omega)=\frac{1}{2\pi}\left|\int\frac{d^{2}\mu_{\kappa}(t)}{dt^{2}}w(t)e^{-i\omega t}dt\right|^{2} \tag{7.73}
$$

The incorporation of a complex absorbing potential (CAP) is frequently preferred to mitigate artifacts arising from the finite-basis approximation,
see Section [7.4.2.3](sec_TDKS_JobControl.md#sec:TDKS:CAP).

A script is provided to obtain the spectrum after the TDKS simulation is completed:

- •

`$QC/bin/tools/tdks_hhg.py`

This uses Eq. ([7.73](#eq:hhg2)) with $w(t)$ taken to be the Hamming window function.[[1579]](../bib_references/bib.md#bib1642)

For $\kappa=z$, the script can be run as follows:

> ```qchem
> python3 $QC/bin/tools/tdks_hhg.py z output spectrum.txt
> ```

The file `spectrum.txt` produced by the processing script will contain two columns: harmonic order and logarithmic strength (arbitrary units).
The harmonic order is $\omega$ divided by FIELD_FREQUENCY, and the logarithmic strength is $\log[H(\omega)]$.
These data can be visualized as an $(x,y)$ plot to view the spectrum. Users of **Q-Chem**’s TDKS code for HHG spectra are asked to cite
Ref. [[1579]](../bib_references/bib.md#bib1642)
.
