# Exercise 15: The QR algorithm

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Part A
A = np.array([[1, 4, 8, 4],
              [4, 2, 3, 7],
              [8, 3, 6, 9],
              [4, 7, 9, 2]]).astype(float)

Q, R = qr_householder(A)
print('Matrix Q:')
print(Q)
print('Matrix R:')
print(R)
print('Matrix QR:')
print(Q @ R)

# Part B
eigvalues, eigvectors = eigsys_qr(A, qr_householder)
print('The eigenvalues of A are:')
print(eigvalues)