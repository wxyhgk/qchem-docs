---
title: "6.6.4 RI-MP2 的 GPU 实现"
---

## 6.6.4 RI-MP2 的 GPU 实现

（2026 年 7 月 4 日）

**Q-Chem** 目前提供了使用图形处理器（Graphics Processing Units, GPU）加速 RI-MP2 计算的可能性。当前该功能仅支持支持 CUDA 的 NVIDIA 显卡，例如（按自 2008 年以来的历史顺序）GeForce、Quadro、Tesla 和 Fermi 系列显卡。有关支持 CUDA 的显卡的更多信息，可访问

`http://www.nvidia.com/object/cuda_gpus.html`

需要注意的是，这些 GPU 有特定的电源与主板要求。

软件要求包括安装合适的 NVIDIA CUDA 驱动程序（至少 1.0 版本，当前为 3.2）以及线性代数库 CUBLAS（至少 1.0 版本，当前为 2.0）。这些可以一并从 NVIDIA 的开发者网站下载：

`http://developer.nvidia.com/object/cuda_3_2_downloads.html`

为了让仅拥有单精度 GPU 的用户也能获得*优于*单精度的结果，我们实现了一种混合精度算法。其基本思路是注意到 RI-MP2 矩阵中包含*大量*数值上“小”的元素和*少量*数值上“大”的元素。后者在仅使用单精度的计算中会极大地影响计算精度，但其计算所涉及的计算周期相对较少。因此，给定阈值 $\delta$，我们对“小”元素与“大”元素进行分离，并使用 GPU（以单精度）加速那些计算密集型的前者运算，而在 CPU（使用双精度）上计算后者。这样，我们就可以通过调节 $\delta$ 参数来决定所需的双精度成分多少，从而在计算速度与精度之间权衡取舍。

CUDA_RI-MP2

### `CUDA_RI-MP2`

> **启用 RI-MP2 的 GPU 实现**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **取值选项**：
>     * FALSE
>     * GPU 启用，MGEMM 关闭
>     * TRUE
>     * GPU 启用，MGEMM 开启
> * **建议**：若要用 GPU 运行 RI-MP2，必须将其设置为 1

USECUBLAS_THRESH

### `USECUBLAS_THRESH`

> **设置发送到 GPU 的矩阵规模阈值（规模过小则不值得发送到 GPU）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`250`
> * **取值选项**：
>     * n
>     * 用户自定义阈值
> * **建议**：使用默认值。更小的设置可能会严重阻碍 GPU 加速效果

USE_MGEMM

### `USE_MGEMM`

> **使用混合精度矩阵方案（MGEMM）。如果希望在单精度下进行计算（或者拥有仅支持单精度的 GPU），但要将 RI-MP2 计算的某些部分保留在双精度下，则开启此项）**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **取值选项**：
>     * FALSE
>     * MGEMM 禁用
>     * TRUE
>     * MGEMM 启用
> * **建议**：在使用单精度显卡时启用

MGEMM_THRESH

### `MGEMM_THRESH`

> **设置 MGEMM 阈值，用于确定矩阵元素中“大”与“小”的分离界限。较大的阈值将使结果更接近单精度结果。注意，期望的系数应乘以 10000 以确保其为整数值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`10000`
> * **取值选项**：
>     * $n$
>     * 用户指定阈值
> * **建议**：对于小分子以及至三重 $\zeta$（triple-$\zeta$）规模的基组，默认值即可保证结果与双精度值偏差不大。对于更大的分子以及更大的基组，则应谨慎地减小该数值。

???+ example "示例 6.6：RI-MP2 双精度计算"
    ```qchem
    $molecule
       0 1
       c
       h1  c  1.089665
       h2  c  1.089665  h1  109.47122063
       h3  c  1.089665  h1  109.47122063  h2   120.
       h4  c  1.089665  h1  109.47122063  h2  -120.
    $end
    
    $rem
       METHOD       rimp2
       BASIS        cc-pvdz
       AUX_BASIS    rimp2-cc-pvdz
       CUDA_RIMP2   1
    $end
    ```

???+ example "示例 6.7：使用 MGEMM 的 RI-MP2 计算"
    ```qchem
    $molecule
       0 1
       c
       h1  c  1.089665
       h2  c  1.089665  h1  109.47122063
       h3  c  1.089665  h1  109.47122063  h2   120.
       h4  c  1.089665  h1  109.47122063  h2  -120.
    $end
    
    $rem
       METHOD         rimp2
       BASIS          cc-pvdz
       AUX_BASIS      rimp2-cc-pvdz
       CUDA_RIMP2     1
       USE_MGEMM      1
       MGEMM_THRESH   10000
    $end
    ```
