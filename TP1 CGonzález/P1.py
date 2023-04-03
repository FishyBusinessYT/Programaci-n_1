# IMPORTANTE: No creo que haga falta copiar y pegar la explicación de el siguiente bucle en todos los ejercicios.
# Cuando sea usado, en lugar de la explicación va a haber una referencia a este archivo.
# Gracias.

while True:                                             # Iniciamos un bucle infinito en caso de que algo falle.
    edad = input("Ingrese su edad: ")                   # Guardamos la edad del usuario en una variable.
    try:
        edad = int(edad)                                # Verificamos que sea un número entero.
        break
    except ValueError:
        print("¡Esa edad no vale!")                     # Si no lo es, le avisamos y empezamos de nuevo hasta que lo sea.

print(
    "Sos mayor de edad." if edad > 17 and edad < 100    # Si la edad del usuario es mayor a 17, es mayor.
    else "Sos menor de edad.")                          # Si no, es menor.