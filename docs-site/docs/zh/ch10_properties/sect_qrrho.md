---
title: "10.8.3 低频振动模式的处理"
---

## 10.8.3 低频振动模式的处理

（2026 年 7 月 4 日）

低频振动模式通常源于分子内围绕单键的受阻旋转或近自由旋转。对于此类内部旋转，谐振子近似存在问题：当频率趋于零时，它会给出无限大的振动熵 $S_{\mathrm{vib}}$。

为解决这一问题，Grimme[[496]](../bib_references/bib.md#bib507)
提出通过在自由转子熵 $S_{\mathrm{FR}}$ 与谐振子振动熵 $S_{\mathrm{HO}}$ 之间进行插值，来强制给出有限的振动熵，即

<a id="eq:Grimme_interpolation"></a>
$$
S_{\mathrm{vib}}(\nu_{i})=\big{(}1-\omega(\nu_{i})\big{)}S_{\mathrm{FR}}(\nu_{i})+\omega(\nu_{i})S_{\mathrm{HO}}(\nu_{i}), \tag{10.71}
$$

其中

<a id="eq:Chai_MHG_interpolator"></a>
$$
\omega(\nu_{i})=\frac{1}{1+(\nu_{0}/\nu_{i})^{\alpha}} \tag{10.72}
$$

是 Chai 和 Head-Gordon 提出的阻尼函数，[[224]](../bib_references/bib.md#bib219)

其中 $\alpha$ 和 $\nu_{0}$ 为固定参数。
该函数被用作权重函数，可实现从低频下的自由转子熵到频率 $\nu_{i}$ 高于截断值 $\nu_{0}$ 时的谐振子振动熵的平滑过渡。
后来该方法被进一步扩展，用于在自由转子 $H_{\mathrm{FR}}$ 与包含零点振动能
$H_{\mathrm{ZPVE}}$ 的谐振子 $H_{\mathrm{HO}}$ 之间对振动焓贡献进行插值，如[[822]](../bib_references/bib.md#bib853)

<a id="eq:MHG_interpolation"></a>
$$
H_{\mathrm{vib}}(\nu_{i})=\big{[}1-\omega(\nu_{i})\big{]}H_{\mathrm{FR}}(\nu_{i})+\omega(\nu_{i})\big{[}H_{\mathrm{HO}}(\nu_{i})+H_{\mathrm{ZPVE}}(\nu_{i})\big{]}\;. \tag{10.73}
$$

这同样减小了将平动和转动自由度当作低频振动来处理所带来的误差，对于较大分子的吸附或缔合过程尤其重要。
该处理方式被称为准刚性转子-谐振子（quasi-rigid-rotor-harmonic-oscillator，qRRHO）方法。

qRRHO 方案是 **Q-Chem** 中的默认设置，所有热力学量都会分别在标准温度和压力（298.15 K
和 1.00 atm）下按 RRHO（不进行插值）和 qRRHO 方案输出。若要更改后者，用户可以指定一个 *$isotopes* 段（详见示例及第 [10.8.2](ex_Isotope-Mass.md) 节）。两个插值函数所使用的 $\alpha$ 和 $\omega_{0}$ 可分别通过 QRRHO_ALPHA 和 QRRHO_OMEGA_CUTOFF 进行修改。

QRRHO_ALPHA

### `QRRHO_ALPHA`

> **指定 Chai 和 Head-Gordon 阻尼函数中的指数，用于在 qRRHO 方案中对振动焓和熵进行插值。若要单独更改熵插值的指数，请指定 MRRHO_ALPHA。**
>
> * **类型**：`INTEGER`
> * **默认值**：`4`
> * **选项**：
>     * $\alpha$
>     * qRRHO 方案中使用的无量纲插值指数。
> * **建议**：使用默认值。

QRRHO_OMEGA_CUTOFF

### `QRRHO_OMEGA_CUTOFF`

> **设置 Chai-Head-Gordon 阻尼函数中的频率截断值，用于在 qRRHO 方案中对振动焓和熵进行插值。若要单独更改熵插值的频率截断值，请指定 MRRHO_OMEGA_CUTOFF。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $\omega_{0}$
>     * qRRHO 方案中使用的插值截断频率，单位为 cm
>     * ${}^{-1}$
>     * 。
> * **建议**：使用默认值。

???+ example "示例 10.41：在 HF/3-21G 理论水平上进行谐振子振动分析，其中 RRHO 和
qRRHO 的热力学性质在 298.15 K 和 1.00 atm 下输出。"
    ```qchem
    $molecule
    0 1
    C     1.682185104800      0.240320237000      0.000000000000
    O     0.894276382600      1.089998584000      0.000000000000
    O     2.480949717100     -0.590833069200      0.000000000000
    C    -1.682185094800     -0.240320333400      0.000000000000
    O    -0.894276273900     -1.089998812500      0.000000000000
    O    -2.480949835800      0.590833394100      0.000000000000
    $end
    
    $rem
    JOBTYPE         opt
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    JOBTYPE         freq
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 10.42：在 HF/3-21G 理论水平上进行谐振子振动分析，其中 RRHO 和
qRRHO 的热力学性质在标准温度和压力以及两个附加温度（273.15 K 和 313.15 K）下输出。
关于 $isotopes 段的更多细节，请参见第 10.8.2 节。"
    ```qchem
    $molecule
    0 1
    C     1.682185104800      0.240320237000      0.000000000000
    O     0.894276382600      1.089998584000      0.000000000000
    O     2.480949717100     -0.590833069200      0.000000000000
    C    -1.682185094800     -0.240320333400      0.000000000000
    O    -0.894276273900     -1.089998812500      0.000000000000
    O    -2.480949835800      0.590833394100      0.000000000000
    $end
    
    $rem
    JOBTYPE         opt
    METHOD          hf
    BASIS           3-21G
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    JOBTYPE         freq
    METHOD          hf
    BASIS           3-21G
    ISOTOPES        true
    INTEGRAL_SYMMETRY    false
    POINT_GROUP_SYMMETRY false
    $end
    
    $isotopes
    2 1
    0 273.15 1.0
    0 313.15 1.0
    $end
    ```
