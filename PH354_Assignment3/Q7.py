# Exercise 7: The roots of a polynomial

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
tol = 1e-12
bounds = [[0.03, 0.04], [0.16, 0.17], [0.38, 0.39], [0.61, 0.62], [0.83, 0.84], [0.96, 0.97]]
x = np.linspace(0, 1, 101)
h_derivative = 1e-8

# Defining the polynomial of which the roots we have to find
def P(x, *argv):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1


# Graphing it to find approximate bounds
plt.title('Graphical solution of P(x)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid(axis='both')
plt.scatter(x, P(x))
plt.yscale('linear')


# Upon graphing, we bracket the roots by modifying the bounds accordingly.

# Finding roots of P(x)
print('The 6 roots of P(x):')
for idx in range(len(bounds)):
    print('P_' + str(idx) + ': %.10f' % newton(P, np.mean(bounds[idx]), tol, h_derivative))

plt.show()