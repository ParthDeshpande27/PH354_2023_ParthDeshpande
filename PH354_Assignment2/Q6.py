# Exercise 5: Error in Simpson's rule

# ANSWERS
# The errors do not agree perfectly because the estimated error is only till O(h**8). We should get a
# better estimate of the error upon considering more terms.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
a = 0
b = 2
n = np.array([11, 21])
h = (b-a)/(n-1)


# Defining the integrand
def function_1(x):
    return x**4 - 2*x + 1


# Results
I = np.zeros_like(n, dtype=float)
for idx in range(len(I)):
    I[idx] = quad_int_func(function_1, a, b, n[idx])
Error = (I[1] - I[0])/(((n[1] - 1)/(n[0] - 1))**4 - 1)
print("Quadratic integration with n = " + str(n[0]) + ":")
print(I[0])
print("Quadratic integration with n = " + str(n[1]) + ":")
print(I[1])
print("Estimate of the error in the integration with n = " + str(n[1]) + ":")
print(Error)
print("Error compared to precise answer: ")
True_Error = 4.4 - I[1]
print(True_Error)
print("Percentage error in the estimated error: ")
percent_error_in_error = 100*(Error - True_Error)/True_Error
print(percent_error_in_error)



