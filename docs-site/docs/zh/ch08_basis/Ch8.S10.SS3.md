---
title: "8.10.3 内置 ECP"
---

## 8.10.3 内置有效核势（ECP）

(2026 年 7 月 4 日)

## 8.10.3.1 简介

**Q-Chem** 配备了若干标准的有效核势（Effective Core Potential, ECP）集合，通过在 *$rem* 块中使用 ECP 关键字来指定。本章末尾对这些内置 ECP 进行了较为详细的介绍，它们分为四大族：

- Hay-Wadt（即 Los Alamos）系列（fit-HWMB 和 fit-LANL2DZ）
- Stevens-Basch-Krauss-Jansien-Cundari 系列（fit-SBKJC）
- Christiansen-Ross-Ermler-Nash-Bursten 系列（fit-CRENBS 和 fit-CRENBL）
- Stuttgart-Bonn 系列（SRLC 和 SRSC）
- Karlsruhe def2-ECP，与 def2 基组（Basis Set）配合使用

其中大多数系列的参考文献以及其定义与特性信息可在 Basis Set Exchange 上找到：[[1123]](../bib_references/bib.md#bib1170)

`https://www.basissetexchange.org`

每个内置 ECP 都配有一个与之匹配的、用于价电子的轨道基组。一般而言，建议将两者搭配使用；如果选择了非匹配基组，**Q-Chem** 会在输出文件中打印一条警告信息。若完全省略 *$rem* 中的 BASIS 关键字，**Q-Chem** 会自动提供与之匹配的基组。

以下 *$rem* 变量用于控制所使用的 ECP：

### `ECP`

> **定义所使用的有效核势及其关联基组**
>
> * **类型**：`STRING`
> * **默认值**：`No ECP`
> * **可选值**：
>     * General, Gen
>     * 用户自定义（User defined.，需要 $ecp 关键字）
>     * Symbol
>     * 使用上文讨论的标准 ECP。
> * **建议**：推荐对第一排过渡金属及更重的元素使用 ECP。更多细节请参阅相关综述文献。

## 8.10.3.2 组合使用 ECP

如果需要，你可以为体系中的不同元素使用不同的 ECP 集合。当你想使用某个特定 ECP，却发现它并非对分子中的所有元素都可用时，这一点尤其有用。要组合不同的 ECP 集合，需将 ECP 和 BASIS 关键字设置为 "GEN"（或等价地设置为 "GENERAL"），然后在输入文件中添加一个 *$ecp* 块和一个 *$basis* 块。在这两个块中，你必须指明希望使用的 ECP 和轨道基组，各元素之间用 "****" 分隔。此外还有一个内置的组合方式，通过指定 ECP = fit-LACVP 即可调用。它会自动为 H–Ar 之间的原子分配 6-31G 基组，为更重的原子分配 fit-LANL2DZ。

## 8.10.3.3 示例

???+ example "示例 8.6: 在键长 2.4 Å 下计算 AgCl 的 HF/fit-LANL2DZ 能量。"
    ```qchem
    $molecule
       0  1
       Ag
       Cl  Ag  r
    
       r  =  2.4
    $end
    
    $rem
       METHOD   hf           Hartree-Fock calculation
       ECP      fit-lanl2dz  Using the Hay-Wadt ECP
       BASIS   lanl2dz       And the matching basis set
    $end
    ```

???+ example "示例 8.7: 使用 B3LYP/def2-SV(P) 计算 HI 的单点能（对 I 使用 def2-ECP）。"
    ```qchem
    $molecule
       0 1
       H    0.0    0.0    0.0
       I    0.0    0.0    1.5
    $end
    
    $rem
       METHOD           b3lyp
       BASIS            def2-sv(p)
       ECP              def2-ecp
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 8.8: 使用 HF/fit-LANL2DZ 优化 Se ${}_{8}$ 的结构，随后在 MP2/fit-LANL2DZ 水平上进行单点能计算。"
    ```qchem
    $molecule
       0  1
       x1
       x2   x1  xx
       Se1  x1  sx  x2  90.
       Se2  x1  sx  x2  90.  Se1  90.
       Se3  x1  sx  x2  90.  Se2  90.
       Se4  x1  sx  x2  90.  Se3  90.
       Se5  x2  sx  x1  90.  Se1  45.
       Se6  x2  sx  x1  90.  Se5  90.
       Se7  x2  sx  x1  90.  Se6  90.
       Se8  x2  sx  x1  90.  Se7  90.
    
       xx = 1.2
       sx = 2.8
    $end
    
    $rem
       JOBTYPE    opt
       METHOD     hf
       ECP        fit-lanl2dz
       BASIS         lanl2dz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD        mp2       MP2 correlation energy
       ECP           fit-lanl2dz   Hay-Wadt ECP and basis
       BASIS         lanl2dz
       SCF_GUESS     read      Read in the MOs
    $end
    ```

???+ example "示例 8.9: 使用 Stuttgart 相对论 ECP 计算 CdBr ${}_{2}$ 的 HF 几何结构。
Cd 原子采用小核（small-core）ECP 与基组，Br 原子采用大核（large-core）ECP 与基组。"
    ```qchem
    $molecule
       0  1
       Cd
       Br1  Cd  r
       Br2  Cd  r  Br1  180.0
    
       r = 2.4
    $end
    
    $rem
       JOBTYPE    opt   Geometry optimization
       METHOD     hf    Hartree-Fock theory
       ECP        gen   Combine ECPs
       BASIS      gen   Combine basis sets
       PURECART   1     Use pure d functions
    $end
    
    $ecp
       Cd
       srsc
       ****
       Br
       srlc
       ****
    $end
    
    $basis
       Cd
       srsc
       ****
       Br
       srlc
       ****
    $end
    ```
