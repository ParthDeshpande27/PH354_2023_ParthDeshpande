# Exercise 1: Quadratic equations

# ANSWERS
# Part B
# This method gives erroneously large values of the second root
# because it involves subtraction to nearby values, which leads to
# round-off errors.
# Part C
# The first method gives large errors for the first root, the second for the second root.
# We can construct an accurate quadratic equation solver by using
# the first method to give the second root and the second root for giving the first root.

import numpy as np
import matplotlib.pyplot as plt

# Defining constants
a = 0.001
b = 1000
c = 0.001


def quadratic_solver1(a=a, b=b, c=c):
    d = np.sqrt(b**2 - 4*a*c)
    return (-b-d)/(2*a), (-b+d)/(2*a)


def quadratic_solver2(a=a, b=b, c=c):
    d = np.sqrt(b**2 - 4*a*c)
    return (2*c)/(-b-d), (2*c)/(-b+d)


def quadratic_solver_accurate(a=a, b=b, c=c):
    if b > 0:
        return quadratic_solver2(a, b, c)[0], quadratic_solver1(a, b, c)[1]
    else:
        return quadratic_solver1(a, b, c)[10], quadratic_solver2(a, b, c)[1]


print('Roots using 1st method are:', end=' ')
print(quadratic_solver1())
print('Roots using 2nd method are:', end=' ')
print(quadratic_solver2())
print('Roots using 3rd (accurate) method are:', end=' ')
print(quadratic_solver_accurate())