---
title: "2.2.3 可自定义的归档文件（Customizable Archive Files）"
---

## 2.2.3 可自定义的归档文件

（2026 年 7 月 4 日）

**Q-Chem** 支持可自定义的归档文件（archive file），允许保存计算过程中的各类数据。归档文件的内容由输入文件中 *$schema* 区段所指定的数据关键字（data keyword）控制。该 schema 的格式采用 YAML，目前缩进层级必须严格为 2 个空格。

以下数据关键字在 *$schema* 区段中有效：

| ApproxHessian | ContractionCoefficients | Coordinates |
| --- | --- | --- |
| DensityMatrix | Energy | FockMatrix |
| Gradient | NAlpha | NBeta |
| Nuclei | OrbitalCoefficients | OrbitalEnergies |
| OrthonormalizationMatrix | OverlapMatrix | PrimitiveExponents |
| PrimitivesPerShell | ShellCoordinates | ShellToAtomMap |
| ShellTypes | SpContractionCoefficients | TotalCharge |

数据可以采用嵌套结构，例如不仅可以输出最终的分子轨道（MO）系数，还可以输出自洽场（SCF）每一圈的系数。
以下容器层级（container level）可供使用，用于控制这种嵌套程度：

| BasisSet | GeomOpt | GeomOptStep |
| --- | --- | --- |
| SCF | SCFStep | Structure |

归档文件写入 `$QCSCRATCH/savename/qch5_archive.h5`，其内容可使用标准的 HDF5 工具访问。

???+ example "示例 2.2：展示在 $schema 区段中为归档文件自定义 schema 规范的示例输入。在第一个作业中，SCF 数据采用了嵌套结构，从而请求在每一圈打印 MO 系数。在第二个作业中，请求了与格式化检查点文件（formatted checkpoint file）类似基组（Basis Set）数据。"
    ```qchem
    $molecule
    0 1
    C          0.00000       -0.00000       -0.68020
    C         -0.00000        0.00000        0.68020
    H         -0.00000       -0.89374       -1.19620
    H          0.00000        0.89374       -1.19620
    H         -0.00000       -0.89374        1.19620
    H          0.00000        0.89374        1.19620
    $end
    
    $rem
      JOBTYPE  opt
      METHOD   hf
      BASIS    sto-3g
    $end
    
    $schema
    GeomOpt
      GeomOptStep
        SCF
          Energy
          OrbitalCoefficients
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
      METHOD    hf
      BASIS     sto-3g
    $end
    
    $schema
    SCF
      Energy
      FockMatrix
      DensityMatrix
      OrbitalCoefficients
    BasisSet
      ShellTypes
      ShellToAtomMap
      ShellCoordinates
      PrimitivesPerShell
      PrimitiveExponents
      ContractionCoefficients
      SpContractionCoefficients
    $end
    
    
    ```
