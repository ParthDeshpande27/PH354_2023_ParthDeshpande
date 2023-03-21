# Exercise 3: Gaussian integral

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
n = (np.rint(np.logspace(1, 5, 10))).astype(int)

# Defining the integrand
def function_1(x):
    return np.exp((-1) * x ** 2)


# Defining E(x) with integration method being quadratic
def E(x, n):
    a = 0
    b = x
    return quad_int_func(function_1, a, b, n)


# Creating the variable x
x = np.linspace(0, 3, 31)

# Plotting all graphs
for idx in range(len(n)):
    plt.plot(x, E(x, n[idx]), label='N:' + str(n[idx]))
plt.title('Calculating the Gaussian integral')
plt.xlabel('x')
plt.ylabel('E(x)')
plt.legend()
plt.yscale('linear')
plt.xscale('linear')
plt.show()



