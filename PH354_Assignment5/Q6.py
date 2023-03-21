# Exercise 6: Importance sampling formula

# ANSWERS
# We got __ which is close to 0.84

# Importing useful modules
import random
from math import sqrt, exp

# Defining constants
N = int(1e6)
a = 0
b = 1
w_int = 2


# Defining the integrand
def f(x):
    return x**(-1/2) / (exp(x) + 1)


# Defining the weighting function
def w(x):
    return x**(-1/2)


# Defining f(x)/ w(x)
def g(x):
    return 1 / (exp(x) + 1)


# Define a function that carries out importance sampling
def importance_sampling(g, w_int, N):
    sum = 0
    sq_sum = 0
    prefac = w_int / N
    for i in range(N):
        y = random.uniform(0, 1)
        x = y**2
        sum += g(x)
        sq_sum += g(x)**2
    g2w = sq_sum / N
    gw2 = (sum / N)**2
    varwg = (g2w - gw2)
    error = sqrt(varwg / N) * w_int
    return prefac * sum, error


ISInt, ISError = importance_sampling(g, w_int, N)
print("Value of the integral: ", ISInt)
print("Error estimate: ", ISError)
