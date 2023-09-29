fib = [0, 1]
r = 0
while fib[-1] < 4000000:
    r += fib[-1] if fib[-1] % 2 == 0 else 0
    fib.append(fib[-1] + fib[-2])