import pandas as pd
import numpy as np
# Load the CSV file
data = pd.read_csv('data/Car Movement Data Collection.csv')

# Drop the existing 'Method' column
data = data.drop('Method', axis=1)

# Add a new 'Method' column with all values set to "Method 1"
data['Method'] = 'Method 1'
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')
linear_y = np.linspace(0,200,len(data))
data['Coordinate Y'] = linear_y
# Save the modified DataFrame to a new CSV file
data.to_csv('data/car_movement.csv', index=False)
