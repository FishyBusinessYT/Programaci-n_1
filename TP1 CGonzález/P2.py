# Documentación en el archivo P1

while True:
    n1 = input("Ingrese un número: ")
    try:
        n1 = float(n1)
        break
    except ValueError:
        print("¡Eso no vale!")

while True:
    n2 = input("Ingrese otro número: ")
    try:
        n2 = float(n2)
        break
    except ValueError:
        print("¡Eso no vale!")

print(
    "El primero es mayor al segundo." if n1 > n2            # Se explica solo. Revisamos qué número es mayor
    else "El segundo es mayor al primero." if n2 > n1       # y lo escribimos en la consola.
    else "Son iguales.")                                    # Escribimos que son iguales, si lo son.