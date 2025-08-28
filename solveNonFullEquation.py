from Monomial import *
from sqrt_guess import sqrt_guess
def solveC(poly:list[Monomial]) -> None :
    if poly[0].coefficient == 0:
        print("Any real number is a solution")
    else:
        print("No solution.")

def solveB(poly:list[Monomial]) -> None :
    print("0")

def solveBC(poly:list[Monomial]) -> None :
    sol = - poly[0].coefficient / poly[1].coefficient
    print(f"{smart_format(sol)}")

def solveA(poly:list[Monomial]) -> None :
    print("0")

def solveAB(poly:list[Monomial]) -> None :
    solveB(poly)
    solveBC(poly)

def solveAC(poly:list[Monomial]) -> None :
    sol1, sol2 = sqrt_guess(- poly[0].coefficient / poly[1].coefficient)
    print(sol1)
    print(sol2)

def solveNonFullEquation(poly: list[Monomial]) -> None :
    maxExp = max(poly).exponent
    if maxExp < 1:
        solveC(poly)
        return

    print("The solution is")
    if maxExp == 1:
        if len(poly) == 1:
            solveB(poly)
        else:
            solveBC(poly)
    elif maxExp == 2:
        if len(poly) == 1:
            solveA(poly)
        elif poly[0].exponent != 0:
            solveAB(poly)
        else:
            solveAC(poly)  
    else:
        raise ValueError("Equation should not have reached here")
    
    