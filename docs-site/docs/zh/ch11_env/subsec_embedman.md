---
title: "11.6.5 基于「EmbedMan」的先前实现"
---

## 11.6.5 基于「EmbedMan」的先前实现

（2026 年 7 月 4 日）

**Q-Chem** 中基于投影的嵌入（projection-based embedding）最初是通过「EmbedMan」模块实现的，该模块基于旧的 SCF 模块，而该模块已不再是默认选项。
此实现对 Fock 矩阵施加了一个能级移动投影算符（level-shift projection operator），以强制属于片段 1 和片段 2 的轨道之间的正交性。
对于 1-in-2 情形，Fock 矩阵可写为

<a id="eq:des_fock"></a>

$$
\mathbf{f}^{(1)}=\mathbf{h}+\mathbf{J}[\gamma^{(1)}+\gamma^{(2)}]+\nu_{xc}[\gamma^{(1)}+\gamma^{(2)}]+\mu\mathbf{P}^{(2)} \tag{11.120}
$$

其中 $\mathbf{P}^{(2)}$ 是能级移动投影算符，其构造方式为：

<a id="eq:des_proj"></a>

$$
\mathbf{P}^{(2)}_{\alpha\beta}=[\mathbf{S}\gamma^{(2)}\mathbf{S}]_{\alpha\beta} \tag{11.121}
$$

其中 $\gamma^{(2)}$ 是片段 2 的局域化密度（localized density），$\mathbf{S}$
是 AO 重叠矩阵。收敛后，会在最终能量上添加一个能量修正项，以考虑能级移动投影算符对 Fock 矩阵能量的贡献。修正项的计算方式如下：

<a id="eq:des_corr"></a>

$$
E_{\mathrm{correction}}=\mu*\mathrm{tr}(\gamma^{(1)}\mathbf{P}^{(2)}) \tag{11.122}
$$

一旦计算出片段 1-in-2 的 KS-DFT 能量，即可对该收敛密度施加 post-SCF 方法，以获得片段 1 的高级别 QM 加和能量（additive energy）。
同样的程序可对片段 2-in-1 重复执行，但不继续施加 post-SCF 方法，从而得到片段 2 的低级别 QM 加和能量。然后将这些能量求和得到总能量。

要通过「EmbedMan」模块运行嵌入计算，须将超分子体系拆分为编号为 1 和 2 的两个片段，并将
EMBEDMAN 设为 1。这是通过标准的 **Q-Chem** 片段输入语法完成的。
需要运行两个独立的作业来求得在高级别 QM 理论下片段 1-in-2 的能量，以及在低级别 QM 理论下片段 2-in-1 的能量。
*$molecule* 部分中片段的顺序决定了哪个片段将经过高级别 QM 计算。
用户须单独提交一个作业来进行 2-in-1 的低级别 QM 计算，其中片段顺序颠倒，并将 EMBED_THEORY 设为 0（即默认值）。
然后将各计算的最终能量相加，以确定总的 QM/QM 嵌入能量。

对于当前 **Q-Chem** 的密度嵌入（density embedding）实现，需要将基组指定为 MIXED，这要求为每个原子分别定义基组。
使用 CCSD(T) 时，应将 CCMAN2 指定为 TRUE，以调用 **Q-Chem** 最新的耦合簇代码。
当前密度嵌入实现仅可与以下设置组合使用：SCF_ALGORITHM = DIIS、INCFOCK = 0
以及 PURECART = 222。
还建议用户禁用对称性，即设置 INTEGRAL_SYMMETRY =
FALSE 和 POINT_GROUP_SYMMETRY = FALSE。请参阅示例输入以获取正确的作业设置。

### `EMBEDMAN`

> **开启密度嵌入功能。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不使用密度嵌入。
>     * 1
>     * 开启密度嵌入。
> * **推荐设置**：用于 QM/QM 密度嵌入计算。

### `EMBED_THEORY`

> **指定对片段 1 执行的 post-DFT 方法。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不使用 post-HF 方法，仅对片段 1 进行 DFT 计算。
>     * 1
>     * 对片段 1 执行 CCSD(T) 计算。
>     * 2
>     * 对片段 1 执行 MP2 计算。
> * **推荐设置**：对于片段 1-in-2 的高级别 QM 计算，此项应设为 1 或 2；对于片段 2-in-1 的低级别 QM 计算，应设为 0。

### `EMBED_MU`

> **指定投影算符缩放因子 $\mu$ 的指数值 [式 ( 11.120 ) 和 ( 11.122 )]。**
>
> * **类型**：`INTEGER`
> * **默认值**：`7`
> * **选项**：
>     * n
>     * $\mu=10^{n}$
>     * .
> * **推荐设置**：推荐使用 2 - 7 范围内的值。$\mu$ 值越大，片段分子轨道（MO）的正交性越好，但 $\mu>10^{7}$ 会引入数值噪声。$\mu<10^{2}$ 会导致非加和项（non-additive terms）过大。在 $10^{2}-10^{7}$ 范围内，能量修正对 $\mu$ 的变化相当不敏感。

### `EMBED_THRESH`

> **指定用于确定哪些 MO 属于哪些片段的 AO 贡献阈值截断值**
>
> * **类型**：`INTEGER`
> * **默认值**：`500`
> * **选项**：
>     * n
>     * 阈值
>     * $=n/1000$
> * **推荐设置**：可接受的值范围为 0 到 1000。仅当分子轨道（MO）局域化程度不高时才需要调整此参数。

???+ example "示例 11.11.47：He-in-HF 的 MP2/PBE 密度嵌入计算输入。两个作业的总最终能量之和即为 QM/QM 总能量。"
    ```qchem
    $comment
    2023/4/5 use core guess becuase autosad and sad do not work with basis mixed
    $end
    
    $molecule
       0 1
    --
       0 1
       He      -4.63032        2.10289       -1.62399
    --
       0 1
       F       -8.00612        1.74605       -1.25581
       H       -7.40964        1.84462       -0.47756
    $end
    
    $rem
       EXCHANGE        PBE
       CORRELATION     PBE
       BASIS           mixed  ! Must specify basis sets per atom in $basis section below
       PURECART        222
       MAX_SCF_CYCLES  100
       SCF_ALGORITHM   DIIS
       INCFOCK         0
       CC_SYMMETRY     false
       EMBEDMAN        1      ! Turning density embedding on
       EMBED_THEORY    2      ! Running MP2 on fragment 1 in 2, or He in FH
       EMBED_MU        7      ! Default value
       EMBED_THRESH    500    ! Default value for assigning MOs to fragments
       SCF_GUESS       CORE
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $basis
      he 1
      6-31G
      ****
      f 2
      6-31G
      ****
      h 3
      6-31G
      ****
    $end
    
    @@@
    
    $molecule
    0 1
    --
    0 1
       F       -8.00612        1.74605       -1.25581
       H       -7.40964        1.84462       -0.47756
    --
    0 1
       He      -4.63032        2.10289       -1.62399
    $end
    
    $rem
      EXCHANGE        PBE
      CORRELATION     PBE
      BASIS           mixed
      PURECART        222
      MAXSCF          100
      SCF_ALGORITHM   DIIS
      INCFOCK         0
      EMBEDMAN        1
      EMBED_THEORY    0      ! There will be no post-DFT calculations for HF-in-He
      SCF_GUESS       core
      INTEGRAL_SYMMETRY    false
      POINT_GROUP_SYMMETRY false
    $end
    
    $basis
      f 1
      6-31G
      ****
      h 2
      6-31G
      ****
      he 3
      6-31G
      ****
    $end
    ```
