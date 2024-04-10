import json
from collections import defaultdict
import datetime

class VehicleDataManager:
    """
    A class to manage, process, and store data received from vehicles in a VANET.

    Attributes:
    -----------
    data_storage : defaultdict
        A dictionary to store data for each vehicle, keyed by vehicle ID.

    Methods:
    --------
    receive_data(json_data):
        Processes and stores the received JSON data from vehicles.
    get_data_by_id(vehicle_id):
        Retrieves data for a specific vehicle ID.
    sort_data_by_time():
        Sorts the stored data for each vehicle based on the timestamp.
    """

    def __init__(self):
        self.data_storage = defaultdict(list)

    def receive_data(self, json_data):
        """
        Processes and stores the received JSON data from a vehicle.

        Parameters:
        -----------
        json_data : str
            The JSON string containing the vehicle's data.
        """
        data = json.loads(json_data)
        vehicle_id = data['ID']
        self.data_storage[vehicle_id].append(data)

    def get_data_by_id(self, vehicle_id):
        """
        Retrieves data for a specific vehicle ID.

        Parameters:
        -----------
        vehicle_id : int
            The ID of the vehicle whose data is to be retrieved.

        Returns:
        --------
        list
            A list of data points for the specified vehicle.
        """
        return self.data_storage.get(vehicle_id, [])

    def sort_data_by_time(self):
        """
        Sorts the stored data for each vehicle based on the timestamp.
        """
        for vehicle_id in self.data_storage:
            self.data_storage[vehicle_id].sort(key=lambda x: x['time'])

# Example usage
manager = VehicleDataManager()
manager.receive_data(sample_data.to_json())  # Assuming sample_data is a VehicleData instance
manager.sort_data_by_time()

# To get data for a specific vehicle ID
vehicle_id = 1  # Example ID
print("Data for Vehicle ID", vehicle_id, ":", manager.get_data_by_id(vehicle_id))
