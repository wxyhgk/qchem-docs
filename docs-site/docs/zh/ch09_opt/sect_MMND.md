---
title: "9.9.8 Meyer-Miller 非绝热动力学"
---

## 9.9.8 Meyer-Miller 非绝热动力学

（2026 年 7 月 4 日）

作为 Tully 的 FSSH 算法（见第 [9.9.7 节](sect_fssh.md)）的替代方案，**Q-Chem** 也可以使用经典的 Meyer-Miller（MM）哈密顿量产生振动-电子（vibronic）动力学，从而执行基于轨迹的电子非绝热模拟。[[943]](../bib_references/bib.md#bib983)
 此外，该动力学还可以施加对称准经典（symmetrical quasi-classical，SQC）量子化程序，[[276]](../bib_references/bib.md#bib277)
 从而有效地定义电子态。[[277]](../bib_references/bib.md#bib278)
 关于此方法在 **Q-Chem** 中实现方式的详细信息可参见文献 [[1340]](../bib_references/bib.md#bib1398)
。简而言之，Meyer-Miller 哈密顿量将电子非绝热过程中的电子自由度（DOF）映射为一组相互耦合的经典谐振子，每个电子态对应一个振子。经典振动激发在这些振子之间的转移决定了处于活跃状态的电子态，或更准确地说，决定了构成有效多态势能面（PES）的电子态组合，而核自由度也在该势能面上以经典方式传播。

在绝热表示中（与 **Q-Chem** 生成的 Born-Oppenheimer PES 相关），Meyer-Miller 哈密顿量为

<a id="eq:MMad"></a>

$$
H(\mathbf{x,p,R,P})=\frac{1}{2\boldsymbol{\mu}}\bigg{(}\mathbf{P}+\sum_{I,J}^{F}(x_{I}p_{J}-x_{J}p_{I})\mathbf{d}_{IJ}(\mathbf{R})\bigg{)}^{2}+\sum_{I}^{F}\bigg{(}\frac{1}{2}p_{I}^{2}+\frac{1}{2}x_{I}^{2}-\gamma_{I}\bigg{)}E_{I}(\mathbf{R}) \tag{9.65}
$$

其中 $\{x_{I},p_{I}\}$ 是与 $F$ 个电子态集合相对应的“电子振子”的坐标和动量，$\mathbf{R,\,P}$ 是具有约化质量 $\boldsymbol{\mu}$ 的核自由度的坐标和动量，${E_{I}}(\mathbf{R})$ 是绝热态 $I$ 对应的 Born-Oppenheimer 势能面（PES），$\textbf{d}_{IJ}(\textbf{R})=\bigl{\langle}\Psi_{I}\big{|}\vec{\nabla}_{\textbf{R}}\Psi_{J}\bigr{\rangle}$ 是电子态 $I$ 与 $J$ 之间的标准一阶导数耦合矢量，$\{\gamma_{I}\}$ 是一组零点能参数。因此，式 ([9.65](#eq:MMad)) 中 $F$ 个经典振子的演化描述了 MM 模型中的电子组态，特别是与每个振子相关的经典作用量。

在 **Q-Chem** 中通过 QCMD_METHOD rem 变量请求对称准经典 Meyer-Miller（SQC/MM）方法。对式 ([9.65](#eq:MMad)) 所产生的经典哈密顿动力学进行量子化是以对称方式完成的，*即*，同时针对动力学电子变量的初始值和终值。这一步骤首先通过从“加窗（windowing）”函数中蒙特卡洛采样作用量来实现。在指定终时刻的量子化则根据同一加窗函数对随时间演化的作用量进行“分箱（binning）”来完成。在 **Q-Chem** 的实现中，仅采用“三角（triangle）”形式的加窗函数，[[278]](../bib_references/bib.md#bib279)
 该形式被普遍发现优于文献 [[277]](../bib_references/bib.md#bib278)
 中原有的直方图（histogram）形式窗口。此外，还提供了使用文献 [[279]](../bib_references/bib.md#bib281)
 中 $\gamma$-调整协议的选项，并通过 SQC_GAMADJUST 关键字请求。通常推荐使用该选项。$\gamma$-调整程序的关键在于针对每个自由度（以及每条轨迹）设定式 ([9.65](#eq:MMad)) 中的 $\{\gamma_{I}\}$，使得作用在核上的初始力与初始纯量子态——*即*单一 PES——的力一致。Ehrenfest 模拟同样可用，其动力学与 SQC 计算等价，但 Ehrenfest 方法不使用对称加窗函数来选择初始条件并估计最终布居数，而是使用 $\gamma=0$ 的整数初始电子作用量变量，并在每个所期望的终时刻利用这些作用量变量的*取值*来估计电子态布居数。

初始核自由度的采样分布通过 QCMD_INITNUC 关键字请求。目前支持从 Wigner 分布或 Boltzmann 分布中同时采样初始位置和速度。从这两种分布中的任一种进行采样都需要有可用的频率计算结果。或者，用户也可以使用 *$velocity* 节输入速度，如第 [9.9.2 节](sub_aimd_jobcontrol.md) 所述。

### `QCMD_METHOD`

> **指定非绝热 Meyer-Miller 分子动力学方法。**
>
> * **类型**：`STRING`
> * **默认值**：`0`
> * **选项**：
>     * Ehrenfest
>     * 传统 Ehrenfest 分子动力学。
>     * SQC
>     * 对称准经典 Meyer-Miller 分子动力学
> * **建议**：无

### `QCMD_INITSTATE`

> **指定初始占据的电子态。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * $n$
>     * 一个小于
>     * CIS_N_ROOTS
>     * 的整数。
> * **建议**：无

### `QCMD_INITNUC`

> **指定采样初始核位置和速度时所使用的分布。**
>
> * **类型**：`STRING`
> * **默认值**：`0`
> * **选项**：
>     * Wigner
>     * Wigner 分布。
>     * Boltzmann
>     * Boltzmann 分布
> * **建议**：与 AIMD_TEMP 配合使用。

### `QCMD_WARMUP`

> **指定在动力学开始之前，初始构型与采样构型之间线性插值的步数，以实现准确的状态跟踪。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
> * **建议**：无

### `SQC_GAMADJUST`

> **指定 $\gamma$-调整协议。**
>
> * **类型**：`STRING`
> * **默认值**：`True`
> * **选项**：
>     * True
>     * 使用
>     * $\gamma$
>     * -调整协议。
>     * False
> * **建议**：通常推荐使用 $\gamma$-调整协议。

???+ example "示例 9.45：Ehrenfest 模拟。"
    ```qchem
    $molecule
    0 1
     Na      0.00000000      0.00000000      0.93444743
      H      0.00000000      0.00000000     -0.93444743
    $end
    
    $rem
       JOBTYPE                  freq
       METHOD                   hflyp
       BASIS                    6-31g*
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE                 aimd
       METHOD                  hflyp
       BASIS                   6-31g*
       CIS_N_ROOTS             6
       CIS_SINGLETS            true
       CIS_TRIPLETS            false
       AIMD_METHOD             qcmd      !initiates quasi-classical nonadiabatic dynamics
       QCMD_METHOD             ehrenfest
       TIME_STEP               10        !in atomic units
       AIMD_STEPS              340
       QCMD_INITSTATE          5         !start on S5
       QCMD_INITNUC            boltzmann !sample from a Boltzmann distribution
       AIMD_TEMP               300
       RPA                     0
    $end
    ```

???+ example "示例 9.46：SQC/MM 模拟。"
    ```qchem
    $molecule
    0 1
      C     -1.10077021     -0.38619733      0.05617695
      C      0.09675762     -1.08610723     -0.30779113
      C      1.28662554     -0.41739388     -0.28021086
      O      1.41824439      0.84326764      0.06159343
      O     -1.12106364      0.80448471      0.39946439
      H      0.49060260      1.16255871      0.27980893
      H      0.06099112     -2.12846061     -0.60005353
      H      2.23038546     -0.89206633     -0.54524306
      H     -2.05177379     -0.94757617      0.02607669
    $end
    
    $rem
       JOBTYPE                  freq
       METHOD                   pbe0
       BASIS                    6-31g*
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
       JOBTYPE                 aimd
       METHOD                  pbe0
       BASIS                   6-31g*
       CIS_N_ROOTS             4
       CIS_SINGLETS            true
       CIS_TRIPLETS            false
       AIMD_METHOD             qcmd      !initiates quasi-classical nonadiabatic dynamics
       QCMD_METHOD             sqc
       TIME_STEP               10        !in atomic units
       AIMD_STEPS              340
       QCMD_INITSTATE          2         !start on S2
       QCMD_INITNUC            wigner    !sample from a Wigner distribution
       SQC_GAMADJUST           true
       AIMD_TEMP               0
       RPA                     0
    $end
    
    ```
