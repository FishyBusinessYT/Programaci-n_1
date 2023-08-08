from a import firstFunc
from b import secondFunc
for i in range(51):
    print(
        f'''
        Value: {i}
        First: {firstFunc(i)}
        Second: {secondFunc(i)}
        '''
    )