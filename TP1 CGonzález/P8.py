# Documentación en el archivo P1

while True:
    n1 = input("Ingrese el primer númerro: ")
    try:
        n1 = int(n1)
        break
    except ValueError:
        print("¡Ese no vale!")

while True:
    n2 = input("Ingrese el segundo númerro: ")
    try:
        n2 = int(n2)
        break
    except ValueError:
        print("¡Ese no vale!")

while True:
    n3 = input("Ingrese el tercer númerro: ")
    try:
        n3 = int(n3)
        break
    except ValueError:
        print("¡Ese no vale!")

# Esta parte casi que se explica sola.

if n1 == n2 == n3:                      # Si los tres son iguales, sacarlo por consola.
    print("Los tres son iguales.")
elif (n1 in [n2, n3] or n2 == n3):      # Si n1 es igual a n2 o n3, o n2 y n3 son iguales, entonces hay dos números iguales.
    print("Solo hay dos iguales.")
else:                                   # En cualquier otro caso, son todos distintos.
    print("Los tres son únicos.")