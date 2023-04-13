from mazo import Mazo

mazo = Mazo()

scoreboard = {
    "Us": 0,
    "Them": 0
}

print(mazo.deal())

# while scoreboard["Us"] < 30 and scoreboard["Them"] < 30:
#     pass