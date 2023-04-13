#Ver si la clave está hasheada o no.
#Eliminar los caracteres numéricos de cada clave.

UsersHashedPass = [
    "$@8A4Jxx",
    "43@@*$",
    "Zjg491AA3",
    "bvALLj49x",
    "zc9j$u$4@3#",
    "svt@$4##",
    "hola",
    "112345543",
    "1234321",
    "9876543210"
]

for index1, password in enumerate(UsersHashedPass):
    for index, char in enumerate(password):
        if index == 0:
            continue
        if char == password[index-1]:
            print(password)
            break
    for char in password:
        if char in "1234567890":
            password = password.replace(char, "")
    UsersHashedPass[index1] = password

print(UsersHashedPass)