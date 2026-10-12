---
title: "11.5.11 fEFP 输入结构"
---

## 11.5.11 fEFP 输入结构

（2026 年 7 月 4 日）

位于 `$QC/bin` 中的两步脚本 `prefefp.pl` 允许用户将 PDB 文件中的分子结构拆分为加帽片段（capped fragments），输出为 **gamess** 格式，从而可以生成用于 fEFP 计算的参数。

要使用 `prefefp.pl` 脚本，你需要一个 PDB 文件、一个 MAP 文件，以及一个包含所有 `.efp` 参数文件的目录。
运行以下命令以：(1) 生成用于产生 $N$ 个 EFP 参数（对应 $N$ 个加帽片段）的 $N$ 个输入文件，以及 (2) 创建 XYZ 格式的 EFP 输入文件。

```qchem
perl prefp.pl 1 <PDB file> <MAP file>
perl prefp.pl 2 <PDB file> <.efp path> <MAP file> <GMS input file name>
```

在第一步中，脚本借助 MAP 文件将生物分子（PDB 格式）拆分为 $N$ 个片段，并生成 $N$ 个 **gamess** MAKEFP 输入文件。

在第二步中，脚本分析由 **gamess** MAKEFP 生成的 `.efp` 文件，并使用同一个 MAP 文件对其进行自动编辑，从而生成最终的 EFP 输入文件（XYZ 格式）。

MAP 文件是脚本必需的输入。它定义了属于每个 EFP 片段的原子组，既用于 MAKEFP 计算，也用于后续的 EFP 作业。以下是 MAP 文件的说明：每个片段使用 $RESIDUE 节描述，并以 $end 结束。在本例中，Lys2 通过切断肽键提取出来，被切断的键用氢原子饱和。各变量的说明如下。

```qchem
$Residue
Name = lys2
PreAtoms = 14-35
NH = 14,12
CH = 34,36
PostAtoms = 14-35
Rescharge = +1
USEFP = lys2
$end
```

前四行是脚本第一步（**gamess** MAKEFP 作业）所必需的；后面的各行则是实际 EFP 作业所必需的：

- `Name`：残基名称
- `PreAtoms`：属于该残基、用于 **gamess** MAKEFP 计算的原子。
- `CH、NH 或 OH`：
在化学键断裂的情况下，会添加一个氢原子，使得在 X–Y 键中（其中 X 属于 Lys2 残基，Y 属于前一个或后一个残基），Y 原子沿 X–Y 轴方向被 H 取代。X-H 键的默认平衡距离设置为：C–H 键 1.08 Å，N–H 键 1.00 Å，O–H 键 0.94 Å。
需要指定 X 原子和 Y 原子的原子编号。
- `PostAtoms`：
当使用 HLA 或 CLA 方案时，在移除重叠的片段原子或加帽基团之后，属于该残基的原子。这一重要步骤根据截断程序（cutoff procedure，多极子的默认截断值设为 1.3 Å，极化展开点的默认截断值设为 1.2 Å）移除这些原子的多极子和极化展开点。重复点处的多极子展开会被消除，但为了保持每个氨基酸上的净整数电荷，加帽基团的单极子展开会重新分配到天然片段上。该方法称为 Expand-Remove-Redistribute（展开-移除-再分配）。关于极化展开点，当一个氢原子饱和悬挂键时仅移除一个极化展开点，而当加帽基团为胺或醛时，分别移除 6 个或 5 个极化展开点。
- `ResCharge`：移除重叠片段原子后残基的净电荷（*参见* LA 方案）。
- `USEFP`：
在实际 EFP 计算中，与该片段一起使用的 EFP 片段名称（以及 `.efp` 文件名称）。

!!! note "注意"
    - 在 MFCC 方案中，concap 片段名称的前两个字母必须为 "CC"。

    - 如果不存在 *PostAtoms* 关键字，第二个脚本将生成一个不对参数做任何修改的 EFP 作业文件，这对 MFCC 方案很有用。

    - **Q-Chem** 的 EFP 实现目前不支持偶极-四极极化率（dipole–quadrupole polarizabilities）。使用 **gamess** 生成的 `.efp` 文件中可能包含这些项，若要让 **Q-Chem** 读取该文件，应将其移除。

