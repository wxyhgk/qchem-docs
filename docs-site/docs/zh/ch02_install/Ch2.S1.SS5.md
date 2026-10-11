---
title: "2.1.5 用户账户配置"
---

## 2.1.5 用户账户配置

（2026 年 7 月 4 日）

为了使各个用户能够运行 **Q-Chem**，必须正确设置用户的文件访问权限，
以便该用户能够读取、写入和执行所需的 **Q-Chem** 文件。在您的机器上
创建一个 *qchem* 用户组，并将 **Q-Chem** 目录的组属主递归地更改为
*qchem* 组，可能会带来便利。

在运行任何 **Q-Chem** 计算之前，需要先初始化 **Q-Chem** 的运行时环境，
具体做法是加载（source）环境设置脚本 qcenv.sh（用于 bash）或
qcenv.csh（用于 csh 和 tcsh），这些脚本在成功安装后会被放置在 **Q-Chem** 的顶层目录中。
对用户而言，更 convenient 的做法是将 **Q-Chem** 的环境设置加入到自己的
shell 启动脚本中，*e.g.*，csh 或 tcsh 分别对应 `.cshrc` 或 `.tcshrc`，bash 则对应 `.bashrc`。

若使用 csh 或 tcsh shell，请将以下几行添加到用户主目录下的 `.cshrc` 文件中：

> ```qchem
> #
> setenv  QC         qchem_root_directory_name
> setenv  QCSCRATCH  scratch_directory_name
> source  $QC/qcenv.csh
> #
> ```

若使用 Bourne 再次式 shell（bash），请将以下几行添加到用户主目录下的 `.bashrc` 文件中：

> ```qchem
> #
> export QC=qchem_root_directory_name
> export QCSCRATCH=scratch_directory_name
> . $QC/qcenv.sh
> #
> ```
