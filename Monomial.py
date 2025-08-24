from dataclasses import dataclass
from logging import *
from typing import *

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
