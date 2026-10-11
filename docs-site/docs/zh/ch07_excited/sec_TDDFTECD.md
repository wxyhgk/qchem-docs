---
title: "7.3.9 电圆二色性"
---

## 7.3.9 电圆二色性

(July 4, 2026)

圆二色性（circular dichroism, CD）定义为样品对左旋与右旋圆偏振光的差分吸收，表示为 $\Delta\varepsilon=\varepsilon_{\text{L}}-\varepsilon_{\text{R}}$。电子圆二色性（electronic circular dichroism, ECD）专门探测电子跃迁，其强度由从基态到第 $n$ 个激发态跃迁的旋光强度（rotatory strength）$R_{0n}$ 来表征。在电偶极近似之外，ECD 的贡献包含电偶极-磁偶极项以及电偶极-电四极项。对于各向同性体系（如稀溶液），由于旋转平均的作用，电偶极-电四极贡献消失，旋光强度简化为

<a id="Ch7.E35"></a>
$$
R_{0n}=\mathrm{Im}\big{[}\bm{\mu}_{0n}\cdot\mathbf{m}_{n0}\big{]}, \tag{7.35}
$$

其中 $\bm{\mu}_{0n}$ 是跃迁电偶极矩，$\mathbf{m}_{n0}$ 是跃迁磁偶极矩。计算旋光强度有两种表述形式，取决于跃迁电偶极矩的求值方式。一种是“长度规范”（length-gauge），其中跃迁电偶极矩由下式给出

<a id="Ch7.E36"></a>
$$
\bm{\mu}_{0n}^{\text{(l)}}=-e\langle\Psi_{0}|\hat{\mathbf{r}}|\Psi_{n}\rangle. \tag{7.36}
$$

另一种是“速度规范”（velocity-gauge，亦称为跃迁电速度偶极），定义为

<a id="Ch7.E37"></a>
$$
\bm{\mu}_{0n}^{\text{(v)}}=-\frac{e}{i\omega_{n}}\langle\Psi_{0}|\hat{\mathbf{p}}|\Psi_{n}\rangle. \tag{7.37}
$$

因此，长度规范和速度规范下的旋光强度分别为 $R_{0n}^{\text{(l)}}=\mathrm{Im}\big{[}\bm{\mu}_{0n}^{\text{(l)}}\cdot\mathbf{m}_{n0}\big{]}$ 与 $R_{0n}^{\text{(v)}}=\mathrm{Im}\big{[}\bm{\mu}_{0n}^{\text{(v)}}\cdot\mathbf{m}_{n0}\big{]}$。在有限基组内，长度规范与速度规范的表述并不等价：长度规范下旋光强度的值依赖于原点（或位置），而速度规范下的旋光强度与原点无关。因此，推荐使用速度规范的表述形式。

ECD 旋光强度的计算支持 CIS 和 TDDFT 任务，并且在所有激发态计算完成后自动执行。请注意，如果同时求解了 TDA 和 TDDFT（即 RPA）方程，则仅计算 TDDFT 激发态的旋光强度。输出中会给出两种规范下的旋光强度，以及每个态的跃迁电速度偶极矩和跃迁磁偶极矩。由于 $\bm{\mu}_{0n}^{\text{(v)}}$ 和 $\mathbf{m}_{n0}$ 为纯虚数，因此只打印它们的虚部。
