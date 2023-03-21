# Exercise 6: Fast Fourier Transform

# ANSWERS

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt

# Importing data
pitch = np.loadtxt('pitch.txt')
N = len(pitch)

# Defining the custom Fourier transforms

def my_fft(x):
    n = len(x)
    if n == 1 + 0j: return x
    else:
        even = my_fft(x[::2])
        odd = my_fft(x[1::2])
        twiddle = np.exp(2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + twiddle[:n//2]**(-1) * odd,
                               even + twiddle[n//2:]**(-1) * odd])


def my_ifft(x):
    n = len(x)
    if n == 1 + 0j: return x
    else:
        even = my_fft(x[::2])
        odd = my_fft(x[1::2])
        twiddle = np.exp(-2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + twiddle[:n//2]**(-1) * odd,
                               even + twiddle[n//2:]**(-1) * odd])


# Defining constants
colors = ['black', 'red']
thicknesses = [0.8, 1.2]
transforms = [np.fft.fft, my_fft]
transform_names = ['numpy FFT', 'my FFT']
time = np.arange(0, N, 1)

diff_fft = np.fft.fft(pitch) - my_fft(pitch)

plt.plot(np.real(diff_fft), label='Real part of the difference', linewidth=0.5)
plt.plot(np.imag(diff_fft), label='Imaginary part of the difference', linewidth=0.5)
plt.plot(np.abs(diff_fft), label='Absolute part of the difference', linewidth=0.5)
plt.grid()
plt.xlabel('x')
plt.ylabel('$\Delta f(x)$')
plt.legend()
plt.title('Difference in FFTs')
plt.savefig('Q6_difference.jpg')
plt.show()


# Plotting the graphs
for idx, transform in enumerate(transforms):
    ck2 = np.abs(transform(pitch))**2
    plt.plot(ck2, label=str(transform_names[idx]), linewidth=thicknesses[idx], color=colors[idx])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Pitch FFT')
    plt.savefig('Q6_' + str(idx+1) + '.jpg')
    plt.show()

