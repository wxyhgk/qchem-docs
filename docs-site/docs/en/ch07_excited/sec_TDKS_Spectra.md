---
title: "7.4.3 Calculation of Absorption Spectra"
---

## 7.4.3 Calculation of Absorption Spectra

(July 4, 2026)

## 7.4.3.1 Theory

The absorption cross-section $\sigma_{\kappa\kappa}(\omega)$ for light polarized in the $\kappa$ direction
($\kappa\in\{x,y,z\}$) can be obtained from the imaginary part ($\Im$) of the frequency-dependent
polarizability, $\alpha_{\kappa\kappa}(\omega)$:[[1578]](../bib_references/bib.md#bib1641)

<a id="Ch7.E65"></a>

$$
\sigma_{\kappa\kappa}(\omega)=\left(\frac{4\pi\omega}{c}\right)\Im\bigl{[}\alpha_{\kappa\kappa}(\omega)\bigr{]}\;. \tag{7.65}
$$

Within the electric dipole approximation, a rotationally-averaged absorption spectrum $A(\omega)$ is then simply

<a id="eq:RT-TDDFT_spectrum"></a>

$$
A(\omega)=\tfrac{1}{3}\bigl{[}\sigma_{xx}(\omega)+\sigma_{yy}(\omega)+\sigma_{zz}(\omega)\bigr{]}\;. \tag{7.66}
$$

Components $\alpha_{\kappa\lambda}(\omega)$ of the frequency-dependent
polarizability tensor $\bm{\alpha}(\omega)$ are obtained from the Fourier transform ($\mathcal{F}$)
of the time-dependent dipole moment component $\mu_{\kappa}(t)$, for a perturbing field $\mathcal{E}_{\lambda}$
in the $\lambda$ direction:[[1578]](../bib_references/bib.md#bib1641)

<a id="eq:TDKS-FT"></a>

$$
\alpha_{\kappa\lambda}(\omega)=\frac{\mathcal{F}\bigl{[}\mu_{\kappa}(t)\bigr{]}}{\mathcal{F}\bigl{[}\mathcal{E}_{\lambda}(t)\bigr{]}}\;. \tag{7.67}
$$

To compute the spectrum in Eq. ([7.66](#eq:RT-TDDFT_spectrum)), three
separate perturbations in the $x$, $y$, and $z$ directions are required, else some excitations may be missing if their
transition moment is strictly perpendicular to the applied field, causing the matrix element
$\langle\Psi_{n}|\mathcal{E}_{\lambda}|\Psi_{0}\rangle$ to vanish. However, these three perturbations $\mathcal{E}_{x}$,
$\mathcal{E}_{y}$, and $\mathcal{E}_{z}$ can be applied all at once in a single calculation, in order to generate a superposition
consisting of all possible excitations out of the ground state.

## 7.4.3.2 Fourier Transform Scripts

Two different scripts are provided to obtain the spectrum after the TDKS simulation is completed:

- •

`$QC/bin/tools/tdks_fft.py`
- •

`$QC/bin/tools/tdks_pade.py`

The first of these uses the Fourier transform method in Eq. ([7.67](#eq:TDKS-FT)) directly while the second
makes use of Padé approximants to obtain comparable spectra with shorter propagation times.[[566]](../bib_references/bib.md#bib585)

The scripts can be run as follows:

> ```qchem
> $QC/bin/tools/tdks_fft.py output spectrum.txt
> $QC/bin/tools/tdks_pade.py output spectrum.txt
> ```

The file `spectrum.txt` produced by the processing script will contain two columns: frequency (eV) and strength (arbitrary units).
These data can be visualized as an $(x,y)$ plot to view the spectrum.

???+ example "Example 7.35: TDKS job using a CW field and a CAP."
    ```qchem
    $molecule
       0 1
       H    0.000000   0.000000   0.000000
       H    0.000000   0.000000   0.750000
    $end
    
    $rem
       BASIS                6-31G
       METHOD               lrc-wpbe
       TDKS                 true
       LRC_DFT              true
       OMEGA                300
       SCF_CONVERGENCE      9
       INTEGRAL_SYMMETRY    false
    $end
    
    $tdks
       DT                   0.10
       MAXITER              5
       PROPAGATOR           MMUT
       FIELD_VECTOR         1 1 1
       FIELD_TYPE           cw
       FIELD_FREQUENCY      1.55
       FIELD_AMP            0.0001
       DO_CAP               true
       CAP_TYPE             atom_centered_spherical
       CAP_R0               18.5  ! units are bohr
       CAP_ETA              0.1   ! units are hartree/bohr^2
    $end
    ```

## 7.4.3.3 Dipole Filtering

An important but not-well-recognized aspect of TDKS broadband spectrum calculations is that they may be contaminated by continuum
artifacts corresponding to transitions to high-energy virtual MOs.[[1514]](../bib_references/bib.md#bib1584)

This can be especially problematic for core-level spectra, where one x-ray edge may exhibit artifacts arising from a lower-energy edge.
For example, N(1s) $\to$ continuum transitions can appear at energies comparable to the oxygen K-edge consisting of
O(1s) $\to$ valence transitions.[[566]](../bib_references/bib.md#bib585)

This is unfortunate, since x-ray spectroscopy is a potentially useful application of the real-time approach, whereas a state-by-state
approach (as in LR-TDDFT or any other eigenvalue-based method) may require the calculation of hundreds of individual states in order
to obtain a converged spectrum. The TDKS approach is almost always (significantly) more expensive than LR-TDDFT,[[566]](../bib_references/bib.md#bib585)

but the former lacks the large memory bottleneck that is incurred by the latter.

Fortunately, artificial states appearing in the TDKS spectrum can be eliminated by means of a dipole-filtering technique,[[1514]](../bib_references/bib.md#bib1584)

although this does require some advance knowledge of what transitions to expect. The key is to recognize that the dipole moment is a
linear function of the density matrix,

<a id="Ch7.E68"></a>

$$
\mu_{\lambda}(t)=\text{tr}\big{[}\mathbf{P}(t)\;\mathbf{D}_{\lambda}(t)\big{]}\;. \tag{7.68}
$$

Here, $\lambda\in\{x,y,z\}$ represents a Cartesian component of the dipole moment and $\mathbf{D}_{\lambda}$ is the matrix representation of
the dipole moment operator $\hat{\mu}_{\lambda}$, expressed in the MO basis. The sum over occupied MOs $k$ allows us to decompose
$\mu_{\lambda}$ into a separate contribution from each. To do this, define a matrix

<a id="Ch7.E69"></a>

$$
\mathbf{D}_{\lambda,k}=\left(\begin{array}[]{ccccc}0&\cdots&(\mathbf{D}_{\lambda})_{1,k}&\cdots&0\\
\vdots&&\vdots&&\vdots\\
(\mathbf{D}_{\lambda})_{k,1}&\cdots&(\mathbf{D}_{\lambda})_{k,k}&\cdots(\mathbf{D}_{\lambda})_{k,n_{\text{occ}}}\\
\vdots&&\vdots&&\vdots\\
0&\cdots&(\mathbf{D}_{\lambda})_{n_{\text{occ}},k}&\cdots&0\\
\end{array}\right) \tag{7.69}
$$

in which all but the $k$th row and column of $\mathbf{D}_{\lambda}$ have been set to zero. Then

<a id="eq:dipole-filter"></a>

$$
\mu_{\lambda}(t)=\sum_{k}^{\text{occ}}\mu_{\lambda,k}(t) \tag{7.70}
$$

where

<a id="Ch7.E71"></a>

$$
\mu_{\lambda,k}(t)=\text{tr}\big{[}\mathbf{P}(t)\;\mathbf{D}_{\lambda,k}(t)\big{]}\;. \tag{7.71}
$$

Taking the Fourier transform of the time series $\mu_{\lambda,k}(t)$ provides the spectral contribution of the $k$th MO, and the sum of all such
contributions affords the full TDKS spectrum. This need not be done on an orbital-by-orbital basis; instead, contributions
from groups of MOs could be summed together, representing various partitions of the summation in Eq. ([7.70](#eq:dipole-filter)).
An oxygen K-edge spectrum that is free of contamination from
N(1s) $\to$ continuum transitions could be obtained by only allowing the sum over $k$ to include the O(1s) orbital(s).

The aforementioned technique is a way of decomposing the full TDKS spectrum into contributions from individual occupied MOs or
groups thereof. Arbitrary groupings can be computed, although only when those groups of MOs are non-disjoint will the Fourier
transforms sum to the full TDKS spectrum. In this way, the effects of different occupied MOs can be deleted from the spectrum, both to look
for (and remove) artifacts, but also to assign spectral features by determining the occupied MOs from which they arise.

Dipole filtering is accomplished by adding the keyword **active_groups** to the *$tdks* input section.
An example of the format is

```qchem
¯         active_groups  k1 k2 k3 | k4 k5 | k6 k7 k8
```

This requests a decomposition into three groups of occupied MOs, with indices $\{k_{1},k_{2},k_{3}\}$ for the first group,
$\{k_{4},k_{5}\}$ for the second group, and $\{k_{6},k_{7},k_{8}\}$ for the third. (Group indices are separated by the “`|`” symbol.)
For unrestricted calculations, the $\alpha$- and $\beta$-spin MO indices for the active groups must be listed separately, using
keywords **active_alpha_groups** and **active_beta_groups** that both have the same format as **active_groups**.

### `active_groups`

> **Specify groups of active MO indices for dipole filtering. INPUT SECTION: $tdks**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * $k_{1}~{}k_{2}\cdots\text{|}k_{3}~{}k_{4}\cdots$: Define groups $\{k_{1},k_{2},\ldots\}$ and $\{k_{3},k_{4},\ldots\}$ .
> * **Recommendation**: Use if desired. In addition to the full dipole moment function $\bm{\mu}(t)$ , separate dipole moment functions for each group will be written to the scratch directory. For unrestricted SCF calculations, use active_alpha_groups and active_beta_groups instead.

The following example demonstrates how to decompose the absorption spectrum for TiO${}_{2}$ into contributions from
Ti(1s), Ti(2s), O(1s), and Ti(2p) orbitals. In order to setup this job, one must have performed a prior SCF calculation to ascertain
which indices correspond to the MOs of interest.

???+ example "Example 7.36: Example of dipole filtering for TDKS. Note that the propagation time ( maxiter )
would need to be much longer for a real simulation."
    ```qchem
    $comment
    TDKS with dipole filtering
    Decompose the spectrum into contributions from active groups of occupied MOs,
       1    |    2    |  3 4  |  5 6 7
     Ti(1s)    Ti(2s)   O(1s)   Ti(2p)
    $end
    
    $molecule
    0 1
    Ti  0.0000000 0.000000  0.6131572
    O  -1.3586178 0.000000 -0.3066726
    O   1.3586178 0.000000 -0.3066726
    $end
    
    $rem
    exchange src1-r1
    basis    def2-tzvpd
    tdks     true
    thresh   12
    scf_convergence 8
    sym_ignore      true
    $end
    
    $tdks
    active_groups  1 | 2 | 3 4 | 5 6 7
    dt 0.02
    maxiter 10
    Propagator MMUT
    field_vector 1 1 1
    field_type delta
    field_amp 0.0001
    $end
    
    ```

The relevant output from a TDKS calculation with dipole filtering is placed into the scratch directory, in a sub-directory named
`$QCSCRATCH/tdks-dipole`. Upon completion of the calculation that director is copied into the same directory that contains
the input and output files, and is renamed as `outFileName.tdks-dipole` where `outFileName` is the **Q-Chem** output file.
For restricted SCF calculations, the `tdks-dipole` directory contains a file named `full.dat` consisting of the full dipole
moment function, arranged as components $\mu_{x}(t)$, $\mu_{y}(t)$, and $\mu_{z}(t)$. In the same directory are files named
`group.n.dat` that contain the same information but restricted to the $n$th group of MOs. For unrestricted SCF calculations,
`full.dat` is replaced by `full-alpha.dat` and `full-beta.dat`, while `group.n.dat` is replaced by
`group-alpha.n.dat` and `group-beta.n.dat`. The data in these `.dat` files can be individually Fourier transformed
to obtain spectral contributions from each group of MOs. If there are no omissions and no redundancies in the list of MOs, then the
group spectra should sum to the full spectrum. For example, `full-alpha.dat` and `full-beta.dat` together provide the
full spectrum for an unrestricted TDKS calculation.
