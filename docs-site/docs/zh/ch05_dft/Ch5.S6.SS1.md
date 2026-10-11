---
title: "5.6.1 引言"
---

## 5.6.1 引言

（2026 年 7 月 4 日）

像 LRC-$\omega$PBE 这样的 RSH 泛函，试图在尽可能小地扰动原始泛函（在本例中为 PBE）的前提下引入 100% 的长程（LR）Hartree-Fock 交换；而另一些 RSH 泛函则更具经验性质，其程分离参数（range-separation parameters）已与泛函中的所有其他参数一同经过精细的参数化拟合。由于这些泛函的程分离参数应视为固定值，我们首先在 [5.6.2 节](subsec_wb97series.md) 中讨论它们。
用户自定义的程分离参数取值在 [5.6.3 节](ex_ks-wb97xd4.md) 中讨论，而 [5.6.4 节](subsubsec_w-tuning.md) 则介绍了一种程序，可为 LRC-$\omega$PBE 或 LRC-$\mu$PBE 等泛函选取最优的、体系特定的该参数（$\omega$ 或 $\mu$）值。
