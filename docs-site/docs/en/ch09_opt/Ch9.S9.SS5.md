---
title: "9.9.5 Vibrational Spectra"
---

## 9.9.5 Vibrational Spectra

(July 4, 2026)

The inherent nuclear motion of molecules is experimentally observed by the
molecules’ response to impinging radiation. This response is typically
calculated within the mechanical and electrical harmonic approximations (second
derivative calculations) at critical-point structures. Spectra, including
anharmonic effects, can also be obtained from dynamics simulations. These
spectra are generated from dynamical response functions, which involve the
Fourier transform of auto-correlation functions. **Q-Chem** can provide both the
vibrational spectral density from the velocity auto-correlation function

<a id="Ch9.E63"></a>

$$
D(\omega)\propto\int_{-\infty}^{\infty}dt\ e^{-i\omega t}\langle\vec{v}(0)\bm{\cdot}\vec{v}(t)\rangle \tag{9.63}
$$

and infrared absorption intensity from the dipole
auto-correlation function

<a id="Ch9.E64"></a>

$$
I(\omega)\propto\frac{\omega}{2\pi}\int_{-\infty}^{\infty}dt\ e^{-i\omega t}\langle\vec{\mu}(0)\bm{\cdot}\vec{\mu}(t)\rangle \tag{9.64}
$$

These two features are activated by the AIMD_NUCL_VACF_POINTS and
AIMD_NUCL_DACF_POINTS keywords, respectively, where values indicate
the number of data points to include in the correlation function. Furthermore,
the AIMD_NUCL_SAMPLE_RATE keyword controls the frequency at which
these properties are sampled (entered as number of time steps). These
spectra—generated at constant energy—should be averaged over a suitable
distribution of initial conditions. The averaging indicated in the expressions
above, for example, should be performed over a Boltzmann distribution of
initial conditions.

Note that dipole auto-correlation functions can be contaminated with rotational or
translational information, and while the initial
conditions in **Q-Chem** remove translation and rotation, numerical noise in the
forces and propagation can lead to translation and rotation over time. A
translation-rotation correction is activated by the PROJ_TRANSROT keyword.

AIMD_NUCL_VACF_POINTS

### `AIMD_NUCL_VACF_POINTS`

> **Number of time points to use in the velocity auto-correlation function for an AIMD trajectory**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not compute velocity auto-correlation function.
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * Compute velocity auto-correlation function for last
>     * $n$
>     * time steps of the trajectory.
> * **Recommendation**: If the VACF is desired, set equal to the value of AIMD_STEPS .

AIMD_NUCL_DACF_POINTS

### `AIMD_NUCL_DACF_POINTS`

> **Number of time points to use in the dipole auto-correlation function for an AIMD trajectory**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not compute dipole auto-correlation function.
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * Compute dipole auto-correlation function for last
>     * $n$
>     * timesteps of the trajectory.
> * **Recommendation**: If the DACF is desired, set equal to the value of AIMD_STEPS .

AIMD_NUCL_SAMPLE_RATE

### `AIMD_NUCL_SAMPLE_RATE`

> **The rate at which sampling is performed for the velocity and/or dipole auto-correlation function(s). Specified as a multiple of steps; i.e. , sampling every step is 1.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * Update the velocity/dipole auto-correlation function
>     * every
>     * $n$
>     * steps.
> * **Recommendation**: Since the velocity and dipole moment are routinely calculated for ab initio methods, this variable should almost always be set to 1 when the VACF or DACF is desired.

PROJ_TRANSROT

### `PROJ_TRANSROT`

> **Removes translational and rotational drift during AIMD trajectories.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not apply translation/rotation corrections.
>     * TRUE
>     * Apply translation/rotation corrections.
> * **Recommendation**: When computing spectra (see AIMD_NUCL_DACF_POINTS , for example), this option can be used to remove artificial, contaminating peaks stemming from translational and/or rotational motion. Recommend setting to TRUE for all dynamics-based spectral simulations.
