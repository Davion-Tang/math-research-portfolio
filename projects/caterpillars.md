# Caterpillar：毛毛虫树的度数约束与有限证书

[返回总览 / Portfolio](../README.md) · [中文](#中文) · [English](#english)

**$e$-Positive caterpillars have maximum degree at most three**  
Davion Q.B. Tang, David G.L. Wang, Monica M.Y. Wang  
状态 / Status：论文已完成 · Manuscript completed

公开基础工具 / Public basic tools：[精确对称函数运算、图计算与组合序列](../docs/usage.md)。下文的状态转移矩阵、不变锥和证书检查仍属于私有论文实现。The state-transfer matrices, invariant cones, and certificate checks below remain part of the private paper implementation.

## 中文

### 研究目标

毛毛虫树是一类可以由主干路径及其附加叶节点描述的树。本项目研究度数与 $e$-正性的关系，证明：**$e$-正毛毛虫树的最大度至多为 $3$**。

这处理了“含度数至少为 $4$ 的顶点的树不是 $e$-正的”这一猜想的毛毛虫树情形。论文的核心新定理排除最大度恰为 $4$ 的毛毛虫树，并结合已有归约得到上述完整结论。

### 为什么有限计算不够

图的主干可以任意延长，分叉节点的数目和间距也没有预设上界。因此，即使大量小实例均不具有 $e$-正性，也不能直接推出整个图类的结论。需要把无限多个图归约到能够进行归纳的有限状态结构。

### 证明思路

1. **用连通划分约束归约结构。** $e$-正图必须具有每种类型的连通划分。对候选毛毛虫树分析这一必要条件，得到中心结构及奇偶限制。
2. **按关键节点是否相邻分解问题。** 区分度为 $4$ 的中心是否邻接一个度为 $3$ 的顶点，分别组织证明。
3. **构造非负代入。** 选择对每个初等对称函数都取非负值的代入映射。如果该映射使图的色对称函数取负值，就能排除 $e$-正性。
4. **将图扩展写成矩阵转移。** 以有限状态描述添加路径、间隔或字块时的变化；相邻情形通过字表示组织允许的扩展。
5. **利用不变锥处理任意长度。** 精确核查初始状态、允许的转移及最终符号条件，再通过锥的不变性证明这些性质在任意多次扩展后仍成立。
6. **合并结构归约与证书。** 用数学论证连接有限证书和所有适用图，完成一般性结论。

### 主要结果

- 证明 $e$-正毛毛虫树的最大度至多为 $3$。
- 给出两类非蜘蛛毛毛虫树的无穷族，它们虽然具有每种类型的连通划分，却仍然不是 $e$-正的。
- 将相邻情形的证明组织为一组固定代入和四个不变行锥，减少多组代入带来的分类依赖。

“具有每种类型的连通划分”是必要条件而非充分条件；这里不主张所有最大度至多为 $3$ 的毛毛虫树都是 $e$-正的。

### 精确证书的作用

相邻情形使用精确有理数证书核查 **5 组初始条件、17 种允许转移、7 类中央配对**。这些检查避免以浮点近似判断符号，但证书本身并不替代结构归约、状态定义和归纳步骤。公开页面仅介绍证书的逻辑作用，不发布矩阵、生成元、证书数据或验证器。

### 合作与 AI 辅助研究

本人为第一作者，承担主要数学推导与全部 SageMath/Python 程序验证；先计算小规模实例、观察规律并独立推导关键奇偶约束，再按关键节点是否相邻拆分问题。与 GPT 协同探索时，由本人设定数学约束、提出简化方向，模型辅助搜索矩阵递推、不变锥证书与候选论证；本人逐条审查、纠错并与合作者核对数学论证。常用多项式、状态转移和证书检查封装为 Python 函数，以精确有理数运算复核。AI 辅助的范围在论文中披露，合作成果由作者负责。

### 访问说明

论文已完成。本仓库提供经过整理的目标、方法与成果概述及通用基础模块；论文专属实现代码、未公开全文和原始证书继续保存在私有项目中。

## English

### Objective

A caterpillar is a tree described by a spine path and attached leaves. This project proves that **an $e$-positive caterpillar has maximum degree at most three**.

It establishes the caterpillar case of the conjecture that a tree with a vertex of degree at least four is not $e$-positive. The central new theorem excludes caterpillars of maximum degree exactly four; existing reductions extend this to the stated degree bound.

### Why finite examples are insufficient

Spine lengths, branching patterns, and gap lengths are unbounded. Checking many small graphs therefore cannot settle the family. The proof needs a finite structure whose properties remain valid under arbitrarily many extensions.

### Proof outline

1. **Reduce using connected partitions.** The requirement that an $e$-positive graph admit connected partitions of every type imposes structural and parity restrictions on candidate caterpillars.
2. **Separate adjacency cases.** Treat separately whether the degree-four center has a trivalent neighbor.
3. **Choose nonnegative specializations.** Assign nonnegative values to elementary symmetric functions. A negative value of the specialized chromatic symmetric function then rules out $e$-positivity.
4. **Express extensions as matrix transfers.** Encode changes caused by paths, gaps, or word blocks in a finite state space. Word representations organize the allowed extensions in the adjacent case.
5. **Use invariant cones.** Check initial states, allowed transfers, and final sign conditions over the rationals. Cone invariance propagates these properties through arbitrary sequences of extensions.
6. **Complete the general argument.** Combine the certificate with the structural reductions and induction connecting every admissible graph to the finite checks.

### Results

- Every $e$-positive caterpillar has maximum degree at most three.
- Two infinite families of non-spider caterpillars admit connected partitions of every type but are nevertheless not $e$-positive.
- The adjacent case is handled by a single fixed specialization and four invariant row cones, simplifying an earlier approach involving multiple specializations.

Connected partitions of every type provide a necessary condition, not a sufficient condition. The degree bound does not assert that every caterpillar of maximum degree at most three is $e$-positive.

### Role of exact certificates

The adjacent-case certificate checks five seed conditions, seventeen allowed transfers, and seven central pairings using exact rational arithmetic. This avoids floating-point sign decisions. The finite computation remains dependent on the mathematical justification of the reduction, state representation, and induction. This page describes that role without distributing matrices, generators, certificate data, or verifier code.

### Collaboration and AI assistance

As first author, I was responsible for the main mathematical derivations and all SageMath/Python computational verification. I investigated small cases, independently derived the key parity restrictions, and split the problem by adjacency. In collaboration with GPT, I set mathematical constraints and proposed simplifications; the model assisted in exploring matrix recurrences, invariant-cone certificates, and candidate arguments. I reviewed and corrected the outputs and checked the reasoning with my coauthors. Common polynomial operations, state transfers, and certificate checks were organized as Python functions using exact rational arithmetic. The manuscript discloses this assistance, and the authors take responsibility for the joint results.

### Availability

The manuscript is complete. This portfolio publishes a research overview and general basic modules. The unpublished full text, paper-specific implementation code, and raw certificates remain in the private project.
