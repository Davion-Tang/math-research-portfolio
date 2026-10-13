"""Finite, user-selected checks of public basic formulas, not paper theorems."""
from .compositions import integer
from .formulas import collect_terms, cycle_csf, cycle_e_terms, path_csf, spider_csf, weighted_e_terms
from .graphs import cycle_graph, graph_csf, path_graph, spider_graph


def _equal(actual, expected, case):
    if actual != expected:
        differences = {key: (actual.get(key, 0), expected.get(key, 0))
                       for key in actual.keys() | expected.keys()
                       if actual.get(key, 0) != expected.get(key, 0)}
        raise AssertionError(f"{case}: (formula, reference) coefficients differ: {differences}")


def verify_range(min_order: int = 0, max_order: int = 10, *, max_edges: int | None = 18) -> dict:
    """Check all P_n, C_n and unordered positive three-leg tuples in the range.

    Order bounds are inclusive; spider order is a+b+c+1. Invalid cycle orders
    (n < 3) and spider orders (n < 4) do not describe members of those families.
    A resource-budget violation aborts before calculation, never truncates a range.
    """
    min_order = integer(min_order, "min_order")
    max_order = integer(max_order, "max_order")
    if min_order > max_order:
        raise ValueError("min_order must not exceed max_order")
    if max_edges is not None:
        max_edges = integer(max_edges, "max_edges")
        largest_edges = max_order if max_order >= 3 else max(0, max_order - 1)
        if largest_edges > max_edges:
            raise ValueError(f"the requested range needs up to {largest_edges} edges; increase max_edges explicitly")
    counts = {"paths": 0, "cycles": 0, "three_legged_spiders": 0}
    identities = 0
    for n in range(min_order, max_order + 1):
        result = path_csf(n)
        _equal(result, graph_csf(path_graph(n), max_edges=max_edges), f"P_{n}")
        _equal(result, collect_terms(weighted_e_terms(n)), f"path composition sum, n={n}")
        counts["paths"] += 1
        identities += 2
        if n >= 3:
            result = cycle_csf(n)
            _equal(result, graph_csf(cycle_graph(n), max_edges=max_edges), f"C_{n}")
            _equal(result, collect_terms(cycle_e_terms(n)), f"cycle composition sum, n={n}")
            counts["cycles"] += 1
            identities += 2
        for c in range(1, (n - 1) // 3 + 1):
            for b in range(c, (n - 1 - c) // 2 + 1):
                a = n - 1 - b - c
                _equal(spider_csf(a, b, c), graph_csf(spider_graph(a, b, c), max_edges=max_edges),
                       f"S({a},{b},{c})")
                counts["three_legged_spiders"] += 1
                identities += 1
    return {"status": "passed", "min_order": min_order, "max_order": max_order,
            "max_edges": max_edges, "cases": counts, "identities_checked": identities,
            "scope": "finite basic-formula checks; not a proof for unbounded parameters"}

