---
title: "4.7.5 作业控制与示例"
---

## 4.7.5 作业控制与示例

（2026 年 7 月 4 日）

双基组（dual-basis）计算通过以下 *$rem* 变量进行控制。
DUAL_BASIS_ENERGY 用于开启双基组近似。请注意，
若仅使用 BASIS2 而未设置 DUAL_BASIS_ENERGY，则*仅*会利用
基组投影来生成初始猜测，而不会启用双基组近似（参见第 [4.4.5](sect_projection.md) 节）。
OVPROJECTION 是双基组计算的默认投影机制；
不建议对其进行更改。
SCF 变量（*例如*，THRESH）的指定将同时应用于两个基组中的计算。

### `DUAL_BASIS_ENERGY`

> **启用双基组 SCF（HF 或 DFT）能量校正。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * HF 与 DFT 支持解析一阶导数（参见
>     * JOBTYPE
>     * ）
>     * 可与 MP2 或 RI-MP2 结合使用
>     * 参见 BASIS、BASIS2、BASISPROJTYPE
> * **建议**：使用双基组方法以较小的基组代价捕获大基组效应。在与 RI-MP2 结合时尤为有用，因为在 RI-MP2 中 HF 计算往往占主导。小基组计算应仅使用真子集（proper subset）基组。

## 4.7.5.1 示例

???+ example "示例 4.23：双基组 B3LYP 单点能计算的输入。"
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       METHOD              b3lyp
       BASIS               6-31G*
       BASIS2              r64G
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "示例 4.24：使用极小 6-4G 小基组的双基组 B3LYP 单点能计算输入。"
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           rimp2-aug-cc-pVDZ
       BASIS               aug-cc-pVDZ
       BASIS2              racc-pVDZ
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "示例 4.25：双基组 RI-MP2 几何优化的输入。"
    ```qchem
    $molecule
       0 1
       H
       H   1   0.75
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           rimp2-aug-cc-pVDZ
       BASIS               aug-cc-pVDZ
       BASIS2              racc-pVDZ
       DUAL_BASIS_ENERGY   true
    $end
    ```

???+ example "示例 4.26：使用混合基组的双基组 RI-MP2 单点能计算输入。"
    ```qchem
    $molecule
       0 1
       H
       O   1   1.1
       H   2   1.1  1  104.5
    $end
    
    $rem
       JOBTYPE             opt
       METHOD              rimp2
       AUX_BASIS           aux_mixed
       BASIS               mixed
       BASIS2              basis2_mixed
       DUAL_BASIS_ENERGY   true
    $end
    
    $basis
     H 1
     cc-pVTZ
     ****
     O 2
     aug-cc-pVTZ
     ****
     H 3
     cc-pVTZ
     ****
    $end
    
    $basis2
     H 1
     rcc-pVTZ
     ****
     O 2
     racc-pVTZ
     ****
     H 3
     rcc-pVTZ
     ****
    $end
    
    $aux_basis
     H 1
     rimp2-cc-pVTZ
     ****
     O 2
     rimp2-aug-cc-pVTZ
     ****
     H 3
     rimp2-cc-pVTZ
     ****
    $end
    ```
