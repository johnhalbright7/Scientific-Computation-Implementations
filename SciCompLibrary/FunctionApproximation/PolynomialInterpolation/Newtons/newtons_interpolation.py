import numpy as np

def divided_difference(data):
    """Given data it computes the divided difference
    given by [y0,...,yn] recursively (data size > 1)"""
    n = len(data)
    split1 = data[0:n]
    split2 = data[1:n+1]
    return((divided_difference(split2) - divided_difference(split1)) / (data[n-1][0] - data[0][0]))

def newton_coefficients(data):
    """Given data it computes the coefficients for
    Newton form interpolation via divided differences"""
    coefs = np.zeros(len(data))
    coefs[0] = data[0][1]
    for k in range(len(data)):
        coefs[k+1] = divided_difference(data[0:(k+2)])
    return(coefs)
#not checked yet