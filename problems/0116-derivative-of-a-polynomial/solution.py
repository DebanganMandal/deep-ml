import math as m
def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * (n * m.pow(x,(n-1)))