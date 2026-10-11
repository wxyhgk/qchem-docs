---
title: "6.14.4 CCVB-SD"
---

## 6.14.4 CCVB-SD

（2026 年 7 月 4 日）

Small 博士（Dr. D. W. Small）与 Joonho Lee 在伯克利分校与 Head-Gordon 教授合作，开发并实现了一种新颖的单参考（single-reference）耦合簇（coupled-cluster）方法——包含单激发与双激发的 CCVB-SD。[[1276]](../bib_references/bib.md#bib1330)
 CCVB-SD
改进了一种较为粗糙的模型 CCVB（第 [6.19.3](subsec_CCVB.md) 节），可以视为对限制型 CCSD（RCCSD）的一种简单修正。CCVB-SD 继承了 CCVB 与 RCCSD 的良好性质：它是自旋纯的（spin-pure）、尺寸广延的（size-extensive），并且只要仅对价空间（valence space）进行关联处理，就能够断裂多重键。它是一个完整的双激发模型，因此计算标度为 $\mathcal{O}(N^{6})$。
然而，其能量在占据空间与虚空间内的旋转下保持不变，这使得它比 CCVB 更加黑箱化（black-box）。其能量函数如下

<a id="eq:ccvbsd"></a>
$$
E_{\mathrm{CCVB-SD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}}\right)\left|{\hat{H}}\right|\left(\exp\left({\hat{T}}\right)-\hat{\text{I}}_{\text{S}}\frac{\hat{Q}^{2}}{2}\right)\Phi_{0}}\right\rangle_{C} \tag{6.82}
$$

其中 $\hat{\text{I}}_{\text{S}}$ 是单重态投影算符（singlet projection operator），$\hat{Q}$ 是五重态双激发算符（quintet doubles operator）。与 QCCD 不同，CCVB-SD 改进的是右本征函数（right eigenfunction），而左本征函数（left eigenfunction）保持不变。式 ([6.82](#eq:ccvbsd)) 中的五重态项代表近似的连通四激发（connected quadruples），正是它负责描述强关联（strong correlation）。CCVB-SD 的计算开销仅为 RCCSD 的两倍，并且在强关联适用性上优于 QCCD/VQCCD——就大多数多重键断裂而言，本方法在解离极限（dissociation limits）处变为精确的，而 QCCD 除特殊情形外做不到这一点。

尽管 CCVB-SD 可以在没有活性空间（active space）约束的情况下使用，但我们建议用户一般结合价活性空间（valence active space）来使用它。出于基准测试（benchmarking）目的，使用最小基组（minimal basis）会自动给出正确的价空间，同时冻结芯层（frozen cores）。CCVB-SD 的能量及核梯度（nuclear gradients）均可通过 CCMAN2 获得。

需要注意的是，目前 CCVB-SD 尚未实现轨道优化（orbital optimization）。这意味着使用大于最小基组的基组时，需要选择合适的价轨道。因此，我们建议用户先运行 GVB-PP（或 CCVB）以获取初始轨道。轨道优化（*即* CCVB-OD）即将实现，届时运行 CCVB-OD 将比 CCVB-SD 更加黑箱化，因为它无需选取合适的价空间轨道。

此外，目前 CCVB-SD 只能应用于闭壳层（closed-shell）分子。将其推广到开壳层（open-shell）分子的工作正在开发之中。

???+ example "示例 6.47: 苯在最小基组下的 CCVB-SD 力计算。"
    ```qchem
    $comment
    CCVB-SD job for benzene computing energy+gradients.
    It will also print out natural orbital occupation numbers (NOONs)
    $end
    
    $molecule
       0 1
       C    0.000000    0.698200    0.000000
       C    0.000000   -0.698200    0.000000
       C    1.209318    1.396400    0.000000
       C    1.209318   -1.396400    0.000000
       C    2.418636    0.698200    0.000000
       C    2.418636   -0.698200    0.000000
       H   -0.931410    1.235950    0.000000
       H   -0.931410   -1.235950    0.000000
       H    1.209318    2.471900    0.000000
       H    1.209318   -2.471900    0.000000
       H    3.350046    1.235950    0.000000
       H    3.350046   -1.235950    0.000000
    $end
    
    $rem
       JOBTYPE           force
       BASIS             sto-3g
       METHOD            ccvbsd
       THRESH            14
       SCF_ALGORITHM     gdm
       SCF_CONVERGENCE   10
       CC_REF_PROP       true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    ```
