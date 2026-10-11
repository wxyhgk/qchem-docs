---
title: "9.4.1 引言"
---

## 9.4.1 引言

(July 4, 2026)

约束优化（Constrained Optimization）是指在优化分子结构（过渡态或能量极小点）时，固定某些参数（如键长、键角或二面角）的优化过程。**Q-Chem** 能够在离域内坐标（Delocalized Internal Coordinates）中直接处理约束，所采用的方法是拉格朗日乘子法（Lagrange Multipliers）（参见第 [9.1.5 节](sec_geom_opt_theory_constrained.md)）。**Q-Chem** 约束优化的特点包括：

- •

起始几何结构无需满足所要求的约束条件。
- •

约束优化在离域内坐标中进行，对于大分子的优化而言，这通常是最高效的坐标系。
- •

**Q-Chem** 的自由格式 *$opt* 输入节（Input Section）使用户能够便捷地施加约束。

约束通过 *$opt* 输入节来施加，其格式如下所示，该输入节各部分的说明也见下文。

**注意：

与 **Q-Chem** 输入文件的其余部分一样，*$opt* 节对大小写不敏感，但每行的开头不应有空格。
**

> ```qchem
> $opt
> CONSTRAINT
> stre  atom1  atom2  value
> ...
> bend  atom1  atom2  atom3  value
> ...
> outp  atom1  atom2  atom3  atom4  value
> ...
> tors  atom1  atom2  atom3  atom4  value
> ...
> linc  atom1  atom2  atom3  atom4  value
> ...
> linp  atom1  atom2  atom3  atom4  value
> ...
> ENDCONSTRAINT
> 
> FIXED
> atom   coordinate_reference
> ...
> ENDFIXED
> 
> DUMMY
> idum   type   list_length   defining_list
> ...
> ENDDUMMY
> 
> CONNECT
> atom   list_length   list
> ...
> ENDCONNECT
> $end
> ```
