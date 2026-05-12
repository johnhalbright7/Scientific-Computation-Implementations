def basis_func(nodes, j):
    """Creates Specified Lagrange Basis Function"""
    def f_j(x):
        f = 1.0
        for i in range(len(nodes)):
            if (i) != j:
                f *= ((x-nodes[i]) / (nodes[j] - nodes[i]))
        return f
    return f_j

def Lagrange_interpolant(nodes, ys):
    """Creates interpolating polynomial using Lagrange basis functions"""
    return lambda x: sum(ys[i]*basis_func(nodes, i)(x) for i in range(len(nodes)))
