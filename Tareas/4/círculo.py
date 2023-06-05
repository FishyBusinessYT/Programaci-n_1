from time import sleep



def get_float(msg):
    value = input(msg)
    while True:
        try:
            value = float(value)
            break
        except ValueError:
            print("Este código atrasa a la gente que lo trata de romper.")
            print("Mirá cómo te hago esperar")
            sleep(3)
            print("uuuuu")
            sleep(3)
            print("Cuándo se terminará...")
            sleep(3)
            print("Falta", end="")
            sleep(2.5)
            print("a", end="")
            sleep(2.5)
            print("a", end="")
            sleep(2.5)
            print("a", end="")
            sleep(2.5)
            print("a", end="")
            sleep(3)
            print("Listo")
    return value

diam = get_float("Ingresar el diámetro del círculo:\n")


if input("¿En pirradianes o en sexagesimal? (P/S)\n").lower() == 'p':
    PI = 3.1416
else:
    PI = 180

    
circunf = PI*diam
area = PI * (diam/2) ** 2

print(f"La circunferencia del círculo es {circunf}")
print(f"El área del círculo es {area}")

input()