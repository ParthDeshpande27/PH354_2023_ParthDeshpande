# Exercise 10: A random point on the surface of the Earth

# Importing useful modules
import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi, acos


# Generating random theta, phi
theta = 2*pi * random.uniform(0, 1)
phi = acos(1 - 2 * random.uniform(0, 1))
print("Theta: ", theta)
print("Phi: ", phi)

# Plotting the probability distribution of theta and phi
theta_list = []
phi_list = []
N = int(1e6)
for i in range(N):
    theta_list.append(2*pi * random.uniform(0, 1))
    phi_list.append(acos(1 - 2 * random.uniform(0, 1)))

# Plotting the probability distribution of theta
plt.figure()
plt.hist(theta_list, bins=100, density=True)
plt.title("Probability distribution of theta")
plt.xlabel("Theta")
plt.ylabel("Probability")
plt.savefig("Q10_theta.jpg")
plt.show()

# Plotting the probability distribution of phi
plt.figure()
plt.hist(phi_list, bins=100, density=True)
plt.title("Probability distribution of phi")
plt.xlabel("Phi")
plt.ylabel("Probability")
plt.savefig("Q10_phi.jpg")
plt.show()