# Defining custom functions used frequently

import numpy as np
import warnings

# Defining constants
max_iter = 50
h_derivative = 1e-8


def fpi(f, tol, toprint, argv, max_iter=100):
    step = 0
    while True:
        if step > max_iter:
            raise RuntimeError('Did not converge')
        if toprint:
            print(step, argv)
        argv1 = f(argv)
        step += 1
        if np.all(np.abs(np.subtract(argv1, argv)) < tol):
            if toprint:
                print(step, argv1)
            break
        argv = argv1
    return np.array([step, argv1])


def aux_acc_fpi(argv, argv1, argv2):
    argv3 = np.copy(argv).astype(dtype=float)
    for idx in range(len(argv)):
        numerator = (argv1[idx] - argv[idx])**2
        denominator = argv2[idx] - 2*argv1[idx] + argv[idx]
        if denominator == 0:
            argv3[idx] = argv2[idx]
            continue
        argv3[idx] = argv[idx] - numerator/denominator
    return argv3


def acc_fpi(f, tol, toprint, argv, max_iter=100):
    step = 0
    while True:
        if step > max_iter:
            raise RuntimeError('Did not converge')
        if toprint:
            print(step, argv)
        argv1 = f(argv)
        argv2 = f(argv1)
        argv3 = aux_acc_fpi(argv, argv1, argv2)
        step += 1
        if np.all(np.abs(np.subtract(argv3, argv)) < tol):
            if toprint:
                print(step, argv3)
            break
        argv = argv3
    return np.array([step, argv3])


def binary_search(f, tol, bounds, *argv):
    a, b = bounds[0], bounds[1]
    if f(a, *argv) == 0: return a
    elif f(b, *argv) == 0: return b
    elif f(b, *argv) * f(a, *argv) > 0:
        raise Exception('The bounds may not bracket a root.')
    while (b - a) / 2 >= tol:
        c = (a + b) / 2
        if f(c, *argv) == 0:
            return c
        elif f(c, *argv) * f(a, *argv) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def false_position(f, tol, bounds, *argv):
    a, b = bounds[0], bounds[1]
    fa = f(a, *argv)
    fb = f(b, *argv)
    if fa == 0: return a
    elif fb == 0: return b
    elif fa * fb > 0:
        raise Exception('The bounds may not bracket a root.')
    c = (a*f(b, *argv) - b*f(a, *argv))/(f(b, *argv)-f(a, *argv))
    while np.abs(f(c, *argv)) >= tol:
        c = (a*f(b, *argv) - b*f(a, *argv))/(f(b, *argv)-f(a, *argv))
        if f(a, *argv) * f(c, *argv) < 0:
            b = c
        else:
            a = c
    return c


def derivative(f, x, h=h_derivative, *argv):
    derivative = (f(x + h, *argv) - f(x - h, *argv)) / (2*h)
    return derivative


def newton(f, x0, tol, h=h_derivative, *argv):
    x1 = x0 + tol*10
    while np.abs(x1 - x0) >= tol:
        x1 = x0 - f(x0, *argv) / derivative(f, x0, h, *argv)
        x0 = x1
    return x1


def secant(f, x0, tol, *argv):
    x = x0[0] + tol*2
    while np.abs(x - x0[0]) >= tol:
        # Basically an unbracketed false position method
        x = (x0[0] * f(x0[1], *argv) - x0[1] * f(x0[0], *argv)) / (f(x0[1], *argv) - f(x0[0], *argv))
        x0[0] = x0[1]
        x0[1] = x
    return x


def nd_newton(f, jacobian, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        deltax = np.linalg.solve(jacobian(x0), -f(x0))
        x1 = x0 + deltax
        if np.linalg.norm(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0


def Gaussian_elimination(A, v):
    #return np.linalg.solve(A, v)
    N = len(v)
    for m in range(N):
        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div
        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]
    # Backsubstitution
    x = np.empty(N, float)
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i] * x[i]
    return x


def Gaussian_elimination_pp(A, v):

    # Create a copy of A and v to avoid modifying the original input
    A = A.copy()
    v = v.copy()
    N = len(v)

    # Iterate over all the rows
    for m in range(N):
        # Find the row with the largest absolute value in the mth column
        max = m
        for jdx in range(m + 1, N):
            if abs(A[jdx, m]) > abs(A[max, m]):
                max = jdx

        # Exchange the mth row with this row
        if max != m:
            A[[m, max]] = A[[max, m]]
            v[[m, max]] = v[[max, m]]

        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Backsubstitution
    x = np.empty(N, float)
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i] * x[i]
    return x


def Gaussian_elimination_banded_pp(A, v, bandwidth):
    # Bandwidth is the number of non-zero elements above OR below the diagonal
    # Create a copy of A and v to avoid modifying the original input
    A = A.copy()
    v = v.copy()
    N = len(v)

    # Gaussian elimination
    for idx in range(N):
        for jdx in range(idx+1, min(idx+bandwidth+1, N)):
            mul = A[jdx][idx] / A[idx][idx]
            for kdx in range(idx+1, min(idx+bandwidth+1, N)):
                A[jdx][kdx] -= mul * A[idx][kdx]
            v[jdx] -= mul * v[idx]

    x = np.zeros(N, float)
    for idx in range(N - 1, -1, -1):
        x[idx] = v[idx] / A[idx][idx]
        sum = 0
        for jdx in range(idx+1, min(idx+bandwidth+1, N)):
            sum += A[idx][jdx] * x[jdx]
        x[idx] -= sum / A[idx][idx]

    return x


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


def qr_householder(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    #Iterating over all the rows
    for idx in range(n):

        #Calculating the Householder reflection vector
        x = R[idx:, idx]
        v = np.zeros_like(x)
        v[0] = np.sign(x[0])*np.linalg.norm(x)
        v += x 
        v /= np.linalg.norm(v)

        # Forming Q_idx
        Q_idx = np.eye(m)
        Q_idx[idx:, idx:] -= 2.0 * np.outer(v, v)

        # Application of Q_idx on R_idx forms R_idx+1 (i.e., a step forward)
        R = Q_idx @ R
        # Q = I @ Q_1 @ Q_2 .... @ Q_n
        Q = Q @ Q_idx

    return Q, R


def eigsys_qr(A, qr, tol=1e-6):
    A = np.copy(A)
    n = A.shape[0]
    eigvectors = np.eye(n)
    while True:
        Q, R = qr(A)
        A = R @ Q
        eigvectors = eigvectors @ Q
        # np.triu(A, k=1) returns a copy matrix with all values on and
        # below the diagonal 0
        if np.max(np.abs(np.triu(A, k=1))) < tol:
            break
    eigvalues = np.diag(A)
    return eigvalues, eigvectors

