# Exercise 7: Diffraction gratings

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from dcst import dct, dst

# Defining constants in SI units
wavelength = 500e-9
slit_separation = 20e-6
number_of_slits = 10
grating_width = (number_of_slits + 1)*slit_separation
screen_width = 10e-2
focal_length = 1
N = 1000


# Defining the transmission function of the grating
def q(u, alpha=np.pi/slit_separation):
    return (np.sin(alpha * u))**2


# Defining a function that calculates the intensity
def intensity(w, N, lamda=wavelength, f=focal_length):
    k = np.arange(-5*N, 5*N, 1)
    u = np.linspace(-w / 2, w / 2, N)
    y = np.sqrt(q(u))
    y = np.pad(y, (0, int(4.5*N)), mode='constant')
    y = np.pad(y, (int(4.5*N), 0), mode='constant')
    ck2 = np.abs(np.fft.fft(y))**2
    x = (lamda*f/(10*w))*k
    return x, (w/N)**2 * ck2


# Creating the value arrays
x, I_val = intensity(grating_width, N)

# Define a plotting function
def intensity_plot(x, I_val):
    fig, (ax0, ax1) = plt.subplots(nrows=2, gridspec_kw={'height_ratios': [7, 1]})
    ax0.set_title('Intensity through a diffraction grating for q(u)')
    ax0.set_ylabel('I(x)')
    I_val = np.concatenate((np.flip(I_val[0:len(I_val)//2+1]), np.flip(I_val[len(I_val)//2:-1])))
    ax0.plot(x, I_val)
    ax0.set_xlim(-screen_width/2, screen_width/2)
    ax1.set_xlabel('x')
    ax1.imshow(np.atleast_2d(I_val[int(4.75*N):int(5.25*N)]), cmap='gray', extent=(-screen_width/2, screen_width/2, 0, 0.01))
    ax1.set_xlim(-screen_width/2, screen_width/2)

# Plotting the graph
intensity_plot(x, I_val)
plt.savefig('Q7_1.jpg')
plt.show()