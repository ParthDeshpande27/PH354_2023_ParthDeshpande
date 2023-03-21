# Exercise 1: Rolling dice

# Importing useful modules
import random

# Part A

# Generating two random numbers between 1 and 6
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

# Printing the results
print("Dice 1: {}".format(dice_1))
print("Dice 2: {}".format(dice_2))

# Part B

# Initializing the count of 'bingo's (double sixes) to 0
bingo_count = 0
N = int(1e6)

# Rolling two dice N times
for i in range(N):
    # Generating two random numbers between 1 and 6
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    # Checking if both dice are sixes
    if dice_1 == 6 and dice_2 == 6:
        # Incrementing the bingo count if they are
        bingo_count += 1

bingo_fraction = bingo_count / N
print("Fraction of incidence of bingo! (Two sixes): {}".format(bingo_fraction))
print("Percentage deviation from expectation: {:.6f}".format(3600*(bingo_fraction - 1/36)))
