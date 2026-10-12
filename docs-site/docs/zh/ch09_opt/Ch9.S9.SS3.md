---
title: "9.9.3 附加任务控制与示例"
---

## 9.9.3 附加任务控制与示例

（2026 年 7 月 4 日）

### `AIMD_INIT_VELOC`

> **指定选取初始核速度的方法。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **可选值**：
>     * THERMAL
>     * 从麦克斯韦-玻尔兹曼（Maxwell-Boltzmann）
>     * 分布中随机抽样核速度。用户必须通过
>     * $rem
>     * 变量
>     * AIMD_TEMP
>     * 指定以开尔文（Kelvin）为单位的温度。
>     * ZPE
>     * 选取速度使得每个简正模式都被赋予零点振动能量（zero-point vibrational energy），符号随机。该选项要求事先运行一次频率计算任务。
>     * QUASICLASSICAL
>     * 将振动能分配到每个简正模式中。与 ZPE 选项不同，这里的振动能量是在目标模拟温度下从玻尔兹曼（Boltzmann）分布中抽样的。该选项还会触发以下描述的其他若干选项。
>     * OLD
>     * 使用紧接的前一个 AIMD 任务的相同初始速度。
>     * RESTART
>     * 使用前一个 AIMD 任务的最终速度，
>     * 从磁盘读取。
> * **建议**：仅当未在 $velocity 区段中显式指定速度时，才需要设置此变量。

### `AIMD_INIT_VELOC_NANO_RANDOM`

> **使用更精确的随机种子来生成随机初始速度。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **可选值**：
>     * FALSE
>     * 使用精度较低的随机种子。
> * **建议**：除非必要，请保持此选项为 TRUE。当 AIMD_INIT_VELOC 需要抽样随机初始速度时，此选项决定所用随机种子的来源。若将该选项设为 FALSE，则种子基于以秒为单位的系统时间，这意味着在同一秒内启动的两个otherwise完全相同的模拟将产生相同的初始速度。设为 TRUE 时，此类碰撞几乎不可能发生。保留该选项是出于历史兼容目的，通常几乎没有必要将其设为 FALSE。

### `AIMD_MOMENTS`

> **请求在每个时间步输出多极矩（multipole moments）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $n$
>     * 输出前
>     * $n$
>     * 阶多极矩。
> * **建议**：无

### `AIMD_TEMP`

> **指定用于麦克斯韦-玻尔兹曼速度抽样的温度（以开尔文为单位）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **可选值**：
>     * 用户指定的开尔文数值。
> * **建议**：此变量仅与 AIMD_INIT_VELOC = THERMAL 配合使用时才有意义。注意，模拟是在恒定能量而非恒定温度下进行的，因此核平均动能会在模拟过程中波动。

### `DEUTERATE`

> **请求将所有氢原子替换为氘。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE
>     * 用氘替换氢原子。
> * **建议**：替换氢原子可使最快的振动频率降低约 1.4 倍，从而允许在 ELMD 计算中使用更大的虚设质量和时间步长。在 BOMD 计算中没有理由替换氢原子。

???+ example "示例 9.34：在 298 K 下模拟水二聚体的热涨落。"
    ```qchem
    $molecule
       0  1
       O   1.386977   0.011218   0.109098
       H   1.748442   0.720970  -0.431026
       H   1.741280  -0.793653  -0.281811
       O  -1.511955  -0.009629  -0.120521
       H  -0.558095   0.008225   0.047352
       H  -1.910308   0.077777   0.749067
    $end
    
    $rem
       JOBTYPE              aimd
       AIMD_METHOD          bomd
       METHOD               b3lyp
       BASIS                6-31g*
       TIME_STEP            20        (20 a.u. = 0.48 fs)
       AIMD_STEPS           1000
       AIMD_INIT_VELOC      thermal
       AIMD_TEMP            298
       FOCK_EXTRAP_ORDER    6         request Fock matrix extrapolation
       FOCK_EXTRAP_POINTS   12
    $end
    ```

???+ example "示例 9.35：在 CIS 级别计算的第一激发态势能面上模拟 $\rm F^{-}(H_{2}O)_{4}$ 的动力学演化。"
    ```qchem
    $comment
      Note, only a few time steps are taken, a more appropriate
      number would be:
       AIMD_STEPS       827   500 fs
    $end
    
    $molecule
       -1   1
       O  -1.969902  -1.946636   0.714962
       H  -2.155172  -1.153127   1.216596
       H  -1.018352  -1.980061   0.682456
       O  -1.974264   0.720358   1.942703
       H  -2.153919   1.222737   1.148346
       H  -1.023012   0.684200   1.980531
       O  -1.962151   1.947857  -0.723321
       H  -2.143937   1.154349  -1.226245
       H  -1.010860   1.980414  -0.682958
       O  -1.957618  -0.718815  -1.950659
       H  -2.145835  -1.221322  -1.158379
       H  -1.005985  -0.682951  -1.978284
       F   1.431477   0.000499   0.010220
    $end
    
    $rem
       JOBTYPE           aimd
       AIMD_METHOD       bomd
       METHOD            hf
       BASIS             6-31+G*
       ECP               SRLC
       PURECART          1111
       CIS_N_ROOTS       3
       CIS_TRIPLETS      false
       CIS_STATE_DERIV   1         propagate on first excited state
       AIMD_INIT_VELOC   thermal
       AIMD_TEMP         150
       TIME_STEP         25
       AIMD_STEPS        10
    $end
    ```

???+ example "示例 9.36：使用 ELMD 模拟 NaCl 分子的振动。"
    ```qchem
    $molecule
       0  1
       Na   0.000000   0.000000  -1.742298
       Cl   0.000000   0.000000   0.761479
    $end
    
    $rem
       JOBTYPE    freq
       METHOD     b3lyp
       ECP        fit-sbkjc
       BASIS      sbkjc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           aimd
       METHOD            b3lyp
       ECP               fit-sbkjc
       BASIS             sbkjc
       TIME_STEP         14
       AIMD_STEPS        500
       AIMD_METHOD       curvy
       AIMD_FICT_MASS    360
       AIMD_INIT_VELOC   zpe
    $end
    ```

**Q-Chem** 能够使用 RATTLE 算法[[45]](../bib_references/bib.md#bib28)
进行带冻结键的 AIMD 模拟。
通过将 rem 变量
AIMD_INTEGRATION 设置为 RATTLE 即可请求该功能。约束条件通过
*$rattle* 输入区段施加，其格式如下所示。

> ```qchem
> $rattle
>    bond  atom1  atom2  value
>    ....  .....  .....  .....
> $end
> ```

**注意：

键长数值应以埃（Ångstrom）为单位。
**

RATTLE 步的收敛阈值和最大迭代次数由以下 *$rem* 变量控制：RATTLE_THRESH（默认值为 6）和 RATTLE_MAXIT（默认值为 100）。

???+ example "示例 9.37：使用 RATTLE 算法模拟水分子。"
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 1 0.96 2 104.5
    $end
    
    $rem
       JOBTYPE             aimd
       METHOD              b3lyp
       BASIS               6-31G*
       TIME_STEP           15
       AIMD_STEPS          10
       AIMD_INIT_VELOC     thermal Boltzmann distribution
       AIMD_TEMP           300     (in Kelvin)
       AIMD_PRINT          1
       AIMD_INTEGRATION    RATTLE
       DEBUG_RANDOM_SEED   true
    $end
    
    $rattle
       bond 1 2 0.950
       bond 1 3 0.950
       bond 2 3 1.565
    $end
    ```

???+ example "示例 9.38：在每一步进行激子分析（exciton analysis）的激发态 AIMD。"
    ```qchem
    $comment
    AIMD trajectory with wave-function analysis performed at each step.
    This is invoved by  STATE_ANALYSIS=true and AIMD_PRINT=2
    $end
    
    $molecule
    0 1
      O   -2.1904701    0.5202006    0.0237374
      H   -1.2011437    0.4799213    0.0237374
      H   -1.2011437    0.4799213    0.0237374
    $end
    ```
