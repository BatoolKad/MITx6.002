"""
Author: Batool Alkaddah 
Time & Date: 3:12 p.m. 2023-11-18
PyCharm
"""
"""
If you set the seed to a specific value,
you will get the same sequence of random 
numbers every time you run your program. 
"""
import random

# Setting the seed to 42
random.seed(2)

# Now, if you generate random numbers, they will be the same every time
print(random.random())
print(random.randint(1, 10))