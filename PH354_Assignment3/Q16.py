# Exercise 16: Asymmetric quantum well

# ANSWERS
# The ground state energy calculated at N = 10 and N = 100 only
# differed by 1e-7 eV.
# The 10th energy level (i.e., 9th excited state) differed in
# first decimal place (i.e., 0.1 eV)
# Often we are interested in the ground state energy (or the first
# 2-3 excited states), therefore this calculation is very accurate.
# For lower states, the Fourier coefficients of high frequencies are small.

# NOTE: The normalization constant is the same (2.5) for all eigenfunctions considered.
# This is expected because the normalization of a state does not change once set.
# We can easily calculate the normalization constant for one eigenstate and
# extend its usage to every eigenstate.

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from scipy.constants import hbar, pi, m_e, electron_volt

# Defining constants
L = 5    # The width of the well in Angstroms
a = 10           # The value of 'a' in the expression of the potential in eV
factor = (hbar * 1e10)**2 / (m_e * electron_volt) * ((np.pi**2) / (2 * L**2))


# Defining the expression for the Hamiltonian matrix element in eV
def matrix_element(m, n):
    if m == n:
        return factor * n**2 + a/2
    if ((m ^ n) & 1) != 0:
        return (-8 * a * m * n)/(pi * (m**2 - n**2))**2
    else:
        return 0


# Defining a function that creates the matrix to calculate the eigenvalues
def matrix_creator(matrix_element, N):
    return np.array([[matrix_element(m, n) for m in range(1, N+1)] for n in range(1, N+1)])


# Create the matrix
H_10 = matrix_creator(matrix_element, 10)
H_100 = matrix_creator(matrix_element, 100)
# Using eigh instead of eig because eigh sorts the eigenvalues
lamda1, v1 = np.linalg.eigh(H_10)
lamda2, v2 = np.linalg.eigh(H_100)

print('The first 10 energy eigenvalues for N = 10 in eV are: ')
print(lamda1[:10])

print('The first 10 energy eigenvalues for N = 100 in eV are: ')
print(lamda2[:10])


# Defining the wavefunction
def psi_prob(x, n, v):
    sum = 0
    for idx in range(len(v)):
        sum += v[idx][n] * np.sin((idx+1) * pi * x / L)
    return np.abs(sum)**2


# Plotting the graphs
x = np.arange(0, L+0.01, 0.01)
print('It was found that the wavefunctions are not normalized.')
for idx in range(3):
    y = psi_prob(x, idx, v2)
    norm = quad_int(x, y)
    print('The norm of the normalization constant for psi_'+str(idx)+' is:', end=' ')
    print(1/norm)
    plt.plot(x, y/norm, label='$\psi_{'+str(idx)+'}$')
plt.title('$|\psi(x)|^{2}$ for n= 0, 1, 2')
plt.xlabel('x in Angstroms')
plt.ylabel('$|\psi(x)|^{2}$')
plt.legend()
plt.savefig('Q16_wavefunctions.jpg')
plt.show()

