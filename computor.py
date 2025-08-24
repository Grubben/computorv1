#!/usr/bin/env python3
import sys
from Monomial import *
from digitize import digitize
from reduce import reduce
from polyPrint import polyPrint


basicConfig(level=INFO)



#TODO: change this section ########################################
# if len(sys.argv) < 2:
#     exit

# solutions = digitize(sys.argv[1])
digitalForm = digitize("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
###################################################################




reducedForm = reduce(digitalForm)
debug(f"reducedForm: {reducedForm}")


print("Reduced form: ", end="")
polyPrint(reducedForm)


maxExp = tryInt(max(reducedForm).exponent)
print("Polynomial degree:", maxExp)

# if maxExp == 2:
#     discriminant =