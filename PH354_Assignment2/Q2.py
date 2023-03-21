# Exercise 2: Integral using Simpson's rule

# ANSWERS
# Trapezoidal integration converged slower than quadratic upon
# increasing number of slices (larger error in trapezoidal). This is as we would expect.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining the bounds of integration
a = 0
b = 2
n = (np.rint(np.logspace(1, 3, 100))).astype(int)
# n = np.array([11,101,1001])
answers = np.zeros((4, len(n)), dtype=float)
# Defining the expression/function to be integrated
def function_1(x):
    return x**4 - 2*x + 1

for idx in range(len(n)):
    answers[0][idx] = quad_int_func(function_1, a, b, n[idx])
    answers[1][idx] = trap_int_func(function_1, a, b, n[idx])
    answers[2][idx] = (answers[0][idx] - 4.4) / 4.4
    answers[3][idx] = (answers[1][idx] - 4.4) / 4.4

print("For quadratic integration the fractional errors decreased as follows upon increasing n = 10 to 100 to 1000")
print(answers[2])
print("For trapezoidal integration the fractional errors decreased as follows upon increasing n = 10 to 100 to 1000")
print(answers[3])
plt.plot(n, answers[0], label='Trapezoidal integration')
plt.plot(n, answers[1], label='Quadratic integration')
plt.plot(n, np.full_like(n, 4.4, dtype=float), label='Precise answer')
plt.title('Comparing integration methods')
plt.xlabel('Slices')
plt.ylabel('Integral')
plt.legend()
plt.yscale('linear')
plt.xscale('linear')
# plt.xscale('log')
plt.show()




