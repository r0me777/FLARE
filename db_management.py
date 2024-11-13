import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host='localhost', user='your_user', password='your_password', database='testcase'):
        """
        Initialize the DatabaseManager with connection parameters.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()
        self.create_drone_data_table()  # Ensure table exists on initialization

    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_drone_data_table(self):
        """
        Create the drone_data table if it does not exist.
        """
        create_table_query = """
            CREATE TABLE IF NOT EXISTS drone_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                drone_id INT NOT NULL,
                position_x FLOAT NOT NULL,
                position_y FLOAT NOT NULL,
                position_z FLOAT NOT NULL,
                speed FLOAT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
            print("drone_data table is ready.")
        except Error as e:
            print(f"Error creating drone_data table: {e}")
        finally:
            cursor.close()

    def insert_data(self, drone_id, position, speed):
        """
        Insert drone data into the drone_data table.

        Parameters:
            drone_id (int): ID of the drone.
            position (tuple): (x, y, z) coordinates of the drone.
            speed (float): Speed of the drone.
        """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = """
                INSERT INTO drone_data (drone_id, position_x, position_y, position_z, speed)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (drone_id, position[0], position[1], position[2], speed))
                self.connection.commit()
                print(f"Data for Drone {drone_id} inserted into database.")
            except Error as e:
                print(f"Error inserting data: {e}")
            finally:
                cursor.close()

    def close(self):
        """
        Close the database connection.
        """
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Usage Example:
if __name__ == "__main__":
    db_manager = DatabaseManager(user="root", password="1626st0cks!")
    db_manager.insert_data(drone_id=1, position=(10.0, 20.0, 5.0), speed=3.5)
    db_manager.close()
