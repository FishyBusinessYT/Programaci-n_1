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
        if n2 == 0:                             # Variación: Acá revisamos que el divisor no sea 0.
            raise ZeroDivisionError
        break
    except ValueError:
        print("¡Eso no vale!")
    except ZeroDivisionError:                   # El tipo de error usado es irrelevante.
        print("¡No se puede dividir por 0!")

print("La división de ambos es", n1/n2)         # Imprimir el resultado.
print(
    "¡División exacta!" if n1%n2 == 0           # Si la división entre ambos no tiene resto, es exacta
    else "", end="")                            # y lo escribimos por la consola.