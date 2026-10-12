已翻译并写入 `7.9.18_EOM-CC_Job_Control_zh.md`（与本目录既有 `*_zh.md` 命名保持一致）。内容如下：

---
title: "7.9.18 EOM-CC 作业控制"
---

## 7.9.18 EOM-CC 作业控制

（2026 年 7 月 4 日）

确保有足够的资源可用以进行必要的积分计算和变换非常重要。对于 CCMAN/CCMAN2 算法，这些资源通过 *$rem* 变量
CC_MEMORY、MEM_STATIC 和 MEM_TOTAL 来控制（参见
第 [6.17](../ch06_correlation/CCparallel.md) 节）。

EOM 方法中电子关联处理的精确类型由 METHOD 定义（参见第 [7.1](sect_ExStatesSummary.md) 节）。对于
EOM-CCSD，应将 METHOD 设为 EOM-CCSD，
对于 CC2，METHOD = EOM-CC2，
对于 EOM-MP2，
METHOD = EOM-CCSD，*依此类推*。此外，需要通过 XX_STATES 指定*目标态*的数量（XX 表示目标态的类型，*例如*，EE、SF、IP、EA、DIP、DSF 等）。用户必须了解所研究体系的点群对称性，以及初始态和目标态的对称性，还有跃迁的对称性。可以通过 CC_SYMMETRY 关闭对称性的使用。如果将其设为 FALSE，则将分子视为具有 $C_{1}$ 对称性，所有态均为 $A$ 对称性。

!!! note "注意"
    仅支持阿贝尔群；对于所有 CCMAN 和 CCMAN2 作业，必须将 USE_ABELIAN_SUBGROUP
    设为 TRUE（默认即已设置）。


!!! note "注意"
    1.

    在有限差分计算中，对称性会自动关闭，用户必须确保相应地调整 XX_STATES。

    2.

    在 CCMAN2 中，可以在单次计算中请求不同类型的目标态。
    在 CCMAN 中，单次计算中混合不同的 EOM 模型仅允许在 Dyson 轨道计算中使用。


下面我们描述在 EOM-CC/CI 计算中指定关联处理的替代方式。这些关键字最终将被淘汰。默认情况下，波函数 EOM 部分的关联级别（*即*，EOM 算符 $R$ 中的最大激发级别）设为与
CORRELATION 匹配，但用户可以通过使用 EOM_CORR 为参考态和 EOM 态混合不同的关联级别。要请求 CI
计算，请设置 CORRELATION = CI 并通过
EOM_CORR 选择 CI 展开类型。下表显示了默认和允许的
CORRELATION 与 EOM_CORR 组合。

| CORRELATION | 默认 EOM_CORR | 允许的 EOM_CORR | 目标态 | CCMAN / |
| --- | --- | --- | --- | --- |
|  |  |  |  | CCMAN2 |
| CI | none | CIS, CIS(D) | EE, SF | y/n |
|  |  | CISD | EE, SF, IP | y/n |
|  |  | SDT, DT | EE, SF, DSF | y/n |
| CIS(D) | CIS(D) | N/A | EE, SF | y/n |
| CCSD, OD | CISD |  | EE, SF, IP, EA, DIP | y/y |
|  |  | SD(fT) | EE, IP, EA | n/y |
|  |  | SD(dT), SD(fT) | EE, SF, fake IP/EA | y/n |
|  |  | SD(dT), SD(fT), SD(sT) | IP | y/n |
|  |  | SDT, DT | EE, SF, IP, EA, DIP, DSF | y/n |

表 7.1：默认和允许的 CORRELATION 与 EOM_CORR
组合以及有效的目标态类型。最后一列显示该方法在 CCMAN 或 CCMAN2 中是否可用。

表 [7.2](#table:EOMCI) 展示了标准 EOM 和 CI 模型的 CORRELATION
与 EOM_CORR 的正确组合。

| 方法 | CORRELATION | EOM_CORR | 目标态选择 |
| --- | --- | --- | --- |
| CIS | CI | CIS | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| SF-CIS | CI | CIS | SF_STATES |
| CIS(D) | CI | CIS(D) | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| SF-CIS(D) | CI | CIS(D) | SF_STATES |
| CISD | CI | CISD | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| SF-CISD | CI | CISD | SF_STATES |
| IP-CISD | CI | CISD | IP_STATES |
| CISDT | CI | SDT | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| SF-CISDT | CI | SDT 或 DT | SF_STATES |
| EOM-EE-CCSD | CCSD |  | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| EOM-SF-CCSD | CCSD |  | SF_STATES |
| EOM-IP-CCSD | CCSD |  | IP_STATES |
| EOM-EA-CCSD | CCSD |  | EA_STATES |
| EOM-DEA-CCSD | CCSD |  | DIP_STATES |
|  |  |  | DEA_SINGLETS, DEA_TRIPLETS |
| EOM-DIP-CCSD | CCSD |  | DIP_STATES |
|  |  |  | DIP_SINGLETS, DIP_TRIPLETS |
| EOM-2SF-CCSD | CCSD | SDT 或 DT | DSF_STATES |
| EOM-EE-(2,3) | CCSD | SDT | EE_STATES |
|  |  |  | EE_SINGLETS, EE_TRIPLETS |
| EOM-SF-(2,3) | CCSD | SDT | SF_STATES |
| EOM-IP-(2,3) | CCSD | SDT | IP_STATES |
| EOM-SF-CCSD(dT) | CCSD | SD(dT) | SF_STATES |
| EOM-SF-CCSD(fT) | CCSD | SD(fT) | SF_STATES |
| EOM-IP-CCSD(dT) | CCSD | SD(dT) | IP_STATES |
| EOM-IP-CCSD(fT) | CCSD | SD(fT) | IP_STATES |
| EOM-IP-CCSD(sT) | CCSD | SD(sT) | IP_STATES |

表 7.2：常用的 EOM 和 CI 模型。"SINGLETS" 和 "TRIPLETS" 仅适用于闭壳层参考态。

以下是最相关的 EOM-CC 输入选项。

### `EE_STATES`

> **设置要寻找的激发态根数。对于闭壳层参考态，默认为 EE_SINGLETS。对于开壳层参考态，指定所有低能态。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个激发态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `EE_SINGLETS`

> **设置要寻找的单重态激发态根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个激发态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `EE_TRIPLETS`

> **设置要寻找的三重态激发态根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个激发态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `SF_STATES`

> **设置要寻找的自旋翻转目标态根数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 SF 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DSF_STATES`

> **设置要寻找的双自旋翻转目标态根数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个双自旋翻转态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `IP_STATES`

> **设置要寻找的电离目标态根数。默认移除 $\beta$ 电子（参见 EOM_IP_BETA）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个电离态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `IP_ALPHA`

> **设置通过移除 $\alpha$ 电子（$M_{S}=\tfrac{1}{2}$）获得的电离目标态数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个电离态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `IP_BETA`

> **设置通过移除 $\beta$ 电子（$M_{S}=\tfrac{1}{2}$，EOM-IP 的默认选项）获得的电离目标态数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个电离态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `EA_STATES`

> **设置要寻找的电子附着目标态根数。默认附着 $\beta$ 电子（参见 EA_BETA）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 EA 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `EA_ALPHA`

> **设置通过附着 $\alpha$ 电子（$M_{S}=\tfrac{1}{2}$，EOM-EA 的默认选项）获得的电子附着目标态数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 EA 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `EA_BETA`

> **设置通过附着 $\beta$ 电子（$M_{S}=\tfrac{1}{2}$，EA-SF）获得的电子附着目标态数。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 EA 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_STATES`

> **设置要寻找的 DIP 根数。对于闭壳层参考态，默认为 DIP_SINGLETS。对于开壳层参考态，指定所有低能态。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_SINGLETS`

> **设置要寻找的单重态 DIP 根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 单重态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_TRIPLETS`

> **设置要寻找的三重态 DIP 根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 三重态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_AA_STATES`

> **设置要寻找的 $M_{S}=-1$ DIP 根数（移除两个 $\alpha$ 电子）。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_BB_STATES`

> **设置要寻找的 $M_{S}=+1$ DIP 根数（移除两个 $\beta$ 电子）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DIP_AB_STATES`

> **设置要寻找的 $M_{S}=0$ DIP 根数（移除一个 $\alpha$ 和一个 $\beta$ 电子）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_STATES`

> **设置要寻找的 DEA 根数。对于闭壳层参考态，默认为 DEA_SINGLETS。对于开壳层参考态，指定所有低能态。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DIP 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_SINGLETS`

> **设置要寻找的单重态 DEA 根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DEA 单重态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_TRIPLETS`

> **设置要寻找的三重态 DEA 根数。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DEA 三重态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_AA_STATES`

> **设置要寻找的 $M_{S}=1$ DEA 根数（两个 $\alpha$ 电子）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DEA $\alpha\alpha$ 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_BB_STATES`

> **设置要寻找的 $M_{S}=-1$ DEA 根数（两个 $\beta$ 电子）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DEA $\beta\beta$ 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

### `DEA_AB_STATES`

> **设置要寻找的 $M_{S}=0$ DEA 根数（一个 $\alpha$ 和一个 $\beta$ 电子）。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中寻找 $i$ 个 DEA $\alpha\beta$ 态，
>     * 在第二个不可约表示中寻找 $j$ 个态，
>     * 依此类推。
> * **建议**：无

!!! note "注意"
    在激发态计算中指定的对称性是*跃迁*的对称性，而非*目标态*的对称性。目标态的对称性是参考态对称性与跃迁对称性的乘积。对于闭壳层分子，前者为全对称的，因此目标态的对称性与跃迁的对称性相同；但对于开壳层参考态则不然。


!!! note "注意"
    在 **Q-Chem** 的早期版本中，我们使用 EOM_XX_STATES。为实现统一（例如，这些关键字也用于 ADC 方法中指定目标 ADC 态），这些关键字已被替换为 XX_STATES。
    为了向后兼容，
    旧关键字被别名为新关键字，因此旧输入仍然可用。
    然而，这些旧关键字最终将被弃用。建议
    切换到新关键字。


!!! note "注意"
    对于 XX_STATES 选项，如果 **Q-Chem** 怀疑存在简并，它会增加根数；如果无法生成足够的猜测向量来启动计算，它会将其改为更小的值。


### `EOM_FAKE_IPEA`

> **如果设为 TRUE，使用弥散轨道技巧计算伪 EOM-IP 或 EOM-EA 能量和性质。在 CCMAN 中为 EOM-EA 和 Dyson 轨道计算的默认选项。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE（使用正确的 EOM-IP 代码）`
> * **选项**：
>     * FALSE, TRUE
> * **建议**：无。此功能仅在 CCMAN 中有效。

!!! note "注意"
    当 EOM_FAKE_IPEA 设为 TRUE 时，与不使用 EOM_FAKE_IPEA 的相同作业相比，它可能会改变 Hartree-Fock 迭代的收敛性，因为在 Hartree-Fock 迭代开始*之前*，会在对称中心添加一个非常弥散的基函数。出于同样的原因，BASIS2 关键字与 EOM_FAKE_IPEA 不兼容。若要从之前的作业中读取 Hartree-Fock 猜测，必须在该之前的作业中指定 EOM_FAKE_IPEA（即使你不请求任何关联或激发态计算）。目前，EOM-IP/EA-CCSD 目标态的电子密度二阶矩、Mulliken 电荷和自旋密度是不正确的。


### `EOM_USER_GUESS`

> **指定在 EOM 计算中是否使用用户定义的猜测。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 求解与 $eom_user_guess 中指定的跃迁具有最大重叠的态。
> * **建议**：轨道按能量排序，如 CCMAN2 输出开头所示。在 CCMAN 中不可用。

### `EOM_SHIFT`

> **指定 EOM 计算中的能量平移。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$ 对应 $n\cdot 10^{-3}$ Hartree 的平移（即 11000 = 11 Hartree）；围绕此值求解本征态。
> * **建议**：在 CCMAN 中不可用。

### `EOM_NGUESS_DOUBLES`

> **指定为双激发的激发态猜测向量数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$ 包含 $n$ 个为双激发的猜测向量
> * **建议**：应设为预期的双激发态数，否则可能无法找到这些态。

### `EOM_NGUESS_SINGLES`

> **指定为单激发的激发态猜测向量数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`等于所请求的激发态数`
> * **选项**：
>     * $n$ 包含 $n$ 个为单激发的猜测向量
> * **建议**：应大于或等于所请求的激发态数。

### `EOM_PRECONV_SINGLES`

> **不为零时，在完整激发态计算之前先收敛单激发向量。设置预收敛过程的最大迭代次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0 不预收敛
>     * 1 预收敛单激发
> * **建议**：有时有助于解决收敛问题。

!!! note "注意"
    在 CCMAN 中，设置 EOM_PRECONV_SINGLES = $N$ 会导致 $N$ 次 Davidson 迭代来预收敛单激发。


### `EOM_PRECONV_DOUBLES`

> **不为零时，在完整激发态计算之前先收敛双激发向量。设置预收敛过程的最大迭代次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0 不预收敛
>     * N 执行 N 次 Davidson 迭代来预收敛双激发。
> * **建议**：偶尔需要以确保找到双激发态。也用于 DSF、DIP 和 DEA 计算中替代 EOM_PRECONV_SINGLES。

!!! note "注意"
    在 CCMAN2 中不支持 EOM-EE。


### `EOM_PRECONV_SD`

> **不为零时，在完整激发态计算之前先预收敛 EOM 向量。设置预收敛过程的最大迭代次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0 不预收敛
>     * N 执行 N 次 Davidson 迭代来预收敛单激发和双激发。
> * **建议**：偶尔需要以确保找到所有低能态。在 EOM(2,3) 计算中也非常有用。无。

!!! note "注意"
    在 CCMAN2 中不可用。


### `EOM_DAVIDSON_CONVERGENCE`

> **激发态向量 RMS 残差（范数的平方）的收敛判据。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **选项**：
>     * $n$ 对应 $10^{-n}$ 收敛判据
> * **建议**：使用默认值。通常该值应与 EOM_DAVIDSON_THRESHOLD 相同。

### `EOM_DAVIDSON_THRESHOLD`

> **指定在迭代 Davidson 对角化中包含新展开向量的阈值。向量的范数必须高于此阈值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`00103`
> * **选项**：
>     * $abcde$ 整数编码映射为 $abc\times 10^{-(de+2)}$，例如 02505 对应 2.5 $\times 10^{-6}$
> * **建议**：除非遇到收敛问题，否则使用默认值。通常应设为与 EOM_DAVIDSON_CONVERGENCE 相同的值，如果出现收敛问题，尝试设为略大于 EOM_DAVIDSON_CONVERGENCE 的值。

### `EOM_DAVIDSON_MAXVECTORS`

> **指定 Davidson 对角化子空间中的最大向量数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`60`
> * **选项**：
>     * $n$ 在重置子空间之前每个根最多使用 $n$ 个向量
> * **建议**：较大的值会增加磁盘存储，但能加速和稳定收敛。

### `EOM_DAVIDSON_MAX_ITER`

> **Davidson 对角化过程允许的最大迭代次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`30`
> * **选项**：
>     * $n$ 用户自定义的迭代次数
> * **建议**：默认值通常足够。

### `EOM_DIIS_CONVERGENCE`

> **用于求解实值 EOM 态的 DIIS 算法的收敛判据（仅适用于 LIBGMBPT 中的 RI-CC2）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **选项**：
>     * $n$ 对应 $10^{-n}$ 收敛判据。
> * **建议**：过松的收敛判据可能导致找到错误的态。

### `EOM_DIIS_MAXVECTORS`

> **指定 DIIS 子空间的最大尺寸（仅适用于 LIBGMBPT 中的 RI-CC2）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`7`
> * **选项**：
>     * $n$ DIIS 子空间中最多使用 $n$ 个向量。
> * **建议**：较大的值会增加磁盘存储，但能加速和稳定收敛。

### `EOM_DIIS_MAX_ITER`

> **DIIS 过程允许的最大迭代次数（仅适用于 LIBGMBPT 中的 RI-CC2）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $n$ 用户自定义的迭代次数。
> * **建议**：默认值通常足够。

### `EOM_IPEA_FILTER`

> **如果设为 TRUE，过滤使用弥散轨道实现（参见 EOM_FAKE_IPEA）获得的 EOM-IP/EA 振幅。有助于收敛。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE（EOM-IP 或 EOM-EA 振幅不会被过滤）`
> * **选项**：
>     * FALSE, TRUE
> * **建议**：无

!!! note "注意"
    在 CCMAN2 中不可用。


### `CC_FNO_THRESH`

> **初始化 FNO 截断并设置两种截止阈值（OCCT 和 POVO）使用的值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * 范围 0000-10000
>     * $abcd$ 对应 $ab.cd$%
> * **建议**：无

### `CC_FNO_USEPOP`

> **截断方案的选择。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 0 POVO
> * **建议**：无

### `SCALE_NUCLEAR_CHARGE`

> **将每个原子核的电荷按某个值进行缩放。核排斥能是针对未缩放的核电荷计算的。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$ 向分子添加 $(1+n/100)e$ 的总正电荷。
> * **建议**：无

### `ADD_CHARGED_CAGE`

> **添加给定半径和总电荷的点电荷笼。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0 无笼。
>     * 1 十二面体笼。
>     * 2 球形笼。
> * **建议**：球形笼预期能给出更准确的结果，尤其是对于小半径。

### `CAGE_RADIUS`

> **定义带电笼的半径。**
>
> * **类型**：`INTEGER`
> * **默认值**：`225`
> * **选项**：
>     * $n$ 半径为 $n/100$ Å。
> * **建议**：无

### `CAGE_POINTS`

> **定义球形笼的点电荷数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $n$ 使用的点电荷数。
> * **建议**：无

### `CAGE_CHARGE`

> **定义笼的总电荷。**
>
> * **类型**：`INTEGER`
> * **默认值**：`400`
> * **选项**：
>     * $n$ 笼的总电荷为 $n/100$ a.u.
> * **建议**：无

### `EOM_EE_IV_PROJ`

> **在使用 EOM-EE-CCSD 计算激发态时启用内价层投影算符的应用。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$ 用于构造内价层投影算符的活性占据轨道数。轨道从底部开始计数，冻结轨道不计入。
> * **建议**：无

### `EOM_IP_IV_PROJ`

> **在使用 EOM-IP-CCSD 计算电离态时启用内价层投影算符的应用。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$ 用于构造内价层投影算符的活性占据轨道数。轨道从底部开始计数，冻结轨道不计入。
> * **建议**：无
