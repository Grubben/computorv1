from Monomial import *

def solve0dEquation(poly:list[Monomial]) -> None :
    if poly[0].coefficient == 0:
        print("Any real number is a solution")
    else:
        print("No solution.")

def solve1dEquation(poly: list[Monomial]) -> None :
    if len(poly) == 1:
        solve0dEquation(poly)
    else:
        sol = - poly[0].coefficient / poly[1].coefficient
        print("The solution is")
        print(f"{sol:.7g}")
    
    