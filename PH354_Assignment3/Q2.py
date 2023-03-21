# Exercise 2: Calculating derivatives

# ANSWERS

# Part A
# The true analytical value does not match with the calculated numerical value
# because we would have to take arbitrarily small step size delta (which we are not taking)
# Instead, we approximate the true derivative by taking the slope of a secant.

# Part B
# Initially, the error decreases because the approximation error
# (which goes as O(delta) for forward differences) decreases.
# However, after some point, the round-off error
# (which goes as O(1/delta)) begins building up (after delta = 1e-8, which matches with
# theoretical expectations).


import numpy as np
import matplotlib.pyplot as plt

# Defining constants
delta = 10.0 ** (-np.arange(2, 16, 2))


def f(x):
    return x*(x-1)


def dfdx(f, x, delta):
    return (f(x+delta) - f(x))/delta


print('True value of the derivative of f(x) = x(x-1) at x=1:', end=' ')
print(1)
print('Numerical derivatives:', end=' ')
derivatives = dfdx(f, 1, delta[:])
print(derivatives)

f1 = plt.figure(1)
plt.title('Relative error in the numerical derivative for different $\delta$')
plt.xlabel('$\delta$')
plt.ylabel('Relative error in the numerical derivative')
plt.loglog(delta, abs((derivatives-1)))
plt.savefig('Q2_1.jpg')
plt.show()

