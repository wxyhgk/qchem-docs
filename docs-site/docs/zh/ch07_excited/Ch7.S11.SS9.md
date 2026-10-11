---
title: "7.11.9 librassf 有效哈密顿量分析"
---

## 7.11.9 **librassf** 有效哈密顿量分析

（2026 年 7 月 4 日）

Bloch 有效哈密顿量（Bloch effective Hamiltonian）可与 RAS-1SF 计算结合使用，以确定多中心体系的磁耦合。 **librassf** 模块提供了早期 CASMAN 代码中微扰方法[[927]](../bib_references/bib.md#bib966)的变分版本。

请注意，此实现仍处于测试阶段。

在 **librassf** 中进行分析是一个两步过程。
首先，必须使用 Boys 定域化方法对活性空间轨道进行定域化，
即将 CAS_LOCAL_ALGO 和 CAS_LOCAL 设置为 1。
（也可以将 CAS_LOCAL 设置为 2 来使用 Pipek-Mezey 方法。）
定域化后的 RAS2 轨道会以 Molden 文件格式自动输出到输出文件中。
随后用户可以可视化这些定域化轨道，并按需手动将轨道指定给各个中心。

轨道指定完成后，即可运行 Bloch 有效哈密顿量计算。
这需要将 RASSF_DO_BLOCH 设置为 true，并在 *$rassf_bloch_sites* 段中定义轨道指定。
该段包含三行。第一行指定中心总数，
第二行指定每个中心的轨道数，
第三行是属于各中心的轨道的有序列表。
注意轨道编号从 1 开始。例如对于双铬配合物（dichromium complex），若
轨道 3、4、5 定域在第一个 Cr 原子上，而 1、2、6 定域在第二个 Cr 原子上，则该段应按如下方式定义：

> ```qchem
> $rassf_bloch_sites
> 2
> 3 3
> 3 4 5 1 2 6
> $end
> ```
