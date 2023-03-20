pointer = 0
memory = {}
loopData = []

lens = 0

file = open("bf.bf")

file = list("".join(char for char in file.read() if char in ".,[]<>+-?*"))

def findBracket():
    lensclone = lens
    openbrackets = 1
    while openbrackets != 0:
        lensclone += 1
        if file[lensclone] == "[":
            openbrackets += 1
        elif file[lensclone] == "]":
            openbrackets -= 1
    return lensclone

while lens < len(file):
    if pointer < 0:
        exit(f"You can't go further back, {lens}")
    if pointer not in memory:
        memory[pointer] = 0
    if memory[pointer] < 0:
        memory[pointer] = 256 + memory[pointer]
    elif memory[pointer] > 255:
        memory[pointer] = memory[pointer] - 256
    match file[lens]:
        case "+":
            memory[pointer] += 1
        case "-":
            memory[pointer] -= 1
        case ">":
            pointer += 1
        case "<":
            pointer -= 1
        case ",":
            inp = input()
            memory[pointer] = 0 if inp == "" else ord(inp[0])
        case ".":
            print(chr(memory[pointer]), end="")
        case "[":
            if memory[pointer]:
                loopData.append([lens, findBracket()])
                lens += 1
                continue
            lens = findBracket()
        case "]":
            if memory[pointer] == 0:
                loopData.pop()
            else:
                lens = loopData[-1][0]
        case "?":
            print(f"Pointer: {pointer}\nMemory: {memory}\nLens: {lens}\nLoop data: {loopData}", sep="\n")
        case "*":
            print(f"I'm fine until {lens}!", sep="\n")

    lens += 1