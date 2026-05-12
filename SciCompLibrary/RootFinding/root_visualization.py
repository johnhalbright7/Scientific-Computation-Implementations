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
zoom = 0
for result in bi.bisection_iteration(f, -0.9, 1.0):
    if type(result) == tuple: # The recursion isn't done
        plt.axvline(result[0], color='g')
        plt.axvline(result[1], color='g')
        if zoom % 5 == 0 and zoom > 1:
            max_buffer = max(abs(result[0]/2), abs(result[1]/2))
            plt.xlim(result[0]-max_buffer, result[1]+max_buffer)
        fig.canvas.draw()
        plt.pause(0.5)
    elif type(result) == float:
        root = result
    zoom+=1
        

print('Point found!')
plt.plot(root, f(root))
plt.show()