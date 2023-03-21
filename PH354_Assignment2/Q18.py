# Exercise 18: Differentiating by integrating
import math

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import pi
import cmath

# Defining constants in SI units
N = 100
k = np.linspace(0, N-1, N)
z_k = np.exp(k * (2*pi*1j / N))
m = np.linspace(0, 20, 21).astype(int)

# Defining the function
def function_1(z):
    return np.exp(2*z)


# Defining the derivative
def Derivative_0(f, m):
    return math.factorial(m) * sum(f(z_k) * np.exp(k * (-2*pi*1j*m / N))) / N


print("The first 20 derivatives of the given function e^2z at z=0: ")
for idx in m:
    print("Derivative for m = " + str(idx) + " is equal to", end=' ')
    print(np.real(Derivative_0(function_1, idx)))

# As the printed output shows, the values are close to powers of 2 as expected.