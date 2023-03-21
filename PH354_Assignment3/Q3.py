# Exercise 3: Percolation transition

# ANSWERS

# Note
# The accelerated fixed point iteration (using Steffensen's method) took 4 iterations to give
# an answer accurate to 10 decimal places!!

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
np.set_printoptions(precision=14)

# Defining constants
c = 2
tol = 1e-6
step = 0.01
c_val = np.arange(0+step, 3+step, step)
x0 = 1


def f(argv):
    return np.array([1 - np.exp(-1 * argv[0] * argv[1]), argv[1]])


print('Solution using FPI with number of steps, x and c:')
print(fpi(f, tol, True, [x0, c]))
print('Solution using accelerated FPI with number of steps, x and c:')
print(acc_fpi(f, tol, True, [x0, c]))

acc_fpi_val = np.zeros((len(c_val)), dtype=float)
for idx in range(len(c_val)):
    acc_fpi_val[idx] = acc_fpi(f, tol, False, [x0, c_val[idx]])[1][0]

plt.plot(c_val, acc_fpi_val)
plt.title('Solution to $x = 1 - e^{-cx}$ against c')
plt.xlabel('c')
plt.ylabel('$x_{*}$')
plt.savefig('Q3_1.jpg')
plt.show()
