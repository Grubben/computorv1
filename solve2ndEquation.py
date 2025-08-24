from Monomial import *

def mysqrt(num, *, tolerance: float = 1e-12, max_iter: int = 50):
    # Convert input to complex if necessary
    if isinstance(num, (int, float)):
        if num < 0:
            num = complex(num, 0)
        else:
            num = float(num)
    else:
        num = complex(num)

    if num == 0:
        return (0, 0)

    # Initial guess
    g = num if abs(num) >= 1 else 1

    for _ in range(max_iter):
        g_next = 0.5 * (g + num / g)
        if abs(g_next - g) <= tolerance * max(abs(g_next), 1.0):
            root = g_next
            return (root, -root)
        g = g_next

    # fallback (shouldn’t really happen)
    return (g, -g)


def solve2ndEquation(poly: list[Monomial]):
    discriminant = poly[1].coefficient * poly[1].coefficient - 4 * poly[2].coefficient * poly[0].coefficient
    debug(discriminant)

    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
    elif discriminant == 0:
        print("Discriminant is zero, the only solution is:")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")

    print(mysqrt(5), mysqrt(37), mysqrt(36), mysqrt(-4), mysqrt(-7))