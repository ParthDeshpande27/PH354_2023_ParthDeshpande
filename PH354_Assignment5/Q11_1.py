# Centre-anchoring
# ANSWERS

# Importing useful modules
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import numpy as np
from time import time

# Timing the code
start_time = time()

# Defining constants
L = 101  # Grid shape[0] = shape[1] = L

# Checking if a particle should be anchored
def to_be_anchored(position, L, anchored_positions):
    x, y = position

    # Check if position neighbors an anchored position
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 and dy == 0) or (dx != 0 and dy != 0):
                continue
            neighbor_pos = (x + dx, y + dy)
            if neighbor_pos in anchored_positions:
                return True

    # Check if position is at the centre
    if x == L//2 and y == L//2:
        return True

    return False


# Defining function to check if particle is out of bounds
def out_of_bounds(x, y, L):
    return x < 0 or x >= L or y < 0 or y >= L


# Defining function to take the steps of the random walk
def stepping(x, y):
    # Choosing a random direction to move in
    dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    # Updating the position
    x += dx
    y += dy
    return x, y


# Defining function to generate a random position on the circle
def rand_pos(r, L):
    while True:
        theta = random.uniform(0, 2*np.pi)
        x = int(L//2 + r*np.cos(theta))
        y = int(L//2 + r*np.sin(theta))
        if np.hypot(x-L//2, y-L//2) >= r:
            break
    return x, y


def run(L):
    global trajectory
    grid = np.zeros((L, L))  # Grid to visualise the particles
    anchored = []  # List to store the anchored particles

    (x_m, y_m) = (L // 2, L // 2)   # Initial position of the particle in the middle of the grid
    trajectories = [[(x_m, y_m)]]   # Adding the trajectory to the list of trajectories
    grid[x_m, y_m] = 1              # Updating the grid
    anchored.append((x_m, y_m))     # Adding the anchored particle to the list of anchored particles

    r = 0  # Initial radius of the circle
    # Simulating for each particle till r = L//4
    while r <= L//4:
        trajectory = []  # List to store the trajectory of the particle
        while True:
            x, y = rand_pos(r+1, L)  # Random position on the circle
            trajectory.append((x, y))  # Initial position of the particle
            # Simulating for each step
            while not to_be_anchored((x, y), L, anchored):
                x1, y1 = stepping(x, y)
                # Check if the particle is moving out of bounds
                while out_of_bounds(x1, y1, L):
                    x1, y1 = stepping(x, y)
                x, y = x1, y1
                trajectory.append((x, y))
                if np.hypot(x-L//2, y-L//2) > 2*r:
                    trajectory.clear()
                    break
            if to_be_anchored((x, y), L, anchored):
                break
        # Updating the grid and the anchored particles
        grid[x, y] = 1
        anchored.append((x, y))
        trajectories.append(trajectory)
        dist_from_centre = np.hypot(x-L//2, y-L//2)
        if dist_from_centre > r:
            r = dist_from_centre
    return grid, trajectories, anchored


# Running the simulation
grid, trajectories, anchored = run(L)

# Plotting the final state of the grid
fig0 = plt.figure(0)
plt.imshow(grid, cmap='gray')
plt.title('Final state of the grid')
plt.savefig('Q11_1_centre.jpg')
plt.show()

# Plotting the final state of the grid with the most recent anchored particle being hotter

# Create a colormap that maps age to color
age_cmap = cm.get_cmap('hot', len(anchored))

# Create a copy of the grid and normalize the anchored particle indices
colored_grid = np.zeros((L, L, 3))
for i, particle in enumerate(anchored):
    colored_grid[particle] = age_cmap(i)[:3]

# Plotting the final state of the grid with the most recent anchored particle being hotter
fig2 = plt.figure(2)
plt.imshow(colored_grid, cmap='hot')
plt.title('Age-wise final grid state')
plt.colorbar()
plt.savefig('Q11_2_centre.jpg')
plt.show()

# Plotting the trajectories of the particles in 3D
fig1 = plt.figure(1)
ax = fig1.add_subplot(111, projection='3d')
for trajectory in trajectories:
    x_vals = [x for x, y in trajectory]
    y_vals = [y for x, y in trajectory]
    time_list = list(range(len(trajectory)))
    ax.plot(x_vals, y_vals, time_list, marker='.', markersize=0.1)
plt.xlim(0, L-1)
plt.ylim(0, L-1)
plt.title('3D plot for DLA trajectories')
plt.xlabel('X position')
plt.ylabel('Y position')
ax.set_zlabel('Time')
ax.set_box_aspect((2, 2, 7))
plt.tight_layout()
plt.savefig('Q11_3_centre.jpg')
plt.show()

# Printing the time taken to run the code
end_time = time()
print('Time taken to run the code: {:.2f} seconds'.format(end_time - start_time))