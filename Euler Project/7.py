#Find the 10001st prime number
prims = []
for i in range(2, 110000):
    isprim = True
    for p in prims:
        if i%p == 0:
            isprim = False
            break
    if isprim:
        prims.append(i)
print(len(prims))
print(prims[10000])