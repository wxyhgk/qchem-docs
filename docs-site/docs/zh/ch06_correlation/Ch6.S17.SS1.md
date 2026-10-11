# 6 并行化（Parallelization）

## 6.1 概述（Overview）

（本节内容来自 Q-Chem 7.0 手册第 6 章）

---

(July 15, 2026)

# 第 6 章 并行化（Parallelization）

## 6.1 概述（Overview）

(July 15, 2026)

以下内容介绍 Q-Chem 7.0 的并行化特性。

## 6.1.1 基于共享内存和分布式内存的混合并行（Hybrid Shared-Memory/Distributed-Memory Parallelism）

???+ example "示例 6.1：使用共享内存与分布式内存混合并行（Hybrid Shared-Memory/Distributed-Memory Parallelism）的描述"

    ??? example "6.1 节示例的描述"

        $rem
        ...
        $end

(July 15, 2026)

以下小节介绍 Q-Chem 7.0 中可用的并行选项。

## 6.1.2 使用共享内存和分布式内存进行并行化（Using Shared-Memory and Distributed-Memory Parallelization）

???+ example "示例 6.2：混合共享内存/分布式内存并行化（Hybrid Shared-Memory/Distributed-Memory Parallelization）的描述"

    ??? example "6.2 节示例的描述"

        $rem
        ...
        $end

(July 15, 2026)

## 6.1.3 Q-Chem 中的多线程线性代数（Multithreaded Linear Algebra in Q-Chem）

(July 15, 2026)

Q-Chem 使用 ScaLAPACK/BLAS 进行密集线性代数运算。

???+ example "示例 6.3：多线程线性代数（Multithreaded Linear Algebra）的描述"

    ??? example "6.3 节示例的描述"

        $rem
        ...
        $end

(July 15, 2026)

## 6.1.4 使用多线程积分（Using Multithreaded Integration）

(July 15, 2026)

## 6.1.5 在共享内存计算环境中设置 OMP_NUM_THREADS 环境变量（Setting the OMP_NUM_THREADS Environment Variable on Shared-Memory Computing Environments）

(July 15, 2026)

## 6.1.6 使用多线程 TD-DFT（Using Multithreaded TD-DFT）

(July 15, 2026)

## 6.1.7 使用多线程局部电子关联方法（Using Multithreaded Local Electron Correlation Methods）

(July 15, 2026)

## 6.2 使用分布式内存（Using Distributed Memory）

(July 15, 2026)

## 6.3 使用全局数组（Using Global Arrays）

(July 15, 2026)

以下小节介绍并行实现所使用的工具。

## 6.4 并行实现的通用信息（General Information About the Parallel Implementation）

(July 15, 2026)

以下示例展示了如何使用 `$rem` 输入变量 `$ecpi`。

## 6.5 使用 $ecpi 输入变量进行并行化（Parallelization with the $ecpi Input Variable）

(July 15, 2026)

以下内容介绍 Q-Chem 中可用的并行选项。

## 6.6 分布式内存计算的输入变量（Input Variables for Distributed-Memory Computing）

(July 15, 2026)

# 第 7 章 量子化学方法（Quantum Chemical Methods）

(July 15, 2026)

## 7.1 Hartree-Fock 方法（Hartree-Fock Method）

(July 15, 2026)

### 7.1.1 Hartree-Fock 互换（Hartree-Fock Interchange）

(July 15, 2026)

## 7.2 二阶与三阶微扰理论（Second- and Third-Order Perturbation Theory）

(July 15, 2026)

## 7.3 Møller-Plesset 级数收敛加速方法（Convergence Acceleration for Møller-Plesset Series）

(July 15, 2026)

## 7.4 耦合簇方法（Coupled-Cluster Methods）

(July 15, 2026)

## 7.5 图形处理器单元（Graphical Processing Units）

(July 15, 2026)

以下小节描述 Q-Chem 中可用的图形处理器（GPU）加速。

## 7.6 密度泛函理论（Density Functional Theory）

(July 15, 2026)

## 7.7 对称适配扰动态微扰理论（Symmetry-Adapted Perturbation Theory, SAPT）

(July 15, 2026)

# 第 8 章 激发态方法（Excited-State Methods）

(July 15, 2026)

## 8.1 含时密度泛函理论（Time-Dependent Density Functional Theory, TD-DFT）

(July 15, 2026)

## 8.2 Hartree-Fock 配置相互作用（Hartree-Fock Configuration Interaction, HF-CIS）

(July 15, 2026)

## 8.3 二阶代数-变分法（Algebraic-Diagrammatic Construction Through Second Order, ADC(2)）

(July 15, 2026)

## 8.4 相似耦合簇配置相互作用（Similarity-Transformed Coupled-Cluster Configuration Interaction, EOM-CC）

(July 15, 2026)

## 8.5 其他激发态方法（Other Excited-State Methods）

(July 15, 2026)

# 第 9 章 解析梯度与非解析梯度（Analytic and Non-Analytic Gradients）

(July 15, 2026)

## 9.1 Hartree-Fock 解析梯度（Analytic Hartree-Fock Gradients）

(July 15, 2026)

## 9.2 含时 Hartree-Fock 解析梯度（Analytic Time-Dependent Hartree-Fock Gradients）

(July 15, 2026)

## 9.3 含时密度泛函理论解析梯度（Analytic Time-Dependent Density Functional Gradients）

(July 15, 2026)

## 9.4 MP2 解析梯度（Analytic MP2 Gradients）

(July 15, 2026)

## 9.5 耦合簇解析梯度（Analytic Coupled-Cluster Gradients）

(July 15, 2026)

## 9.6 ADC(2) 解析梯度（Analytic ADC(2) Gradients）

(July 15, 2026)

## 9.7 CIS(D) 解析梯度（Analytic CIS(D) Gradients）

(July 15, 2026)

## 9.8 密度泛函理论解析梯度（Analytic Density Functional Gradients）

(July 15, 2026)

## 9.9 数值梯度（Numerical Gradients）

(July 15, 2026)

## 9.10 非绝热耦合（Nonadiabatic Couplings）

(July 15, 2026)

## 9.11 几何优化（Geometry Optimization）

(July 15, 2026)

# 第 10 章 其他性质（Other Properties）

(July 15, 2026)

## 10.1 分子性质（Molecular Properties）

(July 15, 2026)

## 10.2 自然键轨道分析（Natural Bond Orbital Analysis）

(July 15, 2026)

## 10.3 能量分解分析（Energy Decomposition Analysis）

(July 15, 2026)

# 第 11 章 强制场计算（Forced-Field Computations）

(July 15, 2026)

# 第 12 章 势能面扫描（Potential Energy Surface Scans）

(July 15, 2026)

# 第 13 章 复合方法（Composite Methods）

(July 15, 2026)

# 第 14 章 生物分子与显式溶剂建模（Biomolecules and Explicit-Solvation Modeling）

(July 15, 2026)

# 第 15 章 光谱学（Spectroscopy）

(July 15, 2026)

# 第 16 章 溶剂化模型（Solvation Models）

(July 15, 2026)

# 第 17 章 取代基与轨道冻结（Substituents and Orbital Freezing）

(July 15, 2026)

# 第 18 章 过渡态与反应路径搜索（Transition States and Reaction Path Searches）

(July 15, 2026)

# 第 19 章 表面建模（Modeling Surfaces）

(July 15, 2026)

# 第 20 章 作业控制（Job Control）

(July 15, 2026)

# 第 21 章 常用功能（Usual Functionality）

(July 15, 2026)

# 第 22 章 输入/输出格式（Input/Output Format）

(July 15, 2026)

# 第 23 章 Q-Chem 实用工具（Q-Chem Utilities）

(July 15, 2026)

# 第 24 章 安装（Installation）

(July 15, 2026)

# 第 25 章 关键词（Keywords）

(July 15, 2026)

# 附录 A 基组（Appendix A Basis Sets）

(July 15, 2026)

# 附录 B 交换关联泛函（Appendix B Exchange-Correlation Functionals）

(July 15, 2026)

# 附录 C 平面波方法（Appendix C Plane-Wave Methods）

(July 15, 2026)

# 附录 D 几何优化坐标选择（Appendix D Geometry Optimization Coordinate Selection）

(July 15, 2026)

# 附录 E 隐式溶剂模型（Appendix E Implicit Solvation Models）

(July 15, 2026)

# 附录 F 隐式溶剂输入变量（Appendix F Implicit Solvation Input Variables）

(July 15, 2026)

# 附录 G 示例（Appendix G Examples）

(July 15, 2026)

# 附录 H 缩写列表（Appendix H Abbreviations List）

(July 15, 2026)

# 附录 I 参考文献（Appendix I References）

(July 15, 2026)
