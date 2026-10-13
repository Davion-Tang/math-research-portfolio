# Spider：树形图的匹配规则与正性证明

[返回总览 / Portfolio](../README.md) · [中文](#中文) · [English](#english)

**The spiders $S(4m+2,2m,1)$ are $e$-positive**  
Davion Q.B. Tang, David G.L. Wang, Monica M.Y. Wang  
[公开论文 / Public paper: arXiv:2405.04915](https://arxiv.org/abs/2405.04915)

期刊进度 / Journal status：初审已通过（作者提供，2026-10-13） · Initial review passed (author-reported, 13 October 2026).

公开基础工具 / Public basic tools：[路径与三臂蜘蛛 CSF、组合权重](../docs/formulas.md)。这些基础函数不包含本文的专属单射或逐结论验证器。These utilities do not include this paper's specialized injections or theorem-by-theorem verifiers.

## 中文

### 研究目标

Spider 是若干条路径共用一个中心顶点形成的树。本项目研究三条腿长分别为 $4m+2$、$2m$、$1$ 的树族，目标是证明其对每个整数 $m\geq1$ 都具有 $e$-正性，从而解决针对这一参数族提出的猜想。

### 关键困难

利用组合序列展开色对称函数后，会出现带正权重和负权重的项。问题不只是为每个负项找到一个正项，还要确保分类覆盖全部负项、不同负项不重复使用同一份正贡献，并且补偿后的总权重非负。

### 证明思路

1. **分离和整理展开。** 利用 composition method，将待处理系数组织为带权组合序列，并化简到关键的负贡献类别。
2. **按序列特征分类。** 根据部件及奇偶结构划分情形，使每一类都有明确的处理规则。
3. **构造显式单射。** 重排序列部件，将负贡献对象映射到具有相同初等对称函数单项式的正贡献对象；必要时使用一对正项。
4. **检查覆盖、唯一性与权重。** 证明映射的像满足约束、映射具有单射性、不同匹配不会重复占用正项，并验证权重足以补偿。
5. **合并各类。** 将各个类别的非负贡献合并，得到整个参数族的 $e$-正性。

### 主要结果与研究角色

核心结果是对全部整数 $m\geq1$ 成立的正性定理。显式单射构造是论文的主要贡献之一。本人为第一作者，负责主要证明构造及全部 SageMath/Python 计算验证，并参与论文写作。研究中将常用多项式计算、序列处理与匹配检查组织为函数模块，按核验反馈回查数学推导；结果为上述三位作者的合作成果。

### 计算验证范围

内部验证工作以作者修订稿为准，为其中 **8 项新编号结果**设置检查入口，检查展开恒等式、分支条件、映射唯一性、权重补偿及最终系数。尤其区分不同分支，以及两个输入相同的情况下正项只能计数一次的规则。

记录的检查覆盖全部八项结果的 $m=1,2,3$，并将四个单射检查扩展至 $m=4$；小参数下的空定义域单独说明。软件的 16 项测试及 Windows/Linux 自动测试已于 2026-10-12 通过。有限参数检查是辅助证据，不能替代对任意 $m$ 的数学证明。

### 版本与访问说明

公开 arXiv 页面目前列出 v3（2025-08-30）。内部验证对应作者随后提供的 22 页修订稿，不能把该修订稿的结果编号、页码直接视为公开 arXiv v3 的编号、页码。本仓库另有通用基础模块；论文专属实现代码和修订稿文件不在本仓库发布。

## English

### Objective

A spider is a tree formed by joining paths at a common central vertex. This project establishes $e$-positivity for the three-legged family $S(4m+2,2m,1)$ for every integer $m\geq1$, resolving the conjecture for this family.

### Main difficulty

A composition-indexed expansion contains both positive and negative contributions. Matching a negative term to a positive term is insufficient unless every negative term is covered, positive contributions are not reused, and the resulting total weight is nonnegative.

### Proof outline

1. **Organize the expansion.** Use the composition method to isolate the contributions that require compensation.
2. **Divide the domain.** Classify compositions by their structural and parity properties.
3. **Construct explicit injections.** Rearrange parts to associate each negative contribution with one or, where needed, two positive contributions representing the same elementary symmetric-function monomial.
4. **Prove correctness.** Establish the image constraints, injectivity, non-reuse of positive terms, and the required weight inequalities.
5. **Combine the cases.** Sum the nonnegative grouped contributions to obtain the theorem for the full parameter family.

### Outcome and role

The main result holds for every integer $m\geq1$. Explicit injection constructions are a central contribution. As first author, I was responsible for the main proof constructions and all SageMath/Python computational verification, and contributed to writing. Common polynomial operations, sequence processing, and matching checks were organized into reusable functions, with computational feedback used to revisit derivations. The paper is joint work with the coauthors listed above.

### Computational scope

Internal verification provides checks for eight new numbered results in the author's revised manuscript. The checks address identities, branch conditions, injectivity, compensation, and final coefficients. They distinguish branch changes and diagonal cases in which a common positive image must be counted only once.

Recorded checks cover all eight results for $m=1,2,3$, with the four injection checks additionally tested at $m=4$. Empty domains at small parameters are identified explicitly. Sixteen software tests and automated Windows/Linux runs passed on 12 October 2026. These finite checks support the implementation; the unbounded theorem relies on the mathematical proof.

### Version and availability

The public arXiv record currently lists v3, dated 30 August 2025. Internal verification instead follows a subsequently supplied 22-page author revision. Its numbering and pagination should not be assumed to match the public version. General basic modules are provided separately; neither the paper-specific implementation nor that revised manuscript file is distributed in this portfolio.
