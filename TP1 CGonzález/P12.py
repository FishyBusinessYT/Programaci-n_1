# Documentación en el archivo P1

while True:
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        break
    except ValueError:
        print("¡Esa edad no vale!")

# El concepto es el mismo del punto anterior, pero con más chequeos.

if edad < 4:
    print("¡No te hace falta pagar!")
    quit()
elif edad < 18:
    print("El precio para menores es de $50.")
    quit()
elif edad >= 18:
    print("El precio para mayores de edad es de $100.")
    quit()
