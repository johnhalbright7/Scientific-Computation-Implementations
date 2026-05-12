def Newtons(f, df, x_0, tol = 1e-8, maxiter = 500):
    """Applies Newton's method to f using an initial guess x_0"""
    x = x_0
    if abs(f(x_0)) < tol:
        return(x_0)
    else:
        for i in range(maxiter):
            x = x - f(x) / df(x)
            if abs(f(x)) < tol:
                return(x)
    print("Maximum Iterations Reached")
    return(x)