file = open("bf.bf")
file = list("".join(char for char in file.read() if char in ".,[]<>+-?*"))
print(len(file))