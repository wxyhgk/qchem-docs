---
title: "4.6.3 线性标度交换（LinK）矩阵计算"
---

## 4.6.3 线性标度交换（LinK）矩阵计算

(July 4, 2026)

Hartree-Fock 计算以及流行的杂化密度泛函（例如 B3LYP）同样需要双电子积分来评估与单个行列式相关的交换能。交换能不存在有用的多极展开，因为双电子积分的bra（左矢）和ket（右矢）通过密度矩阵相耦合，而密度矩阵承载了交换效应。幸运的是，对于存在 HOMO/LUMO 间隙（gap）的体系，密度矩阵元随距离呈指数衰减。[[1221]](../bib_references/bib.md#bib1278)
绝缘性越好，电子结构越定域，指数衰减速率就越快。因此，对于绝缘体而言，对交换能有数值显著性的贡献仅有线性数量个。通过智能化的数值阈值设置，可以以线性标度的计算代价严格地求解交换矩阵。为此，**Q-Chem** 内置了线性标度 K（LinK）方法[[1011]](../bib_references/bib.md#bib1049)
，用于以线性标度代价计算交换能及其梯度[[1012]](../bib_references/bib.md#bib1050)
（前提是密度矩阵高度稀疏）。在小分子极限下，LinK 方法实质上退化为常规的、用于交换项的直接自洽场（direct SCF）方法（不引入显著额外开销），而对于密度矩阵确实高度稀疏的（极）大体系，则可获得大幅加速。完整细节请参阅原始论文。[[1011]](../bib_references/bib.md#bib1049)
可以通过以下选项显式请求使用 LinK（尽管当程序认为其为更优算法时，**Q-Chem** 会自动开启该选项）。

LIN_K

### `LIN_K`

> **控制是否使用精确交换（exact exchange）的线性标度计算（LinK）。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`由程序决定，当使用 CFMM 时即开启 LinK。`
> * **可选值**：
>     * TRUE
>     * 使用 LinK
>     * FALSE
>     * 不使用 LinK
> * **建议**：用于含有大量原子的 HF 和杂化密度泛函理论（DFT）计算。

???+ example "示例 4.19: 大型单点能计算的 Q-Chem 输入。当请求使用 LinK 时，CFMM 会被自动开启。"
    ```qchem
    $comment
       HF/3-21G single point calculation on a large molecule
       read in the molecular coordinates from file
    $end
    
    $molecule
       read base_pair.inp
    $end
    
    $rem
       METHOD     HF      Hartree-Fock
       BASIS      sto-3g  Basis set
       LIN_K      TRUE    Calculate K using LinK
    $end
    ```
