"""Run from the repository root: python -m examples.basic_usage"""
from csf_basics import (collect_terms, cycle_csf, format_e, graph_csf, path_csf,
                        spider_csf, spider_graph, weighted_e_term, weighted_e_terms)

print("X(P_4) =", format_e(path_csf(4)))
print("X(C_4) =", format_e(cycle_csf(4)))
print("X(S(2,1,1)) =", format_e(spider_csf(2, 1, 1)))
term = weighted_e_term((2, 3))
print("Ordered I =", term.composition, "; w_I =", term.coefficient,
      "; w_I e_I =", format_e(term.as_polynomial()))
print("Path terms for n=3, including zeros:")
for term in weighted_e_terms(3, include_zero=True):
    print(term)
assert collect_terms(weighted_e_terms(4)) == path_csf(4)
assert spider_csf(2, 1, 1) == graph_csf(spider_graph(2, 1, 1))

