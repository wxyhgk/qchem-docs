---
title: "9.11.3 CAP-AIMD 任务控制与示例"
---

## 9.11.3 CAP-AIMD 任务控制与示例

(July 4, 2026)

若要运行 CAP-AIMD（复吸收势 - 从头算分子动力学）模拟，必须设置以下三项：

- •

JOBTYPE = AIMD，位于 *$rem* 中，
- •

COMPLEX_CCMAN = TRUE，位于 *$rem* 中（参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节），以及
- •

CS_HF = 1，位于 *$complex_ccman* 中（参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）。

目前，CAP-AIMD 模拟仅可使用长方体（cuboid）类型的 CAP，因此还需要在 *$complex_ccman* 区段中设置 CAP_TYPE = 1（参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）。

进行 CAP-AIMD 模拟时，除 [9.9.2](sub_aimd_jobcontrol.md) 节所述内容外，还会在 AIMD 目录中生成两个额外文件：

- •

`CAP_EComponents`：记录每一步的总复数能量、经 CAP 修正的总复数能量，以及 CAP 对总复数能量贡献的实部与虚部——全部以原子单位（a.u.）计。
- •

`CAP_PositionAndWidth`：记录每一步的总复数能量（以 a.u. 计）以及共振宽度（以电子伏特 eV 计）。

CAP_AIMD_SWITCH

### `CAP_AIMD_SWITCH`

> **当最后一个 alpha 占据轨道能量的实部为负时，在 CAP-AIMD 模拟过程中将 CAP_ETA 置为零**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 当最后一个 alpha 占据轨道能量的实部变为负值时，将
>     * CAP_ETA
>     * 置为零。
>     * FALSE
>     * 在整个模拟过程中保持用户设定的
>     * CAP_ETA
>     * 恒定不变。
> * **建议**: 使用默认值。

CS_STRICT

### `CS_STRICT`

> **通过在适用时读取复密度矩阵或复分子轨道系数文件，为 CAP-HF 计算确定 Mulliken 电荷、多极矩和复轨道能量**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 通过在适用时读取——复密度矩阵或复分子轨道系数文件，为 CAP-HF 计算确定 Mulliken 电荷、多极矩和复轨道能量。
>     * FALSE
>     * 在为 CAP-HF 计算确定 Mulliken 电荷、多极矩和轨道能量时，不读取复密度矩阵或复分子轨道系数文件。
> * **建议**: 对于 CAP-HF 计算设为 'TRUE'。

SKIP_OLD_SCFMAN

### `SKIP_OLD_SCFMAN`

> **仅跳过旧的 SCF 驱动模块**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 仅
>     * 跳过旧的 SCF 驱动模块
>     * FALSE
>     * 不跳过旧的 SCF 驱动模块
> * **建议**: 在对临时阴离子（temporary anions）执行 CAP 计算时，将此变量设为 FALSE 可能有所帮助。

CS_SCF_FINAL_PRINT

### `CS_SCF_FINAL_PRINT`

> **控制 CAP-SCF 过程的输出详细程度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * 打印 CAP-SCF 能量的直接分解结果。
>     * 2
>     * 基于复系数矩阵打印 CAP-SCF 能量的分解结果。
>     * 若请求以下选项，此项也为必需。
>     * 3
>     * 级别 2 加上复轨道能量矩阵
>     * F
>     * 的对角元。由级别 2 触发。
>     * 4
>     * 级别 2 加上复动能矩阵
>     * T
>     * 的对角元。由级别 2 触发
>     * 5
>     * 级别 2 加上复电子-核库仑势能矩阵
>     * V
>     * 的对角元。由级别 2 触发。
>     * 6
>     * 级别 2 加上 CAP 矩阵
>     * W
>     * 的对角元。由级别 2 触发。
>     * 7
>     * 级别 2 加上复单电子总能量矩阵
>     * $\textbf{T}+\textbf{V}+\textbf{W}$
>     * 的对角元。由级别 2 触发。
>     * 8
>     * 级别 2 加上复电子总能量矩阵
>     * $\textbf{T}+\textbf{V}+\textbf{W}+\textbf{F}$
>     * 的对角元。由级别 2 触发。
>     * 9
>     * 级别 2 至 8。由级别 2 触发。
> * **建议**: 通常级别 1 就足够了。该 $rem 变量的值会先被转换为一组互不相同的取值；因此，例如 "1111" 等价于 "1"，而 "28224" 等价于 "248"。若请求级别 3–9，请记得同时请求级别 2。

???+ example "示例 9.9.49: N ${}_{2}^{-}$ 的 CAP-HF 单点计算，含复数能量的能量分解。基组为 cc-PVTZ+3p。"
    ```qchem
    $molecule
    -1 2
    N
    N   1  1.098
    $end
    
    $rem
    ¯JOBTYPE¯¯SP
    ¯METHOD¯¯¯hf
    ¯BASIS¯¯¯general
    ¯GEN_SCFMAN¯¯TRUE
    ¯SKIP_OLD_SCFMAN¯true¯! skip old scfman drivers
    ¯SCF_CONVERGENCE¯8
    ¯SCF_GUESS¯¯CORE
    ¯COMPLEX_CCMAN¯¯TRUE
    ¯UNRESTRICTED¯¯TRUE
    ¯CS_STRICT¯¯TRUE¯! Determine orbital energies and props. using the complex density matrix/complex MO coefficients
    ¯CS_SCF_FINAL_PRINT¯1111¯! Print summary of energy decomposition
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1
    ¯CAP_TYPE ¯¯1
    ¯CAP_ETA ¯¯420
    ¯CAP_X ¯¯¯3535
    ¯CAP_Y ¯¯¯3535
    ¯CAP_Z ¯¯¯8102
    $end
    
    $basis
    N     0
    S    7   1.00
      11420.                     0.00052898
       1712.                     0.00409115
        389.3                    0.02101161
        110.0                    0.08163835
         35.57                   0.23564992
         12.54                   0.43792615
          4.644                  0.35006007
    S    7   1.00
      11420.                     0.00000185
       1712.                     0.00000699
        110.0                   -0.00073647
         35.57                  -0.00718168
         12.54                  -0.04679022
          4.644                 -0.12512392
          0.5118                 0.78627029
    S    1   1.00
          1.293                  1.000000
    S    1   1.00
          0.1787                 1.000000
    P    3   1.00
         26.63                   0.014670
          5.948                  0.091764
          1.742                  0.298683
    P    1   1.00
          0.5550                 1.000000
    P    1   1.00
          0.1725                 1.000000
    D    1   1.00
          1.654                  1.000000
    D    1   1.00
          0.469                  1.000000
    F    1   1.00
          1.093                  1.000000
    ¯P    1   1.00
    ¯¯0.08625       1.000000
          ¯P    1   1.00
          ¯¯0.043125      1.000000
          ¯P    1   1.00
          ¯¯0.0215625     1.000000
    ****
    $end
    ```

???+ example "示例 9.9.50: N ${}_{2}^{-}$ 的 CAP-AIMD 模拟。基组为 cc-PVTZ+3p。"
    ```qchem
    $molecule
    -1 2
    N
    N   1  1.098
    $end
    
    
    $rem
     JOBTYPE¯¯AIMD
     METHOD¯¯¯HF
     BASIS¯¯¯GENERAL
     GEN_SCFMAN¯¯TRUE
     SKIP_OLD_SCFMAN¯TRUE¯¯! Skip old scfman drivers
     SCF_CONVERGENCE¯8
     MAX_SCF_CYCLES¯¯200
     SCF_GUESS¯¯CORE
     COMPLEX_CCMAN¯¯TRUE¯¯! Activate Complex CCMAN. Necessary for CAP calculations.
     UNRESTRICTED¯¯TRUE
     TIME_STEP¯¯10
     AIMD_STEPS¯¯200
     FOCK_EXTRAP_ORDER      0
     FOCK_EXTRAP_POINTS     0
     AIMD_MOMENTS¯¯1
     AIMD_TEMP¯¯300
     AIMD_INIT_VELOC¯THERMAL
     CAP_AIMD_SWITCH¯TRUE¯¯! Set CAP_ETA=0 when extra electron is bound
     CS_STRICT¯¯TRUE¯¯! Determine orbital energies and props. using the complex density. matrix/complex MO coefficients
     INTEGRAL_SYMMETRY      FALSE
     POINT_GROUP_SYMMETRY   FALSE
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1¯¯! Do complex HF
    ¯CAP_TYPE ¯¯1¯¯! CAP type is cuboid.
    ¯CAP_ETA ¯¯420
    ¯CAP_X ¯¯¯3535
    ¯CAP_Y ¯¯¯3535
    ¯CAP_Z ¯¯¯8102
    $end
    
    $basis
    N     0
    S    7   1.00
      11420.                     0.00052898
       1712.                     0.00409115
        389.3                    0.02101161
        110.0                    0.08163835
         35.57                   0.23564992
         12.54                   0.43792615
          4.644                  0.35006007
    S    7   1.00
      11420.                     0.00000185
       1712.                     0.00000699
        110.0                   -0.00073647
         35.57                  -0.00718168
         12.54                  -0.04679022
          4.644                 -0.12512392
          0.5118                 0.78627029
    S    1   1.00
          1.293                  1.000000
    S    1   1.00
          0.1787                 1.000000
    P    3   1.00
         26.63                   0.014670
          5.948                  0.091764
          1.742                  0.298683
    P    1   1.00
          0.5550                 1.000000
    P    1   1.00
          0.1725                 1.000000
    D    1   1.00
          1.654                  1.000000
    D    1   1.00
          0.469                  1.000000
    F    1   1.00
          1.093                  1.000000
    ¯P    1   1.00
    ¯¯0.08625       1.000000
          ¯P    1   1.00
          ¯¯0.043125      1.000000
          ¯P    1   1.00
          ¯¯0.0215625     1.000000
    ****
    $end
    ```

???+ example "示例 9.9.51: C ${}_{2}$ H ${}_{4}^{-}$ 的 CAP-AIMD 模拟。基组为 cc-PVTZ+3p(C)。先执行一次 CAP 单点计算，然后将 CAP-SCF 解读入作为 CAP-AIMD 部分的初始猜测。该流程很有用，例如当希望使用 MOM_START 选项（第 4.5.14 节）以在模拟过程中保持轨道占据数不变时。"
    ```qchem
    $molecule
    -1 2
    C    0.0000   0.0000   0.0000
    H    0.0000   0.0000   1.0742
    H    0.9596   0.0000  -0.4829
    C   -1.1191   0.0000  -0.6897
    H   -2.0787   0.0000  -0.2068
    H   -1.1191   0.0000  -1.7639
    $end
    
    
    $rem
     METHOD¯¯¯HF
     BASIS¯¯¯GENERAL
     GEN_SCFMAN¯¯TRUE
     SKIP_OLD_SCFMAN¯TRUE¯! skip old scfman drivers
     SCF_CONVERGENCE¯8
     SCF_GUESS¯¯CORE
     COMPLEX_CCMAN¯¯TRUE
     UNRESTRICTED¯¯TRUE
     CS_STRICT¯¯TRUE¯! Determine orbital energies and props. using the complex density matrix/complex MO coefficients
     CS_SCF_FINAL_PRINT¯1111¯! Print summary of energy decomposition
     INTEGRAL_SYMMETRY ¯FALSE
     POINT_GROUP_SYMMETRY¯FALSE
    $end
    
    $complex_ccman
     CS_HF ¯¯¯1
     CAP_TYPE ¯¯1
     CAP_ETA ¯¯230
     CAP_X ¯¯¯4360
     CAP_Y ¯¯¯2680
     CAP_Z ¯¯¯4360
    $end
    
    $basis
    H¯0
    cc-pvtz
    ****
    C     0
    S    8   1.00
       8236.0000000              0.0005310
       1235.0000000              0.0041080
        280.8000000              0.0210870
         79.2700000              0.0818530
         25.5900000              0.2348170
          8.9970000              0.4344010
          3.3190000              0.3461290
          0.3643000             -0.0089830
    S    8   1.00
       8236.0000000             -0.0001130
       1235.0000000             -0.0008780
        280.8000000             -0.0045400
         79.2700000             -0.0181330
         25.5900000             -0.0557600
          8.9970000             -0.1268950
          3.3190000             -0.1703520
          0.3643000              0.5986840
    S    1   1.00
         11.8760000              1.0000000
    S    1   1.00
          4.2920000              1.0000000
    S    1   1.00
          0.9059000              1.0000000
    S    1   1.00
          0.1285000              1.0000000
    P    3   1.00
         18.7100000              0.0140310
          4.1330000              0.0868660
          1.2000000              0.2902160
    P    1   1.00
         33.1900000              1.0000000
    P    1   1.00
          8.7780000              1.0000000
    P    1   1.00
          0.3827000              1.0000000
    P    1   1.00
          0.1209000              1.0000000
    D    1   1.00
         14.8390000              1.0000000
    D    1   1.00
          1.0970000              1.0000000
    D    1   1.00
          0.3180000              1.0000000
    F    1   1.00
          0.7610000              1.0000000
          P¯1¯¯1.00
          ¯¯0.06045¯1.00
          P¯1¯¯1.00
          ¯¯0.030225¯1.00
          P¯1¯¯1.00
          ¯¯0.0151125¯1.00
    ****
    $end
    
    
    @@@
    
    
    $molecule
     READ
    $end
    
    $velocity
    3.6095e-05   4.1623e-06   2.3754e-05
    -9.7386e-04  -1.4552e-05  -1.2310e-03
    -2.8737e-04   1.2165e-04   2.9068e-04
    3.3619e-05  -1.3939e-04   1.0849e-04
    6.4312e-04   2.0187e-04  -4.2066e-04
    -2.1196e-04   1.3012e-03  -2.1364e-04
    $end
    
    $rem
    ¯JOBTYPE¯¯AIMD
    ¯METHOD¯¯¯HF
    ¯BASIS¯¯¯GENERAL
    ¯GEN_SCFMAN¯¯TRUE
    ¯SKIP_OLD_SCFMAN¯TRUE
    ¯SCF_CONVERGENCE¯8
    ¯MAX_SCF_CYCLES¯¯3000
    integral_symmetry FALSE
    point_group_symmetry False
    ¯SCF_GUESS¯¯READ
    ¯COMPLEX_CCMAN¯¯TRUE
    ¯UNRESTRICTED¯¯TRUE
    ¯MOM_START¯¯1
    ¯MOM_METHOD¯¯MOM
    ¯TIME_STEP¯¯2
    ¯AIMD_STEPS¯¯200
       ¯FOCK_EXTRAP_ORDER      0
       ¯FOCK_EXTRAP_POINTS     0
      ¯AIMD_MOMENTS¯¯1
      ¯AIMD_PRINT¯¯2¯! Print Mulliken charges and dipole moments at each step
    ¯CS_STRICT¯¯TRUE
    $end
    
    $complex_ccman
    ¯CS_HF ¯¯¯1
    ¯CAP_TYPE ¯¯1
    ¯CAP_ETA ¯¯230
    ¯CAP_X ¯¯¯4360
    ¯CAP_Y ¯¯¯2680
    ¯CAP_Z ¯¯¯4360
    $end
    
    $basis
    H¯0
    cc-pvtz
    ****
    C     0
    S    8   1.00
       8236.0000000              0.0005310
       1235.0000000              0.0041080
        280.8000000              0.0210870
         79.2700000              0.0818530
         25.5900000              0.2348170
          8.9970000              0.4344010
          3.3190000              0.3461290
          0.3643000             -0.0089830
    S    8   1.00
       8236.0000000             -0.0001130
       1235.0000000             -0.0008780
        280.8000000             -0.0045400
         79.2700000             -0.0181330
         25.5900000             -0.0557600
          8.9970000             -0.1268950
          3.3190000             -0.1703520
          0.3643000              0.5986840
    S    1   1.00
         11.8760000              1.0000000
    S    1   1.00
          4.2920000              1.0000000
    S    1   1.00
          0.9059000              1.0000000
    S    1   1.00
          0.1285000              1.0000000
    P    3   1.00
         18.7100000              0.0140310
          4.1330000              0.0868660
          1.2000000              0.2902160
    P    1   1.00
         33.1900000              1.0000000
    P    1   1.00
          8.7780000              1.0000000
    P    1   1.00
          0.3827000              1.0000000
    P    1   1.00
          0.1209000              1.0000000
    D    1   1.00
         14.8390000              1.0000000
    D    1   1.00
          1.0970000              1.0000000
    D    1   1.00
          0.3180000              1.0000000
    F    1   1.00
          0.7610000              1.0000000
          P¯1¯¯1.00
          ¯¯0.06045¯1.00
          P¯1¯¯1.00
          ¯¯0.030225¯1.00
          P¯1¯¯1.00
          ¯¯0.0151125¯1.00
    ****
    $end
    ```
