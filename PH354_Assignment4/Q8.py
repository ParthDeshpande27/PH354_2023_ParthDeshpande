# Exercise 8: Image deconvolution

# ANSWERS
# There are several limitations to the arbitrary deblurring of an image:
# 1. The point spread function is usually not known.
# 2. There is noise in the data.
# 3. Some wavy artifacts are introduced in the process, especially around the edges.
#    Why is this? We are introducing a cut-off epsilon value in the Fourier transform of the point spread
#    function to avoid round-off errors, i.e., there will be contributions from frequencies
#    not originally present.


# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt

# Loading the blurred image data
blurred_image = np.loadtxt('blur.txt')
K = blurred_image.shape[0]
L = blurred_image.shape[1]

# Defining constants
sigma = 25.0
epsilon = 1e-3
x = np.arange(0, L, 1)
y = np.arange(0, K, 1)
ax, ay = np.meshgrid(x, y)


# Defining the gaussian point spread function
def gaussian(x, y, sigma=sigma):
    return  np.exp(-((x) ** 2 + (y) ** 2) / (2 * sigma ** 2)).astype(float) + \
            np.exp(-((x-L) ** 2 + (y) ** 2) / (2 * sigma ** 2)).astype(float) + \
            np.exp(-((x) ** 2 + (y-K) ** 2) / (2 * sigma ** 2)).astype(float) + \
            np.exp(-((x-L) ** 2 + (y-K) ** 2) / (2 * sigma ** 2)).astype(float)


# Plotting the blurred image
plt.imshow(blurred_image, cmap='gray')
plt.title('The blurred image')
plt.savefig('Q8_1.jpg')
plt.show()

# Plotting the spread function
point_spread_val = gaussian(ax, ay)
plt.imshow(point_spread_val, cmap='gray')
plt.title('The point spread function')
plt.savefig('Q8_2.jpg')
plt.show()

# Unblurring the image
point_spread_fft = np.fft.rfft2(point_spread_val)
point_spread_fft[np.abs(point_spread_fft) < epsilon] = epsilon
blurred_image_fft = np.fft.rfft2(blurred_image)
unblurred_image_fft = blurred_image_fft / point_spread_fft
unblurred_image = np.fft.irfft2(unblurred_image_fft)

# Plotting the unblurred image
plt.imshow(unblurred_image, cmap='gray')
plt.title('The unblurred image')
plt.savefig('Q8_3.jpg')
plt.show()
