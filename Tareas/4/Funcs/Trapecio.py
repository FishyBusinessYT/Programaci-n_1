def calc(l, a):
    L = -(l**2 - a**2) ** (1/2)
    p = l*3 + L
    A = p*a/2
    return p, A, L