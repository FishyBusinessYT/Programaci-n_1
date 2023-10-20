n = 100
m = ["a", "b", "c", "d", "e", "f"]
k = 3

ms = n // len(m)
rem = n % len(m)

begin = m.copy()
end = m[0:rem]

appendix = begin[0:k]


while n:
    end.append(appendix)