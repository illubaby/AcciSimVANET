import matplotlib.pyplot as plt

# Example data for point A
x_A = [0, 1, 2, 3, 3]
y_A = [0, 0, 0, -0.2, -0.6]

# Example data for point B
x_B = [4, 4, 4, 2]
y_B = [-0.4, -0.2, 0.1, 0.1]

# Plotting the trajectory for point A
plt.plot(x_A, y_A, marker='o', color='blue', label='Trajectory of A')

# Plotting the trajectory for point B
plt.plot(x_B, y_B, marker='o', color='orange', label='Trajectory of B')

# Adding the legend
plt.legend()

# Adding title
plt.title('Trajectories of Points A and B')

# Labeling the axes
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Display the plot
plt.show()
