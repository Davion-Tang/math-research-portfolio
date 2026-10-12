# 数学研究项目 | Mathematical Research Portfolio

**汤麒宝 · Davion Q.B. Tang**  
北京理工大学 · Beijing Institute of Technology  
代数组合、图论与计算验证 · Algebraic combinatorics, graph theory, and computational verification

[中文介绍](#中文介绍) · [English overview](#english-overview)

## 中文介绍

这里介绍我作为第一作者参与完成的三个合作研究项目，主题是图的色对称函数与 $e$-正性。每个项目页面说明研究问题、主要结果、证明思路，以及计算验证在研究中的作用。

**本仓库公开项目介绍。三个项目的实现代码保存在各自的私有仓库，本仓库不提供源代码、可执行程序、原始证书数据或未公开的论文全文。**

### 项目导航

| 项目 | 研究目标与结果 | 主要方法 | 详细介绍 |
|---|---|---|---|
| Spider：树形图的组合匹配 | 证明 $S(4m+2,2m,1)$ 对所有整数 $m\geq1$ 都是 $e$-正的 | 组合序列、分类、显式单射与权重补偿 | [Spider](projects/spiders.md) |
| KPKP / Kayak：多类图的统一展开 | 构造多类图的正 $e_I$-展开，并研究公式之间的特化关系 | 参数化图结构、组合指标展开、配对与重排 | [KPKP / Kayak](projects/kayak.md) |
| Caterpillar：毛毛虫树的度数约束 | 证明 $e$-正毛毛虫树的最大度至多为 $3$ | 连通划分、代入映射、转移矩阵、不变锥与精确证书 | [Caterpillar](projects/caterpillars.md) |

### 共同研究问题

色对称函数把一个图的所有合法着色编码为对称函数。将它写成初等对称函数基的线性组合后，若所有系数都非负，就称这个图是 **$e$-正的**。研究的难点是控制一般参数下的全部系数，而不仅是计算几个小规模实例。

这三个项目分别从三个方向处理这一问题：通过单射补偿负项；构造直接可见的正展开；通过非负代入得到负值，排除 $e$-正性。

### 证明与计算的分工

研究工作结合实例计算、规律观察、严格推导和独立核查。有限范围检验用于检查公式、分类边界和实现；一般性结论依靠论文中的证明。有限证书只有与完整的结构归约及归纳论证结合，才能支持任意规模的结论。

Spider 和 Kayak 的验证程序曾于 **2026-10-12** 通过 Windows、Linux 上 Python 3.11 / 3.13 的自动测试。这里记录的是当时的测试结果，不是公开代码下载入口，也不表示穷举了全部参数。

### 阅读与代码状态

- 项目介绍：公开，可从上表进入中英双语说明。
- Spider / Kayak 论文：项目页面提供公开 arXiv 链接及版本说明。
- Caterpillar 论文：已完成；本仓库提供研究概述，不附论文全文。
- 三个实现仓库：保持私有。这个介绍仓库不提供可直接运行的复现包。

## English overview

This portfolio presents three collaborative research projects in which I am the first author. They study chromatic symmetric functions and $e$-positivity through combinatorial constructions, explicit expansions, and exact certificates.

**This is a public documentation repository. The implementations are maintained in three separate private repositories. Source code, executable programs, raw certificate data, and unpublished manuscript files are not distributed here.**

### Projects

| Project | Research objective and outcome | Main methods | Project page |
|---|---|---|---|
| Spiders | Establish $e$-positivity of $S(4m+2,2m,1)$ for every integer $m\geq1$ | Compositions, explicit injections, and weight compensation | [Spiders](projects/spiders.md#english) |
| KPKP / Kayak | Obtain positive composition-indexed expansions for several graph families | Parameterized constructions, specialization, pairing, and rearrangement | [KPKP / Kayak](projects/kayak.md#english) |
| Caterpillars | Prove that an $e$-positive caterpillar has maximum degree at most three | Connected partitions, specializations, transfer matrices, invariant cones, and rational certificates | [Caterpillars](projects/caterpillars.md#english) |

### Research context

The chromatic symmetric function encodes a graph's proper colorings. A graph is $e$-positive when its expansion in the elementary symmetric-function basis has only nonnegative coefficients. The challenge is to control all relevant coefficients for general parameters.

The projects approach this challenge by compensating negative terms through injections, constructing positive expansions, and ruling out positivity through carefully chosen specializations.

### Role of computation

Computational experiments help identify patterns and check formulas, boundary cases, and implementations. General statements are established by mathematical proofs. A finite certificate supports an unbounded conclusion only when the structural reduction and induction connecting it to that conclusion have been justified.

On **12 October 2026**, the Spider and Kayak verification programs passed automated tests on Windows and Linux with Python 3.11 and 3.13. This is a historical validation summary, not a claim of exhaustive verification over all parameters or a public software release.

The project pages provide paper references, proof outlines, and validation scope in both languages. The Caterpillar manuscript is complete; its full text is not included here. The three implementation repositories remain private.

---

Last updated / 更新日期：2026-10-12
