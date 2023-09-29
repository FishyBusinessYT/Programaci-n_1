continueLoop = True
n = 0
while continueLoop:
    continueLoop = False
    n += 20
    for i in range(1, 20):
        if n%i != 0:
            continueLoop = True
            break

print(n)