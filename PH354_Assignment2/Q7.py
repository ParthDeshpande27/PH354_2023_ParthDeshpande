# Exercise 7: Adaptive trapezoidal integration and Romberg integration

# ANSWERS

# Part A
# Due to my interpretation of the adaptive integration (total slices don't go
# as powers of 2), outputting values of integral and intermediate slices
# makes little sense and only the final estimate of the integral and the error is printed.

# Part B
# As seen from the printed output, Romberg integration is much faster.

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
print("The number of slices, value of the integral, error, and time required using adaptive trapezoidal integration is: ")
start1 = time.time()
print(adaptive_trap(function_1, a, b, tol))
end1 = time.time()
print("The time required in seconds is %f" % (end1 - start1))
print("")
print("The number n, value of the integral and time required using Romberg integration is: ")
start2 = time.time()
print(Romberg_int(function_1, a, b, tol))
end2 = time.time()
print("The time required in seconds is %f" % (end2 - start2))

print("\nAs you can see, Romberg integration is much faster even for greater accuracy than required.")
