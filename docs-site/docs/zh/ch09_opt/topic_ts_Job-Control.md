---
title: "9.2.1 任务控制概述"
---

## 9.2.1 任务控制概述

(July 4, 2026)

显然，在开始几何优化或过渡态搜索之前，必须指定理论级别、基组（Basis Set）和初始分子几何构型。这些内容在本手册的其他章节中已有描述，本节仅介绍与优化相关的专用任务控制变量。

几何优化的任务控制变量采用通用 rem 变量模式 GEOM_OPT。这些是最初在 **Optimize** 驱动模块中使用的 rem 变量，参见第 9.2.2 节 [9.2.2](topic_ts_Job-Control-Optimize.md)。**Libopt3** 的任务控制变量则包含在 *$geom_opt* 区段中，相较原始的 rem 变量，它为用户提供了更为精细的任务控制能力，参见第 9.2.5 节 [9.2.5](topic_ts_Job-Control-Libopt3.md)。为保证已有工作流的用户不受影响，当 GEOM_OPT 变量在 **Libopt3** 驱动模块中存在匹配的变量/控制项时，同样可以被读取。rem 变量设置优先级由高到低的顺序如下：1) *$geom_opt* 变量，2) GEOM_OPT 变量，3) 默认值。

JOBTYPE

### `JOBTYPE`

> **指定计算类型。**
>
> * **类型**：`STRING`
> * **默认值**：`默认为单点能计算（single-point），应改为以下选项之一。`
> * **可选值**：
>     * OPT
>     * 平衡结构优化。
>     * TS
>     * 过渡态结构优化。
>     * RPATH
>     * 内禀反应坐标（Intrinsic Reaction Coordinate, IRC）路径跟随。
> * **建议**：视具体应用而定。

GEOM_OPT_DRIVER

### `GEOM_OPT_DRIVER`

> **控制几何优化驱动模块的选择。**
>
> * **类型**：`STRING`
> * **默认值**：`LIBOPT3`
> * **可选值**：
>     * OPTIMIZE
>     * 使用原始的优化驱动模块。
>     * LIBOPT3
>     * 使用 **Libopt3** 驱动模块。
