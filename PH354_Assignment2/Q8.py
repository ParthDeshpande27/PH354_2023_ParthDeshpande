# Exercise 8: Adaptive Simpson's integration

# ANSWERS
# For adaptive trapezoidal integration: n = 2286
# For adaptive quadratic integration: n = 42
# For Romberg integration: n = 7


import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
import time

# Defining constants
a = 0
b = 1
tol = 1e-6

# Defining the integrand
def function_1(x):
    return np.sin(np.sqrt(100*x))**2


# Results
print("The number of slices, value of the integral, error, and time required using adaptive quadratic integration is: ")
start1 = time.time()
print(adaptive_quad(function_1, a, b, tol))
end1 = time.time()
print("The time required in seconds is %f" % (end1 - start1))

# print("\nAs you can see, Romberg integration is still faster than adaptive quadratic integration.")



