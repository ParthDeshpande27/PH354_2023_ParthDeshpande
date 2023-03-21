# Exercise 4: Integral using Monte Carlo method

# ANSWERS
# We indeed find the mean value method error to be somewhat smaller (0.0053 compared to 0.0089)
# compared to Monte Carlo integration.

# Importing useful modules
import random
from math import sin, sqrt

# Defining constants
N = 10000   # Number of points to use in the Monte Carlo integration
a = 0       # Lower bound of integration
b = 2       # Upper bound of integration
c = 1       # Upper bound of the rectangle that contains the region of integration

# Part A


# Defining the function that does Monte Carlo integration
def MCI(f, a, b, c, N):
    Area = c * (b - a)
    count = 0
    for idx in range(N):
        x = random.uniform(a, b)
        y = random.uniform(0, c)
        if y <= f(x):
            count += 1
    Integral = count * Area / N
    Error = sqrt(Integral * (Area - Integral) / N)
    return Integral, Error


# Defining the integrand
def f(x):
    return sin(1/((2-x)*x))**2


MCInt, MCError = MCI(f, a, b, c, N)
print("Integral using the Monte Carlo method:", MCInt)
print("Error estimate on the method:", MCError)

# Part B


# Defining the function that carries out the integration using the mean value method
def MVI(f, a, b, N):
    dx = (b - a) / N
    sum = 0
    sqsum = 0
    for idx in range(N):
        x = random.uniform(a, b)
        sum += f(x)
        sqsum += f(x)**2
    Integral = sum * dx
    avgf = sum / N
    avgf2 = sqsum / N
    varf = avgf2 - avgf**2
    Error = (b - a) * sqrt(varf / N)
    return Integral, Error


MVInt, MVError = MVI(f, a, b, N)
print("Integral using mean value Monte Carlo method:", MVInt)
print("Error estimate:", MVError)

