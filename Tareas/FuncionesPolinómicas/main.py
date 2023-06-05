from random import randint as r
from math import sqrt

class Funcion():
    def __init__(self, a, b, c) -> None:
        a = a if a != 0 else 1
        self.datos = {
            "a": a,
            "b": b,
            "c": c,
            "h_vertice": 0,
            "k_vertice": 0,
            "raiz_1": 0,
            "raiz_2": 0,
            "disc": 0,
            "tipo_raices": "",
            "orient_parab": ""
        }

        self.expressions = {
            "polinomica": "",
            "canonica": "",
            "factorizada": ""
        }
    
        self.datos["disc"] = (b ** 2) - (4 * a * c)
        self.datos["h_vertice"] = -b/(2*a)
        self.datos["k_vertice"] = a*self.datos["h_vertice"]**2 + b*self.datos["h_vertice"] + c
        self.datos["orient_parab"] = "arriba" if a < 0 else "abajo"
        self.expressions["polinomica"] = f"{a}x^2 + {b}x + {c}"
        self.expressions["canonica"] = f"{a}(x-{self.datos['h_vertice']})^2 + {self.datos['k_vertice']}"


        if self.datos["disc"] >= 0:
            self.datos["tipo_raices"] = "diferentes"
            if not self.datos["disc"]:
                self.datos["tipo_raices"] = "iguales"
            
            self.datos["raiz_1"] = min(self.raices())
            self.datos["raiz_2"] = max(self.raices())

            self.expressions["factorizada"] = f"{a}(x - {self.datos['raiz_1']}) * (x - {self.datos['raiz_2']})"

        else:
            self.datos["tipo_raices"] = "complejas conjugadas"

        for key in self.datos:
            try:
                self.datos[key] = round(self.datos[key], 2)
            except:
                pass

    def raices(self) -> list:
        return [ 
            (-self.datos["b"] + sqrt(self.datos["disc"])) / (2 * self.datos["a"]),
            (-self.datos["b"] - sqrt(self.datos["disc"])) / (2 * self.datos["a"])
            ] 
    def obtener_problema(self):
        problema = "Obtener {} de esta función {}:\n{}"
        dato = [elem for elem in self.datos][r(0, 9)]
        tipo = [elem for elem in self.expressions][r(0, 2)]
        formula = self.expressions[tipo]

        return problema, dato, tipo, formula

fuasdasd = Funcion(r(-10, 10), r(-10, 10), r(-10, 10))

#problema = fuasdasd.obtener_problema()
#print(problema[0].format(problema[1], problema[2], problema[3]))
#a = 0
#while a != str(fuasdasd.datos[problema[1]]):
#    a = input()
#    print(fuasdasd.datos[problema[1]] if a == "listo" else "", end="")

fuasdasd = Funcion(r(-10, 10), r(-10, 10), r(-10, 10))

problema = fuasdasd.obtener_problema()
print(problema[0].format(problema[1], problema[2], problema[3]))
a = 0

while a != str(fuasdasd.datos["disc"]):
    a = input()
    print(fuasdasd.datos[problema[1]] if a == "listo" else "", end="")