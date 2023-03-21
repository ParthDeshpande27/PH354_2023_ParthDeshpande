# Exercise 10: Period of an anharmonic oscillator

# ANSWERS
# Part A
# n is the exponent in the potential form (4, here) and k is the stiffness (1, here)
# m is the mass and a is the amplitude
# Prefactor = Sqrt( 8*m / (k*a**(n-2)) )
# T = Prefactor * Integration from 0 to 1 of (1 - y**n)**(-1/2) dy

# Part C
# From the Prefactor we can see that T is proportional to a**(1 - n/2)
# i.e., for n = 4, T is inversely proportional to a
# Therefore, as a decreases, T increases (i.e., blows up for a = 0)
# Another way to look at this:
# Taking n to be very large, we should get something like an infinite potential well.
# For a<1, we should get T ~ very large and for a>1, T ~ 0.
# i.e., for small amplitudes, the potential is too flat.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *

# Defining constants
m = 1
n = 20
n_graph = 101
amplitude = np.linspace(0, 2, n_graph)
stiffness = 1
exponent = 4

# Defining the potential
def V(x):
    return stiffness * x**exponent


# Defining the integrand
def function_1(x, amplitude, m):
    return (2*(V(amplitude) - V(x))/m)**(-1/2)


# Defining T(a)
def T(amplitude, m):
    x, w = gaussxwab(n, 0, amplitude)
    return 4*sum(w * function_1(x, amplitude, m))


# Plotting the graph
T_val = np.zeros_like(amplitude)
for idx in range(len(amplitude)):
    T_val[idx] = T(amplitude[idx], m)
plt.plot(amplitude, T_val)
plt.title('Calculating the time period of V(x) = ' + str(stiffness) + '*x^' + str(exponent) + ' oscillator against amplitude')
plt.xlabel('Amplitude')
plt.ylabel('Time period')
plt.legend()
plt.yscale('linear')
plt.xscale('linear')
plt.show()




