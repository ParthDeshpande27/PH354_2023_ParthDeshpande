# Exercise 11: Gaussian elimination with partial pivoting

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
x = Gaussian_elimination_pp(A, v)
print(x)

# Defining the matrix B
B = np.array([[ 0, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)

# Defining the vector v
v1 = np.array([-4, 3, 9, 7], float).transpose()

print('w,x,y,z with pivoting:')
y = Gaussian_elimination_pp(B, v1)
print(y)
print('w,x,y,z using numpy.linalg.solve:')
y = np.linalg.solve(B, v1)
print(y)
# print('w,x,y,z without pivoting:')
# y = Gaussian_elimination(B, v1)
# print(y)