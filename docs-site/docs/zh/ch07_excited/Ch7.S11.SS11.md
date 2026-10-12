---
title: "7.11.11 RASCI1 实现的作业控制"
---

## 7.11.11 RASCI1 实现的作业控制

（2026 年 7 月 4 日）

目前 RASCI1 与 RASCI2 实现采用不同的关键字（将在未来版本中统一）。本小节适用于 RASCI1（使用精确积分的自旋适配算法）。

RASCI1 方法的使用通过在 *$rem* 变量中将 CORRELATION 设置为 RASCI 来控制，且 EXCHANGE 应设置为 HF。RASCI1 实现仅与限制轨道（restricted orbitals）兼容，*即*，UNRESTRICTED = FALSE。

最小输入还要求指定 RAS_ROOTS 的期望（非零）值、"活跃" RAS2 空间中的电子数，以及 RAS1 和 RAS2 子空间中的轨道数。

### `RAS_ROOTS`

> **设置要计算的 RAS-CI 根（roots）数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $n$
>     * $n>0$
>     * 计算
>     * $n$
>     * 个 RAS-CI 态
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_ELEC`

> **设置 RAS2 中的电子数（活跃电子）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n>0$
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_ELEC_ALPHA`

> **设置 RAS2 中自旋-$\alpha$ 电子数（活跃电子）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n>0$
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_ELEC_BETA`

> **设置 RAS2 中自旋-$\beta$ 电子数（活跃电子）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n>0$
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_ACT`

> **设置 RAS2 中的轨道数（活跃轨道）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n>0$
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_OCC`

> **设置 RAS1 中的轨道数**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n>0$
> * **建议**：这些是在引入 $hole$（空穴）类型激发之前最初双占据的轨道（RAS1）。RAS1 空间从最低轨道开始直至该数目，即目前尚不支持冻结轨道选项。仅适用于 RAS-CI。

### `RAS_DO_HOLE`

> **控制 RAS-CI 波函数中是否包含空穴（hole）激发。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * TRUE
>     * 包含空穴组态（RAS1 到 RAS2 的激发）
>     * FALSE
>     * 不包含空穴组态
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_DO_PART`

> **控制 RAS-CI 波函数中是否包含粒子（particle）激发。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * TRUE
>     * 包含粒子组态（RAS2 到 RAS3 的激发）
>     * FALSE
>     * 不包含粒子组态
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_AMPL_PRINT`

> **定义打印 CI 振幅时使用的绝对阈值（$\times 10^{2}$）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`10`
> * **选项**：
>     * $n$
>     * 用户定义的整数，
>     * $n\geq 0$
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_ACT_ORB`

> **设置用户选择的活跃轨道（RAS2 轨道）。**
>
> * **类型**：`INTEGER ARRAY`
> * **默认值**：`From`（自动生成）
> * **选项**：
>     * $[i,j,k...]$
>     * 轨道数目必须等于
>     * RAS_ACT
>     * 变量的值
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_NATORB`

> **控制自然轨道占据数的计算。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 为所有态计算自然轨道占据数
>     * FALSE
>     * 不计算自然轨道占据数
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_NATORB_STATE`

> **将第 $i$ 个计算得到的 RAS-CI 态的自然轨道保存到 .fchk 文件中。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $i$
>     * 保存第
>     * $i$
>     * 个态的自然轨道
> * **建议**：无。仅适用于 RAS-CI，且需 GUI = 2。

### `RAS_GUESS_CS`

> **控制 RAS-CI 中闭壳层猜测组态（guess configuration）的数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 强制以
>     * $n$
>     * 个闭壳层猜测组态开始
> * **建议**：仅对单重态的计算有意义。仅适用于 RAS-CI。

### `RAS_SPIN_MULT`

> **指定要计算的根的自旋多重度**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 0
>     * 计算任意自旋多重度
>     * $2n+1$
>     * 用户定义的整数，
>     * $n\geq 0$
> * **建议**：该选项仅适用于 $M_{S}=0$ 的体系，即 $\alpha$ 与 $\beta$ 电子数相同的情况。

### `RAS_PT2`

> **对 RAS-CI 能量执行二阶微扰修正**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 计算 RASCI(2) 能量修正
>     * FALSE
>     * 不计算 RASCI(2) 能量修正
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_PT2_PARTITION`

> **指定 RASCI(2) 中的分割方案（partitioning scheme）**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 2
>     * Epstein-Nesbet (EN) 分割
>     * 0
>     * 同时执行 DK 分割和 EN 分割
> * **建议**：仅适用于设置了 RAS_PT2 为 true 的 RAS-CI。

### `RAS_PT2_VSHIFT`

> **定义 RASCI(2) 中的能级位移（$\times 10^{3}~{}au$）**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 用户定义的整数
> * **建议**：仅适用于设置了 RAS_PT2 为 true 的 RAS-CI。

### `RAS_SRDFT`

> **执行短程密度泛函 RAS-CI（short-range density functional RAS-CI）计算**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 计算 RASCI-
>     * $sr$
>     * DFT 态和能量
>     * FALSE
>     * 不执行 RASCI-
>     * $sr$
>     * DFT 计算
> * **建议**：无。仅适用于 RAS-CI。需要设置 RAS_SRDFT_EXC 和 RAS_SRDFT_COR。

### `RAS_SRDFT_EXC`

> **定义短程交换泛函**
>
> * **类型**：`STRING`
> * **默认值**：`无默认值`
> * **选项**：
>     * NAME
>     * 使用
>     * =
>     * NAME
>     * ，其中
>     * NAME
>     * 是第
>     * 5.3.3
>     * 节列出的短程交换泛函之一
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_SRDFT_COR`

> **定义短程关联泛函**
>
> * **类型**：`STRING`
> * **默认值**：`无默认值`
> * **选项**：
>     * NAME
>     * 使用
>     * =
>     * NAME
>     * ，其中
>     * NAME
>     * 是第
>     * 5.3.4
>     * 节列出的短程关联泛函之一
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_OMEGA`

> **在 RAS-CI-$sr$ DFT 方法中设置库仑程分离（range-separation）参数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`400`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\omega=n/1000$
>     * ，单位为 bohr
>     * ${}^{-1}$
> * **建议**：无。程分离参数通常记为 $\omega$ 或 $\mu$。仅适用于 RAS-CI。

### `RAS_SRDFT_DAMP`

> **在 RAS-CI-$sr$ DFT 方法中设置阻尼因子（$\alpha<1$）。**
>
> * **类型**：`REAL`
> * **默认值**：`0.5`
> * **选项**：
>     * $\alpha$
>     * 阻尼因子
>     * $0<\alpha<1$
> * **建议**：当 RAS-CI-$sr$ DFT 迭代出现收敛问题时进行调整。仅适用于 RAS-CI

### `RAS_SRDFT_SA_ROOTS`

> **设置在 RAS-CI-$sr$ DFT 中用于构建态平均（state averaged）参考密度的根列表。**
>
> * **类型**：`INTEGER ARRAY`
> * **默认值**：`所有计算得到的态`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 态列表。
> * **建议**：无。仅适用于 RAS-CI

### `RAS_NFRAG`

> **若 $n>0$，则激活 RAS-CI 中的激发分析（excitation analysis）**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 要考虑的片段（fragment）数目
> * **建议**：仅适用于 RAS-CI。打印信息的详细程度由 RAS_PRINT 控制。

### `RAS_NFRAG_ATOMS`

> **设置每个片段中的原子数。**
>
> * **类型**：`INTEGER ARRAY`
> * **默认值**：`None`
> * **选项**：
>     * $[i,j,k...]$
>     * 各数值之和必须等于
>     * 体系中的原子总数
> * **建议**：无。仅适用于 RAS-CI。

### `RAS_FRAG_SETS`

> **定义每个不相交集合（disjoint set）中用于轨道定域化的轨道数。**
>
> * **类型**：`INTEGER ARRAY`
> * **默认值**：`[NOcc,NAct,NVir]`
> * **选项**：
>     * $[i,j,k...]$
>     * 定义要定域化到
>     * $n$
>     * 个片段中的正则分子轨道（canonical MOs）集合
> * **建议**：在 RAS1、RAS2 和 RAS3 空间内设置可降低定域化过程的计算开销，还可能得到质量更好的片段轨道。仅适用于 RAS-CI。

### `CALC_SOC`

> **控制是否为 EOM-CC、RAS-CI、TDDFT/TDA 及 TDDFT 计算自旋-轨道耦合（SOC）常数。**
>
> * **类型**：`INTEGER/LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不执行 SOC 计算。
>     * TRUE
>     * 执行 SOC 计算。
> * **建议**：除 TRUE 和 FALSE 之外，EOM-CC 程序还支持更多 SOC 评估变体；见第 7.9.21.4 节。

### `RAS_SOC_2E`

> **控制是否计算 RAS-CI SOC 的双电子平均场（mean-field）贡献。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * FALSE
>     * 不计算双电子平均场贡献。
>     * TRUE
>     * 计算双电子平均场贡献。
> * **建议**：无。

### `RAS_SOC_SYM_DENS`

> **控制是否计算对称密度（symmetric density）形式的 SOC。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * FALSE
>     * 不采用对称密度方案。
>     * TRUE
>     * 采用对称密度方案。
> * **建议**：无。
