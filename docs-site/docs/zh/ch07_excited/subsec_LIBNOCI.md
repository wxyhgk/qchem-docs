---
title: "7.5.2 任务控制"
---

## 7.5.2 任务控制

（2026 年 7 月 4 日）

**Q-Chem** 提供了一个名为 **libnoci** 的专用程序包，用于运行 NOCI（非正交组态相互作用）计算，可通过 USE_LIBNOCI = TRUE 访问。
**libnoci** 的实现引入了灵活的任务控制机制，用户可自行定义用于为 NOCI 基组生成多个组态的方法。
首先，必须选择一组参考行列式（reference determinants），既可以通过单次自洽场（SCF）计算来完成，也可以根据 *$rem* 变量 NOCI_REFGEN 的要求，从文件中读取轨道系数组来生成。
在这些参考组态的基础上，随后通过 SCF 亚稳态动力学（metadynamics）方法，或通过对参考行列式施加激发，生成多个非正交组态，具体方式由 *$rem* 变量 NOCI_DETGEN 指定。
当在活性空间内通过激发生成多个组态时，活性轨道由 *$active_orbitals* 输入段控制。例如：

> ```qchem
> $active_orbitals
>     1 4 11 14
> $end
> ```

$\beta$ 轨道的编号以 $\alpha$ 分子轨道（MO）总数作为偏移量（*例如*，上述示例选取了 $\alpha$ 轨道 1 和 4，以及 $\beta$ 轨道 1 和 4，其中 $\alpha$ 分子轨道总数为 10，包含占据轨道与虚轨道）。所得到的多个行列式随后会在 SCF 级别上分别进行弛豫，除非使用 SKIP_SCFMAN = TRUE 显式跳过此步骤。最后，利用完整的多行列式组集运行 NOCI 计算。

**libnoci** 程序包还兼容新的 SCF 亚稳态动力学实现（见第 [4.9.3](../ch04_scf/subsubsec_SCFMetadynNOCI.md) 节），
以及全纯 Hartree–Fock（holomorphic Hartree–Fock）方法，该方法可在所有几何结构上对多个 Hartree–Fock 解进行连续延拓（见第 [4.9.4](../ch04_scf/sec_HoloHF.md) 节）。

### `USE_LIBNOCI`

> **启用 libnoci 以运行 NOCI 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `False`: 不使用 libnoci （采用 Q-Chem 原始实现）。
>     * `True`: 使用 libnoci 实现。
> * **建议**: 下文详述的各 $rem 变量仅在 libnoci 中可用。

### `NOCI_REFGEN`

> **控制初始参考行列式的生成方式。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 通过单次 SCF 计算生成初始参考行列式。
>     * `1`: 从先前的计算中读取（多个）初始参考行列式。
> * **建议**: 可通过 SCF_READMINIMA 指定要从先前计算中读取的具体参考行列式。

### `NOCI_DETGEN`

> **控制用于 NOCI 的多行列式的生成方式。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 仅使用初始参考行列式。
>     * `1`: 从每个参考行列式生成 CIS 激发组态。
>     * `2`: 从每个参考行列式生成全部 FCI 激发组态。
>     * `3`: 使用 SCF 亚稳态动力学生成
>     * $n$: 个多行列式，其中
>     * $n$: 通过 SCF_SAVEMINIMA =
>     * $n$: 指定。
>     * `4`: 从每个参考行列式生成全部 CAS 激发组态，其中活性轨道通过 $active_orbitals 输入段指定。
> * **建议**: 默认情况下，这些多行列式会在运行 NOCI 之前于 SCF 级别进行优化。可通过指定 SKIP_SCFMAN = TRUE 来关闭此行为。

### `NOCI_NEIGVAL`

> **指定要输出的 NOCI 本征值数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 增大该值可输出能量逐渐升高的 NOCI 能级。

### `NOCI_PRINT`

> **指定 NOCI 的调试输出级别。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 增大该值可获得更多调试信息。

???+ example "示例 7.39: 在 libnoci 实现中对 H ${}_{2}$ 运行 NOCI，多行列式由 SCF 亚稳态动力学生成。"
    ```qchem
    $molecule
       0 1
       H    0.0000000   0.0000000   0.0000000
       H    0.0000000   0.0000000   4.0000000
    $end
    
    $rem
       EXCHANGE                   hf
       CORRELATION                noci
       UNRESTRICTED               true
       BASIS                      sto-3g
       SCF_CONVERGENCE            10
       MAX_SCF_CYCLES             1000
       MOM_START                  1
       USE_LIBNOCI                true
       SCF_SAVEMINIMA             4
       SCF_MINFIND_RANDOMMIXING   30000
       SCF_MINFIND_MIXMETHOD      1
       NOCI_REFGEN                0
       NOCI_DETGEN                3
       NOCI_NEIGVAL               4
    $end
    ```
