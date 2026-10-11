---
title: "9.4.7 Atomic Confining Potentials as Alternatives to Constrained Optimization"
---

## 9.4.7 Atomic Confining Potentials as Alternatives to Constrained Optimization

(July 4, 2026)

In principle, the same effect of constrained optimization using fixed atoms can
be achieved instead using a soft harmonic confining potentials of the form

<a id="eq:Vconf_cart"></a>

$$
V_{\text{conf}}(\mathbf{r}_{1},\mathbf{r}_{2},\ldots)=\frac{1}{2}\sum_{i}k\|\mathbf{r}_{i}-\mathbf{r}_{i}^{0}\|^{2}\;. \tag{9.42}
$$

This represents an external potential that confines the *i*th atom (having coodinates
$\mathbf{r}_{i}$) around the position $\mathbf{r}_{i}^{0}$. The above implementation will be
referred to as the *cartesian* confiner, as it is based on the cartesian coordinates
of each confined atom. An alternative way to implement harmonic confiners is to use
a *pairwise* harmonic confining potential of the form

<a id="eq:Vconf_pair"></a>

$$
V_{\text{conf}}(\mathbf{r}_{1},\mathbf{r}_{2},\ldots,\mathbf{r}_{N})=\frac{1}{2}\sum^{N}_{i>j}k\|\mathbf{r}_{ij}-\mathbf{r}_{ij}^{0}\|^{2}\;. \tag{9.43}
$$

This represents an external potential that confines the $i$th and $j$th atoms (having
distance between them $\mathbf{r}_{ij}$) to the initial (or specified distance) of
$\mathbf{r}_{ij}^{0}$. In applications to cluster models of enzymes (as a low-cost
alternative to QM/MM simulations), it is necessary to lock certain atoms at their
crystallographic positions in order to relax the geometry (in the gas phase or
in continuum solvent) without collapsing the active-site
model.[[1253]](../bib_references/bib.md#bib1306)

Use of a pairwise confining potential between each unique pair of confined atoms
allows optimizations to proceed in an *unconstrained* manner, using delocalized
internal coordinates (rather than Cartesian coordinates) for efficiency, yet achieves
a similar effect as the traditional fixed-atom approach that is widely used in
cluster models of enzymatic reactions. The fixed atom constraint can be better mimicked
by tethering an atom to a geometric position, but in doing so the ability to run
optimization in internal coordinates is lost. [[1253]](../bib_references/bib.md#bib1306)
 Moreover, the use of
harmonic confining potentials results in fewer imaginary frequencies that plague
fixed-atom optimizations, making it straightforward to compute zero-point vibrational
corrections.[[302]](../bib_references/bib.md#bib307)

Harmonic confining potentials are activated by setting the *$rem* variable
HARM_OPT to either 1 or 2, listing the indices of the confined atoms in the
*$harmonic_opt* section. Only one type of confiner can be used for any specific jobs.
For the cartesian confiners, the equilibrium positions ($\mathbf{r}_{i}^{0}$) must
be specified in the *$coords* section as shown in the example below.

???+ example "Example 9.14: Geometry optimization and subsequent frequency calculation using cartesian confining potentials."
    ```qchem
    $molecule
    0 1
      C         2.2847229688   -0.3069830925   -0.2968221397
      C         0.9156471557    0.1503924513    0.1693932675
      N        -0.0576877706   -0.7876400788    0.0645249649
      H         2.9837678662    0.5043669375   -0.1693203557
      H         2.2497378474   -0.5929607607   -1.3422589452
      H         2.6126794028   -1.1626691284    0.2825927880
      O         0.6966207559    1.2669942030    0.6077661092
      C        -1.4350712383   -0.4874947903    0.4670886412
      H         0.1463602169   -1.6783001309   -0.3307859180
      C        -2.1768099264    0.3412632672   -0.5936684676
      H        -1.3995705380    0.0636682083    1.3955334557
      H        -1.9421824240   -1.4270154508    0.6422037013
      H        -1.6624625664    1.2829541077   -0.7297597438
      H        -3.1943263155    0.5415731987   -0.2762358302
      H        -2.2051967614   -0.1880845317   -1.5391034623
    $end
    
    $rem
       JOBTYPE OPT
       BASIS  3-21G
       METHOD  HF
       point_group_symmetry false
       NO_REORIENT TRUE
       HARM_OPT 1 ! Turn on cartesian harmonic confining potential
       HOATOMS 2  ! No. of confined atoms
       HARM_FORCE 450 ! Force constant of the potential
    $end
    
    $harmonic_opt
    1 10 ! indices of the confined atoms
    $end
    
    $coords !coordinates of confined atoms
      C1    2.2847229688   -0.3069830925   -0.2968221397
     C10   -2.1768099264    0.3412632672   -0.5936684676
    $end
    
    $geom_opt
    initial_hessian = simple
    hessian_verify = recomputed !Recompute Exact Hessian for verification
    final_vibrational_analysis = true !Perform Vibrational Analysis on optimized Hessian
    $end
    
    ```

For pairwise confiners, pairwise distances between two constrained atoms ($\mathbf{r}_{ij}^{0}$)
may optionally be placed in these *$coords* section, and if no $\mathbf{r}_{ij}^{0}$ are
specified, the starting atom distances given in the *$molecule* are used to calculate
the equilibrium distances. An example of a pairwise confiner optimization followed by a
frequency calculation is shown below.

???+ example "Example 9.15: Geometry optimization and subsequent frequency calculation using pairwise confining potentials.
Note the lack of a $coords in the frequency calculation. Compound jobs will carry the
equilibrium coordinates from one job to the next. Separately run pairwise confiner jobs will need
specified $coords to maintain the same potential energy surface."
    ```qchem
    $molecule
    
    0 1
     H  -0.68168  -1.29335  0.69937
     C  -0.01515  -0.39524  0.63493
     N  1.06556  -0.59220  1.63009
     H  1.57017  -1.42548  1.41732
     H  1.68831  0.18821  1.62555
     C  -0.82092  0.86652  1.01181
     H  -1.07481  0.84874  2.09044
     H  -0.23531  1.78800  0.81958
     O  -1.99965  0.85940  0.24056
     H  -2.47074  1.65064  0.46275
     C  0.53081  -0.25778  -0.78386
     O  1.40105  0.49365  -1.18881
     O  -0.00029  -1.09878  -1.69507
     H  0.36786  -0.92650  -2.55634
    
    $end
    
    $rem
     JOBTYPE = OPT
     BASIS = MINIX
     METHOD = HF3c
    
     HARM_OPT = 2 ! Turn on pairwise harmonic confining potential
     HOATOMS = 2 ! No. of confined atoms
     HARM_FORCE = 50 ! force per spring (scaled by 1/1000)
    $end
    
    $harmonic_opt ! specifies which atoms to be confined
    3 11
    $end
    
    $coords ! optional for pairwise - specifies distance between pairs of atoms
     3 11 50.0
    $end
    
    @@@
    
    $molecule
     READ
    $end
    
    $rem
     JOBTYPE = FREQ
     BASIS = MINIX
     METHOD = HF3c
    
     HARM_OPT = 2
     HOATOMS = 2
     HARM_FORCE = 50
    $end
    
    $harmonic_opt
    3 11
    $end
    ```

After each geometry optimization using a pairwise harmonic confiner, the *$coords*
section is printed in the output under "Harmonic Coords Print:". This allows users
to be able to maintain the same potential energy surface between jobs. For example, a
geometry optimization with pairwise confiners would generate a *$coords* section which
could then used in a frequency job that needs to match the forces of the optimization job.

HARM_OPT

### `HARM_OPT`

> **Controls whether the job uses confining potentials**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not use the potentials
>     * 1
>     * Use cartesian confining potential
>     * 2
>     * Use pairwise confining potential
> * **Recommendation**: False

HOATOMS

### `HOATOMS`

> **Controls the number of confined atom**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * User defined
> * **Recommendation**: None

HARM_FORCE

### `HARM_FORCE`

> **Sets the force constant for harmonic confiner, in units of N/m. For pairwise confiner the force is divided by 1000, so a set value of 5000 applies a force constant of 5 N/m to each spring.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * User defined
> * **Recommendation**: None
