menu1 = {
    "Hamburguesa": 10.99,
    "Ensalada César": 8.99,
    "Sándwich de Pavo": 7.99,
    "Tarta de Chocolate": 5.99,
    "Pasta Carbonara": 14.75,
    "Pizza de Pepperoni": 13.50,
    "Filete de Ternera": 19.99,
    "Pollo Frito": 10.75,
    "Sopa de Tomate": 6.49,
    "Tacos de Pollo": 8.99,
    "Tarta de Manzana": 6.99
}

menu2 = {
    "Hamburguesa": 10.99,
    "Pizza": 12.99,
    "Pasta Alfredo": 15.99,
    "Ensalada César": 8.99,
    "Sopa de Tomate": 6.99,
    "Filete de Salmón": 18.99,
    "Tacos de Carnitas": 9.99,
    "Pollo a la Parrilla": 13.99,
    "Tacos de Carnitas": 9.99,
    "Sándwich de Pavo": 7.99,
    "Tarta de Chocolate": 5.99
}

for dish in menu2:
    if dish in menu1:
        menu1[dish] += menu2[dish]
    else:
        menu1[dish] = menu2[dish]

print("Menú del día:\n")
for dish in menu1:
    print(dish + ":", menu1[dish])
