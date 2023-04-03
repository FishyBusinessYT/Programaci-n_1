from datetime import datetime

año = datetime.now().year                       # Obtener el año actual con la librería /datetime/

# Documentación en el archivo P1

while True:
    año2 = input("Ingresar el año a comparar: ")
    try:
        año2 = int(año2)
        break
    except ValueError:
        print("¡Eso no vale!")

diferencia = año - año2

if abs(diferencia) == 1:                                                # Si hay una diferencia de uno entre los años:
    print(
    f"Falta 1 año para que sea {año2}." if año < año2                   # Si año es menor a año2, año2 es en el futuro.
    else f"{año2} fue hace 1 año." if año > año2                        # Si no, año2 es en el pasado.
    else f"Ya es {año2}"                                                # Si no, es este año.
    )
    quit()

# Misma lógica, pero para cuando la diferencia es mayor a un año.

print(
    f"Flatan {-diferencia} años para que sea {año2}." if año < año2
    else f"{año2} fue hace {diferencia} años." if año > año2
    else f"Ya es {año2}"
    )