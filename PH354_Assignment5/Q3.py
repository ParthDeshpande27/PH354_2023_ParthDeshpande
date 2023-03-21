# Exercise 3: Brownian motion

# ANSWERS
# Visualization becomes a bit difficult (especially for the 2D plot since every point
# has been visited) for very large N.
# It might be more enlightening to plot the graphs for smaller N (i.e., 1e4).
# The 2D plot is difficult to interpret since every point has been visited.
# The 3D plot is easier since it shows the trajectory of the particle. However,
# it is still difficult to see the particle's trajectory since the aspect is too large.
# The heatmap is a bit easier to interpret since it shows the number of visits to each point.
# The heatmap shows a uniform distribution of visits to each point, which is what we expect.

# Importing useful modules
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

L = 101             # Grid steps
steps = int(1e6)    # Number of steps to simulate
time = np.arange(steps+1)
x = L // 2          # Start position in the middle of the grid
y = L // 2
trajectory = [(x, y)]  # List to store the particle's trajectory
grid = np.zeros((L, L))  # Grid to store the number of visits to each point


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


def run(x, y, trajectory, steps):
    for i in range(steps):
        x1, y1 = stepping(x, y)
        # Check if the particle is moving out of bounds
        while out_of_bounds(x1, y1, L):
            x1, y1 = stepping(x, y)
        x, y = x1, y1
        grid[x, y] += 1
        trajectory.append((x, y))
    return trajectory


x_vals, y_vals = zip(*run(x, y, trajectory, steps))

fig0 = plt.figure(0)
plt.plot(x_vals, y_vals, marker='.', markersize=0.1)
plt.xlim(0, L-1)
plt.ylim(0, L-1)
plt.title('2D plot for Brownian motion')
plt.xlabel('X position')
plt.ylabel('Y position')
plt.tight_layout()
plt.gca().set_aspect('equal')
plt.savefig('Q3_2D.jpg')
plt.show()

fig1 = plt.figure(1)
ax = fig1.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, time, marker='.', markersize=0.1)
plt.xlim(0, L-1)
plt.ylim(0, L-1)
plt.title('3D plot for Brownian motion')
plt.xlabel('X position')
plt.ylabel('Y position')
ax.set_zlabel('Time')
ax.set_box_aspect((2, 2, 20))
plt.tight_layout()
plt.savefig('Q3_3D.jpg')
plt.show()

fig2 = plt.figure(2)
plt.imshow(grid, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap for Brownian motion')
plt.xlabel('X position')
plt.ylabel('Y position')
plt.tight_layout()
plt.savefig('Q3_heatmap.jpg')
plt.show()

# # Creating the figure and axes for the animation
# fig, ax = plt.subplots()
# ax.set_xlim(0, L-1)
# ax.set_ylim(0, L-1)
# ax.set_aspect('equal')
# ax.set_title('2D Brownian Motion animation')
# ax.set_xlabel('X position')
# ax.set_ylabel('Y position')
#
# # Creating the line object for the trajectory
# line, = ax.plot([], [], marker='.', markersize=5)
#
#
# # Defining the animation function that updates the line object at each frame
# def animate(frame):
#     line.set_data(x_vals[frame], y_vals[frame])
#     return line,
#
#
# # Creating the animation object
# anim = animation.FuncAnimation(fig, animate, frames=steps, interval=1, blit=True)
#
# # Saving the animation as a GIF file
# anim.save('Q3_2D_animation.gif', writer='pillow')
