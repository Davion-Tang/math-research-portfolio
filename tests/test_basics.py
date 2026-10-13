"""Independent definitions, exact known cases, invalid inputs, and range checks."""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, prod
import unittest

from csf_basics import *
from csf_basics.verification import verify_range


def coloring_value(graph, variables):
    # Direct definition of X_G at concrete variables, independent of subset/CSF formulas.
    return sum(prod(variables[color] for color in coloring)
               for coloring in product(range(len(variables)), repeat=graph.order)
               if all(coloring[u] != coloring[v] for u, v in graph.edges))


def elementary_values(n, variables):
    return {k: sum(prod(items) for items in combinations(variables, k)) for k in range(1, n + 1)}


class BasicFormulaTests(unittest.TestCase):
    def test_compositions_by_independent_cut_masks(self):
        self.assertEqual(list(compositions(0)), [()])
        for n in range(1, 10):
            expected = set()
            for mask in range(1 << (n - 1)):
                cuts = [0] + [i for i in range(1, n) if mask & (1 << (i-1))] + [n]
                expected.add(tuple(b-a for a, b in zip(cuts, cuts[1:])))
            actual = list(compositions(n))
            self.assertEqual(actual, sorted(expected))
            self.assertEqual(list(compositions(n, min_part=2)), [i for i in actual if min(i) >= 2])

    def test_ordered_weights_are_not_partition_weights(self):
        self.assertEqual(weight((2, 3)), 4)
        self.assertEqual(weight((3, 2)), 3)
        self.assertEqual(weight((2, 1)), 0)
        self.assertEqual(weight((1, 2)), 1)
        self.assertEqual(weight(()), 1)
        terms = list(weighted_e_terms(3, include_zero=True))
        self.assertEqual([t.composition for t in terms], [(1, 1, 1), (1, 2), (2, 1), (3,)])
        self.assertEqual([t.coefficient for t in terms], [0, 1, 0, 3])
        self.assertEqual(collect_terms(terms), {(3,): 3, (2, 1): 1})

    def test_exact_known_expansions(self):
        self.assertEqual(path_csf(4), {(4,): 4, (3, 1): 2, (2, 2): 2})
        self.assertEqual(cycle_csf(3), {(3,): 6})
        self.assertEqual(cycle_csf(4), {(4,): 12, (2, 2): 2})
        self.assertEqual(spider_csf(1, 1, 1), {(4,): 4, (3, 1): 5, (2, 2): -2, (2, 1, 1): 1})
        self.assertFalse(is_e_positive(spider_csf(1, 1, 1)))

    def test_newton_identities_against_actual_variables(self):
        for variables in ((1, 2, 4), (0, -1, 3, 5)):
            for n in range(1, 9):
                self.assertEqual(evaluate_e(power_sum_e(n), elementary_values(n, variables)),
                                 sum(x ** n for x in variables))

    def test_direct_proper_coloring_definition(self):
        graphs_to_check = [Graph(0), Graph(3), Graph(4, ((0, 1), (2, 3))), path_graph(5),
                           cycle_graph(5), spider_graph(2, 1, 1), spider_graph(1, 1, 1, 1)]
        for graph in graphs_to_check:
            for variables in ((1, 2, 3), (0, 1, 2)):
                with self.subTest(graph=graph, variables=variables):
                    self.assertEqual(evaluate_e(graph_csf(graph), elementary_values(graph.order, variables)),
                                     coloring_value(graph, variables))

    def test_coloring_counts(self):
        for n in range(1, 9):
            for q in range(5):
                self.assertEqual(principal_specialization(path_csf(n), q), q * (q-1) ** (n-1))
                if n >= 3:
                    self.assertEqual(principal_specialization(cycle_csf(n), q),
                                     (q-1)**n + (-1)**n * (q-1))

    def test_complete_graph_reference(self):
        for n in range(6):
            self.assertEqual(complete_csf(n), graph_csf(complete_graph(n)))

    def test_empty_graph_and_constants(self):
        self.assertEqual(path_csf(0), {(): 1})
        self.assertEqual(graph_csf(Graph(0)), {(): 1})
        self.assertEqual(graph_csf(Graph(3)), {(1, 1, 1): 1})
        self.assertEqual(principal_specialization({(): 1}, 0), 1)
        self.assertEqual(format_e({}), "0")

    def test_arithmetic_and_collection(self):
        self.assertEqual(add({(1, 2): 1}, {(2, 1): -1}), {})
        self.assertEqual(multiply({(2,): Fraction(1, 3)}, {(1,): 3}), {(2, 1): 1})
        self.assertEqual(scale({(2,): 2}, 0), {})
        self.assertEqual(p_to_e({(2, 1): 1}), {(1, 1, 1): 1, (2, 1): -2})

    def test_cache_cannot_be_modified_by_callers(self):
        for function, n in ((path_csf, 7), (cycle_csf, 7), (power_sum_e, 7)):
            expected = function(n)
            changed = function(n)
            changed.clear()
            self.assertEqual(function(n), expected)

    def test_spider_permutation_and_graph_conventions(self):
        expected = spider_csf(3, 2, 1)
        for legs in permutations((3, 2, 1)):
            self.assertEqual(spider_csf(*legs), expected)
        graph = spider_graph(3, 2, 1)
        self.assertEqual((graph.order, len(graph.edges)), (7, 6))

    def test_theta_at_prefix_boundaries(self):
        self.assertEqual([theta((2, 3), a) for a in range(6)], [0, 1, 0, 2, 1, 0])
        self.assertEqual(theta((), 0), 0)

    def test_bad_inputs_are_rejected(self):
        cases = [lambda: path_csf(-1), lambda: path_csf(2.0), lambda: path_csf(True),
                 lambda: cycle_csf(2), lambda: spider_csf(0, 1, 1),
                 lambda: weight((1, 0)), lambda: list(compositions(3, min_part=0)),
                 lambda: Graph(3, ((0, 0),)), lambda: Graph(2, ((0, 2),)),
                 lambda: Graph(2, ((0, 1), (1, 0))), lambda: spider_graph(1, 2),
                 lambda: graph_csf(path_graph(2), basis="x"), lambda: theta((2, 3), 6),
                 lambda: normalize({(1,): 0.5}), lambda: verify_range(3, 2)]
        for case in cases:
            with self.assertRaises((ValueError, TypeError)):
                case()

    def test_resource_guard_is_explicit_not_silent_truncation(self):
        with self.assertRaises(ValueError):
            graph_csf(path_graph(5), max_edges=3)
        self.assertEqual(graph_csf(path_graph(5), max_edges=None), path_csf(5))
        with self.assertRaises(ValueError):
            verify_range(0, 5, max_edges=4)

    def test_custom_range_reports_actual_cases(self):
        report = verify_range(4, 6)
        self.assertEqual(report["cases"], {"paths": 3, "cycles": 3, "three_legged_spiders": 4})
        self.assertEqual(report["identities_checked"], 16)
        self.assertEqual(verify_range(0, 0)["cases"], {"paths": 1, "cycles": 0, "three_legged_spiders": 0})


if __name__ == "__main__":
    unittest.main()

