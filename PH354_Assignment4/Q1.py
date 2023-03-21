# Exercise 1: Fourier transforms of simple functions

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt

# Defining constants
N = 1000
n = np.linspace(0, 1, N)


# Defining the functions
def square(x):
    return np.piecewise(x, [x < (x[-1] - x[0])/2, x >= (x[-1] - x[0])/2], [0, 1]).astype(float)


def modulated(x):
    return np.sin(np.pi * x) * np.sin(20 * np.pi * x)


# Forming the value arrays
values = [square(n), n, modulated(n)]
function_names = ['Square', 'Sawtooth', 'Modulated Sine']

for idx, element in enumerate(values):
    plt.plot(n, element)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.title(function_names[idx])
    plt.grid()
    plt.savefig('Q1_' + str(idx+1) + '.jpg')
    plt.show()

# Forming the FFT value arrays
values_fft = np.abs(np.fft.fft(values))
function_names = ['Square FFT', 'Sawtooth FFT', 'Modulated Sine FFT']


for idx, element in enumerate(values_fft):
    N = len(element)
    plt.plot(n[:N//2], element[:N//2])
    plt.xlabel('$Frequency$')
    plt.ylabel('$|c_{k}|$')
    plt.title(function_names[idx])
    plt.grid()
    plt.savefig('Q1_fft_' + str(idx+1) + '.jpg')
    plt.show()
