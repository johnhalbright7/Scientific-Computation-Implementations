def D1O1(f, x_0, h):
    """First order approximation of the first derivative of f"""
    return((f(x_0+h) - f(x_0)) / h)

def D1O2(f, x_0, h):
    """Second order approximation of the second derivative of f"""
    return((f(x_0 - h) + f(x_0+h)) / (2*h))

def D2O1(f, x_0, h):
    """First order approximation of the second derivative of f"""
    return((f(x_0 - h) - 2*f(x_0) + f(x_0+h)) / (h **2))