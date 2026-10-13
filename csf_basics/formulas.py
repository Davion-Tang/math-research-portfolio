"""Published basic formulas for paths, cycles, and three-legged spiders.

Attribution and conventions are in docs/formulas.md. No paper-specific
injections, theorem verifiers, or caterpillar certificates are included.
"""
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from math import factorial

from .compositions import composition, compositions, integer, weight
from .symmetric import Polynomial, add, e_monomial, multiply, scale


@dataclass(frozen=True)
class CompositionTerm:
    """One ordered summand; the composition is retained before collection."""
    composition: tuple[int, ...]
    coefficient: int

    def __post_init__(self):
        object.__setattr__(self, "composition", composition(self.composition))
        # Standard weights in this module are nonnegative integers.
        object.__setattr__(self, "coefficient", integer(self.coefficient, "coefficient"))

    @property
    def e_index(self) -> tuple[int, ...]:
        return tuple(sorted(self.composition, reverse=True))

    def as_polynomial(self) -> Polynomial:
        return e_monomial(self.composition, self.coefficient)


def weighted_e_term(parts) -> CompositionTerm:
    """Return a single w_I e_I term with its original ordered I attached."""
    parts = composition(parts)
    return CompositionTerm(parts, weight(parts))


def weighted_e_terms(n: int, *, include_zero: bool = False):
    """Generate w_I e_I for I |= n. include_zero keeps zero-weight terms."""
    for parts in compositions(n):
        term = weighted_e_term(parts)
        if term.coefficient or include_zero:
            yield term


def cycle_e_terms(n: int, *, include_zero: bool = False):
    """Generate (i_1-1) w_I e_I for I |= n, with n >= 3."""
    n = integer(n, "n", 3)
    for parts in compositions(n):
        coefficient = (parts[0] - 1) * weight(parts)
        if coefficient or include_zero:
            yield CompositionTerm(parts, coefficient)


def collect_terms(terms) -> Polynomial:
    result = {}
    for term in terms:
        if not isinstance(term, CompositionTerm):
            raise TypeError("expected CompositionTerm objects")
        if term.coefficient:
            result[term.e_index] = result.get(term.e_index, Fraction(0)) + term.coefficient
    return result


@lru_cache(maxsize=128)
def _formula(n: int, family: str):
    # A(z) = 1 / (1 - sum_{k>=2}(k-1)e_k z^k).
    # Multiplying A by the possible first part reproduces the ordered formula.
    tails = [e_monomial(())]
    for degree in range(1, n + 1):
        tails.append(add(*(multiply(e_monomial((k,), k - 1), tails[degree-k])
                           for k in range(2, degree + 1))))
    if n == 0:
        return tuple(e_monomial(()).items())
    result = add(*(multiply(e_monomial((k,), k if family == "path" else k * (k - 1)), tails[n-k])
                   for k in range(1, n + 1)))
    return tuple(result.items())


def path_csf(n: int) -> Polynomial:
    """X_{P_n} in the e basis. n counts vertices; X_{P_0}=1."""
    return dict(_formula(integer(n, "n"), "path"))


def cycle_csf(n: int) -> Polynomial:
    """X_{C_n} in the e basis for simple cycles with n >= 3 vertices."""
    return dict(_formula(integer(n, "n", 3), "cycle"))


def complete_csf(n: int) -> Polynomial:
    """X_{K_n}=n!e_n, including X_{K_0}=1."""
    n = integer(n, "n")
    return e_monomial((n,) if n else (), factorial(n))


def spider_csf(a: int, b: int, c: int) -> Polynomial:
    """Zheng's path-product identity for S(a,b,c); legs count edges.

    Any input order is accepted. The identity uses sorted a >= b >= c >= 1.
    This signed formula calculates an instance; it is not an e-positivity proof.
    For more than three legs use graph_csf(spider_graph(*legs)).
    """
    a, b, c = sorted((integer(x, "leg length", 1) for x in (a, b, c)), reverse=True)
    n = a + b + c + 1
    result = path_csf(n)
    for i in range(1, c + 1):
        result = add(result, multiply(path_csf(i), path_csf(n-i)),
                     scale(multiply(path_csf(b+i), path_csf(n-b-i)), -1))
    return result

