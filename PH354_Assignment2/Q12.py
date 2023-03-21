# Exercise 12: The Stefan–Boltzmann constant

# ANSWERS
# Part A
# The answer amounts to algebraic manipulation, which is expounded in the attached pdf.
# Part B
# Gaussian quadrature was used with n = 40. The upper limit of
# the integral was considered to be L = 50. The value of the integrand at L = 50
# is vanishingly small.
# By comparing with the known value, the calculated value of the integral is
# accurate up to 15 significant digits.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import hbar, pi, c, k, sigma

# Defining constants in SI units
L = 50
n = 40
prefactor = (k**4)/(hbar**3 * (2*pi*c)**2)


# Defining the integrand
def function_1(x):
    return (x**3) / (np.exp(x) - 1)


# Calculating the integral
def I(L, n):
    return gaussian_int(function_1, 0, L, n)


# Getting Stefan-Boltzmann constant
def stefan_boltzmann(L, n):
    return prefactor * I(L, n)


# Printing the results
print("Evaluation of the integral:", end=" ")
print(I(L, n))
print("Evaluation of the integral analytically:", end=" ")
print((pi**4)/15)
print("By comparing with the known value, the calculated value "
      " of the integral is accurate up to 15 significant digits i.e., 14 decimal places.")
print("My value of the Stefan-Boltzmann constant:", end=" ")
print(stefan_boltzmann(L, n))
print("Known value of the Stefan-Boltzmann constant:", end=" ")
print(sigma)
print("By comparing with the known value, the calculated value "
      " of the Stefan-Boltzmann constant is accurate up to 10 significant digits.")




