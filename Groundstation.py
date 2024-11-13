# groundstation.py
from db_management import DatabaseManager


class GroundStation:
    def __init__(self):
        """
        Initializes GroundStation with a database manager.
        """
        self.db_manager = DatabaseManager(user="your_user", password="your_password")

    def receive_data(self, data):
        """
        Receives data from a drone, logs it, and stores it in the database.

        Parameters:
            data (dict): A dictionary containing data from a drone.
        """
        drone_id = data['id']
        position = data['position']
        speed = data['speed']

        print(f"[GroundStation] Received from Drone {drone_id} - Position: {position}, Speed: {speed}")

        self.db_manager.insert_data(drone_id, position, speed)

    def close(self):
        """
        Close the database manager connection.
        """
        self.db_manager.close()


# Usage Example:
if __name__ == "__main__":
    gs = GroundStation()

    # Simulate receiving data from a drone
    gs.receive_data({
        'id': 1,
        'position': (100, 200, 0),
        'speed': 3.5
    })
    gs.receive_data({
        'id': 2,
        'position': (150, 250, 0),
        'speed': 2.0
    })

    gs.close()
