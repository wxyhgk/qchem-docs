---
title: "3.5.1 概述"
---

## 3.5.1 概述

（2026 年 7 月 4 日）

有时将一系列作业（job）放入单个 **Q-Chem** 输入文件中会很有用，各个独立输入之间用仅包含字符串 `@@@` 的一行来分隔。这些作业的输出随后会按顺序追加到单个输出文件中。这样做的好处是（a）在后续作业中使用先前作业获得的信息（*即*，优化后的几何结构）；或（b）将相关的计算保留在同一个输出文件中。

应当注意以下几点限制：

- •

第一个作业会覆盖工作目录中同名的任何已有输出文件。重启（Restarting）该作业同样会覆盖任何已有文件。
- •

**Q-Chem** 会在启动时立即从输入文件中读取所有作业并存储起来。因此，在通过命令行启动 **Q-Chem** 之后，无法再对后续作业的细节做任何修改，即使这些后续作业尚未运行。
- •

如果其中某个作业失败，**Q-Chem** 无论后果如何都会继续执行批处理文件（batch file）中的下一个作业。
- •

程序不会检查依赖关系是否满足，也不会检查信息是否一致。例如，在几何优化之后进行频率计算时，后者不会尝试检查优化是否成功。当从先前作业读取分子轨道（MO）系数时，确保两次计算使用相同基组（Basis Set）是用户的责任，因为程序默认它们是一致的。
- •

在批处理作业中，暂存文件（Scratch File）会从一个作业保留到下一个作业，以便先前作业的信息能与后续作业共享；但在整个批处理作业完成后这些文件会被删除，除非提供了 *–save* 命令行参数，如第 [2 章](../ch02_install/chap_install.md) 所述。

下面的示例请求一个批处理作业，它由（$i$）HF/6-31G* 水平的几何优化；随后是（$ii$）在同一理论水平下、使用先前优化几何结构（并读入优化作业最终得到的分子轨道）的频率计算；最后是（$iii$）在相同几何结构下、但在更高理论水平 MP2/6-311G(d,p) 上的单点计算。

???+ example "示例 3.11：在单个输入文件中使用先前作业信息的示例。"
    ```qchem
    $comment
       Optimize H-H at HF/6-31G*
    $end
    
    $molecule
       0 1
       H
       H  1  r
    
       r = 1.1
    $end
    
    $rem
       JOBTYPE       opt    Optimize the bond length
       METHOD        hf
       BASIS         6-31G*
    $end
    
    @@@
    
    $comment
       Now calculate the frequency of H-H at the same level of theory.
    $end
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE       freq    Calculate vibrational frequency
       METHOD        hf
       BASIS         6-31G*
       SCF_GUESS     read    Read the MOs from disk
    $end
    
    @@@
    
    $comment
      Now a single point calculation at at MP2/6-311G(d,p)//HF/6-31G*
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD        mp2
       BASIS         6-311G(d,p)
    $end
    ```
