---
title: "4.4.3 从磁盘读取分子轨道（MO）"
---

## 4.4.3 从磁盘读取分子轨道（MO）

(July 4, 2026)

有两种方法可以通过从磁盘读取的方式，将之前作业计算得到的 MO 系数加以利用：

1. 依次运行两个独立的作业，通过三个命令行变量调用 **Q-Chem**：

> ```qchem
> localhost-1> qchem job1.in job1.out save
>    localhost-2> qchem job2.in job2.out save
> ```

!!! note "注意"
    (1) 在 `job2.in` 中，*$rem* 变量 SCF_GUESS 必须设置为 READ。
    (2) 作业结束时，临时文件（scratch files）会保留在 `$QCSCRATCH/save` 目录中。

2. 运行批处理作业（batch job），将两个作业放入同一个输入文件中，并用单独一行上的字符串 `@@@` 分隔。

!!! note "注意"
    (1) 在批处理文件的第二个作业中，SCF_GUESS 必须设置为 READ。
    (2) 无需使用第三个 **Q-Chem** 命令行变量。
    (3) 与 SAD 初始猜测（guess）类似，**Q-Chem** 至少需要执行两个 SCF 循环，
    以确保 SCF 正常收敛（即密度的幂等性，idempotency）。


!!! note "注意"
    需要由用户自行确保两个作业所使用的基组（basis sets）相互匹配。程序内部
    不会对此进行检查，不过被读取的占据轨道在读入后会在当前基组下重新正交化。
    如果希望将较小基组的结果投影到较大基组中，请参阅第 [4.4.5](sect_projection.md) 节。


???+ example "示例 4.5：OH 自由基 ROHF 计算的输入文件。先对阳离子进行一次 SCF 循环计算，
以获得质量较好的初始猜测轨道，随后读入这些轨道作为自由基的初始猜测。这样可以避免使用 Q-Chem 默认的
ROHF GWH 猜测，后者往往质量不佳。"
    ```qchem
    $comment
       OH radical, part 1. Do initial iterations of cation orbitals.
    $end
    
    $molecule
       1  1
       O  0.000   0.000   0.000
       H  0.000   0.000   1.000
    $end
    
    $rem
       BASIS           =  6-311++G(2df)
       METHOD          =  hf
       THRESH          =  10
       MAX_SCF_CYCLES  =  2
       SCF_CONVERGENCE =  1
    $end
    
    @@@
    
    $comment
       OH radical, part 2. Read cation orbitals, do the radical
    $end
    
    $molecule
       0  2
       O  0.000   0.000   0.000
       H  0.000   0.000   1.000
    $end
    
    $rem
       BASIS            =  6-311++G(2df)
       METHOD           =  hf
       UNRESTRICTED     =  false
       SCF_ALGORITHM    =  dm
       SCF_CONVERGENCE  =  7
       SCF_GUESS        =  read
       THRESH           =  10
    $end
    ```
