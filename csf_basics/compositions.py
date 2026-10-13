"""Ordered compositions and standard weights; see docs/formulas.md."""
from collections.abc import Iterable, Iterator
from math import prod
from operator import index


def integer(value: int, name: str, minimum: int = 0) -> int:
    """Accept exact integer-like inputs (including Sage integers), not floats/bools."""
    if isinstance(value, bool):
        raise TypeError(f"{name} must be an integer, not bool")
    try:
        value = index(value)
    except TypeError as exc:
        raise TypeError(f"{name} must be an integer") from exc
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def composition(parts: Iterable[int]) -> tuple[int, ...]:
    """Validate positive parts, preserving their order. The empty tuple is allowed."""
    return tuple(integer(part, "part", 1) for part in parts)


def compositions(n: int, *, min_part: int = 1) -> Iterator[tuple[int, ...]]:
    """Generate every ordered composition of n once, in lexicographic order.

    compositions(0) yields (). No recursion-depth or preset order limit is used.
    There are 2**(n-1) compositions when n > 0 and min_part == 1.
    """
    n = integer(n, "n")
    min_part = integer(min_part, "min_part", 1)
    if n == 0:
        yield ()
        return
    prefix: list[int] = []
    remaining, candidate = n, min_part
    while True:
        if candidate <= remaining:
            if candidate == remaining:
                yield tuple(prefix + [candidate])
                candidate += 1
            elif remaining - candidate >= min_part:
                prefix.append(candidate)
                remaining -= candidate
                candidate = min_part
            else:
                candidate = remaining
        elif prefix:
            last = prefix.pop()
            remaining += last
            candidate = last + 1
        else:
            return


def weight(parts: Iterable[int]) -> int:
    """w_I = i_1 product_{j>=2}(i_j-1); use w_()=1 for the empty graph."""
    parts = composition(parts)
    return parts[0] * prod(part - 1 for part in parts[1:]) if parts else 1


def theta(parts: Iterable[int], a: int) -> int:
    """First prefix sum >= a, minus a; require 0 <= a <= sum(parts)."""
    parts = composition(parts)
    a = integer(a, "a")
    if a > sum(parts):
        raise ValueError("a must not exceed the sum of the composition")
    total = 0
    for part in parts:
        if total >= a:
            break
        total += part
    return total - a

