def ispalin(n):
    rev = 0
    num = n
    while num%10 != num:
        rev += num % 10
        rev *= 10
        num -= num%10
        num /= 10
    rev += num
    return rev == n

largest = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        if ispalin(a*b) and largest < a*b:
            largest = a*b
print(largest)
