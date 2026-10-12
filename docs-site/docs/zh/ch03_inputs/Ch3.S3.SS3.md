---
title: "3.3.3 从先前的作业或文件中读取分子坐标"
---

## 3.3.3 从先前的作业或文件中读取分子坐标

(July 4, 2026)

用户常常希望依次执行多项计算，其中后续计算依赖于先前计算所得的结果。例如，先在较低的理论级别上进行几何优化，随后进行振动分析，最后 Perhaps 在更高的理论级别上做单点能计算。为了避免用户手动将优化输出中的坐标复制到振动分析或单点能计算的输入文件中，**Q-Chem** 可以在各个作业（job）之间直接传递这些坐标。

要实现这一点，需要满足以下条件：

- 在分子坐标输入中填写 READ 变量
- 先前计算的暂存文件（scratch files）已被保存。这些文件可以通过下文及第 [2](../ch02_install/chap_install.md) 章所述的 save 选项在多次作业运行中*显式（explicitly）*获得，或者如第 [3.5](sec_multiple_jobs.md) 节所述，在单个输入文件中运行多个计算时*隐式（implicitly）*获得。

```qchem
$molecule
   READ
$end
```

在此示例中，*job1* 的暂存文件被保存在目录 *$QCSCRATCH/job1* 中，随后供 *job2* 计算使用。可通过以下命令实现：

> ```qchem
> localhost-1> qchem job1.in job1.out job1
> localhost-2> qchem job2.in job2.out job1
> ```

在此示例中，`job1` 的暂存文件被保存在目录 `$QCSCRATCH/job1` 中，随后供 `job2` 计算使用。

!!! note "注意"
    必须通过 `job2` 的输入指明程序要读取的具体暂存文件。


READ 功能还可以用于从第二个输入文件中读取分子坐标。第二个文件中坐标的格式遵循标准 **Q-Chem** 输入的格式，并且必须用 *$molecule* 和 *$end* 关键字进行界定。

```qchem
$molecule
   READ filename
$end
```
