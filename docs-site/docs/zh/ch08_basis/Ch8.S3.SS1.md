---
title: "8.3.1 基组符号表示概览"
---

## 8.3.1 基组符号表示概览

（2026 年 7 月 4 日）

下表给出了若干示例，它们遵循指定基组时普遍采用的标准格式。唯一的例外是附加的弥散函数。这些弥散函数最好以类似于极化函数的插入方式来添加：写在括号中，并让轻原子的指定紧跟在重原子指定之后：(*heavy*, *light*)；在需要将弥散函数加到氢原子上但不加到重原子上的少见情形中，则用句点作为占位符。一般形式见表 [8.1](#table:BS:Pople)。这一约定可以应用于表 [8.2](#table:Atoms:Pople) 中所列的具名 Pople 型基组，由此得到的具体示例列于表 [8.3](#table:BS:Pople-ext)。

| 基组名称 ${}^{a}$ | $j$ | $m$ ${}^{b}$ | $n$ ${}^{c}$ |
| --- | --- | --- | --- |
| STO- $j$ ( $k$ +, $l$ +)G( $m$ , $n$ ) | 2,3,6 | d | p |
| $j$ -21( $k$ +, $l$ +)G( $m$ , $n$ ) | 3 | 2d | 2p |
| $j$ -31( $k$ +, $l$ +)G( $m$ , $n$ ) | 4,6 | 3d | 3p |
| $j$ -311( $k$ +, $l$ +)G( $m$ , $n$ ) | 6 | df, 2df, 3df | pd, 2pd, 3pd |

- ${}^{a}$$k$ 和 $l$ 分别表示重原子上和氢原子上的弥散函数组数。
- ${}^{b}$$m$ 表示重原子上的极化函数组数。
- ${}^{c}$$n$ 表示氢原子上的极化函数组数。

表 8.1： 
**Q-Chem** 中可用的 Pople 型基组汇总。

| 符号名称 | 支持的原子 |
| --- | --- |
| STO-2G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K, Ca, Sr |
| STO-3G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ I |
| STO-6G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| 3-21G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ Xe, Cs |
| 4-31G | H, He, Li $\rightarrow$ Ne, P $\rightarrow$ Cl |
| 6-31G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| 6-311G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| G3LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| G3MP2LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

表 8.2： 
**Q-Chem** 中可用的 Pople 基组所支持的原子。

| 符号名称 | 支持的原子 |
| --- | --- |
| 3-21G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr, Rb $\rightarrow$ Xe, Cs |
| 3-21+G | H, He, Na $\rightarrow$ Cl, Na $\rightarrow$ Ar, K, Ca, Ga $\rightarrow$ Kr |
| 3-21G* | Na $\rightarrow$ Ar |
| 6-31G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31+G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-31G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31G(d,p) | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Zn, Ga $\rightarrow$ Kr |
| 6-31G(.,+)G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-31+G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| 6-311G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| 6-311+G | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar |
| 6-311G* | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| 6-311G(d,p) | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ I |
| G3LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Kr |
| G3MP2LARGE | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

表 8.3： 
扩展 Pople 基组的示例。

尽管在现代量子化学中并不常用，Dunning[[354]](../bib_references/bib.md#bib359)
 仍提出了一批早期基组，记为 SV、DZ 和 TZ；见表 [8.4](#table:BS:Dunning-orig-ext)。（不要将它们与同样以 Dunning 之名广为使用的“相关一致”（correlation-consistent）基组相混淆。）原始 Dunning 基组可以用与 Pople 基组类似的命名法来添加弥散函数和极化函数：*name*($k$+,$l$+)($m$d,$n$p)，
其中 $k$ 为额外增加的重原子弥散函数数目，$l$ 为额外增加的轻原子弥散函数数目，
$m$ 为额外增加的重原子 $d$ 极化函数数目，
$n$ 为额外增加的轻原子 $p$ 极化函数数目。

| 符号名称 | 支持的原子 |
| --- | --- |
| SV | H, Li $\rightarrow$ Ne |
| SV* | H, B $\rightarrow$ Ne |
| SV(d,p) | H, B $\rightarrow$ Ne |
| SV(2+,+)(2d,p) | H, B $\rightarrow$ Ne |
| DZ | H, Li $\rightarrow$ Ne, Al $\rightarrow$ Cl |
| DZ+ | H, B $\rightarrow$ Ne |
| DZ++ | H, B $\rightarrow$ Ne |
| DZ* | H, Li $\rightarrow$ Ne |
| DZ** | H, Li $\rightarrow$ Ne |
| DZ(d,p) | H, Li $\rightarrow$ Ne |
| DZ(2+,+)(2d,p) | H, B $\rightarrow$ Ne |
| TZ | H, Li $\rightarrow$ Ne |
| TZ+ | H, Li $\rightarrow$ Ne |
| TZ++ | H, Li $\rightarrow$ Ne |
| TZ* | H, Li $\rightarrow$ Ne |
| TZ** | H, Li $\rightarrow$ Ne |
| TZ(d,p) | H, Li $\rightarrow$ Ne |

表 8.4： 
扩展 Dunning 基组的示例。

与 Dunning 相关联、使用远为广泛的基组是相关一致（“cc”）系列基组。[[355]](../bib_references/bib.md#bib360)

其中的基本系列及其增广（augmented）对应版本列于表 [8.5](#table:Atoms:Dunning-cc)。以 “-PP” 结尾的是赝势基组，仅对重元素定义， intended 与有效核势（effective core potentials, ECPs）配合使用，ECP 相关内容见第 [8.10](sec_ECPs.md) 节。每个相关一致基组（cc-*name*）都有一个“增广”对应版本（aug-cc-*name*），其中包含弥散函数。

| 符号名称 | 支持的原子 |
| --- | --- |
| cc-pVDZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVDZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVDZ-PP | Cu $\rightarrow$ Rn |
| cc-pVTZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVTZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVTZ-PP | Cu $\rightarrow$ Rn |
| cc-pVQZ | H $\rightarrow$ Ar, Ca, Ga $\rightarrow$ Kr |
| cc-pVQZ-full | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pVQZ-PP | Cu $\rightarrow$ Rn |
| cc-pV5Z | H $\rightarrow$ Ar, Ca $\rightarrow$ Kr |
| cc-pV6Z | H $\rightarrow$ Ar except Li, Na, Mg |
| cc-pCVDZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVDZ) |
| cc-pCVTZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVTZ) |
| cc-pCVQZ | H $\rightarrow$ Ar, Ca (H and He use cc-pVQZ) |
| cc-pCV5Z | H, He, B $\rightarrow$ Ar, Ca (H and He use cc-pV5Z) |
| cc-pwCVDZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar |
| cc-pwCVTZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn |
| cc-pwCVQZ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn, Br |
| cc-pwCVDZ-PP | Cu $\rightarrow$ Rn |
| cc-pwCVTZ-PP | Cu $\rightarrow$ Rn |
| cc-pwCVQZ-PP | Cu $\rightarrow$ Rn |
| aug-cc-pVDZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVDZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pVTZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVTZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pVQZ ${}^{a}$ | H $\rightarrow$ Kr |
| aug-cc-pVQZ-PP ${}^{b}$ | Cu $\rightarrow$ Rn |
| aug-cc-pV5Z | H $\rightarrow$ Ar, Sc $\rightarrow$ Kr |
| aug-cc-pV6Z | H $\rightarrow$ Ar except Li, Be, Na, Mg |
| aug-cc-pCVDZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVDZ) |
| aug-cc-pCVTZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVTZ) |
| aug-cc-pCVQZ ${}^{a}$ | H $\rightarrow$ Ar (H and He use aug-cc-pVQZ) |
| aug-cc-pCV5Z | H, He, B $\rightarrow$ Ar (H and He use aug-cc-pV5Z) |
| aug-cc-pwCVDZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar |
| aug-cc-pwCVTZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn |
| aug-cc-pwCVQZ ${}^{c}$ | B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Sc $\rightarrow$ Zn, Br |
| aug-cc-pwCVDZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |
| aug-cc-pwCVTZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |
| aug-cc-pwCVQZ-PP ${}^{c}$ | Cu $\rightarrow$ Rn |

- ${}^{a}$同时提供 may-、jun- 和 jul-cc-p(C)VXZ 变体
- ${}^{b}$同时提供 jun-cc-pVXZ-PP 变体
- ${}^{c}$同时提供 jun-cc-p(w)VXZ(-PP) 变体

表 8.5： 
**Q-Chem** 中相关一致基组所支持的原子。
对于 cc-pVXZ（X = D、T、Q），名称不以 “-full” 结尾的对应于采用分段收缩（segmented contraction）方案的定义，[[308]](../bib_references/bib.md#bib313)
 而以 “-full” 结尾的则对应于最初优化的通用收缩（generally-contracted）定义。
对于所有其他不存在此区别的基组，唯一定义均来自优化的通用收缩。
对于增广基组，脚注标明了“日历”（calendar）变体的可用性。[[1039]](../bib_references/bib.md#bib1083)

相关一致范式的做法是为每一个角动量类别都添加额外的弥散函数，也就是说，对于碳这样的第二周期原子，aug-cc-pVDZ 基组包含弥散 $s$、$p$ 和 $d$ 函数（每个原子 10 个弥散函数），
而氢则包含弥散 $s$ 和 $p$ 函数。aug-cc-pVTZ 基组还为碳加入了弥散 $f$ 函数
（使每个原子共有 20 个弥散函数），并为氢加入了弥散 $d$ 函数。与指数较紧的函数相比，
引入弥散函数的计算代价相对较高，且容易产生阻碍 SCF 收敛的线性相关问题，
详见第 [8.3.2](sec_Basis_Customization.md) 节。同时，弥散函数对于阴离子、
激发态和非共价相互作用的描述往往至关重要，但 aug-cc-pVXZ 中所含的高角动量弥散函数并不总是必需的。
正是出于这一考虑，人们提出了相关一致基组的“日历”版本
（jul-、jun- 和 may-*name*），[[1039]](../bib_references/bib.md#bib1083)
它们从 aug-cc-*name* 出发系统地剔除弥散基函数。jul-cc-pVXZ 基组剔除了氢上的所有弥散
函数，等价于对氢使用 cc-pVXZ、对重原子使用 aug-cc-pVXZ。jun-cc-pVXZ 基组
还进一步剔除每个重原子上角动量最高的弥散函数，*e.g.*，对碳原子而言，剔除弥散 $d$ 函数即得 jun-cc-pVDZ，剔除弥散 $f$ 函数即得 jun-cc-pVTZ。
may-cc-pVXZ 基组则再剔除 jun-cc-pVXZ 中残存的角动量最高的弥散函数，因此对
碳原子而言，may-cc-pVDZ 仅含单个弥散 $s$ 函数，属于最小增广。**Q-Chem** 同时收录了 may-、jun-
和 jul-cc-pVXZ，以及相应的 may-、jun- 和 jul-cc-pCVXZ（两种情形下均为 X = D、T、Q）。
此外还有 aug-cc-pVXZ-PP 对应的 jun-cc-pVXZ-PP 配对，以及 aug-cc-pwCVXZ(-PP) 对应的 jun-cc-pwCVXZ(-PP) 配对，同样取 X = D、T 或 Q。
如果用户想了解这些基组中究竟包含哪些函数，只需在 *$rem* 段中设置 PRINT_GENERAL_BASIS =
TRUE（如第 [8.3.2](sec_Basis_Customization.md) 节所述），即可输出基函数信息的打印结果。

| 符号名称 | 支持的原子 |
| --- | --- |
| TZV | H $\rightarrow$ Kr |
| VDZ | H $\rightarrow$ Kr |
| VTZ | H $\rightarrow$ Kr |

表 8.6： 
**Q-Chem** 中原始 Ahlrichs 基组[[1202]](../bib_references/bib.md#bib1256)所支持的原子。

（请注意，它们与更现代的 Karlsruhe “def2” 基组不同，后者见表 [8.7](#table:Atoms:Karlsruhe-def2)。）

Ahlrichs 这个名字还与两套不同的基组集合相关联。
较旧的一套（TZV、VDZ 和 VTZ）列于表 [8.6](#table:Atoms:Ahlrichs-orig)；[[1202]](../bib_references/bib.md#bib1256)
这些基组虽可使用，但已不再常用。使用远为广泛的是列于表 [8.7](#table:Atoms:Karlsruhe-def2) 的第二代 “def2”
基组，[[1438]](../bib_references/bib.md#bib1504)
它们有时被称为 “Karlsruhe” 基组，以区别于 Ahlrichs 及其同事在卡尔斯鲁厄大学开发的早期基组。这些基组最初是为 SCF 计算设计的，不过
近年来它们在关联波函数计算中也得到了一定应用。弥散函数是后来才补充的，[[1147]](../bib_references/bib.md#bib1199)
通过以 “D” 结尾的名称来表示，*e.g.*，def2-SVP 不含弥散函数，而 def2-SVPD 则含有。
def2-ha 和 def2-ma 变体（*e.g.*，def2-ha-SVP）包含部分增广。[[481]](../bib_references/bib.md#bib492)

def2-ha 基组是“重原子增广”（heavy-augmented）的，去除了氢原子上的所有弥散函数，因此
def2-ha-SVP 由氢上的 def2-SVP 与其他原子上的 def2-SVPD 组合而成。def2-ma 基组是“最小增广”（minimally-augmented）的，
它们是在 def2-ha-SVP 的基础上再剔除每个重原子上角动量最高的弥散函数而构成的，类似于
jun-cc-pVXZ 的做法。

| 符号名称 | 支持的原子 |
| --- | --- |
| def2-mSVP | H–Kr, ${}^{a}$ Rb–Rn (with def2-ECP) |
| def2-SV(P), def2-SVP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-SVP, def2-ha-SVP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-SVPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-TZVP, def2-TZVPP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-TZVP, def2-ma-TZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-ha-TZVP, def2-ha-TZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-TZVPD, def2-TZVPPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-QZVP, def2-QZVPP | H–Kr; Rb–Rn (with def2-ECP) |
| def2-ma-QZVP, def2-ma-QZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-ha-QZVP, def2-ha-QZVPP | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |
| def2-QZVPD, def2-QZVPPD | H–Kr; Rb–La, Hf–Rn (with def2-ECP) |

- ${}^{a}$Na–Kr 与 def2-SV(P) 完全相同

表 8.7： 
**Q-Chem** 中 Karlsruhe “def2” 基组[[1438]](../bib_references/bib.md#bib1504)所支持的原子。

最后，还有一批与 Jensen 之名[[635]](../bib_references/bib.md#bib661)
相关联的基组（见表 [8.8](#table:Atoms:Jensen-pc)），它们主要是为 NMR 计算而开发的。
此外还有一个“通用”（universal）高斯基组，[[310]](../bib_references/bib.md#bib315)
除 Pa–Np 和 Cm–Bk 外，它对 H–Lr 各元素均提供支持。

| 符号名称 ${}^{a}$ | 支持的原子 |
| --- | --- |
| pcseg- $n$ | H $\rightarrow$ Kr |
| pc- $n$ | H $\rightarrow$ Kr |
| pcJ- $n$ | H $\rightarrow$ Ar |
| psS- $n$ | H $\rightarrow$ Ar |
| aug-pcseg- $n$ | H $\rightarrow$ Kr |
| aug-pc- $n$ | H $\rightarrow$ Kr |
| aug-pcJ- $n$ | H $\rightarrow$ Ar |
| aug-psS- $n$ | H $\rightarrow$ Ar |

- ${}^{a}$各系列中 $n=0,1,2,3,4$

表 8.8： 
**Q-Chem** 中可用的 Jensen 极化一致（polarization consistent）基组所支持的原子。应优先使用
pcseg-$n$ 而非 pc-$n$，因为前者在 **Q-Chem** 中效率更高。pcJ-$n$[[636]](../bib_references/bib.md#bib662)
和 pcS-$n$[[635]](../bib_references/bib.md#bib661)
基组分别针对 NMR 自旋-自旋耦合与化学屏蔽进行了优化。
