---
title: "7.3.9 Electric Circular Dichroism"
---

## 7.3.9 Electric Circular Dichroism

(July 4, 2026)

Circular dichroism (CD) is defined as the differential absorption of left- and right-circularly polarized light by a sample, expressed as $\Delta\varepsilon=\varepsilon_{\text{L}}-\varepsilon_{\text{R}}$. Electronic circular dichroism (ECD) specifically probes electronic transitions, and its intensity is characterized by the rotatory strength $R_{0n}$ for a transition from the ground state to the $n$-th excited state. Beyond the electric dipole approximation, the contributions to ECD involve both electric dipole-magnetic dipole and electric dipole-electric quadrupole terms. For an isotropic system (e.g., a dilute solution), the electric dipole-electric quadrupole contribution vanishes due to rotational averaging, and the rotatory strength simplifies to

<a id="Ch7.E35"></a>
$$
R_{0n}=\mathrm{Im}\big{[}\bm{\mu}_{0n}\cdot\mathbf{m}_{n0}\big{]}, \tag{7.35}
$$

where $\bm{\mu}_{0n}$ is the transition electric dipole moment and $\mathbf{m}_{n0}$ is the transition magnetic dipole moment. There are two formulations for calculating the rotatory strength, depending on how the transition electric dipole is evaluated. One is the “length-gauge”, where the transition electric dipole is given by

<a id="Ch7.E36"></a>
$$
\bm{\mu}_{0n}^{\text{(l)}}=-e\langle\Psi_{0}|\hat{\mathbf{r}}|\Psi_{n}\rangle. \tag{7.36}
$$

The other is the “velocity-gauge” (also referred to as the transition electric velocity dipole), defined as

<a id="Ch7.E37"></a>
$$
\bm{\mu}_{0n}^{\text{(v)}}=-\frac{e}{i\omega_{n}}\langle\Psi_{0}|\hat{\mathbf{p}}|\Psi_{n}\rangle. \tag{7.37}
$$

Consequently, the rotatory strengths in the length-gauge and velocity-gauge are $R_{0n}^{\text{(l)}}=\mathrm{Im}\big{[}\bm{\mu}_{0n}^{\text{(l)}}\cdot\mathbf{m}_{n0}\big{]}$ and $R_{0n}^{\text{(v)}}=\mathrm{Im}\big{[}\bm{\mu}_{0n}^{\text{(v)}}\cdot\mathbf{m}_{n0}\big{]}$, respectively. Within a finite basis set, the length-gauge and velocity-gauge formulations are not equivalent: the value of the rotatory strength in the length-gauge is origin- (or position-) dependent, whereas the rotatory strength in the velocity-gauge is independent of the origin. Therefore, the use of the velocity-gauge formulation is recommended.

The calculation of ECD rotatory strengths is supported for CIS and TDDFT jobs, and it is automatically performed after all excited-state calculations are completed. Note that if both TDA and TDDFT (i.e., RPA) equations are solved, only the rotatory strengths of the TDDFT excited states are calculated. The output provides the rotatory strengths in both gauges, as well as the transition electric velocity dipole and transition magnetic dipole moments for each state. Since $\bm{\mu}_{0n}^{\text{(v)}}$ and $\mathbf{m}_{n0}$ are purely imaginary, only their imaginary parts are printed.
