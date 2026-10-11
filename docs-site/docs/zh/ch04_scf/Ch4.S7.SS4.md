---
title: "4.7.4 基组配对"
---

## 4.7.4 基组配对

(2026 年 7 月 4 日)

我们建议使用小基组为目标基组真子集的基组配对（例如 6-31G 配对 6-31G*）。这类配对不仅能产生更精确的结果，而且在能量和梯度的计算中都能实现更高效的积分筛选。针对许多标准基组（包括 Dunning 型的 cc-pV$X$Z 基组及其增广变体）已经开发并充分测试了相应的子集。配对方案汇总于表 [4.2](#tab:DBsummary)；这些截断方案的详细信息见图 [4.1](#fig:DBfig)。

针对 6-31G* 型计算还有一种新的配对方案。6-4G 子集（在 **Q-Chem** 中命名为 r64G）是按*原始（primitive）*函数取子集得到的，为该基组区间提供了一个更小、更快的替代选择。[[1302]](../bib_references/bib.md#bib1357)
投影代码中（仍为 OVPROJECTION）一个依具体情况而定的开关可以正确处理 6-4G。
对于 DB-HF，计算按上文所述进行。
对于 DB-DFT，需对双基组（dual-basis）校正施加经验缩放因子（详见文献 [[1302]](../bib_references/bib.md#bib1357)）。
该缩放由代码自动处理并相应输出。

自 **Q-Chem** 3.2 版起，基组投影代码还经过改造以正确处理线性相关性问题，[[1299]](../bib_references/bib.md#bib1358)
 而线性相关性在大型增广基组（aug-cc-pVTZ，*等等*）计算中常常会带来麻烦。
投影代码中使用相同的标准关键字 LIN_DEP_THRESH 来判定线性相关性。
由于处理线性相关性的方案所限，现在仅允许真子集配对。

与单基组计算一样，用户指定的通用基组（general）或混合基组（mixed basis set）也可用于双基组计算（见第 [8](../ch08_basis/chap_basis.md) 章）。
目标基组在标准的 *$basis* 区块中指定。
较小的次基组放在类似的 *$basis*2 区块中；该区块内的语法与 *$basis* 的语法相同。
通用与混合小基组分别通过 BASIS2 = BASIS2_GEN 和
BASIS2 = BASIS2_MIXED 启用。

| BASIS | BASIS2 |
| --- | --- |
| cc-pVTZ | rcc-pVTZ |
| cc-pVQZ | rcc-pVQZ |
| aug-cc-pVDZ | racc-pVDZ |
| aug-cc-pVTZ | racc-pVTZ |
| aug-cc-pVQZ | racc-pVQZ |
| 6-31G* | r64G, 6-31G |
| 6-31G** | r64G, 6-31G |
| 6-31++G** | 6-31G* |
| 6-311++G(3df,3pd) | 6-311G*, 6-311+G* |

表 4.2: 推荐的双基组配对汇总与命名

<a id="Ch4.Ex5"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&-\\
&-\\
s\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d\\
&p\\
s\\
\end{array}\\
&$cc-pVTZ$&$rcc-pVTZ$&&$cc-pVTZ$&$rcc-pVTZ$\\
\end{array}\\
$$

<a id="Ch4.Ex6"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&-\\
s&&-\\
&p&&-\\
s&&-\\
&-\\
s\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d&&g\\
&p&&f\\
s&&d\\
&p\\
s\\
\end{array}&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&d\\
&p\\
s\\
\end{array}\\
&$cc-pVQZ$&$rcc-pVQZ$&&$cc-pVQZ$&$rcc-pVQZ$\\
\end{array}\\
$$

<a id="Ch4.Ex7"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&\\
&p\\
s^{\prime}&\\
\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&\\
&-\\
s^{\prime}&\\
\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVDZ$&$racc-pVDZ$&&$aug-cc-pVDZ$&$racc-pVDZ$\\
\end{array}\\
$$

<a id="Ch4.Ex8"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&d\\
&p\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccc}s\\
&p\\
s&&-\\
&p\\
s&&-\\
&-\\
s^{\prime}\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d\\
&p&&-\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVTZ$&$racc-pVTZ$&&$aug-cc-pVTZ$&$racc-pVTZ$\\
\end{array}\\
$$

<a id="Ch4.Ex9"></a>
$$
\begin{array}[]{cccccc}$H-He:$&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{cccc}s\\
&p\\
s&&-\\
&p&&-\\
s&&-\\
&p&&-\\
s&&-\\
&-\\
s^{\prime}\end{array}&$Li-Ne:$&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&f\\
s&&d&&g\\
&p&&f\\
s&&d&&g^{\prime}\\
&p&&f^{\prime}\\
s&&d^{\prime}\\
&p^{\prime}\\
s^{\prime}\end{array}&\scriptsize\begin{array}[]{ccccc}s\\
&p\\
s&&d\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&d&&-\\
&p&&-\\
s&&-\\
&p^{\prime}\\
s^{\prime}\end{array}\\
&$aug-cc-pVQZ$&$racc-pVQZ$&&$aug-cc-pVQZ$&$racc-pVQZ$\\
\end{array}
$$

图 4.1: cc-pV(T,Q)Z 与 aug-cc-pV(D,T,Q)Z 截断基组配对的结构。最紧凑的函数列于顶部。
带撇号的函数表示弥散函数增广。破折号表示相对于配对的标准基组所删除的函数。
每一组均展示了氢与重原子的截断方式，以及在 **Q-Chem** 中使用的命名。
