---
title: "6.7.1 概述"
---

## 6.7.1 概述

(July 4, 2026)

MP2(attenuator, basis) 通过将库仑算符（Coulomb operator）拆分为两部分并仅保留短程双电子相互作用来近似 MP2，类似于 CASE 近似，[[350]](../bib_references/bib.md#bib354)
 但无需修改底层的自洽场（SCF）计算。虽然 MP2 是一种相对高效的关联能（correlation energy）估算方法，但它随基组（Basis Set）尺寸的收敛速度较慢——并且即使在完整基组极限下，其对于长程相互作用的物理描述也存在根本性的不准确。基组重叠误差（basis set superposition error）以及 MP2 层面对长程相互作用的处理，通常都会人为地增大非相互作用的关联能。衰减 MP2（Attenuated MP2）在分子间和分子内相互作用方面对 MP2 有所改进，对非共价复合物的相对能和结合能表现出显著更好的性能，常常优于 MP2 的完整基组估算值。[[466]](../bib_references/bib.md#bib478)

衰减 MP2 记作 MP2(attenuator, basis)，**Q-Chem** 中基于互补 terf 函数实现了该方法，其定义如下：

<a id="Ch6.E32"></a>

$$
\rm{s}(r)=\rm{terfc}(r,r_{0})=\frac{1}{2}\left\{\rm{erfc}\left[\omega(r-r_{0})\right]+\rm{erfc}\left[\omega(r+r_{0})\right]\right\} \tag{6.32}
$$

通过选择 terfc 短程算符，我们能够在最优地保留库仑算符短程行为的同时，在距离 $r_{0}$ 附近平滑而迅速地将其关闭。由于这直接针对基组重叠误差，因此必须针对特定基组进行参数化。目前已针对 aug-cc-pVDZ[[466]](../bib_references/bib.md#bib478)
 和
aug-cc-pVTZ[[465]](../bib_references/bib.md#bib479)
 基组完成了参数化。在完成进一步测试之前，不推荐将其他基组用于一般用途。

能量和梯度均可使用，无论是否采用分辨率恒等（resolution of the identity）近似，分别通过关联关键字 ATTMP2 和 ATTRIMP2 启用。

???+ example "示例 6.21: RI-MP2(terfc, aug-cc-pVDZ) 能量计算示例"
    ```qchem
    $molecule
       0 1
       O    -1.551007   -0.114520    0.000000
       H    -1.934259    0.762503    0.000000
       H    -0.599677    0.040712    0.000000
    $end
    
    $rem
       METHOD          attrimp2
       BASIS           aug-cc-pvdz
       AUX_BASIS       rimp2-aug-cc-pvdz
    $end
    ```

???+ example "示例 6.22: MP2(terfc, aug-cc-pVTZ) 几何优化示例"
    ```qchem
    $molecule
       0 1
       H    0.0   0.0   0.0
       H    0.0   0.0   0.9
    $end
    
    $rem
       JOBTYPE         opt
       METHOD          attmp2
       BASIS           aug-cc-pvtz
    $end
    ```
