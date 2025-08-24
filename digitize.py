from typing import *
from dataclasses import dataclass
from logging import *

def tryInt(num: int | float) -> int | float:
    if isinstance(num, float):
        return int(num) if num.is_integer() else num
    return num


@dataclass(order=True)
class Monomial:
    exponent:       float = 0
    coefficient:    float = 0

    def __str__(self) -> str:
        # I need the abs because of the project output "specifications". I'm playing it safe
        return f"{abs(tryInt(self.coefficient))} * X^{abs(tryInt(self.exponent))}"
# debug(Monomial(5).exponent, Monomial(5 ,4).exponent, Monomial(exponent=3).coefficient)


def digitize(equation: str) -> list[Monomial | Literal['='] ]:
    # print(equation)
    poly : list[Monomial] = []

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
    debug(poly)
    return poly