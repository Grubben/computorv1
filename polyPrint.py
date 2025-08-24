from Monomial import *

def polyPrint(poly: list[Monomial]) -> None:
    if poly[0].coefficient < 0:
        print("-", end="")
    print(poly[0], end="")
    for monom in poly[1:]:
        if monom.coefficient >= 0:
            print(" + ", sep="", end="")
        else:
            print(" - ", sep="", end="")
        print(monom, end='')
    print(" = 0")