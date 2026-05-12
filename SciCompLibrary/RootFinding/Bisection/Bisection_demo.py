import numpy as np
import Bisection_code

def f(x):
    return(x+np.sin(x)) # unique root at 0

root = Bisection_code.bisection(f, -0.9, 1.0)
print(root)

