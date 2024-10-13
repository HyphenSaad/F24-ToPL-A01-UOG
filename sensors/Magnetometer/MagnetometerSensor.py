from ..Base.SensorBase import SensorBase
from .MagnetometerCalculator import MagnetometerCalculator

class MagnetometerSensor(SensorBase):
    """
    A class to store and process Magnetometer Sensor Data.

    This class inherits from SensorBase and provides functionality to store
    magnetometer sensor data.

    Attributes:
        mag_X (float): Magnetometer reading on X-axis.
        mag_Y (float): Magnetometer reading on Y-axis.
        mag_Z (float): Magnetometer reading on Z-axis.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.
    """

    def __init__(self, app_timestamp, sensor_timestamp, mag_X, mag_Y, mag_Z, accuracy):
        """
        Initialize the MagnetometerSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            mag_X (float): Magnetometer reading on X-axis.
            mag_Y (float): Magnetometer reading on Y-axis.
            mag_Z (float): Magnetometer reading on Z-axis.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('MAGN', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.mag_X = float(mag_X)
        self.mag_Y = float(mag_Y)
        self.mag_Z = float(mag_Z)

    def export_row(self, index, include_calculated=False):
        """
        Export magnetometer data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string containing the index and magnetometer data.
        """
        base_row = f'{index},{self.mag_X},{self.mag_Y},{self.mag_Z}'
        if include_calculated:
            calculator = MagnetometerCalculator()
            magnitude = calculator.calculate_magnitude(self.mag_X, self.mag_Y, self.mag_Z)
            heading = calculator.calculate_compass_heading(self.mag_X, self.mag_Y)
            return f'{base_row},{magnitude},{heading}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include headers for calculated values.

        Returns:
            str: A comma-separated string containing the headers.
        """
        return 'index,mag_x,mag_y,mag_z' + (',magnitude,heading' if include_calculated else '')