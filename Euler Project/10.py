num = 2000000
primes = [True for i in range(num+1)]
p = 2
result = 2
while p*p <= num:
    if primes[p]:
        for i in range(p*p, num+1, p):
            primes[i] = False
    p += 1
for p in range(3, num+1, 2):
    if primes[p]:
        result += p
print(result)