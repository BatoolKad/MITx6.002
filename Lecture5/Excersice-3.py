"""
Author: Batool Alkaddah 
Time & Date: 2:36 p.m. 2023-11-18
PyCharm
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 14

def stochasticNumber():
        '''
        Stochastically generates and returns a uniformly distributed even number between 9 and 21
        Note!! When you are using:
        random.randrange(
        start: The start of the range (inclusive)
        stop: The end of the range (exclusive)
        step: The step value (default is 1)
        )!
        '''
        x_random = random.randrange(10,22,2)
        return x_random

print(stochasticNumber())
print(stochasticNumber())
