---
title: "7.9.14 CC、IP-CC 与 SF-CC 计算中的冻结自然轨道"
---

## 7.9.14 CC、IP-CC 与 SF-CC 计算中的冻结自然轨道

(July 4, 2026)

如果使用冻结自然轨道（frozen natural orbital, FNO）方法截断虚空间，可大幅节省计算量（参见第 [6.15.1 节](../ch06_correlation/sec_FNOCC.md)）。
FNO 方法向 EOM-CC 框架下电离态的扩展也已被提出并进行了基准测试。[[748]](../bib_references/bib.md#bib781)
除基态耦合簇（coupled-cluster）计算之外，FNO 还可用于
EOM-IP-CCSD、EOM-IP-CCSD(dT/fT) 以及 EOM-IP-CC(2,3)。在 EOM-IP-CC 中，FNO 是针对参考（中性）态计算的，
随后用于描述多个感兴趣的目标（电离）态。不同的截断方案在第 [6.15.1 节](../ch06_correlation/sec_FNOCC.md) 中有详细描述。

为降低 EOM-SF-CCSD 计算的成本，人们提出了一种特殊的 FNO 变体——开壳层冻结自然轨道近似（open-shell frozen natural orbital approximation, OSFNO）。[[1104]](../bib_references/bib.md#bib1153)

该方法采用两步方案。
首先，通过对 alpha 占据轨道与 beta 虚轨道的重叠矩阵进行奇异值分解，找出参考态的开壳层轨道。
这些轨道包含了 EOM-SF 波函数的主要振幅。
然后，在分离出开壳层轨道之后，通过对 MP2 密度矩阵的单重态部分（以 alpha-beta 自旋轨道对的形式）进行奇异值分解，对其余虚空间进行变换。
参考文献 [[1104]](../bib_references/bib.md#bib1153) 中的基准测试表明，
该方案可实现与 FNO 相近的加速比，同时对共价型和离子型 EOM-SF 态的相对能量引入的误差极小。
特别地，在典型的 OSFNO 截断（保留 99% 的总占据数）下，单分子磁体的单重态–三重态能隙误差小于 18 cm${}^{-1}$。
性质计算的误差同样很小。
OSFNO 通过 rem 变量 CC_OSFNO = TRUE 启用。
CC_FNO_THRESH 与 CC_FNO_USEPOP 关键字的用法与传统 FNO 相同。

由于实现的限制，点群对称性无法与 FNO/OSFNO 一同使用，因此会被自动禁用。
请相应调整您的输入，设置 CC_SYMMETRY = FALSE。

OSFNO 可以与轨道局域化结合以生成有效哈密顿量，如第 [13.6 节](../ch13_specialized/sec_EffHam.md) 所述。

### `CC_OSFNO`

> **启用 OSFNO。仅适用于开壳层参考态。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: activate
> * **建议**: 用于从开壳层参考态出发的 EOM-SF-CCSD 计算。仅在 CCMAN2 中可用。

???+ example "示例 7.91: 一个 EOM-SF-CCSD 任务，演示 OSFNO 在能量与性质计算中的用法。"
    ```qchem
    $molecule
       0 3
       C
       H 1 rCH
       H 1 rCH 2 aHCH
    
       rCH = 1.0775
       aHCH = 133.29
    $end
    
    $rem
       METHOD           eom-ccsd
       BASIS            cc-PVTZ
       SF_STATES        [4]
       CC_SYMMETRY      false
       CC_EOM_PROP      1
       CC_EOM_PROP_TE   1
       CC_OSFNO         true
       CC_FNO_THRESH    9900
    $end
    ```
