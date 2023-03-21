# Exercise 11: Diffraction off a straight edge

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *

# Defining constants in SI units
wavelength = 1
n = 50
n_graph = 1001
x = np.linspace(-5, 5, n_graph)
z = 3
u = x * np.sqrt(2 / (wavelength * z))

# Defining C(u)
def C(u):
    x, w = gaussxwab(n, 0, u)
    return sum(w * np.cos(x**2 * np.pi/2))


# Defining S(u)
def S(u):
    x, w = gaussxwab(n, 0, u)
    return sum(w * np.sin(x**2 * np.pi/2))


# Defining I_normalized(x, z, wavelength)
def I_normalized(u):
    return ((2*C(u) + 1)**2 + (2*S(u) + 1)**2)/8


# Plotting the graph
I_normalized_val = np.zeros_like(u)
for idx in range(len(u)):
    I_normalized_val[idx] = I_normalized(u[idx])
plt.plot(x, I_normalized_val)
plt.title('Intensity profile of diffraction past straight edge')
plt.xlabel('x')
plt.ylabel('I/I_0')
plt.legend()
plt.yscale('linear')
plt.xscale('linear')
plt.show()




