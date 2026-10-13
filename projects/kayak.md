# KPKP / Kayak：多类图结构的统一正展开

[返回总览 / Portfolio](../README.md) · [中文](#中文) · [English](#english)

**Positive $e_I$-expansions for KPKP graphs, twinned lollipops, and kayak paddles**  
Davion Q.B. Tang, David G.L. Wang  
[论文版本 / Paper version: arXiv:2408.01385v3](https://arxiv.org/abs/2408.01385v3), 2026-08-06

公开基础工具 / Public basic tools：[路径、圈、$w_Ie_I$ 与精确多项式运算](../docs/formulas.md)。本文统一公式的专属实现与逐定理验证器继续保存在私有项目中。The specialized implementations of the paper's uniform formulas and theorem verifiers remain in the private project.

## 中文

### 研究目标

用统一的组合展开方法描述多类图的色对称函数，并在保留组合序列指标 $I$ 的情况下证明展开系数非负。$e_I$ 是按序列 $I$ 的各部件取初等对称函数后的乘积；不同序列可能对应相同的对称函数单项式，因此逐项非负比合并同类项后再判断非负保留了更多信息。

### 图结构与研究路线

| 阶段 | 图结构 | 研究任务 |
|---|---|---|
| 统一公式 | KPKP：完全图、路径、完全图与尾路径构成的参数族 | 建立统一展开，再通过参数特化对照棒棒糖图及相关图类 |
| 顶点复制 | 路径、环与棒棒糖图的 twinning 变换 | 按顶点所在位置处理局部结构变化 |
| 双环结构 | Kayak paddle：两个环由路径连接 | 给出正展开，并研究路径退化为零条连接边的 infinity graph 情形 |

Twinning 指加入一个与原顶点相邻的新顶点，并使它具有原顶点的所有邻点。

### 证明思路

1. **参数化建模。** 用团大小、路径长度及连接位置统一描述图类。
2. **建立组合展开。** 将图运算转化为带组合序列指标的表达式，保留每个求和项的信息。
3. **通过特化连接图类。** 调整参数，获得较简单图类的公式，并核查退化和边界情形。
4. **构造非负表示。** 对 twinning 与双环结构使用分类、序列重排和配对；Kayak 的分析包含拼接映射、交换首部的对合及系数恒等式。
5. **检查逐项正性。** 在合并相同单项式之前确认相应展开的系数非负，从而得到正 $e_I$-展开及普通 $e$-正性的结论。

### 主要结果与研究角色

项目给出 KPKP、twinned paths、twinned cycles、twinned lollipops、kayak paddles 及 infinity graphs 的相关正展开。本人为第一作者，承担统一公式及推广情形的主要数学推导与全部程序验证，并参与论文写作。使用 SageMath/Python 生成有限范围的样例，将常用多项式、图结构与参数代入组织为可复用函数，并核查边界和已知特例；结果为与 David G.L. Wang 的合作成果。

### 计算验证范围

内部验证对应 v3 的 **9 项新编号结果**，涵盖统一公式、推论和结构变换后的展开。检查先保留有序组合指标并检查符号，再将同类项合并，与从图本身独立计算的结果比较，避免负项被合并后的抵消掩盖。

在默认图阶上界 $8$、连接路径参数上界 $4$ 的检查中，九项结果均通过；16 项软件测试及 Windows/Linux 上 Python 3.11 / 3.13 的自动测试也于 2026-10-12 通过。用户指定的有限范围与理论适用条件共同决定实际检查域；这类检查不构成任意参数下的证明。

### 版本与访问说明

本页对应 2026-08-06 更新的 arXiv v3。该版本修正了 Kayak 的正展开，并加入 infinity graph 推论。本仓库提供研究说明和公开论文链接；实现代码、运行报告原文件均保存在私有项目中。

## English

### Objective

The project develops positive composition-indexed expansions for chromatic symmetric functions of several related graph families. For a composition $I$, the notation $e_I$ denotes the product of elementary symmetric functions indexed by its parts. Different compositions can represent the same monomial, so retaining their coefficients records more information than collecting equal monomials first.

### Graph families and research route

| Stage | Graph structure | Task |
|---|---|---|
| Uniform formula | KPKP graphs built from complete graphs and paths | Derive one parameterized expansion and compare its specializations |
| Vertex twinning | Paths, cycles, and lollipops | Analyze the local change according to the position of the twinned vertex |
| Two-cycle structures | Kayak paddles and infinity graphs | Obtain a positive expansion and handle the zero-edge connection case |

Twinning adds a new vertex adjacent to the original vertex and to all of its neighbors.

### Proof outline

1. **Parameterize the graphs.** Describe clique sizes, path lengths, and attachment positions consistently.
2. **Derive composition expansions.** Translate graph operations into expressions that retain individual summands.
3. **Relate families by specialization.** Recover simpler cases by adjusting parameters and checking boundary conventions.
4. **Organize nonnegative contributions.** Use case analysis, rearrangements, and pairings for twinned and two-cycle structures. The Kayak argument includes concatenation maps, a head-swapping involution, and coefficient identities.
5. **Establish termwise positivity.** Check signs before collecting equal monomials, yielding positive $e_I$-expansions and the associated $e$-positivity statements.

### Outcome and role

The results cover KPKP graphs, twinned paths and cycles, twinned lollipops, kayak paddles, and infinity graphs. As first author, I was responsible for the main derivations of the uniform formula and its extensions, and all computational verification, and contributed to writing. SageMath/Python experiments, reusable polynomial and graph functions, parameter substitutions, and boundary checks supported this work. The results are joint work with David G.L. Wang.

### Computational scope

Internal verification addresses the nine new numbered results in v3. It checks signs with ordered composition indices retained, then compares the collected expansion against an independent computation from the graph. This prevents cancellation after collection from concealing a negative summand.

All nine results passed the default finite checks with graph order at most eight and connecting-path parameters at most four. Sixteen software tests and the Windows/Linux Python 3.11 / 3.13 test matrix passed on 12 October 2026. A requested range is intersected with the hypotheses of each statement; finite checking does not establish an unbounded theorem.

### Version and availability

This page follows arXiv v3, updated on 6 August 2026, including the corrected Kayak expansion and the infinity-graph corollary. This repository supplies an overview and a public paper reference. Implementation code and original machine-readable reports remain private.
