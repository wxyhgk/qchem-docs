---
title: "7.10.9 用于描述亚稳电子态的 CAP/ADC 方法"
---

## 7.10.9 用于描述亚稳电子态的 CAP/ADC 方法

（2026 年 7 月 4 日）

为了描述亚稳电子态并计算此类电子共振的位置与宽度，*复吸收势*（complex absorbing potential, CAP）方法学[[1175]](../bib_references/bib.md#bib1228)
 已通过子空间投影（subspace projection）的方式与所有可用的非 CVS ADC 方法相结合。[[1284]](../bib_references/bib.md#bib1340)

在这一方法中，CAP 被投影到由若干个已收敛的（ADC、IP-ADC 或 EA-ADC）态所张成的子空间上。为此，利用了通过二阶 ISR（imaginary time formalism / intermediate state representation，即中间态表示）计算得到的一电子态密度与态间跃迁密度。

CAP 轨迹（CAP trajectories）的产生以及共振参数的确定可以在计算结束以后
*a posteriori*（即后处理）的方式完成（详见文献 [[1198]](../bib_references/bib.md#bib1252)），
*换言之*，只需执行一次电子结构计算即可。作为该方法的一个显著特点，在一次 ADC 计算中可以处理一系列不同的 CAP 起始值（onset）。

通过设置 ADC_CAP = 1 即可启用 CAP/ADC 计算，这会自动隐含 CAP 强度为 $\eta=1$（或 CAP_ETA = 100000）。可以采用不同的 CAP 类型，不过通常推荐使用平滑 Voronoi CAP[[1283]](../bib_references/bib.md#bib1341)，
 该类型可通过设置 CAP_TYPE = 2 来获得。对于此 CAP 类型，可以使用
CAP_X、CAP_X_STEP 和 CAP_X_END 关键字来控制一系列不同的起始值。例如，若要在起始值 2.0、3.0 和 3.0 处获取子空间投影的 CAP/ADC 输出……
