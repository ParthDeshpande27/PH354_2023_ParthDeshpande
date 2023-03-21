# Exercise 4: Glycolysis

# ANSWERS

import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *

# Defining constants
a = 1
b = 2
tol = 1e-8
x0 = 1
y0 = 1


def f_b(argv):
    x = argv[0]
    y = argv[1]
    a = argv[2]
    b = argv[3]
    return np.array([y*(a + x**2), b/(a + x**2), a, b])


def f_c(argv):
    x = argv[0]
    y = argv[1]
    a = argv[2]
    b = argv[3]
    return np.array([np.sqrt(b/y - a), x/(a + x**2), a, b])


# print('Solution using accelerated FPI for equations in Part B:')
# print(acc_fpi(f_b, tol, False, [x0, y0, a, b]))
print('Solution using accelerated FPI for equations in Part C with'
      '\nnumber of steps, x, y, a, b:')
print(acc_fpi(f_c, tol, False, [x0, y0, a, b]))

