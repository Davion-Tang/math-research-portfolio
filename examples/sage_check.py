"""Optional: sage -python -m examples.sage_check (requires installed SageMath)."""
from sage.all import Graph as SageGraph, graphs

from csf_basics import cycle_csf, path_csf, spider_csf, spider_graph
from csf_basics.sage_bridge import to_sage_e

for n in range(1, 8):
    assert to_sage_e(path_csf(n)) == graphs.PathGraph(n).chromatic_symmetric_function()
for n in range(3, 8):
    assert to_sage_e(cycle_csf(n)) == graphs.CycleGraph(n).chromatic_symmetric_function()
for legs in ((1, 1, 1), (2, 1, 1), (3, 2, 1)):
    graph = spider_graph(*legs)
    sage_graph = SageGraph([list(range(graph.order)), list(graph.edges)], format="vertices_and_edges")
    assert to_sage_e(spider_csf(*legs)) == sage_graph.chromatic_symmetric_function()
print("SageMath agrees on 7 paths, 5 cycles, and 3 spiders.")

