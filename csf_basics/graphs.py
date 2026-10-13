"""Small simple graphs and an independent edge-subset CSF reference algorithm."""
from collections import Counter
from dataclasses import dataclass
from itertools import combinations

from .compositions import integer
from .symmetric import Polynomial, normalize, p_to_e


@dataclass(frozen=True)
class Graph:
    """Vertices are 0,...,order-1. Duplicate edges and loops are rejected."""
    order: int
    edges: tuple[tuple[int, int], ...] = ()

    def __post_init__(self):
        order = integer(self.order, "order")
        edges = []
        for edge in self.edges:
            if len(edge) != 2:
                raise ValueError("each edge must have two endpoints")
            u, v = (integer(endpoint, "endpoint") for endpoint in edge)
            if u >= order or v >= order or u == v:
                raise ValueError("endpoints must be distinct vertices of the graph")
            edges.append(tuple(sorted((u, v))))
        if len(set(edges)) != len(edges):
            raise ValueError("duplicate edges are not allowed")
        object.__setattr__(self, "order", order)
        object.__setattr__(self, "edges", tuple(sorted(edges)))


def path_graph(n: int) -> Graph:
    n = integer(n, "n")
    return Graph(n, tuple((v, v + 1) for v in range(n - 1)))


def cycle_graph(n: int) -> Graph:
    n = integer(n, "n", 3)
    return Graph(n, path_graph(n).edges + ((0, n - 1),))


def complete_graph(n: int) -> Graph:
    n = integer(n, "n")
    return Graph(n, tuple(combinations(range(n), 2)))


def spider_graph(*legs: int) -> Graph:
    """Leg lengths count edges, not vertices; support any number of legs >= 3."""
    if len(legs) < 3:
        raise ValueError("a spider must have at least three positive leg lengths")
    legs = tuple(integer(length, "leg length", 1) for length in legs)
    edges, next_vertex = [], 1
    for length in legs:
        previous = 0
        for _ in range(length):
            edges.append((previous, next_vertex))
            previous = next_vertex
            next_vertex += 1
    return Graph(next_vertex, tuple(edges))


def graph_csf(graph: Graph, *, basis: str = "e", max_edges: int | None = 18) -> Polynomial:
    """Stanley's sum over ALL edge subsets, then optionally convert p to e.

    Complexity is exponential in edge count. max_edges is a user-adjustable
    resource guard, not a mathematical bound; None explicitly removes the guard.
    No instances or subsets are silently skipped.
    """
    if not isinstance(graph, Graph):
        raise TypeError("graph must be a Graph")
    if basis not in ("p", "e"):
        raise ValueError("basis must be 'p' or 'e'")
    if max_edges is not None:
        max_edges = integer(max_edges, "max_edges")
        if len(graph.edges) > max_edges:
            raise ValueError(f"{len(graph.edges)} edges exceed max_edges={max_edges}; raise the budget explicitly")
    coefficients = Counter()
    for mask in range(1 << len(graph.edges)):
        parents = list(range(graph.order))

        def find(vertex):
            while parents[vertex] != vertex:
                parents[vertex] = parents[parents[vertex]]
                vertex = parents[vertex]
            return vertex

        for bit, (u, v) in enumerate(graph.edges):
            if mask & (1 << bit):
                parents[find(u)] = find(v)
        sizes = Counter(find(vertex) for vertex in range(graph.order))
        partition = tuple(sorted(sizes.values(), reverse=True))
        coefficients[partition] += -1 if mask.bit_count() % 2 else 1
    # Counter's unary + would incorrectly discard negative p coefficients.
    powers = normalize(coefficients)
    return powers if basis == "p" else p_to_e(powers)

