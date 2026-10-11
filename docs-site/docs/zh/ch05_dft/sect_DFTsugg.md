---
title: "5.3.2 Suggested Density Functionals"
---

## 5.3.2 Suggested Density Functionals

(July 4, 2026)

**Q-Chem** contains over 150 exchange-correlation functionals, not counting those
that can be straightforwardly appended with a dispersion correction (such as
B3LYP-D3). Therefore, we suggest a few functionals from the second through
fourth rungs of Jacob’s Ladder in order to guide functional selection. Most of
these suggestions come from a benchmark of over 200 density functionals on a
vast database of nearly 5000 data points, covering non-covalent interactions,
isomerization energies, thermochemistry, and barrier heights. **The
single recommended method from each category is indicated in bold.**

From the GGAs on Rung 2, we recommend:

- •

**B97-D3(BJ)**: METHOD = B97-D3 and DFT_D = D3_BJ
- •

revPBE-D3(BJ): METHOD = revPBE and DFT_D = D3_BJ
- •

BLYP-D3(BJ): METHOD = BLYP and DFT_D = D3_BJ
- •

PBE: METHOD = PBE

From the meta-GGAs on Rung 3, we recommend:

- •

**B97M-rV**: METHOD = B97M-rV
- •

MS1-D3(0): METHOD = MGGA_MS1 and DFT_D = D3_ZERO
- •

MS2-D3(0): METHOD = MGGA_MS2 and DFT_D = D3_ZERO
- •

M06-L-D3(0): METHOD = M06-L and DFT_D = D3_ZERO
- •

TPSS-D3(BJ): METHOD = TPSS and DFT_D = D3_BJ

From the hybrid GGAs on Rung 4, we recommend:

- •

$\omega$**B97X-V**: METHOD = wB97X-V
- •

$\omega$B97X-D3S(BJ): METHOD = wB97X-D3S(BJ)
- •

$\omega$B97X-D: METHOD = wB97X-D
- •

B3LYP-D3(BJ): METHOD = B3LYP and DFT_D = D3_BJ
- •

revPBE0-D3(BJ): METHOD = revPBE0 and DFT_D = D3_BJ

From the hybrid meta-GGAs on Rung 4, we recommend:

- •

**COACH**: METHOD = COACH
- •

$\omega$**B97M-V**: METHOD = wB97M-V
- •

CF22D: METHOD = CF22D
- •

M06-2X-D3(0): METHOD = M06-2X and DFT_D = D3_ZERO
- •

TPSSh-D3(BJ): METHOD = TPSSh and DFT_D = D3_BJ

From the double-hybrid GGAs on Rung 5, we recommend:

- •

$\omega$**B97X-2(LP)**: METHOD = wB97X-2(LP)
- •

$\omega$**B97X-2(TQZ)**: METHOD = wB97X-2(TQZ)
- •

**DSD-PBEPBE-D3**: METHOD = DSD-PBEPBE-D3
- •

**revDSD-PBEP86-D4**: METHOD = revDSD-PBEP86-D4

From the double-hybrid mGGAs on Rung 5, we recommend:

- •

$\omega$**B97M-(2)**: METHOD = wB97M-(2)
- •

**PTPSS-D3**: METHOD = PTPSS-D3
