result = 0
for i in range(1000):
    result += i if 0 in [i%3, i%5] else 0
print(result)