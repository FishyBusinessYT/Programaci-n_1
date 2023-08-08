from random import randint as rint
import os

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
frase = "MECOMOLOSMOCOS"
coords = [[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[3, 7],[4, 7],[5, 7],[5, 6],[5, 5],[5, 4],[5, 3],[5, 2]]


def main():
    grid = [[{"revealed": False, "char": abc[rint(0, 31)]} for c in range(14)] for r in range(6)]

    for i, pos in enumerate(coords):
        grid[pos[0]][pos[1]]["char"] = frase[i]

    while True:
        update(grid)
        cell = input().upper()
        row = abc.index(cell[0])
        cell = abc.index(cell[1])
        try:
            for pos in get_neighbors(row, cell):
                grid[pos[0]][pos[1]]["revealed"] = True
        except IndexError:
            print("Esa coordenada no existe. Ten en mente que el formato es [FILA][COLUMNA]")
            input("Enter para continuar: ")


def get_neighbors(row, cell):
    returnValue = []

    row = 1 if row == 0 else 4 if row == 5 else row
    cell = 1 if cell == 0 else 12 if cell == 13 else cell

    for r in range(-1, 2):
        for c in range(-1, 2):
            returnValue.append([row+r, cell+c])

    return returnValue




def update(grid):
    os.system("cls")

    print("[ ]", end=" ")
    for i in range(14):
        print(" " + abc[i], end=" ")
    print()

    r = 0
    for row in grid:
        print(" " + abc[r] + " ", end=" ")
        r += 1
        for cell in row:
            if cell["revealed"]:
                print("[" + cell["char"] + "]", end="")
                continue
            print("[.]", end="")
        print()

if __name__ == "__main__":
    main()

