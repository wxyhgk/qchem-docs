---
title: "2.1.3 Q-Chem 辅助文件（*$QCAUX*）"
---

## 2.1.3 **Q-Chem** 辅助文件（*$QCAUX*）

（2026 年 7 月 4 日）

`$QCAUX` 环境变量用于指定 **Q-Chem** 搜索辅助文件及机器许可证（machine license）的目录。若未显式设置，则默认指向 `$QC/qcaux`。

*$QCAUX* 目录中包含了运行 **Q-Chem** 计算所需的文件，其中包括基组（Basis Set）与有效核势（ECP）的定义文件、SAD 初始猜测（参见第 [4](../ch04_scf/chap_scf.md) 章）、标准有效片段（effective fragment）库（参见第 [11.5](../ch11_env/sect_efp.md) 节），以及用于高效生成双电子积分的 **AOInts** 程序包的相关指令。
