#!/usr/bin/env python3
import sys
from Monomial import Monomial, Literal, debug, tryInt
from logging import *
from digitize import digitize
from reduce import reduce
from polyPrint import polyPrint
from solve2ndEquation import solve2ndEquation

basicConfig(level=INFO)



#TODO: change this section ########################################
# if len(sys.argv) < 2:
#     exit

# solutions = digitize(sys.argv[1])
###################################################################

def computor(equation: str):
    digitalForm = digitize(equation)

    reducedForm = reduce(digitalForm)
    debug(f"reducedForm: {reducedForm}")

    print("Reduced form: ", end="")
    polyPrint(reducedForm)

    maxExp = tryInt(max(reducedForm).exponent)
    print("Polynomial degree:", maxExp)

    if maxExp < 0:
        raise ValueError("Polynomial degree cannot be less than 0.")
    elif maxExp < 2:
        #TODO
        pass
    elif maxExp == 2:
        #TODO
        solve2ndEquation(reducedForm)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    print()

computor("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
print()
computor("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
print()
computor("6 * X^0 = 6 * X^0") #TODO: gotta fix this!
print()
computor("10 * X^0 = 15 * X^0") #TODO: gotta fix this!
print()
computor("1 * X^0 + 2 * X^1 + 5 * X^2 = 0")