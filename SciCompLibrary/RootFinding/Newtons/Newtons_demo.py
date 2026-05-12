import numpy as np
import Newtons_code

def f(x):
    return(x**3)

def df(x):
    return(3*x**2)

root = Newtons_code.Newtons(f, df, 10, tol = 1e-15) # notice it cubes tolerance
print(root)