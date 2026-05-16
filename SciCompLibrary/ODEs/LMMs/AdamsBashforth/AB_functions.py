import numpy as np

def AB_1(f, k, eta, tspan):
    """First order Adams-Bashforth (Forward Euler)"""
    U_0 = eta
    U = np.zeros(int(np.ceil((tspan[1] - tspan[0])/k)+1))
    U[0] = U_0
    U[1] = U_0 + k*f(U_0)
    for n in np.arange(2,int(np.ceil((tspan[1] - tspan[0])/k)+1)):
        U[n] = U[n-1] + k*f(U[n-1])
    return(U)

    