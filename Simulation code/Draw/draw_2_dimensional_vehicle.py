# Adjusting the code to add names for the vectors v1 and v2 and label the edges of the rectangles
import matplotlib.pyplot as plt
# Create a new figure and axis
fig, ax = plt.subplots()

# Define the dimensions and positions of the rectangles (cars)
x1, y1, width1, height1 = 0.1, 0.1, 0.2, 0.5  # Car 1 dimensions
x2, y2, width2, height2 = 0.4, 0.4, 0.3, 0.3  # Car 2 dimensions

# Draw the rectangles
car1 = plt.Rectangle((x1, y1), width1, height1, fill=None, edgecolor='blue', linewidth=2)
car2 = plt.Rectangle((x2, y2), width2, height2, fill=None, edgecolor='green', linewidth=2)

# Add the rectangles (cars) to the plot
ax.add_patch(car1)
ax.add_patch(car2)

# Define and draw the velocity vectors for each car
v1 = [0.2, 0.2]  # Velocity vector for Car 1
v2 = [0.15, -0.15]  # Velocity vector for Car 2
v1_arrow = ax.quiver(x1 + width1/2, y1 + height1/2, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red')
v2_arrow = ax.quiver(x2 + width2/2, y2 + height2/2, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red')

# Label the vectors
ax.text(x1 + width1/2 + v1[0], y1 + height1/2 + v1[1], 'v1', color='red')
ax.text(x2 + width2/2 + v2[0], y2 + height2/2 + v2[1], 'v2', color='red')

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Add labels for dimensions
ax.text(x1 + width1/2, y1 - 0.1, f'x1={x1}, y1={y1}', ha='center')
ax.text(x2 + width2/2, y2 - 0.1, f'x2={x2}, y2={y2}', ha='center')

# Label the edges of the rectangles
ax.annotate(f'{width1}', (x1 + width1/2, y1), textcoords="offset points", xytext=(0, -15), ha='center')
ax.annotate(f'{height1}', (x1, y1 + height1/2), textcoords="offset points", xytext=(-30, 0), va='center')
ax.annotate(f'{width2}', (x2 + width2/2, y2), textcoords="offset points", xytext=(0, -15), ha='center')
ax.annotate(f'{height2}', (x2, y2 + height2/2), textcoords="offset points", xytext=(-30, 0), va='center')

# Display the plot
plt.show()
