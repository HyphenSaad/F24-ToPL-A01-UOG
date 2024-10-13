from ..Base.SensorBase import SensorBase
from .BLE4Calculator import BLE4Calculator

class BLE4Sensor(SensorBase):
    """
    A class to represent a BLE4 Sensor.

    This class inherits from SensorBase and is used to store and process
    BLE4 sensor data.

    Attributes:
        major_id (int): Major ID of the BLE4 device.
        minor_id (int): Minor ID of the BLE4 device.
        RSS (int): Received Signal Strength.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.

    Methods:
        export_row(index, include_calculated): Export BLE4 data as a row for CSV file.
    """

    def __init__(self, app_timestamp, major_id, minor_id, RSS):
        """
        Initialize the BLE4Sensor object.

        Args:
            app_timestamp (float): Application timestamp.
            major_id (int): Major ID of the BLE4 device.
            minor_id (int): Minor ID of the BLE4 device.
            RSS (int): Received Signal Strength.
        """
        super().__init__('BLE4', float(app_timestamp))
        self.major_id = int(major_id)
        self.minor_id = int(minor_id)
        self.RSS = int(RSS)

    def export_row(self, index, include_calculated=False):
        """
        Export BLE4 data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        # created base row with sensor data
        base_row = f'{index},{self.major_id},{self.minor_id},{self.RSS}'
        
        if include_calculated:
            # calculated signal strength using BLE4Calculator
            signal_strength = BLE4Calculator.calculate_signal_strength(self.RSS)
            return f'{base_row},{signal_strength}'
        
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include headers for calculated values.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,major_id,minor_id,RSS' + (',signal_strength' if include_calculated else '')