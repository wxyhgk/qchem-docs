---
title: "5.3.2 推荐的密度泛函"
---

## 5.3.2 推荐的密度泛函

（2026 年 7 月 4 日）

**Q-Chem** 包含超过 150 种交换-关联泛函（exchange-correlation functional），这还不包括那些可以直接附加色散校正（dispersion correction）的泛函（例如 B3LYP-D3）。因此，我们从"雅各布阶梯（Jacob's Ladder）"的第二至第四层中推荐几种泛函，以指导泛函的选择。这些推荐大多来自一项基准测试，该测试在涵盖非共价相互作用、异构化能、热化学和势垒高度的近 5000 个数据点的大型数据库上，对 200 多种密度泛函进行了评估。**每个类别中唯一推荐的方法以粗体标示。**

对于第 2 层的广义梯度近似（Generalized Gradient Approximation, GGA），我们推荐：

- **B97-D3(BJ)**：METHOD = B97-D3 且 DFT_D = D3_BJ
- revPBE-D3(BJ)：METHOD = revPBE 且 DFT_D = D3_BJ
- BLYP-D3(BJ)：METHOD = BLYP 且 DFT_D = D3_BJ
- PBE：METHOD = PBE

对于第 3 层的 meta-GGA，我们推荐：

- **B97M-rV**：METHOD = B97M-rV
- MS1-D3(0)：METHOD = MGGA_MS1 且 DFT_D = D3_ZERO
- MS2-D3(0)：METHOD = MGGA_MS2 且 DFT_D = D3_ZERO
- M06-L-D3(0)：METHOD = M06-L 且 DFT_D = D3_ZERO
- TPSS-D3(BJ)：METHOD = TPSS 且 DFT_D = D3_BJ

对于第 4 层的混合 GGA（hybrid GGA），我们推荐：

- $\omega$**B97X-V**：METHOD = wB97X-V
- $\omega$B97X-D3S(BJ)：METHOD = wB97X-D3S(BJ)
- $\omega$B97X-D：METHOD = wB97X-D
- B3LYP-D3(BJ)：METHOD = B3LYP 且 DFT_D = D3_BJ
- revPBE0-D3(BJ)：METHOD = revPBE0 且 DFT_D = D3_BJ

对于第 4 层的混合 meta-GGA，我们推荐：

- **COACH**：METHOD = COACH
- $\omega$**B97M-V**：METHOD = wB97M-V
- CF22D：METHOD = CF22D
- M06-2X-D3(0)：METHOD = M06-2X 且 DFT_D = D3_ZERO
- TPSSh-D3(BJ)：METHOD = TPSSh 且 DFT_D = D3_BJ

对于第 5 层的双杂化 GGA（double-hybrid GGA），我们推荐：

- $\omega$**B97X-2(LP)**：METHOD = wB97X-2(LP)
- $\omega$**B97X-2(TQZ)**：METHOD = wB97X-2(TQZ)
- **DSD-PBEPBE-D3**：METHOD = DSD-PBEPBE-D3
- **revDSD-PBEP86-D4**：METHOD = revDSD-PBEP86-D4

对于第 5 层的双杂化 meta-GGA，我们推荐：

- $\omega$**B97M-(2)**：METHOD = wB97M-(2)
- **PTPSS-D3**：METHOD = PTPSS-D3
