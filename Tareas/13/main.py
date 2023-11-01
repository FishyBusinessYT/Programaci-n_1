from team import team
def truncadora(start, stop, data):
    length = len(data)
    start = start-1 % length
    stop -= (start // length) * length
    trunclist = [] 
    for i in range(-1 * (-stop // length)): trunclist.extend(data)
    return trunclist[start:stop]
print(truncadora(1, 6, team))