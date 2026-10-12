---
title: "5.3.3 交换泛函"
---

## 5.3.3 交换泛函

（2026 年 7 月 4 日）

!!! note "注意"
    本节中的所有交换泛函均可通过 *$rem* 变量 EXCHANGE 调用。每一类中常用和/或推荐的泛函列在最前面，并以粗体标示。其余泛函按字母顺序排列。


- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

**Slater**：Slater-Dirac 交换泛函（$\alpha=2/3$ 的 X$\alpha$ 方法）[[329]](../bib_references/bib.md#bib333)
- $\bullet$

SR_LSDA (BNL)：Slater-Dirac 交换泛函的短程（short-range）版本[[444]](../bib_references/bib.md#bib464)
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

**PBE**：Perdew、Burke 和 Ernzerhof 交换泛函[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

**B88**：Becke 1988 年交换泛函[[95]](../bib_references/bib.md#bib74)
- $\bullet$

**revPBE**：Zhang 和 Yang 对 PBE 交换泛函的单参数修正[[1552]](../bib_references/bib.md#bib1606)
- $\bullet$

AK13：Armiento-Kümmel 2013 年交换泛函[[52]](../bib_references/bib.md#bib35)
- $\bullet$

B86：Becke 1986 年交换泛函（X$\alpha\beta\gamma$）[[92]](../bib_references/bib.md#bib71)
- $\bullet$

G96：Gill 1996 年交换泛函[[453]](../bib_references/bib.md#bib463)
- $\bullet$

mB86：Becke 1986 年"修正梯度校正"（modified gradient correction）交换泛函[[93]](../bib_references/bib.md#bib72)
- $\bullet$

mPW91：1991 年 Perdew-Wang 交换泛函的修正版本（Adamo 和 Barone）[[18]](../bib_references/bib.md#bib2)
- $\bullet$

muB88 ($\mu$B88)：Hirao 及其合作者提出的 B88 交换泛函短程版本[[609]](../bib_references/bib.md#bib632)
- $\bullet$

muPBE ($\mu$PBE)：Hirao 及其合作者提出的 PBE 交换泛函短程版本[[609]](../bib_references/bib.md#bib632)
- $\bullet$

srPBE：Goll 及其合作者提出的 PBE 交换泛函短程版本[[469]](../bib_references/bib.md#bib481)
- $\bullet$

optB88：Michaelides 及其合作者对原始 B88 交换泛函的重新拟合版本（与 vdW-DF-04 配合使用）[[696]](../bib_references/bib.md#bib728)
- $\bullet$

OPTX：Handy 和 Cohen 提出的双参数交换泛函[[517]](../bib_references/bib.md#bib531)
- $\bullet$

PBEsol：针对固体体系修正的 PBE 交换泛函[[1067]](../bib_references/bib.md#bib1118)
- $\bullet$

PW86：Perdew-Wang 1986 年交换泛函[[1073]](../bib_references/bib.md#bib1108)
- $\bullet$

PW91：Perdew-Wang 1991 年交换泛函[[1063]](../bib_references/bib.md#bib1111)
- $\bullet$

RPBE：Hammer、Hansen 和 Norskov 交换泛函（PBE 的修正版本）[[514]](../bib_references/bib.md#bib527)
- $\bullet$

rPW86：1986 年 Perdew-Wang 交换泛函的修订版本（Murray *et al.*）[[969]](../bib_references/bib.md#bib1010)
- $\bullet$

SOGGA：Zhao 和 Truhlar 提出的二阶 GGA 泛函[[1567]](../bib_references/bib.md#bib1626)
- $\bullet$

wPBE ($\omega$PBE)：Henderson *et al.* 提出的 PBE GGA 短程交换空穴模型[[554]](../bib_references/bib.md#bib569)
- $\circ$

Meta-广义梯度近似（meta-Generalized Gradient Approximation, meta-GGA）

- $\bullet$

**TPSS**：Tao、Perdew、Staroverov 和 Scuseria 交换泛函[[1344]](../bib_references/bib.md#bib1402)
- $\bullet$

**revTPSS**：TPSS 交换泛函的修订版本[[1066]](../bib_references/bib.md#bib1120)
- $\bullet$

BLOC：对 TPSS 交换泛函的微小修正（修改），与 TPSSloc 相关泛函配合使用效果最佳
（两者均由 Della Sala 及其合作者提出）[[264]](../bib_references/bib.md#bib265)
- $\bullet$

modTPSS：TPSS 交换泛函的单参数版本[[1069]](../bib_references/bib.md#bib1117)
- $\bullet$

oTPSS：Grimme 及其合作者提出的带 5 个重新拟合参数的 TPSS 交换泛函（与 oTPSS 相关泛函配合使用）
[[462]](../bib_references/bib.md#bib475)
- $\bullet$

PBE-GX：Pierre-François Loos 提出的首个基于有限均匀电子气（而非无限均匀电子气 UEG）的交换泛函[[860]](../bib_references/bib.md#bib894)
- $\bullet$

PKZB：Perdew、Kurth、Zupan 和 Blaha 交换泛函[[1064]](../bib_references/bib.md#bib1114)
- $\bullet$

regTPSS：TPSS 交换泛函的正则化（regularized）版本（解决极限取值次序问题）[[1191]](../bib_references/bib.md#bib1246)
- $\bullet$

SCAN：强约束且适当规范化（Strongly Constrained and Appropriately Normed）交换泛函[[1327]](../bib_references/bib.md#bib1387)
- $\bullet$

rSCAN：正则化的 SCAN 交换泛函[[83]](../bib_references/bib.md#bib68)
- $\bullet$

r++SCAN：具有均匀密度极限与坐标缩放行为的正则化 SCAN[[421]](../bib_references/bib.md#bib430)
- $\bullet$

r2SCAN：重新正则化的 SCAN 交换泛函[[419]](../bib_references/bib.md#bib428)
- $\bullet$

r4SCAN：在满足 SCAN 精确约束条件下的正则化 SCAN[[421]](../bib_references/bib.md#bib430)
- $\bullet$

revSCAN：SCAN 交换泛函的修订版本[[944]](../bib_references/bib.md#bib984)
- $\bullet$

TM：Tao-Mo 交换泛函，通过对常规交换空穴的精确建模推导得到[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

regTM：正则化的 TM 交换泛函[[1045]](../bib_references/bib.md#bib1090)
- $\bullet$

revTM：修订的 TM 交换泛函[[628]](../bib_references/bib.md#bib648)
- $\bullet$

TASK：TASK 交换泛函[[53]](../bib_references/bib.md#bib36)
- $\bullet$

mTASK：修正的 TASK 交换泛函[[989]](../bib_references/bib.md#bib1031)
