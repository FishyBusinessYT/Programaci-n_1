from mazo import Mazo

mazo = Mazo()

dealtHand = mazo.deal()
result = []
for card in mazo.cards:
    if card in dealtHand:
        result.append(card)

print(result)