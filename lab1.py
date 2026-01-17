#Alice and Bob have 2𝑛 + 1 coins, each with probability of a head equal to 1/2.
#Bob tosses 𝑛 + 1 coins, while Alice tosses the remaining 𝑛 coins. Assuming
#independent coin tosses, show that the probability that after all the coins have been
#tossed, Bob will have gotten more heads than Alice, is 1/2

## n = 300 number of trials = 1000


from random import random

def bobFlip(p):
    x = random()
    if x < p:
        return 1
    else:
        return 0

def aliceFlip(p):
    y = random()
    if y < p:
        return 1
    else:
        return 0

def main_fair(n, p):
    bobCount = 0
    aliceCount = 0
    bobCoins = n + 1
    aliceCoins = n
    
    while bobCoins > 0:
        bobCount += bobFlip(p)
        bobCoins -= 1
    
    while aliceCoins > 0:
        aliceCount += aliceFlip(p)
        aliceCoins -= 1
    
    return bobCount, aliceCount

n = 300
num_rounds = 1000
p_values = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

print("-" * 26)
print("p     relative frequency")
print("-" * 26)

for p in p_values:
    bobWins = 0
    for _ in range(num_rounds):
        bobCount, aliceCount = main_fair(n, p)
        if bobCount > aliceCount:
            bobWins += 1
    relativeFrequency = bobWins / num_rounds
    print(f"{p:.1f}   {relativeFrequency:.3f}")

## Bob will not have a higher/different probability after flipping weighted coins since both bob and alice get new weighted dice. 
## There is still around a 50% chance that bob gets more heads flipped, because the rate changed equally for both of the subjects. :
