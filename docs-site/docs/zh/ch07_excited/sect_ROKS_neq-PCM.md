---
title: "7.7.9 ROKS 与 $\Delta$SCF 的非平衡溶剂化"
---

## 7.7.9 ROKS 与 $\Delta$SCF 的非平衡溶剂化

（2026 年 7 月 4 日）

$\Delta$SCF 计算（*例如*，基于 MOM 的计算）与 ROKS 计算都可以在可极化连续介质模型（Polarizable Continuum Model, PCM）所描述的连续介质溶剂效应下执行。
（溶剂化模型本身的描述见第 [11.2.3](../ch11_env/topic_pcm-em.md) 节。）与基态类似，沿 SCF 流程进行自洽的 PCM 处理可为所计算的激发态提供*平衡*（equilibrium）溶剂化（设置 SOLVENT_METHOD = PCM
并包含 *$pcm* 输入段）。在平衡溶剂化过程中，慢（核）自由度与快（电子）溶剂自由度都会被弛豫（由 *$solvent* 输入段中的 **Dielectric** 控制），这对于长寿命态是合适的。
然而，快速的垂直激发或发射发生在更短的时间尺度上，此时只需要快（电子）溶剂极化发生弛豫（由 **Dielectric_Infi** 控制，见第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节）。
在 **Q-Chem** 中，此类*非平衡*（nonequilibrium）溶剂化效应可以通过微扰态特定（perturbative state-specific, ptSS）校正以一阶精度纳入。[[1530]](../bib_references/bib.md#bib1593)

首先，非平衡 $\Delta$SCF 或 ROKS 计算要求初始状态（吸收过程为基态，发射过程为激发态）已完成平衡溶剂化。通过在 *$pcm* 输入段中将 **RF_ptSS_Save** 设为 **true**，
即可将平衡后的反应场（reaction field）存储到磁盘上。在随后任意一个针对终态的作业中设置 **RF_ptSS_Read** = **true**，便会重新读取该反应场。
这会自动触发一次冻结反应场（frozen reaction field, fRF）SCF，使用所存储的初始状态反应场。所得的 SCF 能量
对应于终态处于初始状态反应场中的零级计算结果。若要获得一阶非平衡结果，需要对终态弛豫快溶剂极化，
即叠加一项微扰 ptSS 校正，该校正会在收敛的 fRF-SCF 计算之后打印输出。

### `RF_ptSS_Save`

> **将当前反应场存储到磁盘。输入段：$pcm**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE
>     * 在当前作业中存储反应场。
>     * FALSE
>     * 在当前作业中不存储反应场。
> * **建议**：反应场是为参考态存储的：对于 $\Delta$ SCF 或 ROKS，参考态就是 SCF 结果本身；而对于 TDDFT + II-SS-PCM，参考态为所选定的参考态（见第 7.3.7.2 节）。若在多个连续作业中开启 RF_ptSS_SAVE，反应场会被覆盖。

### `RF_ptSS_Read`

> **从磁盘读取反应场，并基于它执行 fRF-SCF + ptSS-PCM 计算。输入段：$pcm**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE
>     * 在当前作业中读取反应场。
>     * FALSE
>     * 在当前作业中不读取反应场。
> * **建议**：SCF 结果对应于终态的零级溶剂化。若要获得一阶非平衡溶剂化，需叠加在 fRF-SCF 之后打印的 ptSS 校正。

???+ example "示例 7.60：用 ROKS + PCM 及非平衡 ptSS-PCM 校正计算甲醛在乙腈中的垂直激发能。"
    ```qchem
    $rem
       method               pbe0
       basis                def2-SVP
       scf_convergence      8
       point_group_symmetry false
       solvent_method       pcm
    $end
    
    $pcm
       theory              iefpcm
       rf_ptss_save        true            ! Save the final ground state reaction field
    $end
    
    $solvent
       Dielectric          35.688000       ! Acetonitrile
       Dielectric_Infi     1.806874
    $end
    
    $molecule
       0 1
       H      -0.940372    0.000000    1.268098
       H       0.940372    0.000000    1.268098
       C       0.000000    0.000000    0.682557
       O       0.000000    0.000000   -0.518752
    $end
    
    @@@
    
    $rem
       method               pbe0
       basis                def2-SVP
       scf_guess            read
       roks                 true
       unrestricted         false
       scf_convergence      8
       point_group_symmetry false
       solvent_method       pcm
    $end
    
    $pcm
       theory              iefpcm
       rf_ptss_read        true            ! Read the prior reaction field and start fRF-SCF
    $end
    
    $solvent
       Dielectric          35.688000       ! Acetonitrile
       Dielectric_Infi     1.806874
    $end
    
    $molecule
       0 1
       read
    $end
    ```
