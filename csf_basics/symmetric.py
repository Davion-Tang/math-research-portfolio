"""Sparse exact symmetric functions. A tuple key denotes a basis partition.

For example {(3, 1): 2, (2, 2): -1} represents 2 e_3 e_1 - e_2^2.
The caller specifies the basis: a bare dictionary carries no basis metadata.
"""
from collections.abc import Iterable, Mapping
from fractions import Fraction
from functools import lru_cache
from math import comb, prod
from numbers import Rational

from .compositions import composition, integer

Partition = tuple[int, ...]
Polynomial = dict[Partition, Fraction]


def _rational(value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, Rational):
        raise TypeError("coefficients must be exact integers or rational numbers")
    return Fraction(value)


def normalize(poly: Mapping[Partition, Rational]) -> Polynomial:
    result: Polynomial = {}
    for parts, coefficient in poly.items():
        key = tuple(sorted(composition(parts), reverse=True))
        result[key] = result.get(key, Fraction(0)) + _rational(coefficient)
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def e_monomial(parts: Iterable[int], coefficient: Rational = 1) -> Polynomial:
    """Return coefficient * e_I, collected at the decreasing partition of I."""
    return normalize({composition(parts): coefficient})


def add(*polynomials: Mapping[Partition, Rational]) -> Polynomial:
    result: Polynomial = {}
    for poly in polynomials:
        for key, coefficient in normalize(poly).items():
            result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def scale(poly: Mapping[Partition, Rational], scalar: Rational) -> Polynomial:
    scalar = _rational(scalar)
    return {key: scalar * value for key, value in normalize(poly).items() if scalar}


def multiply(left: Mapping[Partition, Rational], right: Mapping[Partition, Rational]) -> Polynomial:
    """Multiply in a multiplicative basis, e or p; do not mix the two bases."""
    result: Polynomial = {}
    right = normalize(right)
    for key1, value1 in normalize(left).items():
        for key2, value2 in right.items():
            key = tuple(sorted(key1 + key2, reverse=True))
            result[key] = result.get(key, Fraction(0)) + value1 * value2
    return {key: value for key, value in result.items() if value}


@lru_cache(maxsize=128)
def _power_sum_e(n: int) -> tuple[tuple[Partition, Fraction], ...]:
    # Newton identities; cached values are immutable, never exposed dictionaries.
    table = [{}]
    for degree in range(1, n + 1):
        result = e_monomial((degree,), (-1) ** (degree - 1) * degree)
        for i in range(1, degree):
            result = add(result, scale(multiply(e_monomial((i,)), table[degree-i]), (-1) ** (i-1)))
        table.append(result)
    return tuple(table[n].items())


def power_sum_e(n: int) -> Polynomial:
    """Return p_n in the e basis, for n >= 1."""
    return dict(_power_sum_e(integer(n, "n", 1)))


def p_to_e(poly: Mapping[Partition, Rational]) -> Polynomial:
    """Convert a p-basis dictionary to an e-basis dictionary by Newton identities."""
    result: Polynomial = {}
    for parts, coefficient in normalize(poly).items():
        term = e_monomial((), coefficient)
        for part in parts:
            term = multiply(term, power_sum_e(part))
        result = add(result, term)
    return result


def evaluate_e(poly: Mapping[Partition, Rational], values: Mapping[int, Rational]) -> Fraction:
    """Apply e_k -> values[k]; missing required indices raise KeyError."""
    return sum((coefficient * prod(_rational(values[k]) for k in parts)
                for parts, coefficient in normalize(poly).items()), Fraction(0))


def principal_specialization(poly: Mapping[Partition, Rational], colors: int) -> Fraction:
    """Set x_1=...=x_q=1, others 0. For a CSF this counts proper q-colorings."""
    colors = integer(colors, "colors")
    poly = normalize(poly)
    return evaluate_e(poly, {k: comb(colors, k) for parts in poly for k in parts})


def is_e_positive(poly: Mapping[Partition, Rational]) -> bool:
    """Check collected e coefficients of a specific symmetric function."""
    return all(value >= 0 for value in normalize(poly).values())


def format_e(poly: Mapping[Partition, Rational]) -> str:
    chunks = []
    for parts, coefficient in sorted(normalize(poly).items(), reverse=True):
        monomial = "*".join(f"e[{part}]" for part in parts)
        magnitude = abs(coefficient)
        term = monomial if magnitude == 1 and monomial else str(magnitude) + ("*" + monomial if monomial else "")
        prefix = ("-" if coefficient < 0 else "") if not chunks else (" - " if coefficient < 0 else " + ")
        chunks.append(prefix + term)
    return "".join(chunks) or "0"

