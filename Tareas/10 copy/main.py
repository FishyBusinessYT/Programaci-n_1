from random import randint as r

team = [
 ("Debra Capini","Arquero",59,"Portugal"),
 ("Pablo Gonzalez","Delantero",90,"Argentina"),
 ("Hin guin","Aguatero",73,"China"),
 ("Sena Aronson","Delantero",11,"Irlanda"),
 ("Laney Rembrandt","Defensor",10,"Alemania"),
 ("Fernande Gallelli","Mediocampista",62,"España"),
 ("Amery Darey","Arquero",27,"Inglaterra"),
 ("Facundo Aguinaga","Arquero",15,"Argentina"),
 ("Augusto Pulgar","Arquero",69,"Chile"),
 ("Britte Brocks","Defensor",92,"EEUU"),
 ("Rob Issard","Arquero",59,"Canada"),
 ("Susanne Manifould","Delantero",39,"Suecia"),
 ("Elvis Rodriguez","Delantero",80,"Colombia"),
 ("Roman Riquelme","Aguatero",43,"Argentina"),
 ("Genghis Khan","Delantero",861,"Mongolia"),
 ("Baxy Pex","Arquero",37,"Rumania"),
 ("Harriet Elsworth","Delantero",78,"Escocia"),
 ("Robert Downey Jr","Arquero",10,"Paraguay"),
 ("Tomas Maure","Mediocampista",15,"Argentina"),
 ("Tandie Stuttard","Arquero",8,"Filipinas"),
 ("Aldous Menier","Arquero",90,"China"),
 ("Chrysler Skiplorne","Delantero",30,"Inglaterra"),
 ("Salomu Emtiti","Delantero",25,"Nigeria"),
 ("Rudolph Stollberg","Defensor",18,"Inglaterra"),
 ("Marsh Marsh","Arquero",19,"Egipto")
] 
suspended = {"Britte Brocks", "Hin guin", "Tandie Stuttard", "Tomas Maure"}
injured = {*[]}
aguateros = []
countries = {*[]}
tooOld = {*[]}
repeatedCountries = {*[]}
while len(injured) < 6:
    injured.add(team.pop(r(0, len(team)-1)))

for p in team:
    if p[1] == "Aguatero":
        aguateros.append(p)
        
    if p[3] in countries:
        repeatedCountries.add(p[3])
        countries.remove(p[3])
    elif not(p[3] in repeatedCountries):        
        countries.add(p[3])

    if p[0] in suspended:
        team.remove(p)  
    elif p[2] >= 25:
        tooOld.add(p)
        team.remove(p)

team.append(("La Gabi", "Arquero", 23, "Argentina"))

print("Jugadores lesionados: \n", injured)
print("Aguateros: \n", aguateros)
print("Jugadores habilitados para jugar: \n", team)
print("Nacionalidades únicas: \n", countries)


for p in aguateros:
    if len(p[0]) > 10:
        print("Hay un nombre largo entre los aguateros")
        break
for p in team:
    if len(p[0]) > 10:
        print("Hay un nombre largo entre los jugadores")
        break
for p in injured:
    if len(p[0]) > 10:
        print("Hay un nombre largo entre los lesionados")
        break
for p in tooOld:
    if len(p[0]) > 10:
        print("Hay un nombre largo entre los viejos")
        break
