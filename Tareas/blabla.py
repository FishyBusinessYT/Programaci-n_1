lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sumapares = 0
sumaimpares = 0

for y in lista:
    for x in y:
        if x % 2 == 0:
            sumapares += x
            continue
        sumaimpares += x

print(sumapares)
print(sumaimpares)