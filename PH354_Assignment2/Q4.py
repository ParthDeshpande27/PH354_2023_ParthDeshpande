# Exercise 4: The diffraction limit of a telescope

# Please wait for the code to run (you can increase the resolution to get a nicer looking graph)

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
a = 0
b = 20
n_theta = 401
n_x = 401
n_diff = 401
theta = np.linspace(0, np.pi, n_theta)
wavelength = 500e-9
x_min = -1e-6
y_min = -1e-6
x_max = 1e-6
y_max = 1e-6

# Defining the integrand
def function_1(*argv):
    return np.cos(argv[1]*argv[0] - argv[2]*np.sin(argv[0]))


# Defining J(m,x) with integration method being quadratic
def J(m, x):
    return quad_int_func(function_1, 0, np.pi, n_theta, m, x)/np.pi


# Creating the variable x
x = np.linspace(a, b, n_x)

# Plotting Bessel function graphs
plt.figure(0)
for idx in range(3):
    y = np.zeros_like(x)
    for jdx in range(n_x):
        y[jdx] = J(idx, x[jdx])
    plt.plot(x, y, label='J_' + str(idx))
plt.title('Plotting Bessel functions J_0, J_1, J_2')
plt.xlabel('x')
plt.ylabel('J(m,x)')
plt.grid()
plt.legend()
plt.yscale('linear')
plt.xscale('linear')

# Making a density plot for the circular diffraction pattern

# Define I(r)
def Intensity(r, wavelength):
    k = 2*np.pi/wavelength
    if r == 0:
        i = 1.0/4.0
    else:
        i = (J(1, k*r)/(k*r))**2
    return i

# Plotting diffraction pattern graph
plt.figure(1)

# Creating the required arrays

x_val = np.linspace(x_min, x_max, n_diff)
y_val = np.linspace(y_min, y_max, n_diff)
z_val = np.zeros((n_diff, n_diff))
for idx in range(n_diff):
    for jdx in range(n_diff):
        z_val[jdx][idx] = Intensity(np.hypot(x_val[idx], y_val[jdx]), wavelength)

plt.pcolormesh(x_val, y_val, z_val, shading='auto', vmax=0.03)
plt.axis('square')
plt.title('Plotting the circular diffraction pattern, vmax=0.03')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.yscale('linear')
plt.xscale('linear')

plt.show()



