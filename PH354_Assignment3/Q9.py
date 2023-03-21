# Exercise 9: Nonlinear circuits

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
R = np.array([1, 4, 3, 2]) * 1e3
V_T = 0.05
I_0 = 3e-9
V_0 = 5
tol = 1e-13                         # Low tolerance because the currents are in nA
I_initial = np.array([1.0, 1.0, 1.0, 1.0]) * I_0


# Defining the equations vector
def current_equations(I):
    I_D = I_0 * (np.exp((I[1] * R[1] - I[3] * R[3]) / V_T) - 1)
    return np.array([V_0 - I[0]*R[0] - I[1]*R[1],
                     V_0 - I[2]*R[2] - I[3]*R[3],
                     I[0] - I[1] - I_D,
                     I[2] - I[3] + I_D]).transpose()


# Defining the Jacobian
def jacobian(I):
    gamma = I_0 * np.exp((I[1]*R[1] - I[3]*R[3])/V_T) / V_T
    alpha = 1 + R[0]*gamma
    beta = -R[2]*gamma
    return np.array([[-R[0],    -R[1],  0,    0],
                     [0,      0,    -R[2],  -R[3]],
                     [alpha,      -1,  beta,    0],
                     [1 - alpha,    0,   1 - beta,    -1]], float)


I_final = nd_newton(current_equations, jacobian, I_initial, tol)
print('I1 to I4 in A:')
print(I_final)
print('V1 and V2 in V:')
print([I_final[1] * R[1], I_final[3] * R[3]])
print('The diode voltage V:')
V_diode = I_final[1]*R[1] - I_final[3]*R[3]
print(V_diode)
print('This is indeed close to the electronic engineer’s rule of thumb for diodes i.e., 0.6 V.')


