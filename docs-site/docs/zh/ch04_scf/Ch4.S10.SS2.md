---
title: "4.10.2 作业控制"
---

## 4.10.2 作业控制

（2026 年 7 月 4 日）

xTB 计算通过常规的 *$rem* 段进行请求。唯一必需的关键词是 METHOD = XTB；其余所有控制项均为可选。电荷与多重度在 *$molecule* 段中以标准方式指定。在 xTB 模式下，**Q-Chem** 在构造占据模式时会自动使用价电子，因此用户只需给出化学上正确的分子电荷和多重度即可。

### `METHOD`

> **XTB**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **可选项**：
>     * 无。
> * **建议**：设置为 XTB 。

### `BASIS`

> **XTB**
>
> * **类型**：`STRING`
> * **默认值**：`XTB（隐含）`
> * **可选项**：
>     * 无
> * **建议**：对于 METHOD = XTB ，BASIS = XTB 是隐含指定的，可以省略。不允许使用其他基组。

### `XTB_FERMI_TEMP`

> **控制 xTB 计算中用于分数占据的费米展宽（Fermi-smearing）温度。**
>
> * **类型**：`INTEGER`
> * **默认值**：`300`
> * **可选项**：
>     * $n\geq 0$
>     * 以开尔文（Kelvin）为单位的温度。
> * **建议**：默认值通常是合适的。设置 XTB_FERMI_TEMP = 0 可恢复为整数占据。

标准的自洽场（SCF）控制项同样可用，例如 SCF_ALGORITHM 和 SCF_CONVERGENCE。SCF_ALGORITHM = DIIS 为默认设置，而对于困难体系，SCF_ALGORITHM = GDM 或 SCF_ALGORITHM = ROBUST 可能更为有效。
