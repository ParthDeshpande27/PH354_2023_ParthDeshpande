# Exercise 14: Gravitational pull of a uniform sheet

# ANSWERS
# Part A
# The answer is given in the attached pdf.
# Part C
# The artifact comes from our assumption that
# the sheet has negligible thickness and that we have a point mass.
# As z decreases, Fz attains a maximum and begins decreasing. This is due to the z term
# in the numerator (i.e., more mass is to the sides and less is directly downwards. This
# effect is akin to freely floating inside a hollow earth.).
# For a real sheet and unit mass ball of nonzero radius, z cannot become 0, i.e., Fz will never
# reach 0. We could remove the 'artifact' by assuming sheet and ball of nonzero 3D sizes.
# For efficiency, we could use the Shell Theorem and continue assuming the unit mass to be a point.
# That would entail us having to neglect the graph below a certain z.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import G

# Defining constants in SI units
total_mass = 10000
L = 10
total_area = L**2
sigma = total_mass/total_area
z = np.linspace(0, 10, 1001)
n = 100
pts, w = gaussxwab(n, -L / 2, L / 2)

# Defining the integrand
def function_1(x, y, z):
    return (x**2 + y**2 + z**2)**(-3/2)

# Calculating the integral

def Fz(z, pts, w):
    sum = 0
    for idx in range(len(pts)):
        for jdx in range(len(pts)):
            sum += w[idx] * w[jdx] * function_1(pts[idx], pts[jdx], z)
    return sum * z * G * sigma

# Part B

# Plotting the graph
Fz_val = np.zeros_like(z)
for idx in range(len(z)):
    Fz_val[idx] = Fz(z[idx], pts, w)
plt.plot(z, Fz_val)
plt.title('Gravitational force by sheet on unit point mass against distance')
plt.xlabel('z')
plt.ylabel('Fz')
plt.legend()
plt.yscale('asinh')
plt.xscale('asinh')
plt.show()



