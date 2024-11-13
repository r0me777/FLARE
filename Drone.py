import time
from math import sqrt
import random

class Drone:
    def __init__(self, drone_id, start_x=0, start_y=0, start_z=0):
        """

        This class is centered around the drone
        This will be controlling the drones:
            Flight operations
                - Controls are only really centered around propeller speed
                - Depending on the scenario -> Direction
                - Drone's move omnidirectionally
                    -- To simplfy it lets say that drone A needed to go to location 1
                    -- I would know that okay simple move in that direction but how would
                    -- a machine know? Well space is in 3 dimensions and have the dimensions
                    -- of points. on a 2D plan if you are at point (3,4) and you move
                    -- to point (4,5) you got not only go higher but also go to the right.
                    -- Code operations to go right, left etc.. and then maybe call the operations
                    -- to go right 1 and up 1 at the same time.
                    -- Then do that for 3D spaces.

            Ensuring Data Collection
                - Data Collections comes from 2 (so far) places,
                -- INTERNAL --
                - Position
                --EXTERNAL--
                - Camera Data
            Communication between Ground Station
                - Drone will relay position every 0.5 seconds
                - Drone will relay camera data every 0.5 seconds
            Communication between
                - Drones? (onboard adjustments)

        In total:
            This class is centered around the drone.
            It controls the drone's:
                - Flight operations
                - Data collection (internal/external)
                - Communication with ground station // late stage ignore for now
                - Optional inter-drone communication
        """

        self.id = drone_id
        self.x = start_x
        self.y = start_y
        self.z = start_z  # for 3D space not needed right now
        self.speed = random.uniform(1, 5)
        self.data_frequency = 0.5  # seconds for data relay
        self.internal_data = []
        self.external_data = []

    def calculate_distance(self, target_x, target_y, target_z=0):
        """
        Calculate the Euclidean distance to the target position.
        """
        return sqrt((self.x - target_x)**2 + (self.y - target_y)**2 + (self.z - target_z)**2)

    def move_towards(self, target_x, target_y, target_z=0):
        """
        Move towards a specified target in 3D space, with omnidirectional control.
        """
        dx = target_x - self.x
        dy = target_y - self.y
        dz = target_z - self.z
        distance = self.calculate_distance(target_x, target_y, target_z)

        if distance > 0:
            step_size = min(self.speed, distance) / distance
            self.x += dx * step_size
            self.y += dy * step_size
            self.z += dz * step_size

    def collect_internal_data(self):
        """
        Collect internal data, such as position and speed.
        """
        internal_data = {
            'id': self.id,
            'position': (self.x, self.y, self.z),
            'speed': self.speed
        }
        self.internal_data.append(internal_data)
        return internal_data

    def collect_external_data(self):
        """
        Collect external data, like camera or sensor data. Simulated here.
        """
        external_data = {
            'id': self.id,
            'camera_image': f"Simulated image data at ({self.x}, {self.y}, {self.z})"
        }
        self.external_data.append(external_data)
        return external_data

    def relay_data(self):
        """
        Simulate communication to the ground station by printing collected data.
        """
        internal_data = self.collect_internal_data()
        external_data = self.collect_external_data()
        print(f"[Drone {self.id} -> Ground] Internal Data: {internal_data}")
        print(f"[Drone {self.id} -> Ground] External Data: {external_data}")

    def run_operations(self, target_x, target_y, target_z=0, duration=10):
        """
        Simulate drone operations over a period, moving towards a target and relaying data.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            self.move_towards(target_x, target_y, target_z)
            self.relay_data()
            time.sleep(self.data_frequency)  # Simulate real-time data relay

if __name__ == "__main__":
    drone = Drone(drone_id=1)
    drone.run_operations(target_x=10, target_y=15, target_z=5, duration=5)





