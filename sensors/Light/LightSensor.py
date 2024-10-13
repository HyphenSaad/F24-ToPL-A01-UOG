from ..Base.SensorBase import SensorBase
from .LightCalculator import LightCalculator

class LightSensor(SensorBase):
    """
    A class to represent a Light Sensor.

    This class inherits from SensorBase and is used to store and process
    light sensor data.

    Attributes:
        light (float): Light intensity value.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export light data as a row for CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, light, accuracy):
        """
        Initialize the LightSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            light (float): Light intensity value.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('LIGH', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.light = float(light)
    
    def export_row(self, index, include_calculated=False):
        """
        Export light data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.light}'
        if include_calculated:
            double_light = LightCalculator.calculate_double_light(self.light)
            day_night = LightCalculator.detect_day_night(self.light)
            return f'{base_row},{double_light},{day_night}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for CSV export.

        Args:
            include_calculated (bool): Whether to include calculated values in the headers.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,light' + (',double_of_light,day_night' if include_calculated else '')