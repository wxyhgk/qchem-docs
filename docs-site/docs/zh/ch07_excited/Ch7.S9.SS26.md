---
title: "7.9.26 EOM-CC(2,3) 作业控制"
---

## 7.9.26 EOM-CC(2,3) 的作业控制

（2026 年 7 月 4 日）

通过 METHOD=EOM-CC(2,3) 调用 EOM-CC(2,3)。
以下选项可用：

### `EOM_PRECONV_SD`

> **先求解 EOM-CCSD 方程并打印能量，随后将 EOM-CCSD 矢量用作 EOM-CC(2,3) 的初始矢量。对于采用能量可加性方案（energy additivity schemes）的计算非常方便。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 执行
>     * $n$
>     * 次 SD 迭代
> * **建议**：建议开启此选项

### `CC_REST_AMPL`

> **即便使用了 CC_REST_OCC 和 CC_REST_VIR 关键字，仍强制在完整空间（full space）中确定积分、$T$ 振幅与 $R$ 振幅。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * FALSE
>     * 施加限制
>     * TRUE
>     * 不施加限制
> * **建议**：无

### `CC_REST_TRIPLES`

> **将 $R_{3}$ 振幅限制在活性空间（active space）内，即要求从一个活性占据轨道中移除一个电子，并向一个活性虚轨道中添加一个电子。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 1
>     * 施加限制
> * **建议**：无

### `CC_REST_OCC`

> **设置受限的占据轨道数目，包含冻结（frozen）占据轨道。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 限制
>     * $n$
>     * 个占据轨道。
> * **建议**：无

### `CC_REST_VIR`

> **设置受限的虚轨道数目，包含冻结（frozen）虚轨道。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 限制
>     * $n$
>     * 个虚轨道。
> * **建议**：无

为了选取活性空间，可以通过在 *$reorder_mo* 小节中指定新的顺序来重排轨道。该小节由两行数字组成（$\alpha$ 与 $\beta$ 两套），从 $1$ 开始，到 $n$ 结束，其中 $n$ 是所指定的最后一个轨道的编号。

以下 *$reorder_mo* 小节示例展示了将第 16 和 17 号轨道对 $\alpha$ 和 $\beta$ 电子同时交换：

> ```qchem
> $reorder_mo
>    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   17  16
>    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   17  16
> $end
> ```

## 7.9.26.1 示例

???+ example "示例 7.158：亚甲基（methylene）的 EOM-SF(2,3) 计算。"
    ```qchem
    $molecule
       0 3
       C
       H 1 CH
       H 1 CH 2 HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       METHOD             eom-cc(2,3)
       BASIS              6-31G
       SF_STATES          [2,0,0,2]
       N_FROZEN_CORE      1
       N_FROZEN_VIRTUAL   1
       EOM_PRECONV_SD     20 Get EOM-CCSD energies first (max_iter=20).
    $end
    ```

???+ example "示例 7.159：对一个具有拉长 CC 键的甲烷进行活性空间 EOM-SF(2,3) 计算。HF MO 需按 $reorder_mo 小节所指定的方式重排，使得三激发（triples）的活性空间由 sigma 与 sigma* 轨道组成。"
    ```qchem
    $molecule
       0 3
       C
       H  1  CH
       H  1  CHX  2  HCH
       H  1  CH   2  HCH  3  A120
       H  1  CH   2  HCH  4  A120
    
       CH   = 1.086
       HCH  = 109.4712206
       A120 = 120.
       CHX  = 1.8
    $end
    
    $rem
       METHOD            eom-cc(2,3)
       BASIS             6-31G*
       SF_STATES         [1,0]
       N_FROZEN_CORE     1
       EOM_PRECONV_SD    20   does eom-ccsd first, max_iter=20
       CC_REST_TRIPLES   1   triples are restricted to the active space only
       CC_REST_AMPL      0   ccsd and eom singles and doubles are full-space
       CC_REST_OCC       4   specifies active space
       CC_REST_VIR       17  specifies active space
       PRINT_ORBITALS    10  (number of virtuals to print)
    $end
    
    $reorder_mo
       1 2 5 4 3
       1 2 3 4 5
    $end
    ```

???+ example "示例 7.160：水阳离子三个最低电子态的 EOM-IP-CC(2,3) 计算。"
    ```qchem
    $molecule
    0 1
       H   0.774767     0.000000     0.458565
       O   0.000000     0.000000    -0.114641
       H  -0.774767     0.000000     0.458565
    $end
    
    $rem
       METHOD       eom-cc(2,3)
       BASIS        6-311G
       IP_STATES    [1,0,1,1]
    $end
    ```
