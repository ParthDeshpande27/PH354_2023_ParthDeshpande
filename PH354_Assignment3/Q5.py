# Exercise 5: Wien’s displacement constant

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from scipy.constants import h, c, k, pi

# Defining constants
alpha = 2*pi*h*c**2
beta = h*c/k
tol = 1e-6
a = 4
b = 5
wavelength = 502e-9


# Defining the equation for intensity
def I(lamda, T):
    return alpha/(lamda**5 * (np.exp(beta/(lamda*T)) - 1))


# Defining the equation for binary search method
def f(x):
    return 5*np.exp(-x) + x - 5


# Finding a root of $ 5 * e^{-x} + x - 5 $
x_root = binary_search(f, tol, [a, b])
print('The root of the equation is %f' % x_root)
displacement_constant = beta/x_root
print('The obtained value of Wien\'s displacement_constant in Kelvin metre is %f' % displacement_constant)
sun_surface_temp = displacement_constant/wavelength
print('The surface temperature of the Sun in Kelvin can be estimated to be %f' % sun_surface_temp)
