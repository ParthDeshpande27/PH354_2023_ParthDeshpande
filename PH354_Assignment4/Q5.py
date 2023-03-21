# Exercise 5: Comparison of the DFT and DCT

# ANSWERS

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt
from dcst import dct, idct

# Importing data
dow = np.loadtxt('dow2.txt')

# Defining constants
percent_accepted = [100.0, 2.0]
colors = ['black', 'red']
thicknesses = [0.8, 1.2]
transforms = [[np.fft.rfft, np.fft.irfft], [dct, idct]]
transform_names = ['DFT', 'DCT']
time = np.arange(0, len(dow), 1)


# Defining the smoothening function
def smoothen(data, percent, ft, ift):
    N = len(data)
    ck2 = ft(data)
    ck2_smooth = np.zeros_like(ck2)
    idx = int(N*percent/100)
    ck2_smooth[:idx] = ck2[:idx]
    return ift(ck2_smooth)


# Plotting the graphs
for jdx, transform in enumerate(transforms):
    for idx, percent in enumerate(percent_accepted):
        plt.plot(time, smoothen(dow, percent*(1+jdx), transform[0], transform[1]), label='%Accepted = ' + str(percent), linewidth=thicknesses[idx], color=colors[idx])
    plt.grid()
    plt.xlabel('Days')
    plt.ylabel('Dow')
    plt.legend()
    plt.title('Dow Jones Industrial Average using ' + str(transform_names[jdx]))
    plt.savefig('Q5_' + str(jdx+1) + '.jpg')
    plt.show()