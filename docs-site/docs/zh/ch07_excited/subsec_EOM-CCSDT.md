---
title: "7.9.23 用于高精度计算的 EOM-CCSDT（仅限 CCMAN2）"
---

## 7.9.23 用于高精度计算的 EOM-CCSDT
（仅限 CCMAN2）

（2026 年 7 月 4 日）

运动方程单、双、三激发（equation-of-motion singles, doubles and triples, EOM-CCSDT）方法[[884]](../bib_references/bib.md#bib917)

是 EOM-CCSD 方法的扩展，其在耦合簇（CC）层级和运动方程（EOM）层级均完整包含三激发（在单激发和双激发之外）。从概念上讲，EOM-CCSD 与 EOM-CCSDT 是相似的；二者唯一的区别在于截断层级。由于 CC 哈密顿矩阵是非厄米的，左、右本征矢并非彼此的厄米共轭，但可以选择它们构成一组相互双正交的集合。利用式 ([7.97](sec_EOMEE.md#eq747))，可以求得右本征矢，这对于获得相应目标态的能量（以及激发能）已经足够。而对于梯度和性质计算，还必须额外求解各对应态的左本征矢。

在 EOM-CCSDT 中，CCSDT 哈密顿矩阵构建至三激发块，从而给出 CC 哈密顿量的一体、二体和三体本征矢。因此，与 EOM-CCSD 的结果相比，EOM-CCSDT 计算得到的能量和性质精度几乎高出一个数量级。例如，EOM-CCSDT 对单激发态和单键断裂的精度约为 $\sim 0.01$ eV，对双激发态的精度为 0.1–0.2 eV。相比之下，在 EOM-CCSD 层级，这些误差分别达到 0.1–0.2 eV 和 $>1$ eV 的量级。EOM-CCSDT 的计算标度为 ${\cal{O}}({N^{8}})$，而 EOM-CCSD 为 ${\cal{O}}({N^{6}})$。与 EOM-CC(2,3) 不同，EOM-CCSDT 方法是严格尺寸可加（size-intensive）的，EOM-CCSD 也是如此；但其计算代价高昂，只有在谨慎管理内存的情况下才能使用。目前，EOM-CCSDT 提供 SF、EE、IP、EA、DIP 和 DEA 变体，[[884]](../bib_references/bib.md#bib917)

且仅支持单点能计算，可通过设置 METHOD = EOM-CCSDT 来调用。EOM-CCSDT 在新版耦合簇程序套件（CCMAN2）中实现，同时支持双精度和单精度计算。其他作业控制变量与 EOM-CCSD 类似。

下面给出采用 EOM-CCSDT 计算激发能的示例。

**注意：**

**对于非平凡（规模较大）的计算，建议使用
CC_BACKEND=XM。
**

???+ example "示例 7.152：使用 EOM-EE-CCSDT/STO-3G（单精度设置）
计算 BH 的第一单重激发态（B ${}_{1}$ ）与第一三重激发态（B ${}_{2}$ ）
能量。"
    ```qchem
    $comment
    Computation of energies singlet and a triplet excited states of BH
    using EOM-EE-CCSDT/STO-3G
    $end
    
    $molecule
    0 1
    B
    H  1  1.234347
    $end
    
    $rem
    basis=sto-3g
    job_type=sp
    method eom-ccsdt
    cc_single_prec=1
    eom_single_prec=1
    n_frozen_core fc
    ee_singlets=[0,0,1,0]
    ee_triplets=[0,0,0,1]
    $end
    
    ```

???+ example "示例 7.153：使用 EOM-SF-CCSDT/STO-3G（双精度设置）
计算 BH 的单重基态与最低三重态
能量。"
    ```qchem
    $comment
    Computation of spin-flipping excitation energies of
    BH using EOM-SF-CCSDT/STO-3G, UHF reference
    $end
    
    $molecule
    0 3
    B
    H 1 1.191857
    $end
    
    $rem
    jobtype=sp
    method eom-ccsdt
    basis=sto-3g
    sf_states=[1,0,0,1]
    eom_nguess_singles=4
    n_frozen_core fc
    $end
    ```

下面给出采用 EOM-CCSDT 方法计算电离能/电子亲和能的示例。

???+ example "示例 7.154：使用 EOM-IP-CCSDT/6-31G*（双精度设置）
计算 N ${}_{2}$ 的单重基态及最低四个 IP 态
能量。"
    ```qchem
    $molecule
    0 1
    N
    N 1  1.097685
    $end
    
    $rem
    method=eom-ccsdt
    IP_states=[4]
    basis=6-31G*
    cc_symmetry=false
    EOM_davidson_convergence=6
    job_type=sp
    $end
    ```

???+ example "示例 7.155：使用 EOM-EA-CCSDT/6-31G*（双精度设置）
计算 C ${}_{2}$ 的单重基态及最低四个 EA 态
能量。"
    ```qchem
    $molecule
    0 1
    C
    C 1  1.243
    $end
    
    $rem
    method=eom-ccsdt
    EA_states=[4]
    basis=6-31G*
    cc_symmetry=false
    EOM_davidson_convergence=6
    job_type=sp
    $end
    ```

???+ example "示例 7.156：使用 EOM-DIP-CCSDT/6-31G（双精度设置）
计算 O 的单重基态及最低两个 DIP 态
能量。"
    ```qchem
    $molecule
    -2 1
    O
    $end
    
    $rem
    method=eom-ccsdt
    basis=6-31g
    DIP_STATES=[2]
    cc_symmetry=false
    $end
    
    ```

???+ example "示例 7.157：使用 EOM-DEA-CCSDT/6-31G（双精度设置）
计算 C 的单重基态及最低两个 DEA 态
能量。"
    ```qchem
    $molecule
    2  1
    C
    $end
    
    $rem
    method=eom-ccsdt
    basis=6-31g
    DEA_STATES=[2]
    cc_symmetry=false
    $end
    
    ```
