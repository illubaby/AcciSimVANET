import matplotlib.pyplot as plt

# Specified data for 7 vehicles
data = {
    'Vehicle 1': {'x': [0, 1, 2, 3, 4,4,4,4,4], 'y': [1, 1, 1, 1, 1,0,-1,-2,-3]},
    'Vehicle 2': {'x': [1, 2, 3, 4, 5,5,5,5,5], 'y': [2, 2, 2, 2, 2,1,0,-1,-2]},
    'Vehicle 3': {'x': [2, 3, 4, 5, 6,6,6,6,6], 'y': [3,3,3,3,3,2,1,0,-1]},
    'Vehicle 4': {'x': [7,7,7,7,7,6,5,4,3,2], 'y': [1,2,3,4,5,5,5,5,5,5]},
    'Vehicle 5': {'x': [0,1,2,3,4,5,6,7], 'y': [7,7,7,7,7,7,7,7]},
    'Vehicle 6': {'x': [9,9,9,9,9,9,9,9,9,8], 'y': [-2,-1,0,1,2,3,4,5,6,7]},
    'Vehicle 7': {'x': [8,8,8,8,8,8,8,8,8,8], 'y': [-2,-1,0,1,2,3,4,5,6,7]}
}

# Plot each vehicle's trajectory
for vehicle, coords in data.items():
    plt.plot(coords['x'], coords['y'], marker='o', label=vehicle)

# Add legend, title, and axis labels
plt.legend()
plt.title('Trajectories of Multiple Vehicles')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
