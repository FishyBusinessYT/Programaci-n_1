from time import sleep
from Funcs import Hexagono, Circulo, Pentagono, Rombo, Trapecio

# 6 archivos
# 1 función, 1 figura cada uno.

# Deben retornar perímetro y área de las siguientes figuras:

# Hexágono
# Pentágono
# Rombo
# Trapecio
# Círculo

# El hexa-rombi-trappenta-triángulo.
# Que reciba 2 parámetros y calcule el área total.

# Para el caso del círculo, hay que hacer una transformación de pirradianes a sexagesimal.

# Cada una debe pedir sus datos. ESE PEDIDO DE DATOS DEBE SER A TRAVÉS DE UNA FUNCIÓN


def Triangulo_calc(b):
    h = (b**2 - (b / 2) ** 2) ** (1 / 2)
    p = b * 3
    a = h * b / 2
    return h, p, a


def get_float(msg):
    while True:
        value = input(msg)
        try:
            value = float(value)
            break
        except ValueError:
            print("Este código atrasa a la gente que lo trata de romper.")
            print("Mirá cómo te hago esperar.")
            sleep(3)
            print("uuuuu")
            sleep(3)
            print("Cuándo se terminará...")
            sleep(3)
            print("Faltaaaaaaaaaaaaa")
            sleep(3)
            print("aaaaaaaaaaaaaaaaa")
            sleep(3)
            print("aaaaaaaaaaaaaaaaa")
            sleep(3)
            print("aaaaaaaaaaaaaaaaa")
            sleep(3)
            print("aaaaaaaaaaaaaaaaa")
            sleep(10)
            print("Listo")
            sleep(1)
    return value


def printsleep(phrases):
    for phrase in phrases:
        print(phrase)
        sleep(0.1)


def main():
    texto = [
        "¡Bienvenido a la experiencia/calculadora del hexa-rombi-trappenta-triángulo!",
        "Como todos sabemos, un hexa-rombi-trappenta-triángulo es una figura muy simple.",
        "Sin embargo, algunos pueden tener dificultades entendiendo como funciona el hexa-rombi-trappenta-triángulo.\n",
        "Vamos a empezar con un par de propiedades que tiene el hexa-rombi-trappenta-triángulo:\n",
        "1: Todos los lados del hexa-rombi-trappenta-triángulo son iguales, a excepción de la base de su parte trapecial.",
        "2: Todas las apotemas y alturas del hexa-rombi-trappenta-triángulo son iguales.\n",
        "Con eso dicho, vamos a ver al hexa-rombi-trappenta-triángulo por partes:\n",
        '"Triángulo", que viene de triángulo (duh). Es la parte triangular del hexa-rombi-trappenta-triángulo y define un montón de cosas más adelante.',
        "Para calcular este pedazo de hexa-rombi-trappenta-triángulo, necesitamos su altura, nada más:\n",
    ]
    printsleep(texto)

    lados = get_float(
        "Ingresar la longitud de los lados del hexa-rombi-trappenta-triángulo: "
    )
    alturas, peri_tri, area_tri = Triangulo_calc(lados)
    peri_hex, area_hex = Hexagono.calc(lados, alturas)
    peri_rmb, area_rmb = Rombo.calc(lados, alturas)
    peri_trp, area_trp, base_trp = Trapecio.calc(lados, alturas)
    peri_pen, area_pen = Pentagono.calc(lados, alturas)

    texto = [
        "\n¡Bien! Apuesto a que no probaste mil veces a ver si podías darle cosas que no eran números a la experiencia/calculadora del hexa-rombi-trappenta-triángulo, como un ser normal!\n",
        f"El perímetro de la parte triangular del hexa-rombi-trappenta-triángulo es {peri_tri}",
        f"El área de la parte triangular del hexa-rombi-trappenta-triángulo es {area_tri}",
        f"La altura de la parte triangular del hexa-rombi-trappenta-triángulo es {alturas}\n",

        'La siguiente parte es "Hexa", que viene de hexágono. Es la parte con forma de hexágono del hexa-rombi-trappenta-triángulo.',
        f"El perímetro de la parte Hexagonal del hexa-rombi-trappenta-triángulo es {peri_hex}",
        f"El área de la parte hexagonal del hexa-rombi-trappenta-triángulo es {area_hex}\n",

        'La siguiente parte es "Rombi", que viene de rombo. Es la parte con forma de rombo del hexa-rombi-trappenta-triángulo.',
        f"El perímetro de la parte rombal del hexa-rombi-trappenta-triángulo es {peri_rmb}",
        f"El área de la parte rombal del hexa-rombi-trappenta-triángulo es {area_rmb}\n",

        'La siguiente parte es "Trap", que viene de trapecio. Es la parte con forma de trapecio del hexa-rombi-trappenta-triángulo.',
        f"El perímetro de la parte trapecial del hexa-rombi-trappenta-triángulo es {peri_trp}",
        f"El área de la parte trapecial del hexa-rombi-trappenta-triángulo es {area_trp}",
        f"La base mayor de la parte trapecial del hexa-rombi-trappenta-triángulo es {base_trp}\n",

        'La siguiente parte es "Penta", que viene de pentágono. Es la parte con forma de pentágono del hexa-rombi-trappenta-triángulo.',
        f"El perímetro de la parte pentagonal del hexa-rombi-trappenta-triángulo es {peri_pen}",
        f"El área de la parte pentagonal del hexa-rombi-trappenta-triángulo es {area_pen}\n",
    ]
    printsleep(texto)


if __name__ == "__main__":
    main()

input()