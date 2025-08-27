from dataclasses import dataclass
from logging import debug
from typing import Literal
from fractions import Fraction

def tryInt(num: int | float | Fraction, wantAbs=False) -> str:
    """
        Prepares a number for representation in program. Cuts all unnecessary extra zeros.
        2.0 -> 2
        2   -> 2
        2/3 -> 2/3
    """
    if isinstance(num, int):
        final = num
    elif num.is_integer():
        final = int(num)
    else:
        final = num
    
    if wantAbs:
        return str(abs(final))
    return str(final)

@dataclass(order=True)
class Monomial:
    exponent:       float | Fraction = 0
    coefficient:    float | Fraction = 0

    def __str__(self) -> str:
        # I need the abs because of the project output "specifications". I'm playing it safe
        return f"{tryInt(float(self.coefficient), True)} * X^{tryInt(self.exponent, True)}"
# debug(Monomial(5).exponent, Monomial(5 ,4).exponent, Monomial(exponent=3).coefficient)
