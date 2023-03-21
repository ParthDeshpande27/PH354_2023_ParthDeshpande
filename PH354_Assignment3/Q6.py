# Exercise 6: 1D finite potential well

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from scipy.constants import hbar, electron_mass, electron_volt

# Defining constants
V = 20      # potential height in eV
w = 1e-9    # potential width in m
alpha = w * np.sqrt(2 * electron_mass * electron_volt) / hbar
tol = 1e-5
bounds = [[0.2, 0.4], [1.2, 1.3], [2.7, 2.9], [5.0, 5.1], [7.8, 7.9], [11.2, 11.3], [15.0, 15.1]]
E_val = np.arange(0.1, 20-0.1, 0.1)

# Defining the equation for false position method
def f(E, V=V, alpha=alpha):
    beta = np.sqrt(E/(V-E))
    gamma = alpha * np.sqrt(E)
    return np.sin(gamma) - 2*np.cos(gamma) / (beta - 1/beta)


# Graphing it to find approximate bounds
plt.title('Graphical solution of bound states in finite potential well')
plt.xlabel('E in eV')
plt.ylabel('f(E)')
plt.grid(axis='both')
plt.scatter(E_val, f(E_val))
plt.yscale('asinh')


# Upon graphing, we find a singularity at 10 (as expected). We modify the bounds accordingly.

# Finding roots of f(E) to find bound energy eigenstates in eV
print('The first 6 energy levels in eV:')
for idx in range(len(bounds)):
    print('E_' + str(idx) + ': %.4f' % false_position(f, tol, bounds[idx]))

plt.show()