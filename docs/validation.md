# 验证记录 | Validation record

日期 / Date: **2026-10-13**  
环境 / Environment: **Windows, Python 3.12.14**

## 已完成的本地检查 | Completed local checks

```bash
python -m unittest discover -s tests -v
python -m csf_basics verify --min-order 0 --max-order 13
python -m examples.basic_usage
```

- **18 项测试通过。** 包括用独立切割位置枚举组合、已知小图展开、Newton 恒等式的数值代入、直接按合法着色定义计算、孤立顶点与空图、符号、参数边界和命令行错误退出。
- **103 项恒等式核对通过。** 覆盖 14 个路径、11 个简单圈和 53 个不同的三臂蜘蛛；图阶区间为 $0\leq n\leq13$，三臂蜘蛛按排序后的腿长计数。
- **Python 示例运行通过。** 包含有序权重与分拆指标的区别，以及蜘蛛公式与独立图计算的对照。

- **18 tests passed.** They include independent cut-position enumeration, known small expansions, numerical checks of Newton identities, direct evaluation from proper colorings, isolated vertices, the empty graph, signs, input boundaries, and command-line failure behavior.
- **103 identity comparisons passed.** The inclusive range $0\leq n\leq13$ contains 14 paths, 11 simple cycles, and 53 distinct sorted three-legged spiders.
- **The Python example passed.** It demonstrates ordered weights versus partition indices and compares the spider identity against independent graph computation.

```json
{
  "status": "passed",
  "min_order": 0,
  "max_order": 13,
  "max_edges": 18,
  "cases": {
    "paths": 14,
    "cycles": 11,
    "three_legged_spiders": 53
  },
  "identities_checked": 103
}
```

路径、圈各有两条对照：快速公式对图的边子集计算，以及快速公式对有序组合展开。每个三臂蜘蛛有一条公式对图计算的对照。因此总数为 $2(14+11)+53=103$。

Each path and cycle has two comparisons: its fast formula against the edge-subset reference, and its fast formula against the ordered composition sum. Each spider contributes one formula-versus-graph comparison, giving $2(14+11)+53=103$.

## 自动测试与 SageMath 状态 | CI and SageMath status

[GitHub Actions 配置](../.github/workflows/tests.yml) 已准备好，上传后会在 Windows/Linux 与 Python 3.11/3.13 的四个组合上运行 18 项测试、图阶至 10 的范围检查和 Python 示例。**本记录不把尚未运行的公开仓库 CI 标为通过。** 实际状态请查看仓库的 Actions 页面。

The [GitHub Actions workflow](../.github/workflows/tests.yml) is prepared for Windows/Linux and Python 3.11/3.13. After upload, its four jobs will run the tests, range verification through order 10, and the Python example. **This record does not claim that pending public-repository CI has passed.** See the Actions page for actual run status.

本次基础模块的本地检查没有使用 SageMath 环境；可选转换接口和 [Sage 对照示例](../examples/sage_check.py) 已提供，但这里不声称 Sage 对照已执行成功。论文研究过程中使用的 SageMath/Python 与本次独立发布的基础包，应区别对待。

The local checks of this basic package did not run in SageMath. The optional bridge and [comparison example](../examples/sage_check.py) are included, but no successful Sage execution is claimed here. The SageMath/Python used during the research should be distinguished from validation of this newly packaged public module.

## 证据范围 | Scope of evidence

这些检查针对本次公开基础模块。有限测试既不覆盖无限参数，也不替代论文中的数学证明；私有论文验证器的历史测试另见各项目页。三篇论文的专属证明代码、匹配规则及原始证书没有随本包发布。

These checks concern the public basic modules. Finite tests neither cover unbounded parameters nor replace mathematical proofs. Historical tests of the private paper verifiers are described separately on the project pages. Paper-specific proof implementations, matching rules, and raw certificates are not included in this package.
