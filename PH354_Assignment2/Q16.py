# Exercise 16: Diffraction gratings

# ANSWERS

# Part A
# slit separation is pi/alpha (The answer is given in the attached pdf).

# Part C
# Gaussian quadrature was used to calculate the integrals.
# The number of points is decided by how much the function oscillates in the interval of integration.
# By Sampling theorem, the number of points should be at least larger than twice the number of oscillations.
# The integrand has number of oscillations of the order 10. Therefore, n=100 for gaussian quadrature
# should give us accurate results.
# (A rough calculation is done in the attached pdf)


import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *

# Defining constants in SI units
wavelength = 500e-9
slit_separation = 20e-6
number_of_slits = 10
grating_width = (number_of_slits + 1)*slit_separation
screen_width = 10e-2
focal_length = 1
x = np.linspace(-screen_width/2, screen_width/2, 1001)
y = np.linspace(0, 0.1, 1)
n = 100
pts, weights = gaussxwab(n, -grating_width/2, grating_width/2)
q2lim = np.array([-5, 5, 50, 70]) * 1e-6

# Part B

# Defining the transmission function of the grating
def q(u, alpha=np.pi/slit_separation):
    return (np.sin(alpha * u))**2


# Defining the transmission function of the grating for Part E, I
def q1(u, alpha=np.pi/slit_separation, beta=np.pi/(2*slit_separation)):
    return (np.sin(alpha * u) * np.sin(beta * u))**2


# Defining the transmission function of the grating for Part E, II
def q2(u):
    if q2lim[0] <= u <= q2lim[1] or q2lim[2] <= u <= q2lim[3]:
        return 1
    else:
        return 0


# Defining the integral
def integral(x, qi, u=pts, w=weights, lamda=wavelength, f=focal_length):
    I = sum(w * np.sqrt(qi(u)) * np.exp(1j * 2 * np.pi * x * u / (lamda * f)))
    return I


# Defining intensity(x)
def intensity(x, qi, u=pts, w=weights, lamda=wavelength, f=focal_length):
    I = sum(w * np.sqrt(qi(u)) * np.exp(1j * 2 * np.pi * x * u / (lamda * f)))
    return abs(I)**2


# Plotting the graphs
I_val = np.zeros_like(x)
transmission_functions = [q, q1, q2]


# Define a plotting function
def intensity_plot(x, I_val, idx):
    fig, (ax0, ax1) = plt.subplots(nrows=2, gridspec_kw={'height_ratios': [7, 1]})
    ax0.set_title('Intensity through a diffraction grating for q(u)_' + str(idx))
    ax0.set_ylabel('I(x)')
    ax0.plot(x, I_val)
    ax1.set_xlabel('x')
    ax1.imshow(np.atleast_2d(I_val), cmap='gray', extent=(-screen_width/2, screen_width/2, 0, 0.01))


# Part C, D, E1
for idx in range(len(transmission_functions)-1):
    for jdx in range(len(x)):
        I_val[jdx] = intensity(x[jdx], transmission_functions[idx])
    intensity_plot(x, I_val, idx)


# Part E2
def E2_intensity(x):
    pts1, weights1 = gaussxwab(n, q2lim[0], q2lim[1])
    pts2, weights2 = gaussxwab(n, q2lim[2], q2lim[3])
    I1, I2 = 0, 0
    for idx in range(len(pts1)):
        I1 += weights1[idx] * np.sqrt(q2(pts1[idx])) * np.exp(1j * 2 * np.pi * x * pts1[idx] / (wavelength * focal_length))
        I2 += weights2[idx] * np.sqrt(q2(pts2[idx])) * np.exp(1j * 2 * np.pi * x * pts2[idx] / (wavelength * focal_length))
    return np.abs(I1 + I2)**2


for jdx in range(len(x)):
    I_val[jdx] = E2_intensity(x[jdx])
intensity_plot(x, I_val, len(transmission_functions)-1)

plt.show()