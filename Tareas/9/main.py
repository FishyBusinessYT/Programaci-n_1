def get(text):
    result = float
    while True:
        try:
            result = float(input(text))
            break
        except ValueError:
            print("Ese no es un valor válido.")
    return result

print("//SET 1")
set1 = {*[]}
for i in range(5):
    set1.add(get(f"Ingrese un número ({i+1}): "))

print("//SET 2")
set2 = {*[]}
for i in range(5):
    set2.add(get(f"Ingrese un número ({i+1}): "))

overlapSet = set1.intersection(set2)
print(overlapSet)