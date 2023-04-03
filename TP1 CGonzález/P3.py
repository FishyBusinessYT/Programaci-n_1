# Documentación en el archivo P1

while True:
    nro = input("Ingrese un número entero: ")
    try:
        nro = int(nro)
        break
    except ValueError:
        print("¡Ese no vale!")

print("Es par." if nro % 2 == 0 else "Es impar.")       # Si el resto de la división entre N y 2 es 0, N es par.