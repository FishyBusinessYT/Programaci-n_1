nums = []
i = 0
while i < 3:
    try:
        num = int(input("Ingresar un número: "))
        nums.append(num)
        i += 1
    except ValueError:
        print("Eso no es un número.")
        continue

r = 0
for num in nums:
    print(num)
    r += num

print(f"La suma de esos números es {r}")
