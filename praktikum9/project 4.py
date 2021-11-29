import random
def shuffleString(x, n):
    list = []
    i = 0
    while i < n:
        pengacakan = ''.join(random.sample(x,len(x)))
        if(pengacakan not in list):
            list += [pengacakan]
            i += 1
    print(list)
shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)
