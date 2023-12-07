"""
Author: Batool Alkaddah 
Time & Date: 2:23 p.m. 2023-11-18
PyCharm
"""
import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    Random Documentation:
     - random.randrange(start, stop[, step]): Return a randomly selected element from range(start, stop, step).

    '''
    return random.randrange(0,99,2)

    # while True:
    #     if x%2==0:
    #         return x
    #     else:
    #         x = random.randint(1, 100)


print(genEven())