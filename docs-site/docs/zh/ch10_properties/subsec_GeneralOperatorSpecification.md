---
title: "10.14.3 $response 节与算符指定"
---

## 10.14.3 *$response* 节与算符指定

(July 4, 2026)

用于求解响应向量（response vectors）的算符指定方式设计得非常灵活。*$response* 输入节的一般形式如下

> ```qchem
> $response
>   keyword_1 setting_1
>   keyword_2 setting_2
>   ...
>   [operator_1_label, operator_1_origin]
>   [operator_2_label, operator_2_origin]
>   [operator_3_label, operator_3_origin]
>   ...
> $end
> ```

其中的关键字与[第 10.14.2 节](subsec_responsemanJobControl.md)中列出的关键字相同（RESPONSE 除外）。

算符的指定写在由 `[]` 包裹的一行中，其中第一个元素是[表 10.4](#tab:responseman_operators) 中的标签，第二个元素是[表 10.5](#tab:responseman_origins) 中的标签。算符指定的出现顺序可以任意。响应值会针对算符及其分量的所有可能排列组合进行计算。

对于笛卡尔矩（Cartesian moment）算符，可以在 `[]` 内指定第三个字段作为展开的阶数，以 $(i,j,k)$ 的形式输入。例如,要求出原点位于 (0.2, 0.3, 0.4) a.u.、阶数为 (2, 5, 4) 的矩对分子的响应，可使用如下算符指定

> ```qchem
> [multipole, (0.2, 0.3, 0.4), (2, 5, 4)]
> ```

Table 10.4: 可用算符

| 算符标签 | 描述 | 积分 |
| --- | --- | --- |
| dipole 或 diplen | 电偶极矩（长度规范） | $\langle\chi_{\mu}\|\mathbf{r}_{O}\|\chi_{\nu}\rangle$ |
| quadrupole | 二阶矩（长度规范） | $\langle\chi_{\mu}\|\mathbf{r}\mathbf{r}^{T}\|\chi_{\nu}\rangle$ |
| multipole | 任意阶笛卡尔矩（长度规范） | $\langle\chi_{\mu}\|x^{i}y^{j}z^{k}\|\chi_{\nu}\rangle$ |
| fermi 或 fc | 费米接触（Fermi contact） | $\frac{4\pi g_{e}}{3}\langle\chi_{\mu}\|\delta(\mathbf{r}_{K})\|\chi_{\nu}\rangle$ |
| spindip 或 sd | 自旋偶极（spin dipole） | $\frac{g_{e}}{2}\langle\chi_{\mu}\|\frac{3\mathbf{r}_{K}\mathbf{r}_{K}^{T}-r_{K}^{2}}{r_{K}^{5}}\|\chi_{\nu}\rangle$ |
| angmom 或 dipmag | 角动量 | $\langle\chi_{\mu}\|\mathbf{L}_{O}\|\chi_{\nu}\rangle$ |
| dipvel | 电偶极矩（速度规范） | $\langle\chi_{\mu}\|\mathbf{\nabla}\|\chi_{\nu}\rangle$ |

Table 10.5: 可用算符原点

| 原点标签 | 描述 |
| --- | --- |
| zero | 笛卡尔原点，等同于 (0.0, 0.0, 0.0) |
| (x, y, z) | 任意点（双精度，单位为 bohr） |
