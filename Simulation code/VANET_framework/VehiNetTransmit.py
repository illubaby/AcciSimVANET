import json
import time
class VehicleData:
    """
    A class to represent the data associated with a vehicle in a VANET.

    Attributes:
    -----------
    velocity : float
        The current speed of the vehicle (in km/h).
    angle : float
        The angle of movement of the vehicle in degrees.
    delta_t : float
        The time elapsed since the last broadcast of data (in seconds).
    Delta_t : float
        The regular interval at which the vehicle broadcasts its data (in seconds).
    last_broadcast_time : float
        The timestamp of the last data broadcast (internal use).
    ID : int
        The unique identifier of the vehicle.
    dimension_x : float
        The width of the vehicle (in meters).
    dimension_y : float
        The length of the vehicle (in meters).
    position_x : float
        The x-coordinate of the vehicle's position (in meters).
    position_y : float
        The y-coordinate of the vehicle's position (in meters).

    Methods:
    --------
    broadcast_data():
        Calculates the time elapsed since the last broadcast and prepares the data packet for transmission.
    to_json():
        Converts the vehicle data to a JSON string format for transmission.
    """

    def __init__(self, velocity, angle,delta_t, Delta_t,ID,last_broadcast_time,dimension_x,dimension_y):
        self.velocity = velocity                                    # Velocity of the Vehicle
        self.angle = angle                                          # Angle of Movement
        self.delta_t = delta_t                                      # Time Elapsed Since Last Broadcast
        self.Delta_t = Delta_t                                      # Broadcast Cycle Time
        self.last_broadcast_time  = last_broadcast_time             # Initialize last broadcast time
        self.ID = ID                                                # ID of that vehicle
        self.dimension_x = dimension_x                              # distance across the widest part of the car, usually including the side mirrors.
        self.dimension_y = dimension_y                              # the mesurement from the frontmost point of the car to the rearmost point
    def broadcast_data(self):
        """
        Calculates the time elapsed since the last broadcast (delta_t) and updates the last broadcast time.
        Returns the data packet with updated information.

        Returns:
        --------
        dict
            A dictionary containing the vehicle's current data.
        """
        current_time = time.time()
        delta_t = current_time - self.last_broadcast_time
        self.last_broadcast_time = current_time
        return {
            'velocity': self.velocity,
            'angle': self.angle,
            'delta_t': delta_t,
            'Delta_t': self.Delta_t,
            'ID': self.ID,
            'last_broadcast_time' : self.last_broadcast_time,
            'dimension_x': self.dimension_x, 
            'dimension_y': self.dimension_y            
        }

    def to_json(self):
        """
        Converts the vehicle data attributes to a JSON string.

        Returns:
        --------
        str
            JSON string representation of the vehicle data.
        """
        return json.dumps(self.__dict__)

def transmit_data(vehicle_data):
    """
    Simulates the transmission of vehicle data. This function can be expanded to include actual data transmission logic.

    Parameters:
    -----------
    vehicle_data : VehicleData
        The vehicle data to be transmitted.
    """
    print("Transmitting data:", vehicle_data.to_json())
# Example usage
vehicle1 = VehicleData(velocity=60, angle=30, delta_t=1, Delta_t=5, ID=1, 
                       last_broadcast_time=time.time(), dimension_x=2, dimension_y=4)
vehicle2 = VehicleData(velocity=50, angle=45, delta_t=1, Delta_t=5, ID=2, 
                       last_broadcast_time=time.time(), dimension_x=2, dimension_y=4)
