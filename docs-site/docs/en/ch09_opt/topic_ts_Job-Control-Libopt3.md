---
title: "9.2.5 Libopt3 Job Control"
---

## 9.2.5 **Libopt3** Job Control

(July 4, 2026)

Within **Libopt3** there is a separate *$geom_opt* section for
geometry optimization job controls, which provide greater control then the
GEOM_OPT variables. This new section contains all the following input
variables for the LIBOPT3 driver.

### `ALGORITHM`

> **Specifies which type of minimization algorithm to use. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `BFGS (OPT) / BOFILL (TS)`
> * **Options**:
>     * `SD`: Steepest Descent
>     * `CG`: Conjugate Gradient
>     * `Newton`: Exact Newton’s Method
>     * `BFGS`: Broyden-Fletcher-Goldfarb-Shanno
>     * `167`: Broyden C. G. SIAM J. App. Math. (1970) ,
>     * `6`: , pp. 76 . Link ,
>     * `1236`: Shanno D. F. Math. Comp. (1970) ,
>     * `24`: , pp. 647 . Link ,
>     * `467`: Goldfarb G. Math. Comp. (1970) ,
>     * `24`: , pp. 23 . Link ,
>     * `391`: Fletcher R. Comput. J. (1970) ,
>     * `13`: , pp. 317 . Link
>     * `LBFGS`: Limited-memory BFGS
>     * `SR1`: Symmetric-Rank One (Murtagh-Sargent)
>     * `970`: Murtagh B. A., Sargent R. W. H. Comput. J. (1970) ,
>     * `13`: , pp. 185 . Link
>     * `PSB`: Powell symmetric Broyden
>     * `BOFILL`: Bofill combination of PSB and SR1
>     * `142`: Bofill J. M. J. Comput. Chem. (1994) ,
>     * `15`: , pp. 1 . Link
>     * `FS`: Farkas and Schlegel combination of SR1 and BFGS
>     * `377`: Farkas Ö., Schlegel H. B. J. Chem. Phys. (1999) ,
>     * `111`: , pp. 10806 . Link
> * **Recommendation**: Steepest descent and conjugate gradient methods are slow to converge in general but are useful when the near the minimum. Best to start with other algorithms and finalize with these two methods if a tighter converged minimum is needed. Newton’s will be efficient but requires a Hessian evaluation at each step, so the cost of the Hessian calculation must be accounted for when using exact Newton’s method. BFGS is a default algorithm for jobtype = OPT for its speed and efficiency for finding the minimum. L-BFGS is recommended when dealing with very large systems when memory is of concern. The default algorithm for jobtype = TS is Bofill.

### `COORDINATES`

> **Specifies which type of coordinate system to use for optimization. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `Delocalized`
> * **Options**:
>     * `Cartesian`
>     * `Cartesian Coordiantes`
>     * `Redundant`
>     * Redundant Internal Coordinates
>     * `Delocalized`
>     * Delocalized Natural Internal Coordinates
> * **Recommendation**: Cartesian can be more stable than internal coordinates but are generally slower than internal coordinates. If there are problems with internal coordinate optimization restart with Cartesian coordinates at the last known internal coordinate geometry can be controlled with OPTIMIZATION_RESTART .

### `MAXITER`

> **Maximum number of geometry optimization cycles. INPUT SECTION: $geom_opt**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * `Integer`: Any positive integer
> * **Recommendation**: None

### `INITIAL_HESSIAN`

> **Specifies the type of initial Hessian to use. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `Model (OPT) / EXACT (TS)`
> * **Options**:
>     * `Identity`
>     * `Identity Matrix`
>     * `Simple`
>     * Simple Approximate Guess Hessian
>     * `Model`
>     * Model Approximate Guess Hessian
>     * `Exact`: Analytical Hessian
>     * `Read`: Read-in Hessian
> * **Recommendation**: The initial guess Hessian for Cartesian coordinates is a unit matrix where for internal coordinates it is an approximate Hessian based on the internal coordinates. 67 Bakken V., Helgaker T. J. Chem. Phys. (2002) , 117 , pp. 9160 . Link The model approximate Hessian is based on a force constant matrix. 1211 Schlegel H. B. Theor. Chem. Acc. (1984) , 66 , pp. 333 . Link , 1480 Wittbrodt J. M., Schlegel H. B. J. Mol. Struct. (Theochem) (1997) , 398 , pp. 55 . Link The exact Hessian is always a quality initial Hessian but could be costly but can be calculated at the start of the optimization or read in from scratch. The default for OPT is the model approximate guess Hessian but for TS the Exact analytical Hessian will be used.

### `CONVERGENCE_CHECK`

> **Specifies the type of convergence check during geometry optimization. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `DEFAULT`
> * **Options**:
>     * `Default`: Check max absolute gradient component and ( maximum absolute displacement or change in energy)
>     * `Energy`: Change in energy
>     * `Gradient`: Check norm of gradient
> * **Recommendation**: None.

### `GRADIENT_CONVERGENCE`

> **The value of maximum absolute gradient or norm of gradient for convergence check. INPUT SECTION: $geom_opt**
>
> * **Type**: `FLOAT`
> * **Default**: `3e-4`
> * **Options**:
>     * `Float`: Any positive float
> * **Recommendation**: This variable is used as the comparison value for the gradient checked with CONVERGENCE_CHECK .

### `DISPLACEMENT_CONVERGENCE`

> **The value of maximum absolute displacement for convergence check. INPUT SECTION: $geom_opt**
>
> * **Type**: `FLOAT`
> * **Default**: `1.2e-3`
> * **Options**:
>     * `Float`: Any positive float
> * **Recommendation**: None.

### `ENERGY_CONVERGENCE`

> **The value of maximum absolute energy difference for convergence check. INPUT SECTION: $geom_opt**
>
> * **Type**: `FLOAT`
> * **Default**: `1e-6`
> * **Options**:
>     * `Float`: Any positive float
> * **Recommendation**: None.

### `STEP_LIMITER`

> **Specifies the type of limiter to use for adjustment of the step during geometry optimization. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `RMS (OPT) / NORM (TS)`
> * **Options**:
>     * `RMS`: Root mean square of the step
>     * `NORM`: Norm of the step
> * **Recommendation**: Adjust the type of condition used for MAX_DISPLACEMENT .

### `MAX_DISPLACEMENT`

> **The value of maximum for the STEP_LIMITER of the Eigenvector following algorithm step. INPUT SECTION: $geom_opt**
>
> * **Type**: `FLOAT`
> * **Default**: `3e-1`
> * **Options**:
>     * `Float`: Any positive float
> * **Recommendation**: If this value is too large there may be trouble with the optimization and a small value could require additional optimization cycles.

### `RECOMPUTE_HESSIAN`

> **Recompute the exact Hessian during optimization algorithms INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `False`
> * **Options**:
>     * `None`: Do not recompute of Hessian
>     * `Recompute`: Compute Hessian during optimization
> * **Recommendation**: Recompute the exact Hessian during optimization during BFGS, SR1, PSB, BOFILL, and FS Quasi-Newton Hessian update algorithms.

### `RECOMPUTE_HESSIAN_CYCLES`

> **The number of cycles before recomputing the Hessian during optimization algorithms. INPUT SECTION: $geom_opt**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * `Integer`: Any positive integer
> * **Recommendation**: None.

### `STEP_SEARCH_ALGORITHM`

> **Specifies the type of algorithm for geometry step generation. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `EFA`
> * **Options**:
>     * `EFA`: Eigenvector Following Algorithm
>     * `LS`: Simple Line Search
> * **Recommendation**: For Quasi-Newton methods the default step generation is Eigenvector following algorithm, but line search can be used if desired.

### `EIGENVECTOR_ALGORITHM`

> **Specifies the type of Eigenvector algorithm. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `RFO`
> * **Options**:
>     * `RFO`: Rational Function Optimization
>     * `PRFO`: Partitioned Rational Function Optimization
> * **Recommendation**: This allows the switching of the Eigenvector following algorithm for state specific searches with PRFO.

### `PRINT_LEVEL`

> **Specifies the printing verbosity of the optimizer. INPUT SECTION: $geom_opt**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: General Print
>     * `10`: Verbose
> * **Recommendation**: None.

### `MAX_LBGFGS_HISTORY`

> **Specifies the number of cycles to retain for L-BFGS history. INPUT SECTION: $geom_opt**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * `Integer`: Any positive integer
> * **Recommendation**: It is recommended to keep this number small.

### `LS_PARAM`

> **Specifies the type of line search algorithm to use. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `Quasi-Newton`
> * **Options**:
>     * `Quasi-Newton`
>     * `Quasi-Newton`
>     * `Strict`
>     * `Strict line search parameters`
>     * `Very_Strict`: Very strict line search parameters
> * **Recommendation**: None

### `LS_MAXITER`

> **Specifies the number of maximum iterations to perform during line search step calculation. INPUT SECTION: $geom_opt**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * `Integer`: Any positive integer
> * **Recommendation**: None

### `LS_PRINT`

> **Specifies the verbosity of printing for the line search algorithm. INPUT SECTION: $geom_opt**
>
> * **Type**: `String`
> * **Default**: `Minimal`
> * **Options**:
>     * `Minimal`
>     * `Minimal printing`
>     * `Verbose`
>     * `Verbose printing`
> * **Recommendation**: None

### `HESSIAN_VERIFY`

> **Specifies the type of verification with the Hessian after geometry optimization INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `RESULT`
> * **Options**:
>     * `No_Verification`: Do no verification of optimization
>     * `Result`: Verify with final Hessian obtained during optimization
>     * `Without`: Verify without a Hessian (Only convergence criteria)
>     * `Recomputed`: Verify with recomputed exact Hessian
> * **Recommendation**: None.

### `OPTIMIZATION_RESTART`

> **Specifies if optimization should restart in Cartesian coordinates after back-transformation failure with internal coordinate optimizations. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `TRUE`
> * **Options**:
>     * `True`: Restart with Cartesian Coordinates
>     * `False`: Do not restart
> * **Recommendation**: Restart a failed back-transformation internal coordinate optimization job in Cartesian coordinates. This will use the current retained updated Internal coordinate Hessian transform it to Cartesian coordinates and continue the optimization from the last known position.

### `FINAL_ZMAT_PRINT`

> **Controls if a Z -matrix is printed at the end of the job. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `TRUE`
> * **Options**:
>     * `True`: Construct Z -matrix and print
>     * `False`: Do calculate or print Z -matrix
> * **Recommendation**: After optimization the final structure can be used to compute and print the final Z -matrix. This can be turned off if molecule contains many atoms and Z-Matrix is not needed.

### `FINAL_VIBRATIONAL_ANALYSIS`

> **Run Vibrational Analysis after geometry optimization. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `False`
> * **Options**:
>     * `True`: Perform Vibrational Analysis
>     * `False`: Do not compute vibrational analysis
> * **Recommendation**: Vibrational analysis can be performed only if the final Hessian for verification was recomputed, HESSIAN_VERIFY

### `PRINT_TOPOLOGY`

> **Print the topology for optimization. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `FALSE`
> * **Options**:
>     * `True`: Print the topology
>     * `False`: Do not print the topology
>     * `Terminate`: Print the topology and terminate job
> * **Recommendation**: Print the topology used in optimization. In addition the topology can be printed then the job terminated.

### `USER_TOPOLOGY`

> **Specifies if a user provided topology is to be read. INPUT SECTION: $geom_opt**
>
> * **Type**: `STRING`
> * **Default**: `Generated`
> * **Options**:
>     * `Generated`: Generate the topology
>     * `Read`
>     * Read a user provided topology.
> * **Recommendation**: A user can provide a topology for a given molecule in the $geom_opt_topology section in the input.

A user defined topology can be read in using the USER_TOPOLOGY keyword
and providing the topology in *$geom_opt_topology* section. The available
topology definitions that can be used are:

**1 (Bond)**

A-B

**2 (Angle) **

A-C-B (Apex is B)

**4 (Torsion)**

Torsion A-B-C-D

**5 (Co-Linear Angle) use with 6**

D A-B-C (ABC is Linear)

**6 (Co-Linear Angle) use with 5**

D A-B-C (ABC is Linear)

**Note: 

The first line is the total number of coordinates to read.
Then the following lines are the coordinate definition to be used, following the
definition above: coordinate type, atom number 1, ….
**

> ```qchem
> $geom_opt_topology
> Total Number of Coordinates
> 1   atomA  atomB !Bonds
> ...
> 2   atomA  atomC  atomB !Angles
> ...
> 4   atomA  atomB  atomC atomD !Torsions
> ...
> 5   atomD  atomA  atomB atomC !Co-linear Torsion
> ...
> 6   atomD  atomA  atomB atomC !Co-linear Torsion
> $end
> ```
