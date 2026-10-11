---
title: "8.10.6 有效核势（ECP）与电子相关"
---

## 8.10.6 有效核势（ECP）与电子相关

（2026 年 7 月 4 日）

有效核势（Effective Core Potential, ECP）软件包已与电子相关软件包集成，因此可以将 **Q-Chem** 的任何后 Hartree-Fock（post-Hartree-Fock）方法应用于部分原子带有赝势（pseudopotential）的体系。当然，被 ECP 替换掉的芯电子（core electrons）对相关能的贡献*不*包含在内。从这个意义上说，使用 ECP 得到的相关能与冻结芯（frozen-core）计算的相关能具有可比性。不过，使用 ECP 实际上会同时移除芯电子*以及*相应的虚（未占据）轨道（virtual/unoccupied orbitals）。

在采用 ECP 的密度泛函理论（Density Functional Theory, DFT）计算中，交换-相关能量完全由非芯电子贡献。当不存在化学上重要的芯/价（core/valence）效应时，这样做是令人满意的；但如果存在此类效应，则可能引入显著误差，尤其当你使用的是“大芯”（large-core）ECP 时更是如此。第 [5](../ch05_dft/chap_DFT.md) 章中讨论的任何局域泛函、梯度校正泛函及杂化泛函（hybrid functionals）均可使用，你也可以用用户自定义的杂化泛函执行 ECP 计算。

???+ example "示例 8.11: 使用 HF/fit-LANL2DZ 优化 Se ${}_{8}$ 的结构，随后在 MP2/fit-LANL2DZ 水平上进行单点能计算。"
    ```qchem
    $molecule
       0  1
       x1
       x2   x1  xx
       Se1  x1  sx  x2  90.
       Se2  x1  sx  x2  90.  Se1  90.
       Se3  x1  sx  x2  90.  Se2  90.
       Se4  x1  sx  x2  90.  Se3  90.
       Se5  x2  sx  x1  90.  Se1  45.
       Se6  x2  sx  x1  90.  Se5  90.
       Se7  x2  sx  x1  90.  Se6  90.
       Se8  x2  sx  x1  90.  Se7  90.
    
       xx = 1.2
       sx = 2.8
    $end
    
    $rem
       JOBTYPE    opt
       METHOD     hf
       ECP        fit-lanl2dz
       BASIS      lanl2dz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE       sp        Single-point energy
       METHOD        mp2       MP2 correlation energy
       ECP           fit-lanl2dz   Hay-Wadt ECP and basis
       BASIS         lanl2dz
       SCF_GUESS     read      Read in the MOs
    $end
    ```
