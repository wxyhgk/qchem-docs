---
title: "4.5.11 Newton 方法"
---

## 4.5.11 Newton 方法

（2026 年 7 月 4 日）

**Q-Chem** 还提供了多种 Newton 方法用于收敛 SCF 问题。在这些方法中，轨道旋转空间中所取的步长计算为 $\boldsymbol{\Delta}=-\mathbf{H}^{-1}\mathbf{g}$，其中 $\mathbf{g}$ 和 $\mathbf{H}$ 分别是 SCF 能量关于轨道旋转变量的梯度和*精确* Hessian 矩阵。在能量极小值附近的二次区域中，Hessian 矩阵是正定的，通过走 Newton 步可以非常高效地到达极小值，通常只需很少的步数。然而，当远离极小值时，Hessian 矩阵往往是不定的（indefinite），Newton 步甚至可能无法导致能量下降。由于获取 SCF 轨道 Hessian（在实际实现中为 Hessian-向量乘积）在计算上代价高昂，通常建议使用另一种算法（*例如* GDM）执行 SCF 计算，然后在误差低于某个阈值后再开始使用 Newton 方法。有关通用混合算法计算的作业控制细节及其中示例，请参见第 [4.5.12](sub_custom_algorithm.md) 节。此外，在 **Q-Chem** 对 Newton 方法的实现中还采用了线搜索（line search）算法，以防止步长过大（overstepping）。

在 **Q-Chem** 中这些方法的实际实现里，Newton 步是通过迭代求解线性方程 $\mathbf{H}\boldsymbol{\Delta}=-\mathbf{g}$ 来计算的。这避免了显式地求值并求逆 SCF 轨道 Hessian，因此在计算上更为高效。目前支持共轭梯度（conjugate-gradient，CG）和最小残差（minimal residual，MINRES）求解器，它们分别对应 **Q-Chem** 中的 NEWTON_CG 和 NEWTON_MINRES 算法。CG 方法要求 Hessian 矩阵正定，而这在远离收敛时可能无法满足。在这些情况下，当检测到负曲率时（依据 $(\mathbf{p}^{(i)})^{T}\mathbf{H}\mathbf{p}^{(i)}<0$，其中 $\mathbf{p}^{(i)}$ 是第 $i$ 次迭代时对解向量 $\boldsymbol{\Delta}^{(i)}$ 的更新），CG 迭代将被终止。随后，未收敛的 $\boldsymbol{\Delta}^{(i)}$ 将被采纳为更新方向（详见参考文献 

）。另一方面，MINRES 算法不要求 Hessian 矩阵正定，因此除存在奇异性外，该方法在大多数情况下都能求解出 $\boldsymbol{\Delta}$。然而，如上所述，当 Hessian 不正定时，所获得的更新（轨道旋转）可能无法使能量下降。

**Q-Chem** 中还实现了“无鞍点”（saddle-free）Newton-CG 算法（SF_NEWTON_CG）。该方法旨在当存在负特征值时，通过使用如下修改后的 Hessian 来恢复 Hessian 矩阵的曲率：

<a id="eq:sf_newton"></a>

$$
\widetilde{\mathbf{H}}=\mathbf{H}-\mathbf{v}_{-}\lambda_{-}\mathbf{v}_{-}^{T} \tag{4.44}
$$

其中 $\lambda_{-}$ 是由负特征值构成的对角矩阵，$\mathbf{v}_{-}$ 表示相应的特征向量。在每次迭代中，算法首先使用 Davidson 算法求解最低的若干个特征值与特征向量，然后使用 CG 求解 $\widetilde{\mathbf{H}}\boldsymbol{\Delta}=-\mathbf{g}$，此时修改后的 Hessian 保证是正定的。

???+ example "示例 4.15: 使用 NEWTON_CG 算法对水分子进行 SCF 计算"
    ```qchem
    $molecule
    0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
    $end
    
    $rem
       jobtype  sp
       method   b3lyp
       basis    6-31g(d)
       scf_algorithm   newton_cg
       scf_convergence 9
    $end
    ```
