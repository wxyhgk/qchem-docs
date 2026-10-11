---
title: "11.8.3 解读输出结果"
---

## 11.8.3 解读输出结果

（2026 年 7 月 4 日）

自洽场（SCF）收敛之后，极化嵌入（Polarizable Embedding, PE）模块会打印 PE 能量贡献的汇总信息，例如：

```qchem
----------------------------------------------------------------------
Polarizable Embedding Summary:

   Electrostatics:
      Electronic:                   0.30901227399981
      Nuclear:                      -0.32134940137969
      Multipole:                    0.00000000000000
      Total:                        -0.01233712737988

   Polarization:
      Electronic:                   -0.01817189734325
      Nuclear:                      0.01717961961137
      Multipole:                    -0.02091890381649
      Total:                        -0.02191118154837

   Total Energy:                    -0.03424830892825
----------------------------------------------------------------------
```

如果执行了 PE-ADC 计算，微扰修正会与激发能一起打印输出：

```qchem
Excited state 1 (singlet, A)                                     [converged]
  ----------------------------------------------------------------------------
  Term symbol:  2 (1) A                                     R^2 =  1.84764e-13

  Total energy:                                           -483.3704138865 a.u.
  Excitation energy:                                               3.906651 eV
  -------------------------------------------
  PE ptSS energy correction:                                      -0.001804 eV
  Corrected Excitation Energy (ptSS):                              3.906651 eV
  ----------------------------------------------------------------------------
```
