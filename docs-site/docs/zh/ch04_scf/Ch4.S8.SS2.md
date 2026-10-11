---
title: "4.8.2 作业控制"
---

## 4.8.2 作业控制

（2026 年 7 月 4 日）

HFPC/DFPC 计算通过以下 *$rem* 变量进行控制。HFPT 用于开启 HFPC/DFPC 近似。注意 HFPT_BASIS 用于指定辅助基组（secondary basis set）。

HFPT

### `HFPT`

> **激活 HFPC/DFPC 计算。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * 仅单点能（Single-point energy only）
> * **建议**：使用双重基组（Dual-Basis）以较小的基组代价捕捉大基组效应。推荐的基组、泛函与网格搭配请参阅参考文献。

HFPT_BASIS

### `HFPT_BASIS`

> **指定 HFPC/DFPC 计算中所用的辅助基组。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * None
> * **建议**：推荐的基组、泛函与网格搭配请参阅参考文献。

DFPT_XC_GRID

### `DFPT_XC_GRID`

> **指定 HFPC/DFPC 计算中所用的辅助网格。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * None
> * **建议**：推荐的基组、泛函与网格搭配请参阅参考文献。

DFPT_EXCHANGE

### `DFPT_EXCHANGE`

> **指定 HFPC/DFPC 计算中所用的辅助泛函。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * None
> * **建议**：推荐的基组、泛函与网格搭配请参阅参考文献。
