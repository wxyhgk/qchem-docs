---
title: "5.3.5 交换-关联泛函"
---

## 5.3.5 交换-关联泛函

（2026 年 7 月 4 日）

**注意：

本节中的所有交换-关联泛函均可通过 *$rem* 变量 METHOD 调用。出于向后兼容性的考虑，除标注星号（*）的泛函之外，所有交换-关联泛函均可使用 *$rem* 变量 EXCHANGE 调用。每个类别中流行和/或推荐的泛函列在最前面，并以粗体标示。其余泛函按字母顺序排列。
**

- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

**SPW92***：Slater LSDA 交换 + PW92 LSDA 关联
- $\bullet$

LDA：Slater LSDA 交换 + VWN5 LSDA 关联
- $\bullet$

SVWN5*：Slater LSDA 交换 + VWN5 LSDA 关联
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

**B97-D3(0)**：B97-D，采用拟合的 DFT-D3(0) 尾部项替代原始的 DFT-D2 尾部项[[486]](../bib_references/bib.md#bib504)
- $\bullet$

**B97-D**：Grimme 提出的 9 参数色散校正（DFT-D2）泛函[[494]](../bib_references/bib.md#bib502)
- $\bullet$

**PBE***：PBE GGA 交换 + PBE GGA 关联
- $\bullet$

**BLYP***：B88 GGA 交换 + LYP GGA 关联
- $\bullet$

**revPBE***：revPBE GGA 交换 + PBE GGA 关联
- $\bullet$

BEEF-vdW：通过贝叶斯误差估计（Bayesian error estimation）框架开发的 31 参数半经验交换泛函，与 PBE 关联及 vdW-DF-10 非局域关联（NLC）配对使用[[1449]](../bib_references/bib.md#bib1510)
- $\bullet$

BOP：B88 GGA 交换 + BOP“单参数渐进式（one-parameter progressive）”GGA 关联[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

BP86*：B88 GGA 交换 + P86 GGA 关联
- $\bullet$

BP86VWN*：B88 GGA 交换 + P86VWN5 GGA 关联
- $\bullet$

BPBE*：B88 GGA 交换 + PBE GGA 关联
- $\bullet$

EDF1：对 BLYP 的改进，在 6-31+G* 基组下具有良好的表现[[25]](../bib_references/bib.md#bib9)
- $\bullet$

EDF2：对 B3LYP 的改进，在 cc-pVTZ 基组下针对频率计算具有良好的表现[[828]](../bib_references/bib.md#bib864)
- $\bullet$

GAM：Truhlar 及其合作者提出的 21 参数非可分离梯度近似泛函[[1534]](../bib_references/bib.md#bib1596)
- $\bullet$

HCTH93（HCTH/93）：Handy 及其合作者基于 93 个体系训练的 15 参数泛函[[516]](../bib_references/bib.md#bib530)
- $\bullet$

HCTH120（HCTH/120）：Boese *et al.* 基于 120 个体系训练的 15 参数泛函[[137]](../bib_references/bib.md#bib127)
- $\bullet$

HCTH147（HCTH/147）：Boese *et al.* 基于 147 个体系训练的 15 参数泛函[[137]](../bib_references/bib.md#bib127)
- $\bullet$

HCTH407（HCTH/407）：Boese 和 Handy 基于 407 个体系训练的 15 参数泛函[[138]](../bib_references/bib.md#bib128)
- $\bullet$

HLE16 – 将 HCTH/407 交换泛函乘以 1.25 增强 + 将 HCTH/407 关联泛函乘以 0.5 增强[[1400]](../bib_references/bib.md#bib1460)
- $\bullet$

KT1：专为磁屏蔽常数计算设计的 GGA 泛函[[674]](../bib_references/bib.md#bib699)
- $\bullet$

KT2：专为磁屏蔽常数计算设计的 GGA 泛函[[674]](../bib_references/bib.md#bib699)
- $\bullet$

KT3：在主族核磁共振（NMR）屏蔽常数方面结果有所改进的 GGA 泛函[[675]](../bib_references/bib.md#bib700)
- $\bullet$

mPW91*：mPW91 GGA 交换 + PW91 GGA 关联
- $\bullet$

N12：Peverati 和 Truhlar 提出的 21 参数非可分离梯度近似泛函[[1086]](../bib_references/bib.md#bib1132)
- $\bullet$

OLYP*：OPTX GGA 交换 + LYP GGA 关联
- $\bullet$

PBEOP：PBE GGA 交换 + PBEOP“单参数渐进式”GGA 关联[[1377]](../bib_references/bib.md#bib1438)
- $\bullet$

PBEsol*：PBEsol GGA 交换 + PBEsol GGA 关联
- $\bullet$

PW91*：PW91 GGA 交换 + PW91 GGA 关联
- $\bullet$

RPBE*：RPBE GGA 交换 + PBE GGA 关联
- $\bullet$

rVV10*：rPW86 GGA 交换 + PBE GGA 关联 + rVV10 非局域关联[[1192]](../bib_references/bib.md#bib1247)
- $\bullet$

SOGGA*：SOGGA GGA 交换 + PBE GGA 关联
- $\bullet$

SOGGA11：Peverati、Zhao 和 Truhlar 提出的 20 参数泛函[[1089]](../bib_references/bib.md#bib1128)
- $\bullet$

VV10：rPW86 GGA 交换 + PBE GGA 关联 + VV10 非局域关联[[1416]](../bib_references/bib.md#bib1477)
- $\circ$

元广义梯度近似（Meta-Generalized Gradient Approximation, meta-GGA）

- $\bullet$

**B97M-V**：Mardirossian 和 Head-Gordon 提出的 12 参数组合优化、色散校正（VV10）泛函[[904]](../bib_references/bib.md#bib938)
- $\bullet$

**B97M-rV***：B97M-V 密度泛函，其中 VV10 NLC 泛函被替换为 rVV10 NLC 泛函[[907]](../bib_references/bib.md#bib940)
- $\bullet$

**M06-L**：Zhao 和 Truhlar 提出的 34 参数泛函[[1565]](../bib_references/bib.md#bib1624)
- $\bullet$

**TPSS***：TPSS meta-GGA 交换 + TPSS meta-GGA 关联
- $\bullet$

**revTPSS***：revTPSS meta-GGA 交换 + revTPSS meta-GGA 关联
- $\bullet$

B97MV-D3s(BJ)：B97M-V 密度泛函，其中 VV10 NLC 泛函被替换为 DFT-D3s(BJ)（s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959）
- $\bullet$

B97MV-D4：B97M-V 密度泛函，其中 VV10 NLC 泛函被替换为 DFT-D4（s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487）
- $\bullet$

BLOC*：BLOC meta-GGA 交换 + TPSSloc meta-GGA 关联
- $\bullet$

M11-L：Peverati 和 Truhlar 提出的 44 参数双范围（dual-range）泛函[[1085]](../bib_references/bib.md#bib1131)
- $\bullet$

mBEEF：64 参数交换泛函，与 PBEsol 关联泛函配对使用[[1448]](../bib_references/bib.md#bib1511)
- $\bullet$

MGGA_MS0：MGGA_MS0 meta-GGA 交换 + regTPSS GGA 关联[[1328]](../bib_references/bib.md#bib1384)
- $\bullet$

MGGA_MS1：MGGA_MS1 meta-GGA 交换 + regTPSS GGA 关联[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MS2：MGGA_MS2 meta-GGA 交换 + regTPSS GGA 关联[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MVS：MGGA_MVS meta-GGA 交换 + regTPSS GGA 关联[[1326]](../bib_references/bib.md#bib1386)
- $\bullet$

MN12-L：Peverati 和 Truhlar 提出的 58 参数元非可分离梯度近似泛函[[1087]](../bib_references/bib.md#bib1133)
- $\bullet$

MN15-L：Yu、He 和 Truhlar 提出的 58 参数元非可分离梯度近似泛函[[1533]](../bib_references/bib.md#bib1598)
- $\bullet$

oTPSS*：oTPSS meta-GGA 交换 + oTPSS meta-GGA 关联
- $\bullet$

PKZB*：PKZB meta-GGA 交换 + PKZB meta-GGA 关联
- $\bullet$

revM06-L：31 参数修订版 M06-L 泛函
- $\bullet$

SCAN*：SCAN meta-GGA 交换 + SCAN meta-GGA 关联
- $\bullet$

rSCAN：rSCAN 交换 + rSCAN 关联
- $\bullet$

r++SCAN：r++SCAN 交换 + r++SCAN 关联
- $\bullet$

r2SCAN：r2SCAN 交换 + r2SCAN 关联
- $\bullet$

r4SCAN：r4SCAN 交换 + r2SCAN 关联
- $\bullet$

revSCAN：revSCAN 交换 + revSCAN 关联
- $\bullet$

t-HCTH（$\tau$-HCTH）：Boese 和 Handy 提出的 16 参数泛函[[139]](../bib_references/bib.md#bib129)
- $\bullet$

TM*：TM meta-GGA 交换 + TM meta-GGA 关联[[1343]](../bib_references/bib.md#bib1403)
- $\bullet$

revTM：revTM 交换 + revTM 关联
- $\bullet$

regTM：regTM 交换 + regTPSS 关联
- $\bullet$

rregTM：regTM 交换 + rregTM 关联
- $\bullet$

TASK：TASK 交换 + PW92 关联
- $\bullet$

mTASK：mTASK 交换 + PW92 关联
- $\bullet$

VSXC：Voorhis 和 Scuseria 提出的 21 参数泛函[[1393]](../bib_references/bib.md#bib1448)
- $\circ$

全局杂化广义梯度近似（Global Hybrid Generalized Gradient Approximation, GH GGA）

- $\bullet$

**B3LYP**：20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% VWN1RPA LSDA 关联 + 81% LYP GGA 关联[[96]](../bib_references/bib.md#bib78)
- $\bullet$

**PBE0**：25% HF 交换 + 75% PBE GGA 交换 + PBE GGA 关联[[19]](../bib_references/bib.md#bib3)
- $\bullet$

**revPBE0**：25% HF 交换 + 75% revPBE GGA 交换 + PBE GGA 关联
- $\bullet$

**B97**：Becke 原始的 10 参数密度泛函，含 19.43% HF 交换[[99]](../bib_references/bib.md#bib81)
- $\bullet$

B1LYP：25% HF 交换 + 75% B88 GGA 交换 + LYP GGA 关联[[17]](../bib_references/bib.md#bib1)
- $\bullet$

B1PW91：25% HF 交换 + 75% B88 GGA 交换 + PW91 GGA 关联[[17]](../bib_references/bib.md#bib1)
- $\bullet$

B3LYP5：20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% VWN5 LSDA 关联 + 81% LYP GGA 关联[[96]](../bib_references/bib.md#bib78)
- $\bullet$

B3P86：20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% VWN1RPA LSDA 关联 + 81% P86 GGA 关联
- $\bullet$

B3PW91：20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% PW92 LSDA 关联 + 81% PW91 GGA 关联[[96]](../bib_references/bib.md#bib78)
- $\bullet$

B5050LYP：50% HF 交换 + 8% Slater LSDA 交换 + 42% B88 GGA 交换 + 19% VWN5 LSDA 关联 + 81% LYP GGA 关联[[1239]](../bib_references/bib.md#bib1294)
- $\bullet$

B97-1：Becke B97 密度泛函的自洽参数化版本，含 21% HF 交换[[516]](../bib_references/bib.md#bib530)
- $\bullet$

B97-2：Tozer 及其合作者对 B97 的重新参数化，含 21% HF 交换[[1477]](../bib_references/bib.md#bib1539)
- $\bullet$

B97-3：Keal 和 Tozer 提出的 B97 的 16 参数版本，含约 $\approx$ 26.93% HF 交换[[676]](../bib_references/bib.md#bib701)
- $\bullet$

B97-K：Boese 和 Martin 针对动力学对 B97 的重新参数化，含 42% HF 交换[[140]](../bib_references/bib.md#bib130)
- $\bullet$

BHHLYP：50% HF 交换 + 50% B88 GGA 交换 + LYP GGA 关联，有时也称为 BH&H-LYP[[484]](../bib_references/bib.md#bib496)
- $\bullet$

HFLYP*：100% HF 交换 + LYP GGA 关联
- $\bullet$

MPW1K：42.8% HF 交换 + 57.2% mPW91 GGA 交换 + PW91 GGA 关联[[865]](../bib_references/bib.md#bib900)
- $\bullet$

MPW1LYP：25% HF 交换 + 75% mPW91 GGA 交换 + LYP GGA 关联[[18]](../bib_references/bib.md#bib2)
- $\bullet$

MPW1PBE：25% HF 交换 + 75% mPW91 GGA 交换 + PBE GGA 关联[[18]](../bib_references/bib.md#bib2)
- $\bullet$

MPW1PW91：25% HF 交换 + 75% mPW91 GGA 交换 + PW91 GGA 关联[[18]](../bib_references/bib.md#bib2)
- $\bullet$

O3LYP：11.61% HF 交换 + $\approx$ 7.1% Slater LSDA 交换 + 81.33% OPTX GGA 交换 + 19% VWN5 LSDA 关联 + 81% LYP GGA 关联[[586]](../bib_references/bib.md#bib609)
- $\bullet$

PBEh-3c：Grimme 及其合作者提出的低成本组合方案，仅可与 def2-mSVP 基组配合使用[[487]](../bib_references/bib.md#bib508)
- $\bullet$

PBE50：50% HF 交换 + 50% PBE GGA 交换 + PBE GGA 关联[[114]](../bib_references/bib.md#bib101)
- $\bullet$

SOGGA11-X：Peverati 和 Truhlar 提出的 21 参数泛函，含 40.15% HF 交换[[1083]](../bib_references/bib.md#bib1129)
- $\bullet$

WC04：为计算 ${}^{13}$C 化学位移而优化的杂化密度泛函[[1469]](../bib_references/bib.md#bib285)
- $\bullet$

WP04：为计算 ${}^{1}$H 化学位移而优化的杂化密度泛函[[1469]](../bib_references/bib.md#bib285)
- $\bullet$

X3LYP：21.8% HF 交换 + 7.3% Slater LSDA 交换 + $\approx$ 54.24% B88 GGA 交换 + $\approx$ 16.66% PW91 GGA 交换 + 12.9% VWN1RPA LSDA 关联 + 87.1% LYP GGA 关联[[1506]](../bib_references/bib.md#bib1567)
- $\circ$

全局杂化元广义梯度近似（Global Hybrid Meta-Generalized Gradient Approximation, GH meta-GGA）

- $\bullet$

**CF22D**：含 46.2806% HF 交换及经验阻尼色散项的全局泛函，由 Truhlar、Wang、He 及其合作者采用监督学习协议开发[[850]](../bib_references/bib.md#bib884)
- $\bullet$

**M06-2X**：Zhao 和 Truhlar 提出的 29 参数泛函，含 54% HF 交换[[1569]](../bib_references/bib.md#bib1628)
- $\bullet$

**TPSSh**：10% HF 交换 + 90% TPSS meta-GGA 交换 + TPSS meta-GGA 关联[[1294]](../bib_references/bib.md#bib1350)
- $\bullet$

**revTPSSh**：10% HF 交换 + 90% revTPSS meta-GGA 交换 + revTPSS meta-GGA 关联[[286]](../bib_references/bib.md#bib290)
- $\bullet$

M08-HX：Zhao 和 Truhlar 提出的 47 参数泛函，含 52.23% HF 交换[[1568]](../bib_references/bib.md#bib1627)
- $\bullet$

B1B95：28% HF 交换 + 72% B88 GGA 交换 + B95 meta-GGA 关联[[98]](../bib_references/bib.md#bib80)
- $\bullet$

B3TLAP：17.13% HF 交换 + 9.66% Slater LSDA 交换 + 72.6% B88 GGA 交换 + PK06 meta-GGA 关联[[1125]](../bib_references/bib.md#bib1173)
- $\bullet$

BB1K：42% HF 交换 + 58% B88 GGA 交换 + B95 meta-GGA 关联[[1560]](../bib_references/bib.md#bib1618)
- $\bullet$

BMK：Boese-Martin 动力学泛函（Boese-Martin functional for kinetics），含 42% HF 交换[[140]](../bib_references/bib.md#bib130)
- $\bullet$

dlDF：Szalewicz 及其合作者提出的无色散密度泛函（Dispersion-less density functional，基于 M05-2X 泛函形式）[[1078]](../bib_references/bib.md#bib1123)
- $\bullet$

M05：Zhao、Schultz 和 Truhlar 提出的 22 参数泛函，含 28% HF 交换[[1561]](../bib_references/bib.md#bib1622)
- $\bullet$

M05-2X：Zhao、Schultz 和 Truhlar 提出的 19 参数泛函，含 56% HF 交换[[1562]](../bib_references/bib.md#bib1623)
- $\bullet$

M06：Zhao 和 Truhlar 提出的 33 参数泛函，含 27% HF 交换[[1569]](../bib_references/bib.md#bib1628)
- $\bullet$

M06-HF：Zhao 和 Truhlar 提出的 32 参数泛函，含 100% HF 交换[[1566]](../bib_references/bib.md#bib1625)
- $\bullet$

M08-SO：Zhao 和 Truhlar 提出的 44 参数泛函，含 56.79% HF 交换[[1568]](../bib_references/bib.md#bib1627)
- $\bullet$

MGGA_MS2h：9% HF 交换 + 91 % MGGA_MS2 meta-GGA 交换 + regTPSS GGA 关联[[1325]](../bib_references/bib.md#bib1385)
- $\bullet$

MGGA_MVSh：25% HF 交换 + 75 % MGGA_MVS meta-GGA 交换 + regTPSS GGA 关联[[1326]](../bib_references/bib.md#bib1386)
- $\bullet$

MN15：Truhlar 及其合作者提出的 59 参数泛函，含 44% HF 交换[[1532]](../bib_references/bib.md#bib1597)
- $\bullet$

MPW1B95：31% HF 交换 + 69% mPW91 GGA 交换 + B95 meta-GGA 关联[[1563]](../bib_references/bib.md#bib1619)
- $\bullet$

MPWB1K：44% HF 交换 + 56% mPW91 GGA 交换 + B95 meta-GGA 关联[[1563]](../bib_references/bib.md#bib1619)
- $\bullet$

PW6B95：Zhao 和 Truhlar 提出的 6 参数组合，包含 28 % HF 交换、72 % 优化后的 PW91 GGA 交换以及重新优化的 B95 meta-GGA 关联[[1564]](../bib_references/bib.md#bib1621)
- $\bullet$

PWB6K：Zhao 和 Truhlar 提出的 6 参数组合，包含 46 % HF 交换、54 % 优化后的 PW91 GGA 交换以及重新优化的 B95 meta-GGA 关联[[1564]](../bib_references/bib.md#bib1621)
- $\bullet$

revM06：32 参数泛函，含 40.41% HF 交换[[1428]](../bib_references/bib.md#bib1489)
- $\bullet$

r2SCANh：10% HF 交换 + 90% r2SCAN meta-GGA 交换 + r2SCAN meta-GGA 关联[[172]](../bib_references/bib.md#bib166)
- $\bullet$

r2SCAN0：25% HF 交换 + 75% r2SCAN meta-GGA 交换 + r2SCAN meta-GGA 关联[[172]](../bib_references/bib.md#bib166)
- $\bullet$

r2SCAN50：50% HF 交换 + 50% r2SCAN meta-GGA 交换 + r2SCAN meta-GGA 关联[[172]](../bib_references/bib.md#bib166)
- $\bullet$

SCAN0：25% HF 交换 + 75% SCAN meta-GGA 交换 + SCAN meta-GGA 关联[[602]](../bib_references/bib.md#bib625)
- $\bullet$

t-HCTHh（$\tau$-HCTHh）：Boese 和 Handy 提出的 17 参数泛函，含 15% HF 交换[[139]](../bib_references/bib.md#bib129)
- $\bullet$

TPSS0：25% HF 交换 + 75% TPSS meta-GGA 交换 + TPSS meta-GGA 关联[[492]](../bib_references/bib.md#bib500)
- $\circ$

范围分离杂化广义梯度近似（Range-Separated Hybrid Generalized Gradient Approximation, RSH GGA）

- $\bullet$

**wB97X-V**（$\omega$B97X-V）：10 参数组合优化、色散校正（VV10）泛函，短程（SR）HF 交换 16.7%，长程（LR）HF 交换 100%，$\omega=0.3$[[903]](../bib_references/bib.md#bib937)
- $\bullet$

wB97XV-D3s(BJ)（$\omega$B97XV-D3s(BJ)）：$\omega$B97X-V，其中 VV10 NLC 泛函被替换为 DFT-D3s(BJ)（s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959）
- $\bullet$

wB97XV-D4（$\omega$B97XV-D4）：$\omega$B97X-V，其中 VV10 NLC 泛函被替换为 DFT-D4（s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487）
- $\bullet$

wB97X-D（$\omega$B97X-D）：15 参数色散校正（DFT-CHG）泛函，短程 HF 交换约 $\approx$ 22.2%，长程 HF 交换 100%，$\omega=0.2$[[224]](../bib_references/bib.md#bib219)
- $\bullet$

wB97X-D3（$\omega$B97X-D3）：16 参数色散校正（DFT-D3(0)）泛函，短程 HF 交换约 $\approx$ 19.57%，长程 HF 交换 100%，$\omega=0.25$[[832]](../bib_references/bib.md#bib225)
- $\bullet$

KS-$\omega$B97X-D4（用法参见示例 [5.6.3](ex_ks-wb97xd4.md)）：10 参数组合优化、色散校正（D4）泛函，短程 HF 交换约 $\approx$ 18.7%，长程 HF 交换 100%，$\omega=0.3$[[815]](../bib_references/bib.md#bib858)
- $\bullet$

CAM-B3LYP：Handy 及其合作者提出的库仑衰减方法（Coulomb-attenuating method, CAM）泛函[[1512]](../bib_references/bib.md#bib1575)
- $\bullet$

CAM-QTP00：重新参数化的 CAM-B3LYP，设计目标是针对水分子的所有占据轨道满足 IP 定理[[1399]](../bib_references/bib.md#bib1459)
- $\bullet$

CAM-QTP01：重新参数化的 CAM-B3LYP，针对水分子的价层电离能（IP）、34 个激发态以及 G2-1 原子化能进行了优化[[643]](../bib_references/bib.md#bib667)
- $\bullet$

HSE-HJS： screened-exchange“HSE06”泛函，短程 HF 交换 25%，长程 HF 交换 0%，$\omega$=0.11，采用更新后的 HJS PBE 交换空穴（exchange hole）模型[[721]](../bib_references/bib.md#bib753)
- $\bullet$

LC-rVV10*：LC-VV10 密度泛函，其中 VV10 NLC 泛函被替换为 rVV10 NLC 泛函[[907]](../bib_references/bib.md#bib940)
- $\bullet$

LC-VV10：短程 HF 交换 0% + 长程 HF 交换 100% + $\omega$PBE GGA 交换 + PBE GGA 关联 + VV10 非局域关联（$\omega$=0.45）[[1416]](../bib_references/bib.md#bib1477)
- $\bullet$

LC-wPBE08（LC-$\omega$PBE08）：短程 HF 交换 0% + 长程 HF 交换 100% + $\omega$PBE GGA 交换 + PBE GGA 关联（$\omega$=0.45）[[1446]](../bib_references/bib.md#bib1508)
- $\bullet$

LRC-BOP（LRC-$\mu$BOP）：短程 HF 交换 0% + 长程 HF 交换 100% + $\mu$B88 GGA 交换 + BOP GGA 关联（$\omega$=0.47）[[1285]](../bib_references/bib.md#bib1337)
- $\bullet$

LRC-wPBE（LRC-$\omega$PBE）：短程 HF 交换 0% + 长程 HF 交换 100% + $\omega$PBE GGA 交换 + PBE GGA 关联（$\omega$=0.3）[[1177]](../bib_references/bib.md#bib1230)
- $\bullet$

LRC-wPBEh（LRC-$\omega$PBEh）：短程 HF 交换 20% + 长程 HF 交换 100% + 80% $\omega$PBE GGA 交换 + PBE GGA 关联（$\omega$=0.2）[[1178]](../bib_references/bib.md#bib1231)
- $\bullet$

N12-SX：26 参数非可分离 GGA，短程 HF 交换 25%，长程 HF 交换 0%，$\omega=0.11$[[1088]](../bib_references/bib.md#bib1134)
- $\bullet$

rCAM-B3LYP：重新拟合的 CAM-B3LYP，目标是最小化多电子自相互作用误差[[260]](../bib_references/bib.md#bib261)
- $\bullet$

wB97（$\omega$B97）：13 参数泛函，短程 HF 交换 0%，长程 HF 交换 100%，$\omega=0.4$[[223]](../bib_references/bib.md#bib218)
- $\bullet$

wB97X（$\omega$B97X）：14 参数泛函，短程 HF 交换约 $\approx$ 15.77%，长程 HF 交换 100%，$\omega=0.3$[[223]](../bib_references/bib.md#bib218)
- $\bullet$

wB97X-rV*（$\omega$B97X-rV）：$\omega$B97X-V 密度泛函，其中 VV10 NLC 泛函被替换为 rVV10 NLC 泛函[[907]](../bib_references/bib.md#bib940)
- $\circ$

范围分离杂化元广义梯度近似（Range-Separated Hybrid Meta-Generalized Gradient Approximation, RSH meta-GGA）

- $\bullet$

**COACH**：精细优化且适当约束的杂化（Carefully Optimized and Appropriately Constrained Hybrid, COACH）泛函，属于范围分离杂化 meta-GGA 类，短程 HF 交换 22.878981%，长程 HF 交换 100%，$\omega=0.27$，采用 VV10 $b=5.5$、$C=0.01$，并带有三体 D4-ATM 校正，其中 $s_{9}=1.0$、$a_{1}=0.215$、$a_{2}=5.8$
- $\bullet$

**wB97M-V**（$\omega$B97M-V）：12 参数组合优化、色散校正（VV10）泛函，短程 HF 交换 15%，长程 HF 交换 100%，$\omega=0.3$[[905]](../bib_references/bib.md#bib939)
- $\bullet$

wB97MV-D3s(BJ)（$\omega$B97M-D3s(BJ)）：wB97M-V，其中 VV10 NLC 泛函被替换为 DFT-D3s(BJ)（s6 = 1.0, s8 = 0.2641, a1 = 0.0, a2 = 5.4959）
- $\bullet$

wB97MV-D4（$\omega$B97M-D4）：wB97M-V，其中 VV10 NLC 泛函被替换为 DFT-D4（s6 = 1.0, s8 = 0.5093, s9 = 1.0, a1 = 0.0662, a2 = 5.4487）
- $\bullet$

GAS22：基于 $\omega$B97M-V、通过 SyFES 演化得到的范围分离杂化 meta-GGA 泛函[[868]](../bib_references/bib.md#bib904)
- $\bullet$

M06-SX：局域 revM06-L 泛函，短程 HF 交换 33.5%[[1429]](../bib_references/bib.md#bib1490)
- $\bullet$

M11：40 参数泛函，短程 HF 交换 42.8%，长程 HF 交换 100%，$\omega=0.25$[[1084]](../bib_references/bib.md#bib1130)
- $\bullet$

MN12-SX：58 参数非可分离 meta-GGA，短程 HF 交换 25%，长程 HF 交换 0%，$\omega=0.11$[[1088]](../bib_references/bib.md#bib1134)
- $\bullet$

revM11：22 参数泛函，短程 HF 交换 22.5%，长程 HF 交换 100%，$\omega=0.4$[[1401]](../bib_references/bib.md#bib1461)
- $\bullet$

wB97M-rV*（$\omega$B97X-rV）：$\omega$B97M-V 密度泛函，其中 VV10 NLC 泛函被替换为 rVV10 NLC 泛函[[907]](../bib_references/bib.md#bib940)
- $\bullet$

wM05-D（$\omega$M05-D）：21 参数色散校正（DFT-CHG）泛函，短程 HF 交换约 $\approx$ 36.96%，长程 HF 交换 100%，$\omega=0.2$[[833]](../bib_references/bib.md#bib224)
- $\bullet$

wM06-D3（$\omega$M06-D3）：25 参数色散校正 [DFT-D3(0)] 泛函，短程 HF 交换约 $\approx$ 27.15%，长程 HF 交换 100%，$\omega=0.3$[[832]](../bib_references/bib.md#bib225)
- $\circ$

双杂化广义梯度近似（Double Hybrid Generalized Gradient Approximation, DH GGA）

**注意：

若要对 MP2 部分使用分辨率恒等（resolution-of-the-identity）近似，需通过 *$rem* 变量 AUX_BASIS_CORR 指定辅助基组
**

- $\bullet$

**wB97X-2(LP)**（$\omega$B97X-2(LP)）：13 参数泛函，短程 HF 交换约 $\approx$ 67.88%，长程 HF 交换 100%，SS MP2 关联约 $\approx$ 58.16%，OS MP2 关联约 $\approx$ 47.80%，$\omega=0.3$[[225]](../bib_references/bib.md#bib221)
- $\bullet$

**wB97X-2(TQZ)**（$\omega$B97X-2(TQZ)）：13 参数泛函，短程 HF 交换约 $\approx$ 63.62%，长程 HF 交换 100%，SS MP2 关联约 $\approx$ 52.93%，OS MP2 关联约 $\approx$ 44.71%，$\omega=0.3$[[225]](../bib_references/bib.md#bib221)
- $\bullet$

**XYG3**：80.33% HF 交换 - 1.4% Slater LSDA 交换 + 21.07% B88 GGA 交换 + 67.89% LYP GGA 关联 + 32.11% MP2 关联（用 B3LYP 轨道计算）[[1551]](../bib_references/bib.md#bib1610)
- $\bullet$

**XYGJ-OS**：77.31% HF 交换 + 33.93% Slater LSDA 交换 - 23.21% B88 GGA 交换 + 32.68% VWN1RPA LSDA 关联 + 27.54% LYP GGA 关联 + 43.64% OS MP2 关联（用 B3LYP 轨道计算）[[1543]](../bib_references/bib.md#bib1611)
- $\bullet$

**XYG-OS5**：89.28% HF 交换 + 22.69% Slater LSDA 交换 + 23.09% VWN1RPA LSDA 关联 - 6.35% LYP GGA 关联 + 55.74% OS MP2 关联（用 B3LYP 轨道计算）[[1544]](../bib_references/bib.md#bib1616)
- $\bullet$

**wDSD72-PBEP86-D4**（$\omega$DSD72-PBEP86-D4）：0.72 范围分离 HF 交换（$\omega$ = 0.13 bohr${}^{-1}$）+ 0.28 PBE GGA 交换 + 0.3425 P86 GGA 关联 + 0.6904 OS MP2 关联 + 0.1343 SS MP2 关联，配合 DFT-D4（s6 = 0.4685, s8 = 0, s9 = 1.0, a1 = 0.1884, a2 = 5.0101）[[1196]](../bib_references/bib.md#bib949)
- $\bullet$

xDSD75-PBEP86-D4：0.75 HF 交换 + 0.25 PBE GGA 交换 + 0.3517（SCF 循环期间为 1.0）P86 GGA 关联 + 0.6623 OS MP2 关联 + 0.1168 SS MP2 关联，配合 DFT-D4（s6 = 0.4246, s8 = 0, s9 = 1.0, a1 = 0.2828, a2 = 4.7204）[[1196]](../bib_references/bib.md#bib949)
- $\bullet$

revDOD-PBEP86-D4：0.69 HF 交换 + 0.31 PBE GGA 交换 + 0.4301 P86 GGA 关联 + 0.6131 OS MP2 关联，配合 DFT-D4（s6 = 0.6158, s8 = 0, s9 = 1.0, a1 = 0.344, a2 = 4.2427）[[1196]](../bib_references/bib.md#bib949)
- $\bullet$

revDSD-PBEP86-D4：0.69 HF 交换 + 0.31 PBE GGA 交换 + 0.4224 P86 GGA 关联 + 0.5935 OS MP2 关联 + 0.0566 SS MP2 关联，配合 DFT-D4（s6 = 0.5917, s8 = 0, s9 = 1.0, a1 = 0.371, a2 = 4.2014）[[1196]](../bib_references/bib.md#bib949)
- $\bullet$

DSD-PBEPBE-D3：68% HF 交换 + 32% PBE GGA 交换 + 49% PBE GGA 关联 + 13% SS MP2 关联 + 55% OS MP2 关联，带 DFT-D3(BJ) 尾部项[[715]](../bib_references/bib.md#bib747)
- $\bullet$

DSD-PBEP86-D3：69% HF 交换 + 31% PBE GGA 交换 + 44% P86 GGA 关联 + 22% SS MP2 关联 + 52% OS MP2 关联，带 DFT-D3(BJ) 尾部项[[715]](../bib_references/bib.md#bib747)
- $\bullet$

B2-PLYP：53% HF 交换 + 47% B88 GGA 交换 + 73% LYP GGA 关联 + 27% MP2 关联[[493]](../bib_references/bib.md#bib501)
- $\bullet$

B2NC-PLYP：0.81 HF 交换 + 0.19 B88 GGA 交换 + 0.45 LYP GGA 关联 + 0.55 MP2 关联[[1531]](../bib_references/bib.md#bib1595)
- $\bullet$

mPW2-PLYP：0.55 HF 交换 + 0.45 mPW GGA 交换 + 0.75 LYP GGA 关联 + 0.25 MP2 关联[[1219]](../bib_references/bib.md#bib503)
- $\bullet$

mPW2NC-PLYP：0.67 HF 交换 + 0.33 mPW GGA 交换 + 0.51 LYP GGA 关联 + 0.49 MP2 关联[[1531]](../bib_references/bib.md#bib1595)
- $\bullet$

B2GP-PLYP：65% HF 交换 + 35% B88 GGA 交换 + 64% LYP GGA 关联 + 36% MP2 关联[[669]](../bib_references/bib.md#bib694)
- $\bullet$

LS1DH-PBE：75% HF 交换 + 25% PBE GGA 交换 + 57.8125% PBE GGA 关联 + 42.1875% MP2 关联[[1367]](../bib_references/bib.md#bib1427)
- $\bullet$

PBE-QIDH：69.3361% HF 交换 + 30.6639% PBE GGA 交换 + 66.6667% PBE GGA 关联 + 33.3333% MP2 关联[[158]](../bib_references/bib.md#bib151)
- $\bullet$

PBE0-2：$\approx$ 79.37% HF 交换 + $\approx$ 20.63% PBE GGA 交换 + 50% PBE GGA 关联 + 50% MP2 关联[[226]](../bib_references/bib.md#bib223)
- $\bullet$

PBE0-DH：50% HF 交换 + 50% PBE GGA 交换 + 87.5% PBE GGA 关联 + 12.5% MP2 关联[[157]](../bib_references/bib.md#bib150)
- $\bullet$

SOS0-PBE0-2：0.79 HF 交换 + 0.21 PBE GGA 交换 + 0.5 PBE GGA 关联 + 0.66667 OS MP2 关联
- $\circ$

双杂化元广义梯度近似（Double Hybrid Meta-Generalized Gradient Approximation, DH MGGA）

- $\bullet$

**wB97M(2)**：14 参数泛函形式，包含基于 $\omega$B97M-V 轨道的 MP2 关联[[906]](../bib_references/bib.md#bib941)
- $\bullet$

**wB97M(OS)**：13 参数泛函形式，包含基于 $\omega$B97M-V 轨道的自旋相反（opposite-spin）缩放 MP2 关联
- $\bullet$

**PTPSS-D3**：50% HF 交换 + 50% Re-Fit TPSS meta-GGA 交换 + 62.5% Re-Fit TPSS meta-GGA 关联 + 37.5% OS MP2 关联，带 DFT-D3(0) 尾部项[[463]](../bib_references/bib.md#bib476)
- $\bullet$

Pr2SCAN69-D4：0.69 HF 交换 + 0.31 r2SCAN meta-GGA 交换 + 0.56 r2SCAN meta-GGA 关联 + 0.592593 OS MP2 关联，配合 DFT-D4（s6 = 0.7167, s8 = 0, s9 = 1.0, a1 = 0.4644, a2 = 5.2563）[[1483]](../bib_references/bib.md#bib167)
- $\bullet$

Pr2SCAN50-D4：0.5 HF 交换 + 0.5 r2SCAN meta-GGA 交换 + 0.75 r2SCAN meta-GGA 关联 + 0.333333 OS MP2 关联，配合 DFT-D4（s6 = 0.7964, s8 = 0.3421, s9 = 1.0, a1 = 0.4663, a2 = 5.7916）[[1483]](../bib_references/bib.md#bib167)
- $\bullet$

wPr2SCAN50-D4（$\omega$Pr2SCAN50-D4）：0.5 范围分离 HF 交换（$\omega$ = 0.214 bohr${}^{-1}$）+ 0.5 r2SCAN meta-GGA 交换 + 0.65 r2SCAN meta-GGA 关联 + 0.46667 OS MP2 关联，配合 DFT-D4（s6 = 0.8143, s8 = 0.3842, s9 = 1.0, a1 = 0.4135, a2 = 5.8773）[[1483]](../bib_references/bib.md#bib167)
- $\bullet$

DSD-PBEB95-D3：66% HF 交换 + 34% PBE GGA 交换 + 55% B95 GGA 关联 + 9% SS MP2 关联 + 46% OS MP2 关联，带 DFT-D3(BJ) 尾部项[[715]](../bib_references/bib.md#bib747)
- $\bullet$

PWPB95-D3：50% HF 交换 + 50% Re-Fit PW91 GGA 交换 + 73.1% Re-Fit B95 meta-GGA 关联 + 26.9% OS MP2 关联，带 DFT-D3(0) 尾部项[[463]](../bib_references/bib.md#bib476)
