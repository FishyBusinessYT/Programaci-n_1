def get(text):
    result = int
    while True:
        try:
            result = input(text)
            result = int(result)
            break
        except ValueError:
            if result == "exit":
                exit()
    return result

while True:
    t1 = get("Ingresar suma de incógnitas: ")
    t2 = get("Ingresar suma ponderada: ")
    w1 = get("Ingresar ponderación de la primera incógnita: ")
    w2 = get("Ingresar ponderación de la segunda incógnita: ")

    x = w2*t1-t2
    x /= w1 - w2
    x *= -1
    y = t1-x

    print("\n\n x =", x)
    print("\n\n y =", y)