from random import randint
def get(text):
    result = int
    while True:
        try:
            result = input(text)
            if not result:
                break
            result = int(result)
            break
        except ValueError:
            print("Ese no es un número válido.")
    return result

set2 = {*[]}
while len(set2) < 10:
    set2.add(randint(1, 10000))

set1 = {*[]}
num = get("Ingresar un número: ")
while num:
    set1.add(num)
    num = get("Ingresar un número: ")
set1.pop()
set1.pop()

print(set1.union(set2))