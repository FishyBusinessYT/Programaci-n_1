import os
from random import randint as r

directory = os.path.dirname(os.path.realpath(__file__))
file = open(directory + "\\save.txt", "r")
money = int(file.read())
file.close()
file = open(directory + "\\save.txt", "w")

numbers = {
    0: "",
    1: "RED",
    2: "BLACK",
    3: "RED",
    4: "BLACK",
    5: "RED",
    6: "BLACK",
    7: "RED",
    8: "BLACK",
    9: "RED",
    10: "BLACK",
    11: "BLACK",
    12: "RED",
    13: "BLACK",
    14: "RED",
    15: "BLACK",
    16: "RED",
    17: "BLACK",
    18: "RED",
    19: "RED",
    20: "BLACK",
    21: "RED",
    22: "BLACK",
    23: "RED",
    24: "BLACK",
    25: "RED",
    26: "BLACK",
    27: "RED",
    28: "BLACK",
    29: "BLACK",
    30: "RED",
    31: "BLACK",
    32: "RED",
    33: "BLACK",
    34: "RED",
    35: "BLACK",
    36: "RED"
}

while True:
    #Get bet data:
    betMoney = int(input("Enter your bet amount:\n"))
    if betMoney > money:
        print("Not enough money.")
        continue

    money -= betMoney

    bet = input("What will you bet for?\n")
    bet = bet.upper()

    #The original reward is equal to the bet amount entered, multiplied according to the kind of bet entered.
    reward = betMoney

    #Get a random place for the ball to land on.
    ballLand = r(0, 36)

    match bet[0]:
        case "N":
            try:
                if int(bet[1:]) > 36 or int(bet[1:]) < 0:
                    print("Please enter a valid slot.")
            except ValueError:
                print("Please enter a valid slot.") 
            if ballLand == bet[1:]:
                betMoney += reward * 35
        case "C":
            if ballLand % 3 == bet[1:]:
                betMoney += reward * 2
        case "D":
            if ballLand <= 12 and bet[1:] == 1:
                betMoney += reward * 2
            elif ballLand <= 24 and bet[1:] == 2:
                betMoney += reward * 2
            elif ballLand <= 36 and bet[1:] == 3:
                betMoney += reward * 2
        case "B":
            if numbers[ballLand] == "BLACK":
                betMoney += reward
        case "R":
            if numbers[ballLand] == "RED":
                betMoney += reward
        case "E":
            if ballLand % 2 == 0:
                betMoney += reward
        case "O":
            if ballLand % 2 == 1:
                betMoney += reward
        case "L":
            if ballLand <= 18:
                betMoney += reward
        case "H":
            if ballLand > 18:
                betMoney += reward
        case "Q":
            file.write(str(betMoney+money))
            file.close()
            quit()
    money += betMoney
    betMoney = 0
    print(money)
'''
    #This dictionary will contain the bets the user makes.
    bettingData = {
        "numbers": [],
        "column": [],
        "dozen": [],
        "color": None,
        "evnodd": None,
        "hilo": None
    }

    for bet in bets:
        if bet.isdigit():
            bettingData["numbers"].append(int(bet))
            continue

        match bet:
            case "C1" | "C2" | "C3":
                bettingData["column"].append(bet)
            case "D1" | "D2" | "D3":
                bettingData["dozen"].append(bet)
            case "BLACK" | "RED":
                if not bettingData["color"]:
                    bettingData["color"] = bet
                else:
                    print(f'Detected two opposing bets. Keeping first bet: {bettingData["color"]}')
            case "EVEN" | "ODD":
                if not bettingData["evnodd"]:
                    bettingData["evnodd"] = bet
                else:
                    print(f'Detected two opposing bets. Keeping first bet: {bettingData["evnodd"]}')
            case "HIGH" | "LOW":
                if not bettingData["hilo"]:
                    bettingData["hilo"] = bet
                else:
                    print(f'Detected two opposing bets. Keeping first bet: {bettingData["hilo"]}')
            case _:
                print(f"Invalid bet value {bet} will be ignored.")

        bettingData["numbers"].sort()

        if not ballLand in bettingData["numbers"]:
            betMoney = 0
        
        if bettingData["numbers"].length == 5:
            print("You cannot bet on 5 numbers.")
        
        elif bettingData["numbers"].length > 6:
            print("You cannot bet on that many numbers.")

        elif list(range(bettingData["numbers"][-1]+1)) == bettingData["numbers"]:
            if bettingData["numbers"].length == 6:
                if ballLand in bettingData["numbers"]:
                    betMoney += reward * 5
                else:
                    betMoney = 0
            elif bettingData["numbers"].length == 3:
                if ballLand in bettingData["numbers"]:
                    betMoney += reward * 11
                else:
                    betMoney = 0

        elif list(range(bettingData["numbers"][-1]+1)).pop(2) == bettingData["numbers"] and bettingData["numbers"].length == 4:
            if ballLand in bettingData["numbers"]:
                betMoney += reward * 8
            else:
                betMoney = 0

        el
'''