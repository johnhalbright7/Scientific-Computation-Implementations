def bisection(f, a, b, tol1 = 1e-8, tol2 = 1e-8, maxiter = 500, k=0):
    """Inputs a function f
    left and right interval points a, b, 
    and a desired tolerance. 
    Returns estimated root.
    """
    if f(a)*f(b) > 0:
        return("Bisection fails for this problem")
    elif f(a)*f(b) == 0:
        if f(a) == 0:
            return(a)
        else:
            return(b)
    else:
        c = (a+b)/2
        k = k+1
        if k >= maxiter:
            print("Maximum iterations reached, resulting root may be innacurate")
            return(c)
        if (abs(f(c)) < tol1) or (abs(c-b)<tol2):
            return(c)
        if (f(a)*f(c) ==0) or( f(c)*f(b) == 0):
            return(c)
        elif (f(a)*f(c) < 0):
            return(bisection(f, a, c, tol1, tol2, maxiter, k = k))
        else:
            return(bisection(f, c, b, tol1, tol2, maxiter, k = k))
        
            
