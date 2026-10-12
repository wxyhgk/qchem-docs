---
title: "9.2.5 Libopt3 作业控制"
---

## 9.2.5 **Libopt3** 作业控制

(July 4, 2026)

**Libopt3** 内部设有独立的 *$geom_opt* 区段用于几何优化作业控制，其提供的控制能力比 GEOM\_OPT 变量更为强大。这一新区段包含了 LIBOPT3 驱动器的以下所有输入变量。

### `ALGORITHM`

> **指定使用哪种类型的极小化算法。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `BFGS (OPT) / BOFILL (TS)`
> * **可选项**:
>     * `SD`: 最速下降法（Steepest Descent）
>     * `CG`: 共轭梯度法（Conjugate Gradient）
>     * `Newton`: 精确牛顿法（Exact Newton's Method）
>     * `BFGS`: Broyden-Fletcher-Goldfarb-Shanno
>     * `167`: Broyden C. G. SIAM J. App. Math. (1970) ,
>     * `6`: , pp. 76 . Link ,
>     * `1236`: Shanno D. F. Math. Comp. (1970) ,
>     * `24`: , pp. 647 . Link ,
>     * `467`: Goldfarb G. Math. Comp. (1970) ,
>     * `24`: , pp. 23 . Link ,
>     * `391`: Fletcher R. Comput. J. (1970) ,
>     * `13`: , pp. 317 . Link
>     * `LBFGS`: 有限内存 BFGS（Limited-memory BFGS）
>     * `SR1`: 对称秩一法（Symmetric-Rank One，Murtagh-Sargent）
>     * `970`: Murtagh B. A., Sargent R. W. H. Comput. J. (1970) ,
>     * `13`: , pp. 185 . Link
>     * `PSB`: Powell 对称 Broyden 法（Powell symmetric Broyden）
>     * `BOFILL`: Bofill 提出的 PSB 与 SR1 组合方法
>     * `142`: Bofill J. M. J. Comput. Chem. (1994) ,
>     * `15`: , pp. 1 . Link
>     * `FS`: Farkas 与 Schlegel 提出的 SR1 与 BFGS 组合方法
>     * `377`: Farkas Ö., Schlegel H. B. J. Chem. Phys. (1999) ,
>     * `111`: , pp. 10806 . Link
> * **建议**: 最速下降法和共轭梯度法通常收敛较慢，但在接近平衡点位置时较为有用。最好先使用其他算法，若需要更严格收敛的极小点，再用这两种方法进行收尾优化。牛顿法效率很高，但每一步都需要计算 Hessian 矩阵，因此在使用精确牛顿法时必须考虑 Hessian 计算的代价。对于 jobtype = OPT，默认算法为 BFGS，因为它在寻找极小点时速度快且效率高。当处理非常大的体系且内存受限时，推荐使用 L-BFGS。对于 jobtype = TS，默认算法为 Bofill。

### `COORDINATES`

> **指定优化时使用哪种类型的坐标系。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `Delocalized`
> * **可选项**:
>     * `Cartesian`: 笛卡尔坐标（Cartesian Coordinates）
>     * `Redundant`: 冗余内坐标（Redundant Internal Coordinates）
>     * `Delocalized`: 离域自然内坐标（Delocalized Natural Internal Coordinates）
> * **建议**: 笛卡尔坐标有时比内坐标更稳定，但通常收敛速度比内坐标慢。如果内坐标优化出现问题，可在最后已知的内坐标几何结构处改用笛卡尔坐标重新开始优化，该行为可通过 OPTIMIZATION_RESTART 控制。

### `MAXITER`

> **几何优化的最大循环步数。输入区段：$geom_opt**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **可选项**:
>     * `Integer`: 任意正整数
> * **建议**: 无

### `INITIAL_HESSIAN`

> **指定所使用的初始 Hessian 矩阵类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `Model (OPT) / EXACT (TS)`
> * **可选项**:
>     * `Identity`: 单位矩阵（Identity Matrix）
>     * `Simple`: 简单近似猜测 Hessian（Simple Approximate Guess Hessian）
>     * `Model`: 模型近似猜测 Hessian（Model Approximate Guess Hessian）
>     * `Exact`: 解析 Hessian（Analytical Hessian）
>     * `Read`: 读入的 Hessian（Read-in Hessian）
> * **建议**: 笛卡尔坐标的初始猜测 Hessian 为单位矩阵，而内坐标的初始猜测 Hessian 则是基于内坐标的近似 Hessian。67 Bakken V., Helgaker T. J. Chem. Phys. (2002) , 117 , pp. 9160 . Link 模型近似 Hessian 基于力常数矩阵构建。1211 Schlegel H. B. Theor. Chem. Acc. (1984) , 66 , pp. 333 . Link , 1480 Wittbrodt J. M., Schlegel H. B. J. Mol. Struct. (Theochem) (1997) , 398 , pp. 55 . Link 精确 Hessian 始终是高质量的初始 Hessian，但代价可能较高，可在优化开始时计算，也可从头读入。OPT 的默认值是模型近似猜测 Hessian，而 TS 则默认使用精确解析 Hessian。

### `CONVERGENCE_CHECK`

> **指定几何优化过程中的收敛检查类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `DEFAULT`
> * **可选项**:
>     * `Default`: 检查梯度的最大绝对分量以及（最大绝对位移或能量变化）
>     * `Energy`: 能量变化
>     * `Gradient`: 检查梯度范数
> * **建议**: 无。

### `GRADIENT_CONVERGENCE`

> **用于收敛检查的梯度最大绝对值或梯度范数的阈值。输入区段：$geom_opt**
>
> * **类型**: `FLOAT`
> * **默认值**: `3e-4`
> * **可选项**:
>     * `Float`: 任意正浮点数
> * **建议**: 该变量作为与 CONVERGENCE_CHECK 中所检查梯度进行比较的判据值。

### `DISPLACEMENT_CONVERGENCE`

> **用于收敛检查的最大绝对位移阈值。输入区段：$geom_opt**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.2e-3`
> * **可选项**:
>     * `Float`: 任意正浮点数
> * **建议**: 无。

### `ENERGY_CONVERGENCE`

> **用于收敛检查的能量差最大绝对值阈值。输入区段：$geom_opt**
>
> * **类型**: `FLOAT`
> * **默认值**: `1e-6`
> * **可选项**:
>     * `Float`: 任意正浮点数
> * **建议**: 无。

### `STEP_LIMITER`

> **指定几何优化中用于调整步长时所采用的限制器类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `RMS (OPT) / NORM (TS)`
> * **可选项**:
>     * `RMS`: 步长的均方根（Root mean square of the step）
>     * `NORM`: 步长的范数（Norm of the step）
> * **建议**: 调整用于 MAX_DISPLACEMENT 的判据类型。

### `MAX_DISPLACEMENT`

> **Eigenvector following 算法步长中 STEP_LIMITER 的最大值阈值。输入区段：$geom_opt**
>
> * **类型**: `FLOAT`
> * **默认值**: `3e-1`
> * **可选项**:
>     * `Float`: 任意正浮点数
> * **建议**: 若该值过大，优化可能会出现问题；若该值过小，则可能需要额外的优化循环步数。

### `RECOMPUTE_HESSIAN`

> **在优化算法过程中是否重新计算精确 Hessian。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `False`
> * **可选项**:
>     * `None`: 不重新计算 Hessian
>     * `Recompute`: 在优化过程中计算 Hessian
> * **建议**: 在使用 BFGS、SR1、PSB、BOFILL 和 FS 等拟牛顿（Quasi-Newton）Hessian 更新算法时，可在优化过程中重新计算精确 Hessian。

### `RECOMPUTE_HESSIAN_CYCLES`

> **优化算法过程中重新计算 Hessian 之前所间隔的循环步数。输入区段：$geom_opt**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **可选项**:
>     * `Integer`: 任意正整数
> * **建议**: 无。

### `STEP_SEARCH_ALGORITHM`

> **指定几何步长生成所使用的算法类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `EFA`
> * **可选项**:
>     * `EFA`: 本征矢量跟踪算法（Eigenvector Following Algorithm）
>     * `LS`: 简单线搜索（Simple Line Search）
> * **建议**: 对于拟牛顿方法，默认的步长生成方式是本征矢量跟踪算法，但如有需要也可以使用线搜索。

### `EIGENVECTOR_ALGORITHM`

> **指定本征矢量算法的类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `RFO`
> * **可选项**:
>     * `RFO`: 有理函数优化（Rational Function Optimization）
>     * `PRFO`: 分域有理函数优化（Partitioned Rational Function Optimization）
> * **建议**: 该变量允许在态特定（state specific）搜索中将本征矢量跟踪算法切换为 PRFO。

### `PRINT_LEVEL`

> **指定优化程序的打印详细程度。输入区段：$geom_opt**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选项**:
>     * `0`: 常规打印（General Print）
>     * `10`: 详细打印（Verbose）
> * **建议**: 无。

### `MAX_LBGFGS_HISTORY`

> **指定 L-BFGS 历史中所保留的循环步数。输入区段：$geom_opt**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **可选项**:
>     * `Integer`: 任意正整数
> * **建议**: 建议将该数值保持得较小。

### `LS_PARAM`

> **指定所使用的线搜索算法类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `Quasi-Newton`
> * **可选项**:
>     * `Quasi-Newton`: 拟牛顿（Quasi-Newton）
>     * `Strict`: 严格线搜索参数（Strict line search parameters）
>     * `Very_Strict`: 非常严格的线搜索参数（Very strict line search parameters）
> * **建议**: 无

### `LS_MAXITER`

> **指定线搜索步长计算过程中执行的最大迭代次数。输入区段：$geom_opt**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **可选项**:
>     * `Integer`: 任意正整数
> * **建议**: 无

### `LS_PRINT`

> **指定线搜索算法的打印详细程度。输入区段：$geom_opt**
>
> * **类型**: `String`
> * **默认值**: `Minimal`
> * **可选项**:
>     * `Minimal`: 最少打印（Minimal printing）
>     * `Verbose`: 详细打印（Verbose printing）
> * **建议**: 无

### `HESSIAN_VERIFY`

> **指定几何优化结束后对 Hessian 进行校验的类型。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `RESULT`
> * **可选项**:
>     * `No_Verification`: 不对优化进行校验
>     * `Result`: 使用优化过程中获得的最终 Hessian 进行校验
>     * `Without`: 不使用 Hessian 进行校验（仅使用收敛判据）
>     * `Recomputed`: 使用重新计算的精确 Hessian 进行校验
> * **建议**: 无。

### `OPTIMIZATION_RESTART`

> **指定在内坐标优化反变换失败后，是否改用笛卡尔坐标重新开始的优化。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `TRUE`
> * **可选项**:
>     * `True`: 使用笛卡尔坐标重新开始优化
>     * `False`: 不重新开始优化
> * **建议**: 当内坐标优化的反变换失败时，改用笛卡尔坐标重新开始该优化作业。此操作会使用当前保留的、已更新的内部坐标 Hessian，将其变换为笛卡尔坐标 Hessian，并从最后已知的几何位置继续优化。

### `FINAL_ZMAT_PRINT`

> **控制是否在作业结束时打印 Z-矩阵。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `TRUE`
> * **可选项**:
>     * `True`: 构建 Z-矩阵并打印
>     * `False`: 不计算也不打印 Z-矩阵
> * **建议**: 优化完成后，可使用最终结构计算并打印最终的 Z-矩阵。若分子包含大量原子且不需要 Z-矩阵，可关闭此功能。

### `FINAL_VIBRATIONAL_ANALYSIS`

> **在几何优化后运行振动分析。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `False`
> * **可选项**:
>     * `True`: 执行振动分析
>     * `False`: 不进行振动分析计算
> * **建议**: 仅当用于校验的最终 Hessian 已被重新计算时（参见 HESSIAN_VERIFY），才能执行振动分析。

### `PRINT_TOPOLOGY`

> **打印优化所使用的拓扑结构。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `FALSE`
> * **可选项**:
>     * `True`: 打印拓扑结构
>     * `False`: 不打印拓扑结构
>     * `Terminate`: 打印拓扑结构并终止作业
> * **建议**: 打印优化中所使用的拓扑结构。此外，还可以选择打印拓扑结构后立即终止作业。

### `USER_TOPOLOGY`

> **指定是否读入用户提供的拓扑结构。输入区段：$geom_opt**
>
> * **类型**: `STRING`
> * **默认值**: `Generated`
> * **可选项**:
>     * `Generated`: 自动生成拓扑结构
>     * `Read`: 读入用户提供的拓扑结构。
> * **建议**: 用户可以在输入的 $geom_opt_topology 区段中为给定分子提供拓扑结构。

可以使用 USER_TOPOLOGY 关键字并提供 *$geom_opt_topology* 区段来读入用户定义的拓扑结构。可用的拓扑定义类型如下：

**1（键，Bond）**

A-B

**2（角，Angle）**

A-C-B（顶点为 B）

**4（二面角，Torsion）**

二面角 A-B-C-D

**5（共线角，Co-Linear Angle）与 6 配合使用**

D A-B-C（ABC 为线性）

**6（共线角，Co-Linear Angle）与 5 配合使用**

D A-B-C（ABC 为线性）

**注意：**

**第一行是要读取的坐标总数。
随后的每一行是按照上述定义的坐标类型来书写的坐标定义：坐标类型，原子编号 1，……
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
