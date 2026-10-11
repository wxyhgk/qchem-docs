---
title: "9.4.2 带一般约束的几何优化"
---

## 9.4.2 带一般约束的几何优化

(July 4, 2026)

CONSTRAINT 和 ENDCONSTRAINT 分别定义了 *$opt* 中约束部分的开始与结束，在该部分之内用户可以指定最多六种不同类型的约束：

**原子间距（interatomic distances）**

数值单位为埃（Ångstroms）；*value* $>0$：

`stre   atom1   atom2   value

`

**键角（angles）**

数值单位为度，$0\leq value\leq 180$；*atom2* 是弯曲角（bend）的中心原子：

`bend   atom1   atom2   atom3   value

`

**面外弯曲角（out-of-plane-bends）**

数值单位为度，$-180\leq value\leq 180$ *atom2*；指 *atom4* 与 *atom1–atom2–atom3* 平面之间的夹角：

`outp   atom1   atom2   atom3   atom4   value

`

**二面角（dihedral angles）**

数值单位为度，$-180\leq value\leq 180$；指 *atom1–atom2–atom3* 平面与 *atom2–atom3–atom4* 平面之间的夹角：

`tors   atom1   atom2   atom3   atom4   value

`

**共面弯曲角（coplanar bends）**

数值单位为度，$-180\leq value\leq 180$；指 *atom1–atom2–atom3* 在 *atom2–atom3–atom4* 平面内的弯曲：

`linc   atom1   atom2   atom3   atom4   value

`

**垂直弯曲角（perpendicular bends）**

数值单位为度，$-180\leq value\leq 180$；指 *atom1–atom2–atom3* 垂直于 *atom2–atom3–atom4* 平面的弯曲：

`linp   atom1   atom2   atom3   atom4   value

`

???+ example "示例 9.11: 带键长和键角约束的甲醇几何优化。"
    ```qchem
    $molecule
       0  1
       C   0.14192   0.33268   0.00000
       O   0.14192  -1.08832   0.00000
       H   1.18699   0.65619   0.00000
       H  -0.34843   0.74268   0.88786
       H  -0.34843   0.74268  -0.88786
       H  -0.77395  -1.38590   0.00000
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            hf
       BASIS             3-21g
       GEOM_OPT_PRINT    6
    $end
    
    $opt
       CONSTRAINT
       stre  1  6  1.8
       bend  2  1  4  110.0
       bend  2  1  5  110.0
       ENDCONSTRAINT
    $end
    ```
