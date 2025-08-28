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


def hasWeird(poly: list[Monomial]) -> float | Fraction:
    """Checks if there are fractional or negative exponents"""
    for m in poly:
        if isinstance(m.exponent, Fraction):
            m.exponent = MyFraction.from_fraction(m.exponent)
        if m.exponent < 0 or not m.exponent.is_integer():
            return m.exponent
    return Fraction("0/1")