---
title: "12.16.3 采用选定片段占据-虚轨道对的 ALMO-CIS/TDA"
---

## 12.16.3 采用选定片段占据-虚轨道对的 ALMO-CIS/TDA

(2026 年 7 月 4 日)

**Q-Chem** 6.0 及更高版本支持采用选定片段占据-虚轨道对的 ALMO-CIS/TDA 计算，*即*，在公式 ([12.85](Ch12.S16.SS1.md#eq:almo-cis)) 中仅考虑对应于所选占据轨道与虚轨道之间跃迁的激发振幅。要运行此类计算，需设置 ALMOCIS_FRAGOV $>0$，目前支持三种不同的模式：

ALMOCIS_FRAGOV

### `ALMOCIS_FRAGOV`

> **执行从第 1 个片段的占据轨道到整个体系虚轨道跃迁的 ALMO-CIS/TDA 计算**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 执行标准的 ALMO-CIS/TDA 计算（若
>     * LOCAL_CIS
>     * $>0$
>     * ）
>     * 1
>     * 从 $frag_ov_pairs 区段读取用户指定的活性片段占据-虚（O-V）对
>     * 2
>     * 仅在第
>     * 一
>     * 个片段上激发
>     * 3
>     * 从第
>     * 一
>     * 个片段的占据轨道激发到体系中所有虚轨道
> * **建议**: 无

*$frag_ov_pairs* 区段的格式：

> ```qchem
> $frag_ov_pairs
>    [number of frag_ov_pairs]
>    [occ_frg_idx1]  [vir_frg_idx1]
>    [occ_frg_idx2]  [vir_frg_idx2]
>    ...
> $end
> ```

这些改进的 ALMO-CIS/TDA 模型可用于模拟复杂环境中的激发态，例如溶液中发色团的局域激发或其向溶剂的电荷转移（charge-transfer-to-solvent, CTTS）激发。需要注意的是，此类计算必须采用迭代的 Davidson 算法，*即*，EIGSLV_METH = 1。

???+ example "示例 12.55: 采用用户指定占据-虚轨道对（O(1) -> V(1) 与 O(1) -> V(2)）对甲酰胺-水复合物进行 ALMO-TDA 计算"
    ```qchem
    $molecule
    0 1
    --
    0 1
      C         1.1508059365    0.2982718924    0.0240277739
      O         0.3545181649    1.2334803420   -0.0015882208
      N         0.8104369587   -1.0072797234    0.0043506838
      H         2.2327270535    0.4686363261    0.0666232655
      H        -0.1675092286   -1.2596328526   -0.0352400180
      H         1.5210524537   -1.7122494331    0.0139809901
    --
    0 1
      O        -1.9693273428   -0.2999882700   -0.2293071572
      H        -1.3827632725    0.4697313642   -0.1375254289
      H        -2.7470364523   -0.0962178118    0.2907490329
    $end
    
    $rem
    jobtype     sp
    basis       6-31G*
    method      pbe0
    frgm_method stoll
    cis_n_roots     4
    thresh         12
    local_cis       1
    almocis_fragov  1
    eigslv_meth     1  ! iterative method
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $frag_ov_pairs
    2
    1 1
    1 2
    $end
    ```
