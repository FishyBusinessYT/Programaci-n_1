notasDiagnóstico = [7, 3, 2, 5, 4, 2, 1]
notasDiagnóstico.sort()
print(f"La nota más baja es {notasDiagnóstico[0]}")
print(f"La nota más alta es {notasDiagnóstico[-1]}")

#Alternativa

notasDiagnóstico = [7, 3, 2, 5, 4, 2, 1]
print(f"La nota más baja es {min(notasDiagnóstico)}")
print(f"La nota más alta es {max(notasDiagnóstico)}")