from random import randint as r

números = [
    [],
    [],
    []
]

for _ in range(5):
    números[0].append(r(0, 100))

for _ in range(5):
    números[1].append(r(0, 100))

for x in range(5):
    números[2].append(números[1][x] - números[0][x])

print(números)