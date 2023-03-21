# Exercise 7: The Ising model

# ANSWERS
# The energy minimum is not quite at -400 since I'm not considering the periodic boundary conditions.
# The magnetization can go to +/- 400 as expected, which is the maximum possible value.

# Importing useful modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

# Measuring the time taken to run the code
start_time = time()

# Defining constants
K = 20
L = 20
J = -1
k_B = 1
T = [1, 2, 3]
# T = [1]*80
N = int(1e6)


# Defining a function that returns the element at the given index of the array, or 0 if index is out of bounds.
def get_value(arr, indices):
    for i, index in enumerate(indices):
        if index < 0 or index >= arr.shape[i]:
            return 0
    return arr[tuple(indices)]


# Defining a function that calculates the energy of a spin configuration
def calculate_energy(spins, J):
    # Use np.roll to get the contributions of the nearest neighbors in each direction
    left = np.roll(spins, 1, axis=1)
    left[:, 0] = 0
    right = np.roll(spins, -1, axis=1)
    right[:, -1] = 0
    up = np.roll(spins, 1, axis=0)
    up[0, :] = 0
    down = np.roll(spins, -1, axis=0)
    down[-1, :] = 0
    # Calculate the energy contributions from the nearest neighbors
    energy = -J * np.sum(spins * (left + right + up + down)) / 2
    return energy


# Implementing the Metropolis algorithm for Markov chain Monte Carlo simulation
def metropolis(spins, J, temperature, n_steps):
    rows, cols = spins.shape
    energy = calculate_energy(spins, J)
    magnetization = np.sum(spins)
    spins_vid = []
    energies = []
    magnetizations = []
    for step in range(n_steps):

        # Choose a random spin to flip
        i = np.random.randint(0, rows)
        j = np.random.randint(0, cols)
        spin = spins[i][j]

        # Calculate the energy difference if this spin is flipped
        delta_E = -J * spin * (get_value(spins, (i+1, j)) + get_value(spins, (i-1, j)) + get_value(spins, (i, j+1)) + get_value(spins, (i, j-1)))

        # Apply Metropolis acceptance rule
        if delta_E < 0 or np.random.uniform() < np.exp(-delta_E/(k_B * temperature)):
            spin *= -1
            energy += delta_E
            magnetization += 2 * spin

        # Add the new spin configuration to the array
        spins[i][j] = spin

        energies.append(energy)
        magnetizations.append(magnetization)
        spins_vid.append(spins.copy())
    return spins, spins_vid, energies, magnetizations

# # Positive magnetization count
# pos_magnetization_count = 0

for idx, element in enumerate(T):

    # Initialising the spin configuration
    spins = np.random.choice([-1, 1], size=(K, L))

    # Running the simulation
    spins, spins_vid, energies, magnetizations = metropolis(spins, J, element, N)

    # Plotting the magnetization
    plt.plot(magnetizations)
    plt.title('Magnetization for T = ' + str(element))
    plt.xlabel('Time in steps')
    plt.ylabel('Magnetization')
    # plt.xscale('log')
    plt.savefig('Q7_T=' + str(element) + '_magnetization.jpg')
    plt.show()
    plt.close()
    # if magnetizations[-1] > 0:
    #     pos_magnetization_count += 1


    # Plotting the energy
    plt.plot(energies)
    plt.title('Energy for T = ' + str(element))
    plt.xlabel('Time in steps')
    plt.ylabel('Energy')
    # plt.xscale('log')
    plt.savefig('Q7_T=' + str(element) + '_energy.jpg')
    plt.show()
    plt.close()

    # Plotting the final spin configuration
    plt.imshow(spins, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Final spin configuration for T = ' + str(element))
    plt.savefig('Q7_T=' + str(element) + '_spins_final.jpg')
    plt.show()
    plt.close()

    # # Plotting the spin configuration evolution and saving as a GIF
    # fig = plt.figure()
    # plt.title('Spin configuration evolution for T = ' + str(element))
    # plt.xlabel('x')
    # ims = []
    # for i in range(len(spins_vid)):
    #     im = plt.imshow(spins_vid[i], cmap='gray', animated=True)
    #     ims.append([im])
    # plt.colorbar()
    # anim = animation.ArtistAnimation(fig, ims, interval=20, blit=True, repeat_delay=1000)
    # anim.save('Q7_T=' + str(element) + '_spins_evolution.gif')
    # anim.save('Q7_T=' + str(element) + '_spins_evolution.mp4')
    # # plt.show()
    # plt.close()

# Printing the time taken to run the code
print('Time taken to run the code: ' + str(time() - start_time) + ' seconds')
# Printing the number of positive magnetization values
print('Number of positive magnetization values: ' + str(pos_magnetization_count))
