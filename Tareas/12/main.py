menu = {
    "Hamburguesa": 10.99,
    "Pizza": 12.99,
    "Pasta Alfredo": 15.99,
    "Ensalada César": 8.99,
    "Sopa de Tomate": 6.99,
    "Filete de Salmón": 18.99,
    "Pollo a la Parrilla": 13.99,
    "Tacos de Carnitas": 9.99,
    "Sándwich de Pavo": 7.99,
    "Tarta de Chocolate": 5.99
}
price = 0

print("Menú del día:\n")
for dish in menu:
    print(dish)

while True:
    iput = input("¿Qué plato desea?\n")
    while iput not in menu:
        print("Ese plato no se encuentra en nuestro menú.")
        iput = input("¿Qué plato desea?\n")
    price += menu[iput]
    if input("Enter para agregar otro plato: "):
        break
    

print("El precio a pagar es de $" + str(price))