from random import randint as r

lista = [r(1, 10) for i in range(3)]

minimo = 10
maximo = 0

for i in lista:
    if i > maximo:
        maximo = i
    
    if i < minimo:
        minimo = i

print(minimo, maximo)