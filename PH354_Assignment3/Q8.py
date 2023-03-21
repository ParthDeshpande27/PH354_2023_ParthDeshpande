# Exercise 8: The Lagrange point

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
w = 2.662e-6
tol = 1e-6
h_derivative = 1e-8
x = np.linspace(0, 1, 1000)
bounds = [0.92, 0.93]
alpha = m/M
gamma = R**3 * w**2 / (G * M)


# Defining the equation for x
def P(x):
    return alpha * (x**2) - ((1 - x)**2) - gamma * ((x**3) * ((1 - x)**2))


# Graphing it to find approximate bounds
plt.title('Graphical solution of abs(P(x)) on a log-scale')
plt.xlabel('r')
plt.ylabel('P(x)')
plt.scatter(x, abs(P(x)))
plt.grid(axis='both')
plt.yscale('log')

# Upon graphing, we bracket the roots by modifying the bounds accordingly.

# Finding the root of P(x)
x_1 = secant(P, bounds, tol)
print('x_1: %.4E' % x_1)
L_1 = R * x_1
print('L_1 in metres: %.4E' % L_1)

plt.show()
