# Exercise 1: Velocity Graphs

# Comments
# The velocities are very small and yet lead to large displacements due to the large timescales involved.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Importing data from text file
velocities_data = np.loadtxt("velocities.txt")

# Creating the time and velocity arrays
time = velocities_data.transpose()[:][0]
velocity = velocities_data.transpose()[:][1]

# Calculating the slice width
h = (time[-1] - time[0])/len(time)

# Calculating the distance traveled by trapezoidal rule
distance_traveled = np.zeros_like(time)
for idx in range(len(time)-1):
    distance_traveled[idx+1] = distance_traveled[idx] + (time[idx+1] - time[idx])*velocity[idx]

# Plotting both graphs
plt.plot(time, velocity, label='Velocity-Time graph')
plt.plot(time, distance_traveled, label='Displacement-Time graph')
plt.title('Moving particle graphs')
plt.xlabel('Time')
plt.ylabel('Displacement and Velocity')
plt.legend()
# plt.yscale('asinh')
plt.yscale('linear')
plt.show()