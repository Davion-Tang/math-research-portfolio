# 基础公式与约定 | Basic formulas and conventions

[总览 / Portfolio](../README.md) · [使用方法 / Usage](usage.md)

这些是已公开的通用公式。代码是本次整理的基础实现，不包含三篇论文的新单射构造、统一正展开的专属验证器或毛毛虫树证书。下列数学式同时适用于两种语言的说明。

These are established public formulas. This package is a newly organized basic implementation; it does not distribute the papers' specialized injections, uniform-expansion verifiers, or caterpillar certificates. The displayed formulas are shared by the Chinese and English explanations.

## 1. 组合与权重 | Compositions and weights

令 $I=(i_1,\ldots,i_r)\vDash n$ 为正整数的有序组合：

$$w_I=i_1\prod_{j=2}^r(i_j-1),\qquad e_I=\prod_{j=1}^r e_{i_j}.$$

`compositions(n)` 枚举全部有序组合；`weight(I)` 计算 $w_I$；`weighted_e_term(I)` 返回包含原组合、系数和排序后指标的对象，`weighted_e_terms(n)` 生成一整族项。尾部含 $1$ 的组合可能具有零权重，默认省去零项，`include_zero=True` 可保留。

`compositions(n)` enumerates ordered positive compositions. `weight(I)` evaluates $w_I$. `weighted_e_term(I)` retains the ordered composition, its coefficient, and its decreasing elementary-basis index; `weighted_e_terms(n)` generates a family of such terms. Zero-weight terms are omitted unless `include_zero=True`.

例如 / Example:

$$w_{(2,3)}e_{(2,3)}=4e_2e_3,\qquad w_{(3,2)}e_{(3,2)}=3e_3e_2.$$

两者对应同一个 $e$-单项式，但权重不同。先排序组合再计算权重会得到错误结果。`collect_terms` 在权重确定后才合并。

These have the same elementary monomial but different ordered weights. Sorting before computing the weight is incorrect. `collect_terms` combines equal monomials only after weights have been evaluated.

代码约定 / Software conventions: $e_{()}=1$, $w_{()}=1$，`compositions(0)` 产生 `()`。这是处理空图的扩展约定。These empty-composition conventions support the empty graph.

`theta(I,a)` implements the prefix surplus, for $0\leq a\leq |I|$:

$$\Theta_I(a)=\min\{i_1+\cdots+i_k:0\leq k\leq r,\ i_1+\cdots+i_k\geq a\}-a.$$

来源 / Sources: [Spider paper, §2, weight definition](https://arxiv.org/html/2405.04915v3#S2); [KPKP/Kayak paper, §2, prefix statistics](https://arxiv.org/html/2408.01385v3#S2).

## 2. 路径 | Paths

$P_n$ 表示 $n$ 个顶点的路径，含 $n-1$ 条边（$n\geq1$）。$P_0$ 为代码中的空图，$X_{P_0}=1$。

$P_n$ has $n$ vertices and $n-1$ edges for $n\geq1$. The software also defines the empty graph $P_0$ with $X_{P_0}=1$.

$$X_{P_n}=\sum_{I\vDash n}w_Ie_I.$$

`path_csf(n)` 返回合并后的 $e$-基展开。`collect_terms(weighted_e_terms(n))` 给出相同结果，但显式枚举有序求和项。

`path_csf(n)` returns the collected elementary expansion. `collect_terms(weighted_e_terms(n))` obtains the same result by explicitly enumerating ordered summands.

$$X_{P_4}=4e_4+2e_3e_1+2e_2^2.$$

来源 / Source: Shareshian–Wachs path formula, as stated in [Lemma 2.1 in §2 of the Spider paper](https://arxiv.org/html/2405.04915v3#S2).

## 3. 圈 | Cycles

$C_n$ 是 $n\geq3$ 个顶点的简单圈。某些文献另设 $C_2=K_2$；本接口不采用这一扩展，输入 $n<3$ 会报错。

$C_n$ is a simple cycle with $n\geq3$ vertices. Some papers extend the notation by $C_2=K_2$; this API does not use that extension and rejects $n<3$.

$$X_{C_n}=\sum_{I=(i_1,\ldots)\vDash n}(i_1-1)w_Ie_I.$$

`cycle_csf(n)` 返回合并后的结果；`cycle_e_terms(n)` 保留有序求和项。

`cycle_csf(n)` returns the collected result; `cycle_e_terms(n)` retains the ordered summands.

$$X_{C_3}=6e_3,\qquad X_{C_4}=12e_4+2e_2^2.$$

来源 / Source: the standard path/cycle composition expansions recalled in [KPKP/Kayak paper, §2](https://arxiv.org/html/2408.01385v3#S2), with their original attribution there.

## 4. 三臂蜘蛛 | Three-legged spiders

腿长 $a,b,c$ 均以边数计，图阶 $n=a+b+c+1$。实现接受任意顺序的三个正整数，并先整理为 $a\geq b\geq c\geq1$。

Leg lengths count edges, so the graph order is $n=a+b+c+1$. The function accepts any ordering of three positive integers and first sorts them into $a\geq b\geq c\geq1$.

$$X_{S(a,b,c)}=X_{P_n}+\sum_{i=1}^c\left(X_{P_i}X_{P_{n-i}}-X_{P_{b+i}}X_{P_{n-b-i}}\right).$$

`spider_csf(a,b,c)` 实现这条路径乘积恒等式。这里出现减法，**不保证任意蜘蛛图都 $e$-正**。例如爪图：

`spider_csf(a,b,c)` implements this path-product identity. It is a signed expression and **does not imply that every spider is $e$-positive**. For example, the claw has

$$X_{S(1,1,1)}=4e_4+5e_3e_1-2e_2^2+e_2e_1^2.$$

`spider_graph(*legs)` 支持至少三臂；超过三臂时，通过 `graph_csf(spider_graph(*legs))` 独立计算，不能使用这条三臂公式。

`spider_graph(*legs)` supports three or more legs. For more than three, use `graph_csf(spider_graph(*legs))`; the displayed identity applies specifically to three legs.

来源 / Source: Zheng's identity, quoted as [Lemma 2.2 in §2 of the Spider paper](https://arxiv.org/html/2405.04915v3#S2).

## 5. 完全图 | Complete graphs

$$X_{K_n}=n!e_n\quad(n\geq1),\qquad X_{K_0}=1.$$

`complete_csf(n)` 实现该式，`complete_graph(n)` 构建对应图。每个合法着色必须使用互不相同的颜色，对每组颜色有 $n!$ 种分配，因此得到该式。

`complete_csf(n)` implements the formula and `complete_graph(n)` constructs the graph. Proper colorings use distinct colors, with $n!$ assignments for each color set, directly giving the identity.

## 6. 独立参考算法 | Independent reference algorithm

对简单无向图 $G=(V,E)$，使用 Stanley 的边子集公式：

For a simple undirected graph $G=(V,E)$, the reference uses Stanley's edge-subset expansion:

$$X_G=\sum_{A\subseteq E}(-1)^{|A|}p_{\lambda(A)}.$$

$\lambda(A)$ 是生成子图 $(V,A)$ 的连通分量大小构成的分拆，孤立顶点也必须计入。`graph_csf(..., basis="p")` 给出幂和基结果；默认再用 Newton 恒等式转为 $e$ 基：

$\lambda(A)$ records the connected-component sizes of the spanning subgraph $(V,A)$, including isolated vertices. `graph_csf(..., basis="p")` returns the power-sum expansion. The default converts it using Newton identities:

$$p_n=(-1)^{n-1}ne_n+\sum_{i=1}^{n-1}(-1)^{i-1}e_ip_{n-i}.$$

这一路径不调用路径、圈或蜘蛛的专门公式，因此可用于交叉核对。时间随边数呈指数增长；默认 `max_edges=18`，可显式修改或在 Python 中设为 `None`。超预算会报错，不截断计算。

This route never invokes the specialized path, cycle, or spider formulas, making it useful for cross-checking. Its runtime is exponential in edge count. The default `max_edges=18` is adjustable, and Python callers may set `None` explicitly. Exceeding a budget raises an error instead of truncating the calculation.

来源 / Source: Stanley (1995), Theorem 2.5; formula and attribution are documented in the [official SageMath graph reference](https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph.html#sage.graphs.graph.Graph.chromatic_symmetric_function).

## 7. 合并结果的计算方式 | Computing collected results

为避免在只需要合并结果时枚举全部 $2^{n-1}$ 个组合，`path_csf` 和 `cycle_csf` 使用上述组合公式的生成函数递推。令

To avoid enumerating all $2^{n-1}$ ordered compositions when only collected coefficients are wanted, `path_csf` and `cycle_csf` use a recurrence equivalent to those formulas. Define

$$A_0=1,\qquad A_r=\sum_{k=2}^r(k-1)e_k A_{r-k}\quad(r\geq1).$$

则 / Then, for positive $n$,

$$X_{P_n}=\sum_{k=1}^n ke_k A_{n-k},\qquad X_{C_n}=\sum_{k=2}^n k(k-1)e_k A_{n-k}\quad(n\geq3).$$

$A_r$ 对后续部件贡献的乘积求和；前面的 $k$ 或 $k(k-1)$ 正是首部件的权重。代码在返回前合并分拆指标。该递推仍受分拆数与内存限制，不承诺任意大的参数都能即时算完。

$A_r$ sums the weights of the remaining parts, and the first part contributes $k$ or $k(k-1)$. The code collects partition indices before returning. Output size and memory still grow with the partition count; no claim of instantaneous computation at arbitrarily large parameters is made.

