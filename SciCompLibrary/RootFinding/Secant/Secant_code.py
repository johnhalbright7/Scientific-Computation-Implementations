def Secant(f, x_0, x_1, tol = 1e-8, maxiter = 500):
    """Finds the root of a given function using the secant method"""
    if (abs(f(x_0)) < tol):
        return(x_0)
    if (abs(f(x_1)) < tol):
        return(x_1)
    else:
        x_n1 = x_0
        x_n = x_1
        for i in range(maxiter):
            temp = x_n
            x_n = x_n - f(x_n)*((x_n - x_n1) / (f(x_n) - f(x_n1)))
            if f(x_n) < tol:
                return(x_n)
            x_n1 = temp
        print("Maximum Iterations Reached")
        return(x_n)
