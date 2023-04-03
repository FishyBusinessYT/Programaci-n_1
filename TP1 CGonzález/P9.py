# Documentación en el archivo P1

while True:
    año = input("Ingresar un año: ")
    try:
        año = int(año)
        break
    except ValueError:
        print("¡Eso no vale!")

# Guardar si es múltiplo de 4, 400, y 100 en sus respectivas variables.

mult4 = True if año % 4 == 0 else False
mult400 = True if año % 400 == 0 else False
mult100 = True if año % 100 == 0 else False

# Si es múltiplo de 400 o es múltiplo de 4 y no de 100, es bisiesto.

print(
    "Es bisiesto." if mult400 or (mult4 and not mult100) 
    else "No es bisiesto.")