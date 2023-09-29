tup1 = (1, 2)
tup2 = (3, 4)

print(tup2)
print(tup1)

## Alternativa:

tup3 = tup1
tup1 = tup2
tup2 = tup3

print(tup1)
print(tup2)

#Suma de tuplas

tup1 = (2, 3, 4, 5, 5, 1, 5)
tup2 = (4, 6, 1, 4, 9, 2, 7)



tup3 = tuple(tup1[x] + tup2[x] for x in range(len(tup1)))

print(tup3)

#Tuple a lista

tup1 = tuple(int(input()) for i in range(3))
ls = list(tup1)

print(ls)

#Mayor valor y menor valor

tup1 = (10, 7, 3, 6, 1, 45, 64, -14, 1431, 45, 35, 35, 234, 2, 14, 12, 7, -75, 2, 57, 474, 15, 1345, 346)

print(max(tup1))
print(min(tup1))