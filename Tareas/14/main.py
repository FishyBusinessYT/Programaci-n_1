dictionary = {
    "c": 1,
    "n": 2,
    "u": 3,
    "s": 4,
    "a": 5,
    "o": 6,
    "q": 7,
    "i": 8,
    "t": 9,
    "r": 10,
    "e": 11    
}

vocals = ""
vocalvalues = ""
consonants = ""
consonantvalues = ""
primes = ""
primevalues = []


for l in dictionary:
    isprim = True
    i = dictionary[l]
    if i != 1:
        for p in primevalues:
            if i%p == 0:
                isprim = False
                break
        if isprim:
            primevalues.append(i)
            primes += l

    if l in "aeiou":
        vocals += l
        vocalvalues += str(dictionary[l])
    else:
        consonants += l
        consonantvalues += str(dictionary[l])


dictionary[primes] = int(str(primevalues).replace(", ", "")[1:-1])
dictionary[vocals] = int(vocalvalues)
dictionary[consonants] = int(consonantvalues)


frontiers = "cnusaoqitre"
frontiervalues = ""

hexagons = list(frontiers)

upperLimit = len(hexagons)//2 - 1

hexagons.pop(-1)
hexagons.pop(upperLimit+1)
hexagons.pop(upperLimit)
hexagons.pop(0)
print(hexagons)