---
title: "5.6.2 半经验 RSH 泛函"
---

## 5.6.2 半经验 RSH 泛函

（2026 年 7 月 4 日）

半经验 RSH 泛函包括 Chai 和 Head-Gordon 开发的 $\omega$B97、$\omega$B97X 和 $\omega$B97X-D 泛函[[223]](../bib_references/bib.md#bib218)；Mardirossian 和 Head-Gordon 开发的 $\omega$B97X-V 与 $\omega$B97M-V[[903]](../bib_references/bib.md#bib937)；Peverati 和 Truhlar 开发的 M11[[1084]](../bib_references/bib.md#bib1130)；Chai 及其合作者开发的 $\omega$B97X-D3、$\omega$M05-D 和 $\omega$M06-D3[[833]](../bib_references/bib.md#bib224)；以及 Truhlar 及其合作者开发的屏蔽交换（screened exchange）泛函 N12-SX 和 MN12-SX[[1088]](../bib_references/bib.md#bib1134)。对于这些泛函，其程分离（range-separation）参数应视为固定值。近年来，Mardirossian 和 Head-Gordon 通过组合筛选方法开发了两种 RSH 泛函 $\omega$B97X-V 和 $\omega$B97M-V，前者在超过 100,000 个候选泛函中进行筛选，后者则筛选了超过 100 亿个候选泛函。这两种泛函均使用了 VV10 非局域相关泛函，以改善对非共价相互作用和异构化能量的描述。$\omega$B97M-V 是一个含 12 个参数的 meta-GGA（元广义梯度近似）泛函，短程精确交换比例为 15%，长程精确交换比例为 100%，在"雅各布阶梯"（Jacob's Ladder）第 4 层（rung 4）所提供的泛函中，它是面向各类应用最为精确的泛函之一。这一结论已通过基准测试得到验证：将该泛函在近 5000 个数据点上与 **Q-Chem** 中可用的 200 余种其他泛函进行了对比。[[905]](../bib_references/bib.md#bib939)
