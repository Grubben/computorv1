#!/usr/bin/env python3
import sys
from Monomial import *
from logging import basicConfig, INFO
from digitize import digitize
from reduce import reduce
from polyPrint import polyPrint, hasWeird
from solve2ndEquation import solve2ndEquation
from solve1dEquation import solve1dEquation
basicConfig(level=INFO)


def computor(equation: str):
    digitalForm = digitize(equation)

    reducedForm = reduce(digitalForm)
    debug(f"reducedForm: {reducedForm}")

    print("Reduced form: ", end="")
    polyPrint(reducedForm)


    if weird := hasWeird(reducedForm):
        print(f"Polynomial degree is not specified for there is a fractional exponent: {weird}")
        return

    maxMonom = max(reducedForm)
    if isinstance(maxMonom.exponent, Fraction) and not MyFraction.from_fraction(maxMonom.exponent).is_integer():
        #TODO: this needs to be reworked since I made the hasWeird
        print(f"Polynomial degree is not specified for there is a fractional exponent: {maxMonom.exponent}")
        return
    elif maxMonom.exponent > 0:
        print("Polynomial degree:", tryInt(maxMonom.exponent))

    if maxMonom.exponent < 0:
        raise ValueError("Polynomial degree cannot be less than 0.")
    elif len(reducedForm) < 2 or maxMonom.exponent < 2:
        solve1dEquation(reducedForm)
    # elif len(reducedForm) < 2:
    #     solve1dEquation(reducedForm)
    elif maxMonom.exponent == 2:
        solve2ndEquation(reducedForm)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    print()

# computor("4 * X^2/3 - 8 * X^0 = 0")
# print()
# computor("2/3 * X^2 = 0")
# print()
# computor("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
# print()
# computor("5 * X^0 + 4 * X^1 = 4 * X^0")
# print()
# computor("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
# print()
# computor("6 * X^0 = 6 * X^0")
# print()
# computor("10 * X^0 = 15 * X^0")
# print()
# computor("1 * X^0 + 2 * X^1 + 5 * X^2 = 0")

# computor("3 * X^0 + 2 * X^1 + 7 * X^-2 = -4 * X^0")
# print()
# computor("- 3 * X^0 - 2 * X^1 - 7 * X^2 = - 4 * X^0")
# print()

computor("2/3 * X^0 + 5/6 * X^1 + 9/7 * X^2 = 5/4 * X^2 - 123/7 * X^1/4")
print()

if len(sys.argv) < 2:
    exit(1)
else:
    computor(sys.argv[1])