# Exercise 19: Image processing and the STM

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import G

# Defining some global constants
h = 30000.0
h_stm = 2.5
phi = math.radians(45)


# Loading the files
altitude_data = np.loadtxt('altitude.txt')
stm_data = np.loadtxt('stm.txt')
x = np.arange(0, len(stm_data[0]), h)
y = np.arange(0, len(stm_data[1]), h)

# Defining the function for intensity
def I(grid, h=h, phi=phi):
    grad = gradient(grid, h)
    intensity = (np.cos(phi)*grad[0] + np.sin(phi)*grad[1]) / np.hypot(1, grad[0], grad[1])
    return intensity


# Plotting the graphs
f = [0, 1, 2, 3, 4]

f[0] = plt.figure(0)
plt.title('Density map of raw altitude data')
plt.imshow(altitude_data)
plt.xticks()
#plt.savefig('Q19_0')

f[1] = plt.figure(1)
plt.title('Relief map of altitude data')
plt.imshow(I(altitude_data))
#plt.savefig('Q19_1')


f[2] = plt.figure(2)
plt.title('Density map of raw STM data')
plt.imshow(stm_data)
#plt.savefig('Q19_2')

f[3] = plt.figure(3)
plt.title('Relief map of STM data')
plt.imshow(I(stm_data, h_stm))
#plt.savefig('Q19_3')


plt.show()