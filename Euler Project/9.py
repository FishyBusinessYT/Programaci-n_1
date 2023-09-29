from time import perf_counter_ns as time

start = time()
for c in range(335, 501):
    for b in range((1000-c)//2, 1000-c):
        a = 1000-c-b
        if a*a + b*b == c*c:
            print(a, b, c)
end = time()

print(end - start)