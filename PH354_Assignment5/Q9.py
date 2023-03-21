# Exercise 9: The dimer covering problem

# ANSWERS
# I have hidden the animation creating code because it takes a long time to run (took me about 1.5 hours).

# Importing useful modules
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from time import time

# Measuring the time taken to run the code
start_time = time()

# Defining constants
L = 50
tau = int(2.5e4)
T0 = 1
T_min = 1e-6
alpha = 0.9999


# Define the energy function
def energy(dimers):
    return -len(dimers)


# Define the move function
def move(dimers, lattice):
    dimers1 = dimers.copy()
    lattice1 = lattice.copy()

    # Randomly select a cell
    i, j = np.random.choice(L, 2)

    if lattice1[i, j] == 0:
        # If the cell is empty, try to add a dimer
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        random.shuffle(directions)

        for direction in directions:
            neighbor_i, neighbor_j = i + direction[0], j + direction[1]
            if 0 <= neighbor_i < L and 0 <= neighbor_j < L and lattice1[neighbor_i, neighbor_j] == 0:
                lattice1[i, j] = 1
                lattice1[neighbor_i, neighbor_j] = 1
                dimers1.append(((i, j), (neighbor_i, neighbor_j)))
                break

    else:
        # If the cell is occupied, remove the dimer
        for dimer in dimers1:
            if (i, j) in dimer:
                lattice1[dimer[0][0], dimer[0][1]] = 0
                lattice1[dimer[1][0], dimer[1][1]] = 0
                dimers1.remove(dimer)
                break

    return dimers1, lattice1


# Define the simulated annealing function
def simulated_annealing(T, alpha, tau):
    dimers = []
    lattice = np.zeros((L, L))
    lattice_frames = [lattice.copy()]
    old_energy = energy(dimers)
    energies = [old_energy]
    step = 0

    while T > T_min and step < tau:
        dimers1, lattice1 = move(dimers, lattice)
        new_energy = energy(dimers1)
        delta_E = new_energy - old_energy
        if delta_E < 0 or random.random() < np.exp(-delta_E / T):
            dimers, lattice = dimers1, lattice1
            old_energy = new_energy
        T = T * alpha
        step += 1
        energies.append(new_energy)
        lattice_frames.append(lattice.copy())

    return dimers, lattice, energies, lattice_frames


dimers, lattice, energies, lattice_frames = simulated_annealing(T0, alpha, tau)

# Print the number of steps taken
print("Number of steps: ", len(lattice_frames))
# Print the number of dimers
print("Number of dimers: ", len(dimers))
# Print the final energy
print("Final energy: ", energy(dimers))
# Print the fill fraction
print("Fill fraction: ", 2 * len(dimers) / (L * L))

# Plot the energy as a function of the number of steps
plt.figure()
plt.plot(energies)
plt.title("Energy as a function of the number of steps")
plt.xlabel("Number of steps")
plt.ylabel("Energy")
plt.savefig("Q9_energy.jpg")
plt.show()

# Plot the final lattice
plt.figure()
plt.imshow(lattice, cmap='gray')
plt.title("Final lattice")
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Q9_final_cover.jpg")
plt.show()

# # Plotting the lattice and saving as a GIF
# fig = plt.figure()
# plt.title('Lattice evolution')
# ims = []
# for i in range(len(lattice_frames)):
#     im = plt.imshow(lattice_frames[i], cmap='gray', animated=True)
#     ims.append([im])
# plt.colorbar()
# anim = animation.ArtistAnimation(fig, ims, interval=10, blit=True, repeat_delay=1000)
# # anim.save('Q9_lattice_evolution.gif')
# anim.save('Q9_lattice_evolution.mp4')
# plt.show()
# plt.close()

# Print the time taken to run the code
print("Time taken in seconds: ", time() - start_time)
