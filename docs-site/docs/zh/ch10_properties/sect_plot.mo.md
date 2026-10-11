---
title: "10.5.4 使用 *$plots* 生成体数据（Volumetric Data）"
---

## 10.5.4 使用 *$plots* 生成体数据

(July 4, 2026)

可视化 **Q-Chem** 所计算的电荷密度与分子轨道的最简单方式，是借助图形用户界面（GUI），如前一节所述的那些工具。另一种在生成用于发表的高质量图像时常常有用的做法是，在用户指定的网格点集上求值某些密度与轨道。这通过调用 *$plots* 选项来实现，而该选项本身需要通过设置 IANLTY = 200 来启用。

*$plots* 输入的格式记录如下。它允许绘制分子轨道、SCF 基态密度，以及由 CIS、RPA 或 TDDFT/TDA 或 TDDFT 计算得到的激发态密度。此外，与激发态相关的跃迁密度（transition densities）、附着/脱离密度（attachment/detachment densities）或自然跃迁轨道（natural transition orbitals，NTO）（在与上述相同的理论级别上）也可以绘制。关于这些不同可能性的描述，请参见文献 [[572]](../bib_references/bib.md#bib586)。
请注意，目前绘制复值轨道以及复吸收势 Hartree-Fock（Complex-Absorbing-Potential Hartree-Fock）计算的电子密度，只能通过直接生成 cube 文件来实现（参见第 [10.5.5](sec_cubefiles.md) 节）。

默认情况下，*$plots* 命令的输出是工作目录中的一个（或多个）纯文本文件，命名为 `plot.mo`、*etc.*。随后必须使用能够进行三维绘图的第三方程序来可视化这些结果。（第 [10.5.5](sec_cubefiles.md) 节给出了一些建议。）

使用 *$plots* 选项的一个示例输入组（input deck）如下：

???+ example "示例 10.24: 在沿键轴的 $1\times 1\times 15$ 网格上求值 H ${}_{2}$ 的 HOMO 和 LUMO 的作业。绘图输出保存在名为 plot.mo 的 ASCII 文件中，该文件为每个网格点列出 $x$ 、 $y$ 、 $z$ 以及每个所请求 MO 的值。"
    ```qchem
    $molecule
       0  1
       H   0.0   0.0   0.35
       H   0.0   0.0  -0.35
    $end
    
    $rem
       METHOD     hf
       BASIS      6-31g**
       IANLTY     200
    $end
    
    $plots
       Plot the HOMO and the LUMO on a line
       1   0.0   0.0
       1   0.0   0.0
      15  -3.0   3.0
       2   0   0   0
       1   2
    $end
    ```

**Q-Chem** 输入组中 *$plots* 段的一般格式。

> *$plots*
> 
> 
>         一行注释 
> 
> 
>         用 3 行指定三维网格点集： 
> 
> 
>                $N_{x}\quad x_{\mathrm{min}}\quad x_{\mathrm{max}}$ 
> 
> 
>                $N_{y}\quad y_{\mathrm{min}}\quad y_{\mathrm{max}}$ 
> 
> 
>                $N_{z}\quad z_{\mathrm{min}}\quad z_{\mathrm{max}}$ 
> 
> 
>         一行包含 4 个整数，指示要绘制的项目数量： 
> 
> 
>                $N_{\mathrm{MO}}\quad N_{\mathrm{Rho}}\quad N_{\mathrm{Trans}}\quad N_{\mathrm{DA}}$ 
> 
> 
>         一行可选的整数列表，给出要求值的 MO
> （仅当 $N_{\mathrm{MO}}>0$ 时）
> 
> 
>                MO(1)  MO(2) $\ldots$ MO($N_{\mathrm{MO}}$) 
> 
> 
>         一行可选的整数列表，给出要求值的密度
> （仅当 $N_{\mathrm{Rho}}>0$ 时） 
> 
> 
>                Rho(1)  Rho(2) $\ldots$ Rho($N_{\mathrm{Rho}}$) 
> 
> 
>         一行可选的整数列表，给出要求值的跃迁密度
> （仅当 $N_{\mathrm{Trans}}>0$ 时） 
> 
> 
>                Trans(1)  Trans(2) $\ldots$ Trans($N_{\mathrm{Trans}}$) 
> 
> 
>         一行可选的、用于脱离/附着密度的态编号
> （若 $N_{\mathrm{DA}}>0$） 
> 
> 
>                DA(1)  DA(2) $\ldots$ DA($N_{\mathrm{DA}}$) 
> 
> 
> *$end*

*$plots* 关键字段的第一行保留给注释。第 2–4 行列出单一维度的点数以及网格的范围（注意：若未设置 INPUT_BOHR，则坐标范围以埃（Ångstroms）为单位，而所有输出均以原子单位给出）。第 5 行必须包含 4 个非负整数，分别指示需要进行网格值计算的：分子轨道（$N_{\mathrm{MO}}$）、电子密度（$N_{\mathrm{Rho}}$）、跃迁密度以及附着/脱离密度（$N_{\mathrm{DA}}$）的数量。

最后一行指定要绘制哪些 MO、电子密度、跃迁密度以及 CIS 附着/脱离态（若某类要绘制的项目数量为零，该行可以留空或删除）。分子轨道按 $1\ldots N_{\alpha},N_{\alpha}+1\ldots N_{\alpha}+N_{\beta}$ 编号；电子密度编号方式为 0 = 基态，1 = 第一激发态，2 = 第二激发态，*etc.*；而附着/脱离则由态 $1\rightarrow N_{\mathrm{DA}}$ 指定。

默认情况下，所有输出数据都打印到工作目录中的文件，并覆盖任何同名的现有文件。

- •

分子轨道数据打印到名为 `plot.mo` 的文件。
- •

密度绘制到 `plots.hf`。
- •

限制性非弛豫（Restricted unrelaxed）附着/脱离分析输出到：

- **–**

`plot.attach.alpha`
- **–**

`plot.detach.alpha`
- •

非限制性非弛豫（Unrestricted unrelaxed）附着/脱离分析输出到：

- **–**

`plot.attach.alpha`
- **–**

`plot.detach.alpha`
- **–**

`plot.attach.beta`
- **–**

`plot.detach.beta`
- •

限制性弛豫（Restricted relaxed）附着/脱离分析绘制到：

- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.detach.rlx.alpha`
- •

非限制性弛豫（Unrestricted relaxed）附着/脱离分析输出到：

- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.attach.rlx.alpha`
- **–**

`plot.attach.rlx.beta`
- **–**

`plot.detach.rlx.beta`

输出以原子单位打印，先给出坐标，随后是各项目的值，如下所示：

> ```qchem
> x1   y1   z1      a1   a2  ...  aN
> x2   y1   z1      b1   b2  ...  bN
> ...
> ```

除了标准的一维、二维或三维笛卡尔网格之外，用户可能希望在其自选的一组网格点上绘制轨道或密度。这些点通过 *$grid* 输入段指定，其格式 simply 是所有用户指定网格点的笛卡尔坐标：

> ```qchem
> x1   y1   z1
> x2   y2   z2
> ...
> ```

*$plots* 段仍须按上述方式指定，但如果存在 *$grid* 输入段，那么这些用户指定的网格点将覆盖 *$plots* 段中所指定的网格点。

**Q-Chem** 的 *$plots* 工具允许用户直接利用上一次计算保存的振幅（amplitudes）来绘制跃迁密度和脱离/附着密度，而无需重新求解 post-SCF（CIS、RPA、TDA 或 TDDFT）方程。要利用此功能，必须使用同一个 **Q-Chem** scratch 目录，并且 *$rem* 变量 SKIP_CIS_RPA 必须设置为 TRUE。为进一步减少计算时间，*Srem* 变量 SCF_GUESS 可以设置为 READ。

SKIP_CIS_RPA

### `SKIP_CIS_RPA`

> **在波函数分析时跳过 CIS、RPA、TDA 或 TDDFT 方程的求解。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE / FALSE
> * **建议**: 若同一计算此前已运行过且保留了 scratch 文件，则将其设置为 true 以加速绘图数据的生成。

## 10.5.4.1 新的 *$plots* 输入

新版 *$plots* 段格式为体数据的生成提供了可读且友好的输入。该输入段可分为三个部分。第一部分包含定义三维网格点集的基本绘图选项。第二部分是密度或轨道的选择。高级选项包含在最后一部分。

在新绘图格式下，有多种定义三维网格点的方式。如果未给出任何绘图选项，则网格盒（mesh box）的边界为分子坐标的最大值/最小值 $\pm~{}3.0$ Å。只需将 `grid_range` 设置为大于或小于 $3.0$ 的值（也接受负数），即可相应地简单放大或缩小默认盒子。若要自定义网格盒，请将 `grid_range` 设置为所需的边界：

> ```qchem
> $plots
>   grid_range (-1,1)  (-1,1)  (-1,1)
> $end
> ```

这定义了一个以分子坐标原点为中心、尺寸为 2$\times$2$\times$2 的网格盒。注意括号内没有空格。

单一维度的点数等于盒长除以 `grid_spacing`。默认的网格点间距为 $0.3$ Å。若要绕过 `grid_spacing` 的使用并自定义三维点的数量，请将 `grid_points` 设置为所需的值。

要在新绘图格式下生成 cube 文件（第 [10.5.5](sec_cubefiles.md) 节），只需在 *$rem* 段中设置 MAKE_CUBE_FILES = TRUE。新绘图格式通过请求 PLOTS = 1 来启用。

表 10.3: 新版 *$plots* 输入段的选项

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">选项</span></th>
<td class="ltx_td ltx_align_left ltx_border_tt">说明</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">基本绘图选项</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_range</th>
<td class="ltx_td ltx_wrap ltx_align_left">以 Å 为单位的网格盒边界${}^{\dagger}$，或在默认边界${}^{\dagger\dagger}$上的增量/减量</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_spacing</th>
<td class="ltx_td ltx_align_left">以 Å 为单位的网格点间距${}^{\dagger\dagger\dagger}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">grid_points</th>
<td class="ltx_td ltx_align_left">
$N_{x}$ $N_{y}$ $N_{z}$
</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">密度/轨道选择${}^{\star}$</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">alpha_molecular_orbital</th>
<td class="ltx_td ltx_align_left">要评价的 alpha MO 的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">beta_molecular_orbital</th>
<td class="ltx_td ltx_align_left">要评价的 beta MO 的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">total_density</th>
<td class="ltx_td ltx_align_left">要评价的总密度的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">spin_density</th>
<td class="ltx_td ltx_align_left">要评价的自旋密度的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">transition_density</th>
<td class="ltx_td ltx_align_left">要评价的跃迁密度的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">natural_transition_orbital</th>
<td class="ltx_td ltx_align_left">要评价其 NTO 的激发态的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">attachment_detachment_density</th>
<td class="ltx_td ltx_align_left">要评价的脱离-附着密度的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">natural_bond_orbital</th>
<td class="ltx_td ltx_align_left">每个态要评价的 NBO 的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">nbo_state</th>
<td class="ltx_td ltx_align_left">要评价其 NBO 的态的整数范围</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_bold">高级选项</span></th>
<td class="ltx_td ltx_border_t"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">reduced_density_gradient</th>
<td class="ltx_td ltx_align_left">调用非共价相互作用（NCI）图</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">orbital_laplacians</th>
<td class="ltx_td ltx_align_left">评价轨道的拉普拉斯量（Laplacians）</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">average_local_ionization</th>
<td class="ltx_td ltx_wrap ltx_align_left">在给定电子密度等值面值下评价平均局域电离能[[1261]](../bib_references/bib.md#bib1314)。默认值为 $0.0135e/\textrm{\AA}^{3}$（$\approx 0.002e/a^{3}_{0}$）。</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">elf</th>
<td class="ltx_td ltx_align_left">调用电子局域化函数（electron localization function，ELF）图</td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="2">
${}^{\dagger}$格式为：$(x_{\mathrm{min}},x_{\mathrm{max}})(y_{\mathrm{min}},y_{\mathrm{max}})(z_{\mathrm{min}},z_{\mathrm{max}})$
</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\dagger\dagger}$默认值是在由分子坐标导出的边界上增加 $3.0$ Å</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\dagger\dagger\dagger}$默认值为 $0.3$ Å；可被选项 ’grid_points’ 覆盖</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row" colspan="2">
${}^{\star}$输入格式：n-m 或 n，表示第 n 个轨道或态；基态使用 $0$</th>
</tr>
</tfoot>
</table>

???+ example "示例 10.25: 生成 cube 文件：基态及前两个激发态的总密度、前两个激发态的跃迁密度和脱离/附着密度，以及第 28 至 31 个 alpha 分子轨道，并使用自定义的三维网格盒与网格点。"
    ```qchem
    $molecule
    0 1
      C    0.0000000   -0.0000000   -0.6133791
      O   -0.0000000    0.0000000    0.6060734
      H    0.0000000    0.9391300   -1.1555819
      H    0.0000000   -0.9391300   -1.1555819
    $end
    
    $rem
       METHOD           cis
       BASIS            6-31+G*
       CIS_N_ROOTS      4
       CIS_TRIPLETS     false
       MAKE_CUBE_FILES  true   ! triggers writing of cube files
       PLOTS            true
    $end
    
    $plots
       grid_range                     (-8,8) (-8,8) (-8,8)
       grid_points                    40 40 40
       total_density                  0-2
       transition_density             1-2
       attachment_detachment_density  1-2
       alpha_molecular_orbital        28-31
    $end
    ```

???+ example "示例 10.26: 生成苯胺（aniline）基态的平均局域电离能与总密度的 cube 文件。"
    ```qchem
    $molecule
    0 1
      H        -2.952725   -0.026758    0.000000
      C        -1.871492   -0.010683    0.000000
      C        -1.172124   -0.001127   -1.197270
      H        -1.709244   -0.009471   -2.137819
      C         0.211522    0.017487   -1.202676
      H         0.754733    0.024328   -2.137945
      C         0.916518    0.025234    0.000000
      N         2.357874    0.119819    0.000000
      H         2.747183   -0.346427   -0.829920
      H         2.747183   -0.346427    0.829920
      C         0.211522    0.017487    1.202676
      H         0.754733    0.024328    2.137945
      C        -1.172124   -0.001127    1.197270
      H        -1.709244   -0.009471    2.137819
    $end
    
    $rem
       EXCHANGE         hf
       BASIS            6-31g*
       MAKE_CUBE_FILES  true
       PLOTS            true
    $end
    
    $plots
       grid_spacing   0.1
       total_density  0
       average_local_ionization
    $end
    ```
