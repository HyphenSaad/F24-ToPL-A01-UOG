from ..Base.SensorBase import SensorBase
from .TemperatureCalculator import TemperatureCalculator

class TemperatureSensor(SensorBase):
    """
    A class to store and process temperature sensor data.

    This class inherits from SensorBase and provides functionality
    to store temperature data.

    Attributes:
        temp (float): The temperature value in Celsius.

    Inherited Attributes:
        tag (str): Sensor tag or ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export temperature data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.

    Inherited Methods:
        Other methods inherited from SensorBase.
    """

    def __init__(self, app_timestamp, sensor_timestamp, temp, accuracy):
        """
        Initialize the TemperatureSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            temp (float): Temperature value in Celsius.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('TEMP', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.temp = float(temp)
    
    def export_row(self, index, include_calculated=True):
        """
        Export temperature data as a row for CSV file.

        Args:
            index (int): Row index.
            include_calculated (bool): Whether to include the calculated temperature in Fahrenheit.

        Returns:
            str: Comma-separated string containing index, temperature in Celsius, and optionally temperature in Fahrenheit.
        """
        base_row = f'{index},{self.temp}'
        if include_calculated:
            # calculated temperature in fahrenheit using TemperatureCalculator
            temp_in_fahrenheit = TemperatureCalculator.celsius_to_fahrenheit(self.temp)
            return f'{base_row},{temp_in_fahrenheit}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for calculated temperature in Fahrenheit.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,temp' + (',temp_in_fahrenheit' if include_calculated else '')