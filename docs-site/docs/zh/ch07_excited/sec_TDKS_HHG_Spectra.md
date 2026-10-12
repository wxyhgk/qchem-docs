---
title: "7.4.4 高次谐波产生（HHG）光谱的计算"
---

## 7.4.4 高次谐波产生（HHG）光谱的计算

（2026 年 7 月 4 日）

偶极加速度形式下的高次谐波产生（high-harmonic generation, HHG）光谱 $H(\omega)$ 由下式计算[[258]](../bib_references/bib.md#bib259)

<a id="eq:hhg"></a>

$$
H(\omega)=\sum_{\kappa=x,y,z}\frac{1}{2\pi}\left|\int\frac{d^{2}\mu_{\kappa}(t)}{dt^{2}}w(t)e^{-i\omega t}dt\right|^{2} \tag{7.72}
$$

其中 $w(t)$ 是用于改善光谱质量的某种窗函数，$\mu_{\kappa}(t)$ 是含时偶极矩分量。
对于沿 $\kappa$ 方向偏振的光（$\kappa\in\{x,y,z\}$），有 $\mu_{\lambda}(t)=0$（$\lambda\in\{x,y,z\},\lambda\neq\kappa$），此时式 ([7.72](#eq:hhg)) 变为

<a id="eq:hhg2"></a>

$$
H(\omega)=\frac{1}{2\pi}\left|\int\frac{d^{2}\mu_{\kappa}(t)}{dt^{2}}w(t)e^{-i\omega t}dt\right|^{2} \tag{7.73}
$$

通常更倾向于引入复吸收势（complex absorbing potential, CAP），以减弱由有限基组近似所产生的伪影，参见第 [7.4.2.3](sec_TDKS_JobControl.md#sec:TDKS:CAP) 节。

我们提供了一个脚本，可在 TDKS 模拟完成后用于获取光谱：

- `$QC/bin/tools/tdks_hhg.py`

该脚本使用式 ([7.73](#eq:hhg2))，其中 $w(t)$ 取为 Hamming 窗函数[[1579]](../bib_references/bib.md#bib1642)。

当 $\kappa=z$ 时，可以按如下方式运行该脚本：

> ```qchem
> python3 $QC/bin/tools/tdks_hhg.py z output spectrum.txt
> ```

处理脚本生成的 `spectrum.txt` 文件将包含两列：谐波阶数与对数强度（任意单位）。
谐波阶数为 $\omega$ 除以 FIELD_FREQUENCY，对数强度为 $\log[H(\omega)]$。
这些数据可以作为 $(x,y)$ 图进行可视化，以查看光谱。我们将 **Q-Chem** 的 TDKS 代码用于 HHG 光谱的用户，请引用文献 [[1579]](../bib_references/bib.md#bib1642)
。
