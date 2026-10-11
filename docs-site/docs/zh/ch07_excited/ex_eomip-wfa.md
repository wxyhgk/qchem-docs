---
title: "7.9.30 EOM/CI 波函数的解释与轨道编号"
---

## 7.9.30 EOM/CI 波函数的解释与轨道编号

(2026 年 7 月 4 日)

要确定电子态的特征（*e.g.*，$\rm HOMO\rightarrow LUMO$ 激发、开壳层双自由基，*etc.*），始终需要对主波函数振幅进行分析。CCMAN 模块会使用其内部的轨道编号方案来打印主要的 EOM/CI 振幅，该编号方案会在输出开头打印出来。典型的 CCMAN EOM-CCSD 输出如下所示：

> ```qchem
> Root 1 Conv-d yes Tot Ene= -113.722767530 Hartree (Ex Ene 7.9548 eV),
> U1^2=0.858795, U2^2=0.141205 ||Res||=4.4E-07
> Right U1:
>        Value                   i            ->    a
>        0.5358                  7( B2  ) B   ->   17( B2  ) B
>        0.5358                  7( B2  ) A   ->   17( B2  ) A
>       -0.2278                  7( B2  ) B   ->   18( B2  ) B
>       -0.2278                  7( B2  ) A   ->   18( B2  ) A
> ```

这意味着该电子态是由占据轨道 #7（具有 $b_{2}$ 对称性）向虚拟轨道 #17（同样具有 $b_{2}$ 对称性）的激发所产生的。两个最大的振幅分别对应于 $\beta\rightarrow\beta$ 和 $\alpha\rightarrow\alpha$ 激发（自旋部分用 $A$ 或 $B$ 表示）。该任务的轨道编号由以下映射表定义：

> ```qchem
> The orbitals are ordered and numbered as follows:
> Alpha orbitals:
> Number  Energy    Type    Symmetry  ANLMAN number  Total number:
>   0    -20.613     AOCC      A1      1A1     1
>   1    -11.367     AOCC      A1      2A1     2
>   2     -1.324     AOCC      A1      3A1     3
>   3     -0.944     AOCC      A1      4A1     4
>   4     -0.600     AOCC      A1      5A1     5
>   5     -0.720     AOCC      B1      1B1     6
>   6     -0.473     AOCC      B1      2B1     7
>   7     -0.473     AOCC      B2      1B2     8
> 
>   0      0.071     AVIRT     A1      6A1     9
>   1      0.100     AVIRT     A1      7A1     10
>   2      0.290     AVIRT     A1      8A1     11
>   3      0.327     AVIRT     A1      9A1     12
>   4      0.367     AVIRT     A1     10A1     13
>   5      0.454     AVIRT     A1     11A1     14
>   6      0.808     AVIRT     A1     12A1     15
>   7      1.196     AVIRT     A1     13A1     16
>   8      1.295     AVIRT     A1     14A1     17
>   9      1.562     AVIRT     A1     15A1     18
>  10      2.003     AVIRT     A1     16A1     19
>  11      0.100     AVIRT     B1      3B1     20
>  12      0.319     AVIRT     B1      4B1     21
>  13      0.395     AVIRT     B1      5B1     22
>  14      0.881     AVIRT     B1      6B1     23
>  15      1.291     AVIRT     B1      7B1     24
>  16      1.550     AVIRT     B1      8B1     25
>  17      0.040     AVIRT     B2      2B2     26
>  18      0.137     AVIRT     B2      3B2     27
>  19      0.330     AVIRT     B2      4B2     28
>  20      0.853     AVIRT     B2      5B2     29
>  21      1.491     AVIRT     B2      6B2     30
> ```

第一列是 CCMAN 的内部编号（*e.g.*，上例中的 7 和 17）。其后依次是轨道能量、轨道类型（冻结、限制、活性、占据、虚拟）以及轨道对称性。请注意，轨道先按对称性分块，然后在每个对称性块内按能量排序，（*i.e.*，先是所有占据的 $a_{1}$，然后是所有 $a_{2}$，*etc.*），并从 0 开始编号。占据轨道与虚拟轨道分别编号，并且冻结轨道不纳入 CCMAN 编号。最后两列给出以最终 ANLMAN 打印结果为基准的编号（从 1 开始），*e.g.*，我们的占据轨道 #7 在最终打印结果中将被编号为 1$B_{2}$。最后一列给出绝对轨道编号（所有占据轨道与所有虚拟轨道合在一起，从 1 开始），外部可视化工具通常使用这一编号。

CCMAN2 在每个不可约表示（irrep）内按能量对轨道编号，并对占据轨道和虚拟轨道采用统一的编号方案。这一编号与 SCF 波函数分析最终打印结果中的编号完全一致。轨道能量打印在相应振幅的旁边。例如，典型的 CCMAN2 EOM-CCSD 输出如下所示：

> ```qchem
> EOMEE-CCSD transition 2/A1
>  Total energy = -75.87450159 a.u.  Excitation energy = 11.2971 eV.
>  R1^2 = 0.9396  R2^2 = 0.0604  Res^2 = 9.51e-08
> 
>  Amplitude    Orbitals with energies
>   0.6486       1 (B2) A                  ->    2 (B2) A
>               -0.5101                          0.1729
>   0.6486       1 (B2) B                  ->    2 (B2) B
>               -0.5101                          0.1729
>  -0.1268       3 (A1) A                  ->    4 (A1) A
>               -0.5863                          0.0404
>  -0.1268       3 (A1) B                  ->    4 (A1) B
>               -0.5863                          0.0404
> ```

这表明对于该电子态，最大的 EOM 振幅对应于从第一个 b${}_{2}$ 轨道（轨道能量 $-0.5101$）到第二个 b${}_{2}$ 轨道（轨道能量 0.1729）的跃迁。

对 EOM-CC 计算最完整的分析可通过部署 **libwfa** 模块中包含的通用波函数分析工具来实现，该工具在第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节中介绍。通过设置 STATE_ANALYSIS = TRUE 可启用 EOM-CC 态分析。此外，还应相应地设置用于控制态性质与态间性质计算的关键词。

**注意：

波函数分析仅对 CCMAN2 可用。
**

???+ example "示例 7.179: EOM-IP 态（He ${}_{3}^{+}$ ）的波函数分析。"
    ```qchem
    $molecule
       0 1
       He
       He   1       R1
       He   2       R1      1       A
    
       R1 = 1.236447
       A  = 180.00
    $end
    
    $rem
       METHOD            = EOM-CCSD
       BASIS             = 6-31G
       IP_STATES         = [1,0,0,0,0,1,0,0]
       CC_EOM_PROP       = true   Analyze state properties (state OPDM)
       CC_REF_PROP       = true   Analyze reference state and difference OPDM
       CC_STATE_TO_OPT   = [1,1]  Compute transition properties wrt 1st EOM state of 1st irrep
       CC_TRANS_PROP     = true   Analyze transitions (transition OPDM)
       STATE_ANALYSIS    = true
       MOLDEN_FORMAT     = true
       NTO_PAIRS         = 2
    $end
    ```
