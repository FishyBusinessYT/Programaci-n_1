from random import shuffle as shuffle

cards = [
    "1_Espada",
    "1_Basto",
    "7_Espada",
    "7_Oro",
    "3_Espada",
    "3_Basto",
    "3_Oro",
    "3_Copa",
    "2_Espada",
    "2_Basto",
    "2_Oro",
    "2_Copa",
    "1_Oro",
    "1_Copa",
    "12_Espada",
    "12_Basto",
    "12_Oro",
    "12_Copa",
    "11_Espada",
    "11_Basto",
    "11_Oro",
    "11_Copa",
    "10_Espada",
    "10_Basto",
    "10_Oro",
    "10_Copa",
    "7_Basto",
    "7_Copa",
    "6_Espada",
    "6_Basto",
    "6_Oro",
    "6_Copa",
    "5_Espada",
    "5_Basto",
    "5_Oro",
    "5_Copa",
    "4_Espada",
    "4_Basto",
    "4_Oro",
    "4_Copa"
    ]
shuffleCards = cards.copy()

def deal() -> list:
    shuffle(shuffleCards)
    cards = [shuffleCards.pop() for _ in range(3)]
    return cards
def reset() -> None:
    return cards.copy()

dealtHand = deal()
dealtHand2 = deal()
shuffleCards = reset()

print(dealtHand)
print(dealtHand2)
print(shuffleCards == cards)

result = []
for card in cards:
    if card in dealtHand:
        result.append(card)

for card in cards:
    if card in dealtHand2:
        result.append(card)

print(result)