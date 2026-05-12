import matplotlib.pyplot as plt
import numpy as np

import Bisection.Bisection_code as bi

x = np.linspace(-5, 5, 1000)
y = x ** 2

def f(x):
    return(x+np.sin(x)) # unique root at 0

fig = plt.figure(figsize = (10, 5))
plt.ion()
plt.grid(True)
plt.plot(x, x+np.sin(x))
plt.show()
plt.pause(2)
root = 0
for result in bi.bisection_iteration(f, -0.9, 1.0):
    if type(result) == tuple: # The recursion isn't done
        plt.axvline(result[0])
        plt.axvline(result[1])
        fig.canvas.draw()
        plt.pause(0.5)
    elif type(result) == float:
        root = result
        

print('Point found!')
plt.plot(root, f(root))
plt.show()