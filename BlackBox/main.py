import os
from box import Box


def main():
    os.system("cls")

    print("[Black Box]")
    input()

    size = get("Please enter box size:\n", int)
    balls = get("Please enter ball amount:\n", int)

    box = Box(size, balls)
    print(box)


def get(text, itype):
    os.system("cls")
    result = int
    while True:
        try:
            result = itype(input(text))
            break
        except ValueError:
            os.system("cls")
            print("That's not a valid input. Please try again:")
    return result


if __name__ == "__main__":
    main()
