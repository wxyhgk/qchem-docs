---
title: "2.1.6 进一步定制"
---

## 2.1.6 进一步定制

(July 4, 2026)

**Q-Chem** 提供了一种简单的机制，使用户能够设置用户自定义的长期默认值，以覆盖程序内置的默认值。这类默认值最适用于与具体机器相关的特性，例如内存分配，因为可用内存总量会因硬件和记账（accounting）配置的不同而因机器而异。不过，用户也可以发现此定制功能的其他重要用途。**Q-Chem** 从四个来源获取输入初始化变量：

1. 用户输入文件
2. `$HOME/.qchemrc` 文件
3. `$QC/config/preferences` 文件
4. “出厂安装”（Factory installed）的程序默认值

在此列表中位置靠前的输入机制会覆盖位置靠后的机制。机制 #2 和 #3 允许用户为某些变量指定备选默认设置，从而覆盖 **Q-Chem** 的“出厂安装”默认值。这可以由系统管理员通过在 `$QC/config` 目录中添加 `preferences` 文件来实现，也可以由个人用户通过在主目录中放置 `.qchemrc` 文件来实现。

!!! note "注意"
    `.qchemrc` 和 `preferences` 文件并非运行 **Q-Chem** 的必需文件，并且目前仅支持 *$rem* 输入段中的关键字。


`.qchemrc` 和 `preferences` 文件的格式由一个 *$rem* 关键字段组成，与 **Q-Chem** 输入文件中的写法相同，并以通常的 *$end* 关键字结束。其他任何 `$whatever` 段都会被忽略。为便于结果复现，作业输出文件的开头附近会包含 `.qchemrc` 文件（如果存在）的副本。（`.qchemrc ` 和 `preferences` 文件的权限必须设置为允许调用 **Q-Chem** 的用户读取。）两种文件的格式如下：

```qchem
$rem
   BASIS = 6-31G*
   METHOD = B3LYP
$end
```

```qchem
$rem
   MEMORY = 4000
   NCPU = 8
$end
```
