# Exercise 17: Electric field of a charge distribution

# Note: The centres of the point charges show weird
# behaviours since the potential and the field blow up there. This causes the gradient to be
# incalculable (i.e., the point charges may seem like a white centre even if blackness depicts magnitude
# electric field)

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import epsilon_0, pi
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib import cm

# Defining constants in SI units
grid_spacing = 0.01
dipole_data = np.array([[-0.05, 0, -1], [0.05, 0, 1]])
L = 0.1
q0 = 100
a_x = np.arange(-0.5, 0.5+grid_spacing, grid_spacing)
a_y = np.arange(-0.5, 0.5+grid_spacing, grid_spacing)
a_xx, a_yy = np.meshgrid(a_x, a_y)
n = 32
pts, weights = gaussxwab(n, -L/2, L/2)

# Part A

# Defining the potential function
def phi(q, x, y):
    return q / (4 * pi * epsilon_0 * np.hypot(x, y))


# Plotting the potential due to dipole
grid_potential = phi(dipole_data[0][2], a_xx - dipole_data[0][0], a_yy - dipole_data[0][1]) + \
                 phi(dipole_data[1][2], a_xx - dipole_data[1][0], a_yy - dipole_data[1][1])
f1 = plt.figure(1)
plt.imshow(grid_potential, extent=[-0.5, 0.5, -0.5, 0.5], vmin=-1e10, vmax=1e10, cmap='RdBu')
plt.gca().set_aspect('equal')
plt.xlabel('x in meters')
plt.ylabel('y in meters')
plt.title('Potential field in volts for a dipole')
plt.colorbar()
plt.legend()

# Part B

# Plotting the electric field due to dipole
f2 = plt.figure(2)
Ef = -gradient(grid_potential, grid_spacing)
E_mag = np.hypot(Ef[0], Ef[1])
plt.imshow(E_mag, extent=[-0.5, 0.5, -0.5, 0.5],  norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,
                                              vmin=1e10, vmax=1e12, base=10), cmap='RdBu')
plt.colorbar()
plt.streamplot(a_x, a_y, Ef[0], Ef[1])
plt.gca().set_aspect('equal')
plt.xlabel('x in meters')
plt.ylabel('y in meters')
plt.title('Electric field in volts/metre for a dipole')
plt.legend()

# Part C


# Defining the charge density
def sigma(x, y):
    return q0 * np.sin((2 * np.pi * x)/L) * np.sin((2 * np.pi * y)/L)


# Plotting the potential due to charge density
def charge_dist_potential(x, y):
    sum = 0
    for jdx in range(len(pts)):
        for idx in range(len(pts)):
            sum += weights[idx] * weights[jdx] * phi(sigma(pts[idx], pts[jdx]), x-pts[idx], y-pts[jdx])
    return sum


grid_potential1 = charge_dist_potential(a_xx, a_yy)
print(np.shape(grid_potential1))
f3 = plt.figure(3)
plt.imshow(grid_potential1, extent=[-0.5, 0.5, -0.5, 0.5], vmin=-1e8, vmax=1e8, cmap='RdBu')
plt.gca().set_aspect('equal')
plt.xlabel('x in meters')
plt.ylabel('y in meters')
plt.title('Potential field in V due to sigma')
plt.colorbar()
plt.legend()


# Plotting the electric field due to charge density
f4 = plt.figure(4)
Ef1 = -gradient(grid_potential1, grid_spacing)
E_mag1 = np.hypot(Ef1[0], Ef1[1])
plt.imshow(E_mag1, extent=[-0.5, 0.5, -0.5, 0.5],  norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,
                                              vmin=1e8, vmax=1e10, base=10), cmap='RdBu')
plt.colorbar()
plt.streamplot(a_x, a_y, Ef1[0], Ef1[1])
plt.gca().set_aspect('equal')
plt.xlabel('x in meters')
plt.ylabel('y in meters')
plt.title('Electric field in V/m due to sigma')
plt.legend()
plt.show()

