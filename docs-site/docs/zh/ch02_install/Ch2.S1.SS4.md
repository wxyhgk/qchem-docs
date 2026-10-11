---
title: "2.1.4 Q-Chem 运行时环境变量"
---

## 2.1.4 **Q-Chem** 运行时环境变量

（2026 年 7 月 4 日）

**Q-Chem** 在执行任何计算之前，需要预先设置以下 Shell 环境变量：

| QC | 定义 Q-Chem 目录结构所在的位置。`qchem.install` Shell 脚本会自动确定该位置。 |
| --- | --- |
| QCAUX | 定义 Q-Chem 所需的辅助信息所在的位置，其中包括运行 Q-Chem 所需的许可证（License）。若用户未显式设置，则默认指向 `$QC/qcaux`。 |
| QCSCRATCH | 定义 Q-Chem 存放临时文件的目录。作业成功结束后，Q-Chem 通常会删除这些文件，但若需要也可以保留。因此，`$QCSCRATCH` 应设置为希望保存文件的位置。 |
