# 数学研究项目 | Mathematical Research Portfolio

**汤麒宝 · Davion Q.B. Tang**  
北京理工大学 · Beijing Institute of Technology  
代数组合、图论与计算验证 · Algebraic combinatorics, graph theory, and computational verification

[中文介绍](#中文介绍) · [English overview](#english-overview)

## 中文介绍

这里介绍我作为第一作者参与完成的三个合作研究项目，主题是图的色对称函数与 $e$-正性。每个项目页面说明研究问题、主要结果、证明思路，以及计算验证在研究中的作用。

**本仓库公开中英双语项目介绍和可运行的色对称函数基础模块。三个论文项目的完整验证程序、专属匹配构造、原始证书和未公开全文仍保存在私有项目中。**

### 可运行的基础模块

`csf_basics` 将常用图结构、组合序列和精确多项式运算组织为可复用的 Python 函数。代码对应已有基础公式，并附来源；这些通用公式不作为本人的新定理。

| 模块 | 公开内容 |
|---|---|
| [组合序列](csf_basics/compositions.py) | 枚举 $I\vDash n$、计算 $w_I=i_1\prod_{j\geq2}(i_j-1)$ 和 $\Theta_I(a)$ |
| [基础公式](csf_basics/formulas.py) | $X_{P_n}$、$X_{C_n}$、$X_{S(a,b,c)}$、$X_{K_n}$；生成单个或整族 $w_Ie_I$ |
| [对称函数运算](csf_basics/symmetric.py) | 精确加法、乘法、合并同类项、$p\to e$ 换基、代入与系数符号检查 |
| [图结构与独立计算](csf_basics/graphs.py) | 路径、圈、任意至少三臂蜘蛛图、完全图；用边子集公式独立计算 CSF |
| [范围验证](csf_basics/verification.py) | 按用户指定的图阶范围核对基础公式，报告实际覆盖数量 |

在仓库根目录运行，Python 3.10+，无需第三方运行依赖：

```bash
python -m csf_basics path 4
python -m csf_basics cycle 4
python -m csf_basics spider 6 2 1
python -m csf_basics terms 3 --include-zero
python -m csf_basics verify --min-order 0 --max-order 10
python -m unittest discover -s tests -v
```

```python
from csf_basics import path_csf, weighted_e_term, format_e

print(format_e(path_csf(4)))
# 4*e[4] + 2*e[3]*e[1] + 2*e[2]*e[2]
term = weighted_e_term((2, 3))
print(term.composition, term.coefficient, term.e_index)
# (2, 3) 4 (3, 2): ordered I is retained before collecting e monomials
```

[公式、来源与约定](docs/formulas.md) · [API 与使用方法](docs/usage.md) · [验证记录](docs/validation.md) · [Python 示例](examples/basic_usage.py) · [可选 SageMath 对照](examples/sage_check.py)

$P_n,C_n$ 的 $n$ 是顶点数；$S(a,b,c)$ 的腿长是边数，图阶为 $a+b+c+1$。三臂蜘蛛公式会先排序腿长，多臂情况可调用通用图计算。快速公式接口没有预设参数上界，但输出规模仍受计算资源限制。独立边子集核对需要指数时间，默认边数预算为 18，可显式提高；超预算会报错，不会静默缩小范围。

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
- 通用基础计算：本仓库公开提供，可直接运行并指定范围检查。
- 三个论文实现仓库：保持私有；这里的基础模块不等同于论文逐定理验证程序或完整复现包。

## English overview

This portfolio presents three collaborative research projects in which I am the first author. They study chromatic symmetric functions and $e$-positivity through combinatorial constructions, explicit expansions, and exact certificates.

**This repository publishes bilingual project overviews and executable basic CSF modules. Complete paper-specific verifiers, specialized matching constructions, raw certificates, and unpublished manuscripts remain in the private projects.**

### Executable basic modules

The `csf_basics` Python package provides reusable graph constructions, ordered compositions, and exact symmetric-function operations. The formulas are established results with references, not new theorems claimed by this portfolio.

| Module | Public functionality |
|---|---|
| [Compositions](csf_basics/compositions.py) | Enumerate $I\vDash n$, compute $w_I$ and the prefix surplus $\Theta_I(a)$ |
| [Formulas](csf_basics/formulas.py) | Paths, simple cycles, three-legged spiders, complete graphs, and ordered $w_Ie_I$ terms |
| [Symmetric functions](csf_basics/symmetric.py) | Exact arithmetic, collection, $p$-to-$e$ conversion, specialization, coefficient signs |
| [Graphs](csf_basics/graphs.py) | Graph constructors and an independent edge-subset CSF calculation |
| [Verification](csf_basics/verification.py) | Exhaustive basic-formula checks within a user-selected finite graph-order interval |

The commands and Python example above run from the repository root with Python 3.10+ and no third-party runtime dependencies. See the bilingual [formula reference](docs/formulas.md), [usage guide](docs/usage.md), and [validation record](docs/validation.md). An [optional SageMath example](examples/sage_check.py) demonstrates conversion and external comparison.

For $P_n,C_n$, $n$ counts vertices. Spider legs count edges, so $S(a,b,c)$ has $a+b+c+1$ vertices. The fast spider formula accepts three legs in any order; spiders with more legs use the generic graph algorithm. Fast formulas have no preset parameter cap, but remain resource-limited. Independent subset verification takes exponential time: its default edge budget is 18, can be raised explicitly, and never silently truncates the requested range.

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

Last updated / 更新日期：2026-10-13
