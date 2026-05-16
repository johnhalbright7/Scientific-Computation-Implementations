import AB_functions
import numpy as np
import matplotlib.pyplot as plt

def f(u): # u' = -1* u
    return(-1*u) # solution is u(t) = e^{-(t-1)}*eta

U_pred = AB_functions.AB_1(f, 0.01, 1, np.array([1, 2]))
U_true = np.exp(-(np.arange(1, 2.01, 0.01)-1))
plt.plot(np.arange(1, 2.01, 0.01), U_pred, linewidth = 3)
plt.plot(np.arange(1, 2.01, 0.01), U_true, linewidth = 3, linestyle = "dashed")
plt.show()