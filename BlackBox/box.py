from random import randint as r


class Box:
    def __init__(self, s, b) -> None:

        if b > s*s:
            b = s
        
        self.matrix = [[" " for _ in range(s)] for _ in range(s)]
        self.lasers = "" #[[" " for _ in range(s)] for _ in range(4)]
        self.balls = b
        self.scale = s


        while b > 0:
            rw, cl = r(0, s - 1), r(0, s - 1)
            if self[rw][cl] == "●":
                continue
            self[rw][cl] = "●"
            b -= 1
        
        print(self)
        self.calculate()

    def __call__(self, pos) -> str:
        return self.matrix[pos[0]][pos[1]]

    def __getitem__(self, index) -> list:
        return self.matrix[index]

    def __str__(self) -> str:
        string = ""
        for row in self.matrix:
            for cell in row:
                string += "[" + str(cell) + "]"
            string += "\n"
        return string

    def calculate(self):
        laser = V(-1, 0, [1, 0])
        print(laser.check)



class V:
    def __init__(self, x:int, y:int, fwd:list) -> None:
        self.pos = [x, y]
        self.fwd = fwd

    @property
    def check(self):
        _ = [self.fwd[0] + self.nflip(self.fwd)[0], self.fwd[1] + self.nflip(self.fwd)[1]]
        return [
            self + self.fwd,
            self + [1, 1],
            self + _
        ]

    def flip(self, l):
        return [l[1], l[0]]
    
    def nflip(self, l):
        return [-l[1], -l[0]]
    
    def __add__(self, other):
        result = [self[0] + other[0], self[1] + other[1]]
        return result
    
    def __getitem__(self, index):
        return self.pos[index]

a = Box(5, 30)