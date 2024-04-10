import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data/car_1.csv')

# Convert 'Time' to a datetime object if it's not already
data['Time'] = pd.to_datetime(data['Time'])

plt.figure(figsize=(10, 5))
plt.scatter(data['Coordinate X'], data['Coordinate Y'])
plt.xlabel('Coordinate X')
plt.ylabel('Coordinate Y')
plt.title('Scatter Plot of Coordinates')
plt.show()

