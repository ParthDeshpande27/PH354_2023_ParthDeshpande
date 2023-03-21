# Exercise 5: Volume of a hypersphere

# ANSWERS
# With 1e7 points, I got 2.5634 while with 1e6 points I got 2.5211.
# (From wikipedia, the answer is ~2.550).

# Importing useful modules
import random

# Defining constants
N = int(1e6)    # Number of points to use in the Monte Carlo integration
R = 1           # Radius of the sphere
D = 10          # Dimension of the sphere


# Defining the function that checks if the generated point is inside the sphere
def is_in_sphere(x, R):
    return sum([x_i**2 for x_i in x]) <= R**2


# Defining the function that does Monte Carlo integration
def MCV(R, D, N):
    Cube_volume = (2*R)**D
    count = 0
    for i in range(N):
        x = [random.uniform(-R, R) for j in range(D)]
        if is_in_sphere(x, R):
            count += 1
    return Cube_volume * count / N


print("Volume of a 10D unit sphere: ", MCV(R, D, N))
