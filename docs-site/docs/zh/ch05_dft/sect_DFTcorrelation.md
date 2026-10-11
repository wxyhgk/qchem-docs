---
title: "5.3.4 相关泛函"
---

## 5.3.4 相关泛函

（2026 年 7 月 4 日）

**注意：

本节中的所有相关泛函均可通过 *$rem* 变量 CORRELATION 来调用。每个类别中流行和/或推荐的泛函列在最前面，并以粗体标示。其余泛函按字母顺序排列。
**

- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

**PW92**：Perdew-Wang 于 1992 年提出的 LSDA 相关能参数化形式[[1074]](../bib_references/bib.md#bib1110)
- $\bullet$

**VWN5**（VWN）：Vosko-Wilk-Nusair LSDA 相关能参数化形式 #5[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

srVWN：Toulouse 及其合作者提出的 VWN 相关泛函的短程（short-range）版本[[1366]](../bib_references/bib.md#bib1426)
- $\bullet$

Liu-Parr：源自泛函展开表述的 Liu-Parr $\rho^{1/3}$ 模型[[848]](../bib_references/bib.md#bib870)
- $\bullet$

PK09：Proynov-Kong 于 2009 年提出的 LSDA 相关能参数化形式[[1127]](../bib_references/bib.md#bib1176)
- $\bullet$

PW92RPA：采用 RPA 数值的 Perdew-Wang 1992 年 LSDA 相关能参数化形式[[1074]](../bib_references/bib.md#bib1110)
- $\bullet$

srPW92：Paziani 及其合作者提出的 PW92 相关泛函的短程版本[[1056]](../bib_references/bib.md#bib1101)
- $\bullet$

PZ81：Perdew-Zunger 于 1981 年提出的 LSDA 相关能参数化形式[[1075]](../bib_references/bib.md#bib1107)
- $\bullet$

VWN1：Vosko-Wilk-Nusair LSDA 相关能参数化形式 #1[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN1RPA：采用 RPA 数值的 Vosko-Wilk-Nusair LSDA 相关能参数化形式 #1[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN2：Vosko-Wilk-Nusair LSDA 相关能参数化形式 #2[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN3：Vosko-Wilk-Nusair LSDA 相关能参数化形式 #3[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

VWN4：Vosko-Wilk-Nusair LSDA 相关能参数化形式 #4[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

Wigner：Wigner 相关泛函（LYP 的简化形式）[[1467]](../bib_references/bib.md#bib1530)
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

BOP：采用适合 B88 交换的参数化的“单参数渐进式（one-parameter progressive）”相关泛函[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

**PBE**：Perdew、Burke 和 Ernzerhof 相关泛函[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

**LYP**：Lee-Yang-Parr 反平行自旋（opposite-spin）相关泛函[[780]](../bib_references/bib.md#bib813)
- $\bullet$

P86：基于 PZ81 LSDA 泛函的 Perdew-Wang 1986 年相关泛函[[1076]](../bib_references/bib.md#bib1109)
- $\bullet$

P86VWN5：基于 VWN5 LSDA 泛函的 Perdew-Wang 1986 年相关泛函[[1076]](../bib_references/bib.md#bib1109)
- $\bullet$

PBEloc：由 Della Sala 及其合作者对 beta 项进行修改后的 PBE 相关泛函
- $\bullet$

PBEBOP：采用适合 PBE 交换的参数化的“单参数渐进式”相关泛函[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

PBEsol：针对固体体系改进的 PBE 相关泛函[[1067]](../bib_references/bib.md#bib1118)
- $\bullet$

srPBE：Goll 及其合作者提出的 PBE 相关泛函的短程版本[[469]](../bib_references/bib.md#bib481)
- $\bullet$

PW91：Perdew-Wang 于 1991 年提出的相关泛函[[1063]](../bib_references/bib.md#bib1111)
- $\bullet$

regTPSS：对 PBE 相关泛函的轻微改进（也称为 vPBEc）[[1191]](../bib_references/bib.md#bib1246)
- $\circ$

元广义梯度近似（Meta-Generalized Gradient Approximation, meta-GGA）

- $\bullet$

**TPSS**：Tao、Perdew、Staroverov 和 Scuseria 相关泛函[[1344]](../bib_references/bib.md#bib1402)
- $\bullet$

**revTPSS**：TPSS 相关泛函的修订版本[[1066]](../bib_references/bib.md#bib1120)
- $\bullet$

B95：Becke 于 1995 年提出的两参数相关泛函[[98]](../bib_references/bib.md#bib80)
- $\bullet$

oTPSS：由 Grimme 及其合作者提出、带 2 个重新拟合参数的 TPSS 相关泛函（与 oTPSS 交换泛函配合使用）[[462]](../bib_references/bib.md#bib475)
- $\bullet$

PK06：Proynov-Kong 的“tLap”泛函，同时依赖于 $\tau$ 和拉普拉斯算符（Laplacian）[[1125]](../bib_references/bib.md#bib1173)
- $\bullet$

PKZB：Perdew、Kurth、Zupan 和 Blaha 相关泛函[[1064]](../bib_references/bib.md#bib1114)
- $\bullet$

SCAN：强约束且适当归一化（Strongly Constrained and Appropriately Normed）相关泛函[[1327]](../bib_references/bib.md#bib1387)
- $\bullet$

rSCAN：正则化（Regularized）的 SCAN 相关[[83]](../bib_references/bib.md#bib68)
- $\bullet$

r++SCAN：具有均匀密度极限与坐标缩放行为的正则化 SCAN[[421]](../bib_references/bib.md#bib430)
- $\bullet$

r2SCAN：重新正则化的 SCAN 相关[[419]](../bib_references/bib.md#bib428)
- $\bullet$

revSCAN：修订的 SCAN 相关[[944]](../bib_references/bib.md#bib984)
- $\bullet$

TM：Tao-Mo 相关泛函，是对 TPSS 相关泛函的轻微改进[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

revTM：修订的 TM 相关[[628]](../bib_references/bib.md#bib648)
- $\bullet$

rregTM：修订的正则化 TM 相关[[625]](../bib_references/bib.md#bib649)
- $\bullet$

TPSSloc：将其中的 PBE 成分替换为 PBEloc 相关泛函后的 TPSS 相关泛函
