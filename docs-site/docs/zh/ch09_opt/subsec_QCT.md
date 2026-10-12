---
title: "9.9.6 准经典分子动力学"
---

## 9.9.6 准经典分子动力学

(July 4, 2026)

所谓"准经典"（quasi-classical）轨迹[[668]](../bib_references/bib.md#bib693)（QCT）在初始速度设置步骤中向每个振动模式注入振动能，从而可以改善纯经典模拟的结果，例如在计算光电子[[747]](../bib_references/bib.md#bib780)或红外光谱时的表现。[[1142]](../bib_references/bib.md#bib1194) 改进之处包括：在较低温度下光谱线宽与实验符合得更好，以及振动频率与非谐（anharmonic）计算结果符合得更好。

低温下的改进可以这样理解：即便在低温下，由于零点运动（zero-point motion）的存在，原子核仍在运动。准经典初始速度中已经包含了这一零点运动，因此在低温下也能得到有限的峰宽。与之相反，经典模拟在低温极限下给出的峰宽为零，因为热能随温度降低而趋于零。同样地，即使在室温下，高频模式的量子振动能也往往显著大于经典动能。因此 QCT-MD 通常会对势能面上能量更高、非谐性更强的区域进行采样，而经典模拟只能访问低能区域。这两种效应既可以带来更准确的峰宽，也能实现对势能面上非谐部分更真实的采样。不过，QCT-MD 方法也存在重要的局限性，这些局限性将在下文说明，用户需要仔细监控。

在我们的 QCT-MD 实现中，初始振动量子数是通过从目标模拟温度下的振动玻尔兹曼（Boltzmann）分布中随机抽样生成的。为了保证结果的可复现性，每条轨迹（及其对应的振动量子数集合）都由 AIMD_QCT_WHICH_TRAJECTORY 变量赋予的唯一编号来标识。若要遍历不同的初始条件，只需使用不同的 AIMD_QCT_WHICH_TRAJECTORY 取值运行多条轨迹。也可以将该变量设为负值，从而指定与一定数量轨迹的平均相对应的初始速度。我们 QCT-MD 实现的更多技术细节详见文献 [[747]](../bib_references/bib.md#bib780) 的附录 A。

### `AIMD_QCT_WHICH_TRAJECTORY`

> **从随机分布中选取一组振动量子数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * $n$: 选取第 $n$ 组随机初始速度。 $-n$ 使用 $n$ 组随机初始速度的平均值。
> * **建议**: 如果你希望初始速度对应于某一组特定的振动占据数，请选择一个正数，并为每条轨迹选择不同的编号。如果希望初始速度对应于 $n$ 条轨迹的平均，请选择一个负数。

下面是一个运行水的振动光谱 QCT-MD 模拟的简单示例输入。大多数输入变量与上文描述的经典 MD 相同。准经典初始条件的启用方式是将 AIMD_INIT_VELOC 变量设置为 QUASICLASSICAL。

???+ example "示例 9.41: 使用 QCT-MD 模拟水的红外光谱。"
    ```qchem
    $molecule
       0  1
       O     0.000000    0.000000    0.520401
       H    -1.475015    0.000000   -0.557186
       H     1.475015    0.000000   -0.557186
    $end
    
    $rem
       JOBTYPE                     freq
       INPUT_BOHR                  true
       METHOD                      hf
       BASIS                       3-21g
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE                     aimd
       INPUT_BOHR                  true
       METHOD                      hf
       BASIS                       3-21g
       SCF_CONVERGENCE             6
       TIME_STEP                   20    !  (in atomic units)
       AIMD_STEPS                  1250  !  600 fs total simulation time
       AIMD_TEMP                   12
       AIMD_PRINT                  2
       FOCK_EXTRAP_ORDER           6     ! Use a 6th-order extrapolation
       FOCK_EXTRAP_POINTS          12    ! of the previous 12 Fock matrices
       AIMD_MOMENTS                1
       AIMD_NUCL_SAMPLE_RATE       5
       AIMD_NUCL_VACF_POINTS       1000
       AIMD_INIT_VELOC             quasiclassical
       AIMD_QCT_WHICH_TRAJECTORY   1     ! Loop over several values to get
                                         ! the correct Boltzmann distribution.
    $end
    ```

沿着轨迹计算光谱性质，即可得到其他类型的光谱。例如，我们观察到光电子光谱可以很好地通过沿轨迹计算垂直电子脱离能（vertical detachment energies, VDEs）、并将 VDE 生成为直方图的方式来近似[[747]](../bib_references/bib.md#bib780)。我们在 `$QC/aimdman/tools` 子目录中提供了若干简单脚本，希望对用户有所帮助，并可作为开发更复杂工具的基础。例如，我们包含了可沿轨迹执行计算的脚本（`md_calculate_along_trajectory`），以及沿轨迹计算垂直电子脱离能的脚本（`calculate_rel_energies`）。

QCT 代码的另一个用途是通过蒙特卡洛（Monte Carlo, MC）算法生成从振动波函数中采样的随机几何结构。其触发方式是将 AIMD_QCT_INITPOS 和 AIMD_QCT_WHICH_TRAJECTORY 两个变量都设置为负数（例如 $-m$ 和 $-n$），并将 AIMD_STEPS 设为零。这样将在用户指定的模拟温度下，生成 $m$ 个从振动波函数中采样的随机几何结构，该波函数对应于 $n$ 条轨迹的平均。

### `AIMD_QCT_INITPOS`

> **选择 QCT-MD 模拟中的初始几何结构。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $0$: 使用平衡几何结构。
>     * $n$: 按照谐振振动波函数选取一个随机几何结构。 $-n$ 生成 $n$ 个从谐振振动波函数中采样的随机几何结构。
> * **建议**: 无。

对于在谐振子模型下描述良好的体系，以及主要依赖于基态动力学性质的情形，这种简单的 MC 方法可能给出定性正确的光谱。事实上，可以认为在描述极低温度下的振动效应时，它比 QCT-MD 更可取，因为几何结构是从真正的量子分布中采样的（而经典和准经典 MD 则不然）。我们在 *$QC/aimdman/tools* 目录中还提供了另一个脚本，用于辅助计算振动平均性质（`monte_geom`）。

???+ example "示例 9.42: 对 HCl 振动波函数进行 MC 采样。
基于 1 开尔文下的谐振振动波函数，生成 HCl 的 1000 个随机几何结构。
该波函数对 1000 组随机振动量子数取平均（ i.e. ，在本例中由于温度极低，
即对应基态）。"
    ```qchem
    $molecule
       0 1
       H    0.000000    0.000000   -1.216166
       Cl   0.000000    0.000000    0.071539
    $end
    
    $rem
       JOBTYPE                    freq
       METHOD                     b3lyp
       BASIS                      6-311++G**
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE                    aimd
       METHOD                     B3LYP
       BASIS                      6-311++G**
       SCF_CONVERGENCE            1
       MAX_SCF_CYCLES             0
       TIME_STEP                  20     (in atomic units)
       AIMD_STEPS                 0
       AIMD_INIT_VELOC            quasiclassical
       AIMD_QCT_VIBSEED           1
       AIMD_QCT_VELSEED           2
       AIMD_TEMP                  1     (in Kelvin)
       AIMD_QCT_WHICH_TRAJECTORY  -1000 ! set to the desired trajectory number
       AIMD_QCT_INITPOS           -1000
    $end
    ```

也可以将某些模式设为非活跃（inactive），*i.e.*，只向一部分模式注入振动能（其余模式均设为零）。活跃模式的列表可以通过 *$qct_active_modes* 段指定。此外，还可以使用 *$qct_vib_distribution* 输入段为每个模式显式指定振动量子数。也可以用 *$qct_vib_phase* 设置相位（允许取值为 1 和 $-$1）。下面是一个简单的示例输入：

```qchem
$qct_active_modes
  1
$end

$qct_vib_distribution
  0
$end

$qct_vib_phase
  1
$end
...
```

最后，我们简要说明 QCT-MD 的局限性。最严重的局限可能来自于所谓的"动能溢出"（kinetic energy spilling）问题[[298]](../bib_references/bib.md#bib302)，即动能可能在各模式之间发生非物理的转移。之所以会出现这种情况，是因为初始速度是按照量子能级选取的，而这些能级通常远高于对应经典系统的能级。此外，经典运动方程还允许各模式之间转移零点能的非整数倍，这导致动能转移的选律（selection rules）有所不同。通常，能量会从高能模式溢出到低能模式，从而产生虚假的"热"动力学。第二个问题在于 QCT-MD 实际上基于经典牛顿（Newtonian）动力学，这意味着在低温下其概率分布与真正的量子分布相比可能出现定性错误[[747]](../bib_references/bib.md#bib780)。

**Q-Chem** 实现了一个用于沿轨迹监控每个简正模式内部动能的程序，并且在准经典模拟中该程序会自动启用。因此，用户可以监控那些某一个或多个模式的动能显著大于初始动能的轨迹，并将这类轨迹剔除。（另一种做法是参见文献 [[298]](../bib_references/bib.md#bib302)，其中提出了处理零点能泄漏问题的不同方法。）此外，该监控程序还会沿轨迹打印（谐振）振动波函数的平方。这使得用户可以利用谐振量子分布对低温结果进行加权。
