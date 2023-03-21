import math
import numpy as np
from gaussxw import *


def trap_int(x, y):
    n = len(x)
    if n == 0 or n == 1:
        return 0
    h = (x[1] - x[0])
    ans = (h/2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return ans


def quad_int(x, y):
    # I'm calling this method quadratic
    # even though in case n is odd, the cubic method is being used
    # (since the error bound is similar in both cases).
    n = len(x)
    if n == 0 or n == 1:
        return 0
    h = (x[1] - x[0])
    ans = 0
    if n == 2:
        return trap_int(x, y)
    if n == 3:
        return (h/3) * (y[0] + 4 * y[1] + y[2])
    if n == 4:
        return ((3*h)/8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])
    if n % 2 != 0:
        ans = (h/3) * (y[0] + 2 * sum(y[2:n-1:2]) + 4 * sum(y[1:n:2]) + y[n-1])
    if n % 2 == 0:
        ans = quad_int(x[0:n-4], y[0:n-4]) + ((3*h)/8) * (y[n-4] + 3 * y[n-3] + 3 * y[n-2] + y[n-1])
    return ans


def quad_int_func(f, a, b, n, *argv):
    x = np.linspace(a, b, n)
    y = f(x, *argv)
    return quad_int(x, y)


def trap_int_func(f, a, b, n, *argv):
    x = np.linspace(a, b, n)
    y = f(x, *argv)
    return trap_int(x, y)


def adaptive_trap_alt(f, a, b, tol):
    # Initialization
    h = (b - a) / 2
    t1 = h * (f(a) + f(b)) / 2
    t2 = h * (f(a) + 2 * f(b / 2) + f(b)) / 2
    # Recursion
    def adaptive_trap_alt_recursion(f, a, b, tol, h, t1, t2):
        c = (a + b) / 2
        h_left = (b - a) / 4
        h_right = (b - a) / 4
        t_left = (h_left / 2) * (f(a) + 2 * f(c - h_left) + f(c))
        t_right = (h_right / 2) * (f(c) + 2 * f(c + h_right) + f(b))
        t_center = t_left + t_right
        error = (t_center - t1) / 3
        if abs(error) < tol:
            return t_center + error
        else:
            return adaptive_trap_alt_recursion(f, a, c, tol / 2, h_left, t_left, t_center) \
                   + adaptive_trap_alt_recursion(f, c, b, tol / 2, h_right, t_right, t_center)
    return adaptive_trap_alt_recursion(f, a, b, tol, h, t1, t2)


def adaptive_trap(f, a, b, tol=1e-6, slices=0, sum=0, error=0):
    I1 = trap_int_func(f, a, b, 2)
    I2 = trap_int_func(f, a, b, 3)
    I2_error = abs((I2-I1)/3.0)
    if I2_error < tol:
        slices += 1
        sum += I2
        error += I2_error
    else:
        idx, left, er1 = adaptive_trap(f, a, (a+b)/2, tol/2)
        jdx, right, er2 = adaptive_trap(f, (a+b)/2, b, tol/2)
        slices = idx + jdx
        sum = left + right
        error = er1 + er2
    return slices, sum, error


def adaptive_quad(f, a, b, tol=1e-6, slices=0, sum=0, error=0):
    I1 = quad_int_func(f, a, b, 3)
    I2 = quad_int_func(f, a, b, 5)
    I2_error = abs((I2-I1)/15.0)
    if I2_error < tol:
        slices += 1
        sum += I2
        error += I2_error
    else:
        idx, left, er1 = adaptive_quad(f, a, (a+b)/2, tol/2)
        jdx, right, er2 = adaptive_quad(f, (a+b)/2, b, tol/2)
        slices = idx + jdx
        sum = left + right
        error = er1 + er2
    return slices, sum, error


def Romberg_int(f, a, b, tol, n=15, toprint=1, sigdig=6):
    # The error is O(h_n^{2n})
    # if toprint = 1, print all the estimates and the errors, the time required
    # sigdig is the number of digits after the decimal point to be printed
    # Returns integral and error
    n_tol = 0
    R = np.zeros((n, n))
    if toprint == 1:
        print('\nRomberg triangle')
    for idx in range(n):
        if idx > 1 and abs(R[idx-1][idx-1] - R[idx-1][idx-2]) < tol:
            n_tol = idx
            break
        R[idx][0] = trap_int_func(f, a, b, 2**idx + 1)
        if toprint == 1:
            print('')
            print("%.*f" % (sigdig, R[idx][0]), end=' ')
        for jdx in range(idx):
            R[idx][jdx+1] = R[idx][jdx] + (R[idx][jdx] - R[idx-1][jdx]) / (4**(jdx+1) - 1)
            if toprint == 1:
                print("%.*f" % (sigdig, R[idx][jdx+1]), end=' ')
    if toprint == 1:
        print('\n\nError estimates')
        for idx in range(n_tol):
            print('')
            for jdx in range(idx+1):
                if jdx < idx:
                    print("%.*f" % (sigdig, R[idx][jdx+1] - R[idx][jdx]), end=' ')
                else:
                    print("NaN", end=" ")
    print('\n')
    return n_tol, R[n_tol-1][n_tol-2], R[n_tol-1][n_tol-1] - R[n_tol-1][n_tol-2]


def gaussian_int(f, a, b, n):
    x, w = gaussxwab(n, a, b)
    return sum(w * f(x))


def partial_derivative(f, x, y, h):
    return (f(x+h, y) - f(x, y))/h

def gradient(grid, h):
    # Initializing the gradient ndarray
    gradient = np.zeros((2, len(grid[:, 0]), len(grid[0, :])))
    for idx in range(2):
        if idx == 1:
            grid = grid.transpose()
            gradient = gradient.swapaxes(1, 2)
        # Calculating the partial derivatives
        # At the boundaries
        gradient[idx, :, 0] = (grid[:, 1] - grid[:, 0]) / h
        gradient[idx, :, -1] = (grid[:, -1] - grid[:, -2]) / h
        # In the bulk
        for i in range(1, len(grid[0, :]) - 1):
            gradient[idx, :, i] = (grid[:, i+1] - grid[:, i-1]) / (2*h)

    return gradient.swapaxes(1, 2)