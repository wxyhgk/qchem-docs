---
title: "6.9.2 MPR-BWs2 任务控制"
---

## 6.9.2 MPR-BWs2 任务控制

(July 4, 2026)

MPR-BWs2 已作为 RI-BW-s2 程序的一个特定分支实现。
其调用方式为：在 *$rem* 段中设置 METHOD = RIBWS2，
并在 *$bws2* 段中写入 METHOD = MPR-BWS2。
迭代与非迭代参数，以及用于控制迭代方法收敛行为的附加变量，
同样在 *$bws2* 段中定义。与 MPR-BWs2 无关的变量请参见 [6.8](topic_bws2.md)。

### `METHOD`

> **定义所使用的关联能表达式。输入段：$bws2**
>
> * **类型**: `STRING`
> * **默认值**: `BWS2`
> * **可选值**:
>     * MPR-BWS2
> * **建议**: 若要启用 MPR-BWs2，需将 method 关键字设置为 MPR-BWS2 或 MPRBWS2

### `MPR_A0`

> **控制 $A_{0}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `1000`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{0}$
>     * 的取值。
> * **建议**: 由于在 BW-s2 理论中 $A_{0}$ 等于 $\alpha$，其标准值设为 $\alpha=A_{0}=1$，此时可重现 BW-s2。如果输入文件中同时定义了 MPR_A0 和 ALPHA，则以最后读取到的为准。

### `MPR_A1`

> **控制 $A_{1}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{1}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_A2`

> **控制 $A_{2}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{2}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_A3`

> **控制 $A_{3}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{3}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_A4`

> **控制 $A_{4}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{4}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_B0`

> **控制 $B_{0}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{0}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_B1`

> **控制 $B_{1}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{1}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_B3`

> **控制 $B_{3}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{3}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_B4`

> **控制 $B_{4}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{4}$
>     * 的取值。
> * **建议**: 取值过大会导致收敛问题。

### `MPR_A0_NONITER`

> **控制非迭代贡献中 $A_{0}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{0}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_A1_NONITER`

> **控制非迭代贡献中 $A_{1}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{1}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_A2_NONITER`

> **控制非迭代贡献中 $A_{2}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{2}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_A3_NONITER`

> **控制非迭代贡献中 $A_{3}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{3}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_A4_NONITER`

> **控制非迭代贡献中 $A_{4}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $A_{4}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_B0_NONITER`

> **控制非迭代贡献中 $B_{0}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{0}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_B1_NONITER`

> **控制非迭代贡献中 $B_{1}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{1}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_B3_NONITER`

> **控制非迭代贡献中 $B_{3}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{3}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `MPR_B4_NONITER`

> **控制非迭代贡献中 $B_{4}$ 参数的取值。输入段：$bws2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 其中
>     * $n/1000$
>     * 即为
>     * $B_{4}$
>     * 的非迭代取值。
> * **建议**: 可取任意值。

### `PARAM_GRADIENT`

> **控制是否计算能量对各参数的导数。输入段：$bws2**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * TRUE
>     * 计算迭代与非迭代参数的梯度。
>     * FALSE
>     * 不计算参数梯度。
> * **建议**: 如有需要，设置为 TRUE。

???+ example "示例 6.24：在甲醛上进行 $A_{0}=1$、$B_{0}=-1$ 的 MPR-BWs2 计算。"
    ```qchem
    $comment
        Standard MPR-BWs2 calculation
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              1000                ! A_0 = 1.0
    MPR_B0              -1000               ! B_0 = -1.0
    MAX_CYCLES          50
    $end
    ```

???+ example "示例 6.25：包含非迭代贡献的甲醛 MPR-BWs2 计算。"
    ```qchem
    $comment
        MPR-BWs2 calculation with non-iterative contributions
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              500                 ! A_0 = 0.5
    MPR_B1_NONITER      -1500               ! non-iterative B_0 = -1.5
    MAX_CYCLES          50
    $end
    ```

???+ example "示例 6.26：包含参数梯度的甲醛 MPR-BWs2 计算。"
    ```qchem
    $comment
        MPR-BWs2 calculation with parameter gradient
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              1500                ! A_0 = 1.5
    MAX_CYCLES          50
    PARAM_GRADIENT      TRUE                ! activate parameter gradient
    $end
    ```
