import matplotlib.pyplot as plt
import numpy as np

def calculate_new_position(x0, y0, v, phi, delta_t):
    phi_radians = np.radians(phi)
    delta_x = v * np.cos(phi_radians) * delta_t
    delta_y = v * np.sin(phi_radians) * delta_t
    return x0 + delta_x, y0 + delta_y

# Function to generate random movement data
def generate_random_data(n):
    velocities = np.random.uniform(0.5, 2, n)  # Random velocities between 0.5 and 2
    angles = np.random.uniform(-90, 90, n)     # Random angles between -90 and 90 degrees
    times = np.random.uniform(0.5, 2, n)       # Random times between 0.5 and 2
    return list(zip(velocities, angles, times))

# Number of movements
n = 5  # For example, 5 movements

# Generate random movement data for A and B
data_A = generate_random_data(n)
data_B = generate_random_data(n)

# Initial positions of A and B
A_position = (0, 0)
B_position = (4, 0)

# Lists to store the trajectories
trajectory_A_x = [A_position[0]]
trajectory_A_y = [A_position[1]]
trajectory_B_x = [B_position[0]]
trajectory_B_y = [B_position[1]]

# Update positions and record trajectories
for (v_A, phi_A, delta_t_A), (v_B, phi_B, delta_t_B) in zip(data_A, data_B):
    A_position = calculate_new_position(*A_position, v_A, phi_A, delta_t_A)
    B_position = calculate_new_position(*B_position, v_B, phi_B, delta_t_B)
    trajectory_A_x.append(A_position[0])
    trajectory_A_y.append(A_position[1])
    trajectory_B_x.append(B_position[0])
    trajectory_B_y.append(B_position[1])

# Plotting
plt.figure()
plt.plot(trajectory_A_x, trajectory_A_y, '-o', label='Trajectory of A')
plt.plot(trajectory_B_x, trajectory_B_y, '-o', label='Trajectory of B')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Trajectories of Points A and B')
plt.legend()
plt.grid(True)
plt.show()
