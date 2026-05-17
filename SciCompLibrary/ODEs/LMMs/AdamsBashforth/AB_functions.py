import numpy as np

def AB_1(f, k, eta, tspan):
    """First order Adams-Bashforth (Forward Euler)"""
    U = np.zeros(int(np.ceil((tspan[1] - tspan[0])/k)+1))
    U[0] = eta
    for n in np.arange(1,int(np.ceil((tspan[1] - tspan[0])/k)+1)):
        U[n] = U[n-1] + k*f(U[n-1])
    return(U)

def AB_2(f, k, eta, tspan):
    """Second order Adams-Bashforth
    eta is a vector of U0, U1 as needed"""
    U = np.zeros(int(np.ceil((tspan[1] - tspan[0])/k)+1))
    U[0] = eta[0]
    U[1] = eta[1]
    for n in np.arange(2,int(np.ceil((tspan[1] - tspan[0])/k)+1)):
        U[n] = U[n-1] + (k / 2)*(-f(U[n-2]) + 3*f(U[n-1]))
    return(U)