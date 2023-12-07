"""
Author: Batool Alkaddah 
Time & Date: 9:57 a.m. 2023-12-05
PyCharm
"""
import random

"""
You have a bucket with 3 red balls and 3 green balls.
 Assume that once you draw a ball out of the bucket,
 you don't replace it. What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem.
 Feel free to write a helper function if you wish.
  DO NOT import random, it will be imported for you.
"""
random.seed(2)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    prob = 0

    for i in range(numTrials):
        bucket = [1, 1, 1, 0, 0, 0]
        trail = []
        for n in range(3):
            random_ball = random.choice(bucket)
            trail.append(random_ball)
            bucket.remove(random_ball)

        if sum(trail) == 0 or sum(trail)==3:
            prob +=1


    return prob/numTrials


    # prob = 0
    #
    # for _ in range(numTrials):
    #     bucket = [1, 1, 1, 0, 0, 0]
    #     trail = random.sample(bucket, 3)
    #
    #     if sum(trail) == 0 or sum(trail) == 3:
    #         prob += 1
    #
    # return prob / numTrials

print(noReplacementSimulation(1000))