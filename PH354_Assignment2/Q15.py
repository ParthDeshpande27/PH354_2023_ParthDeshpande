# Exercise 15: The gamma function

# ANSWERS
# Part B and C
# The answer is given in the attached pdf. Appropriate value of c is a - 1.
# Part D
# The new expression e**( (a - 1)lnx - x) is better because we calculate the total exponent first
# and then exponentiate it instead of calculating very large and very small values and then multiplying them
# which would cause more errors.


import numpy as np
import matplotlib.pyplot as plt
from custom_functions import *
from gaussxw import *
from scipy.constants import G, pi

# Defining constants in SI units
n = 100
values = np.array([3, 6, 10])

# Part A

# Defining the integrand
def function_1(x, a):
    return np.exp((a-1)*np.log(x) - x)


f1 = plt.figure(1)
a_x = np.linspace(0,5,100)
a_a = np.array([2,3,4])
plt.title('Integrand of gamma function for gamma of (2, 3 and 4)')
plt.xlabel('x')
plt.ylabel('Integrand value')
for idx in a_a:
    plt.plot(a_x, function_1(a_x, idx))

# Part E


# Defining gamma(a)
def gamma(a):
    z, w = gaussxwab(n, 0, 1)
    return sum(w * ((a-1)/((1-z)**2)) * function_1(z*(a-1)/(1-z), a))


# Printing the results
print("Obtained gamma(3/2):", end=" ")
a1 = gamma(3.0/2.0)
print(a1)
print("Known gamma(3/2):", end=" ")
a2 = np.sqrt(np.pi)/2
print(a2)
print("Percetange error in calculated gamma(3/2):", end=" ")
print(100*(a1-a2)/a2)
print("Obtained values for gamma of %s:" % values)
for idx in values:
    print(gamma(idx))
print("Values for factorial of %s:" % (values - 1))
for idx in values:
    print(math.factorial(idx - 1))

plt.show()


