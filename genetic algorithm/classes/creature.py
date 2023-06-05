from random import randint as r

class Creature():
    def __init__(self) -> None:
        self.positon = [r(1, 99), r(1, 99)]
    def frame(self) -> None:
        