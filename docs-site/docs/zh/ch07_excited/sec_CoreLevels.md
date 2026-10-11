---
title: "7.12 核电离能与核激发态"
---

# 7.12 核电离能与核激发态

(July 4, 2026)

Q-Chem 5.2 中的核能级光谱学 —— 由南加州大学 Anna Krylov 教授主讲

在使用高能辐射的实验（如 X 射线光谱学、EXAFS、NEXAFS、XAS、XES、RIXS、REXS 等）中，核电子可以被电离或激发到低能虚轨道。在 **Q-Chem** 中计算核电子的电离能或激发能有多种途径。由于核能级态具有极高的能量且嵌入电离连续态中，即它们属于 Feshbach 共振[[1193]](../bib_references/bib.md#bib1248)，因此需要对常规的激发态和电离态方法进行改进才能处理这类核能级态。

- [7.12.1 核激发态的多体方法](ex_InvCore.md)

- [7.12.2 基于含时密度泛函理论（TDDFT）的 X 射线光谱计算](subsec_TDDFT-Xray.md)

- [7.12.3 基于 Kohn-Sham 本征值的计算方法](Ch7.S12.SS3.md)

- [7.12.4 基于约束开壳层 Kohn-Sham（ROKS）的核激发计算](ex_COCOREIP.md)
