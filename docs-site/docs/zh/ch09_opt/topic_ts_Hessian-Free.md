```markdown
---
title: "9.2.3 免 Hessian 的驻点表征"
---

## 9.2.3 免 Hessian 的驻点表征

(July 4, 2026)

**Q-Chem** 允许用户在对几何结构优化或过渡态搜索所找到的驻点进行表征时，无需执行完整的解析 Hessian 计算——后者有时不可用或在计算上负担过高。该功能通过 Sharada *et al.*[[1243]](../bib_references/bib.md#bib1297)
 开发的有限差分 Davidson 过程实现。
对于几何结构优化，它求解 Hessian 的最低本征值（$\lambda_{1}$），并检查是否满足 $\lambda_{1}>0$（负的 $\lambda_{1}$ 表明存在鞍点）；对于过渡态（TS）搜索，它求解最低两个本征值，若 $\lambda_{1}<0$ 且 $\lambda_{2}>0$，则表明为过渡态。在收敛时，将更新后的 P-RFO（近似）Hessian 的最低本征向量用作 Davidson 求解器的初始猜测。

这种免 Hessian 表征方法的计算成本取决于 Davidson 求解器的收敛速度。例如，要对能量极小点进行表征，需要 $2\times N_{\mathrm{iter}}$ 次总能量 + 梯度计算，其中 $N_{\mathrm{iter}}$ 是 Davidson 算法收敛所需的迭代次数，而系数 “2” 对应每次迭代中的正向和负向位移。根据文献 [[1243]](../bib_references/bib.md#bib1297)
，对于较大的体系，该方法可能比精确的 Hessian 计算高效得多。

???+ note "注意"
    目前，该方法不支持 QM/MM 或包含固定原子的体系。

GEOM_OPT_CHARAC

### `GEOM_OPT_CHARAC`

> **使用有限差分 Davidson 方法对所得到的能量极小点/过渡态进行表征。**
```
</think>

??
