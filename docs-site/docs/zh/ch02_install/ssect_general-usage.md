---
title: "2.2.1 一般用法"
---

## 2.2.1 一般用法

（2026 年 7 月 4 日）

安装完成并对用户账户进行必要的调整之后，用户即可运行 **Q-Chem**。**Q-Chem** 有多种调用方式：

1. 1.

**IQmol** 为 **Q-Chem** 软件包提供了完全集成的图形界面，其中包含一个带上下文帮助的高级输入生成器，能够引导你了解 **Q-Chem** 提供的众多选项。它还提供分子构建器、作业提交与监控工具，并可视化分子轨道、电子密度和振动频率。最新版本及下载/安装说明，请参阅 **IQmol** 主页（`http://www.iqmol.org`）。
2. 2.

*qchem* 命令行 shell 脚本。命令行执行的简单格式如下所示。本手册的其余部分将详细介绍输入文件的创建方法。
3. 3.

通过第三方图形用户界面（GUI）调用。其中最流行的两种是：

- •

面向电子结构软件的通用 Web 界面 **WebMO**（`www.webmo.net`）。
- •

Wavefunction 公司在某些平台上提供的 **Spartan** 用户界面。有关当前的可用性详情，请联系 Wavefunction, Inc.（`www.wavefun.com`）或 **Q-Chem**。

只要 **Q-Chem** 已正确安装在你的机器上，并且必要的环境变量已在 `.cshrc`、`.profile` 或等效的登录文件中设置好，使用 **Q-Chem** 命令行 shell 脚本（*qchem*）就非常简单。如果配置正确，`$PATH` 变量会在登录时自动完成必要的修改，从而可以在工作目录中调用 **Q-Chem**。

*qchem* shell 脚本可以采用以下几种方式使用：

> ```qchem
> qchem infile outfile
> qchem infile outfile savename
> qchem -save infile outfile savename
> qchem -archive infile outfile
> ```

其中 `infile` 是格式规范的 **Q-Chem** 输入文件的文件名（详见第 [3](../ch03_inputs/chap_inputs.md) 章及本手册其余部分），`outfile` 则是 **Q-Chem** 写入作业输出信息的文件名。

**注意：

如果 `outfile` 已存在于工作目录中，它将被覆盖。
**

使用命令行变量 `savename` 可以在多次运行之间保存几个关键的暂存（scratch）文件，当要求 **Q-Chem** 读取先前作业的信息时，这是必需的。如果未给出 `savename` 参数，**Q-Chem** 会在运行结束时删除所有临时暂存文件。被保存的文件位于 `$QCSCRATCH/savename/` 中，包括当前分子几何结构、当前分子轨道与密度矩阵以及当前力常数（如有）等文件。*–save* 选项与 `savename` 连用表示保存所有临时文件，而不仅仅是上述几个必需的文件。通常不需要这样做。当指定了 `$QCLOCALSCR` 时，临时文件将存储在该目录下，并在正常终止时复制到 `$QCSCRATCH/savename/`。

输入参数 `infile`、`outfile` 和 *save* 的名称可由用户自行决定（遵循通常的 UNIX 文件和目录命名限制）。为 `infile` 和 `outfile` 使用相同的作业名但配以不同的后缀可能比较方便。例如：

> ```qchem
> localhost-1> qchem water.in water.out &
> ```

表示调用 **Q-Chem**，输入取自 `water.in`，输出写入 `water.out`。`&` 将作业放到后台运行，这样你就可以在当前 shell 中继续工作。

> ```qchem
> localhost-2> qchem water.com water.log water &
> ```

表示调用 **Q-Chem**，输入文件位于 `water.com`，输出写入 `water.log`，关键暂存文件保存在目录 `$QCSCRATCH/water/` 中。

## 2.2.1.1 OpenMP 并行化

**Q-Chem** 可以在单个节点上利用 OpenMP 协议在多个处理器上进行线程化并行执行。要使用 OpenMP 线程运行 **Q-Chem** 计算，请通过 *qchem* 命令选项 *-nt* 指定线程数（*nthreads*）。由于每个线程占用一个 CPU 核心，出于性能考虑，指定的线程数不应超过可用 CPU 核心的总数。未指定时，线程数默认为 1（串行计算）。

> ```qchem
> qchem -nt nthreads infile outfile
> qchem -nt nthreads infile outfile save
> qchem -save -nt nthreads infile outfile save
> ```

要在 Slurm 作业调度系统下运行并行 **Q-Chem**，请在启动 **Q-Chem** 时添加 *-slurm* 命令行参数。例如：

> ```qchem
> qchem -slurm -nt nthreads infile outfile
> ```

## 2.2.1.2 MPI+OpenMP 混合并行化

自 v6.3.0 起，**Q-Chem** 可以在多进程 OpenMP 并行化的基础上，使用消息传递接口（MPI）协议跨多个处理器核心和/或多个计算节点进行并行执行，适用于某些作业类型；v5.4.0 之前的旧 MPI 并行功能已被弃用。这种混合方案涉及多个 MPI 进程，每个进程再派生若干 OpenMP 线程。在该混合方案中，跨节点通信由 MPI 协议处理，节点内通信则隐式地使用 OpenMP 线程完成，以高效利用共享内存并行（SMP）系统。这种并行化策略符合当前集群计算向多核架构发展的趋势。在 v6.3.x 和 v6.4.0 中，新的混合 MPI+OpenMP 方案*仅*适用于涉及有限差分导数或多体相互作用（many-body interaction）方法的计算，且不依赖于无法进行类似并行化的先前计算。例如，在这些旧版本中，不能使用 SCF_GUESS = READ 来启动这些计算。此外，使用 **Libopt3** 库进行几何优化，可以配合支持 MPI+OpenMP 的有限差分梯度来实现。在 v7.0 中，新的混合 MPI+OpenMP 方案扩展至包括使用 DIIS 和 GDM SCF 算法进行的非 RI（resolution-of-identity）Hartree–Fock 与 DFT 的 SCF 能量计算，以及针对 RHF、UHF 和 ROHF 拟设（ansätze）的稳健 SCF 流程。对于这种 MPI+OMP 并行的 SCF 方案，Q-Chem v7.0 采用重复式 Fock（replicated-Fock）方法，要求用户在同一物理节点上派生多个 MPI 秩（rank）时考虑每个秩的内存需求。

要使用 MPI 运行并行计算，请使用选项 *-np* 指定要派生的 MPI 进程数，方式如下：

> ```qchem
> qchem -mpi -np nprocs infile outfile
> qchem -mpi -np nprocs infile outfile savename
> qchem -save -mpi -np nprocs infile outfile savename
> ```

其中 *nprocs* 是要使用的处理器数量。如果未给出 *-np* 开关，**Q-Chem** 将默认在单个节点上本地运行。

要运行混合 MPI+OpenMP 计算，请同时使用选项 *-mpi*、*-np* 和 *-nt*，其中 *-np* 后跟要派生的 MPI 进程数，*-nt* 后跟每个 MPI 进程使用的 OpenMP 线程数，方式如下：

> ```qchem
> qchem -mpi -np nprocs -nt nthreads infile outfile
> qchem -mpi -np nprocs -nt nthreads infile outfile savename
> qchem -save -mpi -np nprocs -nt nthreads infile outfile savename
> ```

当指定了附加参数 *savename* 时，MPI 秩 `n` 上的临时文件存储在名为 `$QCSCRATCH/savename.n` 的文件夹中。
作业成功完成后，相关的暂存信息会被复制回头节点上的 `$QCSCRATCH/savename` 文件夹。
如果作业异常终止，这些文件将不会被复制到头节点。

在带有 PBS、SLURM 等批处理调度器的计算机系统上，用户可能需要设置 `$QCMPIRUN` 环境变量，使其指向系统中使用的 *mpirun* 或 *srun* 命令。此外，对于 SLURM 调度器，可能还需要将 `$QCMPI` 设置为 “srun”。更多详情请阅读 `$QC/README.Parallel` 文件。如遇任何问题，请联系 **Q-Chem**（`support@q-chem.com`）。

## 2.2.1.3 基于 **BrianQC** 的 GPU 加速 **Q-Chem**

自 5.0 版本起，**Q-Chem** 计算的核心部分可以使用 **BrianQC** GPU 模块进行加速。它通过提供计算 Fock 矩阵各组成部分（式 ([4.18](../ch04_scf/Ch4.S2.SS2.md#eq416))）例程来实现这一点，这些组成部分包括核心哈密顿量（core Hamiltonian）、库仑（Coulomb）、交换（exchange）以及交换-相关（Eq. ([5.9](../ch05_dft/sec_Kohn-Sham.md#eq437)))）积分，以及它们的一阶导数和二阶导数中最耗时的部分。在计算 Hartree-Fock 和密度泛函理论（Density Functional Theory, DFT）的能量、梯度、振动频率以及其他需要这些量的计算时，这可以带来显著的速度提升。支持将交换贡献拆分为两项的程域分离混合密度泛函（式 ([5.12](../ch05_dft/Ch5.S3.SS1.md#eq:erf_partition))）。

要调用 **BrianQC**，请在启动 **Q-Chem** 时传入 *-gpu* 标志。由于 **BrianQC** 并不能加速 **Q-Chem** 计算的所有部分，且 GPU 加速可与 OpenMP 线程透明协同工作，因此仍然重要的是使用 OpenMP 线程对计算的其余部分进行并行化。

> ```qchem
> qchem -gpu -nt nthreads infile outfile
> ```

使用 **BrianQC** 的要求如下：

- •

单独的 **BrianQC** 许可证
- •

64 位的 Linux 或 Windows 操作系统
- •

基于 Pascal、Volta、Turing 或 Ampere 架构的 Nvidia GPU
- •

角动量不超过 $g$ 的基组（Basis Set）
- •

每个 GPU 上只运行一个 **Q-Chem** 计算

欲了解更多信息，请访问 `https://www.brianqc.com/`。
