# Exercise 9: Heat capacity of a solid

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *

# Defining constants
k_B = 1.380649e-23
V = 0.001
rho = 6.022e28
Debye_T = 428
n = 50
n_graph = 1000
T = np.linspace(5, 500, n_graph)


# Defining the integrand
def function_1(x):
    return (x**4)*np.exp(x)/((np.exp(x)-1)**2)


# Defining Cv
def Cv(T, V, rho, Debye_T, n):
    a = 0
    b = Debye_T/T
    prefactor = 9*V*rho*k_B/(b**3)
    return prefactor * gaussian_int(function_1, a, b, n)


# Plotting the graph
Cv_val = np.zeros_like(T)
for idx in range(len(T)):
    Cv_val[idx] = Cv(T[idx], V, rho, Debye_T, n)
plt.plot(T, Cv_val)
plt.title('Calculating the heat capacity of Aluminium against temperature')
plt.xlabel('T')
plt.ylabel('Cv(T)')
plt.legend()
plt.yscale('linear')
plt.xscale('linear')
plt.show()




