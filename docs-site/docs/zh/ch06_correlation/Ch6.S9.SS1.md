---
title: "6.9.1 引言"
---

## 6.9.1 引言

（2026 年 7 月 4 日）

最大物理正则化（Maximum Physical Regularisation, MPR）既可以理解为尺寸一致的 Brillouin-Wigner 理论（size-consistent Brillouin-Wigner theory, BW-s2）的推广，也可以理解为 Møller-Plesset 微扰理论（Møller-Plesset perturbation theory, MP2）的推广。在这两种理论框架中，它都向未微扰哈密顿量（unperturbed Hamiltonian）中引入了额外的项，使用户能够以更高的参数精度来调控基态性质与基态能量。MPR-BWs(2) 中的二阶能量由一个表面上与 MP2 和 BW-s2 都颇为相似的方程给出：

<a id="Ch6.E39"></a>
$$
E_{\text{c}}^{(2)}=\frac{1}{4}\sum\limits_{ijab}\langle ab||ij\rangle{t^{ab}_{ij}}^{(1)} \tag{6.39}
$$

其中一阶振幅 ${t^{ab}_{ij}}^{(1)}$ 由其线性振幅方程（linear amplitude equation）确定。与 BW-s2 高度类似，MPR-BWs2 包含两个矩阵 $W_{ij}$ 和 $W_{ab}$，它们对未微扰基态的物理描述进行补充与重塑。MPR-BWs2 的振幅方程为：

<a id="Ch6.E40"></a>
$$
\sum\limits_{c}\big{(}(f_{ac}+W_{ac}){t^{cb}_{ij}}^{(1)}+(f_{cb}+W_{cb}){t^{ac}_{ij}}^{(1)}\big{)}-\sum\limits_{k}\big{(}(f_{ik}+W_{ik}){t^{ab}_{kj}}^{(1)}+(f_{kj}+W_{kj}){t^{ab}_{ik}}^{(1)}\big{)}+\langle ij||ab\rangle=0 \tag{6.40}
$$

MPR-BWs2、BW-s2 与 MP2 之间的核心区别在于 $W_{ab}$ 和 $W_{ij}$ 的定义。MPR-BWs2 的占据（occupied）块包含五个不同的贡献项。第一项（$A_{0}$）与 BW-s2 完全相同，其特点是取迹后等于二阶能量乘以 $A_{0}$：

<a id="Ch6.E41"></a>
$$
W_{ij}\leftarrow\frac{A_{0}}{8}\big{(}{t^{ab}_{ik}}^{(1)}\langle ab||jk\rangle+{t^{ab}_{jk}}^{(1)}\langle ab||ik\rangle\big{)} \tag{6.41}
$$

类似地，第二项（$A_{1}$）取迹后等于二阶关联能（second order correlation energy）的反平行自旋（opposite-spin）部分，用空间轨道（spatial orbitals）表示时最为简洁：

<a id="Ch6.E42"></a>
$$
W_{ij}\leftarrow\frac{A_{1}}{2}\big{(}{t^{a\overline{b}}_{i\overline{k}}}^{(1)}(ia|\overline{kb})+{t^{a\overline{b}}_{j\overline{k}}}^{(1)}(ja|\overline{kb})\big{)} \tag{6.42}
$$

其余的占据项包含伪密度矩阵（pseudo-density matrices）$\rho_{ij}$ 和 $\rho_{ab}$，其定义与 MP2 中的类似，但与真正的二阶 MPR-BWs2 密度矩阵（density matrix）存在显著差异：

<a id="Ch6.E43"></a>
$$
\rho_{ij}=-\frac{1}{2}{t^{ab}_{ik}}^{(1)}{t^{ab}_{jk}}^{(1)} \tag{6.43}
$$

<a id="Ch6.E44"></a>
$$
\rho_{ab}=\frac{1}{2}{t^{ac}_{ij}}^{(1)}{t^{bc}_{ij}}^{(1)} \tag{6.44}
$$

$A_{2}$ 和 $A_{3}$ 项构造如下：

<a id="Ch6.E45"></a>
$$
W_{ij}\leftarrow A_{2}\langle ik||jl\rangle\rho_{kl}+A_{3}\langle ia||jb\rangle\rho_{ab} \tag{6.45}
$$

最后是 $A_{4}$ 项，由与 Fock 矩阵（Fock matrix）的对称缩并给出：

<a id="Ch6.E46"></a>
$$
W_{ij}\leftarrow\frac{A_{4}}{2}\big{(}f_{ik}\rho_{kj}+f_{jk}\rho_{ki}\big{)} \tag{6.46}
$$

虚轨道（virtual）参数以其对应的占据参数来命名，因此 $B_{0}$ 和 $B_{1}$ 参数为：

<a id="Ch6.E47"></a>
$$
W_{ab}\leftarrow\frac{B_{0}}{8}\big{(}{t^{ac}_{ij}}^{(1)}\langle bc||ij\rangle+{t^{bc}_{ij}}^{(1)}\langle ac||ij\rangle\big{)} \tag{6.47}
$$

<a id="Ch6.E48"></a>
$$
W_{ab}\leftarrow\frac{B_{1}}{2}\big{(}{t^{a\overline{c}}_{i\overline{j}}}^{(1)}(ib|\overline{jc})+{t^{b\overline{c}}_{i\overline{j}}}^{(1)}(ia|\overline{jc}) \tag{6.48}
$$

$B_{2}$ 参数本应将 $\rho_{ab}$ 缩并进 $W_{ab}$，但被有意地不予实现，因为其计算过程中包含一个 $O(V^{4})$ 量级的步骤，其中 $V$ 为虚轨道数目。$B_{3}$ 和 $B_{4}$ 项为：

<a id="Ch6.E49"></a>
$$
W_{ab}\leftarrow B_{3}\langle ai||bj\rangle\rho_{ij} \tag{6.49}
$$

<a id="Ch6.E50"></a>
$$
W_{ab}\leftarrow\frac{B_{4}}{2}\big{(}f_{ac}\rho_{cb}+f_{bc}\rho_{ca}\big{)} \tag{6.50}
$$

关于这些参数及其各自项的物理诠释，参见文献 [[335]](../bib_references/bib.md#bib339)
。

由于对振幅具有二次依赖关系的项随后会将振幅方程变为一个三次张量方程（cubic tensor equation），因此第 [6.8](topic_bws2.md) 节所描述的自洽（self-consistent）构造方案的收敛有时难以实现，甚至无法收敛。有鉴于此，对每个参数的效应采用非迭代（non-iterative）方式近似处理往往是最佳选择。从 Hylleraas 泛函（Hylleraas functional）可以看出，二阶关联能可以重写为：

<a id="Ch6.E51"></a>
$$
E^{(2)}_{\text{c}}=-\sum\limits_{pq}P^{(2)}_{pq}(f_{pq}+W_{pq}) \tag{6.51}
$$

其中 $P^{(2)}_{pq}$ 表示精确的二阶密度矩阵。将 $P^{(2)}_{ij}$ 替换为 $\rho_{ij}$、将 $P^{(2)}_{ab}$ 替换为 $\rho_{ab}$，并减去迭代贡献项，即定义了非迭代近似：

<a id="Ch6.E52"></a>
$$
E^{(2)}_{\text{c},\>\text{noniter}}=\sum\limits_{ij}\rho_{ij}W^{\text{noniter}}_{ij}-\sum\limits_{ab}\rho_{ab}W^{\text{noniter}}_{ab} \tag{6.52}
$$
