---
title: "7.9.13 针对不稳定参考态及其他方法的 EOM-DIP 电荷稳定化"
---

## 7.9.13 针对不稳定参考态及其他方法的 EOM-DIP 电荷稳定化

(2026 年 7 月 4 日)

当参考态对于电子脱附（electron detachment）不稳定时，EOM-DIP 的性能会恶化，[[740]](../bib_references/bib.md#bib773)
 这通常出现在使用双阴离子参考态、通过 EOM-DIP 描述中性双自由基的情形。
这些态的典型特征是占据的 Hartree–Fock 能量级具有正（非束缚）本征值，
对应于一个不可归一化的波函数。
（这些本质上是离散化的连续态解，
在高斯基组（Basis Set）中被粗略地表示出来。

）
所有激发态方法在处理位于电离阈值或电子脱附阈值之上的激发态时，
都会遇到类似的问题。

为解决这一问题，可以采用电荷稳定化方法。[[740]](../bib_references/bib.md#bib773)

这一方法可用于任何电子结构方法，它引入一个额外的库仑（Coulomb）势来稳定波函数。共有三种实现方式：

- 对核电荷进行缩放（scaling），通过 *$rem* 变量 SCALE_NUCLEAR_CHARGE 实现。
- 用户自定义核电荷，通过设置 CHARGE_STABILIZE = TRUE 并在 *$nuclear_charges* 输入段中指定新电荷来激活。*$nuclear_charges* 输入段的格式与
*$van_der_waals* 段相同，后者在第 [11.2.10](../ch11_env/subsec_LD.md) 节中有描述。
- 添加一个"带电笼"（charged cage），*即*，在分子周围布置一组点电荷，通过设置
ADD_CHARGED_CAGE = TRUE 来激活。
提供两种类型的笼（球形与十二面体形）；笼的形状、半径、点数和总电荷均由用户设置。

对于 EOM 方法，当计算目标态密度时（*例如*设置 CC_EOM_PROP = TRUE 时），
会对外部库仑势对 EOM 能量的影响进行微扰估计。
电荷稳定化技术也可用于其他方法，包括基态密度泛函理论（Density Functional Theory, DFT）（以描述亚稳基态）和含时密度泛函理论（TDDFT）（以改进对自电离共振的描述）。
对于 EOM 之外的方法，不施加任何特殊修正，得到的只是"通常"的电子结构，但核电荷被修改或存在附加点电荷。
在这种情况下，建议使用不同的核电荷值进行若干次计算，以便将结果外推至真实的原子序数。

 在此过程中，只有那些稳定化程度足以得到束缚态波函数的计算才应用于外推。
对于产生非束缚占据能级（自洽场（SCF）本征值 $\epsilon_{i}>0$）的计算
不应认真对待，因为它们代表的是正交化后的离散化连续态，而非真正的束缚态解。
此类解的结果会随基组选择发生强烈变化，且这种变化本质上毫无意义。

以下描述和示例展示了电荷稳定化的全部三种机制。

### `SCALE_NUCLEAR_CHARGE`

> **对核电荷进行缩放。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $N$: 以某种方式缩放核电荷，所添加的电荷为 $N$ /100（以原子单位计）
> * **建议**: 对于 EOM 方法，可以配合此选项施加微扰修正（如上所述），但对于其他电子结构方法，得到的只是核电荷被修改后的传统计算。

???+ example "示例 7.89: 使用带电笼进行稳定化的 EOM-DIP 激发能与性质计算。"
    ```qchem
    $molecule
      -2 1
       C   0.000000     0.000000     0.106788
       H  -0.989216     0.000000    -0.320363
       H   0.989216     0.000000    -0.320363
    $end
    
    $rem
       METHOD                     eom-ccsd
       BASIS                      6-311g(d,p)
       SCF_ALGORITHM              diis_gdm
       SCF_CONVERGENCE            8
       CC_T_CONV                  8
       EOM_DAVIDSON_CONVERGENCE   5
       CC_SYMMETRY                false
       DIP_SINGLETS               [1]    ! Compute one EOM-DIP singlet state
       DIP_TRIPLETS               [1]    ! Compute one EOM-DIP triplet state
       CC_EOM_PROP                true   ! Compute excited state properties
       ADD_CHARGED_CAGE           2      ! 1 for dodecahedral, 2 for spherical
       CAGE_RADIUS                225    ! Radius = 2.25 A
       CAGE_CHARGE                500    ! Total Charge = 5 a.u.
       CAGE_POINTS                100    ! Place 100 point charges
       INTEGRAL_SYMMETRY          false ! charged cage may violate point-group symmetry
    $end
    ```

???+ example "示例 7.90: 通过修改核电荷稳定 SO ${}_{4}^{2-}$。"
    ```qchem
    $comment
       Charge stabilization of an unbound anion (sulfate) by changing nuclear charge
       for S.  Format for nuclear charges section is same as van_der_waals section.
    $end
    
    $molecule
       -2 1
       S     0.0000000000    0.0000000000    0.0000000000
       O     0.8960432838    0.8960432838    0.8960432838
       O    -0.8960432838   -0.8960432838    0.8960432838
       O    -0.8960432838    0.8960432838   -0.8960432838
       O     0.8960432838   -0.8960432838   -0.8960432838
    $end
    
    $rem
       METHOD             mp2
       BASIS              aug-cc-pvdz
       CHARGE_STABILIZE   1
    $end
    
    $nuclear_charges
       1
       16 16.5
    $end
    ```
