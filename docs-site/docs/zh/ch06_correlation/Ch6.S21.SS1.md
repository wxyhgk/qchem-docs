---
title: "6.21.1 引言"
---

## 6.21.1 引言

(July 4, 2026)

通过在波函数中处理所有可能的电子组态，即采用全组态相互作用（Full Configuration Interaction, FCI）方法，可以得到电子薛定谔方程的精确解。然而，电子组态数目随体系尺寸呈指数增长，这使得该方法除对最小的体系外均不可行。而增量法（method of increments）则可以在保持尺寸广延性（size extensivity）的同时，以多项式计算成本系统地捕捉电子关联。这一称为增量 FCI（incremental FCI, iFCI）的方法利用关联能的多体展开（many-body expansion），将其分离为 $n$ 体项。随着 $n$ 阶数的升高，结果向 FCI 解收敛，且通常 $n$ 无需增长到计算上难以承受的大小即可 achieves 良好的收敛。该方法高度可并行化。
