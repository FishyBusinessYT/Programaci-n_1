# Un planeta habitable debe:
# 1- Estar a menos de 100 años luz.
# 2- Tener una temperatura entre -20 y 50 grados Celsius
# 3- Tener una gravedad entre 5 y 10 m/s^2


planetas = {
    "tierra": {
        "distancia": 0.0,
        "temperatura": 15.0,
        "gravedad": 9.8
    },
    "marte": {
        "distancia": 0.5,
        "temperatura": -65.0,
        "gravedad": 3.7
    },
    "proxima centauri b": {
        "distancia": 4.2,
        "temperatura": -40.0,
        "gravedad": 7.0
    }
}
viable = lambda d, t, g: d <= 100 and t >= -20 and t <= 50 and g <= 10 and g >=5 
for planeta in planetas:
    if viable(planetas[planeta]["distancia"], planetas[planeta]["temperatura"], planetas[planeta]["gravedad"]):
        print(planeta)