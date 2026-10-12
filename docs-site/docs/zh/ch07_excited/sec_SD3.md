---
title: "7.9.27 EOM-CCSD 与 CCSD 的非迭代三激发修正"
---

## 7.9.27 EOM-CCSD 与 CCSD 的非迭代三激发修正

（2026 年 7 月 4 日）

三激发对 EOM-CCSD 能量的影响可以通过微扰理论以经济高效的 ${\cal{O}}({N^{7}})$ 计算方案加以包含。以 EOM-CCSD 波函数作为零级波函数，第 $\mu$ 个 EOM-EE 或 SF 态的二阶三激发修正为：

<a id="Ch7.E123"></a>

$$
\Delta E^{(2)}_{\mu}=-\frac{1}{36}\sum_{i,j,k}\sum_{a,b,c}\frac{{\tilde{\sigma}_{ijk}^{abc}}(\mu){\sigma_{ijk}^{abc}}(\mu)}{D_{ijk}^{abc}-\omega_{\mu}} \tag{7.123}
$$

其中 $i,j$ 和 $k$ 表示占据轨道，$a,b$ 和 $c$ 为虚轨道指标。$\omega_{\mu}$ 是第 $\mu$ 个态的 EOM-CCSD 激发能。
量 $\tilde{\sigma}$ 和 $\sigma$ 定义为：

<a id="A3.S8.EGx59"></a>

$$
\displaystyle\tilde{\sigma}_{ijk}^{abc}(\mu) \tag{7.124}
$$

其中，$L$ 和 $R$ 分别是第 $\mu$ 个态的左本征矢和右本征矢。
分母 $D_{ijk}^{abc}$ 的两种不同选取方式分别定义了 (dT) 和 (fT) 修正变体。
在 (fT) 中，$D_{ijk}^{abc}$ 仅取 Hartree–Fock 轨道能之差。
更为精确（但并非完全轨道不变）的 (dT) 修正则采用 $\bar{H}$ 的完整三体对角元
$\langle\Phi_{ijk}^{abc}|(He^{(T_{1}+T_{2})})_{C}|\Phi_{ijk}^{abc}\rangle$
作为分母 $D_{ijk}^{abc}$。
对于参考态（*例如*，基态 CCSD 波函数），(fT) 和 (dT) 修正分别等价于
Piecuch 及其合作者提出的 CCSD(2)${}_{T}$ 和 CR-CCSD(T)${}_{L}$ 修正。[[1091]](../bib_references/bib.md#bib1136)

EOM-SF-CCSD(dT) 和 EOM-SF-CCSD(fT) 方法相较于 EOM-SF-CCSD 可带来系统性的改进，
将误差降至 1 kcal/mol 以下。理论背景和详细基准测试参见文献 [[887]](../bib_references/bib.md#bib921)。

类似的修正也适用于 EOM-IP-CCSD，[[888]](../bib_references/bib.md#bib922)
其中三激发对应于 $3h2p$ 激发；以及 EOM-EA-CCSD，其中三激发对应于 $2h3p$ 激发。

!!! note "注意"
    由于轨道非不变性问题，不建议使用 (dT) 修正。


!!! note "注意"
    EOM-IP-CCSD(fT) 修正现已在 CCMAN 和 CCMAN2 中均可用。


!!! note "注意"
    在 CCMAN2 中，三激发修正可使用两种不同的后端进行计算，
    即 **libtensor** 和 **libpt**。前者效率更高，推荐用于较大规模的计算任务（参见第 [6.13.3](../ch06_correlation/sec_dT.md) 节）。


## 7.9.27.1 非迭代三激发修正的任务控制

三激发修正可通过 METHOD 或 EOM_CORR 关键字请求：

### `METHOD`

> **指定计算方法。**
>
> * **类型**：`STRING`
> * **默认值**：`无默认值`
> * **选项**：
>     * EOM-CCSD(DT)
>     * EOM-CCSD(dT)，适用于 EE、SF 和 IP
>     * EOM-CCSD(FT)
>     * EOM-CCSD(fT)，适用于 EE、SF、IP 和 EA
>     * EOM-CCSD(ST)
>     * EOM-CCSD(sT)，适用于 IP
> * **建议**：无

### `EOM_CORR`

> **指定关联级别。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * SD(DT)
>     * EOM-CCSD(dT)，适用于 EE、SF 和 IP
>     * SD(FT)
>     * EOM-CCSD(fT)，适用于 EE、SF、IP 和 EA
>     * SD(ST)
>     * EOM-CCSD(sT)，适用于 IP
> * **建议**：无

!!! note "注意"
    在 CCMAN2 中，EOM-IP-CCSD(fT) 可在设置 USE_LIBPT = TRUE 或不设置的情况下计算。


## 7.9.27.2 示例

???+ example "示例 7.161: CH ${}^{+}$ 的 EOM-EE-CCSD(fT) 计算。"
    ```qchem
    $molecule
       1 1
       C
       H  C  1.13092
    $end
    
    $rem
       METHOD                 eom-ccsd(ft)
       BASIS                  general
       EE_STATES              [1,0,1,1]
       EOM_DAVIDSON_MAX_ITER  60  increase number of Davidson iterations
    $end
    
    $basis
     H   0
     S   3  1.00
           19.24060000         0.3282800000E-01
           2.899200000         0.2312080000
          0.6534000000         0.8172380000
     S   1  1.00
          0.1776000000          1.000000000
     S   1  1.00
          0.0250000000          1.000000000
     P   1  1.00
           1.00000000          1.00000000
     ****
     C   0
     S   6  1.00
           4232.610000         0.2029000000E-02
           634.8820000         0.1553500000E-01
           146.0970000         0.7541100000E-01
           42.49740000         0.2571210000
           14.18920000         0.5965550000
           1.966600000         0.2425170000
     S   1  1.00
           5.147700000          1.000000000
     S   1  1.00
          0.4962000000          1.000000000
     S   1  1.00
          0.1533000000          1.000000000
     S   1  1.00
          0.0150000000          1.000000000
     P   4  1.00
           18.15570000         0.1853400000E-01
           3.986400000         0.1154420000
           1.142900000         0.3862060000
          0.3594000000         0.6400890000
     P   1  1.00
          0.1146000000          1.000000000
     P   1  1.00
          0.0110000000          1.000000000
     D   1  1.00
          0.750000000          1.00000000
     ****
    $end
    ```

???+ example "示例 7.162: 卡宾（亚甲基）的 EOM-SF-CCSD(dT) 计算。"
    ```qchem
    $molecule
       0 3
       C
       H 1 CH
       H 1 CH 2 HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       METHOD            eom-ccsd(dt)
       BASIS             6-31G
       SF_STATES         [2,0,0,2]
       N_FROZEN_CORE     1
       N_FROZEN_VIRTUAL  1
       CCMAN2            false   !only works in ccman1
    $end
    ```

???+ example "示例 7.163: Mg 的 EOM-IP-CCSD(dT) 计算。"
    ```qchem
    $molecule
       0 1
       Mg    0.000000     0.000000    0.000000
    $end
    
    $rem
       N_FROZEN_CORE  1
       CORRELATION    ccsd
       EOM_CORR       sd(dt)
       BASIS          6-31g
       IP_STATES      [1,0,0,0,0,1,1,1]
       CCMAN2         false               NYI in ccman2
    $end
    ```
