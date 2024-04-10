import csv
from VANET_framework.VehiNetTransmit import VehicleData
from typing import List, Dict
import math
from VANET_framework.Global import c
# Your VehicleData class and other functions go here
def circumcirle_radius(x,y):
    return math.sqrt(x**2+y**2)/2
def my_vehicle_accident(x,y,t):
    return x+y>t*c
def read_csv_and_create_vehicle_movements(file_path):
    vehicle_movements = []  # List to store the movement records of a single vehicle
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convert last_broadcast_time to timestamp if necessary
            vehicle_record = VehicleData(
                velocity=float(row['velocity']),
                angle=float(row['angle']),
                delta_t=float(row['delta_t']),
                Delta_t=float(row['Delta_t']),
                ID=int(row['ID']),
                last_broadcast_time=(row['last_broadcast_time']),
                dimension_x=float(row['dimension_x']),
                dimension_y=float(row['dimension_y'])
            )
            vehicle_movements.append(vehicle_record)
    return vehicle_movements
def read_data_for_multiple_vehicles(file_paths: List[str]) -> Dict[int, List[VehicleData]]:
    all_vehicle_movements = {}
    for file_path in file_paths:
        vehicle_id = int(file_path.split('_')[-1].split('.')[0])  # Extracting vehicle ID from file name
        all_vehicle_movements[vehicle_id] = read_csv_and_create_vehicle_movements(file_path)
    return all_vehicle_movements

def check_similar(x, y,tolerance):
    if (abs(x-y)<=tolerance):
        return True
    return False

def is_accident(all_vehicles_data):
    num_records = len(all_vehicles_data[1])
    for j in range(num_records):
        for i in all_vehicles_data:
            # print(f"{all_vehicles_data[i][j].ID} {all_vehicles_data[k][j].last_broadcast_time}")
            # print(1)
            for k in range(i+1,len(all_vehicles_data)+1):
                # print(f"{all_vehicles_data[i][j].ID} {all_vehicles_data[k][j].ID}")
                # print(all_vehicles_data[k][j].last_broadcast_time)
                # if other vehicle get accident
                if check_similar(all_vehicles_data[i][j].angle,all_vehicles_data[k][j].angle,1):
                    if check_similar(all_vehicles_data[i][j].delta_t,all_vehicles_data[k][j].delta_t,1):
                        print(f"Accident happen at {all_vehicles_data[i][j].last_broadcast_time}")
                        return all_vehicles_data[i][j].last_broadcast_time
    return False
    #if my vehicle accident