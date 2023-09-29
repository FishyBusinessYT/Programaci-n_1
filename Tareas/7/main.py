import turtle as tt

def main():
    wn = tt.Screen()
    wn.setup(1000, 1000)
    wn.setworldcoordinates(0, 1000, 1000, 0)
    turt = tt.Turtle()
    turt.penup()

    info = [
        [-1, -1, -1],
        [-1, -1, -1]
    ]

    print("Cuadrado 1 (trasero):")
    info[0] = [get("Insertar coordenada de origen x: "), get("Insertar coordenada de origen y: "), get("Ingresar tamaño del cuadrado: ")]
    print("Cuadrado 2 (frontal):")
    info[1] = [get("Insertar coordenada de origen x: "), get("Insertar coordenada de origen y: "), get("Ingresar tamaño del cuadrado: ")]

    turt.goto(info[0][0], info[0][1])
    turt.color("black")
    turt.begin_fill()
    for i in range(4):
        turt.forward(info[0][2])
        turt.left(90)
    turt.end_fill()
    turt.goto(info[1][0], info[1][1])
    turt.color("gray")
    turt.begin_fill()
    for i in range(4):
        turt.forward(info[1][2])
        turt.left(90)
    turt.end_fill()
    
    tt.done()
    


def get(text):
    result = int
    while True:
        try:
            result = int(input(text))
            if result < 0:
                raise ValueError 
            break
        except ValueError:
            print("Ese no es un número válido.")
    return result

if __name__ == "__main__":
    main()