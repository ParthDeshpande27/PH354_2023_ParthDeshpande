# Exercise 12: Exercise 10 using numpy.linalg.solve

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
V_0 = 5

# Defining the matrix A
A = np.array([[ 4, -1, -1, -1],
           [-1, -1, -1, 4],
           [-1, 0, 3, -1],
           [-1, 3, 0, -1]], float)

# Defining the vector v
v = np.array([V_0, 0, 0, V_0], float).transpose()

print('The four voltages in Volts are:')
x = np.linalg.solve(A, v)
print(x)
print('The same answer is obtained as in Exercise 10')
