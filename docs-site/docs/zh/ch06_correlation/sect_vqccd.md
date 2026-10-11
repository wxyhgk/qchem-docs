---
title: "6.14.3 VQCCD"
---

## 6.14.3 VQCCD

（2026 年 7 月 4 日）

VQCCD 方法是前文第 [6.12.8 节](topic_odcc.md) 中所述的 QCCD 方法的活性空间（active space）版本。VQCCD 既可以计算能量，也可以计算梯度，因此可以进行结构优化。由于修正后的能量泛函不易受到非变分坍缩（non-variational collapse）的影响，VQCCD 的适用范围远比 VOD 方法广泛。目前的测试结果表明，VQCCD 能够以与完整价层 CASSCF 相近的精度描述双键断裂过程；对于三键断裂的势能曲线，其定性行为是正确的，但定量上存在数十 kcal/mol 量级的误差。就计算成本随体系规模的标度关系而言，VQCCD 与 VOD 方法相同，但其前置因子（prefactor）明显更大。
