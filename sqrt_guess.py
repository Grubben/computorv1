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

def sqrt_guess(num, tolerance=1e-12, max_iter=200) -> tuple[float, float] | tuple[complex, complex]:
    #TODO: wait what?? what have i been doing? why am i outputting 2 options???
    if num == 0:
        return (0.0, 0.0)
    
    elif num > 0:
        return pos_sqrt(num, tolerance, max_iter)

    else:
        return neg_sqrt(num, tolerance, max_iter)
