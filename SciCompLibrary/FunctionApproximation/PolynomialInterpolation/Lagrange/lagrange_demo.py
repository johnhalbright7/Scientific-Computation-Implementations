import numpy as np
import lagrange_interpolant
import matplotlib.pyplot as plt

data = np.array([[-2, -1], [0, 2], [3, 1]]) 
nodes = np.array([data[i][0] for i in range(len(data))])
ys = np.array([data[i][1] for i in range(len(data))])

f = lagrange_interpolant.Lagrange_interpolant(nodes, ys)

plt.grid(True)
plt.plot(np.linspace(-4, 4, 1000), f(np.linspace(-4, 4, 1000)))
plt.plot(nodes, ys, marker='x', color='red', linestyle = '')
plt.show()