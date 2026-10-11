---
title: "7.11.14 librassf 的作业控制选项"
---

## 7.11.14 librassf 的作业控制选项

（2026 年 7 月 4 日）

**librassf** 模块可以通过在 *$rem* 变量段中设置 EXCHANGE = HF、
CORRELATION = RASCI2 以及 LIBRASSF = 1 来启用。用户还应通过适当设置 RAS_N_ROOTS
来指明所求根（roots）的数目。尽管该模块是通过 RASCI2 调用的，
但大多数作业控制选项与 RASCI1 中的选项更为相似，唯有 RAS_N_ROOTS 例外。

自旋翻转（spin-flip）以及 IP/EA 的数目由 *$rem* 变量
RASSF_DELTA_ALPHA（移除的 alpha 电子数）和
RASSF_DELTA_BETA（添加的 beta 电子数）决定。
空穴（hole）和粒子（particle）激发可以通过设置 RAS_DO_HOLE
和 RAS_DO_PART 关键字来添加。此外，包含本征值和本征向量的
文本文件可以通过 RASSF_WRITE_EVALS 和 RASSF_WRITE_EVECS 关键字进行输出。

RAS_N_ROOTS

### `RAS_N_ROOTS`

> **设置所要计算的 RAS-CI 根的数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * $n>0$
>     * 计算
>     * $n$
>     * 个 RAS-CI 态
> * **建议**: 无。

RASSF_DELTA_ALPHA

### `RASSF_DELTA_ALPHA`

> **设置相对于参考态移除的 alpha 电子数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $0$
>     * 不移除 alpha 电子（用于 EA）
>     * $1$
>     * 移除一个 alpha 电子（用于 1SF、IP）
>     * $2$
>     * 移除两个 alpha 电子（用于 2SF、1SF-IP）
> * **建议**: 无。

RASSF_DELTA_BETA

### `RASSF_DELTA_BETA`

> **设置相对于参考态添加的 beta 电子数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $0$
>     * 不添加 beta 电子（用于 IP）
>     * $1$
>     * 添加一个 beta 电子（用于 1SF、EA）
>     * $2$
>     * 添加两个 beta 电子（用于 2SF、1SF-EA）
> * **建议**: 无。

RAS_DO_HOLE

### `RAS_DO_HOLE`

> **启用空穴激发。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不进行空穴激发（用于 CAS 或 RAS(p)）
>     * $1$
>     * 单空穴激发（用于 RAS(h) 或 RAS(h,p)）
> * **建议**: 无。

RAS_DO_PART

### `RAS_DO_PART`

> **启用粒子激发。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不进行粒子激发（用于 CAS 或 RAS(h)）
>     * $1$
>     * 单粒子激发（用于 RAS(p) 或 RAS(h,p)）
> * **建议**: 无。

N_FROZEN_CORE

### `N_FROZEN_CORE`

> **冻结的核心轨道数目。**
>
> * **类型**: `SIZE_T`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * $n\geq 0$
>     * 冻结的核心轨道数目。
> * **建议**: 无。

N_FROZEN_VIRTUAL

### `N_FROZEN_VIRTUAL`

> **冻结的虚拟轨道数目。**
>
> * **类型**: `SIZE_T`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * $n\geq 0$
>     * 冻结的虚拟轨道数目。
> * **建议**: 无。

RASSF_GUESS

### `RASSF_GUESS`

> **决定在 Davidson 算法中使用哪一组初始猜测向量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `$2$`
> * **选项**:
>     * $0$
>     * 随机正交归一猜测（CAS 的默认设置）
>     * $1$
>     * 单位矩阵猜测（identity guess）
>     * $2$
>     * CAS 猜测（RAS 的默认设置）
> * **建议**: 对于较大的分子，建议从 CAS 猜测开始计算。如果 Davidson 算法遇到本征向量线性相关的问题，可考虑使用单位矩阵猜测。随机正交归一猜测需要构建一个大型 $NxN$ 矩阵，因此仅适用于行列式数目较少的计算。

RASSF_WRITE_EVALS

### `RASSF_WRITE_EVALS`

> **决定是否将本征值写入输出文件。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不将本征值写入输出文件
>     * $1$
>     * 将本征值写入输出文件
> * **建议**: 无。

RASSF_WRITE_EVECS

### `RASSF_WRITE_EVECS`

> **决定是否将本征向量写入输出文件。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不将本征向量写入输出文件
>     * $1$
>     * 将本征向量写入输出文件
> * **建议**: 无。

CAS_LOCAL

### `CAS_LOCAL`

> **决定是否进行轨道定域化。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不做定域化
>     * $1$
>     * Boys 定域化
>     * $2$
>     * Pipek-Mezey 定域化
> * **建议**: 无。

CAS_LOCAL_ALGO

### `CAS_LOCAL_ALGO`

> **传递给定域化程序。若进行 Boys 定域化则设置为 1。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 不做定域化
>     * $1$
>     * Boys 定域化
>     * $2$
>     * Pipek-Mezey 定域化
> * **建议**: 无。

RASSF_DO_BLOCH

### `RASSF_DO_BLOCH`

> **决定是否进行有效哈密顿量（effective Hamiltonian）分析。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $0$
>     * 跳过分析
>     * $1$
>     * 进行有效哈密顿量分析
> * **建议**: 无。
