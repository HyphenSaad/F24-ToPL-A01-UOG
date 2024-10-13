from ..Base.SensorBase import SensorBase
from .HumidityCalculator import HumidityCalculator

class HumiditySensor(SensorBase):
    """
    A class to represent a Humidity Sensor.

    This class inherits from SensorBase and is used to store and process
    humidity sensor data.

    Attributes:
        humi (float): Humidity value.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export humidity data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, humi, accuracy):
        """
        Initialize the HumiditySensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            humi (float): Humidity value.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('HUMI', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.humi = float(humi)

    def export_row(self, index, include_calculated=False):
        """
        Export humidity data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.humi}'
        if include_calculated:
            humi_in_percent = HumidityCalculator.calculate_humidity_percentage(self.humi)
            return f'{base_row},{humi_in_percent}'
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
        return 'index,humi' + (',humi_in_percent' if include_calculated else '')