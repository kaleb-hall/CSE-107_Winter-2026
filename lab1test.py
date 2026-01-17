#Alice and Bob have 2𝑛 + 1 coins, each with probability of a head equal to 1/2.
#Bob tosses 𝑛 + 1 coins, while Alice tosses the remaining 𝑛 coins. Assuming
#independent coin tosses, show that the probability that after all the coins have been
#tossed, Bob will have gotten more heads than Alice, is 1/2

## n = 300 number of trials = 1000


## relative Frequency = when did bob get more heads than alice / 1000
from random import random

def bobFlip():
    x = random()
    if x >= .5:
        return 1
    else:
        return 0

def aliceFlip():
    y = random()
    if y >= .5:
        return 1
    else:
        return 0 

def main_fair(n):
    bobCount = 0
    aliceCount = 0
    bobCoins = n + 1
    aliceCoins = n
    
    while bobCoins > 0:
        bobCount += bobFlip()
        bobCoins -= 1
    
    while aliceCoins > 0:
        aliceCount += aliceFlip()
        aliceCoins -= 1
    
    return bobCount, aliceCount

n = 300
num_rounds = 1000
bobWins = 0

for _ in range(num_rounds):
    bobCount, aliceCount = main_fair(n)
    if bobCount > aliceCount:
        bobWins += 1


relativeFrequencyFair = bobWins / 1000
print(f"relative frequency of bob's wins with a fair coin is: {relativeFrequencyFair:.3f}")




