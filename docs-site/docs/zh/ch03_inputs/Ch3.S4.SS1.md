---
title: "3.4.1 概述"
---

## 3.4.1 概述

(July 4, 2026)

输入文件中的 *$rem* 部分是用户用来指定所要执行的计算类型(*即*理论级别、基组（Basis Set）、收敛判据、附加的特殊功能，*等等*)的手段。关键字 *$rem* 标志着整个作业定义的起始。在 *$rem* 部分中，用户插入 **$rem** **变量**（每行一个），用以定义计算的基本细节。允许的格式可以是

> ```qchem
> REM_VARIABLE     VALUE    [ comment ]
> ```

也可以采用另一种形式

> ```qchem
> REM_VARIABLE   =  VALUE   [ comment ]
> ```

“=”号会被自动丢弃，并且只读取剩下的前两个参数，因此其余所有文本都会被忽略，可以用来在输入文件中放置注释。于是，负责 **Q-Chem** 作业控制的 *$rem* 部分具有如下示例所示的形式。

文本输入文件中 *$rem* 部分的通用格式为

> ```qchem
> $rem
>   REM_VARIABLE  value  [ comment ]
>   REM_VARIABLE  value  [ comment ]
>   ...
> $end
> ```

**注意：**

1.

可以使用制表符（Tab）来编排输入格式。

2.

以感叹号‘!’开头的行被视为注释，程序将忽略该行。

3.

*$rem* 变量不区分大小写（整个 **Q-Chem** 输入文件同样如此）。

4.

取决于具体的 *$rem* 变量，“`value`”可以是关键字（字符串）、整数或逻辑值（true 或 false）。

5.

完整的 *$rem* 变量列表可见附录 [B](../app_b_quickref/app_quick_ref.md)。

**

在本手册中，*$rem* 变量将按以下格式描述：

IQMOL_FCHK

### `IQMOL_FCHK`

> **控制是否打印可被 IQmol 程序读取的格式化检查点文件（formatted checkpoint file）。**
>
> * **类型（Type）**：`LOGICAL`
> * **默认值（Default）**：`FALSE`
> * **选项（Options）**：
>     * TRUE
>     * 生成名为
>     * inputfilename.fchk
>     * 的检查点文件
>     * 。
> * **建议（Recommendation）**：对于许多 Q-Chem 作业而言，没有理由不生成检查点文件。注意 GUI = 2（IQmol 所使用）与 = TRUE 含义相同。

若某个特定的 *$rem* 变量已指明默认设置，则无需声明该变量即可使用该默认设置。例如，变量 JOBTYPE 的默认值为 SP，表示单点能计算，因此要执行此类计算，用户**并****不**需要设置 JOBTYPE 变量。而要执行几何结构优化，则必须通过设置 JOBTYPE = OPT 来覆盖这一默认值。管理员对默认 *$rem* 设置的偏好可在 `QC/config/preferences` 文件中指定，用户的偏好则可在 `$HOME/.qchemrc` 文件中指定，这两者均在第 [2.1.6](../ch02_install/sect_customization.md) 节中说明。

**Q-Chem** 为大多数 *$rem* 变量提供了默认值，但用户始终必须自行指定其中少数几个。例如在单点能计算中，最低要求是 BASIS（定义基组）与 METHOD（定义交换与关联的理论级别）。例如，METHOD = HF 调用 Hartree-Fock 计算，而 METHOD = CIS 则指定 CIS 激发态计算。

```qchem
$rem
  BASIS         6-31G*   Just a small basis set
  METHOD        mp2      MP2
$end
```

理论级别也可以由另外两个 *$rem* 变量取值来指定，即 EXCHANGE（定义处理交换的理论级别）与 CORRELATION（定义处理电子关联的理论级别，如有需要）。对于用运动方程（equation-of-motion, EOM）方法计算的激发态（第 [7](../ch07_excited/chap_excited.md) 章），还有第三个 *$rem* 变量 EOM_CORR，用于指定目标态的关联级别。

对于密度泛函理论（Density Functional Theory, DFT）计算，METHOD 指定某个交换-关联泛函；支持的泛函列表见第 [5.4](../ch05_dft/sect_DFT_METHOD.md) 节。对于波函数方法，METHOD 支持的取值可在第 [6.1](../ch06_correlation/sect_c5Intro.md) 节（基态方法）与第 [7.1](../ch07_excited/sect_ExStatesSummary.md) 节（激发态方法）中查到。如果使用 CORRELATION 关键字请求诸如 MP2 或 CC 这样的波函数关联处理，则 EXCHANGE 默认取 HF。
