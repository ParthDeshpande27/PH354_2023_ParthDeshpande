# Exercise 13: Quantum uncertainty in the harmonic oscillator

import math
import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *

# Defining constants in SI units
L = 1000
a_num = np.array([0, 1, 2, 3])
a_x = np.linspace(-4, 4, 1000)
b_num = 30
b_x = np.linspace(-10, 10, 2000)
c_n = 100
c_num = 5
c_L = 8

# Defining H(n,x)
def Hbar(n, x):
    if n == 0:
        return 1/np.sqrt(np.sqrt(np.pi))
    elif n == 1:
        return x * np.sqrt(2/np.sqrt(np.pi))
    else:
        return np.sqrt(2/n)*x*Hbar(n-1, x) - np.sqrt((n-1)/n)*Hbar(n-2, x)

def H(n, x):
    H = np.zeros((n+1, len(x)))
    if n == 0:
        return 1
    if n == 1:
        return 2*x
    H[0] = 1
    H[1] = 2 * x
    for i in range(2, n+1):
        H[i] = 2 * x * H[i-1] - 2 * (i-1) * H[i-2]
    return H[n]

# Defining the wavefunction
def Psi(n, x):
    return H(n, x) * np.exp((-1/2) * x**2) / np.sqrt(np.sqrt(np.pi) * 2**n * math.factorial(n))

# Part A: Plotting the wavefunctions for different n
f1 = plt.figure(1)
for idx in a_num:
    plt.plot(a_x, Psi(idx, a_x), label='n = ' + str(idx))
plt.title('Plotting the wavefunctions for different n')
plt.xlabel('x')
plt.ylabel('Psi(n, x)')
plt.legend()

# Part B: Plotting the wavefunction for n = 30
# Please wait for about 10-20 seconds for the generation of the figures
f2 = plt.figure(2)
plt.plot(b_x, Psi(b_num, b_x), label='n = ' + str(b_num))
plt.title('Plotting the wavefunction for n = 30')
plt.xlabel('x')
plt.ylabel('Psi(' + str(b_num) + ', x)')
plt.legend()

# Part C: Quantum uncertainty


# Defining the integrand
def function_1(n,x):
    return x**2 * abs(Psi(n, x))**2


def x_avg(c_num):
    x, w = gaussxwab(c_n, -c_L, c_L)
    return sum(w * function_1(c_num, x))


print("The uncertainty for the particle in n = " + str(c_num) + ' is: ', end=' ')
experimental_uncertainty = np.sqrt(x_avg(c_num))
print(experimental_uncertainty)
print("The expected uncertainty for the particle in n = " + str(c_num) + ' is: ', end=' ')
theoretical_uncertainty = np.sqrt(c_num + 0.5)
print(theoretical_uncertainty)
print("The percentage error in the obtained uncertainty for the particle in n = " + str(c_num) + ' is: ', end=' ')
percent_error = 100*(experimental_uncertainty - theoretical_uncertainty)/theoretical_uncertainty
print(percent_error)
plt.show()






