from dataclasses import dataclass
from logging import debug
from typing import Literal, Union
from fractions import Fraction


class MyFraction(Fraction):
    def __new__(cls, numerator=0, denominator=None):
        return super().__new__(cls, numerator, denominator)
    
    def is_integer(self) -> bool:
        return self.denominator == 1
    
    @classmethod
    def from_fraction(cls, frac: Fraction) -> "MyFraction":
        # Create MyFraction from numerator and denominator of the Fraction
        return cls(frac.numerator, frac.denominator)

def smart_format(sol: Fraction | MyFraction | float | complex) -> str:
    if isinstance(sol, complex):
        real = float(sol.real)
        imag = float(sol.imag)
        return f"{real:.7g} + {imag:.7g}j"
    elif isinstance(sol, Fraction):
        return f"{float(sol):.7g}"
    else:
        return f"{sol:.7g}"

def tryInt(num: int | float | Fraction, wantAbs=False) -> str:
    """
        Prepares a number for representation in program. Cuts all unnecessary extra zeros.
        2.0 -> 2
        2   -> 2
        2/3 -> 2/3
    """
    if isinstance(num, int):
        final = num
    else:
        if isinstance(num, Fraction):
            num = MyFraction.from_fraction(num)
        if num.is_integer():
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
        return f"{tryInt(self.coefficient, True)} * X^{tryInt(self.exponent, True)}"
# debug(Monomial(5).exponent, Monomial(5 ,4).exponent, Monomial(exponent=3).coefficient)
