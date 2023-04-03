# Filtrar los setups que tengan menos de 24gb de RAM

# Multiplicar el precio de cada setup por 5, sumar el 10% en el total, y a eso restarle el 20%.

# Agregar en todos los setups, excepto aquel con procesador Ryzen, un stock de 10 unidades. 

# Encontrar la posición en la lista de aquel setup cuyo valor sea superior a 2k.

# Encontrar la posición en la lista de aquel setup cuyo valor sea inferior a 1.2k.

setups = [
    {
    "CPU": "Ryzen 5600",
    "RAM": "Fury 32GB",
    "Price": 1999
    },
    {
    "CPU": "Intel i7 11700k",
    "RAM": "HyperX 16GB",
    "Price": 1699
    },
    {
    "CPU": "Intel i5 10200",
    "RAM": "Fury 86GB",
    "Price": 1199
    }
]

total = 0
for setup in setups:
    total += setup["Price"]
total += total/10
total -= total/5
print("El precio revuelto es", total)

for setup in setups:
    if "Ryzen" in setup["CPU"]:
        setup["Stock"] = 10
        print(f"El setup #{setups.index(setup)} tiene {setup['Stock']} unidades en stock.")
    
    if setup["Price"] > 2000:
        print(f"El setup #{setups.index(setup)} vale más de 2000.")

    if setup["Price"] < 1200:
        print(f"El setup #{setups.index(setup)} vale menos de 1200.")
        
    setup_ram = int("".join(char for char in setup["RAM"] if char in "1234567890"))
    if setup_ram >= 24:
        print(f"El setup #{setups.index(setup)} tiene más de 24GB de RAM.")
