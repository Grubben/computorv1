from Monomial import *

def pos_sqrt(num, tolerance, max_iter):
    lo, hi = 0.0, max(1.0, num)
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        sq = mid * mid

        if abs(sq - num) <= tolerance * max(num, 1.0):
            # I need to multiply the tolerance because:
                # - for big numbers the tolerance is too small
                # - for small numbers tolerance is too big
            return (mid, -mid)

        if sq < num:
            lo = mid
        else:
            hi = mid

    mid = 0.5 * (lo + hi)
    return (mid, -mid)

def norm_complex(z: complex) -> complex:
    re = 0.0 if z.real == 0.0 else z.real
    im = 0.0 if z.imag == 0.0 else z.imag
    return complex(re, im)

def neg_sqrt(num, tolerance, max_iter):
    pos_val = -num
    r1, r2 = pos_sqrt(pos_val, tolerance, max_iter)
    return (norm_complex(r1*1j), norm_complex(r2*1j))

def sqrt_guess(num, tolerance=1e-12, max_iter=200):
    #TODO: wait what?? what have i been doing? why am i outputting 2 options???
    if num == 0:
        return (0.0, 0.0)
    
    elif num > 0:
        return pos_sqrt(num, tolerance, max_iter)

    else:
        return neg_sqrt(num, tolerance, max_iter)


def solve2ndEquation(poly: list[Monomial]):
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
    
