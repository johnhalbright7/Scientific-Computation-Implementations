import numpy as np
import Secant_code

def f(x):
    return(x**3)

root = Secant_code.Secant(f,1.0, 2.0, tol = 1e-15) # notice it cubes tolerance
print(root)