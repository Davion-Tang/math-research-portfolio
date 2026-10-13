"""Optional conversion to SageMath; Sage is not required by the base package."""
from .symmetric import normalize


def to_sage_e(poly):
    """Return an element of SymmetricFunctions(QQ).e() inside a Sage environment."""
    try:
        from sage.all import QQ, SymmetricFunctions
    except ImportError as exc:
        raise ImportError("This optional function requires SageMath; run with sage -python") from exc
    e = SymmetricFunctions(QQ).e()
    return sum((QQ(value.numerator) / QQ(value.denominator) * e[list(parts)]
                for parts, value in normalize(poly).items()), e.zero())

