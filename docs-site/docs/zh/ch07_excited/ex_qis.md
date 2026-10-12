---
title: "7.9.31 与量子计算软件包 OpenFermion 的接口"
---

## 7.9.31 与量子计算软件包 OpenFermion 的接口

（2026 年 7 月 4 日）

**Q-Chem** 提供了一项功能，可以转储（dump）与 OpenFermion 软件包[[617]](../bib_references/bib.md#bib969)

（及类似软件）进行接口对接以用于量子计算所需的全部量。该功能由关键字 PRINT_QIS 控制。
将其设置为 TRUE 即可激活转储操作：Fock 算符、双电子积分以及分子轨道能量会被保存为主目录（home directory）下的独立文件。OpenFermion
（开发版本，即将合并入官方 github 仓库）包含一个导入模块，该模块能够识别并读取这些文件，同时还附带若干单元测试。
示例 7.9.31 以水分子为例演示了这一功能。

**注意：

不应冻结核心电子（Core should not be frozen）。
**

### `PRINT_QIS`

> **请求转储 OpenFermion 所需的数据。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `TRUE`: 将 QIS 所需的数据输出到用户目录中。
> * **建议**: 请注意生成文件的体积大小。

???+ example "示例 7.180：水分子的 CCSD/STO-3G 计算，并输出供 OpenFermion 使用的数据。"
    ```qchem
    $comment
    Water molecule in STO-3G basis
    $end
    
    $molecule
    0 1
      H    0.5355326   -0.0489506    0.7341984
      O    0.0563012    0.0114119   -0.1303093
      H   -0.9024750   -0.0253772    0.1144725
    $end
    
    $rem
    method = ccsd
    basis = sto-3g
    print_qis = true
    gui = 2
    n_frozen_core = 0
    $end
    ```
