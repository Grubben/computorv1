from Monomial import *


def digitize(equation: str) -> list[Monomial | Literal['='] ]:
    print(equation)
    poly : list[Monomial | Literal['=']] = []

    exprs = equation.split()
    # Not Necessary: exprs = [expr for expr in sys.argv[1].split(" ") if expr != "" ]
    debug(exprs)

    i : int = 0
    while i < len(exprs):
        # print(exprs[i])
        if exprs[i] == "=":
            poly.append(
                "="
            )
        else:
            if exprs[i] == "0" and i == len(exprs) -1:
                break
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
            poly[-1].coefficient *= Fraction(exprs[i])
            poly[-1].exponent = Fraction(exprs[i + 2][2:]) #TODO: check negative and fraction exps
            i += 2
        i += 1
    debug(poly)
    return poly