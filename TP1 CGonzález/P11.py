# Documentación en el archivo P1

while True:
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        break
    except ValueError:
        print("¡Esa edad no vale!")

while True:
    ingresos = input("Ingrese sus ingresos mensuales en bruto: ")
    try:
        ingresos = int(ingresos)
        break
    except ValueError:
        print("¡Eso no vale!")

# Avisarle al usuario si cumple con los requisitos para pagar impuestos y cerrar el programa.

if edad < 18 or ingresos < 80000:
    print("¡No te hace falta pagar impuestos!")
    quit()


print("Si. Ya tenés que tributar.")