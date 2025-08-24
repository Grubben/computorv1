#!/usr/bin/env python3
import sys
from typing import *
from dataclasses import dataclass

@dataclass(order=True)
class Monomial:
    exponent:       float = 0
    coefficient:    float = 0
# print(Monomial(5).exponent, Monomial(5 ,4).exponent, Monomial(exponent=3).coefficient)

import logging
from logging import debug

logging.basicConfig(level=logging.DEBUG)




def digitize(equation: str) -> list[Monomial | Literal['='] ]:
    # print(equation)
    poly : list[Monomial] = []

    exprs = equation.split()
    # Not Necessary: exprs = [expr for expr in sys.argv[1].split(" ") if expr != "" ]
    print(exprs)

    i : int = 0
    while i < len(exprs):
        # print(exprs[i])
        if exprs[i] == "=":
            poly.append(
                "="
            )
        else:
            poly.append(
                Monomial(0, 1)
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
    return poly

#TODO: change this section ########################################
# if len(sys.argv) < 2:
#     exit

# solutions = digitize(sys.argv[1])
digitalForm = digitize("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
###################################################################

def additiveInvert(poly: list[Monomial]) -> list[Monomial]:
    # for monom in poly:
    #     monom.coefficient *= -1
    # return poly
    return [Monomial(m.exponent, -m.coefficient) for m in poly]

def simplify(poly: list[Monomial]) -> list[Monomial]:
    i: int = 0
    while i < len(poly):
        for m in poly:
            if poly[i] != m and poly[i].exponent == m.exponent:
                poly[i].coefficient += m.coefficient
                poly.remove(m)
        i += 1
        

def reduce(digiPoly: list[Monomial | Literal['=']]) -> list[Monomial]:
    try:
        eq_idx = digiPoly.index("=")
    except ValueError:
        #TODO: make this more robust
        print("No equal found")
        eq_idx = len(digiPoly)
    left = digiPoly[:eq_idx]
    right = digiPoly[eq_idx + 1:]
    debug(f"left: {left}")
    debug(f"right: {right}")

    right = additiveInvert(right)
    debug(f"right's additive inversion: {right}")

    left.extend(right)
    debug(f"before simplification: {left}")

    simplify(left)
    debug(f"simplifiedLeft: {left}")

    return sorted(left)



reducedForm = reduce(digitalForm)
debug(f"reducedForm: {reducedForm}")



# polyPrint(reducedForm)


def tryInt(num: int | float) -> int | float:
    if isinstance(num, float):
        return int(num) if num.is_integer() else num
    return num
maxExp = max(reducedForm).exponent
print("Polynomial degree:", tryInt(maxExp) )
