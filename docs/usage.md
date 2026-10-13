# 使用方法与 API | Usage and API

[总览 / Portfolio](../README.md) · [公式 / Formulas](formulas.md) · [验证 / Validation](validation.md)

## 快速开始 | Quick start

下载并解压仓库，在包含 `README.md` 和 `csf_basics` 的根目录打开终端。基础模块只需要 Python 3.10+；不必先安装 SageMath。也可以在该目录运行 `python -m pip install .` 安装到当前 Python 环境。

Download and extract the repository, then open a terminal at the root containing `README.md` and `csf_basics`. The basic modules require Python 3.10+ without SageMath or other runtime dependencies. Optionally run `python -m pip install .` to install them into the current Python environment.

```bash
python -m examples.basic_usage
python -m csf_basics path 4
python -m csf_basics cycle 4
python -m csf_basics spider 6 2 1
python -m csf_basics terms 5
python -m csf_basics terms 3 --include-zero
```

在有些 Windows 环境中用 `py` 替代 `python`。On some Windows systems, use `py` instead of `python`.

## 返回数据 | Return values

对称函数以 `{partition_tuple: exact_coefficient}` 表示；常用公式返回 $e$ 基。有理数使用 `fractions.Fraction`，不使用浮点数。键是递减分拆，如 `(3,1)` 表示 $e_3e_1$。`{}` 是零，`{(): 1}` 是常数 $1$。

Symmetric functions are dictionaries `{partition_tuple: exact_coefficient}`. Formula functions return the $e$ basis, with exact `fractions.Fraction` coefficients. A decreasing key `(3,1)` denotes $e_3e_1$; `{}` is zero and `{(): 1}` is the constant one.

```python
from csf_basics import *

f = path_csf(4)
assert f == {(4,): 4, (3, 1): 2, (2, 2): 2}
print(format_e(f))

term = weighted_e_term((2, 3))
assert term.composition == (2, 3)
assert term.coefficient == 4
assert term.e_index == (3, 2)
assert term.as_polynomial() == {(3, 2): 4}
assert collect_terms(weighted_e_terms(4)) == f

g = spider_graph(2, 1, 1)
assert graph_csf(g) == spider_csf(2, 1, 1)
four_legged = graph_csf(spider_graph(1, 1, 1, 1))
```

普通字典不记录基的种类；`graph_csf(g, basis="p")` 的键表示 $p_\lambda$，必须先 `p_to_e(...)` 才能与 $e$ 基结果相加或比较。

A dictionary does not carry basis metadata. Keys from `graph_csf(g, basis="p")` denote $p_\lambda$. Apply `p_to_e(...)` before combining or comparing them with $e$-basis results.

## 常用函数 | Common functions

| API | 中文 | English |
|---|---|---|
| `compositions(n, min_part=1)` | 有序正整数组合的生成器；支持 $n=0$ | Generator of ordered compositions; includes the empty case |
| `weight(I)` | $w_I$ | Ordered composition weight |
| `theta(I,a)` | $\Theta_I(a)$，含 $a=0,|I|$ | Prefix surplus, including boundary values |
| `e_monomial(I, coefficient=1)` | 生成 $c e_I$ 并排序基指标 | Construct a collected elementary monomial |
| `weighted_e_term(I)` | 保留原组合的一个 $w_Ie_I$ 对象 | One ordered weighted term |
| `weighted_e_terms(n, include_zero=False)` | 生成全部非零 $w_Ie_I$；可保留零项 | Generate weighted terms, optionally retaining zeros |
| `cycle_e_terms(n)` | 圈的有序展开项 | Ordered cycle summands |
| `collect_terms(terms)` | 合并对应相同分拆的项 | Collect terms at equal partition indices |
| `path_csf(n)` | 路径的 $e$ 展开，$n\geq0$ | Path elementary expansion |
| `cycle_csf(n)` | 简单圈的 $e$ 展开，$n\geq3$ | Simple-cycle elementary expansion |
| `spider_csf(a,b,c)` | 三臂蜘蛛的 $e$ 展开，三参数均正 | Three-legged spider elementary expansion |
| `complete_csf(n)` | $n!e_n$，空图返回 $1$ | Complete-graph elementary expansion |
| `add(f,g)`, `scale(f,c)`, `multiply(f,g)` | 同一乘法基上的精确运算 | Exact arithmetic within the same multiplicative basis |
| `power_sum_e(n)`, `p_to_e(f)` | Newton 恒等式换基 | Power-sum to elementary conversion |
| `evaluate_e(f, values)` | 指定每个所需 $e_k$ 的精确值；缺项报错 | Exact elementary specialization; missing indices raise an error |
| `principal_specialization(f,q)` | $e_k\mapsto\binom{q}{k}$ | Count proper $q$-colorings when $f$ is a CSF |
| `is_e_positive(f)` | 检查合并后的全部系数 | Check collected coefficients of this instance |
| `graph_csf(g, basis="e", max_edges=18)` | 通过边子集独立计算 | Independent reference computation from the graph |
| `format_e(f)` | 显示可读表达式 | Readable elementary-basis formatting |

数值规模参数拒绝负数、浮点数和布尔值，接受精确整数类输入。简单图不允许自环、重边或越界顶点。Python 返回的字典可以修改，不会破坏内部缓存。

Size arguments reject negatives, floats, and booleans, and accept exact integer-like values. Simple graphs reject loops, repeated edges, and invalid endpoints. Returned dictionaries can be modified without corrupting internal caches.

## 自选范围验证 | Choose a verification range

```bash
python -m csf_basics verify --min-order 4 --max-order 10
python -m csf_basics verify --min-order 0 --max-order 13 --max-edges 18
```

```python
from csf_basics.verification import verify_range
report = verify_range(min_order=4, max_order=10, max_edges=18)
print(report)
```

上下界均包含在范围中。程序核对范围内的所有路径、合法简单圈，以及满足 $a\geq b\geq c\geq1$、$a+b+c+1$ 在范围内的所有三臂蜘蛛。同构的腿长排列只计算一次。路径和圈额外核对“生成有序项再合并”与快速公式是否一致。

Bounds are inclusive. Every path, valid simple cycle, and sorted positive triple $a\geq b\geq c\geq1$ whose spider order lies in the range is checked. Equivalent leg permutations are counted once. Paths and cycles are also checked against explicitly generated and collected composition terms.

输出 JSON 报告实际图数和恒等式数。发现差异会报告参数及不一致系数并以失败退出；范围超出边数预算会在计算前报错，不把少算的结果标为通过。若确需更大范围，应显式提高 `--max-edges`，同时考虑指数级耗时。

The JSON report records actual case and identity counts. A mismatch reports its parameters and differing coefficients and exits with failure. Exceeding the edge budget fails before computation, rather than reporting a truncated range as passed. Raise `--max-edges` explicitly for a larger reference calculation, accounting for exponential runtime.

这验证的是有限范围的基础公式实现，不是三篇论文的一般性定理。用户可选择不同范围；未运行的参数不会被声称已经验证。

This checks basic formula implementations on a finite range, not the papers' unbounded theorems. Choosing a new range does not mean its cases have already been tested.

## SageMath（可选）| SageMath (optional)

```python
from csf_basics import path_csf
from csf_basics.sage_bridge import to_sage_e
f = to_sage_e(path_csf(4))
print(f)
```

在已安装 SageMath 的环境中运行 / In an installed SageMath environment:

```bash
sage -python -m examples.sage_check
```

该示例将结果转为 `SymmetricFunctions(QQ).e()`，并与 Sage 的 `Graph.chromatic_symmetric_function()` 比较。普通 Python 模块不依赖 Sage；Sage 示例是否实际通过，以[验证记录](validation.md)或用户自己的运行为准。

The example converts results to `SymmetricFunctions(QQ).e()` and compares against Sage's graph CSF implementation. The base package does not depend on Sage. Actual execution status is recorded in [validation](validation.md), separately from the availability of the example.

官方接口说明 / Official API references: [symmetric functions](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/sf/elementary.html), [graph CSF](https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph.html#sage.graphs.graph.Graph.chromatic_symmetric_function).

