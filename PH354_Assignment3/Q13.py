# Exercise 13: Complicated circuit problem

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
import cmath

# Defining constants
x_0 = 3
C = np.array([1, 0.5]) * 1e-6
w = 100000
R = np.array([1, 2]*3)

# Defining the matrix A
A = np.zeros((3, 3), complex)

A[0][0] = 1/R[0] + 1/R[3] + 1j*w*C[0]
A[0][1] = -1j*w*C[0]

A[1][0] = -1j*w*C[0]
A[1][1] = 1/R[4] + 1/R[1] + 1j*w*C[1]
A[1][2] = -1j*w*C[1]

A[2][1] = -1j*w*C[1]
A[2][2] = 1/R[2] + 1/R[5] + 1j*w*C[1]

print(A)

# Defining the vector v
v = np.array([x_0/R[0], x_0/R[1], x_0/R[2]], float).transpose()

print('The 3 voltages in Volts are:')
x = np.linalg.solve(A, v)
for idx in range(len(x)):
    print('V_' + str(idx) + ' = ', np.abs(x[idx]), ' with phase in degrees = ', np.degrees(cmath.phase(x[idx])))
