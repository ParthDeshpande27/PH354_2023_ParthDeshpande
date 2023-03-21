# Exercise 14: A chain of resistors

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
V_0 = 5
N = [6, 10000]

# Part A


# Defining the matrix A
def A(N):
    equations = np.zeros((N, N))
    for jdx, element in enumerate([3, -1, -1]):
        equations[0][jdx] = element
    for jdx, element in enumerate([-1, 4, -1, -1]):
        equations[1][jdx] = element
    for jdx, element in enumerate([-1, -1, 4, -1]):
        equations[N-2][N - 4 + jdx] = element
    for jdx, element in enumerate([-1, -1, 3]):
        equations[N-1][N - 3 + jdx] = element
    for idx in range(2, N-2):
        for jdx, element in enumerate([-1, -1, 4, -1, -1]):
            equations[idx][idx - 2 + jdx] = element
    return equations


# Defining the vectors v
v0 = np.zeros(N[0]).transpose()
v0[0] = V_0
v0[1] = V_0
v1 = np.zeros(N[1]).transpose()
v1[0] = V_0
v1[1] = V_0
v = [v0, v1]

x0 = np.copy(v0)                          # Stores the solutions for N[0]
x1 = np.copy(v1)                          # Stores the solutions for N[1]
x = [x0, x1]

# Part B
for idx, element in enumerate(N):
    print('The ' + str(element) + ' voltages in Volts are:')
    # x[idx] = np.linalg.solve(A(element), v[idx])
    # x[idx] = Gaussian_elimination(A(element), v[idx])
    # The Naive Gaussian_elimination would have taken 50 minutes to run
    x[idx] = Gaussian_elimination_banded_pp(A(element),  v[idx], 2)
    print(x[idx])
# Part C

# Printing the results to a text file results.txt
with open('potentials.txt', 'w') as file:
    for idx in range(N[1]):
        file.write('V_' + str(idx+1) + ': ' + str(x[1][idx]) + '\n')
