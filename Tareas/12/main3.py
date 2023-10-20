ingredients = {"harina": 0, "azúcar": 0, "leche": 0, "manteca": 0, "huevos": 0, "polvo": 0, "sal": 0, "arándanos": 0, "vainilla": 0}

instructions = "Precalentar el horno a 200°C y colocar capacillos de papel en un molde para muffins. En un tazón grande, mezclar la harina, el azúcar, el polvo de hornear y la sal. En otro tazón, batir los huevos y luego agregar la leche, la manteca derretida y el extracto de vainilla. Mezclar bien. Verter la mezcla líquida en el tazón con los ingredientes secos. Revolver con suavidad hasta que estén bien mezclados. No batas en exceso, solo lo suficiente para que los ingredientes estén incorporados. Colocar suavemente los arándanos en la mezcla. Si estás utilizando arándanos congelados, es importante no descongelarlos antes de usarlos. Llenar cada capacillo de papel hasta aproximadamente 2/3 de su capacidad. Hornear en el horno precalentado durante aproximadamente 20-25 minutos, o hasta que los muffins estén dorados en la parte superior y un palillo o cuchillo insertado en el centro salga limpio. Retirar los muffins del horno y dejarlos enfriar en el molde durante unos minutos antes de transferirlos a una rejilla para que se enfríen por completo. ".replace(",", "").split()

print(instructions)

for word in instructions:
    if word in ingredients:
        ingredients[word] += 1

while True:
    iput = input("Insertar consulta:\n")
    while iput not in ingredients:
        print("Ese ingrediente no es parte de la receta")
        iput = input("Insertar consulta:\n")
    print("Ese ingrediente se menciona " + str(ingredients[iput]) + " veces")
    if input("Enter para hacer otra consulta: "):
        break