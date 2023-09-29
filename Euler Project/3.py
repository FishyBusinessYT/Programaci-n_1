prim = []
for i in range(2, 10000):
    isprim = True
    for p in prim:
        if i%p == 0:
            isprim = False
            break
    if isprim:
        prim.append(i)

n = 600851475143
largest = 0

while n > 0:
    infloop = True
    for p in prim:
        if n%p == 0:
            n /= p
            largest = max(largest, p)
            infloop = False
            break
    if infloop:
        break

print(largest, n)