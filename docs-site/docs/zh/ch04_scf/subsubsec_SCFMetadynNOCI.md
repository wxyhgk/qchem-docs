---
title: "4.9.3 非正交 CI 的多个 SCF 解"
---

## 4.9.3 非正交 CI 的多个 SCF 解

(July 4, 2026)

通过元动力学（metadynamics）找到的解通常是对非绝热（diabatic）势能面的良好近似，在这些势能面上，电子结构随几何构型的变化并不显著。当存在多个能量相近的电子态时，可以通过对这些态构成的矩阵进行对角化来得到绝热态，*即*通过组态相互作用（Configuration Interaction, CI） procedure。由于它们是 SCF 方程的不同解，这些态是非正交的（*即*其中一个无法由另一个的轨道构成的单个行列式得到），因此 CI 会稍复杂一些，对应于非正交 CI（Non-Orthogonal CI, NOCI）。有关 NOCI 的更多信息参见第 [7.5](../ch07_excited/subsec_NOCI.md) 节。

**Q-Chem** 5.2 版本引入了一个新的 NOCI 程序包 **libnoci**，用于定位多个 SCF 解并运行 NOCI 计算（见第 [7.5.2](../ch07_excited/subsec_LIBNOCI.md) 节），其中包括 SCF 元动力学的全新实现。**libnoci** 对 SCF 元动力学的实现可通过 USE_LIBNOCI = TRUE 结合 NOCI_DETGEN = 3 来使用。除了 **Q-Chem** 中原有的 SCF 元动力学功能之外，这一新实现还包括：

- 一种活性空间（active space）方法，其中轨道混合与优化仅在用户定义的轨道子集中进行。
- 对限制（restricted）、非限制（unrestricted）以及广义（generalized）轨道类型的完整支持，同时支持复（Hermite）轨道与全纯（非 Hermite）轨道；见第 [4.9.4](sec_HoloHF.md) 节。

对于 NOCI 特别相关的多个 Hartree-Fock 态，通常源于在占主导地位的分子轨道子集中改变轨道占据数。例如，重要的多个解可能对应于其轨道在 SCF 级别上分别弛豫过的激发行列式，或由主导活性空间中的强混合形成的对称性破缺态。**libnoci** 允许仅在用 *$active_orbitals* 输入段所定义的轨道子集中进行轨道混合与弛豫，从而识别出多个解。
默认情况下，所定位到的多个解随后会在完整的轨道空间中进一步优化，不过可以使用 SKIP_SCFMAN = TRUE 跳过这一步。

最后，**libnoci** 让从先前计算中读取初始猜测（initial guess）的控制更加便捷。使用输入项 NOCI_REFGEN = 1 可以从文件中读取所有先前的解（如果可用），而通过 SCF_READMINIMA 则可以选择特定的子集。

???+ example "示例 4.29: 使用 libnoci 实现的 SCF 元动力学示例。"
    ```qchem
    $molecule
       0 1
       H    0.0000000   0.0000000   0.0000000
       H    0.0000000   0.0000000   4.0000000
    $end
    
    $rem
       METHOD                     hf
       UNRESTRICTED               true
       BASIS                      sto-3g
       SCF_CONVERGENCE            10
       MAX_SCF_CYCLES             1000
       MOM_START                  1
       USE_LIBNOCI                true
       NOCI_DETGEN                3
       SCF_SAVEMINIMA             4
       SCF_MINFIND_RANDOMMIXING   30000
       SCF_MINFIND_MIXMETHOD      1
    $end
    ```

在 **libnoci** 中可以为 SCF 元动力学指定活性轨道。
$\beta$ 轨道的索引以 $\alpha$ 分子轨道（MO）的数目为偏移量，*即*
该示例选取了 $\alpha$ 轨道 1 和 2，以及 $\beta$ 轨道 1 和 2，其中共有 10 个 $\alpha$ 分子轨道（包括占据轨道和虚轨道）。

> > ```qchem
> > $active_orbitals
> >     1 2 11 12
> > $end
> > ```

初始猜测系数也可以按如下方式读入：

> > ```qchem
> > $scf_read
> >     1 2 4 ...
> > $end
> > ```
