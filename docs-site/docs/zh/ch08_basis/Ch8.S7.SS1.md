---
title: "8.7.1 概述"
---

## 8.7.1 概述

(July 4, 2026)

用于描述亚稳电子态（meta-stable electronic states）的复基函数（Complex Basis Function, CBF）方法（参见第 [4.9.5](../ch04_scf/sec_cbfscf.md) 节）要求用户指定一个基组（Basis Set），其中最为弥散的函数具有复标度（complex-scaled）指数。实值基函数通过 *$rem* 关键字 BASIS 指定。复基组（complex basis set）通过 *$rem* 关键字 COMPLEX_BASIS 指定，且它应当是实基组的超集。
若基组被指定为 general 或 mixed 类型，则用户自定义的基组应以与 *$basis* 区段相同的格式录入到一个额外的 *$zbasis* 输入区段中。

**Q-Chem** 会自动确定复基组中新增的基函数，并对这些函数的指数进行标度。例如，若 BASIS 指定为 "cc-pVTZ" 而 COMPLEX_BASIS 指定为 "aug-cc-pVTZ"，则这些增弥散（augmenting）函数将具有复标度指数。指定被标度函数的另一种方式是使用 *$complex_ccman* 区段中的 scaling 变量。如果希望标度与 BASIS 无关，该变量接受一个以逗号分隔的、待标度壳层（shell）索引列表。这要求将 COMPLEX_CCMAN 变量设置为 1，以便识别该 scaling 字符串。这些索引指的是各壳层在基组文件中、或分别在 *$zbasis* 区段中出现的顺序。此外，在存在多个中心的情况下，不同中心上的基函数会被分别编号，编号顺序与中心在 *$molecule* 区段中列出的顺序一致，这使得即使位于同类原子上、中心不同的基函数也可以采用不同的标度。举例来说，在某含有两个原子的计算中，若每个原子各有 10 个壳层，则第一个原子的壳层被赋予索引 1–10，第二个原子的壳层被赋予索引 11–20。下面给出的 *$complex_ccman* 区段即为一个示例，其中请求对壳层 5、6、15 和 16 进行标度。

> ```qchem
> $rem
> ...
> complex_ccman 1
> ...
> $end
> 
> $complex_ccman
>    CS_THETA  0
>    CS_ALPHA  1000
>    scaling 5,6,15,16
> $end
> ```

标度按照如下规则进行

<a id="Ch8.E1"></a>

$$
\alpha\rightarrow\alpha e^{-2i\theta} \tag{8.1}
$$

其中 $\alpha$ 是某个基函数的指数，$\theta$ 由 *$rem* 关键字 COMPLEX_THETA 指定。

COMPLEX_BASIS

### `COMPLEX_BASIS`

> **定义复基组。**
>
> * **类型**：`STRING`
> * **默认值**：`无默认复基组`
> * **可选值**：
>     * Symbol
>     * 使用标准基组
>     * ZBASIS_GENERAL, ZBASIS_GEN
>     * 用户自定义。与
>     * BASIS 相同
>     * ZBASIS_MIXED
>     * 用户自定义混合基组
> * **建议**：参阅文献 1457 White A. F., Head-Gordon M., McCurdy C. W. J. Chem. Phys. (2015) , 142 , pp. 054103 . Link 以及 Basis Set Exchange（基组交换库）。

COMPLEX_THETA

### `COMPLEX_THETA`

> **设置使用复基函数计算中 $\theta$ 的值（单位为度）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $n$
>     * $\theta=n/10$
>     * （度）
> * **建议**：参阅文献 1457 White A. F., Head-Gordon M., McCurdy C. W. J. Chem. Phys. (2015) , 142 , pp. 054103 . Link 。通常应在若干不同的 $\theta$ 值下进行计算（即一条 " $\theta$ -trajectory"，$\theta$ 轨迹）。
