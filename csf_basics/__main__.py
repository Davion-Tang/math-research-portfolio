"""Run with python -m csf_basics; use --help for examples and inclusive bounds."""
import argparse
import json

from . import cycle_csf, format_e, path_csf, spider_csf, weighted_e_terms
from .verification import verify_range


def main():
    parser = argparse.ArgumentParser(description="Exact public CSF basics / 色对称函数基础计算")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for family in ("path", "cycle", "terms"):
        command = subparsers.add_parser(family)
        command.add_argument("n", type=int, help="number of vertices / composition sum")
        if family == "terms":
            command.add_argument("--include-zero", action="store_true")
    spider = subparsers.add_parser("spider")
    spider.add_argument("a", type=int)
    spider.add_argument("b", type=int)
    spider.add_argument("c", type=int)
    verify = subparsers.add_parser("verify", help="inclusive finite graph-order checks")
    verify.add_argument("--min-order", type=int, default=0)
    verify.add_argument("--max-order", type=int, default=10)
    verify.add_argument("--max-edges", type=int, default=18,
                        help="adjustable budget for the exponential independent reference")
    args = parser.parse_args()
    try:
        if args.command == "verify":
            print(json.dumps(verify_range(args.min_order, args.max_order, max_edges=args.max_edges), indent=2))
        elif args.command == "terms":
            for term in weighted_e_terms(args.n, include_zero=args.include_zero):
                print(f"I={term.composition}, w_I={term.coefficient}, e_index={term.e_index}")
        else:
            poly = (spider_csf(args.a, args.b, args.c) if args.command == "spider" else
                    path_csf(args.n) if args.command == "path" else cycle_csf(args.n))
            print(format_e(poly))
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()

