# Exercise 4: Fourier filtering and smoothing

# ANSWERS

# Part D
# When you set a Fourier coefficient to 0, the corresponding frequency component
# disappears from the time series data.
# If you set all Fourier components above a threshold to 0, you will smoothen data
# because you will remove the high frequency components (i.e., noise) from your data.

# Part F
# The square wave function jumps discontinuously between -1 and 1.
# The discrete fourier transform tries to approximate this using very high frequencies
# Now, these high frequencies induce unnecessary wiggles in the constant part of the graph
# (i.e., when the function is either 1 or -1 and doesn't change).
# These are offset using high frequencies that are phase shifted to cancel the wiggles.
# When we discard the high frequencies, the wiggles are not canceled anymore so we can see them.

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt

# Importing data
dow = np.loadtxt('dow.txt')

# Defining constants
percent_accepted = [100.0, 10.0, 2.0]
colors = ['black', 'c', 'red']
thicknesses = [0.8, 1.2, 1.5]
time = np.arange(0, len(dow), 1)


# Defining the smoothening function
def smoothen(data, percent):
    N = len(data)
    ck2 = np.fft.rfft(data)
    ck2_smooth = np.zeros_like(ck2)
    idx = int(N*percent/100)
    ck2_smooth[:idx] = ck2[:idx]
    return np.fft.irfft(ck2_smooth)


# Plotting the graphs
for idx, element in enumerate(percent_accepted):
    plt.plot(time, smoothen(dow, element), label='%Accepted = ' + str(element), linewidth=thicknesses[idx], color=colors[idx])
plt.grid()
plt.xlabel('Days')
plt.ylabel('Dow')
plt.legend()
plt.title('Dow Jones Industrial Average')
plt.savefig('Q4_1.jpg')
plt.show()

# Part F (Square Wave)


# Defining the function
def square_wave(t):
    return np.piecewise(t, [np.floor(2*t) % 2 == 0], [1, -1])


# Defining constants
N = 1000
x = np.linspace(0, 1 - 1/N, N)
percent_accepted = [100.0, 1.0]
square_vals = square_wave(x)

# Plotting the graphs
for idx, element in enumerate(percent_accepted):
    plt.plot(x, smoothen(square_vals, element), label='%Accepted = ' + str(element))
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Square Wave')
plt.savefig('Q4_2.jpg')
plt.show()