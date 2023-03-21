# Exercise 3: Fourier transforms of musical instruments

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ANSWERS

# Part A
# From the waveforms,
# the piano reaches a higher intensity for a brief time.
# The trumpet reaches a lower intensity but is sustained for a longer period.
# From the power spectrum,
# The piano has lower harmonic content (i.e., the number and
# relative intensity of the upper harmonics present in the sound.)
# The trumpet has higher harmonic content (in fact, the highest contribution is from
# the first harmonic).

# Part B
# Middle C is 261 Hz, the lowest frequency peak is about 520 Hz in the power spectra.
# i.e., the note played is C5 (an octave above middle C)


# Loading the data
piano = np.loadtxt('piano.txt')
trumpet = np.loadtxt('trumpet.txt')
data = [piano, trumpet]
instrument_names = ['Piano', 'Trumpet']
thresholds = [0.8e13, 4e13]
N_cutoff = 10000

for jdx, instrument in enumerate(data):

    # Defining constants
    N = len(instrument)
    sampling_freq = 44100
    time_res = 1 / sampling_freq
    print('The frequency resolution in Hz is %f' % (sampling_freq/N))
    time = np.arange(0, N * time_res, time_res)

    # Forming the value arrays
    ck2 = np.abs(np.fft.rfft(instrument))**2
    freqs = np.fft.rfftfreq(N, time_res)
    values = [[time, instrument], [freqs[:N_cutoff], ck2[:N_cutoff]]]
    function_names = [['Time series', 'Time in seconds', 'Amplitude'],
                      ['Power spectrum', 'Frequency in Hz', '$|c_{k}|^{2}$']]
    # Print the peaks
    print('The peaks in Hz for ' + str(instrument_names[jdx]) + ' are:')
    peaks = signal.find_peaks(ck2[10:N_cutoff], distance=100, threshold=thresholds[jdx])[0]
    print(freqs[peaks])

    # Plotting
    for idx, element in enumerate(values):
        plt.plot(element[0], element[1])
        plt.title(str(function_names[idx][0]) + ' for ' + str(instrument_names[jdx]))
        plt.xlabel(function_names[idx][1])
        plt.ylabel(function_names[idx][2])
        plt.grid()
        plt.savefig('Q3_' + str(jdx+1) + '_' + str(idx+1) + '.jpg')
        plt.show()
        plt.close()