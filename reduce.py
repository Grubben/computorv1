from Monomial import *

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
