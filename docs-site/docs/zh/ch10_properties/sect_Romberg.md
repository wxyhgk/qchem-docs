---
title: "10.13.3 Romberg 有限场方法"
---

## 10.13.3 Romberg 有限场方法

（2026 年 7 月 4 日）

[10.13.2 节](sec_finite-field.md)中描述的有限场（FF）方法是对公式 ([10.152](Ch10.S13.SS1.md#eqn:E_F)) 中所建议导数的一种直接的有限差分实现，而在 Romberg 方法[[311]](../bib_references/bib.md#bib328)中，则将 $k$ 个不同外加电场下获得的能量值进行组合，这些电场的振幅构成一个几何级数：

<a id="Ch10.E153"></a>
$$
F(k)=a^{k}F_{0}\;. \tag{10.153}
$$

FF 表达式是通过将具有不同振幅和/或不同外场方向的能量的截断 Taylor 展开组合而得到的。例如，对于对角 $\bm{\beta}$ 张量分量，Romberg FF 表达式为

<a id="Ch10.E154"></a>
$$
\beta_{iii}(k,0)=3\left(\frac{\bigl{[}E(F_{-i}(k+1)-E(F_{i}(k+1))\bigr{]}-a\bigl{[}E(F_{-i}(k)-E(F_{i}(k))\bigr{]}}{a(a^{2}-1)(a^{k}F_{0})^{3}}\right)\;. \tag{10.154}
$$

电场下标 $\pm i$ 指可能的电场方向，*即*，$\pm x$、$\pm y$ 或 $\pm z$。Taylor 展开的截断意味着结果会受到高阶超极化率的污染，为了消除这种污染，使用递归表达式执行连续的“Romberg 迭代”。对于（超）极化率张量 $\bm{\zeta}$ 的一个分量，递归表达式为

<a id="Ch10.E155"></a>
$$
\zeta(k,n)=\frac{a^{2n}\zeta(k,n-1)-\zeta(k+1,n-1)}{a^{2n}-1}\;. \tag{10.155}
$$

该表达式导出一个三角形的 Romberg 表，从而可以监测数值导数的收敛性[[311]](../bib_references/bib.md#bib328)。

与任何有限差分方法一样，用于计算（超）极化率的 FF 方法对数值微分的细节十分敏感。Romberg 方法允许人们找到一个由上下界定义的“场窗口”，在该窗口内有限差分过程是稳定的。低于该窗口的场振幅下的能量值会受到过大舍入误差的影响，这些误差与能量收敛阈值成正比。上界则由对应于基态与激发态能量相交处的临界场振幅所限定。在 Romberg 方法中，这个稳定性窗口定义了一个子三角形，确定该子三角形是分析 Romberg 表时的首要目标。

基于场振幅误差分析的自动化过程已实现在 **Q-Chem** 发行版附带的脚本中。场振幅误差定义为在同一 Romberg 迭代下，对连续场振幅所得到的 $\zeta$ 值之差：

<a id="Ch10.E156"></a>
$$
\epsilon_{k}(n)=\zeta(k+1,n)-\zeta(k,n)\;. \tag{10.156}
$$

根据 Romberg 的递归表达式，场误差预计随着每次迭代而减小。可以使用迭代（阶）误差来检测 Romberg 过程的收敛性，其定义为

<a id="Ch10.E157"></a>
$$
\epsilon_{n}(k)=\zeta(k,n+1)-\zeta(k,n)\;. \tag{10.157}
$$

对这些量的自动化分析在文献 [[311]](../bib_references/bib.md#bib328) 中有详细描述。

**注意： 

•

如果场窗口选择不当，自动化过程可能会失败。

•

Romberg 过程可以针对某一个特定的对角方向执行，也可以针对所有笛卡尔分量执行。对于二阶超极化率，仅可获得 $iiii$、$iijj$ 分量。

**

## 10.13.3.1 如何执行 Romberg 微分过程

要执行（超）极化率的 Romberg 计算，可在 `$QC/bin/tools/Romberg` 目录中使用以下工具：

> `input-Q-Chem-t-rex.sh`
> 
> 
> `parse-t-rex.sh`
> 
> 
> `input-Q-Chem-t-rex-3.0`
> 
> 
> `romberg_tddft_read`
> 
> 
> `romberg_eom_read`
> 
> 
> `T-REX-3.0.3`

需要根据所使用的 shell，将此目录手动添加到 `$PATH` 环境变量中：

> ```qchem
> # bash syntax for ~/.bashrc:
> export PATH="$QC/bin/tools/Romberg:$PATH"
> # csh/tcsh syntax for ~/.cshrc:
> set path=($QC/bin/tools/Romberg $path)
> ```

要运行计算，请创建一个名为 `input` 的输入文件，指定分子、电子结构方法以及若干额外的 *$rem* 变量，这些变量用于

- •

关闭对称性（对于 CC/EOM 计算，设置 INTEGRAL_SYMMETRY 和 CC_SYMMETRY），
- •

请求更高精度的输出（CC_PRINT_PREC），以及
- •

设置非常严格的收敛条件（SCF_CONVERGENCE、CC_CONVERGENCE、EOM_DAVIDSON_CONVERGENCE，*等等*）。

下面给出一个输入文件的示例。

???+ example "示例 10.66：使用 B3LYP 对乙烯分子进行 Romberg 计算的输入文件"
    ```qchem
    $molecule
    0 1
     C        0.00000000   0.00000000 -0.66880000
     H        0.94859916   0.00000000 -1.19917145
     H       -0.94859916   0.00000000 -1.19917145
     C       -0.00000000   0.00000000  0.66880000
     H       -0.54409413   0.77704694  1.19917145
     H        0.54409413  -0.77704694  1.19917145
    $end
    
    $rem
       BASIS            =  sto-3g
       EXCHANGE         =  B3lyp
       SCF_CONVERGENCE  =  13  ! tight convergence for finite field calculations
       SCF_MAX_CYCLES   =  200
       CC_PRINT_PREC    =  16  ! decimal points of total energies
       INTEGRAL_SYMMETRY = false ! all symmetries need to be turned off
    $end
    ```

运行脚本 `input-Q-Chem-t-rex.sh`，并根据提示回答有关场振幅几何级数参数的问题（见下面示例）。该脚本会基于您提供的输入文件模板为 FF 计算生成多个输入文件。所请求的文件名将作为每个自动生成 FF 输入文件的前缀。例如，如果指定文件名为 `water`，则会生成名为 `water001.inp`、`water002.inp`、……的输入文件。这些文件必须在 Romberg 过程之外独立运行，例如在计算集群上运行，或在本地使用 GNU parallel 或 xargs 运行。例如，使用 GNU parallel，每次运行 6 个 **Q-Chem** 作业，每个作业使用 4 个线程：

> ```qchem
> ls hello*.inp | parallel -j6 ’qchem -nt 4 {.}.inp {.}.out’
> ```

运行完计算后，使用脚本 `parse-t-rex.sh` 解析输出文件。然后运行 `T-REX` 程序。根据提示回答问题，以计算偶极矩和（超）极化率（见下面示例）。

Romberg 微分仅适用于已启用高精度总能量输出的方法。在当前版本的 **Q-Chem** 中，CC_PRINT_PREC 已对以下方法实现：HF、DFT、MP2、RI-MP2、MP3、CCD、CCSD、CCSD(T)、QCISD、QCISD(T)、TDDFT 和 EOM-CCSD。

**注意： 

当使用激发态方法（如 TDDFT、CIS 和 EOM-CC）时，在外电场较大时态序（state ordering）可能会发生交换。
**

使用 T-REX 程序，可以计算静态势偶极矩、极化率、一阶和二阶超极化率，可针对某一个特定的对角方向或所有笛卡尔分量，不过二阶超极化率仅限于 $iiii$ 和 $iijj$ 分量。在计算所有分量时，您可以获得偶极矩和极化率的范数、超瑞利散射（Hyper-Rayleigh scattering）一阶超极化率、二阶超极化率的平均值以及其他信息。

## 10.13.3.2 有限场计算的分步示例

将上面给出的用于 DFT 计算的示例 `input` 文件放入一个新目录中；输入文件的名称应为 `input`。运行脚本 `input-Q-Chem-t-rex.sh`。程序会提出以下问题：

> ```qchem
> Components: x=1 y=2 z=3 all_beta=4 all_alpha=5
> 4
> File name
> eth-
> Number of field amplitudes
> 5
> Smallest field amplitude F_0
> 0.0004
> a   (F_k=a^k F_0)
> 2.0
> Number of files created         101
> ```

在本例中，这些回答对应于 $F(k)=2.0^{k}\times 0.0004$ 的 FF 计算，以及外场振幅的几何级数（$k=0,1,2,3,4,5$）。该计算针对所有分量进行设置，生成了输入文件 `eth-001.inp`、`eth-002.inp`、`eth-003.inp`、……，其中所生成输入文件的准确数量取决于所选的几何级数。

在各 FF 计算完成之后（*即*对所有生成的输入执行 **Q-Chem** 作业之后），使用脚本 `parse-t-rex.sh` 解析输出。能量被写入一个名为 `prelogfile` 的文件。

运行 `T-REX` 程序并根据提示回答问题：

> ```qchem
> Components: x=1 y=2 z=3 all_beta=4
> 4
> Number of methods
> 1
> Number of field amplitudes k_max+1
> 5
> Smallest field amplitude   F_0
> 0.0004
> Step-size a
> 2.0
> ```

能量被排序写入一个名为 `logfile` 的文件中，计算结果则打印在 `results` 文件里。
