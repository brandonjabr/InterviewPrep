# Shuffle a list randomly, in place.
import random
def shuffle(lst):
    for i in range(len(lst)):
        n = random.randint(0,len(lst)-1)
        tmp = lst[n]
        lst[n] = lst[i]
        lst[i] = tmp
    return lst