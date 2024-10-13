from ..Base.SensorBase import SensorBase
from .POSICalculator import POSICalculator

class POSI_Sensor(SensorBase):
    """
    A class to store POSI (Position) Sensor Data.

    This class inherits from SensorBase and provides functionality specific to POSI sensors.

    Attributes:
        timestamp (float): The timestamp of the sensor reading.
        counter (int): A counter value associated with the sensor reading.
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.
        floor_id (int): The ID of the floor where the sensor is located.
        building_id (int): The ID of the building where the sensor is located.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify the sensor type.

    Methods:
        export_row(index, include_calculated): Export POSI data as a row for a CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.
    """

    def __init__(self, timestamp, counter, latitude, longitude, floor_id, building_id):
        """
        Initialize a POSI_Sensor object.

        Args:
            timestamp (float): The timestamp of the sensor reading.
            counter (int): A counter value associated with the sensor reading.
            latitude (float): The latitude coordinate.
            longitude (float): The longitude coordinate.
            floor_id (int): The ID of the floor where the sensor is located.
            building_id (int): The ID of the building where the sensor is located.
        """
        super().__init__('POSI')
        self.timestamp = float(timestamp)
        self.counter = int(counter)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.floor_id = int(floor_id)
        self.building_id = int(building_id)
    
    def export_row(self, index, include_calculated=True):
        """
        Export POSI data as a row for a CSV file.

        Args:
            index (int): The index of the row in the CSV file.
            include_calculated (bool): Whether to include the calculated product in the output.

        Returns:
            str: A comma-separated string containing all the sensor data and optionally the calculated product.
        """
        base_data = f'{index},{self.timestamp},{self.counter},{self.latitude},{self.longitude},{self.floor_id},{self.building_id}'
        if include_calculated:
            calculator = POSICalculator()
            lat_long_product = calculator.calculate_lat_long_product(self.latitude, self.longitude)
            return f'{base_data},{lat_long_product}'
        return base_data
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for the calculated value.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,timestamp,counter,latitude,longitude,floor_id,building_id' + (',lat_long_product' if include_calculated else '')