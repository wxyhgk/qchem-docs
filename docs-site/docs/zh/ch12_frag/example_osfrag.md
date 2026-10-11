---
title: "12.2.1 概述"
---

## 12.2.1 概述

（2026 年 7 月 4 日）

若要请求使用上述任何方法，必须指定体系如何划分为片段（Fragment）。体系中的所有原子和所有电子都应被分配到某个片段中。每个片段必须包含整数个电子。在当前实现中，开壳层（Open-shell）和闭壳层（Closed-shell）片段均被允许。为了指定片段，片段描述符（Fragment descriptor）必须插入到 **Q-Chem** 输入文件的 *$molecule* 部分中。一个片段描述符由两行组成：第一行必须以两个连字符开头，后跟可选的注释；第二行必须包含该片段的电荷和多重度（Multiplicity）。至少必须指定两个片段。*$molecule* 部分中的片段描述符不会影响那些并非设计为使用片段化方法的计算任务。

```qchem
$molecule
   0 1
-- water molecule - proton donor
   0 1
   O1
   H2 O1 0.96
   H3 O1 0.96 H2 105.4
-- water molecule - proton acceptor
   0 1
   O4 O1 ROO  H2 105.4 H3   0.0
   X5 O4 2.00 O1 120.0 H2 180.0
   H6 O4 0.96 X5  55.6 O1  90.0
   H7 O4 0.96 X5  55.6 01 -90.0

   ROO = 2.4
$end
```

开壳层体系的 alpha 电子数必须大于 beta 电子数。然而，通过将多重度指定为负值，可以使体系中的单个片段包含过剩的 beta 电子。例如，多重度 $-2$ 表示有一个过剩的 beta 电子，如下例中的第二个片段所示。

```qchem
$molecule
   0 1
--  An alpha spin H atom
   0 2
   H1
--  A beta spin H atom
   0 -2
   H2 H1  1.50
$end
```
