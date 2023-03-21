# Exercise 2: Detecting periodicity

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt

# ANSWERS
# Part A
# From the time series graph, we may estimate the time period to be about 140 months i.e., 11.666 years.
# Part B
# From the power spectrum, the non-zero peak was obtained at f = 0.0076360 per month i.e., the time period of
# the corresponding sine wave is about 131 months or 10.9 years.

# Loading the data
data = np.loadtxt('sunspots.txt')
time = data[:, 0]
spots = data[:, 1]
N = len(time)

# Forming the value arrays
ck2 = np.abs(np.fft.fft(spots))**2
freqs = np.fft.fftfreq(N)
idx1 = np.argmin(np.abs(freqs - 0.005))
idx2 = np.argmin(np.abs(freqs - 0.011))
values = [[time, spots], [freqs[idx1:idx2], ck2[idx1:idx2]]]
function_names = [['Time series', 'Month', 'Number of sunspots'],
                  ['Power spectrum', 'Frequency in month$^{-1}$', '$|c_{k}|^{2}$']]

for idx, element in enumerate(values):
    plt.plot(element[0], element[1])
    plt.title(function_names[idx][0])
    plt.xlabel(function_names[idx][1])
    plt.ylabel(function_names[idx][2])
    plt.grid()
    plt.savefig('Q2_' + str(idx+1) + '.jpg')
    plt.show()
    plt.close()