#!/usr/bin/env python3
import sys

from dataclasses import dataclass
@dataclass
class Monomial:
    coefficient:    float = 0
    exponent:       float = 0
# print(Monomial(5).exponent, Monomial(5 ,4).exponent, Monomial(exponent=3).coefficient)

import logging
from logging import debug

logging.basicConfig(level=logging.DEBUG)




def computor(equation: str):
    # print(equation)
    poly : list[Monomial] = []

    exprs = equation.split()
    # Not Necessary: exprs = [expr for expr in sys.argv[1].split(" ") if expr != "" ]
    print(exprs)

    i : str = 0
    while i < len(exprs):
        # print(exprs[i])
        if exprs[i] == "=":
            poly.append(
                "="
            )
        else:
            poly.append(
                Monomial(1)
            )
            if exprs[i] == "-":
                debug(f"Creating negative polynomial")
                poly[-1].coefficient = -1
                i += 1
            elif exprs[i] == "+":
                debug(f"Creating positive polynomial")
                i += 1
            # else:
            debug(f"{exprs[i]}")
            poly[-1].coefficient *= float(exprs[i])
            poly[-1].exponent = float(exprs[i + 2][2:]) #TODO: check negative and fraction exps
            i += 2
        i += 1
    print(poly)







# if len(sys.argv) < 2:
#     exit

solutions = computor("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
# solutions = computor(sys.argv[1])

