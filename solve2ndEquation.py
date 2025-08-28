from Monomial import *
from sqrt_guess import sqrt_guess

def solve2ndEquationFull(poly: list[Monomial]):
    discriminant = poly[1].coefficient * poly[1].coefficient - 4 * poly[2].coefficient * poly[0].coefficient
    debug(discriminant)

    dsq, _ = sqrt_guess(discriminant) # discriminant_sqrt
    sol1 = (- poly[1].coefficient + dsq) / (2* poly[2].coefficient)
    sol2 = (- poly[1].coefficient - dsq) / (2* poly[2].coefficient)
    debug(sol1)
    debug(sol2)

    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"{smart_format(sol1)}")
        print(f"{smart_format(sol2)}")
    elif discriminant == 0:
        print("Discriminant is zero, the only solution is:")
        print(f"{smart_format(sol1)}")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{smart_format(sol1)}")
        print(f"{smart_format(sol2)}")



import cmath
if __name__ == "__main__":
    print(sqrt_guess(5))
    print(sqrt_guess(37))
    print(sqrt_guess(36))
    print(sqrt_guess(-4))
    print(sqrt_guess(-7))
    
