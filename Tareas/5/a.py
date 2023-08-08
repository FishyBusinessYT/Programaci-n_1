def factorial(n):
    for i in range(1, n):
        n *= i
    return n if n else 1
def firstFunc(n):
    return None if n == 2 else factorial(n) * n**(2-1)/factorial(n) - 2