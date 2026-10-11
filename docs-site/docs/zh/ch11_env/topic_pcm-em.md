---
title: "11.2.3 极化连续介质模型"
---

## 11.2.3 极化连续介质模型（Polarizable Continuum Models, PCM）

（2026 年 7 月 4 日）

多极展开模型（multipolar expansion model）基于球形空腔中点多极子溶和能的精确公式[[948]](../bib_references/bib.md#bib988)，
除了（甚或恰恰）对于小分子而言，这是一种相当粗略的近似；而 Kirkwood-Onsager 模型在很大程度上已被更广义的"表观表面电荷"（apparent surface charge）自洽反应场（SCRF）溶化模型所取代，这类模型通常被称为 PCM[[1363]](../bib_references/bib.md#bib1425)。
这些模型从两个方面改进了多极展开方法。最重要的是，它们对分子形状给出了远为真实的描述，
通常是通过由原子中心球的并集来构造"溶质空腔"（*即*，原子尺度区域与介电连续体之间的界面），模型的这一方面将在第 [11.2.3.2](#subsubsec:pcm_cavity) 节中讨论。此外，
用于使连续体极化的是溶质的精确电子密度（而非多极展开）。溶质与连续体之间的静电相互作用
表现为空腔表面上的诱导电荷密度，在实际计算中该诱导电荷密度被离散化为点电荷。
表面电荷由溶质在空腔表面的静电势决定，因此表面电荷与溶质波函数必须自洽地共同确定。

## 11.2.3.1 形式理论及不同模型的讨论

PCM 的文献历史悠久[[1363]](../bib_references/bib.md#bib1425)，
目前广泛使用的有多种不同模型；这些模型之间的联系并不总是为人所重视[[245]](../bib_references/bib.md#bib245)。

Chipman[[245]](../bib_references/bib.md#bib245)
展示了如何将各种 PCM 表述在一个统一的理论框架之内；综述可参见
文献 [[569]](../bib_references/bib.md#bib580)。
PCM 表现为一组线性方程，

<a id="eq:Kq=Rv"></a>
$$
\mathbf{Kq}=\mathbf{Rv}\;, \tag{11.2}
$$

其中，空腔离散化点处的诱导电荷 $q_{i}$（在式 ([11.2](#eq:Kq=Rv)) 中组织为向量 $\mathbf{q}$）
由溶质在这些相同离散化点处的静电势值 $v_{i}$ 计算得到。矩阵 $\mathbf{K}$ 和 $\mathbf{R}$
的形式取决于所采用的具体 PCM。对于 **Q-Chem** 中可用的各 PCM，这些矩阵已列于
表 [11.3](#table:K-matrix) 中。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">模型</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">文献</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">矩阵</span> $\mathbf{K}$
</td>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">矩阵</span> $\mathbf{R}$
</td>
<td class="ltx_td ltx_align_center ltx_border_tt">
<span class="ltx_text ltx_font_bold">标量</span> $f_{\varepsilon}$
</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row"><span class="ltx_text ltx_font_bold">参考文献</span></th>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">COSMO${}^{a}$
</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_t"><cite class="ltx_cite ltx_citemacro">
</cite>
</th>
<td class="ltx_td ltx_align_center ltx_border_t">$\mathbf{S}$</td>
<td class="ltx_td ltx_align_center ltx_border_t">$-f_{\varepsilon}\mathbf{1}$</td>
<td class="ltx_td ltx_align_center ltx_border_t">$(\varepsilon-1)/(\varepsilon+1/2)$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">C-PCM</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[1375]](../bib_references/bib.md#bib1436)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\mathbf{1}$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/\varepsilon$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">IEF-PCM</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[245]](../bib_references/bib.md#bib245)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}-(f_{\varepsilon}/2\pi)\mathbf{DAS}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\left(\mathbf{1}-\frac{1}{2\pi}\mathbf{DA}\right)$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/(\varepsilon+1)$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">SS(V)PE</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">[[245]](../bib_references/bib.md#bib245)
</th>
<td class="ltx_td ltx_align_center">$\mathbf{S}-(f_{\varepsilon}/4\pi)\bigl{(}\mathbf{DAS}+\mathbf{SAD}^{\dagger}\bigr{)}$</td>
<td class="ltx_td ltx_align_center">$-f_{\varepsilon}\left(\mathbf{1}-\frac{1}{2\pi}\mathbf{DA}\right)$</td>
<td class="ltx_td ltx_align_center">$(\varepsilon-1)/(\varepsilon+1)$</td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="5">
${}^{a}$<span class="ltx_text" style="font-size:80%;">该模型还包含电荷重整化（charge renormalization）校正；参见第&nbsp;<a class="ltx_ref" href="subsec_COSMO-Klamt.html" title="11.2.8 COSMO ‣ 11.2 Chemical Solvent Models ‣ Chapter 11 Molecules in Complex Environments: Solvent Models, QM/MM, QM/EFP, and Embedding Methods ‣ Q-Chem 7.0 User’s Manual"><span class="ltx_text ltx_ref_tag">11.2.8</span></a>&nbsp;节。</span>
</th>
</tr>
</tfoot>
</table>

表 11.3： 
对于 **Q-Chem** 中可用的各种 PCM，式 ([11.2](#eq:Kq=Rv)) 中各矩阵的定义。
矩阵 $\mathbf{S}$ 由空腔电荷之间的库仑相互作用构成，$\mathbf{D}$ 则是
产生外法向电场矢量的矩阵的离散化形式。（详细定义参见
文献 [[246]](../bib_references/bib.md#bib246)。）
矩阵 $\mathbf{A}$ 为对角矩阵，其元素为空腔离散化面元的表面积，$\mathbf{1}$ 为单位矩阵。

最古老的 PCM 是所谓 Tomasi 及其合作者提出的 D-PCM 模型[[946]](../bib_references/bib.md#bib986)，
但与表 [11.3](#table:K-matrix) 中列出的模型不同，D-PCM 需要显式地计算垂直于
空腔表面的电场。这是不可取的，因为与静电势的计算相比，电场的计算既更昂贵又
更容易出现数值问题。此外，在式 ([11.2](#eq:Kq=Rv))
所给出的离散化积分方程层面，对电场的依赖关系可以在形式上被消除[[245]](../bib_references/bib.md#bib245)。
因此，D-PCM 基本上已经过时，**Q-Chem** 中提供的 PCM 只需要计算静电势，而不需要计算电场。

至今仍被广泛使用的最简单的 PCM 是类导体模型 C-PCM[[79]](../bib_references/bib.md#bib61)。
该模型最初由 Klamt 和 Schüürmann 基于导体极限（$\varepsilon\rightarrow\infty$）的论证推导得出，

也可以作为对更形式上正确的模型的近似而推导出来[[244]](../bib_references/bib.md#bib244)。

多年来，出现在该模型中的介电依赖因子（见表 [11.3](#table:K-matrix)）

<a id="eq:f_epsilon"></a>
$$
f_{\varepsilon}=\frac{\varepsilon-1}{\varepsilon+x} \tag{11.3}
$$

曾被取不同的 $x$ 值使用。C-PCM 计算中通常取 $x=0$，而 COSMO 计算中取 $x=1/2$，
不过 Klamt 及其合作者后来建议对中性溶质取 $x=1/2$、对离子取 $x=0$[[694]](../bib_references/bib.md#bib726)。

$f_{\varepsilon}$ 的具体选择可通过 *$pcm* 输入段来控制，其说明见第 [11.2.4](subsec_PCM_job_control.md) 节。

从表 [11.3](#table:K-matrix) 来看，C-PCM 和 COSMO 方法除了表面电荷的轻微
重标定（*即*，取决于 $f_{\varepsilon}$ 的精确选择）之外似乎是相同的，但在历史上，
"Klamt"所使用的术语"COSMO"指的是该模型的一种特殊的"双空腔"（dual-cavity）实现方式，
这使其有别于其他 PCM[[569]](../bib_references/bib.md#bib580)。
这一构造等价于第 [11.2.8](subsec_COSMO-Klamt.md) 节中讨论的"外溢电荷校正"
（outlying charge correction），其目的是考虑溶质电荷密度穿透到空腔表面之外的尾部效应[[692]](../bib_references/bib.md#bib721)。

随后的工作对这一校正的理论依据提出了相当大的怀疑，因为已经证明 C-PCM/COSMO 的
*假设*（ansatz）已经*隐含*了对外溢电荷的校正[[244]](../bib_references/bib.md#bib244)。

关于这一构造以及 COSMO 的进一步讨论将留待第 [11.2.8](subsec_COSMO-Klamt.md) 节。

与 C-PCM 相比，"静电表面与体积极化模拟"（surface and simulation of volume polarization
for electrostatics, SS(V)PE）方法[[245]](../bib_references/bib.md#bib245)
对连续介质静电相互作用给出了更精细的处理。形式上讲，
该模型对*表面极化*（*即*，由包含在溶质空腔内部的溶质电荷所诱导的表面电荷，
由于空腔边界处介电常数的不连续变化而产生的表面极化）给出了精确处理，
同时对*体积极化*（由前述外溢电荷引起）给出了近似处理。"SS(V)PE"这一术语
是 Chipman 的记法[[245]](../bib_references/bib.md#bib245)，
但该模型在积分方程层面与 Cancès *et al.* 最初发展的
"积分方程形式体系"（integral equation formalism, IEF-PCM）在形式上是等价的[[187]](../bib_references/bib.md#bib181)。

当积分方程被离散化为有限维矩阵方程时确实会出现一些差异[[756]](../bib_references/bib.md#bib789)，
并且应从表 [11.3](#table:K-matrix) 中注意到，与 IEF-PCM 相比，SS(V)PE 使用了
$\mathbf{K}$ 矩阵的对称化形式。*非对称*形式的 IEF-PCM 是推荐的方法[[756]](../bib_references/bib.md#bib789)，
尽管在第 [11.2.6](subsec_SS_V_PE.md) 节讨论的 SS(V)PE 等密度（isodensity）实现中只提供对称化版本。
话虽如此，对称版本与非对称版本之间的差异只在范德华空腔表面的情况下才重要；对于
等密度空腔构造而言，这种差异并不显著[[569]](../bib_references/bib.md#bib580)。

与已过时的 D-PCM 方法一样，IEF-PCM 的原始版本显式地要求在空腔表面计算
法向电场，但后来证明这种依赖可以被消除，从而得到表 [11.3](#table:K-matrix)
中描述的版本[[245]](../bib_references/bib.md#bib245)。该版本
只需要静电势，因此更受青睐，我们将此版本记为 IEF-PCM。C-PCM 模型在极限
$\varepsilon\rightarrow\infty$ 下等价于 SS(V)PE[[245]](../bib_references/bib.md#bib245)，
这意味着 C-PCM 必定以某种方式包含了体积极化的*隐含*校正，即使这并非出于设计[[692]](../bib_references/bib.md#bib721)。
对于 $\varepsilon\gtrsim 50$，数值计算表明 SS(V)PE 与 C-PCM 的结果之间基本上没有差异[[756]](../bib_references/bib.md#bib789)。

由于 C-PCM 的计算量比 SS(V)PE 小，它是高介电常数溶剂中 PCM 的首选。
相对于 SS(V)PE 节省的计算量对于大型 QM/MM/PCM 计算任务可能尤为显著。

关于这些模型历史的更详细讨论，参见 Tomasi *et al.* 撰写的篇幅冗长而全面的综述[[1363]](../bib_references/bib.md#bib1425)。
关于这些模型之间联系的简要讨论，参见文献 [[246]](../bib_references/bib.md#bib246)。

## 11.2.3.2 空腔构造与离散化

![图 11.1：PCM 所用各种溶质空腔表面定义的示意图。
751 Lange A. W. et al. Mol. Phys. (2020) , 118 , pp. e1644384 . Link 原子范德华球的并集（以灰色显示）
定义了范德华（vdW）表面（以黑色显示）。请注意，在构造 vdW 表面时，
文献中的实际 vdW 半径有时会被缩放。若将一个探针球（代表假设的溶剂
分子尺寸）在范德华表面上滚动，则其中心点描绘出溶剂可及表面（solvent accessible surface, SAS），
以绿色显示；SAS 等价于将原子半径增加探针球半径后的 vdW 表面。最后，
可以利用探针球，通过以红色显示的内凹（re-entrant）表面元来平滑 vdW 表面上尖锐的
裂隙，从而得到溶剂排除表面（solvent-excluded surface, SES）。](../assets/x2.png)

*图 11.1：PCM 所用各种溶质空腔表面定义的示意图。
751 Lange A. W. et al. Mol. Phys. (2020) , 118 , pp. e1644384 . Link 原子范德华球的并集（以灰色显示）
定义了范德华（vdW）表面（以黑色显示）。请注意，在构造 vdW 表面时，
文献中的实际 vdW 半径有时会被缩放。若将一个探针球（代表假设的溶剂
分子尺寸）在范德华表面上滚动，则其中心点描绘出溶剂可及表面（solvent accessible surface, SAS），
以绿色显示；SAS 等价于将原子半径增加探针球半径后的 vdW 表面。最后，
可以利用探针球，通过以红色显示的内凹（re-entrant）表面元来平滑 vdW 表面上尖锐的
裂隙，从而得到溶剂排除表面（solvent-excluded surface, SES）。*

空腔表面的构造是 PCM 的一个至关重要方面，因为计算所得性质对空腔构造的细节
非常敏感。大多数空腔构造基于原子中心球的并集（见图 [11.1](#fig:PCM_surfs)），
但还有若干种不同的构造方式，其术语在文献中时常被混淆。最简单也是最常见的
是由原子中心球的并集构成的范德华（vdW）表面。以原子 $A$ 为中心的球的半径可以写成如下形式

<a id="eq:PCM_atomic_radii"></a>
$$
R_{A}=\alpha_{\text{vdW}}R_{\text{vdW},A}+R_{\text{probe}} \tag{11.4}
$$

其中 $R_{\text{vdW},A}$ 是原子 $A$ 的 vdW 半径，例如取自 Bondi 发表的 vdW
半径集合[[146]](../bib_references/bib.md#bib136)。
传统上，从晶体学数据中提取的 vdW 半径 $R_{\text{vdW},A}$ 会乘以缩放因子
$\alpha_{\text{vdW}}=1.1$–1.2[[145]](../bib_references/bib.md#bib135)。

这 20% 的放大旨在模拟这样一个事实：溶剂分子无法一直接近到溶质原子的 vdW
半径处，尽管并不完全清楚同一个值是否在所有情况下都是最优的。（缩放因子默认为
$\alpha_{\text{vdW}}=1.2$，但用户可以修改。）

缩放原子半径的替代方案是给每个半径加上某个固定增量 $R_{\text{probe}}$，代表溶剂分子的
近似尺寸，由此得到所谓的*溶剂可及表面*（solvent accessible surface, SAS）。
对于水，常取 $R_{\text{probe}}=1.4$ Å，这大致对应水分子的实际物理尺寸，
尽管取 $R_{\text{probe}}=0.2$–0.5 Å 范围内的值往往能得到更好的溶和能[[569]](../bib_references/bib.md#bib580)。

无论如何，若使用非零的 $R_{\text{probe}}$ 值，则式 ([11.4](#eq:PCM_atomic_radii))
中的缩放因子应设为 $\alpha_{\text{vdW}}=1.0$，因为这两个参数意在模拟同一效应，
即溶剂分子的有限尺寸使其无法一直接近到溶质原子的 vdW 半径处。

从图 [11.1](#fig:PCM_surfs) 可以看出，vdW 表面和 SAS 在原子球相交处都存在尖点（cusp），
尽管随着原子半径被缩放或放大，这些尖点会变得不那么明显。在所谓的
*溶剂排除表面*（solvent-excluded surface, SES）中（有时称为 Connolly 表面或"分子表面"），
这些尖点被消除。SES 利用探针球在同时与两个或多个原子球相切处的球面，
定义"内凹表面"（re-entrant surface）的面元，从而平滑地连接原子（或"接触"）表面[[751]](../bib_references/bib.md#bib790)。

选定空腔表面的模型后，该表面使用以原子为中心的 Lebedev 网格[[777]](../bib_references/bib.md#bib809)
进行离散化，所用的网格与 DFT 数值积分中使用的网格属于同一类。
（SES 内凹面的离散化稍微复杂一些，但思路相似[[751]](../bib_references/bib.md#bib790)。）
表面电荷 $q_{i}$ 位于这些网格点上，Lebedev 求积权重可用于定义与每个离散化
点相关联的表面积[[753]](../bib_references/bib.md#bib786)。

上述离散化程序存在一个长期存在（但未被广泛报道）的问题：当溶质原子发生位移时，
它无法给出连续的能量面，因为随着定义空腔的原子球移动，某些表面网格点
可能会从溶质空腔中出现或消失。这种不良行为会阻碍几何优化的收敛，并且在某些
情况下会导致振动频率计算出现非常大的误差[[753]](../bib_references/bib.md#bib786)。
它也是对分子动力学计算的根本性障碍[[754]](../bib_references/bib.md#bib787)。
Lange 和 Herbert[[753]](../bib_references/bib.md#bib786)
在 York 和 Karplus 早期工作[[1525]](../bib_references/bib.md#bib1589)的基础上，
发展了一种通用方案，以能够给出光滑能量面的方式实现表观表面电荷 PCM，
甚至适用于涉及键断裂的 *从头算*（ab initio）分子动力学模拟[[754]](../bib_references/bib.md#bib787)。
值得注意的是，该方法忠实地保持了 PCM 所基于的底层积分方程理论的性质，
即平滑化程序不会显著扰动溶和能或空腔表面积[[753]](../bib_references/bib.md#bib786)。
这一平滑离散化程序将开关函数（switching function）与空腔表面电荷密度的高斯
模糊化（Gaussian blurring）相结合，因此被称为 PCM 的"Switching/Gaussian"（SwiG）
实现。

当溶质用分子力学或 SCF（Hartree-Fock 或 DFT）电子结构模型描述时，SwiG-PCM 均可
提供单点能和解析能量梯度，只不过对于 SES 空腔模型只能提供单点能。解析 Hessian
矩阵仅对 C-PCM 模型可用。（照常，若请求其他模型的振动频率，将通过解析
能量梯度的有限差分来计算。）相关波函数（correlated wave function）的单点能计算
可以结合这些溶剂模型进行，此时相关波函数计算将使用在连续介电溶剂存在下被极化的
Hartree-Fock 分子轨道（*即*，不存在后 Hartree–Fock 层面的 PCM 校正）。这代表了对
溶剂效应的"零级"处理，能够捕捉连续溶化对分子性质的主导阶效应[[569]](../bib_references/bib.md#bib580)。

鉴于模型本身的粗略性，更自洽地纳入后 Hartree–Fock 溶化效应预计并不重要[[569]](../bib_references/bib.md#bib580)。

使用这些 PCM 的研究者被要求引用文献
[[754]](../bib_references/bib.md#bib787)
和 [[756]](../bib_references/bib.md#bib789)，
其中给出了 **Q-Chem** 实现的细节；若使用 SES，则引用文献 [[751]](../bib_references/bib.md#bib790)；
若使用共轭梯度求解器或其他线性标度选项，则引用文献 [[561]](../bib_references/bib.md#bib576)。
我们特别提请读者关注文献 [[754]](../bib_references/bib.md#bib787)
和 [[1530]](../bib_references/bib.md#bib1593)，
其中评估了使用各种 PCM 和 Lebedev 网格时可以预期的离散化误差；**Q-Chem** 中的
默认网格值即基于这些测试确定。在发表基于 PCM 计算的结果时，必须同时指明
所使用的确切模型（见表 [11.3](#table:K-matrix)）以及空腔的构造方式，并且应避免
使用软件专用的关键字——这类关键字的使用已使连续静电学领域的文献相当混乱[[282]](../bib_references/bib.md#bib287)。

作为良好实践的示例，**Q-Chem** 中的默认空腔构造是使用 Bondi 原子半径的 vdW 空腔[[146]](../bib_references/bib.md#bib136)，
只是对氢原子我们采用修正后的半径 1.1 Å，这是遵循一项重新评估的结论——该评估认为
Bondi 最初给出的氢原子半径 1.2 Å 偏大[[1186]](../bib_references/bib.md#bib1240)。
随后，式 ([11.4](#eq:PCM_atomic_radii)) 中的每个半径 $R_{\text{vdW},A}$ 都
乘以因子 $\alpha_{\text{vdW}}=1.2$ 用于空腔构造。Bondi 未提供的
主族元素半径取自文献 [[889]](../bib_references/bib.md#bib923)。若缺少此类细节，
PCM 计算结果将难以在其他电子结构程序中被复现。

## 11.2.3.3 垂直激发、电离与发射的非平衡溶和

在垂直激发或电离过程中，溶质的电荷分布发生骤然变化。溶剂的各种微观运动
达到特定极化响应所需的特征时间不同，溶剂响应中的快速部分（电子）能够跟上这样的
动态过程，而其余自由度（原子核）则保持初态不变。
溶剂响应的这种分裂导致了非平衡溶和。
文献中已发展出两种描述非平衡溶剂效应的不同方法：线性响应（linear response, LR）
方法[[183]](../bib_references/bib.md#bib178)
和态专化（state-specific, SS）方法[[1365]](../bib_references/bib.md#bib1423)。
两者均已在 **Q-Chem** 中实现[[1530]](../bib_references/bib.md#bib1593)，
在 SCF 层面用于垂直电离，在相应的激发态层面（CIS 和 TDDFT，见第 [7.3.7](../ch07_excited/subsec_tddft-cPCM.md) 节，
或 ADC，见第 [7.10.11](../ch07_excited/topic_abs-adc.md) 节）用于垂直激发。下面对
这些方法作简要介绍，使用非平衡 PCM 功能的用户被要求引用文献
[[1530]](../bib_references/bib.md#bib1593)
和 [[940]](../bib_references/bib.md#bib979)。
针对长寿命激发态的态专化溶剂场平衡（用于计算*例如*发射能）已针对 ADC 系列方法实现，
见第 [7.10.11](../ch07_excited/topic_abs-adc.md) 节；针对 TDDFT 的实现见
第 [7.3.7.2](../ch07_excited/subsec_tddft-cPCM.md#subsubsec:tddft-PCM-iterSS) 节。使用这种平衡溶和
PCM 的用户请引用并参阅文献 [[939]](../bib_references/bib.md#bib982)。

LR 方法将溶化效应视为一对跃迁之间的耦合，一个属于溶质，另一个属于溶剂。
当溶质与溶剂之间的相互作用开启时的跃迁频率，可以通过将该相互作用视为微扰
来确定。在 TDDFT 框架内，溶质与溶剂之间的相互作用由下式给出[[599]](../bib_references/bib.md#bib622)

<a id="eq:LR-term"></a>
$$
\begin{split}\displaystyle\omega^{\prime}=&\displaystyle\int d\mathbf{r}\int d\mathbf{r}^{\prime}\int d\mathbf{r}^{\prime\prime}\int d\mathbf{r}^{\prime\prime\prime}\rho^{\ast}_{\text{tr}}(\mathbf{r})\left(\frac{1}{|\mathbf{r}-\mathbf{r}^{\prime}|}+g_{\mathrm{XC}}(\mathbf{r},\mathbf{r}^{\prime})\right)\\
&\displaystyle\times\chi^{*}(\mathbf{r}^{\prime},\mathbf{r}^{\prime\prime},\omega)\left(\frac{1}{|\mathbf{r}^{\prime\prime}-\mathbf{r}^{\prime\prime\prime}|}+g_{\mathrm{XC}}(\mathbf{r}^{\prime\prime},\mathbf{r}^{\prime\prime\prime})\right)\rho_{\text{tr}}(\mathbf{r}^{\prime\prime\prime})\;,\end{split} \tag{11.5}
$$

其中 $\chi$ 是溶剂的电荷密度响应函数，$\rho_{\text{tr}}(\mathbf{r})$ 是溶质的跃迁密度。
该项给出了对跃迁能的动力学修正，使其与溶剂对以溶质跃迁频率（$\omega$）振荡的
溶质电荷密度的响应相关联。
在 PCM 中，只考虑经典库仑相互作用，式 ([11.5](#eq:LR-term)) 变为

<a id="Ch11.E6"></a>
$$
\begin{split}\displaystyle\omega^{\prime}_{\mathrm{PCM}}=&\displaystyle\int d\mathbf{r}\int d\mathbf{s}\ \frac{\rho^{\ast}_{\text{tr}}(\mathbf{r})}{|\mathbf{r}-\mathbf{s}|}\int d\mathbf{s}^{\prime}\int d\mathbf{r}^{\prime}\,\mathcal{Q}(\mathbf{s},\mathbf{s}^{\prime},\varepsilon)\frac{\rho_{\text{tr}}(\mathbf{r}^{\prime})}{|\mathbf{s}^{\prime}-\mathbf{r}^{\prime}|}\;,\end{split} \tag{11.6}
$$

其中 $\mathcal{Q}$ 是对应一般介电常数 $\varepsilon$ 的 PCM 溶剂响应算符。
$\mathcal{Q}$ 与密度 $\rho_{\text{tr}}(\mathbf{r})$ 的势的积分给出溶剂极化的表面电荷密度。

SS 方法考虑了溶剂部分自由度能够在激发发生时对溶质波函数的变化作出瞬时响应的能力。
这种效应在 LR 方法中未被计入。在 SS 方法中，一般的溶剂化溶质激发态 $\Psi_{i}$
作为如下非线性 Schrödinger 方程的解获得

<a id="eq:SS-sdeq"></a>
$$
\left(\hat{H}^{\mathrm{vac}}+\hat{V}^{\mathrm{slow}}_{0}+\hat{V}^{\mathrm{fast}}_{i}\right)|\Psi_{i}\rangle=E^{\mathrm{SS}}_{i}|\Psi_{i}\rangle \tag{11.7}
$$

该方程依赖于溶质的电荷分布。这里 $\hat{H}^{\mathrm{vac}}$ 是真空中溶质的常规
Hamilton 量，反应场算符 $\hat{V}_{i}$ 产生对应于慢极化响应和快极化响应的
表观表面电荷密度（第 [11.2.3.1](#subsubsec:PCM-theory) 节）的静电势。
溶质相对于溶剂的反应场自洽地被极化。在垂直电离而非激发的情况下，电离态和
未电离态都可以在基态形式体系中处理。对于垂直激发，已针对各种激发态方法发展了
自洽 SS 模型[[611]](../bib_references/bib.md#bib634)，
并已针对 CIS 和 TDDFT 实现。

在线性介电介质中，溶剂极化由电极化率 $\chi=[\varepsilon(\omega)-1]/4\pi$ 决定，
其中 $\varepsilon(\omega)$ 是频率相关的介电常数。对于非常快的垂直跃迁，
介电响应由光学介电常数 $\varepsilon_{\text{opt}}=n^{2}$ 支配，其中 $n$ 是溶剂的
折射率。在 LR 和 SS 方法中，溶剂自由度的快速部分都与溶质密度的变化处于平衡。
在 PCM 框架内，SS 激发态 $i$ 的快溶剂极化电荷可通过求解下列方程获得[[271]](../bib_references/bib.md#bib273)：

<a id="eq:Kq=Rv-fast"></a>
$$
\mathbf{K}_{\varepsilon_{\mathrm{opt}}}\mathbf{q}^{\mathrm{fast,SS}}_{i}=\mathbf{R}_{\varepsilon_{\mathrm{opt}}}\left[\mathbf{v}_{i}+\mathbf{v}(\mathbf{q}^{\mathrm{slow}}_{0})\right]\;. \tag{11.8}
$$

这里 $\mathbf{q}^{\mathrm{fast,SS}}$ 是离散化的快表面电荷。矩阵 $\mathbf{K}$ 和
$\mathbf{R}$（第 [11.2.3.1](#subsubsec:PCM-theory) 节）中的介电常数被替换为光学介电常数，
$\mathbf{v}_{i}$ 是溶质激发态密度 $\rho_{i}$ 的势。量
$\mathbf{v}(\mathbf{q}^{\mathrm{slow}}_{0})$ 是基态下表观表面电荷慢部分的势，这些慢电荷由下式给出

<a id="slow_q"></a>
$$
\mathbf{q}^{\mathrm{slow}}_{0}=\left(\frac{\varepsilon-\varepsilon_{\mathrm{opt}}}{\varepsilon-1}\right)\mathbf{q}_{0}\;. \tag{11.9}
$$

对于 LR-PCM，溶剂极化只受电子密度的一阶变化（TDDFT 线性密度响应）作用，因此
式 ([11.8](#eq:Kq=Rv-fast)) 变为

<a id="Ch11.E10"></a>
$$
\mathbf{K}_{\varepsilon_{\mathrm{opt}}}\mathbf{q}^{\mathrm{fast,LR}}_{i}=\mathbf{R}_{\varepsilon_{\mathrm{opt}}}\mathbf{v}(\rho^{\mathrm{tr}}_{i})\;. \tag{11.10}
$$

**Q-Chem** 提供了用于 CIS/TDDFT 激发的 LR 方法，以及用于垂直电离的自洽 SS 方法
（使用基态 SCF）。自洽 SS 方法也可用于垂直激发，但当激发态之间存在（近）简并时
（例如在锥形 intersections 附近）可能会出现问题。SS 方法的根本问题在于，
每个波函数 $\Psi_{i}$ 都是*不同* Hamilton 量的本征函数，因为
式 ([11.7](#eq:SS-sdeq)) 依赖于所关心的具体态。为避免态排序和非正交性问题，
我们采用对 SS 方法的一阶微扰近似[[182]](../bib_references/bib.md#bib179)
来计算垂直激发能，我们称之为"ptSS"方法[[940]](../bib_references/bib.md#bib979)。
零级激发态波函数可以使用各种激发态方法计算（**Q-Chem** 中目前支持 CIS 和 TDDFT），
其中分子轨道来自基态 PCM 计算、并经过溶剂弛豫。如前所述，LR 和 SS 描述非平衡
溶和中不同的溶剂弛豫特征。在微扰方案中，我们可以利用零级跃迁密度计算 LR 贡献，
我们称之为"ptLR"方法。ptSS 与 ptLR 的组合在与 TDDFT 结合使用时能给出定量上
良好的溶剂致变色（solvatochromatic）位移，但与 ADC 的相关变体结合时则不然，
后者已证明纯 ptSS 方法更优[[1530]](../bib_references/bib.md#bib1593)。

LR 和 SS 方法也可用于光子发射过程的研究[[612]](../bib_references/bib.md#bib635)。
发射过程可以视为激发态势能面驻点处的垂直激发。因此基本要求是为所关心的
激发态准备好经溶剂弛豫的几何结构。TDDFT/LR-C-PCM 的解析梯度和 Hessian 均可用。
关于借助 PCM 进行激发态几何优化的计算细节，请参见第 [7.3.8](../ch07_excited/subsec_tddft-hessian.md) 节。
发射过程比吸收情形稍微复杂。文献中讨论了两种情形，取决于所涉激发态的寿命。
在超快激发态衰变的极限情形下，只有溶剂自由度的快速部分与激发态密度达到平衡。在此
极限下，发射能可以完全按照计算垂直激发能的方式精确计算。此时，激发态几何优化应
在非平衡极限下进行。另一个极限是长寿命激发态，*例如*强荧光物种和磷光。
在长寿命情形下，激发态几何优化应在溶剂平衡极限下进行。因此，激发态应使用平衡的
LR 或 SS 方法计算，而基态则使用非平衡自洽 SS 方法计算。后一种方法已针对 ADC
系列方法实现（见第 [7.10.11](../ch07_excited/topic_abs-adc.md) 节），并针对 TDDFT 实现
（见第 [7.3.7.2](../ch07_excited/subsec_tddft-cPCM.md#subsubsec:tddft-PCM-iterSS) 节）。

## 11.2.3.4 基于约束平衡原理的吸收与发射光谱

对于溶液中的超快过程，如电子转移、光吸收/发射和光电离，
连续介质模型应当结合恰当的非平衡溶化理论，以描述非平衡的溶质–溶剂相互作用。
在传统处理方法中，非平衡静电溶化自由能是由沿连接初始平衡态（eq）与中间非平衡态（neq）
的路径对所谓可逆电功进行积分推导出来的，*即*[[901]](../bib_references/bib.md#bib935)：

<a id="Ch11.E11"></a>
$$
[\rho=0,\Phi=0]\xrightarrow[]{\varepsilon}[\rho_{1},\Phi^{\mathrm{eq}}_{1}]\xrightarrow[]{\varepsilon_{\mathrm{opt}}}[\rho_{2},\Phi^{\mathrm{neq}}_{2}] \tag{11.11}
$$

其中 $\Phi$ 表示总电势，包括真空中由溶质电荷 $\rho$ 产生的势 $\psi$ 和由介质产生的极化势 $\varphi$。
为了处理溶液中的电子吸收与发射光谱，这种非平衡溶化自由能的数值表达式（由从溶质电荷与
极化电荷相互作用中直观地汇集一系列能量项而建立）已在结合 PCM 模型的 TDDFT 中实现[[271]](../bib_references/bib.md#bib273)。

容易验证，这一数值形式可以通过对传统处理方法中非平衡溶化能的解析表达式进行离散化而得到[[821]](../bib_references/bib.md#bib852)。

然而，这种可逆电功方法在超快过程中会高估溶剂重组能，对此存在诸多质疑[[132]](../bib_references/bib.md#bib122)。
现在已经清楚，在初始平衡态与中间非平衡态之间不可能找到一条可逆路径，因此
积分电功不等于静电自由能的变化[[821]](../bib_references/bib.md#bib852)。

Xiangyuan Li *et al.*[[1495]](../bib_references/bib.md#bib1563)
运用约束平衡原理（constrained equilibrium principle），
建立了如下路径的非平衡溶化新理论：

<a id="Ch11.E12"></a>
$$
[\rho_{1},\varphi^{\mathrm{eq}}_{1}]\xrightarrow[]{\mathrm{fast}}[\rho_{2},\varphi^{\mathrm{neq}}_{2}]\xrightarrow[]{-\lambda_{\mathrm{s}}}[\rho_{2},\varphi^{\mathrm{eq}}_{2}]\xrightarrow[]{+\rho_{\mathrm{ex}},\mathrm{quasistatic}}C[\rho_{2}+\rho_{\mathrm{ex}},\varphi^{\mathrm{neq}}_{2}] \tag{11.12}
$$

其中 C 代表约束平衡态，它是通过引入合适的外电荷 $\rho_{\mathrm{ex}}$ 来构造的，
该外电荷用于使"残余"极化势 $\varphi^{{}^{\prime}}=\varphi^{\mathrm{neq}}_{2}-\varphi^{\mathrm{eq}}_{2}$ 达到平衡，
从而将该约束平衡态映射到真实的非平衡态。这样，溶剂重组能可以推导为

<a id="eq:lamuda_re"></a>
$$
\lambda_{\mathrm{s}}=-\frac{1}{2}\int_{V}\rho_{\text{ex}}\;\varphi^{\prime}\;dV \tag{11.13}
$$

于是非平衡溶化自由能简单地由下式给出

<a id="eq:neq_sol"></a>
$$
F^{\mathrm{neq}}_{2}=\frac{1}{2}\int_{V}\rho_{2}\;\varphi^{\mathrm{eq}}_{2}\;dV+\lambda_{\mathrm{s}} \tag{11.14}
$$

关于外（约束）电荷 $\rho_{\mathrm{ex}}$ 或等价的外约束电场 $\mathbf{E}_{\mathrm{ex}}$
获得的更详细描述，请参阅综述[[821]](../bib_references/bib.md#bib852)。

在连续介质模型的框架内，式 ([11.14](#eq:neq_sol)) 的离散化与数值求解表示为[[130]](../bib_references/bib.md#bib118)

<a id="Ch11.E15"></a>
$$
F^{\mathrm{neq}}_{i}=\sum_{m}V_{i,m}Q^{\mathrm{neq}}_{i,m}-\frac{1}{2}\sum_{m}Q^{\mathrm{neq}}_{i,m}D(\varepsilon)Q^{\mathrm{neq}}_{i,m} \tag{11.15}
$$

其中下标 $i$ 表示基态（$i$ = 1）或激发态（$i$ = 2）电子态。
值 $V_{i,m}$ 指溶质在第 $m$ 个面元（tessera）处的静电势。
$Q^{\mathrm{neq}}_{i,m}$ 是非平衡态的表观电荷。量 $D(\varepsilon)$
是 C-PCM 和 IEF-PCM 等 PCM 中出现的方阵（见第 [11.2.3.1](#subsubsec:PCM-theory) 节）。

吸收的垂直激发能定义为

<a id="eq:hv_ab"></a>
$$
hv_{\mathrm{ab}}=G^{\mathrm{neq}}_{2}-G^{\mathrm{eq}}_{1} \tag{11.16}
$$

其中 $G$ 表示溶液中溶质的总自由能，

<a id="Ch11.E17"></a>
$$
G^{\mathrm{eq}}_{1}=E_{1}+F^{\mathrm{eq}}_{1}=E_{1}+\frac{1}{2}\sum_{m}V_{1,m}Q^{\mathrm{eq}}_{1,m}\; \tag{11.17}
$$

量 $G^{\mathrm{eq}}_{1}$ 由基于平衡基态反应场的 SCRF 方法计算，$E_{1}$
表示溶质的基态电子能。
基于平衡基态反应场，并在 TDDFT 框架内采用自洽的态专化方法，$G^{\mathrm{neq}}_{2}$ 由下式给出[[130]](../bib_references/bib.md#bib118)

<a id="eq:G2_neq"></a>
$$
G^{\mathrm{neq}}_{2}=E_{1}+\omega_{\mathrm{ab}}+\sum_{m}V_{1,m}Q^{\mathrm{eq}}_{1,m}+\sum_{m}V_{2,m}(Q^{\mathrm{neq}}_{2,m}-Q^{\mathrm{eq}}_{1,m})-\frac{1}{2}\sum_{m}Q^{\mathrm{neq}}_{2,m}D(\varepsilon)Q^{\mathrm{neq}}_{2,m} \tag{11.18}
$$

其中 $\omega_{\mathrm{ab}}$ 是 TDDFT 激发能。
另一种方式是，基于非平衡激发态反应场，$G^{\mathrm{neq}}_{2}$ 由下式给出[[129]](../bib_references/bib.md#bib119)

<a id="eq:G2_neq_k"></a>
$$
G^{\mathrm{neq}}_{2,k}=E^{k}_{1}+\omega^{k}_{\mathrm{ab}}-\sum_{m}V^{k}_{1,m}Q^{\mathrm{neq},k}_{2,m}-\frac{1}{2}\sum_{m}Q^{\mathrm{neq},k}_{2,m}D(\varepsilon)Q^{\mathrm{neq},k}_{2,m}\;, \tag{11.19}
$$

其中 $k$ 表示在溶质基态几何结构下非平衡激发态反应场的第 $k$ 次迭代。
$\omega^{k}_{\mathrm{ab}}$ 是在非平衡激发态反应场存在下由 TDDFT 计算得到的激发能。
量 $E^{k}_{1}$ 是第 $k$ 次迭代时溶质的基态电子能。
显然，式 ([11.19](#eq:G2_neq_k)) 比式 ([11.18](#eq:G2_neq)) 更具物理意义。

类似地，发射的垂直激发能由下式给出[[129]](../bib_references/bib.md#bib119)

<a id="Ch11.E20"></a>
$$
hv_{\mathrm{em}}=G^{\mathrm{eq}}_{2}-G^{\mathrm{neq}}_{1} \tag{11.20}
$$

其中 $G^{\mathrm{eq}}_{2}$ 和 $G^{\mathrm{neq}}_{1}$ 分别表示在激发态平衡几何结构下的
平衡激发态自由能和非平衡基态自由能。它们可以表示为[[129]](../bib_references/bib.md#bib119)

<a id="Ch11.E21"></a>
$$
\displaystyle G^{\mathrm{neq}}_{1} \tag{11.21a}
$$

量 $\omega^{k}_{\text{em}}$ 可以直接由在第 $k$ 次迭代的平衡激发态反应场中进行的
TDDFT 计算获得。能量 ${E^{k}_{1}}^{\prime}$ 和 $E_{1}^{\prime\prime}$ 分别是在非平衡基态
反应场存在下对应的溶质基态电子能，以及在激发态平衡几何结构下溶质的基态电子能。

要将约束平衡原理应用于垂直吸收和垂直发射，请在 *$pcm* 段中使用
**Td_CEq_NonEq** 关键字。用户被要求引用文献 [[821]](../bib_references/bib.md#bib852)。

**注意：

本方法与自旋翻转（spin-flip）计算不兼容。
**

## 11.2.3.5 非均匀 PCM（Heterogeneous PCM）

为模拟蛋白质及其他各向异性环境，有人提出了"非均匀 PCM"（HetPCM）方法，
其本质是对每个原子球使用不同的介电常数[[613]](../bib_references/bib.md#bib636)。

与可基于明确假设由 Maxwell 方程组推导出的各向同性 PCM[[569]](../bib_references/bib.md#bib580)
不同，HetPCM 完全是*特设的*（ad hoc）。
不过，近期它首次借助使用第 [11.2.11](sect_PEQS.md) 节讨论的 PEqS 方法实现的
精确 Poisson 边界条件进行了检验[[150]](../bib_references/bib.md#bib143)。

对于采用两个不同介电常数的 HetPCM 方法（即用 $\varepsilon=78$ 表示水环境，
用较小值 $\varepsilon_{\text{nonp}}$ 表示非极性或疏水区域），
结果表明，只要 $\varepsilon_{\text{nonp}}\gtrsim 4$，非均匀模型就与相应非均匀介电环境下
Poisson 方程解 reasonably 吻合[[150]](../bib_references/bib.md#bib143)。

这与常用于模拟蛋白质疏水内部的数值相符[[569]](../bib_references/bib.md#bib580)。

关于如何设置 HetPCM 计算的说明，请参见示例 [11.2.4.2](subsec_PCM_job_control.md#ex:HetPCM)。
HetPCM 提供解析梯度。
