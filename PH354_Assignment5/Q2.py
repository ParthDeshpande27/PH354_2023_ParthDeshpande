# Exercise 2: Radioactive decay chain

# Importing useful modules
import random
import matplotlib.pyplot as plt
import numpy as np

# Initialising the number of atoms for each isotope
num_213Bi = 10000
num_209Pb = 0
num_209Tl = 0
num_209Bi = 0

# Defining the time step and total time for the simulation
dt = 1
total_time = 20000


# Defining a function that calculates decay probabilities
def decay_prob(t, hl):
    return 1 - 2 ** (-t / hl)


# Half-lives and 1s decay probabilities
hl_213Bi = 46 * 60
hl_209Pb = 3.3 * 60
hl_209Tl = 2.2 * 60
p_213Bi = decay_prob(1, hl_213Bi)
p_213Bi_to_209Pb = 0.9791
p_213Bi_to_209Tl = 0.0209
p_209Pb_to_209Bi = decay_prob(1, hl_209Pb)
p_209Tl_to_209Pb = decay_prob(1, hl_209Tl)

# Lists to store the number of atoms of each isotope at each time step
time = [0]
num_213Bi_list = [num_213Bi]
num_209Pb_list = [num_209Pb]
num_209Tl_list = [num_209Tl]
num_209Bi_list = [num_209Bi]

# Simulation loop
for t in range(dt, total_time+dt, dt):

    # Decay of 209Pb
    num_209Pb_decayed = 0
    for i in range(num_209Pb):
        if random.random() < p_209Pb_to_209Bi:
            num_209Pb_decayed += 1
    num_209Pb -= num_209Pb_decayed
    num_209Bi += num_209Pb_decayed

    # Decay of 209Tl
    num_209Tl_decayed = 0
    for i in range(num_209Tl):
        if random.random() < p_209Tl_to_209Pb:
            num_209Tl_decayed += 1
    num_209Tl -= num_209Tl_decayed
    num_209Pb += num_209Tl_decayed

    # Decay of 213Bi
    num_213Bi_decayed_to_209Pb = 0
    num_213Bi_decayed_to_209Tl = 0
    for i in range(num_213Bi):
        if random.random() < p_213Bi:
            if random.random() < p_213Bi_to_209Pb:
                num_213Bi_decayed_to_209Pb += 1
            else:
                num_213Bi_decayed_to_209Tl += 1
    num_209Tl += num_213Bi_decayed_to_209Tl
    num_209Pb += num_213Bi_decayed_to_209Pb
    num_213Bi -= (num_213Bi_decayed_to_209Pb + num_213Bi_decayed_to_209Tl)

    # Updating the number of atoms for each isotope
    time.append(t)
    num_213Bi_list.append(num_213Bi)
    num_209Pb_list.append(num_209Pb)
    num_209Tl_list.append(num_209Tl)
    num_209Bi_list.append(num_209Bi)

atom_list = [num_213Bi_list, num_209Pb_list, num_209Tl_list, num_209Bi_list]
graphs = plt.loglog(time, list(np.array(atom_list).T))
plt.title('Bi-213 Decay chain time series')
plt.xlabel('Time in seconds')
plt.ylabel('Number of atoms of the isotope')
plt.grid()
plt.legend(graphs, ('Bi_213', 'Pb_209', 'Tl_209', 'Bi_209'))
plt.savefig('Q2.jpg')
plt.show()
